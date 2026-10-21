#!/usr/bin/env python3
"""prov_synth - synthetic view of the provenance of a ZOO-Project-DRU job.

Reads the CWLProv 0.6.0 research object (BagIt bag, .zip of it, or a bare
directory of ``*.cwlprov.ttl`` files) produced by cwltool ``--provenance`` and
completed by ZOO-Project-DRU with OGC API - Processes job information, builds
an intermediate model (job, agents, delegation chain, document tree, runs and
steps per level, inputs, outputs) and renders it as a readable diagram:

* ``--format svg`` (default): direct SVG, deterministic layered layout using
  the W3C PROV visual conventions (activities blue rectangles, entities yellow
  rounded boxes, agents orange house shapes), one grey band per provenance
  document;
* ``--format dot``: Graphviz DOT (one cluster per provenance document),
  rendered to SVG with the local ``dot`` binary when available.

Redaction is always on: values of roles/keys matching
``(?i)(secret|password|token|access_key|aws_access|credential)`` and endpoints
matching ``\\.svc\\.cluster\\.local`` are replaced with ``[redacted]`` in every
output (SVG, DOT, JSON, logs).

Only ``rdflib`` and ``pyyaml`` are required (plus the ``dot`` binary for
``--format dot``). Nothing is sent over the network.
"""
from __future__ import annotations

import argparse
import contextlib
import fnmatch
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import asdict, dataclass, field, fields, is_dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable
from xml.sax.saxutils import escape as xml_escape

try:
    import rdflib
    from rdflib import BNode, Graph, Literal, Namespace, URIRef
    from rdflib.namespace import RDF, RDFS
except ImportError:  # pragma: no cover
    sys.exit("prov_synth: rdflib is required (pip install --break-system-packages rdflib)")
try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # only needed for --profiles and YAML-encoded packed.cwl

__version__ = "0.1.0"

PROV = Namespace("http://www.w3.org/ns/prov#")
WFPROV = Namespace("http://purl.org/wf4ever/wfprov#")
WFDESC = Namespace("http://purl.org/wf4ever/wfdesc#")
WF4EVER = Namespace("http://purl.org/wf4ever/wf4ever#")
CWLPROV = Namespace("https://w3id.org/cwl/prov#")
RO = Namespace("http://purl.org/wf4ever/ro#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
SCHEMA = Namespace("http://schema.org/")
ZOO = Namespace("https://zoo-project.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")

# --------------------------------------------------------------------------
# Redaction
# --------------------------------------------------------------------------
SECRET_RE = re.compile(r"(?i)(secret|password|token|access_key|aws_access|credential)")
ENDPOINT_RE = re.compile(r"\.svc\.cluster\.local")
PLATFORM_RE = re.compile(r"^(STAGEIN_|STAGEOUT_)|^process$")
REDACTED = "[redacted]"


class Redactor:
    """Tracks secret values and redacts them wherever they would be emitted.

    A value is secret when it is bound to a role/key matching ``SECRET_RE``;
    once known, the same string is redacted everywhere (taint by value).
    Any string mentioning an in-cluster endpoint is redacted as a whole.
    """

    def __init__(self) -> None:
        self.tainted: set[str] = set()
        self.count = 0

    def taint(self, value: str) -> None:
        """Register a secret string (ignored when too short to be meaningful)."""
        v = value.strip()
        if len(v) >= 3:
            self.tainted.add(v)
            if v != value:
                self.tainted.add(value)

    def is_sensitive(self, s: str) -> bool:
        """True when ``s`` contains a known secret or an in-cluster endpoint."""
        return bool(ENDPOINT_RE.search(s)) or any(t in s for t in self.tainted)

    def value(self, v: str | None, key: str | None = None) -> str | None:
        """Return ``v`` or ``[redacted]`` (``key`` is the role/key it is bound to)."""
        if v is None:
            return None
        if key is not None and SECRET_RE.search(key):
            self.taint(v)
            self.count += 1
            return REDACTED
        if self.is_sensitive(v):
            self.count += 1
            return REDACTED
        return v

    def scrub(self, obj: Any) -> Any:
        """Recursively redact every string of a dataclass/list/dict tree in place."""
        if isinstance(obj, str):
            return REDACTED if self.is_sensitive(obj) else obj
        if is_dataclass(obj) and not isinstance(obj, type):
            for f in fields(obj):
                setattr(obj, f.name, self.scrub(getattr(obj, f.name)))
            return obj
        if isinstance(obj, list):
            return [self.scrub(x) for x in obj]
        if isinstance(obj, dict):
            return {k: self.scrub(v) for k, v in obj.items()}
        return obj


# --------------------------------------------------------------------------
# Model
# --------------------------------------------------------------------------
@dataclass
class AgentInfo:
    """A PROV agent shown in the agents row."""
    id: str
    label: str
    name: str
    version: str | None
    kind: str  # server | component | engine | account | software
    part_of: str | None = None


@dataclass
class Delegation:
    """prov:actedOnBehalfOf (delegate acted on behalf of responsible)."""
    delegate: str
    responsible: str
    activity: str | None = None


@dataclass
class Job:
    """The OGC API - Processes job as described by ZOO-Project-DRU."""
    id: str
    activity: str
    process_id: str | None = None
    process_iri: str | None = None
    process_specializes: str | None = None
    server: str | None = None
    location: str | None = None
    entity: str | None = None
    status_entity: str | None = None
    start: str | None = None
    end: str | None = None
    namespace: str | None = None
    status: str | None = None
    status_document: dict[str, Any] = field(default_factory=dict)


@dataclass
class ProvDocument:
    """One provenance document of the research object (after duplicate merge)."""
    name: str
    file: str
    api_path: str
    level: int
    activity: str | None
    parent_doc: str | None = None
    parent_step: str | None = None
    triples: int = 0
    merged_from: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


@dataclass
class Step:
    """A step of a run, grouped by base name (``node_crop``, ``node_crop_2`` ...)."""
    name: str
    instance_names: list[str]
    activity_ids: list[str]
    count: int
    plans: list[str]
    images: list[str]
    start: str | None
    end: str | None
    kind: str = "step"  # application | platform | step
    nested_doc: str | None = None
    shared_activity_starts: int = 1
    cwl_step: str | None = None
    cwl_run: str | None = None
    cwl_class: str | None = None
    cwl_label: str | None = None
    scatter: list[str] = field(default_factory=list)
    profile: str | None = None
    profile_short: str | None = None
    openeo: str | None = None
    profile_matched: bool = False


@dataclass
class Run:
    """A (sub-)workflow run described by one provenance document."""
    activity_id: str
    doc: str
    label: str | None
    plan: str | None
    cwl_process: str | None
    start: str | None
    end: str | None
    starts: int
    iterations: int = 1
    steps: list[Step] = field(default_factory=list)


@dataclass
class IOValue:
    """A workflow input or output (role -> value or collection members)."""
    name: str
    role: str
    kind: str  # literal | collection | dictionary | directory | file | unknown
    value: str | None
    members: list[str] = field(default_factory=list)
    platform: bool = False
    redacted: bool = False
    generated_by: list[str] = field(default_factory=list)
    entity: str | None = None
    lines: list[str] = field(default_factory=list)


@dataclass
class FlowEntity:
    """An intermediate data entity on the path from a producing step to a final output."""
    id: str
    kind: str  # directory | file | dictionary | collection | literal | unknown
    title: str
    summary: str
    members: list[str] = field(default_factory=list)
    produced_by: list[str] = field(default_factory=list)  # step keys "<doc>|<step>"
    used_by: list[str] = field(default_factory=list)
    returned_as: list[str] = field(default_factory=list)  # "<step>: <role>" run-level outputs
    lines: list[str] = field(default_factory=list)


@dataclass
class FlowLink:
    """One PROV relation of an output data flow (entities joined across documents by IRI)."""
    relation: str  # wasGeneratedBy | used
    entity: str
    step: str  # "<doc>|<step>" or "run" for the wrapping workflow run
    role: str
    doc: str
    level: str  # step: recorded on the step activity; run: output of the (sub-)workflow run itself


@dataclass
class DataEdge:
    """Step-to-step data or parameter passing (repeated/scattered instances collapsed)."""
    kind: str  # data: generated by source, used by target | param: input of the parent run passed to a step
    source: str  # step key "<doc>|<step>" or "run" (wrapping workflow run)
    target: str
    source_port: str  # data: output role of the source; param: input role of the parent run
    target_port: str  # input role of the target
    entity_kind: str  # file | folder | literal | collection | dictionary | unknown
    count: int  # distinct entities (data) or usages (param) behind the edge
    names: list[str] = field(default_factory=list)  # basenames of files/folders
    via: str = "direct"  # direct | member (entity reached through hadMember / hadDictionaryMember)
    through: list[str] = field(default_factory=list)  # sub-workflow outputs the data also left by
    drawn_as_entity: bool = False  # already drawn through an output-flow entity box
    platform: bool = False
    note: str | None = None


@dataclass
class OutputFlow:
    """Data flow behind one final output, traced back across levels."""
    output: str
    entity: str
    entities: list[FlowEntity] = field(default_factory=list)
    links: list[FlowLink] = field(default_factory=list)


@dataclass
class ProfileCard:
    """A process profile matched by the --profiles mapping."""
    short: str
    profile: str | None
    openeo: str | None
    kind: str | None
    steps: list[str] = field(default_factory=list)
    note: str | None = None


@dataclass
class Model:
    """Everything the renderers need; serialisable with ``--json``."""
    tool: str
    source: str
    research_object: str | None
    job: Job | None
    agents: list[AgentInfo]
    delegations: list[Delegation]
    documents: list[ProvDocument]
    runs: list[Run]
    inputs: list[IOValue]
    outputs: list[IOValue]
    platform_params_hidden: int
    redactions: int
    flows: list[OutputFlow] = field(default_factory=list)
    dataflow: list[DataEdge] = field(default_factory=list)
    profiles: list[ProfileCard] = field(default_factory=list)
    profiles_title: str | None = None
    profiles_subtitle: str | None = None
    notes: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------
# Input location
# --------------------------------------------------------------------------
RDF_EXT = (".ttl", ".nt", ".jsonld")
ALL_EXT = (".ttl", ".nt", ".jsonld", ".json", ".xml", ".provn")


@dataclass
class Source:
    """Resolved input: provenance directory and optional bag root."""
    prov_dir: Path
    bag_root: Path | None
    primary: Path
    tmp: tempfile.TemporaryDirectory | None = None


def _safe_extract(zf: zipfile.ZipFile, dest: Path) -> None:
    """Extract a zip refusing absolute paths and path traversal."""
    root = dest.resolve()
    for m in zf.infolist():
        target = (dest / m.filename).resolve()
        if not str(target).startswith(str(root)):
            raise ValueError(f"unsafe path in zip: {m.filename!r}")
    zf.extractall(dest)


def locate(path: Path) -> Source:
    """Find the primary provenance document in a bag, a zip or a bare directory."""
    tmp = None
    if path.is_file() and zipfile.is_zipfile(path):
        tmp = tempfile.TemporaryDirectory(prefix="prov_synth_")
        with zipfile.ZipFile(path) as zf:
            _safe_extract(zf, Path(tmp.name))
        path = Path(tmp.name)
    if not path.is_dir():
        raise SystemExit(f"prov_synth: {path} is neither a directory nor a zip file")
    cands = sorted(path.rglob("primary.cwlprov.ttl"), key=lambda p: (len(p.parts), str(p)))
    if not cands:
        cands = sorted(path.rglob("primary.cwlprov.nt"), key=lambda p: (len(p.parts), str(p)))
    if cands:
        primary = cands[0]
    else:
        ttl = sorted(path.rglob("*.cwlprov.ttl"))
        if not ttl:
            raise SystemExit(f"prov_synth: no *.cwlprov.ttl found under {path}")
        # pick the document no other document points to
        targets: set[str] = set()
        for f in ttl:
            g = Graph().parse(f, format="turtle")
            for o in g.objects(None, PROV.has_provenance):
                targets.add(_doc_stem(str(o)))
        roots = [f for f in ttl if _doc_stem(f.name) not in targets] or ttl
        primary = roots[0]
    prov_dir = primary.parent
    bag_root = None
    if prov_dir.name == "provenance" and prov_dir.parent.name == "metadata":
        bag_root = prov_dir.parent.parent
    return Source(prov_dir=prov_dir, bag_root=bag_root, primary=primary, tmp=tmp)


def _doc_stem(iri_or_name: str) -> str:
    """``arcp://…/metadata/provenance/x.cwlprov.ttl`` -> ``x.cwlprov``."""
    name = iri_or_name.rstrip("/").rsplit("/", 1)[-1]
    for ext in ALL_EXT:
        if name.endswith(ext):
            return name[: -len(ext)]
    return name


def _parse(path: Path) -> Graph:
    fmt = {".ttl": "turtle", ".nt": "nt", ".jsonld": "json-ld"}[path.suffix]
    return Graph().parse(path, format=fmt)


def _find_doc_file(prov_dir: Path, stem: str) -> Path | None:
    for ext in RDF_EXT:
        p = prov_dir / f"{stem}{ext}"
        if p.exists():
            return p
    return None


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------
def short_id(iri: str | None) -> str:
    """``urn:uuid:2378e838-…`` -> ``2378e838-c7d3-…``."""
    if not iri:
        return ""
    s = str(iri)
    for p in ("urn:uuid:", "urn:hash::sha1:"):
        if s.startswith(p):
            s = s[len(p):]
    return s


def ellipsize_id(s: str, keep: int = 8) -> str:
    """``2378e838-c7d3-11f1-…`` -> ``2378e838-…``."""
    return s if len(s) <= keep + 2 else s[:keep] + "-…"


def ellipsize(s: str, n: int) -> str:
    """Cut ``s`` to ``n`` characters with an ellipsis."""
    return s if len(s) <= n else s[: max(1, n - 1)] + "…"


def shorten_value(v: str, n: int = 46) -> str:
    """Shorten long literals, keeping the scheme/host and the last path segment of URLs."""
    v = v.strip()
    m = re.match(r"^([a-z0-9+.-]+://[^/]+)(/.*)?/([^/]+)/?$", v)
    if m and len(v) > n:
        cand = f"{m.group(1)}/…/{m.group(3)}"
        if len(cand) <= n:
            return cand
        return "…/" + ellipsize(m.group(3), n - 2)
    return ellipsize(v, n)


def last_segment(v: str) -> str:
    """Last path segment of a URL-like value (used for collection members)."""
    v = v.strip().rstrip("/")
    return v.rsplit("/", 1)[-1] if "://" in v else v


def lit(g: Graph, s: Any, p: Any) -> str | None:
    """First literal value of ``s p ?o`` as a string."""
    o = g.value(s, p)
    return None if o is None else str(o)


def label_of(g: Graph, s: Any) -> str | None:
    """rdfs:label or prov:label."""
    return lit(g, s, RDFS.label) or lit(g, s, PROV.label)


def hhmmss(t: str | None) -> str:
    """ISO timestamp -> ``HH:MM:SS``."""
    if not t:
        return ""
    try:
        return datetime.fromisoformat(t).strftime("%H:%M:%S")
    except ValueError:
        return t[11:19]


def duration(a: str | None, b: str | None) -> str:
    """Human duration between two ISO timestamps (timezone-naive times are taken as UTC)."""
    if not a or not b:
        return ""
    try:
        da, db = datetime.fromisoformat(a), datetime.fromisoformat(b)
        if (da.tzinfo is None) != (db.tzinfo is None):
            da, db = da.replace(tzinfo=None), db.replace(tzinfo=None)
        s = int(round((db - da).total_seconds()))
    except ValueError:
        return ""
    if s < 0:
        return ""
    if s < 60:
        return f"{s}s"
    if s < 3600:
        return f"{s // 60}m{s % 60:02d}s"
    return f"{s // 3600}h{(s % 3600) // 60:02d}m"


def local_name(role: str) -> str:
    """``…/packed.cwl#main/node_crop/item`` -> ``item``."""
    r = str(role).split("#", 1)[-1]
    return r.rsplit("/", 1)[-1]


def step_name_from(label: str | None, plan: str | None) -> str:
    """Step name from ``Run of workflow/packed.cwl#main/node_crop_2`` or the plan IRI."""
    for s in (label, plan):
        if s and "#" in s:
            return s.split("#", 1)[1].rstrip("/").rsplit("/", 1)[-1]
    return short_id(label or plan or "?")


def _times(g: Graph, act: Any, pred: Any, by: Any = None) -> list[str]:
    """Distinct atTime values of qualifiedStart/End (optionally filtered by hadActivity)."""
    out: set[str] = set()
    for q in g.objects(act, pred):
        if by is not None and g.value(q, PROV.hadActivity) not in (by, None):
            continue
        t = g.value(q, PROV.atTime)
        if t is not None:
            out.add(str(t))
    return sorted(out)


# --------------------------------------------------------------------------
# Extraction
# --------------------------------------------------------------------------
class Extractor:
    """Builds a :class:`Model` from the provenance documents of one research object."""

    def __init__(self, src: Source, show_platform: bool = False) -> None:
        self.src = src
        self.show_platform = show_platform
        self.red = Redactor()
        self.graphs: dict[str, Graph] = {}
        self.docs: list[ProvDocument] = []
        self.notes: list[str] = []
        self.cwl: dict[str, dict] = {}
        self._load_cwl()

    # -- packed.cwl -------------------------------------------------------
    def _load_cwl(self) -> None:
        root = self.src.bag_root
        if not root:
            return
        p = root / "workflow" / "packed.cwl"
        if not p.exists():
            return
        try:
            txt = p.read_text()
            d = json.loads(txt) if txt.lstrip().startswith("{") else (yaml.safe_load(txt) if yaml else None)
        except Exception as exc:  # noqa: BLE001
            self.notes.append(f"packed.cwl could not be read ({type(exc).__name__})")
            return
        if not isinstance(d, dict):
            return
        for proc in d.get("$graph", [d]):
            if isinstance(proc, dict) and "id" in proc:
                self.cwl[str(proc["id"]).lstrip("#")] = proc

    def _cwl_step(self, process: str | None, name: str) -> tuple[str | None, str | None, dict | None, list[str]]:
        """Find step ``name`` in CWL process ``process`` -> (step id, run id, run object, scatter)."""
        procs = [self.cwl[process]] if process and process in self.cwl else []
        procs += [p for k, p in self.cwl.items() if k != process]
        for proc in procs:
            for st in proc.get("steps", []) or []:
                sid = str(st.get("id", ""))
                if sid.lstrip("#").rsplit("/", 1)[-1] == name:
                    run = st.get("run")
                    if isinstance(run, str):
                        rid = run.lstrip("#")
                        robj = self.cwl.get(rid)
                    else:
                        robj = run if isinstance(run, dict) else None
                        rid = str(robj.get("id", "")).lstrip("#") if robj else None
                    sc = st.get("scatter") or []
                    sc = [sc] if isinstance(sc, str) else list(sc)
                    return sid.lstrip("#"), rid, robj, [local_name(x) for x in sc]
        return None, None, None, []

    @staticmethod
    def _docker(robj: dict | None) -> str | None:
        if not robj:
            return None
        for r in (robj.get("requirements") or []) + (robj.get("hints") or []):
            if isinstance(r, dict) and r.get("class") == "DockerRequirement":
                return r.get("dockerPull") or r.get("dockerImageId")
        return None

    # -- documents --------------------------------------------------------
    def _load_documents(self) -> None:
        """Load primary + nested documents (following prov:has_provenance), merging duplicates."""
        prim = self.src.primary
        g = _parse(prim)
        stem = _doc_stem(prim.name)
        self.graphs[stem] = g
        self.docs.append(ProvDocument(name=stem, file=prim.name, api_path="/jobs/{jobId}/prov",
                                      level=0, activity=None, triples=len(g)))
        queue = [stem]
        seen = {stem}
        while queue:
            cur = queue.pop(0)
            cg = self.graphs[cur]
            parent = next(d for d in self.docs if d.name == cur)
            by_act: dict[Any, list[str]] = {}
            for act, target in cg.subject_objects(PROV.has_provenance):
                st = _doc_stem(str(target))
                by_act.setdefault(act, [])
                if st not in by_act[act]:
                    by_act[act].append(st)
            for act in sorted(by_act, key=str):
                stems = [s for s in sorted(by_act[act]) if s not in seen]
                loaded: list[tuple[str, Path, Graph]] = []
                for s in stems:
                    seen.add(s)
                    f = _find_doc_file(self.src.prov_dir, s)
                    if f is None:
                        self.notes.append(f"nested document {s} is referenced but not present in the bag")
                        continue
                    loaded.append((s, f, _parse(f)))
                if not loaded:
                    continue
                # canonical = most complete (most triples), then shortest name
                loaded.sort(key=lambda t: (-len(t[2]), len(t[0]), t[0]))
                cname, cfile, cgraph = loaded[0]
                merged = Graph()
                for _, _, gg in loaded:
                    merged += gg
                doc = ProvDocument(name=cname, file=cfile.name,
                                   api_path="/jobs/{jobId}/prov/{provDocument}",
                                   level=parent.level + 1, activity=str(act),
                                   parent_doc=cur, triples=len(cgraph))
                for oname, _, og in loaded[1:]:
                    extra = _ground(og) - _ground(cgraph)
                    rel = ("strict subset" if not extra else f"{len(extra)} statement(s) not in the canonical copy")
                    doc.merged_from.append(oname)
                    msg = (f"{oname} ({len(og)} triples) describes the same activity {short_id(str(act))} as "
                           f"{cname} ({len(cgraph)} triples): {rel}; merged by union, {cname} kept as canonical")
                    doc.notes.append(msg)
                    self.notes.append(msg)
                self.graphs[cname] = merged
                self.docs.append(doc)
                queue.append(cname)

    # -- redaction pre-pass ----------------------------------------------
    def _taint_pass(self) -> None:
        """Register every value bound to a secret-looking role or key before anything is emitted."""
        for g in self.graphs.values():
            for q in list(g.subjects(PROV.hadRole, None)):
                role = str(g.value(q, PROV.hadRole))
                if SECRET_RE.search(local_name(role)):
                    ent = g.value(q, PROV.entity)
                    for v in self._all_values(g, ent):
                        self.red.taint(v)
        root = self.src.bag_root
        if root:
            for rel in ("workflow/primary-job.json", "workflow/primary-output.json", "metadata/zoo/job-status.json"):
                p = root / rel
                if p.exists():
                    try:
                        _taint_json(json.loads(p.read_text()), self.red)
                    except (ValueError, OSError):
                        pass

    @staticmethod
    def _all_values(g: Graph, ent: Any, depth: int = 0) -> list[str]:
        if ent is None or depth > 4:
            return []
        out = [str(o) for o in g.objects(ent, PROV.value)]
        for m in g.objects(ent, PROV.hadMember):
            out += Extractor._all_values(g, m, depth + 1)
        return out

    # -- entities ---------------------------------------------------------
    def describe(self, g: Graph, ent: Any, key: str) -> IOValue:
        """Describe an entity used/generated with role ``key`` (redacted)."""
        types = set(g.objects(ent, RDF.type))
        name = key
        secret = bool(SECRET_RE.search(key))
        v = lit(g, ent, PROV.value)
        if RO.Folder in types:
            members = sorted(str(g.value(p, PROV.pairKey)) for p in g.objects(ent, PROV.hadDictionaryMember)
                             if g.value(p, PROV.pairKey) is not None)
            return IOValue(name, key, "directory", lit(g, ent, CWLPROV.basename) or "directory",
                           [self.red.value(m, key) for m in members], redacted=secret)
        if PROV.Dictionary in types:
            pairs = {}
            for p in g.objects(ent, PROV.hadDictionaryMember):
                k = str(g.value(p, PROV.pairKey))
                e = g.value(p, PROV.pairEntity)
                pv = lit(g, e, PROV.value) if e is not None else None
                if pv is None and e is not None:
                    pv = lit(g, e, CWLPROV.basename) or short_id(str(e))
                pairs[k] = self.red.value(pv, key if secret else k)
            val = pairs.pop("value", None)
            members = [f"{k}: {pairs[k]}" for k in sorted(pairs)]
            return IOValue(name, key, "dictionary", val, members, redacted=secret)
        if PROV.Collection in types:
            vals = []
            for m in g.objects(ent, PROV.hadMember):
                mv = lit(g, m, PROV.value) or lit(g, m, CWLPROV.basename) or short_id(str(m))
                vals.append(self.red.value(mv, key))
            return IOValue(name, key, "collection", None, sorted(vals), redacted=secret)
        if WF4EVER.File in types:
            return IOValue(name, key, "file", lit(g, ent, CWLPROV.basename) or short_id(str(ent)), redacted=secret)
        if v is not None:
            return IOValue(name, key, "literal", self.red.value(v, key), redacted=secret or self.red.is_sensitive(v))
        return IOValue(name, key, "unknown", short_id(str(ent)))

    # -- agents & job -----------------------------------------------------
    def _agents(self, g: Graph) -> tuple[list[AgentInfo], list[Delegation]]:
        agents: list[AgentInfo] = []
        for a in sorted(set(g.subjects(RDF.type, PROV.Agent)) | set(g.subjects(RDF.type, PROV.SoftwareAgent)), key=str):
            if g.value(a, CWLPROV.image) is not None:
                continue  # container agents are shown on their step
            label = label_of(g, a) or short_id(str(a))
            name = lit(g, a, SCHEMA.name)
            version = lit(g, a, SCHEMA.softwareVersion)
            if not name:
                m = re.match(r"^(.*?)\s+v?(\d[\w.+-]*)$", label)
                name, version = (m.group(1), version or m.group(2)) if m else (label, version)
            types = set(g.objects(a, RDF.type))
            if FOAF.OnlineAccount in types:
                kind, name = "account", lit(g, a, FOAF.accountName) or label
            elif WFPROV.WorkflowEngine in types:
                kind = "engine"
            elif g.value(a, SCHEMA.isPartOf) is not None:
                kind = "component"
            elif SCHEMA.SoftwareApplication in types:
                kind = "server"
            else:
                kind = "software"
            agents.append(AgentInfo(id=short_id(str(a)), label=label, name=name, version=version, kind=kind,
                                    part_of=short_id(str(g.value(a, SCHEMA.isPartOf))) if g.value(a, SCHEMA.isPartOf) else None))
        dels: list[Delegation] = []
        for d, r in g.subject_objects(PROV.actedOnBehalfOf):
            act = None
            for q in g.objects(d, PROV.qualifiedDelegation):
                if g.value(q, PROV.hadActivity) is not None:
                    act = short_id(str(g.value(q, PROV.hadActivity)))
            dels.append(Delegation(short_id(str(d)), short_id(str(r)), act))
        dels.sort(key=lambda x: (x.responsible, x.delegate))
        ids = {a.id for a in agents}
        # lint: agents used as subjects of qualifiedStart (wasStartedBy is for activities)
        for a in agents:
            if any(True for _ in g.objects(URIRef("urn:uuid:" + a.id), PROV.qualifiedStart)):
                self.notes.append(f"agent '{a.label}' is the subject of prov:qualifiedStart (wasStartedBy); "
                                  "PROV-DM defines starts for activities only")
        return [a for a in agents if a.id in ids], dels

    def _job(self, g: Graph) -> Job | None:
        cands = [a for a in g.subjects(RDF.type, PROV.Activity)
                 if g.value(a, ZOO.namespace) is not None
                 or (label_of(g, a) or "").startswith("OGC API - Processes job")]
        if not cands:
            return None
        a = sorted(cands, key=str)[0]
        job = Job(id=short_id(str(a)), activity=str(a))
        job.location = lit(g, a, PROV.atLocation)
        job.start = lit(g, a, PROV.startedAtTime)
        job.end = lit(g, a, PROV.endedAtTime)
        job.namespace = lit(g, a, ZOO.namespace)
        st = g.value(a, SCHEMA.actionStatus)
        job.status = str(st).rsplit("/", 1)[-1].replace("ActionStatus", "").lower() if st is not None else None
        for q in g.objects(a, PROV.qualifiedAssociation):
            plan = g.value(q, PROV.hadPlan)
            if plan is not None:
                job.process_iri = str(plan)
                job.process_id = lit(g, plan, DCT.identifier) or str(plan).rstrip("/").rsplit("/", 1)[-1]
                sp = g.value(plan, PROV.specializationOf)
                job.process_specializes = str(sp) if sp is not None else None
        for e in g.subjects(PROV.wasGeneratedBy, a):
            if (e, RDF.type, WFDESC.ProcessRun) in g or str(e).endswith("/jobs/" + job.id):
                job.entity = str(e)
            elif str(e).endswith("job-status.json"):
                job.status_entity = str(e)
        for e in g.subjects(RDF.type, WFDESC.ProcessRun):
            job.entity = job.entity or str(e)
            self.notes.append(f"{e} is typed wfdesc:ProcessRun, a class wfdesc does not define "
                              "(wfprov:ProcessRun is the run class; wfdesc describes plans)")
        for ag in g.objects(a, PROV.wasAssociatedWith):
            loc = lit(g, ag, PROV.atLocation)
            if loc:
                job.server = loc
        if not job.server and job.location:
            job.server = job.location.split("/jobs/")[0]
        root = self.src.bag_root
        if root and (root / "metadata/zoo/job-status.json").exists():
            try:
                sd = json.loads((root / "metadata/zoo/job-status.json").read_text())
                job.status_document = {k: sd.get(k) for k in ("processID", "status", "created", "started",
                                                              "finished", "updated", "progress", "message") if k in sd}
                job.process_id = job.process_id or sd.get("processID")
            except (ValueError, OSError):
                pass
        return job

    # -- runs -------------------------------------------------------------
    def _main_run(self, g: Graph, job: Job | None) -> Any:
        runs = sorted(g.subjects(RDF.type, WFPROV.WorkflowRun), key=str)
        if job:
            informed = [r for r in g.subjects(PROV.wasInformedBy, URIRef(job.activity)) if r in runs]
            if informed:
                return informed[0]
        for r in runs:
            starters = [g.value(q, PROV.hadActivity) for q in g.objects(r, PROV.qualifiedStart)]
            if not any(s in runs for s in starters if s is not None):
                return r
        return runs[0] if runs else None

    def _run(self, docname: str, act: Any, cwl_process: str | None, top: bool) -> Run:
        g = self.graphs[docname]
        plan = None
        for q in g.objects(act, PROV.qualifiedAssociation):
            p = g.value(q, PROV.hadPlan)
            if p is not None and "packed.cwl#" in str(p):
                plan = str(p)
        starts = _times(g, act, PROV.qualifiedStart)
        ends = _times(g, act, PROV.qualifiedEnd)
        run = Run(activity_id=short_id(str(act)), doc=docname, label=label_of(g, act), plan=plan,
                  cwl_process=cwl_process, start=lit(g, act, PROV.startedAtTime) or (starts[0] if starts else None),
                  end=lit(g, act, PROV.endedAtTime) or (ends[-1] if ends else None), starts=max(1, len(starts)))
        children: list[Any] = []
        for s in set(g.subjects(RDF.type, PROV.Activity)) | set(g.subjects(RDF.type, WFPROV.ProcessRun)):
            if s == act:
                continue
            if any(g.value(q, PROV.hadActivity) == act for q in g.objects(s, PROV.qualifiedStart)) \
                    or (s, PROV.wasStartedBy, act) in g:
                children.append(s)
        info = []
        for c in children:
            cplan = None
            for q in g.objects(c, PROV.qualifiedAssociation):
                p = g.value(q, PROV.hadPlan)
                if p is not None:
                    cplan = str(p)
            nm = step_name_from(label_of(g, c), cplan)
            st = _times(g, c, PROV.qualifiedStart, by=act)
            en = _times(g, c, PROV.qualifiedEnd, by=act)
            imgs = sorted({str(g.value(a, CWLPROV.image)) for a in g.objects(c, PROV.wasAssociatedWith)
                           if g.value(a, CWLPROV.image) is not None})
            nested = sorted({_doc_stem(str(o)) for o in g.objects(c, PROV.has_provenance)})
            info.append((c, nm, cplan, st, en, imgs, nested))
        names = {i[1] for i in info}

        def base(n: str) -> str:
            m = re.match(r"^(.+)_(\d+)$", n)
            return m.group(1) if m and int(m.group(2)) >= 2 and m.group(1) in names else n

        groups: dict[str, list] = {}
        for i in info:
            groups.setdefault(base(i[1]), []).append(i)
        steps = []
        undeclared: list[str] = []
        for b, items in groups.items():
            items.sort(key=lambda i: (i[3][0] if i[3] else "", i[1]))
            all_st = sorted(t for i in items for t in i[3])
            all_en = sorted(t for i in items for t in i[4])
            count = sum(max(1, len(i[3])) for i in items)
            shared = max(max(1, len(i[3])) for i in items)
            nested_docs = [d.name for d in self.docs if d.activity in {str(i[0]) for i in items}]
            step = Step(name=b, instance_names=[i[1] for i in items], activity_ids=[short_id(str(i[0])) for i in items],
                        count=count, plans=sorted({i[2] for i in items if i[2]}),
                        images=sorted({im for i in items for im in i[5]}),
                        start=all_st[0] if all_st else None, end=all_en[-1] if all_en else None,
                        nested_doc=nested_docs[0] if nested_docs else None, shared_activity_starts=shared)
            sid, rid, robj, scatter = self._cwl_step(cwl_process, b)
            step.cwl_step, step.cwl_run, step.scatter = sid, rid, scatter
            if robj:
                step.cwl_class = robj.get("class")
                step.cwl_label = robj.get("label")
                if not step.images and self._docker(robj):
                    step.images = [self._docker(robj)]
            if top and re.match(r"^stage_(in|out)(_\d+)?$", b):
                step.kind = "platform"
            elif top and step.nested_doc:
                step.kind = "application"
            # lint: plan IRIs that are not declared sub-processes of the run's plan
            if plan:
                subs = {str(o) for o in g.objects(URIRef(plan), WFDESC.hasSubProcess)}
                undeclared += [p.split('#', 1)[-1] for p in step.plans if subs and p not in subs]
            steps.append(step)
        if undeclared:
            self.notes.append(f"{ellipsize_doc(docname)}: step plan(s) {', '.join(sorted(undeclared))} not declared as "
                              f"wfdesc:hasSubProcess of {str(plan).split('#', 1)[-1]} (plan IRIs of step runs and "
                              "prospective sub-processes differ)")
        steps.sort(key=lambda s: (s.start or "~", s.name))
        run.steps = steps
        return run

    # -- output data flow -------------------------------------------------
    def _flow_index(self) -> None:
        """Index generations and usages of every document (entities joined by IRI)."""
        self._gens: dict[str, list[tuple[str, str, str]]] = {}
        self._uses: dict[str, list[tuple[str, str, str]]] = {}
        for doc, g in self.graphs.items():
            for e, q in g.subject_objects(PROV.qualifiedGeneration):
                a, r = g.value(q, PROV.activity), g.value(q, PROV.hadRole)
                if a is not None:
                    t = (str(a), str(r) if r is not None else "", doc)
                    if t not in self._gens.setdefault(str(e), []):
                        self._gens[str(e)].append(t)
            for a, q in g.subject_objects(PROV.qualifiedUsage):
                e, r = g.value(q, PROV.entity), g.value(q, PROV.hadRole)
                if e is not None:
                    t = (str(e), str(r) if r is not None else "", doc)
                    if t not in self._uses.setdefault(str(a), []):
                        self._uses[str(a)].append(t)

    def _entity_graph(self, e: str) -> Graph:
        """The graph that describes entity ``e`` most completely."""
        best, n = self.graphs[self.docs[0].name], -1
        for g in self.graphs.values():
            k = sum(1 for _ in g.predicate_objects(URIRef(e)))
            if k > n:
                best, n = g, k
        return best

    def _folder_summary(self, g: Graph, e: Any) -> tuple[str, list[str]]:
        """``catalog.json + 2 sub-folders`` from the dictionary members of a folder."""
        files, folders = [], []
        for p in g.objects(e, PROV.hadDictionaryMember):
            k, pe = g.value(p, PROV.pairKey), g.value(p, PROV.pairEntity)
            if k is None:
                continue
            (folders if pe is not None and (pe, RDF.type, RO.Folder) in g else files).append(str(k))
        files.sort()
        folders.sort()
        lead = [f for f in files if f == "catalog.json"][:1] or files[:1]
        parts = lead + ([f"{len(files) - 1} file{'s' if len(files) > 2 else ''}"] if len(files) > 1 else [])
        if folders:
            parts.append(f"{len(folders)} sub-folder{'s' if len(folders) > 1 else ''}")
        return " + ".join(parts) or "empty", files + [f + "/" for f in folders]

    def _trace(self, out: IOValue, main: Any, top: Run, step_by_act: dict[str, tuple[Step, Run]],
               max_depth: int = 4) -> OutputFlow:
        """Trace a final output back through the steps that generated/used its data, at any level."""
        if not hasattr(self, "_gens"):
            self._flow_index()
        run_docs = {d.activity: d.name for d in self.docs if d.activity}
        flow = OutputFlow(output=out.name, entity=out.entity or "")
        oiri = next((k for k in self._gens if short_id(k) == out.entity), None)
        if oiri is None:
            return flow

        def key_of(act: str) -> tuple[str | None, Step | None]:
            if act == str(main):
                return "run", None
            hit = step_by_act.get(short_id(act))
            return (f"{hit[1].doc}|{hit[0].name}", hit[0]) if hit else (None, None)

        def level(act: str, doc: str) -> str:
            # a generation recorded in the document whose run *is* this activity = output of that run
            return "run" if act == str(main) or run_docs.get(act) == doc else "step"

        def add_gens(eiri: str) -> list[str]:
            producers = []
            for act, role, doc in self._gens.get(eiri, []):
                k, _ = key_of(act)
                if k is None:
                    continue
                lv = level(act, doc)
                flow.links.append(FlowLink("wasGeneratedBy", short_id(eiri), k, role.split("#", 1)[-1], doc, lv))
                if lv == "step":
                    producers.append(act)
            return producers

        frontier = [(a, 0) for a in add_gens(oiri)]
        seen: set[str] = set()
        while frontier:
            act, depth = frontier.pop(0)
            if act in seen or depth >= max_depth:
                continue
            seen.add(act)
            k, _ = key_of(act)
            for eiri, role, doc in self._uses.get(act, []):
                nm = local_name(role)
                if SECRET_RE.search(nm) or eiri == oiri:
                    continue
                prods = [a for a, _, d in self._gens.get(eiri, []) if a != act and key_of(a)[0] and level(a, d) == "step"]
                if not prods:
                    continue  # job input or data not produced by a step: not part of the output flow
                if any(x.id == short_id(eiri) for x in flow.entities):
                    flow.links.append(FlowLink("used", short_id(eiri), str(k), role.split("#", 1)[-1], doc, "step"))
                    continue
                g = self._entity_graph(eiri)
                ent = URIRef(eiri)
                iv = self.describe(g, ent, nm)
                fe = FlowEntity(id=short_id(eiri), kind=iv.kind, title=nm, summary="", members=iv.members)
                if iv.kind == "directory":
                    fe.summary, fe.members = self._folder_summary(g, ent)
                elif iv.kind == "collection":
                    fe.summary = f"{len(iv.members)} items"
                else:
                    fe.summary = shorten_value(iv.value or "", 40)
                flow.entities.append(fe)
                flow.links.append(FlowLink("used", fe.id, str(k), role.split("#", 1)[-1], doc, "step"))
                frontier += [(a, depth + 1) for a in add_gens(eiri)]
        # per-entity summaries of the links
        for fe in flow.entities:
            for ln in flow.links:
                if ln.entity != fe.id:
                    continue
                if ln.relation == "used" and ln.step not in fe.used_by:
                    fe.used_by.append(ln.step)
                elif ln.relation == "wasGeneratedBy" and ln.level == "step" and ln.step not in fe.produced_by:
                    fe.produced_by.append(ln.step)
                elif ln.relation == "wasGeneratedBy" and ln.level == "run":
                    fe.returned_as.append(f"{ln.step.split('|')[-1]}: {local_name(ln.role)}")
        return flow

    # -- step-to-step data flow ------------------------------------------
    def _all(self) -> Graph:
        """Union of all documents (entities are joined by IRI)."""
        if not hasattr(self, "_union"):
            self._union = Graph()
            for g in self.graphs.values():
                self._union += g
        return self._union

    def _atoms(self, iri: str, depth: int = 0) -> list[tuple[str, str]]:
        """``iri`` plus its collection/dictionary members (recursively) as (iri, via)."""
        g = self._all()
        out = [(iri, "direct" if depth == 0 else "member")]
        if depth >= 3:
            return out
        s = URIRef(iri)
        mem = {str(m) for m in g.objects(s, PROV.hadMember)}
        for p in g.objects(s, PROV.hadDictionaryMember):
            pe = g.value(p, PROV.pairEntity)
            if pe is not None:
                mem.add(str(pe))
        for m in sorted(mem):
            out += [(a, "member") for a, _ in self._atoms(m, depth + 1)]
        return out

    def _ckey(self, iri: str) -> Any:
        """Content key: content-addressed data for files, member set for collections, IRI otherwise."""
        g = self._all()
        s = URIRef(iri)
        sp = g.value(s, PROV.specializationOf)
        if sp is not None and str(sp).startswith("urn:hash:"):
            return str(sp)
        mem = sorted(str(m) for m in g.objects(s, PROV.hadMember))
        if mem and (s, RDF.type, PROV.Collection) in g and (s, RDF.type, RO.Folder) not in g:
            return ("coll",) + tuple(sorted(str(self._ckey(m)) for m in mem))
        return iri

    def _kind(self, iri: str) -> tuple[str, str | None]:
        """(entity kind, basename) of an entity."""
        g = self._all()
        s = URIRef(iri)
        types = set(g.objects(s, RDF.type))
        bn = lit(g, s, CWLPROV.basename)
        if RO.Folder in types:
            return "folder", bn
        if WF4EVER.File in types:
            return "file", bn
        if PROV.Dictionary in types:
            return "dictionary", None
        if PROV.Collection in types:
            return "collection", None
        if g.value(s, PROV.value) is not None or iri.startswith("urn:hash:"):
            return "literal", None
        return "unknown", bn

    def _dataflow(self, main: Any, runs: list[Run], step_by_act: dict[str, tuple[Step, Run]],
                  flows: list[OutputFlow]) -> list[DataEdge]:
        """Generic step-to-step data flow (generated by A, used by B, also through collection members)
        and parameter passing (inputs of a run used by its child steps), across documents and levels."""
        if not hasattr(self, "_gens"):
            self._flow_index()
        run_docs = {d.activity: d.name for d in self.docs if d.activity}
        top = runs[0]
        # run activity -> key of the box that represents it; step key -> run activity containing it
        run_key: dict[str, str] = {top.activity_id: "run"}
        step_run: dict[str, str] = {}
        for r in runs:
            for st in r.steps:
                k = f"{r.doc}|{st.name}"
                step_run[k] = r.activity_id
                for a in st.activity_ids:
                    if any(rr.activity_id == a for rr in runs):
                        run_key[a] = k
        run_parent = {r.activity_id: step_run.get(run_key.get(r.activity_id, ""), None) for r in runs}

        def step_key(act: str) -> str | None:
            hit = step_by_act.get(short_id(act))
            return f"{hit[1].doc}|{hit[0].name}" if hit else None

        def is_step_gen(act: str, doc: str) -> bool:
            return act != str(main) and run_docs.get(act) != doc and step_key(act) is not None

        # producers by IRI and by content
        by_content: dict[Any, list[str]] = {}
        for e in self._gens:
            by_content.setdefault(self._ckey(e), []).append(e)

        def producers(atom: str) -> list[tuple[str, str]]:
            out = []
            for e in {atom, *by_content.get(self._ckey(atom), [])}:
                for act, role, doc in self._gens.get(e, []):
                    if is_step_gen(act, doc):
                        out.append((act, role))
            return out

        def through(atom: str) -> list[str]:
            out = []
            for act, role, doc in self._gens.get(atom, []):
                if run_docs.get(act) == doc and act != str(main) and run_key.get(short_id(act)):
                    out.append(f"{run_key[short_id(act)].split('|')[-1]}/{local_name(role)}")
            return out

        flow_ents = {fe.id for f in flows for fe in f.entities}
        agg: dict[tuple, dict] = {}
        # ---- data edges
        for act, uses in self._uses.items():
            tk = step_key(act)
            if tk is None or act == str(main):
                continue
            for eiri, role, doc in uses:
                # a container produced by a step is the direct source: do not descend into its members
                atoms = [(eiri, "direct")] if producers(eiri) else self._atoms(eiri)
                for atom, via in atoms:
                    for pact, prole in producers(atom):
                        sk = step_key(pact)
                        if sk is None or sk == tk:
                            continue
                        kind, bn = self._kind(atom)
                        key = ("data", sk, tk, local_name(prole), local_name(role))
                        a = agg.setdefault(key, {"atoms": set(), "names": set(), "kinds": set(), "via": set(),
                                                 "through": set(), "drawn": False})
                        a["atoms"].add(self._ckey(atom))
                        if bn:
                            a["names"].add(bn)
                        a["kinds"].add(kind)
                        a["via"].add(via)
                        a["through"].update(through(atom))
                        if short_id(atom) in flow_ents:
                            a["drawn"] = True
        # ---- parameter passing (parent run input -> child step input, same entity or member of it)
        run_uses: dict[str, list[tuple[str, str]]] = {}
        for r in runs:
            ra = next((k for k in self._uses if short_id(k) == r.activity_id), None)
            if ra:
                run_uses[r.activity_id] = [(e, ro) for e, ro, d in self._uses[ra]]
        for act, uses in self._uses.items():
            tk = step_key(act)
            if tk is None or act == str(main):
                continue
            seen_e: set[tuple[str, str]] = set()
            for eiri, role, doc in uses:
                # (a sub-workflow's inputs are recorded on its run, in its own document: same as step inputs)
                if (eiri, role) in seen_e:
                    continue
                seen_e.add((eiri, role))
                if any(producers(a) for a, _ in self._atoms(eiri)):
                    continue  # data produced by a step: a data edge, not a parameter
                ck = self._ckey(eiri)
                anc = step_run.get(tk)
                skipped: list[str] = []
                found = None
                while anc is not None and found is None:
                    for pe, prole in run_uses.get(anc, []):
                        if pe == eiri or self._ckey(pe) == ck:
                            found = (anc, prole, "direct")
                            break
                        if any(m == eiri or self._ckey(m) == ck for m, _ in self._atoms(pe)[1:]):
                            found = (anc, prole, "member")
                            break
                    if found is None:
                        skipped.append(run_key.get(anc, anc).split("|")[-1])
                        anc = run_parent.get(anc)
                if found is None:
                    continue
                sk = run_key.get(found[0], found[0])
                kind, _ = self._kind(eiri)
                nm = local_name(role)
                key = ("param", sk, tk, local_name(found[1]), nm)
                a = agg.setdefault(key, {"atoms": set(), "names": set(), "kinds": set(), "via": set(),
                                         "through": set(), "drawn": False, "uses": 0, "skipped": set()})
                a["uses"] = a.get("uses", 0) + 1
                a["atoms"].add(str(ck))
                a["kinds"].add(kind)
                a["via"].add(found[2])
                a.setdefault("skipped", set()).update(skipped)
        edges = []
        for (kind, sk, tk, sp, tp), a in agg.items():
            ek = sorted(a["kinds"])
            note = None
            if a.get("skipped"):
                note = (f"not recorded as an input of {', '.join(sorted(a['skipped']))}; "
                        "matched on an ancestor run's input")
            edges.append(DataEdge(kind=kind, source=sk, target=tk, source_port=sp, target_port=tp,
                                  entity_kind=ek[0] if len(ek) == 1 else "/".join(ek),
                                  count=len(a["atoms"]) if kind == "data" else a.get("uses", 1),
                                  names=sorted(a["names"]), via="member" if "member" in a["via"] else "direct",
                                  through=sorted(a["through"]), drawn_as_entity=a["drawn"],
                                  platform=bool(PLATFORM_RE.search(tp)) or bool(SECRET_RE.search(tp)), note=note))
        order = {f"{r.doc}|{s.name}": (i, j) for i, r in enumerate(runs) for j, s in enumerate(r.steps)}
        order["run"] = (-1, 0)
        edges.sort(key=lambda e: (e.kind, order.get(e.source, (9, 9)), order.get(e.target, (9, 9)), e.target_port))
        return edges

    # -- main entry -------------------------------------------------------
    def build(self) -> Model:
        """Load, redact and extract everything into a :class:`Model`."""
        self._load_documents()
        self._taint_pass()
        g0 = self.graphs[self.docs[0].name]
        job = self._job(g0)
        agents, dels = self._agents(g0)
        main = self._main_run(g0, job)
        runs: list[Run] = []
        flows: list[OutputFlow] = []
        dataflow: list[DataEdge] = []
        inputs: list[IOValue] = []
        outputs: list[IOValue] = []
        hidden = 0
        if main is not None:
            self.docs[0].activity = str(main)
            top = self._run(self.docs[0].name, main, "main" if "main" in self.cwl else None, True)
            runs.append(top)
            # nested runs, document order (BFS) but attach to their parent step
            step_by_act: dict[str, tuple[Step, Run]] = {}
            for s in top.steps:
                for a in s.activity_ids:
                    step_by_act[a] = (s, top)
            for d in self.docs[1:]:
                sid = short_id(d.activity)
                parent = step_by_act.get(sid)
                proc = parent[0].cwl_run if parent else None
                if parent:
                    d.parent_step = parent[0].name
                r = self._run(d.name, URIRef(d.activity), proc, False)
                if parent:
                    r.iterations = max(r.starts, parent[0].shared_activity_starts)
                runs.append(r)
                for s in r.steps:
                    for a in s.activity_ids:
                        step_by_act[a] = (s, r)
            # inputs of the wrapping run
            seen: set[str] = set()
            for q in g0.objects(main, PROV.qualifiedUsage):
                role = g0.value(q, PROV.hadRole)
                ent = g0.value(q, PROV.entity)
                if role is None or ent is None:
                    continue
                nm = local_name(str(role))
                if nm in seen:
                    continue
                seen.add(nm)
                iv = self.describe(g0, ent, nm)
                iv.role = str(role).split("#", 1)[-1]
                iv.platform = bool(PLATFORM_RE.search(nm))
                if iv.platform and not self.show_platform:
                    hidden += 1
                    continue
                inputs.append(iv)
            inputs.sort(key=lambda x: (x.platform, x.name.lower()))
            # final outputs: generated by the wrapping run
            for e in sorted(set(g0.subjects(PROV.qualifiedGeneration, None)), key=str):
                gens = list(g0.objects(e, PROV.qualifiedGeneration))
                mine = [q for q in gens if g0.value(q, PROV.activity) == main]
                if not mine:
                    continue
                role = g0.value(mine[0], PROV.hadRole)
                nm = local_name(str(role)) if role is not None else short_id(str(e))
                ov = self.describe(g0, e, nm)
                ov.role = str(role).split("#", 1)[-1] if role is not None else ""
                for q in gens:
                    a = g0.value(q, PROV.activity)
                    if a is not None and a != main and short_id(str(a)) in step_by_act:
                        ov.generated_by.append(step_by_act[short_id(str(a))][0].name)
                ov.entity = short_id(str(e))
                outputs.append(ov)
            flows = [self._trace(o, main, top, step_by_act) for o in outputs]
            dataflow = self._dataflow(main, runs, step_by_act, flows)
        model = Model(tool=f"prov_synth {__version__}", source=str(self.src.bag_root or self.src.prov_dir),
                      research_object=self._ro_id(), job=job, agents=agents, delegations=dels,
                      documents=self.docs, runs=runs, inputs=inputs, outputs=outputs,
                      platform_params_hidden=hidden, redactions=0, flows=flows if main is not None else [],
                      dataflow=dataflow if main is not None else [], notes=sorted(set(self.notes), key=self.notes.index))
        self.red.scrub(model)
        model.redactions = self.red.count
        return model

    def _ro_id(self) -> str | None:
        root = self.src.bag_root
        if root and (root / "bag-info.txt").exists():
            for line in (root / "bag-info.txt").read_text().splitlines():
                if line.startswith("External-Identifier:"):
                    return line.split(":", 1)[1].strip()
        return None


def _ground(g: Graph) -> set:
    """Triples without blank nodes (for duplicate-document comparison)."""
    return {t for t in g if not any(isinstance(x, BNode) for x in t)}


def _taint_json(obj: Any, red: Redactor, key: str = "") -> None:
    """Register secret values found in a JSON document (by key)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            _taint_json(v, red, str(k))
    elif isinstance(obj, list):
        for v in obj:
            _taint_json(v, red, key)
    elif isinstance(obj, str) and SECRET_RE.search(key):
        red.taint(obj)


# --------------------------------------------------------------------------
# Profiles mapping
# --------------------------------------------------------------------------
def apply_profiles(model: Model, path: Path) -> None:
    """Attach process profiles to steps from a YAML mapping (by step name or container image).

    Steps are matched against entries in file order (first match wins); the
    profile cards keep the file order, entries with ``profile: null`` last.
    """
    if yaml is None:
        raise SystemExit("prov_synth: pyyaml is required for --profiles")
    data = yaml.safe_load(path.read_text())
    entries = data.get("mappings", data.get("profiles", [])) if isinstance(data, dict) else data
    entries = [e for e in (entries or []) if isinstance(e, dict)]
    if isinstance(data, dict):
        model.profiles_title = data.get("title")
        model.profiles_subtitle = data.get("subtitle")
    cards: dict[str, tuple[int, ProfileCard]] = {}
    used: set[int] = set()
    for run in model.runs:
        for st in run.steps:
            for idx, ent in enumerate(entries):
                ok = False
                if ent.get("step"):
                    pat = str(ent["step"])
                    ok = any(fnmatch.fnmatchcase(n, pat) for n in [st.name] + st.instance_names)
                if not ok and ent.get("image"):
                    pat = str(ent["image"])
                    ok = any(fnmatch.fnmatchcase(im, pat) or (not any(c in pat for c in "*?[") and pat in im)
                             for im in st.images)
                if not ok:
                    continue
                used.add(idx)
                prof = ent.get("profile")
                short = str(ent.get("short") or (str(prof).rsplit(".", 1)[-1] if prof else "no profile"))
                st.profile, st.profile_short, st.openeo, st.profile_matched = prof, short, ent.get("openeo"), True
                kind = ent.get("kind") or st.cwl_class
                if ent.get("phase"):
                    kind = f"{kind} · {ent['phase']}" if kind else str(ent["phase"])
                key = str(prof) if prof else f"none:{idx}"
                order = idx if prof else 10_000 + idx
                if key in cards:
                    order = min(order, cards[key][0])
                card = cards[key][1] if key in cards else ProfileCard(short=short, profile=prof, openeo=ent.get("openeo"),
                                                                      kind=kind, note=ent.get("note"))
                cards[key] = (order, card)
                if st.name not in card.steps:
                    card.steps.append(st.name)
                break
    model.profiles = [c for _, c in sorted(cards.values(), key=lambda t: t[0])]
    for idx, e in enumerate(entries):
        if idx not in used:
            what = f"step {e['step']}" if e.get("step") else f"image {e.get('image')}"
            model.notes.append(f"profile mapping entry #{idx + 1} ({what}) matched no step "
                               "(or every candidate step was matched by an earlier entry)")


def card_lines(c: ProfileCard, width: float, size: float = 10.5) -> list[str]:
    """Lines of a profile card: name, kind, openEO relation (or the steps without profile)."""
    if c.profile:
        body = [c.kind or "", "openEO: " + (c.openeo or "–")]
    else:
        body = [", ".join(c.steps) + (": " + c.note if c.note else " (no process profile)")]
    out = [c.short]
    for b in body:
        out += wrap_text(b, width, size) or [""]
    return out


# --------------------------------------------------------------------------
# Display helpers shared by renderers
# --------------------------------------------------------------------------
def io_line(v: IOValue, n: int = 58) -> str:
    """One display line ``name = value`` for the inputs/outputs boxes."""
    if v.kind == "collection":
        mem = [last_segment(m) for m in v.members]
        body = "{" + ", ".join(mem) + "}"
        if len(body) > n - len(v.name) - 3:
            body = f"[{len(mem)}] " + ", ".join(ellipsize(m, 26) for m in mem[:2]) + (", …" if len(mem) > 2 else "")
        return ellipsize(f"{v.name} = {body}", n)
    if v.kind == "directory":
        return ellipsize(f"{v.name} = {v.value}/ ({len(v.members)} entries)", n)
    return ellipsize(f"{v.name} = {shorten_value(v.value or '', n - len(v.name) - 3)}", n)


def input_lines(model: Model, n: int = 64, max_members: int = 6) -> list[str]:
    """Lines of the inputs box: one per role; long collections expanded one member per line."""
    out = []
    for v in model.inputs:
        line = io_line(v, n)
        if v.kind == "collection" and (line.endswith("…") or "[" in line.split("=", 1)[1][:3]):
            out.append(f"{v.name} = [{len(v.members)} items]")
            for m in v.members[:max_members]:
                out.append("\u2003– " + shorten_value(m, n + 8))
            if len(v.members) > max_members:
                out.append(f"\u2003… +{len(v.members) - max_members} more")
        else:
            out.append(line)
    if model.platform_params_hidden:
        out.append(f"+ {model.platform_params_hidden} platform parameters hidden (--show-platform-params)")
    return out


def image_short(im: str) -> str:
    """``ghcr.io/org/repo/crop:1.5.0`` -> ``crop:1.5.0``."""
    return im.rsplit("/", 1)[-1]


def step_lines(st: Step, run: Run, top: bool) -> list[str]:
    """Text lines of a step box (title first)."""
    title = st.name + (f" ×{st.count}" if st.count > 1 else "")
    lines = [title]
    if st.kind == "application":
        lines.append(f"the Application {st.cwl_run or ''}".strip())
    elif st.kind == "platform":
        lines.append("platform step")
    elif st.cwl_class == "Workflow":
        lines.append(f"sub-workflow {st.cwl_run or ''}".strip())
    if st.shared_activity_starts > 1:
        lines.append(f"scatter: {st.shared_activity_starts} iterations share one activity id")
    elif st.count > 1 and st.scatter:
        lines.append(f"scatter over {', '.join(st.scatter)}" + (f" · {run.iterations} iterations" if run.iterations > 1 else
                                                                  f": {st.count} runs"))
    elif st.count > 1 and run.iterations > 1:
        lines.append(f"{st.count} runs, one per scatter iteration" if st.count == run.iterations
                     else f"{st.count} runs over {run.iterations} scatter iterations")
    elif st.count > 1:
        lines.append(f"{st.count} runs")
    if st.images and st.kind != "platform":
        ims = sorted({image_short(i) for i in st.images})
        lines.append(ellipsize(", ".join(ims), 40))
    t = f"{hhmmss(st.start)}–{hhmmss(st.end)}" if st.start and st.end else ""
    d = duration(st.start, st.end)
    if t:
        lines.append(t + (f" · {d}" if d else ""))
    return lines


def param_lines(model: Model, key: str, mode: str) -> list[str]:
    """Parameter-passing lines of a step box (``mode``: none | summary | full)."""
    if mode == "none":
        return []
    show_plat = model.platform_params_hidden == 0
    edges = [e for e in model.dataflow if e.kind == "param" and e.target == key]
    vis = [e for e in edges if show_plat or not e.platform]
    hidden = len(edges) - len(vis)
    if mode == "summary":
        names = []
        for e in vis:
            n = e.target_port + (f" ∈ {e.source_port}" if e.via == "member" else "")
            if n not in names:
                names.append(n)
        out = wrap_text("params: " + ", ".join(sorted(names)), 330, 10.5) if names else []
        if hidden:
            out.append(f"+ {hidden} platform parameters")
        return out
    out = []
    for e in vis:
        src = "wrapping run" if e.source == "run" else e.source.split("|")[-1]
        out.append(ellipsize(f"{e.target_port} ← {src}.{e.source_port}" + (" (member)" if e.via == "member" else "")
                             + (f" ×{e.count}" if e.count > 1 else ""), 48))
    if hidden:
        out.append(f"+ {hidden} platform parameters")
    return out


def data_label(e: DataEdge) -> str:
    """``binary_mask_item → rasters · 2 × otsu.tif``."""
    if e.names and len(e.names) == 1:
        what = f"{e.count} × {e.names[0]}" if e.count > 1 else e.names[0]
    elif e.names:
        what = f"{e.count} {e.entity_kind}s ({', '.join(e.names[:3])}{', …' if len(e.names) > 3 else ''})"
    else:
        what = f"{e.count} {e.entity_kind}{'s' if e.count > 1 else ''}"
    return f"{e.source_port} → {e.target_port} · {what}"


def output_lines(o: IOValue, staged: bool = False) -> list[str]:
    """Lines of the result entity box (``staged``: generated by a platform stage-out step)."""
    lines = [f"result · {o.name}"] + (["reference to the staged-out copy"] if staged else [])
    if o.kind == "dictionary":
        lines.append(shorten_value(o.value or "", 40))
        for m in o.members:
            k, _, v = m.partition(": ")
            if k == "type":
                lines.append("type " + ellipsize(v.rsplit("/", 1)[-1], 34))
            else:
                lines.append(ellipsize(f"{k} {last_segment(v)}", 40))
    elif o.kind == "directory":
        lines.append(f"directory {o.value}/")
        lines.append(ellipsize(", ".join(o.members), 40))
    elif o.kind == "collection":
        lines.append(f"{len(o.members)} items")
    else:
        lines.append(shorten_value(o.value or "", 40))
    return lines


def nice_date(t: str | None) -> str:
    """``2026-10-14T…`` -> ``14 October 2026``."""
    try:
        d = datetime.fromisoformat(t or "")
        return f"{d.day} {d.strftime('%B %Y')}"
    except ValueError:
        return ""


def doc_role(model: Model, d: ProvDocument) -> str:
    """Short description of what a document describes, for band headers."""
    if d.level == 0:
        return "engine document completed by ZOO-Project-DRU" if model.job else "engine document"
    step = None
    for r in model.runs:
        for s in r.steps:
            if s.nested_doc == d.name:
                step = s
    if step is None:
        return "nested run"
    if step.kind == "application":
        return "the Application"
    if step.shared_activity_starts > 1:
        return f"{'both' if step.shared_activity_starts == 2 else 'all ' + str(step.shared_activity_starts)} scatter iterations of {step.name}"
    return f"step {step.name}"


def footer_text(model: Model, title: str | None) -> str:
    """Footer naming the job and stating the view is synthetic."""
    j = model.job
    parts = []
    if j:
        host = re.sub(r"^https?://", "", (j.server or "")).split("/")[0]
        parts.append(f"Job {j.id}" + (f" ({j.process_id})" if j.process_id else "") + (f" on {host}" if host else "")
                     + (f", {nice_date(j.start)}" if j.start else "") + ".")
    elif model.runs:
        parts.append(f"Workflow run {model.runs[0].activity_id}.")
    extra = []
    if model.platform_params_hidden:
        extra.append(f"{model.platform_params_hidden} stage-in/stage-out parameters hidden")
    parts.append("Synthetic view generated by prov_synth from the CWLProv research object: identifiers shortened; "
                 "secret values redacted; container-image agents shown on their step"
                 + ("; " + "; ".join(extra) if extra else "") + ".")
    return " ".join(parts)


# --------------------------------------------------------------------------
# SVG renderer
# --------------------------------------------------------------------------
FONT = 'font-family="Helvetica, Arial, sans-serif"'
C_ACT, C_ENT, C_AGT, C_TAG, C_TAGS = "#c9d3fd", "#fffcc0", "#fedfa6", "#e3eedd", "#6b8f5e"
C_BAND, C_BANDS, C_LINE = "#f4f5f7", "#c8ccd2", "#444"

_NARROW = set("ijl.,:;|!'()[]{}/\\ `")
_SEMI = set("frtI-\"* ")
_WIDE = set("mwMW@%")


def text_width(s: str, size: float, bold: bool = False) -> float:
    """Approximate rendered width of ``s`` in Helvetica at ``size`` px."""
    w = 0.0
    for ch in s:
        if ch in _NARROW:
            w += 0.28
        elif ch in _SEMI:
            w += 0.34
        elif ch in _WIDE:
            w += 0.86
        elif ch.isupper():
            w += 0.69
        elif ch.isdigit():
            w += 0.56
        elif ch in "…≙×–—":
            w += 0.9
        else:
            w += 0.56
    return w * size * (1.08 if bold else 1.0) * 1.04


class Svg:
    """Tiny SVG writer with the PROV shapes used by the diagram."""

    def __init__(self) -> None:
        self.out: list[str] = []

    def add(self, s: str) -> None:
        self.out.append(s)

    def text(self, x: float, y: float, s: str, size: float = 12, anchor: str = "middle",
             weight: str = "normal", color: str = "#222") -> None:
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}" text-anchor="{anchor}" '
                 f'font-weight="{weight}" fill="{color}">{xml_escape(s)}</text>')

    def lines(self, cx: float, cy: float, ls: list[str], size: float, left: float | None = None) -> None:
        n = len(ls)
        y0 = cy - (n - 1) * (size + 4) / 2 + size * 0.35
        for i, line in enumerate(ls):
            if left is not None and i > 0:
                self.text(left, y0 + i * (size + 4), line, size, anchor="start")
            else:
                self.text(cx, y0 + i * (size + 4), line, size if i else size + 0.5, weight="bold" if i == 0 else "normal")

    def node(self, x: float, y: float, w: float, h: float, kind: str, ls: list[str], size: float = 11.5,
             tag: str | None = None, left: bool = False) -> None:
        if kind == "act":
            self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{C_ACT}" stroke="#555"/>')
        elif kind == "ent":
            self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="16" fill="{C_ENT}" stroke="#555"/>')
        else:
            self.add(f'<path d="M{x:.1f},{y + 12:.1f} L{x + w / 2:.1f},{y:.1f} L{x + w:.1f},{y + 12:.1f} '
                     f'L{x + w:.1f},{y + h:.1f} L{x:.1f},{y + h:.1f} Z" fill="{C_AGT}" stroke="#555"/>')
        th = h - (24 if tag else 0)
        top = y + (8 if kind == "agt" else 0)
        self.lines(x + w / 2, top + (th - (8 if kind == "agt" else 0)) / 2, ls, size, left=(x + 18) if left else None)
        if tag:
            self.add(f'<rect x="{x + 8:.1f}" y="{y + h - 22:.1f}" width="{w - 16:.1f}" height="17" rx="3" '
                     f'fill="{C_TAG}" stroke="{C_TAGS}"/>')
            self.text(x + w / 2, y + h - 9.5, "≙ " + tag, 10.5, color="#2f4a26")

    def path(self, d: str, dashed: bool = False, head: bool = True) -> None:
        dash = ' stroke-dasharray="5,3"' if dashed else ""
        mk = ' marker-end="url(#ah)"' if head else ""
        self.add(f'<path d="{d}" fill="none" stroke="{C_LINE}" stroke-width="1.2"{dash}{mk}/>')

    def label(self, x: float, y: float, s: str, anchor: str = "middle") -> None:
        # white halo keeps labels readable over lines
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="10.5" text-anchor="{anchor}" fill="{C_LINE}" '
                 f'stroke="#fff" stroke-width="3" paint-order="stroke">{xml_escape(s)}</text>')


@dataclass
class Box:
    """Placed node."""
    x: float
    y: float
    w: float
    h: float

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def bottom(self) -> float:
        return self.y + self.h

    @property
    def right(self) -> float:
        return self.x + self.w


def measure(lines: list[str], size: float, tag: str | None = None, minw: float = 130, pad: float = 24) -> tuple[float, float]:
    """Width/height of a node holding ``lines`` (first line bold)."""
    w = max(text_width(line, size + (0.5 if i == 0 else 0), bold=(i == 0)) for i, line in enumerate(lines)) + pad
    if tag:
        w = max(w, text_width("≙ " + tag, 10.5) + 32)
    h = len(lines) * (size + 4) + 18 + (24 if tag else 0)
    return max(minw, w), h


C_DATA = "#0b7a75"


def render_svg(model: Model, title: str | None = None, dataflow: bool = True, params: str = "summary") -> str:
    """Render the model as a standalone SVG string (deterministic layout)."""
    S = Svg()
    data_edges = [e for e in model.dataflow if dataflow and e.kind == "data" and not e.drawn_as_entity]

    def doc_of(key: str) -> str:
        return model.documents[0].name if key == "run" else key.split("|")[0]

    lane_count: dict[str, int] = {}
    lane_of: list[tuple[int, int | None]] = []
    n_cross = 0
    for e in data_edges:
        sd, td = doc_of(e.source), doc_of(e.target)
        k1 = lane_count.get(sd, 0)
        lane_count[sd] = k1 + 1
        k2 = None
        if td != sd:
            k2 = lane_count.get(td, 0)
            lane_count[td] = k2 + 1
            n_cross += 1
        lane_of.append((k1, k2))
    rows_bottom: dict[str, float] = {}

    def lane_space(doc: str) -> float:
        n = lane_count.get(doc, 0)
        return 16 + 18 * n if n else 0
    has_prof = bool(model.profiles)
    X0 = 40  # content left
    GUT = 30  # gutter lane x for cross-band hierarchy links

    # ---------- measure fixed rows ----------
    agents = order_agents(model)
    agent_sz = []
    for a in agents:
        ls = [a.name] + ([a.version] if a.version else []) + (["user account"] if a.kind == "account" else [])
        w, h = measure(ls, 11.5, minw=110, pad=26)
        agent_sz.append((ls, w, max(h + 6, 46)))
    AG_GAP = 26
    agents_w = sum(w for _, w, _ in agent_sz) + AG_GAP * max(0, len(agent_sz) - 1)

    j = model.job
    top = model.runs[0] if model.runs else None
    job_ls = ent_ls = plan_ls = []
    if j:
        job_ls = [f"Job {ellipsize_id(j.id)}", "wfprov:ProcessRun · "
                  + (f"{hhmmss(j.start)}–{hhmmss(j.end)} UTC" if j.start and j.end else (j.status or ""))]
        if j.status:
            job_ls.append(f"status: {j.status}" + (f" · {duration(j.start, j.end)}" if j.start and j.end else ""))
        ent_ls = ["job entity", f"/jobs/{ellipsize_id(j.id)}"]
        plan_ls = ["process (plan)", f"/processes/{j.process_id}"]
    run_ls = ["Wrapping workflow run", "wfprov:WorkflowRun · cwltool"]
    if top and top.start and top.end:
        run_ls.append(f"{hhmmss(top.start)}–{hhmmss(top.end)} · {duration(top.start, top.end)}")
    in_ls = ["inputs (prov:role = prov:value)"] + input_lines(model)
    lab_w = text_width("wasGeneratedBy", 10.5) + 22

    jw, jh = measure(job_ls, 11.5, minw=200) if j else (0, 0)
    rw, rh = measure(run_ls, 11.5, minw=200)
    jw = rw = max(jw, rw)
    ew, eh = measure(ent_ls, 11.5, minw=150) if j else (0, 0)
    pw, ph = measure(plan_ls, 11.5, minw=150) if j else (0, 0)
    iw, ih = measure(in_ls, 11, minw=220, pad=40)
    jh = max(jh, eh, ph)
    job_row_w = jw + lab_w + ew + 24 + pw if j else 0
    run_row_w = rw + lab_w + iw

    # step boxes
    def step_box(st: Step, run: Run, is_top: bool) -> tuple[list[str], float, float, str | None]:
        ls = step_lines(st, run, is_top) + param_lines(model, f"{run.doc}|{st.name}", params)
        tag = st.profile_short if (has_prof and st.profile_matched) else None
        w, h = measure(ls, 11.5, tag=tag, minw=170)
        return ls, w, h, tag

    platform_steps = {s.name for s in top.steps if s.kind == "platform"} if top else set()
    out_ls = [output_lines(o, bool(set(o.generated_by) & platform_steps)) for o in model.outputs]
    flow_ents = {fe.id: fe for f in model.flows for fe in f.entities}
    used_links = [ln for f in model.flows for ln in f.links if ln.relation == "used"]
    ent_doc = {fid: fe.produced_by[0].split("|")[0] for fid, fe in flow_ents.items() if fe.produced_by}
    ent_boxes: dict[str, Box] = {}
    out_sz = [measure(ls, 11, minw=180) for ls in out_ls]
    max_step_w = max([step_box(s, r, i == 0)[1] for i, r in enumerate(model.runs) for s in r.steps] + [0])
    MW = max(700, agents_w, job_row_w, run_row_w, max_step_w, *(w + lab_w + 180 for w, _ in out_sz))
    MW = min(MW, max(1100, agents_w, job_row_w, run_row_w))
    BAND_X, BAND_W = 20, MW + 40

    y = 20
    title_h = 0
    if title:
        title_h = 34
        y += title_h
    boxes: dict[str, Box] = {}  # step key -> box
    band_rects: list[tuple[float, float, ProvDocument]] = []

    def flow(items: list[tuple[str, float, float]], y0: float, gap: float = 22, rowgap: float = 34
             ) -> tuple[dict[str, Box], list[list[str]], float]:
        """Left-to-right flow with wrapping; returns placed boxes, rows and bottom y."""
        placed: dict[str, Box] = {}
        rows: list[list[str]] = [[]]
        x, rowy, rowh = X0, y0, 0.0
        for key, w, h in items:
            g = gap if not is_ent(key) else lab_w
            if rows[-1] and x + g + w > X0 + MW:
                rowy += rowh + rowgap
                x, rowh = X0, 0.0
                rows.append([])
            elif rows[-1]:
                x += g
            placed[key] = Box(x, rowy, w, h)
            rows[-1].append(key)
            x += w
            rowh = max(rowh, h)
        return placed, rows, rowy + rowh

    def add_flow_entities(items: list, meta: dict, step_key: str) -> None:
        """Insert the flow entities produced by ``step_key`` right after it in the row."""
        for fid, fe in flow_ents.items():
            if fe.produced_by and fe.produced_by[0] == step_key:
                ls = flow_entity_lines(fe, model)
                w, h = measure(ls, 11, minw=200)
                items.append((f"ent:{fid}", w, h))
                meta[f"ent:{fid}"] = (ls, None, None)

    def header(by: float, d: ProvDocument) -> float:
        """Band header (right-aligned); returns its height."""
        right = BAND_X + BAND_W - 12
        S.text(right, by + 17, ellipsize_doc(d.name) + "", 11.5, "end", "bold", "#333")
        S.text(right, by + 31, f"GET {d.api_path} — {doc_role(model, d)}", 10.5, "end", "normal", "#555")
        hh = 40
        if d.merged_from:
            S.text(right, by + 45, "merged with " + ", ".join(ellipsize_doc(m) for m in d.merged_from)
                   + " (same activity, duplicate document)", 10.5, "end", "normal", "#555")
            hh = 54
        return hh


    # ---------- primary band ----------
    d0 = model.documents[0]
    band_y = y
    hh = header(band_y, d0)
    dels = model.delegations
    ids = [a.id for a in agents]
    curves = [d for d in dels if d.delegate in ids and d.responsible in ids
              and ids.index(d.delegate) != ids.index(d.responsible) + 1]
    ay = band_y + hh + (18 + 12 * len(curves) if curves else 6)
    abox: dict[str, Box] = {}
    x = X0
    agent_h = max([h for _, _, h in agent_sz] + [46])
    for a, (ls, w, h) in zip(agents, agent_sz):
        abox[a.id] = Box(x, ay, w, agent_h)
        S.node(x, ay, w, agent_h, "agt", ls, 11.5)
        x += w + AG_GAP
    for k, d in enumerate(curves):
        b1, b2 = abox[d.delegate], abox[d.responsible]
        peak = ay - 14 - 12 * k
        S.path(f"M{b1.cx:.1f},{ay + 1:.1f} C{b1.cx:.1f},{peak:.1f} {b2.cx:.1f},{peak:.1f} {b2.cx:.1f},{ay + 1:.1f}")
        S.label((b1.cx + b2.cx) / 2, peak + 4, "actedOnBehalfOf")
    for d in dels:
        if d in curves or d.delegate not in abox or d.responsible not in abox:
            continue
        b1, b2 = abox[d.delegate], abox[d.responsible]
        yy = ay + agent_h * 0.62
        S.path(f"M{b1.x:.1f},{yy:.1f} L{b2.right + 2:.1f},{yy:.1f}")
    y = ay + agent_h

    server = next((a for a in agents if a.kind == "server"), None)
    jbox = None
    if j:
        jy = y + 58
        jbox = Box(X0, jy, jw, jh)
        S.node(X0, jy, jw, jh, "act", job_ls)
        ebox = Box(jbox.right + lab_w, jy, ew, jh)
        S.node(ebox.x, jy, ew, jh, "ent", ent_ls)
        pbox = Box(ebox.right + 24, jy, pw, jh)
        S.node(pbox.x, jy, pw, jh, "ent", plan_ls)
        S.path(f"M{ebox.x:.1f},{jy + jh * 0.6:.1f} L{jbox.right + 2:.1f},{jy + jh * 0.6:.1f}")
        S.label((ebox.x + jbox.right) / 2, jy + jh * 0.6 - 6, "wasGeneratedBy")
        sx = jbox.x + jbox.w * 0.72
        S.path(f"M{sx:.1f},{jy:.1f} C{sx:.1f},{jy - 26:.1f} {pbox.cx:.1f},{jy - 26:.1f} {pbox.cx:.1f},{jy - 1:.1f}")
        S.label((sx + pbox.cx) / 2, jy - 22, "wasAssociatedWith (hadPlan)")
        if j.process_specializes:
            S.text(pbox.cx, jy + jh + 15, "specializationOf " + j.process_specializes.split("#", 1)[-1].join(["wf:", ""])
                   + " (engine plan)", 10.5, color=C_LINE)
        if server:
            sb = abox[server.id]
            vx = sb.cx if jbox.x < sb.cx < jbox.right else jbox.x + 30
            S.path(f"M{vx:.1f},{jy:.1f} L{vx:.1f},{sb.bottom + 2:.1f}")
            S.label(vx + 6, (jy + sb.bottom) / 2 + 4, "wasAssociatedWith", "start")
        y = jy + jh + (20 if j.process_specializes else 0)

    rbox = None
    if top:
        ry = y + 40
        row_h = max(rh, ih)
        rbox = Box(X0, ry + (row_h - rh) / 2 if ih > rh + 30 else ry, rw, rh)
        S.node(rbox.x, rbox.y, rw, rh, "act", run_ls)
        ibox = Box(rbox.right + lab_w, ry, iw, max(ih, rh))
        S.node(ibox.x, ibox.y, iw, ibox.h, "ent", in_ls, 11, left=True)
        S.path(f"M{rbox.right:.1f},{rbox.y + rh / 2:.1f} L{ibox.x - 2:.1f},{rbox.y + rh / 2:.1f}")
        S.label((rbox.right + ibox.x) / 2, rbox.y + rh / 2 - 6, "used")
        if jbox:
            vx = jbox.x + 40
            S.path(f"M{vx:.1f},{rbox.y:.1f} L{vx:.1f},{jbox.bottom + 2:.1f}")
            S.label(vx + 6, (rbox.y + jbox.bottom) / 2 + 4, "wasInformedBy", "start")
        y = ry + max(row_h, ibox.h)

        # steps row(s) + outputs
        items = []
        meta: dict[str, tuple[list[str], str | None, Step | None]] = {}
        for st in top.steps:
            ls, w, h, tag = step_box(st, top, True)
            key = f"{top.doc}|{st.name}"
            items.append((key, w, h))
            meta[key] = (ls, tag, st)
            add_flow_entities(items, meta, key)
        for k, (o, ls) in enumerate(zip(model.outputs, out_ls)):
            w, h = out_sz[k]
            items.append((f"out:{k}", w, h))
            meta[f"out:{k}"] = (ls, None, None)
        sy = y + (70 if model.outputs else 44)
        placed, rows, bottom = flow(items, sy)
        draw_flow(S, placed, meta)
        boxes.update({k: v for k, v in placed.items() if not is_ent(k)})
        ent_boxes.update({k[4:]: v for k, v in placed.items() if k.startswith("ent:")})
        hierarchy(S, rbox, [placed[k] for k in rows[0] if not is_ent(k)], sy - 16, rows, placed, GUT)
        # final outputs are also generated by the wrapping run itself
        for k, o in enumerate(model.outputs):
            ob = placed[f"out:{k}"]
            lane = sy - 34
            tx = rbox.right - 24
            S.path(f"M{ob.cx:.1f},{ob.y:.1f} L{ob.cx:.1f},{lane:.1f} L{tx:.1f},{lane:.1f} L{tx:.1f},{rbox.bottom + 2:.1f}")
            S.label((ob.cx + tx) / 2, lane - 5, "wasGeneratedBy (output " + o.name + " of the wrapping run)")
        for k, o in enumerate(model.outputs):
            ob = placed[f"out:{k}"]
            gens = [boxes[f"{top.doc}|{g}"] for g in o.generated_by if f"{top.doc}|{g}" in boxes]
            if gens:
                gb = gens[0]
                if abs(gb.y - ob.y) < 1 and gb.right < ob.x:
                    yy = ob.y + min(ob.h, gb.h) / 2
                    S.path(f"M{ob.x:.1f},{yy:.1f} L{gb.right + 2:.1f},{yy:.1f}")
                    S.label((ob.x + gb.right) / 2, yy - 6, "wasGeneratedBy")
                else:
                    ly = max(ob.bottom, gb.bottom) + 10
                    S.path(f"M{ob.cx:.1f},{ob.bottom:.1f} L{ob.cx:.1f},{ly:.1f} L{gb.cx + 20:.1f},{ly:.1f} "
                           f"L{gb.cx + 20:.1f},{gb.bottom + 2:.1f}")
                    S.label((ob.cx + gb.cx) / 2, ly + 13, "wasGeneratedBy")
                    bottom = max(bottom, ly + 14)
        y = bottom
        rows_bottom[d0.name] = bottom
        y += lane_space(d0.name)
    band_rects.append((band_y, y + 18 - band_y, d0))
    y += 18

    # ---------- nested bands ----------
    for r in model.runs[1:]:
        d = next(dd for dd in model.documents if dd.name == r.doc)
        y += 12
        band_y = y
        hh = header(band_y, d)
        items, meta = [], {}
        for st in r.steps:
            ls, w, h, tag = step_box(st, r, False)
            key = f"{r.doc}|{st.name}"
            items.append((key, w, h))
            meta[key] = (ls, tag, st)
            add_flow_entities(items, meta, key)
        incoming = any(ent_doc.get(ln.entity) == r.doc and not ln.step.startswith(r.doc + "|") for ln in used_links)
        sy = band_y + hh + 14 + (22 if incoming else 0)
        placed, rows, bottom = flow(items, sy)
        draw_flow(S, placed, meta)
        boxes.update({k: v for k, v in placed.items() if not is_ent(k)})
        ent_boxes.update({k[4:]: v for k, v in placed.items() if k.startswith("ent:")})
        parent_key = f"{d.parent_doc}|{d.parent_step}"
        pb = boxes.get(parent_key)
        if pb and rows[0]:
            hierarchy(S, pb, [placed[k] for k in rows[0] if not is_ent(k)], sy - 8, rows, placed, GUT, cross=True)
        rows_bottom[d.name] = bottom
        y = bottom + 18 + lane_space(d.name)
        band_rects.append((band_y, y - band_y, d))

    content_bottom = y

    # ---------- output data flow: generation by the producing step, use by other steps ----------
    for f in model.flows:
        for ln in f.links:
            eb = ent_boxes.get(ln.entity)
            sb = boxes.get(ln.step)
            if eb is None or sb is None or ln.level != "step":
                continue
            if ln.relation == "wasGeneratedBy":
                if abs(sb.y - eb.y) < 1 and sb.right < eb.x:
                    yy = eb.y + min(eb.h, sb.h) / 2
                    S.path(f"M{eb.x:.1f},{yy:.1f} L{sb.right + 2:.1f},{yy:.1f}")
                    S.label((eb.x + sb.right) / 2, yy - 6, "wasGeneratedBy")
                else:
                    ly = max(eb.bottom, sb.bottom) + 10
                    S.path(f"M{eb.cx:.1f},{eb.bottom:.1f} L{eb.cx:.1f},{ly:.1f} L{sb.cx:.1f},{ly:.1f} L{sb.cx:.1f},{sb.bottom + 2:.1f}")
                    S.label((eb.cx + sb.cx) / 2, ly + 13, "wasGeneratedBy")
            else:  # used: activity -> entity, entering the entity from above
                lane = eb.y - 22
                sx = sb.x + sb.w * 0.8
                if sb.bottom < lane:
                    S.path(f"M{sx:.1f},{sb.bottom:.1f} L{sx:.1f},{lane:.1f} L{eb.cx:.1f},{lane:.1f} L{eb.cx:.1f},{eb.y - 2:.1f}")
                else:
                    lane = min(eb.y, sb.y) - 22
                    S.path(f"M{sx:.1f},{sb.y:.1f} L{sx:.1f},{lane:.1f} L{eb.cx:.1f},{lane:.1f} L{eb.cx:.1f},{eb.y - 2:.1f}")
                ly = (min(sb.bottom, lane) + lane) / 2 + 4 if sb.bottom < lane else lane - 5
                S.label(sx + 6, ly if sb.bottom < lane else lane - 5, f"used ({local_name(ln.role)})", "start")

    # ---------- step-to-step data flow (distinct colour, lanes below rows, corridor right of the bands) ----------
    outs: dict[str, int] = {}
    ins: dict[str, int] = {}
    cross_j = 0
    labels: list[tuple[float, float, str]] = []
    for e, (k1, k2) in zip(data_edges, lane_of):
        a, b = boxes.get(e.source), boxes.get(e.target)
        if a is None or b is None:
            continue
        sd, td = doc_of(e.source), doc_of(e.target)
        oi, ii = outs.get(e.source, 0), ins.get(e.target, 0)
        outs[e.source], ins[e.target] = oi + 1, ii + 1
        ex = a.x + a.w * 0.62 + 10 * oi
        en = b.x + b.w * 0.38 - 10 * ii
        ly1 = rows_bottom[sd] + 22 + 18 * k1
        if k2 is None:
            d = f"M{ex:.1f},{a.bottom:.1f} L{ex:.1f},{ly1:.1f} L{en:.1f},{ly1:.1f} L{en:.1f},{b.bottom + 3:.1f}"
            lx, ly, seg = (ex + en) / 2, ly1, abs(en - ex)
        else:
            ly2 = rows_bottom[td] + 22 + 18 * k2
            cx = BAND_X + BAND_W + 10 + 8 * cross_j
            cross_j += 1
            d = (f"M{ex:.1f},{a.bottom:.1f} L{ex:.1f},{ly1:.1f} L{cx:.1f},{ly1:.1f} L{cx:.1f},{ly2:.1f} "
                 f"L{en:.1f},{ly2:.1f} L{en:.1f},{b.bottom + 3:.1f}")
            lx, ly, seg = (cx + en) / 2, ly2, abs(cx - en)
        S.add(f'<path d="{d}" fill="none" stroke="{C_DATA}" stroke-width="2.2" marker-end="url(#dh)"/>')
        lab = data_label(e)
        # above the lane if it fits between the verticals, else below it (where no vertical of this edge goes)
        labels.append((lx, ly - 5 if text_width(lab, 10.5, True) + 10 < seg else ly + 13, lab))
    for lx, ly, lab in labels:
        S.add(f'<text x="{lx:.1f}" y="{ly:.1f}" {FONT} font-size="10.5" text-anchor="middle" fill="{C_DATA}" '
              f'font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">{xml_escape(lab)}</text>')

    # ---------- profiles column ----------
    W = BAND_X + BAND_W + 20 + (8 * n_cross + 10 if n_cross else 0)
    col_bottom = 0.0
    if has_prof:
        rx, rwid = BAND_X + BAND_W + 40 + (8 * n_cross if n_cross else 0), 360
        cards = model.profiles
        ty = 20 + title_h
        hdr = [model.profiles_title or "Process profiles", model.profiles_subtitle or ""]
        note = ["≙  the step corresponds to this profile", "(mapping supplied with --profiles;",
                "not asserted in the served provenance)"]
        cy = ty + 120
        card_h = []
        for c in cards:
            ls = card_lines(c, rwid - 50)
            card_h.append((ls, 22 + 17 * len(ls)))
        col_h = 120 + sum(h + 10 for _, h in card_h) + 10
        col_h = max(col_h, content_bottom - ty)
        S.add(f'<rect x="{rx - 10}" y="{ty}" width="{rwid + 10}" height="{col_h:.1f}" rx="6" fill="#fff" '
              f'stroke="{C_TAGS}" stroke-dasharray="4,3"/>')
        S.text(rx + rwid / 2 - 5, ty + 26, hdr[0], 13, weight="bold")
        if hdr[1]:
            S.text(rx + rwid / 2 - 5, ty + 44, hdr[1], 11, color="#444")
        for i, line in enumerate(note):
            S.text(rx + rwid / 2 - 5, ty + 74 + i * 15, line, 11, color="#2f4a26")
        for ls, h in card_h:
            S.add(f'<rect x="{rx + 5}" y="{cy:.1f}" width="{rwid - 20}" height="{h}" rx="4" fill="{C_TAG}" stroke="{C_TAGS}"/>')
            S.text(rx + 17, cy + 20, ellipsize(ls[0], 44), 12, "start", "bold")
            for i, line in enumerate(ls[1:]):
                S.text(rx + 17, cy + 38 + 17 * i, line, 10.5, "start", color="#333")
            cy += h + 10
        col_bottom = ty + col_h
        W = rx + rwid + 20

    # ---------- legend & footer ----------
    leg2 = "child run started by the parent run (wasStartedBy); nested document linked by prov:has_provenance"
    leg3 = ("data flow between steps (generated by one step, used by the next, incl. collection members): "
            "output → input · count")
    W = max(W, 440 + text_width(leg2, 11) + 40, 440 + text_width(leg3, 11) + 40 if data_edges else 0)
    ly = max(content_bottom, col_bottom) + 16
    foot = wrap_text(footer_text(model, title), W - 72, 10.5)
    lh = 76 + 20 * (bool(data_edges) + (params != "none") + has_prof) + 15 * len(foot) + 8
    S.add(f'<rect x="20" y="{ly:.1f}" width="{W - 40}" height="{lh}" rx="6" fill="#fff" stroke="{C_BANDS}"/>')
    S.text(36, ly + 22, "Legend", 12, "start", "bold")
    S.node(40, ly + 36, 90, 30, "act", ["activity"], 11)
    S.node(150, ly + 36, 90, 30, "ent", ["entity"], 11)
    S.node(260, ly + 32, 90, 36, "agt", ["agent"], 11)
    S.path(f"M380,{ly + 44:.1f} L430,{ly + 44:.1f}")
    S.text(440, ly + 48, "PROV relation (PROV direction); between agents: actedOnBehalfOf", 11, "start")
    S.path(f"M380,{ly + 64:.1f} L430,{ly + 64:.1f}", dashed=True)
    S.text(440, ly + 68, leg2, 11, "start")
    yy = ly + 88
    if data_edges:
        S.add(f'<path d="M380,{yy - 4:.1f} L430,{yy - 4:.1f}" stroke="{C_DATA}" stroke-width="2.2" marker-end="url(#dh)"/>')
        S.text(440, yy, "data flow between steps (generated by one step, used by the next, incl. collection members): "
               "output → input · count", 11, "start")
        yy += 20
    if params != "none":
        S.text(440, yy, "params: … inside a step box = inputs passed from the parent run (∈ = member of the parent's array)",
               11, "start")
        yy += 20
    if has_prof:
        S.add(f'<rect x="380" y="{yy - 12:.1f}" width="70" height="16" rx="3" fill="{C_TAG}" stroke="{C_TAGS}"/>')
        S.text(415, yy, "≙ name", 10.5, color="#2f4a26")
        S.text(460, yy, "corresponding process profile (from the --profiles mapping)", 11, "start")
        yy += 20
    for i, line in enumerate(foot):
        S.text(36, yy + 4 + 15 * i, line, 10.5, "start", color="#555")
    H = yy + 4 + 15 * len(foot) + 16

    # ---------- assemble ----------
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}">',
           f"<title>{xml_escape(title or ('Provenance of job ' + j.id if j else 'Provenance'))}</title>",
           '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
           'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#444"/></marker>'
           f'<marker id="dh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
           f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{C_DATA}"/></marker></defs>',
           f'<rect width="{W:.0f}" height="{H:.0f}" fill="#fff"/>']
    if title:
        out.append(f'<text x="20" y="38" {FONT} font-size="17" font-weight="bold" fill="#222">{xml_escape(title)}</text>')
    for by, bh, _ in band_rects:
        out.append(f'<rect x="{BAND_X}" y="{by:.1f}" width="{BAND_W:.1f}" height="{bh:.1f}" rx="6" '
                   f'fill="{C_BAND}" stroke="{C_BANDS}"/>')
    out += S.out
    out.append("</svg>")
    return "\n".join(out)


def ellipsize_doc(name: str) -> str:
    """``workflow_20app.9c4f8bbe-d4e0-….cwlprov`` -> ``workflow_20app.9c4f8bbe-….cwlprov``."""
    return re.sub(r"\.([0-9a-f]{8})-[0-9a-f-]{27}\.", r".\1-….", name)


def wrap_text(s: str, width: float, size: float) -> list[str]:
    """Greedy word wrap using :func:`text_width`."""
    lines, cur = [], ""
    for w in s.split():
        cand = (cur + " " + w).strip()
        if cur and text_width(cand, size) > width:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return lines


def is_ent(key: str) -> bool:
    """Layout keys of entity boxes (final outputs and intermediate flow entities)."""
    return key.startswith(("out:", "ent:"))


def flow_entity_lines(fe: FlowEntity, model: Model) -> list[str]:
    """Lines of an intermediate data entity (e.g. the local STAC catalog produced by the Application)."""
    apps = {s.name for r in model.runs for s in r.steps if s.kind == "application"}
    ret = [x.split(": ", 1) for x in fe.returned_as]
    by_app = [r for r in ret if r[0] in apps]
    role = by_app[0][1] if by_app else (ret[0][1] if ret else fe.title)
    what = "local STAC catalog" if "catalog.json" in fe.members else {"directory": "folder", "file": "file",
                                                                      "collection": "collection"}.get(fe.kind, "data")
    lines = ["data produced by the Application" if by_app else "intermediate data",
             f"output {role} · {what}" if by_app else f"{role} · {what}"]
    lines.append(ellipsize((f"{fe.kind}: " if fe.kind in ("directory", "collection") else "") + fe.summary, 46))
    prod = ", ".join(sorted({p.split("|")[-1] for p in fe.produced_by}))
    used = ", ".join(sorted({u.split("|")[-1] for u in fe.used_by}))
    lines.append(ellipsize(f"generated by {prod} · used by {used}", 50))
    return lines


def draw_flow(S: Svg, placed: dict[str, Box], meta: dict[str, tuple[list[str], str | None, Step | None]]) -> None:
    """Draw the step activities and output entities of a row layout."""
    for key, b in placed.items():
        ls, tag, st = meta[key]
        S.node(b.x, b.y, b.w, b.h, "ent" if is_ent(key) else "act", ls, 11 if is_ent(key) else 11.5, tag=tag)


def hierarchy(S: Svg, parent: Box, first_row: list[Box], bus_y: float, rows: list[list[str]],
              placed: dict[str, Box], gutter: float, cross: bool = False) -> None:
    """Dashed parent -> children connectors (bus per row, gutter lane between wrapped rows)."""
    kids_rows = [[placed[k] for k in row if not is_ent(k)] for row in rows]
    kids_rows = [r for r in kids_rows if r]
    if not kids_rows:
        return
    px = parent.cx if not cross else min(parent.cx, parent.x + 60)
    first = kids_rows[0]
    xs = [b.cx for b in first]
    if len(first) == 1 and abs(first[0].cx - px) < 1:
        S.path(f"M{px:.1f},{parent.bottom:.1f} L{px:.1f},{first[0].y - 2:.1f}", dashed=True)
    else:
        S.path(f"M{px:.1f},{parent.bottom:.1f} L{px:.1f},{bus_y:.1f}", dashed=True, head=False)
        lo, hi = min(xs + [px]), max(xs + [px])
        S.path(f"M{lo:.1f},{bus_y:.1f} L{hi:.1f},{bus_y:.1f}", dashed=True, head=False)
        for b in first:
            S.path(f"M{b.cx:.1f},{bus_y:.1f} L{b.cx:.1f},{b.y - 2:.1f}", dashed=True)
    for row in kids_rows[1:]:
        ry = row[0].y - 12
        S.path(f"M{min(xs + [px]):.1f},{bus_y:.1f} L{gutter:.1f},{bus_y:.1f} L{gutter:.1f},{ry:.1f} "
               f"L{max(b.cx for b in row):.1f},{ry:.1f}", dashed=True, head=False)
        for b in row:
            S.path(f"M{b.cx:.1f},{ry:.1f} L{b.cx:.1f},{b.y - 2:.1f}", dashed=True)


def order_agents(model: Model) -> list[AgentInfo]:
    """Agents ordered along the delegation tree (responsible first, delegates to its right)."""
    by_id = {a.id: a for a in model.agents}
    kids: dict[str, list[str]] = {}
    has_resp = set()
    for d in model.delegations:
        if d.delegate in by_id and d.responsible in by_id:
            kids.setdefault(d.responsible, []).append(d.delegate)
            has_resp.add(d.delegate)
    rank = {"server": 0, "component": 1, "software": 2, "account": 3, "engine": 4}
    roots = sorted([a for a in model.agents if a.id not in has_resp], key=lambda a: (rank.get(a.kind, 5), a.name))
    out: list[AgentInfo] = []

    def visit(a: AgentInfo) -> None:
        if a in out:
            return
        out.append(a)
        for k in sorted(kids.get(a.id, []), key=lambda i: (rank.get(by_id[i].kind, 5), by_id[i].name)):
            visit(by_id[k])

    for r in roots:
        visit(r)
    for a in model.agents:
        visit(a)
    return out


# --------------------------------------------------------------------------
# DOT renderer
# --------------------------------------------------------------------------
def _h(s: str) -> str:
    """Escape for Graphviz HTML-like labels."""
    return xml_escape(s)


def _html_label(lines: list[str], tag: str | None = None, left: bool = False) -> str:
    if left:
        return "<" + f"<b>{_h(lines[0])}</b><br/>" + "".join(f'{_h(x)}<br align="left"/>' for x in lines[1:]) + ">"
    rows = [f"<b>{_h(lines[0])}</b>"] + [_h(x) for x in lines[1:]]
    lab = "<br/>".join(rows)
    if tag:
        return (f'<<table border="0" cellborder="0" cellspacing="2"><tr><td>{lab}</td></tr>'
                f'<tr><td bgcolor="{C_TAG}" color="{C_TAGS}" border="1"><font point-size="9" color="#2f4a26">'
                f'≙ {_h(tag)}</font></td></tr></table>>')
    return f"<{lab}>"


def render_dot(model: Model, title: str | None = None, dataflow: bool = True, params: str = "summary") -> str:
    """Render the model as Graphviz DOT, one cluster per provenance document."""
    has_prof = bool(model.profiles)
    j = model.job
    L = ["digraph prov {", '  graph [rankdir=TB, fontname="Helvetica", fontsize=11, nodesep=0.35, ranksep=0.45, '
         'newrank=true, bgcolor="white"' + (f', label=<<b>{_h(title)}</b>>, labelloc=t' if title else "") + "];",
         '  node [fontname="Helvetica", fontsize=10, style=filled, color="#555555"];',
         '  edge [fontname="Helvetica", fontsize=9, color="#444444", fontcolor="#444444"];']
    act = 'shape=box, fillcolor="' + C_ACT + '"'
    ent = 'shape=box, style="rounded,filled", fillcolor="' + C_ENT + '"'
    agt = 'shape=house, fillcolor="' + C_AGT + '"'
    nid = lambda s: '"' + re.sub(r"[^A-Za-z0-9_]", "_", s) + '"'  # noqa: E731
    for i, d in enumerate(model.documents):
        L.append(f"  subgraph cluster_{i} {{")
        sub = f"GET {d.api_path} — {doc_role(model, d)}"
        if d.merged_from:
            sub += "<br/>merged with " + ", ".join(_h(ellipsize_doc(m)) for m in d.merged_from)
        L.append(f'    label=<<b>{_h(ellipsize_doc(d.name))}</b><br/><font point-size="9">{_h(sub) if not d.merged_from else sub}</font>>; '
                 f'labeljust=r; style="rounded,filled"; fillcolor="{C_BAND}"; color="{C_BANDS}";')
        run = next((r for r in model.runs if r.doc == d.name), None)
        if i == 0:
            for a in order_agents(model):
                ls = [a.name] + ([a.version] if a.version else []) + (["user account"] if a.kind == "account" else [])
                L.append(f"    {nid('ag_' + a.id)} [{agt}, label={_html_label(ls)}];")
            L.append("    { rank=same; " + " ".join(nid("ag_" + a.id) for a in model.agents) + " }")
            if j:
                L.append(f"    {nid('job')} [{act}, label={_html_label([f'Job {ellipsize_id(j.id)}', 'wfprov:ProcessRun', (hhmmss(j.start) + '–' + hhmmss(j.end) + ' UTC') if j.start else ''])}];")
                L.append(f"    {nid('jobent')} [{ent}, label={_html_label(['job entity', '/jobs/' + ellipsize_id(j.id)])}];")
                L.append(f"    {nid('plan')} [{ent}, label={_html_label(['process (plan)', '/processes/' + str(j.process_id)])}];")
                L.append(f"    {{ rank=same; {nid('job')} {nid('jobent')} {nid('plan')} }}")
            if run:
                L.append(f"    {nid('run')} [{act}, label={_html_label(['Wrapping workflow run', 'wfprov:WorkflowRun · cwltool'])}];")
                ins = ["inputs (prov:role = prov:value)"] + input_lines(model)
                L.append(f"    {nid('inputs')} [{ent}, label={_html_label(ins, left=True)}];")
                L.append(f"    {{ rank=same; {nid('run')} {nid('inputs')} }}")
                plat = {s.name for s in run.steps if s.kind == "platform"}
                for k, o in enumerate(model.outputs):
                    L.append(f"    {nid(f'out{k}')} [{ent}, label={_html_label(output_lines(o, bool(set(o.generated_by) & plat)))}];")
        if run:
            for st in run.steps:
                tag = st.profile_short if has_prof and st.profile_matched else None
                ls = step_lines(st, run, i == 0) + param_lines(model, f"{run.doc}|{st.name}", params)
                L.append(f"    {nid('st_' + run.doc + st.name)} [{act}, label={_html_label(ls, tag)}];")
            for fe in {fe.id: fe for f in model.flows for fe in f.entities}.values():
                if fe.produced_by and fe.produced_by[0].split("|")[0] == d.name:
                    L.append(f"    {nid('fe_' + fe.id)} [{ent}, label={_html_label(flow_entity_lines(fe, model))}];")
        L.append("  }")
    # edges
    if j:
        srv = next((a for a in model.agents if a.kind == "server"), None)
        if srv:
            # edges written parent->child with dir=back keep agents on top while arrows follow PROV direction
            L.append(f"  {nid('ag_' + srv.id)} -> {nid('job')} [label=wasAssociatedWith, dir=back];")
        L.append(f"  {nid('job')} -> {nid('jobent')} [label=wasGeneratedBy, dir=back];")
        L.append(f'  {nid("job")} -> {nid("plan")} [label="wasAssociatedWith (hadPlan)"];')
        if model.runs:
            L.append(f"  {nid('job')} -> {nid('run')} [label=wasInformedBy, dir=back];")
    ids = {a.id for a in model.agents}
    for d in model.delegations:
        if d.delegate in ids and d.responsible in ids:
            L.append(f"  {nid('ag_' + d.delegate)} -> {nid('ag_' + d.responsible)} [label=actedOnBehalfOf, constraint=false];")
    if model.runs:
        top = model.runs[0]
        L.append(f"  {nid('run')} -> {nid('inputs')} [label=used];")
        for st in top.steps:
            L.append(f"  {nid('run')} -> {nid('st_' + top.doc + st.name)} [style=dashed];")
        for k, o in enumerate(model.outputs):
            for gname in o.generated_by[:1]:
                L.append(f"  {nid('st_' + top.doc + gname)} -> {nid(f'out{k}')} [label=wasGeneratedBy, dir=back];")
                L.append(f"  {{ rank=same; {nid('st_' + top.doc + gname)} {nid(f'out{k}')} }}")
        for k, o in enumerate(model.outputs):
            L.append(f'  {nid(f"out{k}")} -> {nid("run")} [label="wasGeneratedBy (output {o.name} of the wrapping run)", '
                     "constraint=false];")
        for r in model.runs[1:]:
            d = next(dd for dd in model.documents if dd.name == r.doc)
            parent = nid("st_" + str(d.parent_doc) + str(d.parent_step))
            for st in r.steps:
                L.append(f"  {parent} -> {nid('st_' + r.doc + st.name)} [style=dashed];")
        # step-to-step data flow (same edges as the SVG)
        if dataflow:
            for e in model.dataflow:
                if e.kind != "data" or e.drawn_as_entity:
                    continue
                a = nid("st_" + e.source.replace("|", "")) if e.source != "run" else nid("run")
                b = nid("st_" + e.target.replace("|", ""))
                same = e.source.split("|")[0] == e.target.split("|")[0]
                L.append(f'  {a} -> {b} [label="{_dot_str(data_label(e))}", color="{C_DATA}", fontcolor="{C_DATA}", '
                         f'penwidth=2.2, constraint={"true" if same else "false"}];')
        # output data flow (entities joined across documents by IRI)
        done = set()
        for f in model.flows:
            for ln in f.links:
                if ln.entity == f.entity or (ln.relation, ln.entity, ln.step) in done:
                    continue
                done.add((ln.relation, ln.entity, ln.step))
                stn = nid("run") if ln.step == "run" else nid("st_" + ln.step.replace("|", ""))
                fen = nid("fe_" + ln.entity)
                if ln.relation == "used":
                    L.append(f'  {stn} -> {fen} [label="used ({local_name(ln.role)})"];')
                elif ln.level == "step":
                    L.append(f"  {stn} -> {fen} [label=wasGeneratedBy, dir=back];")
                else:
                    L.append(f'  {fen} -> {stn} [label="wasGeneratedBy (output {local_name(ln.role)})", style=dotted, '
                             "constraint=false];")
    if has_prof:
        L.append("  subgraph cluster_profiles {")
        L.append(f'    label=<<b>{_h(model.profiles_title or "Process profiles")}</b><br/><font point-size="9">'
                 f'{_h(model.profiles_subtitle or "")}<br/>≙ mapping supplied with --profiles</font>>; '
                 f'style="dashed"; color="{C_TAGS}";')
        for k, c in enumerate(model.profiles):
            ls = card_lines(c, 300)
            L.append(f'    {nid(f"prof{k}")} [shape=box, style="rounded,filled", fillcolor="{C_TAG}", color="{C_TAGS}", '
                     f"label={_html_label(ls)}];")
        for k in range(len(model.profiles) - 1):
            L.append(f'    {nid(f"prof{k}")} -> {nid(f"prof{k + 1}")} [style=invis];')
        L.append("  }")
    L.append(f'  footer [shape=plaintext, style="", fontsize=9, fontcolor="#555555", label="{_dot_str(footer_text(model, title))}"];')
    last = model.runs[-1] if model.runs else None
    if last and last.steps:
        L.append(f"  {nid('st_' + last.doc + last.steps[0].name)} -> footer [style=invis];")
    L.append("}")
    return "\n".join(L)


def _dot_str(s: str) -> str:
    """Quote and wrap a plain DOT string."""
    return "\\n".join(wrap_text(s, 900, 9)).replace('"', '\\"')


# --------------------------------------------------------------------------
# Self-test (secret leak check)
# --------------------------------------------------------------------------
def collect_secrets(src: Source) -> set[str]:
    """Known secret strings of a research object: values bound to secret roles/keys, in-cluster endpoints."""
    ex = Extractor(src)
    ex._load_documents()
    ex._taint_pass()
    secrets = set(ex.red.tainted)
    for g in ex.graphs.values():
        for o in g.objects(None, PROV.value):
            if ENDPOINT_RE.search(str(o)):
                secrets.add(str(o).strip())
                m = re.search(r"[\w.-]+\.svc\.cluster\.local", str(o))
                if m:
                    secrets.add(m.group(0))
    return {s for s in secrets if len(s.strip()) >= 3}


def self_test(bags: list[Path], scan: list[Path], profiles: Path | None) -> int:
    """Run the tool on each bag (all formats) and grep every output and log for the bag's secrets."""
    failures = 0
    for bag in bags:
        src = locate(bag)
        label = bag.parent.name if bag.name in ("prov", "") else bag.name
        secrets = collect_secrets(src)
        role_secret_count = 0
        for f in src.prov_dir.glob("*.ttl"):
            role_secret_count += len(re.findall(r"(?i)(SECRET|PASSWORD|TOKEN|ACCESS_KEY)", f.read_text()))
        if role_secret_count and not secrets:
            print(f"FAIL {label}: secret roles present but no secret value collected")
            failures += 1
            continue
        # negative control: the detector must see the secrets in the raw primary document
        raw = src.primary.read_bytes()
        if secrets and not any(x.encode() in raw for x in secrets):
            print(f"FAIL {label}: control check - no known secret found in the raw primary document")
            failures += 1
            continue
        with tempfile.TemporaryDirectory(prefix="prov_synth_test_") as td:
            buf = io.StringIO()
            outs = []
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                for fmt, name in (("svg", "t.svg"), ("dot", "t.dot.svg")):
                    argv = [str(bag), "-o", str(Path(td) / name), "--format", fmt, "--json", str(Path(td) / f"{fmt}.json"),
                            "--show-platform-params", "-v"]
                    if profiles:
                        argv += ["--profiles", str(profiles)]
                    main(argv)
            outs = [p for p in Path(td).iterdir() if p.is_file()]
            texts = {str(p.name): p.read_bytes() for p in outs}
            texts["<stdout/stderr>"] = buf.getvalue().encode()
            for d in scan:
                for p in (d.rglob("*") if d.is_dir() else [d]):
                    if p.is_file():
                        texts[str(p)] = p.read_bytes()
            if not any(REDACTED.encode() in data for data in texts.values()):
                print(f"FAIL {label}: no [redacted] marker in any output (redaction did not run)")
                failures += 1
            leaks = [(name, hashlib.sha256(s.encode()).hexdigest()[:10])
                     for name, data in texts.items() for s in secrets if s.encode() in data]
            if leaks:
                failures += 1
                for name, h in leaks:
                    print(f"FAIL {label}: secret sha256:{h} found in {name}")
            else:
                print(f"PASS {label}: {len(secrets)} known secret strings "
                      f"({', '.join('sha256:' + hashlib.sha256(s.encode()).hexdigest()[:10] for s in sorted(secrets))}) "
                      f"absent from {len(texts)} outputs/logs")
        if src.tmp:
            src.tmp.cleanup()
    return 1 if failures else 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def build_model(path: Path, show_platform: bool = False, profiles: Path | None = None) -> Model:
    """Locate, load and extract a model from a bag / zip / directory."""
    src = locate(path)
    try:
        model = Extractor(src, show_platform=show_platform).build()
    finally:
        if src.tmp:
            src.tmp.cleanup()
    if profiles:
        apply_profiles(model, profiles)
    return model


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point."""
    ap = argparse.ArgumentParser(prog="prov_synth", description=__doc__.split("\n\n")[0])
    ap.add_argument("source", nargs="*", type=Path, help="bag directory, .zip of it, or directory of *.cwlprov.ttl")
    ap.add_argument("-o", "--output", type=Path, help="output file (.svg, or .dot for DOT source only)")
    ap.add_argument("--format", choices=["svg", "dot"], default="svg")
    ap.add_argument("--profiles", type=Path, help="YAML mapping of steps (or container images) to process profiles")
    ap.add_argument("--json", type=Path, help="also write the intermediate model as JSON")
    ap.add_argument("--title", help="diagram title")
    ap.add_argument("--no-dataflow", action="store_true", help="do not draw step-to-step data-flow edges")
    ap.add_argument("--params", choices=["none", "summary", "full"], default="summary",
                    help="parameter passing from parent runs to steps (default: summary)")
    ap.add_argument("--show-platform-params", action="store_true",
                    help="include STAGEIN_*/STAGEOUT_*/process inputs (still redacted)")
    ap.add_argument("--self-test", action="store_true",
                    help="run on each SOURCE and fail if any known secret string appears in outputs/logs")
    ap.add_argument("--scan", type=Path, action="append", default=[],
                    help="with --self-test: extra files/directories to grep for secrets")
    ap.add_argument("-v", "--verbose", action="store_true", help="print a summary and notes to stderr")
    a = ap.parse_args(argv)
    if a.self_test:
        if not a.source:
            ap.error("--self-test needs at least one SOURCE")
        return self_test(a.source, a.scan, a.profiles)
    if len(a.source) != 1 or not a.output:
        ap.error("exactly one SOURCE and -o OUTPUT are required")
    model = build_model(a.source[0], a.show_platform_params, a.profiles)
    if a.json:
        a.json.parent.mkdir(parents=True, exist_ok=True)
        a.json.write_text(json.dumps(asdict(model), indent=2, ensure_ascii=False) + "\n")
    a.output.parent.mkdir(parents=True, exist_ok=True)
    if a.format == "svg":
        a.output.write_text(render_svg(model, a.title, not a.no_dataflow, a.params))
    else:
        dot = render_dot(model, a.title, not a.no_dataflow, a.params)
        if a.output.suffix == ".dot":
            a.output.write_text(dot)
        else:
            src_path = a.output.with_name(re.sub(r"(\.dot)?\.svg$", "", a.output.name) + ".dot")
            src_path.write_text(dot)
            exe = shutil.which("dot")
            if not exe:
                print(f"prov_synth: 'dot' not found; DOT source written to {src_path}", file=sys.stderr)
                return 2
            subprocess.run([exe, "-Tsvg", str(src_path), "-o", str(a.output)], check=True)
    if a.verbose:
        n_steps = sum(len(r.steps) for r in model.runs)
        print(f"prov_synth: {len(model.documents)} documents, {len(model.runs)} runs, {n_steps} step groups, "
              f"{len(model.inputs)} inputs shown ({model.platform_params_hidden} platform hidden), "
              f"{model.redactions} values redacted -> {a.output}", file=sys.stderr)
        for n in model.notes:
            print(f"  note: {n}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
