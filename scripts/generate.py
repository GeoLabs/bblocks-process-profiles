#!/usr/bin/env python3
"""Generate the process-profile Building Blocks of bblocks-process-profiles.

Semi-automated pipeline (Step 3):
  1. read each CWL process from a local clone of its pinned source (never downloaded here);
  2. isolate it (packed $graph elements inherit the document-level keys, see docs/DEVIATIONS.md M-03);
  3. apply the eoap.cct.cwl-to-ogcprocess jq transform (unchanged, from a local clone of bblocks-eoap-cct);
  4. apply the documented manual corrections (M-01, M-02, M-04) and keep the raw output next to them;
  5. template the provenance view, process-type entry, openEO links, execution examples and docs
     from scripts/profiles.yaml (the Step 0 table) and from real `cwltool --provenance` run records
     (scripts/sources.yaml `runs:`, local research objects, never downloaded).

Usage:
  python3 scripts/generate.py --sources-root DIR [--w1 DIR] [--w2 DIR]

DIR must contain clones named as in scripts/sources.yaml (`clone:`), or pass --w1/--w2 explicitly.
Generated files under _sources/<workflow>/<process>/ are overwritten.
"""
import argparse
import copy
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
BASE = "https://geolabs.github.io/bblocks-process-profiles/def/"
PTYPE_SCHEME = BASE + "process-type"
PROCESS_TYPE_REGISTER = BASE + "register"
GEOLABS_AGENT = BASE + "geolabs"
# Activity Type Register (ATR) terms. This is the only place that spells the ATR item class IRI:
# upstream branch `model-tweaks` renames it to ActivityTypeItemClass. Entries take it from here
# and sync_process_type_schema() writes it into _sources/process-type/schema.yaml.
ACTTYPE_NS = "https://w3id.org/ogc/rim/activity-type/"
ATR_ITEM_CLASS = ACTTYPE_NS + "activityTypeItemClass"
ACTIVITY_TYPE_CLASS = ACTTYPE_NS + "ActivityType"
GEOPROC_CLASS = "https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType"
# The action type of an in-place change to a proposal, defined by this register's specification
# (pp:specification, _sources/process-type/ontology.ttl), as gp:, dt: and df: define theirs.
AMENDMENT_ACTION = BASE + "amendmentAction"
PHASE_BASE = BASE + "phase/"
BBLOCK_IRI = "https://www.opengis.net/def/bblocks/"
PREFIX = "ospd.process-profiles."
TODAY = "2026-09-22"
PART1_CORE = "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core"
GENERIC_PROFILES_BASE = "https://geolabs.github.io/bblocks-generic-profiles/def/"
DATA_TYPES_BASE = "https://geolabs.github.io/bblocks-data-types/def/data-type/"
DATA_FORMATS_BASE = "https://w3id.org/geolabs-ospd/data-formats/"

# The two populations of this register (A4.5): the deployable CWL processes of the OSPD reference
# workflows (`processes` in profiles.yaml) and the live processes of the Geonovum testbed
# (`ogcapi_processes`). Checked at generation, so that a change in either is seen.
POPULATIONS = {"cwl": 27, "live": 31}
WORKFLOW_LABELS = {"algae-bloom": "W1 Algae Bloom", "kindgrove": "W2 KindGrove",
                   "water-bodies": "W3 Water Bodies", "kindgrove-steps": "W2b KindGrove (step notebooks)"}

PHASE_LABELS = {
    "filter-configuration": "Filter configuration",
    "selection-filtering": "Selection / filtering",
    "data-retrieval": "Data retrieval",
    "pre-processing": "Pre-processing",
    "scientific-computation": "Scientific computation",
    "export-aggregation": "Export / aggregation",
}

# CWL `format` IRIs (after namespace expansion) -> media types (M-01)
FORMAT_MEDIA = {
    "http://www.opengis.net/def/media-type/ogc/1.0/geotiff": "image/tiff; application=geotiff",
    "https://www.iana.org/assignments/media-types/image/tiff": "image/tiff",
    "https://www.iana.org/assignments/media-types/image/jp2": "image/jp2",
    "https://www.iana.org/assignments/media-types/image/png": "image/png",
    "https://www.iana.org/assignments/media-types/application/geo+json": "application/geo+json",
}


PROCESS_BASE = BASE + "process/"

# JSON-LD context written next to every profile Building Block (context.jsonld).
#
# Without one, bblocks-postprocess derives a context from the annotated schema alone. The
# OGC API - Processes schemas carry almost no x-jsonld-* annotations, so that derived context
# binds none of the properties the examples actually use, every snippet uplifts to an empty
# RDF graph, and the validator reports each one as an error ("**Empty** output Turtle", which
# is hard-coded as is_error and cannot be switched off).
#
# Terms that match no schema property are still emitted, as x-jsonld-extra-terms, so this one
# context also covers the payloads that only exist under $defs: ogcapppkg, execute, results,
# provenance, process-run and process-type.
#
# @vocab is not optional here: the keys of results.json are the process's own output names and
# cannot be enumerated up front. It is re-scoped under inputs/outputs/usedInput so that an
# arbitrary CWL parameter name -- an input literally called `name`, for instance -- cannot be
# captured by a vocabulary term.
PROFILE_CONTEXT = {
    "@context": {
        "@version": 1.1,
        "@vocab": BASE,
        "pp": BASE,
        "proc": "https://w3id.org/ogc/api/processes/",
        "prov": "http://www.w3.org/ns/prov#",
        "dct": "http://purl.org/dc/terms/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "wfprov": "http://purl.org/wf4ever/wfprov#",
        "oa": "http://www.w3.org/ns/oa#",
        "rim": "https://w3id.org/ogc/rim/",
        "acttype": ACTTYPE_NS,
        "owl": "http://www.w3.org/2002/07/owl#",

        "id": "@id",
        # `type` must be claimed here: the inherited /links/type binding (proc:type) is
        # otherwise hoisted to the root and turns every `type` into a literal. Scoping
        # `links` below (as the upstream provenance contexts do) frees the root term.
        "type": "@type",
        "ProcessRun": "wfprov:ProcessRun",
        "WorkflowRun": "wfprov:WorkflowRun",
        "WorkflowEngine": "wfprov:WorkflowEngine",
        "Artifact": "wfprov:Artifact",
        "ProcessType": "pp:ProcessType",
        "ActivityType": "acttype:ActivityType",
        "owlClass": "owl:Class",
        "subClassOf": {"@id": "rdfs:subClassOf", "@type": "@id"},

        # processDescription (OGC API - Processes Part 1)
        "title": "dct:title",
        "description": "dct:description",
        "keywords": "dct:subject",
        "version": "pp:version",
        "mutable": "proc:mutable",
        "jobControlOptions": "proc:jobControlOptions",
        "minOccurs": "proc:minOccurs",
        "maxOccurs": "proc:maxOccurs",
        "outputTransmission": "proc:outputTransmission",
        "metadata": {"@id": "proc:metadata", "@context": {
            "href": {"@id": "proc:href", "@type": "@id"}}},
        "role": {"@id": "proc:role", "@type": "@id"},
        # The data type of a tier-4 input or output (A4.2), a dt:DataType concept of
        # bblocks-data-types, inherited from the Implementation Profile role it is bound to. Same
        # term and property (dct:type) as tiers 2 and 3 in bblocks-generic-profiles.
        "dataType": {"@id": "dct:type", "@type": "@id"},
        # Entity types of a process type that specialises a geoprocessing activity type (the same
        # GeoSPARQL classes as that activity type), and the classification of an amendment.
        "usedEntityType": {"@id": "acttype:usedEntityType", "@type": "@id"},
        "generatedEntityType": {"@id": "acttype:generatedEntityType", "@type": "@id"},
        "changeClassification": {"@id": "rim:changeClassification", "@type": "@vocab"},
        "substantive": "rim:substantiveChange",
        "clarifying": "rim:clarifyingChange",
        "inputs": {"@id": "proc:inputs", "@context": {"@vocab": BASE + "input/"}},
        "outputs": {"@id": "proc:outputs", "@context": {"@vocab": BASE + "output/"}},
        "links": {"@id": "rdfs:seeAlso", "@context": {
            "href": {"@id": "oa:hasTarget", "@type": "@id"},
            "rel": {"@id": "http://www.iana.org/assignments/relation", "@type": "@id",
                    "@context": {"@base": "http://www.iana.org/assignments/relation/"}},
            "type": "dct:type", "title": "rdfs:label"}},
        "response": "proc:response",

        # ogcapppkg (Part 2) / results / execution bundle. `executionUnit` is a link: scoped like
        # `links`, or its media type lands on the root `type` (@type) and becomes a class.
        "executionUnit": {"@id": "proc:executionUnit", "@context": {
            "href": {"@id": "oa:hasTarget", "@type": "@id"},
            "rel": {"@id": "http://www.iana.org/assignments/relation", "@type": "@id",
                    "@context": {"@base": "http://www.iana.org/assignments/relation/"}},
            "type": "dct:format"}},
        "processDescription": {"@id": "pp:processDescription", "@context": {
            "href": {"@id": "rdfs:seeAlso", "@type": "@id"},
            "license": {"@id": "dct:license", "@type": "@id"}}},
        "result": "pp:result",
        "engine": "pp:engine",
        "run": "pp:run",

        # provenance view (W3C PROV) -- same bindings as ogc.bbr.provenance.provenance:
        # activityType / entityType are rdf:types, not pp: properties
        "provType": {"@id": "@type", "@type": "@vocab"},
        "provName": "rdfs:label",
        "activityType": {"@id": "@type", "@type": "@id"},
        "entityType": {"@id": "@type", "@type": "@id"},
        "used": {"@id": "prov:used", "@type": "@id"},
        "wasAssociatedWith": {"@id": "prov:wasAssociatedWith", "@type": "@id"},
        "wasGeneratedBy": {"@id": "prov:wasGeneratedBy", "@type": "@id"},
        "wasDerivedFrom": {"@id": "prov:wasDerivedFrom", "@type": "@id"},
        "wasAttributedTo": {"@id": "prov:wasAttributedTo", "@type": "@id"},
        "qualifiedAssociation": {"@id": "prov:qualifiedAssociation"},
        "agent": {"@id": "prov:agent", "@type": "@id"},
        "hadPlan": {"@id": "prov:hadPlan", "@type": "@id"},
        "specializationOf": {"@id": "prov:specializationOf", "@type": "@id"},
        "startedAtTime": {"@id": "prov:startedAtTime", "@type": "xsd:dateTime"},
        "endedAtTime": {"@id": "prov:endedAtTime", "@type": "xsd:dateTime"},
        "value": "rdf:value",

        # process run / execution bundle -- same bindings as the Wf4Ever bblocks
        # (ogc.bbr.wf4ever.wfprov.ProcessRun / WorkflowRun) and ogc.bbr.provenance.execution
        "describedByProcess": {"@id": "wfprov:describedByProcess", "@type": "@id"},
        "describedByWorkflow": {"@id": "wfprov:describedByWorkflow", "@type": "@id"},
        "usedInput": {"@id": "wfprov:usedInput", "@type": "@id"},
        "wasEnactedBy": {"@id": "prov:wasAssociatedWith", "@type": "@id"},
        "wasPartOfWorkflowRun": {"@id": "wfprov:wasPartOfWorkflowRun", "@type": "@id"},
        "hadSubProcessRun": {"@id": "wfprov:hadSubProcessRun", "@type": "@id"},
        "wasOutputFrom": {"@id": "prov:generated", "@type": "@id"},

        # process-type register entry (mirrors _sources/process-type/context.jsonld)
        "objectIdentifier": {"@id": "rim:objectIdentifier", "@type": "xsd:anyURI"},
        "itemClass": {"@id": "rim:itemClass", "@type": "@id"},
        "inRegister": {"@id": "rim:inRegister", "@type": "@id"},
        "validityStatus": {"@id": "rim:validityStatus", "@type": "@vocab"},
        "publicationStatus": {"@id": "rim:publicationStatus", "@type": "@vocab"},
        "invalid": "rim:invalid",
        "published": "rim:published",
        "hasAction": {"@id": "rim:hasAction", "@type": "@id"},
        "RegisterAction": "rim:RegisterAction",
        "actionType": {"@id": "rim:actionType", "@type": "@vocab"},
        "addition": "rim:additionAction",
        "proposer": {"@id": "rim:proposer", "@type": "@id"},
        "appliesTo": {"@id": "rim:appliesTo", "@type": "@id"},
        "prefLabel": "skos:prefLabel",
        "definition": "skos:definition",
        "inScheme": {"@id": "skos:inScheme", "@type": "@id"},
        "status": "pp:status",
        # Decision D5: the entry separates the meaning of the type (prefLabel, definition,
        # subClassOf) from its classification, its deployment, its plan and its correspondences.
        # `classification` and `correspondences` only group keys in the JSON (@nest): their
        # statements stay on the type. `phase` is a classification (pp:phase), no longer
        # skos:broader, which made the six phases broader concepts of the type. `deployment` is a
        # node of its own: what is deployed, not what the type means.
        "classification": "@nest",
        "correspondences": "@nest",
        "phase": {"@id": "pp:phase", "@type": "@id"},
        "deployment": {"@id": "pp:deployment"},
        "profile": "pp:profile",
        # The plan (prov:Plan) is the Application Package at /processes/{id}/package, kept apart
        # from the type itself; the same IRI is each run's `hadPlan`.
        "plan": {"@id": "pp:plan", "@context": {
            "license": {"@id": "dct:license", "@type": "@id"}}},
        "Plan": "prov:Plan",
        "cwlClass": "pp:cwlClass",
        "cwlId": "pp:cwlId",
        "provenanceClass": {"@id": "pp:provenanceClass", "@type": "@id"},
        "implementsProfile": {"@id": "pp:implementsProfile", "@type": "@id"},
        "cctDependencies": "pp:cctDependency",
        "candidateCctDependencies": "pp:candidateCctDependency",
        "hasStep": {"@id": "pp:hasStep", "@type": "@id"},
        "exactMatch": {"@id": "skos:exactMatch", "@type": "@id"},
        "closeMatch": {"@id": "skos:closeMatch", "@type": "@id"},
        "relatedMatch": {"@id": "skos:relatedMatch", "@type": "@id"},
        "openeoEquivalence": "pp:openeoEquivalence",
        "level": "pp:equivalenceLevel",
        "rationale": "pp:rationale",
        "decomposition": {"@id": "pp:decomposition", "@container": "@list"},
        "stage": "pp:stage",
        "openeo": "pp:openeo",
        "note": "skos:note",
        "serverSideFiles": {"@id": "pp:serverSideFile", "@context": {
            "name": "pp:liveName", "side": "pp:side",
            "implements": {"@id": "pp:implements", "@type": "@id"}, "location": "pp:location"}},
        # An Implementation Profile role that this deployment takes as several inputs, none of
        # which carries the role's representation (raster-crop's bounding box as OTB.ExtractROI's
        # four corner numbers). Declared, like serverSideFiles, so that the gap is explicit.
        "roleDecompositions": {"@id": "pp:roleDecomposition", "@context": {
            "side": "pp:side", "implements": {"@id": "pp:implements", "@type": "@id"},
            "parts": {"@id": "pp:part", "@container": "@list"},
            "selectors": {"@id": "pp:selector", "@context": {"name": "pp:liveName", "values": "rdf:value"}},
            "reproducible": {"@id": "pp:reproducible", "@type": "xsd:boolean"},
            "note": "skos:note"}},
        # A role with a representation that the deployment takes (or returns) as a URL of the data
        # instead of the data (C1, 2026-11-10): reported apart, like serverSideFiles.
        "unboundRoles": {"@id": "pp:unboundRole", "@context": {
            "side": "pp:side", "implements": {"@id": "pp:implements", "@type": "@id"}, "reason": "skos:note"}},
        "fixedRoleValues": {"@id": "pp:fixedRoleValue", "@context": {
            "side": "pp:side", "implements": {"@id": "pp:implements", "@type": "@id"},
            "values": "rdf:value", "reason": "skos:note"}},
        "byReference": {"@id": "pp:byReference", "@context": {
            "name": "pp:liveName", "side": "pp:side",
            "implements": {"@id": "pp:implements", "@type": "@id"}, "note": "skos:note"}},
        # A bound input or output whose Implementation Profile representation this deployment does
        # not serve (no media type exposed), accepted with its reason (A4.3).
        # A CWL CommandLineTool attached to no Implementation Profile, with the reason (decision Q1,
        # 2026-11-11): exclusive of implementsProfile.
        "notAttached": {"@id": "pp:notAttached", "@context": {"reason": "skos:note"}},
        "assumedFormatGaps": {"@id": "pp:assumedFormatGap", "@context": {
            "name": "pp:liveName", "side": "pp:side",
            "implements": {"@id": "pp:implements", "@type": "@id"},
            "served": "pp:servedMediaType", "reason": "skos:note", "evidence": "pp:evidence"}},
    }
}


# ------------------------------------------------------------------ helpers

def dump_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def dump_yaml(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100))


def cwl_items(section):
    """CWL inputs/outputs as an ordered dict, whatever the source form (map or list)."""
    if isinstance(section, dict):
        return {k: (v if isinstance(v, dict) else {"type": v}) for k, v in section.items()}
    return {i["id"].split("#")[-1].split("/")[-1]: i for i in section or []}


def expand(value, ns):
    if isinstance(value, str) and ":" in value and not value.startswith("http"):
        p, local = value.split(":", 1)
        if p in ns:
            return ns[p] + local
    return value


def is_optional(t):
    return (isinstance(t, str) and t.endswith("?")) or (isinstance(t, list) and "null" in t)


def base_type(t):
    if isinstance(t, str):
        return t.rstrip("?")
    if isinstance(t, list):
        nn = [x for x in t if x != "null"]
        return base_type(nn[0]) if len(nn) == 1 else nn
    if isinstance(t, dict):
        return t.get("type")
    return t


def _qn(v):
    return v.get("$") if isinstance(v, dict) else v


def _lst(v):
    return v if isinstance(v, list) else [v]


MEDIA_BY_EXT = {".tiff": "geotiff", ".tif": "geotiff", ".png": "png", ".jp2": "jp2",
                ".geojson": "geojson", ".json": "application/json", ".csv": "text/csv"}


def load_bag(path: Path):
    """Read a `cwltool --provenance` research object (CWLProv 0.6, BagIt).

    Returns the engine, and every activity of every bundle with its plan (`main/step[_N]`), the
    container image, UTC start/end and typed inputs/outputs: a literal (`value`), a file
    (`file`, `sha1`, `size`), a directory (`dir`, `files` listed recursively with relative
    paths) or a list. Two cwltool behaviours are handled here so that nothing else has to know
    about them: `prov:time` is naive local time, so the offset is taken from the engine log,
    which is UTC; and a run that failed inside a scatter has no primary bundle, so all
    `*.cwlprov.json` bundles are read and each activity remembers the scatter iteration of the
    bundle it came from (bundle name suffix `_2`, `_3`, ...; the first iteration has none)."""
    prov_dir = path / "metadata" / "provenance"
    bundles = {}
    for f in sorted(prov_dir.glob("*.cwlprov.json")):
        stem = f.name.split(".", 1)[0]
        if stem == "primary":
            iteration = None
        else:
            m = re.search(r"_(\d+)$", stem)
            iteration = int(m.group(1)) if m else 1
        bundles[iteration if iteration is not None else "primary"] = (f.name, json.loads(f.read_text()))
    if not bundles:
        sys.exit(f"{path}: no *.cwlprov.json bundle found")

    sizes = {p.name: p.stat().st_size for p in (path / "data").rglob("*") if p.is_file()}

    # UTC offset: engine log line for the workflow start vs the earliest prov:time
    offset = timedelta(0)
    logs = list((path / "metadata" / "logs").glob("engine.*.txt"))
    m = logs and re.search(r"\[(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d),\d+\.\d+Z\] \[workflow \] start",
                           logs[0].read_text())
    starts = [datetime.fromisoformat(_qn(v["prov:time"]))
              for _, b in bundles.values() for vv in b.get("wasStartedBy", {}).values() for v in _lst(vv)
              if v.get("prov:time")]
    if m and starts:
        delta = min(starts) - datetime.fromisoformat(m.group(1))
        offset = timedelta(seconds=round(delta.total_seconds() / 900) * 900)

    def utc(t):
        if not t:
            return None
        return (datetime.fromisoformat(_qn(t)) - offset).strftime("%Y-%m-%dT%H:%M:%SZ")

    engine = None
    activities = []
    for iteration, (bundle_name, d) in bundles.items():
        agents = {k: _lst(v)[0] for k, v in d.get("agent", {}).items()}
        ents = {k: _lst(v)[0] for k, v in d.get("entity", {}).items()}
        general = {}
        for vv in d.get("specializationOf", {}).values():
            for v in _lst(vv):
                general[v.get("prov:specificEntity")] = v.get("prov:generalEntity")
        members = {}  # prov:hadMember is a top-level relation in PROV-JSON, not an entity attribute
        for vv in d.get("hadMember", {}).values():
            for v in _lst(vv):
                members.setdefault(v.get("prov:collection"), []).append(v.get("prov:entity"))
        for ag in agents.values():
            label = ag.get("prov:label", "")
            if label.startswith("cwltool ") and engine is None:
                engine = {"name": "cwltool", "version": label.split()[1]}

        def artefact(eid, prefix=""):
            e = ents.get(eid, {})
            base = e.get("cwlprov:basename")
            if "prov:hadDictionaryMember" in e:
                pairs = [ents.get(_qn(mm), {}) for mm in _lst(e["prov:hadDictionaryMember"])]
                if base is None:  # a CWL record (e.g. the EOAP BBox), not a directory
                    return {"record": {p.get("prov:pairKey"): artefact(_qn(p.get("prov:pairEntity"))) for p in pairs}}
                files = []
                for p in pairs:
                    child = artefact(_qn(p.get("prov:pairEntity")), prefix + p.get("prov:pairKey", "") + "/")
                    if "file" in child:
                        files.append({"path": prefix + p.get("prov:pairKey"), "sha1": child["sha1"], "size": child["size"]})
                    elif "dir" in child:
                        files += child["files"]
                return {"dir": base, "files": sorted(files, key=lambda x: x["path"])}
            if eid in members and base is None:
                return {"list": [artefact(mm) for mm in members[eid]]}
            if "prov:value" in e:
                return {"value": _qn(e["prov:value"])}
            sha = eid[5:] if eid.startswith("data:") else (general.get(eid, "")[5:] if str(general.get(eid, "")).startswith("data:") else None)
            if base or sha:
                return {"file": base, "sha1": sha, "size": sizes.get(sha)}
            return {}

        for aid, a in d.get("activity", {}).items():
            a = _lst(a)[0]
            rec = {"id": aid, "iteration": iteration, "bundle": bundle_name, "plan": None, "planIri": None,
                   "image": None, "start": None, "end": None, "inputs": {}, "outputs": {}}
            for vv in d.get("wasStartedBy", {}).values():
                for v in _lst(vv):
                    if v.get("prov:activity") == aid:
                        rec["start"] = utc(v.get("prov:time"))
            for vv in d.get("wasEndedBy", {}).values():
                for v in _lst(vv):
                    if v.get("prov:activity") == aid:
                        rec["end"] = utc(v.get("prov:time"))
            for vv in d.get("wasAssociatedWith", {}).values():
                for v in _lst(vv):
                    if v.get("prov:activity") != aid:
                        continue
                    if v.get("prov:plan"):
                        pfx, sep, local = _qn(v["prov:plan"]).partition(":")
                        if not sep:
                            pfx, local = "", pfx
                        rec["plan"] = local
                        if pfx in d.get("prefix", {}):
                            rec["planIri"] = d["prefix"][pfx] + local
                    img = agents.get(v.get("prov:agent"), {}).get("cwlprov:image")
                    if img:
                        rec["image"] = img
            for rel, key in (("used", "inputs"), ("wasGeneratedBy", "outputs")):
                for vv in d.get(rel, {}).values():
                    for v in _lst(vv):
                        if v.get("prov:activity") == aid and v.get("prov:role"):
                            rec[key][_qn(v["prov:role"]).rsplit("/", 1)[-1]] = artefact(v.get("prov:entity"))
            activities.append(rec)
    return {"path": str(path), "engine": engine, "activities": activities}


def w3c_prov_example(info, exd: Path):
    """The run record as W3C PROV-JSONLD: the CWLProv bundle that holds this profile's activity,
    re-serialised without loss by the `prov` library (>= 2, the PROV-JSONLD serializer). The
    result validates against ogc.ogc-utils.prov.w3c-prov-jsonld and is read as RDF through its
    own context, which makes it the one example whose PROV-O graph is cwltool's, not this
    register's. PROV-JSONLD cannot carry prov:Mention (dropped from PROV-DM's Recommendation; the
    serializer raises), so the mentions cwltool writes for its nested bundles become
    specializationOf + prov:asInBundle, the workaround documented by that building block."""
    src = Path(info["prov"]["path"]) / "metadata" / "provenance" / info["activity"]["bundle"]
    try:
        from prov.model import ProvDocument, PROV
        from prov.serializers import Registry
        Registry.load_serializers()
        if "jsonld" not in Registry.serializers:
            raise ImportError("no PROV-JSONLD serializer")
    except ImportError as e:
        sys.exit(f"the W3C PROV-JSONLD examples need the `prov` library >= 2 ({e}): pip install 'prov>=2'")
    doc = ProvDocument.deserialize(str(src), format="json")

    def demention(bundle):
        for r in list(bundle.get_records()):
            if r.get_type() == PROV["Mention"]:
                bundle._records.remove(r)
                specific, general, in_bundle = (r.formal_attributes[i][1] for i in range(3))
                bundle.specialization(specific, general).add_attributes({PROV["asInBundle"]: in_bundle})
    demention(doc)
    for b in doc.bundles:
        demention(b)
    doc.serialize(str(exd / "cwlprov.jsonld"), format="jsonld", indent=2)


def bag_activity(bag, step, iteration):
    """The activity a profile's `run: {prov, step, iteration}` designates.

    `step` is the plan leaf (`calculate_turbidity`, `select_products`, or `main` for a
    sub-workflow re-rooted in its own bundle); `iteration` selects the scatter iteration bundle
    (1 = first, unsuffixed; N>1 = bundle and step names carry `_N`); no iteration = primary."""
    want_it = iteration if iteration is not None else "primary"
    leaf = step or "main"
    if isinstance(want_it, int) and want_it > 1 and leaf != "main":
        leaf = f"{leaf}_{want_it}"
    for a in bag["activities"]:
        if a["iteration"] == want_it and a["plan"] and a["plan"].rsplit("/", 1)[-1] == leaf:
            return a
    sys.exit(f"{bag['path']}: no activity for step={step!r} iteration={iteration!r} "
             f"(have {[a['plan'] for a in bag['activities'] if a['iteration'] == want_it]})")


def _ref(art, base, hint, d):
    """One artefact of the run record as an OGC results value."""
    if "file" in art:
        mt = hint.get("type") if isinstance(hint, dict) else None
        return {"href": f"{base}/{art['file']}", "type": media(mt or MEDIA_BY_EXT.get(Path(art["file"]).suffix, "application/octet-stream"), d)}
    if "dir" in art:  # the entry point inside the directory is named by the profile
        return {"href": f"{base}/{hint['href']}", "type": media(hint["type"], d)}
    if "list" in art:
        return [_ref(x, base, hint, d) for x in art["list"]]
    return art.get("value")


def _files_in(art):
    if "file" in art:
        return [{"path": art["file"], "sha1": art["sha1"], "size": art["size"]}]
    if "dir" in art:
        # a `glob: '.'` Directory output captures the whole working directory, including hidden
        # files the execution host leaves behind (e.g. macOS Rosetta's `.cache/rosetta` under
        # emulation) that are not a declared CWL output and never get a checksum.
        return [f for f in art["files"] if not any(p.startswith(".") for p in f["path"].split("/"))]
    if "list" in art:
        return [f for x in art["list"] for f in _files_in(x)]
    return []


# ------------------------------------------------------------------ CWL loading and transform

def load_process(proc, sources, roots):
    src = sources[proc["source"]["repo"]]
    path = roots[proc["source"]["repo"]] / src["base_path"] / proc["source"]["file"]
    doc = yaml.safe_load(path.read_text())
    element = proc["source"].get("element")
    if "release" in src:
        # a release-asset source (sources.yaml `release:`, no `commit:`): there is no repo tree
        # path to link to, only the asset's own download URL.
        url = f"{src['repo']}/releases/download/{src['release']}/{proc['source']['file']}"
    else:
        url = f"{src['repo']}/blob/{src['commit']}/{src['base_path']}/{proc['source']['file']}"
    if not element:
        return doc, doc, url
    top = {k: v for k, v in doc.items() if k != "$graph"}
    el = next(e for e in doc["$graph"] if e.get("id") == element)
    if el.get("class") == "Workflow":
        # the transform itself selects the *first* Workflow of the packed document (its own
        # `map(select(.class == "Workflow")) | first`); a document with only one top-level
        # Workflow (W1, W2) always hits the right one regardless of order, but water-bodies packs
        # two (`water-bodies`, `detect_water_body`) -- reorder $graph so the requested element is
        # first, leaving every other member (including the ones it steps into) untouched.
        reordered = dict(doc)
        reordered["$graph"] = [el] + [e for e in doc["$graph"] if e is not el]
        return reordered, el, url + "#" + element
    iso = copy.deepcopy(top)  # M-03: tool inherits document-level annotations
    iso.update(copy.deepcopy(el))
    return iso, el, url + "#" + element


def run_transform(cwl_doc, jq_path: Path):
    r = subprocess.run(["jq", "-f", str(jq_path)], input=json.dumps(cwl_doc),
                       capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


STAC_CATALOG_SCHEMA = {
    "type": "object",
    "required": ["type", "stac_version", "id", "description", "links"],
    "properties": {
        "type": {"type": "string", "enum": ["Catalog"]},
        "stac_version": {"type": "string"},
        "id": {"type": "string"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "links": {"type": "array"},
    },
    "format": "stac-catalog",
}


def correct(pd, cwl_el, ns, secrets, stac_catalog=()):
    """Apply documented manual corrections. Returns (corrected pd, list of corrections)."""
    pd = copy.deepcopy(pd)
    notes = []
    for name in stac_catalog or ():
        schema = pd.get("outputs", {}).get(name, {}).get("schema", {})
        if schema.get("properties", {}).get("type", {}).get("enum") == ["Collection"]:
            pd["outputs"][name]["schema"] = copy.deepcopy(STAC_CATALOG_SCHEMA)
            notes.append(f"M-05 outputs.{name}: the Directory output is a STAC Catalog written by the tool itself "
                         "(run record: `catalog.json` with one Item), not the Collection assumed by the transform")
    for section, key in (("inputs", "inputs"), ("outputs", "outputs")):
        items = cwl_items(cwl_el.get(key))
        for name, spec in items.items():
            fmt = spec.get("format")
            if not fmt or name not in pd.get(section, {}):
                continue
            fmts = fmt if isinstance(fmt, list) else [fmt]
            media = [FORMAT_MEDIA.get(expand(f, ns)) for f in fmts]
            if None in media:
                notes.append(f"{section}.{name}: unknown CWL format {fmts}, left unchanged")
                continue
            schema = pd[section][name]["schema"]
            target = schema["items"] if schema.get("type") == "array" and "items" in schema else schema
            if target.get("contentMediaType") != "application/octet-stream":
                continue
            new = [{"type": "string", "contentEncoding": "binary", "contentMediaType": m} for m in media]
            target.clear()
            if len(new) == 1:
                target.update(new[0])
                notes.append(f"M-01 {section}.{name}: contentMediaType from CWL format `{fmts[0]}` -> `{media[0]}`; contentEncoding binary")
            else:
                target["oneOf"] = new
                notes.append(f"M-01/M-02 {section}.{name}: CWL format list {fmts} -> oneOf {media}")
    for name in secrets or []:
        if name in pd.get("inputs", {}):
            pd["inputs"][name]["schema"]["writeOnly"] = True
            notes.append(f"M-04 inputs.{name}: declared in cwltool:Secrets -> writeOnly: true")
    return pd, notes


# ------------------------------------------------------------------ builders

def bb_id(proc):
    return f"{PREFIX}{proc['workflow']}.{proc['key']}"


def ptype_iri(proc):
    return f"{PTYPE_SCHEME}/{proc['workflow']}/{proc['key']}"


def pd_url(pd):
    return f"https://ospd.example.org/ogc-api/processes/{pd['id']}"


def plan_url(pd):
    """The prov:Plan of a CWL-sourced process: its OGC Application Package, as served by OGC API -
    Processes - Part 2 (DRU) at /processes/{processID}/package (req. /deploy-replace-undeploy/
    package-get-op). The same IRI is the type-level `plan` and every run's `hadPlan`."""
    return pd_url(pd) + "/package"


def execution_unit(url):
    return {"href": url.replace("/blob/", "/raw/", 1), "type": "application/cwl+yaml",
            "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"}


def media(v, d):
    return d["media"].get(v, v)


def execute_doc(proc, d):
    inputs = {}
    for k, v in proc["execute"]["inputs"].items():
        if isinstance(v, dict) and "href" in v:
            href = v["href"]
            if not re.match(r"^[a-z0-9]+://", href):
                # output of the upstream step (illustrative job URL)
                href = f"{d['job_base']}/upstream-step/results/{href}"
            v = {"href": href, "type": media(v["type"], d)}
        inputs[k] = v
    return {"inputs": inputs, "response": "document"}


def results_doc(proc, d, job_id, info):
    base = f"{d['job_base']}/{job_id}/results"
    hints = proc.get("results", {})
    out = {}
    for name, art in info["activity"]["outputs"].items():
        if not art and name in hints:  # not recoverable from the record: keep the declared value
            out[name] = hints[name]
            continue
        ref = _ref(art, base, hints.get(name, {}), d)
        out[name] = ref[0] if proc.get("results_single") and isinstance(ref, list) else ref
    return out


def run_info(proc, bags):
    """Engine, times, container image and the run-record activity a profile's examples come from.
    Every profile points into a run record; there are no illustrative examples."""
    run = proc.get("run", {})
    if not run.get("prov"):
        sys.exit(f"{proc['key']}: run.prov is required (a run record in scripts/sources.yaml `runs:`)")
    bag = bags[run["prov"]]
    act = bag_activity(bag, run.get("step"), run.get("iteration"))
    eng = {"id": f"urn:example:engine:cwltool-{bag['engine']['version']}",
           "name": bag["engine"]["name"], "version": bag["engine"]["version"]}
    return {"engine": eng, "start": act["start"], "end": act["end"], "image": act["image"],
            "prov": bag, "activity": act}


def docker_image(cwl_el, cwl_doc):
    for sect in ("requirements", "hints"):
        for src in (cwl_el, cwl_doc):
            r = src.get(sect) or {}
            if isinstance(r, list):
                r = {x.get("class"): x for x in r}
            if "DockerRequirement" in r:
                return r["DockerRequirement"].get("dockerPull")
    return None


def provenance_chain(proc, pd, exe, res, info, image, d):
    """Provenance view as an instance of ogc.bbr.provenance.provenance (W3C PROV chain)."""
    key = proc["key"]
    run_id = f"urn:example:run:{proc['workflow']}:{key}"
    eng = info["engine"]
    secrets = set(proc.get("secrets", []))
    ents, used, file_inputs = [], [], []
    for name, v in exe["inputs"].items():
        eid = f"urn:example:entity:{key}:in:{name}"
        e = {"id": eid, "provType": "prov:Entity", "entityType": f"{pd_url(pd)}#inputs/{name}"}
        if isinstance(v, dict) and "href" in v:
            e["links"] = [{"href": v["href"], "rel": "item", "type": v["type"]}]
            file_inputs.append(eid)
        elif name not in secrets:
            e["value"] = v
        ents.append(e)
        used.append(eid)
    for name, v in res.items():
        eid = f"urn:example:entity:{key}:out:{name}"
        e = {"id": eid, "provType": "prov:Entity", "entityType": f"{pd_url(pd)}#outputs/{name}",
             "wasGeneratedBy": run_id}
        if file_inputs:
            e["wasDerivedFrom"] = file_inputs
        vals = v if isinstance(v, list) else [v]
        if all(isinstance(x, dict) and "href" in x for x in vals):
            e["links"] = [{"href": x["href"], "rel": "item", "type": x["type"]} for x in vals]
        else:
            e["value"] = v
        e["wasAttributedTo"] = eng["id"]
        ents.append(e)
    activity = {
        "id": run_id,
        "provType": "prov:Activity",
        "activityType": ptype_iri(proc),
        "startedAtTime": info["start"],
        "used": used,
        "wasAssociatedWith": [eng["id"]] + ([f"urn:example:image:{image}"] if image else []),
        "qualifiedAssociation": [{"agent": eng["id"], "hadPlan": plan_url(pd)}],
    }
    if info["end"]:
        activity["endedAtTime"] = info["end"]
    agents = [{"id": eng["id"], "provType": "prov:SoftwareAgent", "name": f"{eng['name']} {eng['version']}"}]
    if image:
        agents.append({"id": f"urn:example:image:{image}", "provType": "prov:SoftwareAgent",
                       "name": f"container image {image}"})
    # The plan the run followed, as this view names it (the Application Package), and as the
    # engine's own CWLProv graph names it (the run-local copy in the research object, an arcp: IRI
    # that changes with every run): the latter is a specialization of the former.
    plans = [{"id": plan_url(pd), "provType": "prov:Plan"}]
    if info["activity"].get("planIri"):
        plans.append({"id": info["activity"]["planIri"], "provType": "prov:Plan",
                      "specializationOf": plan_url(pd)})
    return [activity] + ents + agents + plans, run_id


def process_run(proc, pd, run_id, info, parent_run):
    """CommandLineTool run as ogc.bbr.wf4ever.wfprov.ProcessRun (generic profile gap GP-1)."""
    doc = {
        "id": run_id,
        "type": "ProcessRun",
        "activityType": ptype_iri(proc),
        "describedByProcess": plan_url(pd),
        "usedInput": [{"id": f"urn:example:entity:{proc['key']}:in:{n}"} for n in proc["execute"]["inputs"]],
        "startedAtTime": info["start"],
        "wasEnactedBy": info["engine"]["id"],
    }
    if parent_run:
        doc["wasPartOfWorkflowRun"] = parent_run
    return doc


def execution_bundle(proc, pd, run_id, info, job_id, d):
    """Workflow run as ogc.bbr.provenance.execution: every file of the run record, directories
    included (CWLProv content-addresses each file, so a Directory output gets one artifact per
    member with its own checksum, GP-10). None when a file has no checksum."""
    eng = info["engine"]
    base = f"{d['job_base']}/{job_id}/results"
    outputs = []
    for name, art in info["activity"]["outputs"].items():
        for f in _files_in(art):
            if not f["sha1"]:
                return None
            outputs.append({"id": f"{base}/{f['path']}", "type": "Artifact", "role": "output",
                            "mediaType": media(MEDIA_BY_EXT.get(Path(f["path"]).suffix, "application/octet-stream"), d),
                            "describedByParameter": f"{pd_url(pd)}#outputs/{name}",
                            "wasOutputFrom": run_id, "checksum": {"algorithm": "SHA-1", "value": f["sha1"]}})
    if not outputs:
        return None
    run = {"id": run_id, "type": "WorkflowRun", "activityType": ptype_iri(proc),
           "describedByWorkflow": plan_url(pd), "wasEnactedBy": eng["id"], "status": "successful",
           "jobID": job_id, "startedAtTime": info["start"], "endedAtTime": info["end"]}
    if proc.get("steps"):
        run["hadSubProcessRun"] = [{"id": f"urn:example:run:{proc['workflow']}:{s}"} for s in proc["steps"]]
    engine = {"@id": eng["id"], "@type": "WorkflowEngine", "name": eng["name"], "version": eng["version"]}
    return {"run": run, "engine": engine, "outputs": outputs}


def amendments(proc, parent):
    """The classified amendments of a proposal entry, amended in place (pp:specification): those of
    every entry, those of an entry attached to tier 3, and those recorded in profiles.yaml
    (`amendments`). Each is a rim:RegisterAction of type pp:amendmentAction."""
    out = [("d5-2026-11-09", "2026-11-09", "substantive",
            "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. "
            "The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription "
            "and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped "
            "apart. The plan was already a node of its own.")]
    if proc.get("cwl_class") and proc.get("implementsProfile"):
        on = str(proc["tier3"].get("attached_on", "2026-11-09"))
        out.append((f"tier3-{on}", on, "substantive",
                    f"Attached to the Implementation Profile {proc['implementsProfile']} (implementsProfile), after "
                    "checking its signature (docs/ATTACHMENTS.md)."))
    if parent:
        on = max("2026-11-10", str((proc.get("tier3") or {}).get("attached_on", "2026-11-10")))
        out.append((f"specialisation-{on}", on, "substantive",
                    f"subClassOf changes from {ACTIVITY_TYPE_CLASS} to {parent['id']}, the activity type of the "
                    "operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): "
                    + ", ".join(v for k in ("usedEntityType", "generatedEntityType") for v in _lst(parent.get(k) or []))
                    + "."))
    if proc.get("cwl_class") and not_attached(proc):
        out.append(("not-attached-2026-11-11", "2026-11-11", "clarifying",
                    "notAttached added (absent -> {reason}): the entry now states that this CommandLineTool "
                    "implements no Implementation Profile, with the reason already given in docs/ATTACHMENTS.md "
                    "(profiles.yaml tier3.reason). Nothing else changes: the process was not attached before "
                    "and is not attached now (decision Q1 of 2026-11-11)."))
    for a in proc.get("amendments") or []:
        out.append((a["id"], a["date"], a["classification"], " ".join(a["description"].split())))
    return sorted(out, key=lambda a: a[1])


def register_item_fields(entry_id, proc=None, parent=None):
    """The Registered Item Model core shared by every process-type entry.

    A candidate awaits a register decision: `invalid` (not yet in force) and `published` (visible).
    `hasAction` records its addition, then each classified amendment (amended in place, no new IRI).
    """
    actions = [{
        "id": entry_id + "/actions/addition",
        "type": "RegisterAction",
        "actionType": "addition",
        "proposer": GEOLABS_AGENT,
        "startedAtTime": TODAY + "T00:00:00Z",
        "appliesTo": entry_id,
    }]
    for name, date, classification, description in (amendments(proc, parent) if proc else []):
        actions.append({
            "id": f"{entry_id}/actions/{name}",
            "type": "RegisterAction",
            "actionType": AMENDMENT_ACTION,
            "changeClassification": classification,
            "description": description,
            "proposer": GEOLABS_AGENT,
            "startedAtTime": date + "T00:00:00Z",
            "appliesTo": entry_id,
        })
    return {
        "type": ["ProcessType", "owlClass", "ActivityType"],
        "objectIdentifier": entry_id,
        "itemClass": ATR_ITEM_CLASS,
        "inRegister": PROCESS_TYPE_REGISTER,
        "validityStatus": "invalid",
        "publicationStatus": "published",
        "hasAction": actions,
    }


def parent_activity_type(proc, gp_root):
    """The activity type of the operation a deployed process implements: the `activityType` of its
    Implementation Profile, read from bblocks-generic-profiles. None for a process attached to no
    Implementation Profile, which keeps acttype:ActivityType as its parent."""
    if not proc.get("implementsProfile"):
        return None
    ip_key = proc["implementsProfile"].rstrip("/").rsplit("/", 1)[-1]
    ip = json.loads((gp_root / "_sources" / "implementation-profile" / ip_key / "examples" / f"{ip_key}.json").read_text())
    at_key = ip["activityType"].rstrip("/").rsplit("/", 1)[-1]
    at = json.loads((gp_root / "_sources" / "activity-type" / at_key / "examples" / f"{at_key}.json").read_text())
    if at["subClassOf"] != GEOPROC_CLASS or not (at.get("usedEntityType") or at.get("generatedEntityType")):
        sys.exit(f"{proc['key']}: activity type {at['id']} is not a geoprocessing activity type with an entity type")
    return at


def not_attached(proc, plan=True):
    """Decision Q1 (2026-11-11): a CWL entry (with a plan) that is no Workflow (no steps) and implements
    no Implementation Profile carries `notAttached`, with the reason of profiles.yaml `tier3`."""
    return bool(plan) and not proc.get("steps") and not proc.get("implementsProfile")


def build_entry(proc, pd, definition, deployment, plan, assumed, by_key, parent=None):
    """A process-type entry, in the five parts of decision D5:

    - meaning: `prefLabel`, `definition`, `subClassOf` (with the RIM fields and `inScheme`);
    - classification: `classification.phase`, the six-phase position (pp:phase);
    - deployment: `deployment`, what is deployed (process description, profile block, run class);
    - plan: `plan`, the Application Package of a CWL process (a prov:Plan of its own);
    - correspondences: `correspondences`, the proposed openEO equivalences.

    `implementsProfile` and its binding declarations are the link to tier 3; `hasStep` the steps of a
    Workflow. An entry attached to an Implementation Profile specialises the activity type of its
    operation in bblocks-generic-profiles (D5; decision of 2026-11-10): `subClassOf` is that activity
    type, and the entry declares the same GeoSPARQL entity type(s), as a registered sub-class of
    geoproc:GeoprocessingActivityType must. Any other entry keeps acttype:ActivityType."""
    entry_id = ptype_iri(proc)
    e = {
        "id": entry_id,
        **register_item_fields(entry_id, proc, parent),
        "prefLabel": (proc.get("label") or pd.get("title") or pd["id"]).strip(),
        "definition": " ".join(definition.split()),
        "subClassOf": parent["id"] if parent else ACTIVITY_TYPE_CLASS,
    }
    if parent:
        e.update({k: parent[k] for k in ("usedEntityType", "generatedEntityType") if parent.get(k)})
    e.update({
        "inScheme": PTYPE_SCHEME,
        "classification": {"phase": [PHASE_BASE + p for p in proc["phases"]]},
        "deployment": deployment,
    })
    if plan:
        e["plan"] = plan
    e.update(tier3_link_fields(proc, assumed))
    if not_attached(proc, plan):
        # Decision Q1 (2026-11-11): a CWL CommandLineTool attached to no Implementation Profile
        # records why, from `tier3.reason` in profiles.yaml; audit_planes.py requires one or the other.
        e["notAttached"] = {"reason": " ".join(proc["tier3"]["reason"].split())}
    if proc.get("steps"):
        e["hasStep"] = [ptype_iri(by_key[s]) for s in proc["steps"]]
    e["correspondences"] = correspondences(proc["openeo"])
    return e


def process_type_entry(proc, pd, cwl_el, src, url, by_key, assumed=(), parent=None):
    deployment = {
        "profile": bb_id(proc),
        "processDescription": {"id": pd["id"], "version": pd["version"], "href": pd_url(pd)},
        "provenanceClass": "http://purl.org/wf4ever/wfprov#" + ("WorkflowRun" if cwl_el["class"] == "Workflow" else "ProcessRun"),
    }
    plan = {
        "id": plan_url(pd),
        "type": "Plan",
        "executionUnit": execution_unit(url),
        "cwlClass": cwl_el["class"],
        "cwlId": cwl_el.get("id", pd["id"]),
        "license": src["license"],
        "cctDependencies": proc.get("cct", []),
        "candidateCctDependencies": proc.get("cct_candidates", []),
    }
    definition = (proc.get("definition") or cwl_el.get("doc") or cwl_el.get("label") or pd.get("description") or "")
    return build_entry(proc, pd, definition, deployment, plan, list(assumed), by_key, parent)


def profile_schema(proc, pd, cwl_el, has_exec, inherited=None):
    req_in = [n for n, v in cwl_items(cwl_el.get("inputs")).items()
              if not is_optional(v.get("type")) and "default" not in v and n in pd["inputs"]]
    workflow = cwl_el["class"] == "Workflow"
    defs = {
        "rawProcessDescription": {"$ref": "bblocks://ogc.api.processes.part1.v1.schemas.process"},
        "applicationPackage": {"$ref": "bblocks://ogc.api.processes.part2.v1.schemas.ogcapppkg"},
        "provenance": {"$ref": "bblocks://ogc.bbr.provenance.provenance"},
        "processTypeEntry": {"$ref": f"bblocks://{PREFIX}process-type"},
        "w3cProvJsonLd": {"$ref": "bblocks://ogc.ogc-utils.prov.w3c-prov-jsonld"},
        "execute": {
            "description": ("Execute request for this process. Built on the processDescription input "
                            "schemas and on ogc.api.processes.part1.v1.schemas.link / qualifiedInputValue, "
                            "because ogc.api.processes.part1.v1.schemas.execute rejects plain strings and "
                            "numbers (upstream issue U-01)."),
            "type": "object",
            "required": ["inputs"],
            "properties": {
                "inputs": {
                    "type": "object",
                    "required": req_in,
                    "propertyNames": {"enum": list(pd["inputs"].keys())},
                    "additionalProperties": {"anyOf": [
                        {"$ref": "bblocks://ogc.api.processes.part1.v1.schemas.link"},
                        {"$ref": "bblocks://ogc.api.processes.part1.v1.schemas.qualifiedInputValue"},
                        {"type": ["string", "number", "integer", "boolean", "array", "object"]},
                    ]},
                },
                "outputs": {"type": "object", "propertyNames": {"enum": list(pd["outputs"].keys())}},
                "response": {"enum": ["raw", "document"]},
            },
        },
        "results": {
            "description": "Results document (response=document) for this process (see U-01).",
            "type": "object",
            "propertyNames": {"enum": list(pd["outputs"].keys())},
            "additionalProperties": {"anyOf": [
                {"$ref": "bblocks://ogc.api.processes.part1.v1.schemas.link"},
                {"type": "array", "items": {"$ref": "bblocks://ogc.api.processes.part1.v1.schemas.link"}},
                {"type": ["string", "number", "integer", "boolean", "array", "object"]},
            ]},
        },
    }
    if workflow and has_exec:
        defs["execution"] = {"$ref": "bblocks://ogc.bbr.provenance.execution"}
    else:
        defs["processRun"] = {"$ref": "bblocks://ogc.bbr.wf4ever.wfprov.ProcessRun"}
    pins = {
        "type": "object",
        "required": ["id", "version", "inputs", "outputs"],
        "properties": {
            "id": {"const": pd["id"]},
            "inputs": {"type": "object", "required": list(pd["inputs"].keys()),
                       "propertyNames": {"enum": list(pd["inputs"].keys())}},
            "outputs": {"type": "object", "required": list(pd["outputs"].keys()),
                        "propertyNames": {"enum": list(pd["outputs"].keys())}},
        },
    }
    if inherited:
        # deep copies: a shared object would be dumped as a YAML anchor/alias
        defs["inheritedProcessDescription"] = {"allOf": [
            {"$ref": "bblocks://ogc.api.processes.part1.v1.schemas.process"},
            {"$ref": "bblocks://ogc.api.processes.part2.v1.schemas.staticIndicator"}, copy.deepcopy(pins), inherited]}
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "description": (f"Profile of the OGC API - Processes processDescription of `{pd['id']}` "
                        f"(CWL {cwl_el['class']}). Pins the process id and the input/output names; "
                        "the input/output schemas are those derived from the CWL."),
        "allOf": [
            {"$ref": "bblocks://ogc.api.processes.part1.v1.schemas.process"},
            {"$ref": "bblocks://ogc.api.processes.part2.v1.schemas.staticIndicator"},
            pins,
        ],
        "$defs": defs,
    }


# ------------------------------------------------------------------ documentation

def md_openeo(oe):
    lines = [f"**Level: {oe['level']}.** " + " ".join(oe["rationale"].split()), ""]
    for rel in ("exactMatch", "closeMatch", "relatedMatch"):
        if oe.get(rel):
            lines.append(f"- `{rel}`: " + ", ".join(f"`{t}`" for t in oe[rel]))
    if oe.get("decomposition"):
        lines += ["", "| Stage | openEO | Level | Note |", "|---|---|---|---|"]
        for s in oe["decomposition"]:
            lines.append(f"| {s['stage']} | {', '.join('`'+x+'`' for x in s.get('openeo', [])) or '—'} | "
                         f"{s['level']} | {s.get('note', '')} |")
    return "\n".join(lines)


def description_md(proc, pd, cwl_el, url, src, corrections, has_exec, info, by_key, eoap_commit, gp_root):
    wf = WORKFLOW_LABELS[proc["workflow"]]
    ins = cwl_items(cwl_el.get("inputs"))
    outs = cwl_items(cwl_el.get("outputs"))
    pin = (f"pinned commit `{src['commit'][:7]}`" if "commit" in src
           else f"GitHub Release `{src['release']}`, sha256 `{src['sha256'][:12]}`")
    parts = [
        f"Process profile of **`{pd['id']}`** ({cwl_el['class']}, {wf}).",
        "",
        f"> {(proc.get('label') or cwl_el.get('label') or pd.get('title') or '').strip()}",
        "",
        "## Source",
        "",
        f"- CWL: [{proc['source']['file']}{('#' + proc['source']['element']) if proc['source'].get('element') else ''}]({url}) "
        f"({pin}, license <{src['license']}>). Referenced, not copied.",
        f"- Six-phase position: " + " → ".join(PHASE_LABELS[p] for p in proc["phases"]),
        f"- EOAP CWL custom types used: {', '.join('`'+c+'`' for c in proc.get('cct', [])) or 'none'}"
        + (f"; candidates: {', '.join('`'+c+'`' for c in proc['cct_candidates'])}" if proc.get("cct_candidates") else ""),
    ]
    if proc.get("steps"):
        parts.append("- Steps (profiles): " + ", ".join(f"`{bb_id(by_key[s])}`" for s in proc["steps"]))
    if proc.get("parents"):
        parts.append("- Used by: " + ", ".join(f"`{bb_id(by_key[s])}`" for s in proc["parents"]))
    parts += ["", "| Input | CWL type | Output | CWL type |", "|---|---|---|---|"]
    il, ol = list(ins.items()), list(outs.items())
    for i in range(max(len(il), len(ol))):
        a = il[i] if i < len(il) else ("", {"type": ""})
        b = ol[i] if i < len(ol) else ("", {"type": ""})
        def show(t):
            return t if isinstance(t, str) else json.dumps(t)
        fa = show(a[1].get("type")) if a[0] else ""
        fb = show(b[1].get("type")) if b[0] else ""
        parts.append(f"| {('`'+a[0]+'`') if a[0] else ''} | {fa.replace('|', '/')} | {('`'+b[0]+'`') if b[0] else ''} | {fb.replace('|', '/')} |")
    if proc.get("analysis"):
        parts += ["", "## Analysis", "", proc["analysis"].strip()]
    parts += ["", "## processDescription derivation", "",
              "Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct " 
              f"`{eoap_commit[:7]}`, inline variant)."]
    if corrections:
        parts += ["", "**Manually corrected** (the raw transform output is kept as a separate example):", ""]
        parts += [f"- {c}" for c in corrections]
    else:
        parts += ["", "No manual correction: the example is the unmodified transform output."]
    parts += ["", "## Provenance view", "",
              "Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV "
              "chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation."
              "hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - "
              "Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as "
              "the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is "
              "given as a `prov:specializationOf` that Application Package --, input and output "
              "`prov:Entity` objects (literal "
              "parameters carry `value`, files carry `links`) and the engine / container image as "
              "`prov:SoftwareAgent`."]
    if cwl_el["class"] == "Workflow":
        parts.append("" if has_exec else "")
        parts.append("The workflow run is also given as an `ogc.bbr.provenance.execution` bundle."
                     if has_exec else
                     "No `ogc.bbr.provenance.execution` bundle is given: its artifacts require a checksum, which "
                     "a STAC Directory output does not have (GP-10).")
    else:
        parts.append("The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the "
                     "generic profile has no step-level run (GP-1).")
    parts += ["", "Gaps met here are listed in `docs/PROVENANCE-GAPS.md`."]
    if info.get("prov"):
        run = proc["run"]
        where = f"scatter iteration {run['iteration']}, " if run.get("iteration") else ""
        parts += ["", f"Execution and provenance examples are built from a real `cwltool --provenance` run "
                  f"(CWLProv research object `{run['prov']}`: {info['prov']['note']}), activity "
                  f"`{info['activity']['plan']}` ({where}engine {info['engine']['name']} {info['engine']['version']}). "
                  "Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. "
                  "Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment."]
    parts += ["", "## Implementation Profile (tier 3)", ""]
    att = proc["tier3"]
    if proc.get("implementsProfile"):
        parts += md_binding(proc, pd, gp_root, " ".join(att["reason"].split()))
    else:
        parts += ["Not attached to an Implementation Profile of bblocks-generic-profiles: "
                  + " ".join(att["reason"].split()), "",
                  "The attachment of each CWL process is listed in `docs/ATTACHMENTS.md`."]
    parts += ["", "## openEO equivalence", "", md_openeo(proc["openeo"]), "",
              "## Process type (Activity 4)", "",
              f"Registered ActivityType OWL class `{ptype_iri(proc)}` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision."]
    return "\n".join(parts) + "\n"


def bblock_json(proc, pd, cwl_el, corrections, has_exec, by_key):
    oe = proc["openeo"]
    targets = oe.get("exactMatch", []) + oe.get("closeMatch", []) + oe.get("relatedMatch", [])
    for s in oe.get("decomposition", []) or []:
        targets += s.get("openeo", [])
    # The workflow/step relation is not a schema dependency (a workflow's processDescription does
    # not embed those of its steps), so it cannot go in dependsOn; seeAlso is what the register
    # and the viewer render as navigable links, in both directions.
    related = [bb_id(by_key[s]) for s in proc.get("steps", [])] + [bb_id(by_key[s]) for s in proc.get("parents", [])]
    see = related + [t for t in dict.fromkeys(targets) if t not in related]
    depends = ["ogc.api.processes.part1.v1.schemas.process", "ogc.api.processes.part2.v1.schemas.staticIndicator",
               "ogc.api.processes.part2.v1.schemas.ogcapppkg", "ogc.bbr.provenance.provenance",
               f"{PREFIX}process-type", "eoap.cct.cwl-to-ogcprocess",
               "ogc.ogc-utils.prov.w3c-prov-jsonld"]
    if cwl_el["class"] == "Workflow":
        depends += ["ogc.bbr.provenance.execution"] if has_exec else []
    else:
        depends += ["ogc.bbr.wf4ever.wfprov.ProcessRun"]
    depends += proc.get("cct", [])
    tags = ["OSPD", "process profile", "CWL", cwl_el["class"], proc["workflow"]]
    if corrections:
        tags.append("manually-corrected")
    meta = {
        "$schema": "https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/ogc/bblocks/metadata-schema.yaml",
        "name": f"Process profile: {pd['id']}",
        "abstract": (f"OGC API - Processes profile of the CWL {cwl_el['class']} `{pd['id']}` "
                     f"({WORKFLOW_LABELS[proc['workflow']]}), with its "
                     "provenance view, process-type entry and openEO equivalence."),
        "status": "under-development",
        "dateTimeAddition": f"{TODAY}T00:00:00Z",
        "dateOfLastChange": TODAY,
        "version": "0.1",
        "itemClass": "schema",
        "register": "process-profiles",
        "dependsOn": depends,
        "seeAlso": see + ["ogc.api.processes.part1.v1.requirements.core"],
        "conformanceClasses": [PART1_CORE],
        "scope": "dev",
        "tags": tags,
        "sourceSchema": "schema.yaml",
        "maturity": "development",
        "group": WORKFLOW_LABELS[proc["workflow"]],
    }
    if proc.get("implementsProfile"):
        # as for the live processes (ogcapi_bblock_json): the Implementation is a profile of its
        # Implementation Profile
        meta["isProfileOf"] = generic_profiles_identifier(proc["implementsProfile"])
    return meta


def examples_yaml(proc, cwl_el, url, corrected, has_exec):
    ex = [
        {"title": "Source CWL (referenced)",
         "content": f"The CWL {cwl_el['class']} is referenced, not copied: <{url}>."},
        {"title": "processDescription",
         "content": "OGC API - Processes processDescription derived from the CWL"
                    + (" (manually corrected, see description)." if corrected else "."),
         "snippets": [{"language": "json", "ref": "examples/processDescription.json"}]},
    ]
    if proc.get("implementsProfile"):
        ex.append(inherited_example(proc))
    if corrected:
        ex.append({"title": "Raw cwl-to-ogcprocess output",
                   "content": "Unmodified output of the `eoap.cct.cwl-to-ogcprocess` jq transform.",
                   "snippets": [{"language": "json", "ref": "examples/processDescription.raw.json",
                                 "schema-ref": "#/$defs/rawProcessDescription"}]})
    ex += [
        {"title": "OGC Application Package (deploy)",
         "content": "Part 2 deploy body: the execution unit is a link to the pinned CWL.",
         "snippets": [{"language": "json", "ref": "examples/ogcapppkg.json", "schema-ref": "#/$defs/applicationPackage"}]},
        {"title": "Execute request",
         "snippets": [{"language": "json", "ref": "examples/execute.json", "schema-ref": "#/$defs/execute"}]},
        {"title": "Results",
         "snippets": [{"language": "json", "ref": "examples/results.json", "schema-ref": "#/$defs/results"}]},
        {"title": "Provenance view (generic provenance profile)",
         "content": "W3C PROV chain validated against `ogc.bbr.provenance.provenance`.",
         "snippets": [{"language": "json", "ref": "examples/provenance.json", "schema-ref": "#/$defs/provenance"}]},
    ]
    if cwl_el["class"] == "Workflow":
        if has_exec:
            ex.append({"title": "Execution bundle (generic provenance profile)",
                       "snippets": [{"language": "json", "ref": "examples/execution.json", "schema-ref": "#/$defs/execution"}]})
    else:
        ex.append({"title": "Process run (wfprov:ProcessRun, gap GP-1)",
                   "snippets": [{"language": "json", "ref": "examples/process-run.json", "schema-ref": "#/$defs/processRun"}]})
    ex.append({"title": "Process-type register entry (Activity 4)",
               "snippets": [{"language": "json", "ref": "examples/process-type.json", "schema-ref": "#/$defs/processTypeEntry"}]})
    ex.append({"title": "Run record, W3C PROV-JSONLD (cwltool CWLProv bundle)",
               "content": "The CWLProv bundle of the run record that holds this profile's activity, re-serialised "
                          "as PROV-JSONLD by the `prov` library (mentions of nested bundles rewritten as "
                          "`specializationOf` + `prov:asInBundle`, see that block's notes), validated against "
                          "`ogc.ogc-utils.prov.w3c-prov-jsonld` and read as RDF through its own context: the PROV-O "
                          "graph here is the engine's, not this register's provenance view.",
               "snippets": [{"language": "jsonld", "ref": "examples/cwlprov.jsonld", "schema-ref": "#/$defs/w3cProvJsonLd"}]})
    # Every snippet below is a document about this process, and several carry relative ids
    # (the nested processDescription id of ogcapppkg.json and process-type.json, the id of the
    # processDescription itself). Without a base URI they uplift to file:// IRIs rooted at the
    # uplift working directory; with one they land in the register's process namespace.
    return [e if not e.get("snippets")
            else {"title": e["title"], "base-uri": PROCESS_BASE,
                  **{k: v for k, v in e.items() if k != "title"}}
            for e in ex]


# ------------------------------------------------------------------ live OGC API - Processes
# profiles (sources.yaml `kind: ogcapi-process`): no CWL, no jq transform, no run record -- the
# cached processDescription IS the target shape already. Static processDescription only, by
# design (docs/OPEN-QUESTIONS.md Q-SQLMM): no execute/results/provenance examples, since there is
# no CWLProv-style run record for a live deployed service the way there is for the CWL workflows.

# Fields ZOO-Project adds to an input/output description that OGC API - Processes Part 1 does not
# define; the only ones removed from a live processDescription.
ZOO_INTERNAL_IO = ("extended-schema", "raw_schema1")


def load_ogcapi_process(proc, sources, roots):
    """Reads a cached live processDescription (never downloaded here, see
    run_workflows.py ensure_ogcapi_processes()) and normalises it: drops only the
    ZOO-Project-internal input/output fields (ZOO_INTERNAL_IO) that are not part of OGC API -
    Processes Part 1 and would not uplift to anything meaningful, and trims titles and
    descriptions. Everything else -- minOccurs/maxOccurs, metadata, keywords, links -- is kept as
    the live service serves it (until 2026-10-08 a whitelist dropped those too)."""
    src = sources[proc["source"]["repo"]]
    path = roots[proc["source"]["repo"]] / src["base_path"] / proc["source"]["file"]
    raw = json.loads(path.read_text())
    url = src["repo"] + "/" + raw["id"]

    def clean_io(items):
        # Drop only what is ZOO-Project-internal; everything else (minOccurs/maxOccurs, metadata,
        # keywords, ...) is the live description and is kept as served.
        out = {}
        for k, v in items.items():
            e = {"title": (v.get("title") or "").strip(), "description": (v.get("description") or "").strip()}
            e.update({kk: vv for kk, vv in v.items() if kk not in ZOO_INTERNAL_IO and kk not in e})
            out[k] = e
        return out

    pd = {
        "id": raw["id"],
        "title": raw.get("title", raw["id"]),
        "description": raw.get("description", ""),
        "version": raw.get("version", "1.0.0"),
        "jobControlOptions": raw.get("jobControlOptions", []),
        "outputTransmission": raw.get("outputTransmission", []),
        "inputs": clean_io(raw.get("inputs", {})),
        "outputs": clean_io(raw.get("outputs", {})),
    }
    pd.update({k: v for k, v in raw.items() if k not in pd and k not in ("inputs", "outputs")})
    return raw, pd, url


def ogcapi_process_type_entry(proc, pd, src, url, by_key, assumed=(), parent=None):
    # A natively implemented process (`mutable: false`) has no Application Package -- Part 2's
    # /package is only served for dynamically deployed ones (req. package-get-op C) -- so no plan.
    deployment = {
        "profile": bb_id(proc),
        "processDescription": {"id": pd["id"], "version": pd["version"], "href": url},
        "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
    }
    if src.get("license"):
        deployment["processDescription"]["license"] = src["license"]
    # Inputs and outputs that this deployment passes as names of files stored on the server, not
    # as encoded data (profiles.yaml `server_side_files`), are declared by tier3_link_fields().
    return build_entry(proc, pd, proc.get("definition") or pd.get("description") or "", deployment, None, list(assumed), by_key, parent)


PROFILE_ROLE = "http://www.opengis.net/spec/wps/2.0/def/process-profile/"  # OGC 14-065r1 Table 22
# Table 22 only names profile levels; these say the target is one input/output of an
# Implementation Profile. Defined by bblocks-generic-profiles, not by OGC: nothing is minted
# under opengis.net.
IO_ROLE = GENERIC_PROFILES_BASE + "role/implementation-"


def _merge(first, then):
    return list(first) + [v for v in then if v not in first]


def _contains_all(values):
    return {"allOf": [{"contains": {"const": v}} for v in values]}


def _contains_refs(refs):
    return {"allOf": [{"contains": {"type": "object", "required": ["role", "href"], "properties": {
        "role": {"const": m["role"]}, "href": {"const": m["href"]}}}} for m in refs]}


def inherited_process_description(proc, pd, gp_root):
    """The processDescription of a deployed process (live, or derived from its CWL) with what OGC
    14-065r1 Table 21 says the Implementation (instance level) inherits from its Implementation
    Profile: keywords Extended (E), and, per footnote a, the list of metadata references to superior
    profiles extended with a Table 22 `implementation` reference -- at process level and on every
    input/output bound to one of the Implementation Profile's (`bindings` in profiles.yaml) -- plus
    the `dataType` of the role each bound input/output implements (A4.2). Several inputs may be
    bound to one role that takes a list (calculate-band's band_a..band_z for `rasters`). A role taken
    as several inputs none of which is the role (`role_decompositions`) gets no reference and no
    data type on the parts: the process-type entry declares it. Returns the document and the JSON
    Schema checking exactly that inheritance."""
    ip_iri = proc["implementsProfile"]
    ip_key = ip_iri.rstrip("/").rsplit("/", 1)[-1]
    load = lambda tier, k: json.loads((gp_root / "_sources" / tier / k / "examples" / f"{k}.json").read_text())
    ip = load("implementation-profile", ip_key)
    gp = load("generic-profile", ip["refinesGenericProfile"].rstrip("/").rsplit("/", 1)[-1])
    # Profile-level references (Table 22 roles) live on the process only: the Implementation
    # Profile's own list (concept, generic), extended with `implementation` (footnote a).
    refs = list(ip["metadata"]) + [
        {"title": f"Implementation Profile: {ip['prefLabel']}", "role": PROFILE_ROLE + "implementation", "href": ip_iri}]

    bindings, unbound = proc.get("bindings", {}), proc.get("unbound", {})
    decomposed = proc.get("role_decompositions", {})
    doc = {k: v for k, v in pd.items() if k not in ("inputs", "outputs")}
    # Extend (E), never replace: the inherited values first, then whatever the live service has.
    doc["keywords"] = _merge(ip["keywords"], pd.get("keywords", []))
    doc["metadata"] = refs + list(pd.get("metadata", []))
    rules = {"keywords": _contains_all(ip["keywords"]), "metadata": _contains_refs(refs)}
    for side in ("inputs", "outputs"):
        bound = bindings.get(side, {})
        for live, name in bound.items():
            if live not in pd[side] or name not in ip[side]:
                sys.exit(f"{proc['key']}: binding {side} {live} -> {name}: unknown on the deployed process or on {ip_key}")
        for name, d in (decomposed.get(side) or {}).items():
            unknown = [p for p in d["parts"] + [c["name"] for c in d.get("selectors", [])] if p not in pd[side]]
            if name not in ip[side] or unknown or name in bound.values():
                sys.exit(f"{proc['key']}: role decomposition {side} {name}: unknown role on {ip_key}, "
                         f"unknown parts {unknown}, or the role is also bound")
            for c in d.get("selectors", []):
                # a selector value must be one the deployed input accepts
                allowed = pd[side][c["name"]].get("schema", {}).get("enum")
                if not allowed or set(c["values"]) - set(allowed):
                    sys.exit(f"{proc['key']}: role decomposition {side} {name}: selector {c['name']} {c['values']} "
                             f"not within the values the deployment accepts ({allowed})")
        for name in ((proc.get("fixed_roles") or {}).get(side) or {}):
            if name not in unbound:
                sys.exit(f"{proc['key']}: fixed_roles {side} {name}: a fixed value is declared only for an unbound role")
        missing = set(ip[side]) - set(bound.values()) - set(unbound) - set(decomposed.get(side) or {})
        if missing:
            sys.exit(f"{proc['key']}: {ip_key} {side} {sorted(missing)} neither bound, decomposed nor `unbound` in profiles.yaml")
        for name in set(unbound) & set(ip[side]):
            # C2 (2026-11-10): a deployment may leave unbound a role whose minOccurs is 0 at tier 3,
            # with a reason. The testbed exception (docs/ATTACHMENTS.md): a live process may also
            # leave unbound an input its deployment does not expose, with a reason.
            if name in bound.values() or name in (decomposed.get(side) or {}):
                sys.exit(f"{proc['key']}: role `{name}` is both `unbound` and bound or decomposed")
            if not str(unbound[name]).strip():
                sys.exit(f"{proc['key']}: `unbound` {name} needs a reason")
            floor = 1 if side == "outputs" else ip[side][name].get("minOccurs", gp[side][name].get("minOccurs", 1))
            fixed = ((proc.get("fixed_roles") or {}).get(side) or {}).get(name)
            if fixed and (floor > 0 or not fixed.get("values") or not str(fixed.get("reason", "")).strip()):
                sys.exit(f"{proc['key']}: fixed_roles {side} {name}: only an unbound role of minOccurs 0, with values and a reason")
            if floor > 0 and proc.get("cwl_class"):
                sys.exit(f"{proc['key']}: {side} role `{name}` of {ip_key} is left unbound but its minOccurs at tier 3 "
                         f"is {floor}: only a role of minOccurs 0 may be (testbed exception: live processes only)")
        out, side_rules = {}, {}
        for live, e in pd[side].items():
            name = bound.get(live)
            if not name:
                out[live] = e
                continue
            ipe = ip[side][name]
            # Input/output level: the Implementation Profile input/output's own references (to
            # its Generic Profile input/output) extended with one to that input/output itself.
            meta = list(ipe["metadata"]) + [
                {"title": f"Implementation Profile: {ip['prefLabel']} -- {side[:-1]} `{name}`",
                 "role": IO_ROLE + side[:-1], "href": f"{ip_iri}/{side}/{name}"}]
            # A4.2: the data type of the Implementation Profile role, a dt:DataType concept. Only on
            # bound inputs and outputs: an addition of the deployment (footnote b) has no tier-3
            # counterpart to derive one from.
            out[live] = {**{k: e[k] for k in ("title", "description") if k in e},
                         "dataType": ipe["dataType"],
                         "keywords": _merge(ipe["keywords"], e.get("keywords", [])),
                         "metadata": meta + list(e.get("metadata", [])),
                         **{k: v for k, v in e.items() if k not in ("title", "description", "keywords", "metadata")}}
            side_rules[live] = {"required": ["dataType", "keywords", "metadata"], "properties": {
                "dataType": {"const": ipe["dataType"]},
                "keywords": _contains_all(ipe["keywords"]), "metadata": _contains_refs(meta)}}
            if side == "inputs" and "minOccurs" in e:
                # Only where the live input declares a cardinality. It may restrict the inherited
                # minimum, down to 0 (optional input), never above it -- the rule
                # bblocks-generic-profiles applies to its own Implementation Profiles.
                # maxOccurs: Table 21 footnote d, it may extend.
                floor = ipe.get("minOccurs", gp["inputs"][name].get("minOccurs", 1))
                side_rules[live]["properties"]["minOccurs"] = {"type": "integer", "minimum": 0, "maximum": floor}
        doc[side] = out
        rules[side] = {"type": "object", "required": sorted(side_rules), "properties": side_rules}
    schema = {"description": (f"`{pd['id']}` as the Implementation (instance level) of `{ip_iri}`: "
                              "Table 21 keywords (E) and footnote-a metadata references (Table 22 roles) "
                              "inherited from its Implementation Profile."),
              "type": "object", "required": ["keywords", "metadata"], "properties": rules}
    return doc, schema


def _media_types(schema):
    found = set()

    def walk(node):
        if isinstance(node, dict):
            if "contentMediaType" in node:
                found.add(node["contentMediaType"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(schema)
    return found


def representation_media_types(df_root, iri):
    """Format and media types of a df:Representation, read from the bblocks-data-formats sources:
    the representation's df:format, and every df:mediaType of that format (observed and inferred,
    both media types of the format, as audit_planes.py reads them)."""
    if not iri.startswith(DATA_FORMATS_BASE + "representation/"):
        sys.exit(f"{iri}: not a representation of bblocks-data-formats")
    path = df_root / "_sources" / "representation" / iri.rsplit("/", 1)[-1] / "ontology.ttl"
    if not path.exists():
        sys.exit(f"{iri}: no such representation in {df_root} (use --data-formats)")
    m = re.search(r"df:format\s+<([^>]+)>", path.read_text())
    fmt = m.group(1).rsplit("/", 1)[-1]
    types = set(re.findall(r'df:mediaType\s+"([^"]+)"', (df_root / "_sources" / "format" / fmt / "ontology.ttl").read_text()))
    if not types:
        sys.exit(f"{iri}: format {fmt} has no media type (a format always has one, decision of 2026-11-09)")
    return fmt, types


# The JSON types a deployed input/output may have to be bound to a role that names no
# representation, by the role's data type. A data type not listed here stops the generator.
LITERAL_TYPES = {
    "number": {"number", "integer"},
    "boolean": {"boolean"},
    "expression": {"string"},
    "format-identifier": {"string"},
    "coordinate-reference-system": {"string", "integer"},
    "radiometric-index": {"string"},
    # the new profiles of 2026-11-10
    "band-identifier": {"string"},
    "grid-resolution": {"number", "integer"},
    "colour-map": {"string"},
    "time-interval": {"string"},
    "collection-identifier": {"string"},
}


def _json_types(schema):
    found = set()

    def walk(node):
        if isinstance(node, dict):
            t = node.get("type")
            if t == "array" and "items" in node:
                walk(node["items"])
            elif t:
                found.update(t if isinstance(t, list) else [t])
            for k in ("oneOf", "anyOf", "allOf"):
                for v in node.get(k, []):
                    walk(v)
    walk(schema)
    return found


def binding_check(proc, pd, ip):
    """c6 of the phase-4 review: a deployed input/output bound to a role must have the nature of the
    role, before any format is compared. Bound to a role with a representation (data: raster,
    geometry, ...), it carries a media type, or it is a file name stored on the server
    (`server_side_files`) and a string. Bound to a role without one, its JSON type is one of
    LITERAL_TYPES for the role's data type, and it carries no media type. A server_side_files or
    role_decompositions entry must also be needed: one whose role names no representation stops
    the generator, as one whose representation is served does (format_check)."""
    ssf = proc.get("server_side_files") or {}
    byref = proc.get("by_reference") or {}
    for side in ("inputs", "outputs"):
        bound = (proc.get("bindings", {}).get(side) or {})
        for kind, decl in (("server_side_files", ssf), ("by_reference", byref)):
            for live, role in (decl.get(side) or {}).items():
                if bound.get(live) != role:
                    sys.exit(f"{proc['key']}: {kind} {side} {live} -> {role}: not a binding of that role")
                if not ip[side][role].get("representation"):
                    sys.exit(f"{proc['key']}: {kind} {side} {live}: role `{role}` names no representation, "
                             "the declaration is unnecessary")
                if (ssf.get(side) or {}).get(live) and (byref.get(side) or {}).get(live):
                    sys.exit(f"{proc['key']}: {side} {live} is declared both a server-side file and by reference")
        for role, d in ((proc.get("role_decompositions") or {}).get(side) or {}).items():
            # C11 (2026-11-10): a decomposition may take a literal role (a time interval given by
            # `days_back`, or by `date` + `delta`) as well as a role with a representation.
            if not d.get("parts") or not str(d.get("note", "")).strip():
                sys.exit(f"{proc['key']}: role_decompositions {side} {role}: parts and a note are required")
            if not ip[side][role].get("representation") and "reproducible" not in d:
                sys.exit(f"{proc['key']}: role_decompositions {side} {role}: a literal role's decomposition states "
                         "`reproducible` (false when the parts depend on the time of execution, as `days_back`)")
        for live, role in bound.items():
            e, schema = ip[side][role], pd[side][live].get("schema")
            dtype = e["dataType"].rsplit("/", 1)[-1]
            media, types = _media_types(schema), _json_types(schema)
            if e.get("representation"):
                declared = (ssf.get(side) or {}).get(live) == role or (byref.get(side) or {}).get(live) == role
                if not media and not (declared and types == {"string"}):
                    sys.exit(f"{proc['key']}: {side} {live} ({sorted(types)}, no media type) is bound to `{role}`, "
                             f"a {dtype} role with a representation: neither encoded data nor a declared "
                             "server-side file or reference (by_reference)")
            else:
                if dtype not in LITERAL_TYPES:
                    sys.exit(f"{proc['key']}: {side} {live} -> `{role}`: data type {dtype} has no entry in LITERAL_TYPES")
                if media or not types or types - LITERAL_TYPES[dtype]:
                    sys.exit(f"{proc['key']}: {side} {live} ({sorted(types)}{', media ' + str(sorted(media)) if media else ''}) "
                             f"is bound to `{role}`, a {dtype} role, which takes {sorted(LITERAL_TYPES[dtype])}")


def format_check(proc, pd, gp_root, df_root):
    """A4.3: compare, role by role, the representations of the Implementation Profile with the
    media types this deployment serves (`schema` of the bound inputs and outputs, decision D6).

    A role with representations is served when one of its bound inputs/outputs serves a media type
    of the representation's df:Format. Otherwise it must be declared, each with its reason:
    `server_side_files` (a file name stored on the server), `role_decompositions` (the role is taken
    as several inputs, none of which is the role) or `format_gaps` (an assumed gap: the deployment
    exposes no media type for it). An undeclared gap stops the generator, and so does a declaration
    that no longer matches a gap. Returns the rows of docs/FORMAT-CHECK.md and the entry's
    assumedFormatGaps."""
    ip_key = proc["implementsProfile"].rstrip("/").rsplit("/", 1)[-1]
    ip = json.loads((gp_root / "_sources" / "implementation-profile" / ip_key / "examples" / f"{ip_key}.json").read_text())
    binding_check(proc, pd, ip)
    ssf = proc.get("server_side_files") or {}
    byref = proc.get("by_reference") or {}
    dec = proc.get("role_decompositions") or {}
    gaps = proc.get("format_gaps") or {}
    rows, assumed = [], []
    for side in ("inputs", "outputs"):
        lives = {}
        for live, role in (proc.get("bindings", {}).get(side) or {}).items():
            lives.setdefault(role, []).append(live)
        declared_gaps = dict(gaps.get(side) or {})
        for role, e in ip[side].items():
            for rep in e.get("representation") or []:
                fmt, types = representation_media_types(df_root, rep)
                served = set().union(*(_media_types(pd[side][l].get("schema")) for l in lives.get(role, [])))
                row = {"process": bb_id(proc), "side": side, "role": role, "lives": lives.get(role, []),
                       "format": fmt, "types": sorted(types), "served": sorted(served)}
                ssf_lives = [l for l in lives.get(role, []) if (ssf.get(side) or {}).get(l) == role]
                ref_lives = [l for l in lives.get(role, []) if (byref.get(side) or {}).get(l) == role]
                gap_lives = [l for l in lives.get(role, []) if l in declared_gaps]
                dec_served = set().union(*(_media_types(pd[side][p].get("schema"))
                                           for p in ((dec.get(side) or {}).get(role) or {}).get("parts", [])))
                if types & dec_served:
                    sys.exit(f"{proc['key']}: role_decompositions {side} {role}: a part serves {fmt}, "
                             "the declaration is unnecessary")
                if types & served:
                    row["status"] = "served"
                    if gap_lives:
                        sys.exit(f"{proc['key']}: format_gaps {side} {gap_lives}: {fmt} is served, the gap is stale")
                    stale = [l for l in lives.get(role, []) if ((ssf.get(side) or {}).get(l) == role
                             or (byref.get(side) or {}).get(l) == role) and types & _media_types(pd[side][l].get("schema"))]
                    if stale:
                        sys.exit(f"{proc['key']}: server_side_files or by_reference {side} {stale}: {fmt} is served, "
                                 "the declaration is unnecessary")
                elif ssf_lives:
                    row["status"] = "server-side file"
                elif ref_lives:
                    row["status"] = "by reference"
                elif role in (dec.get(side) or {}):
                    row["status"] = "role decomposition"
                elif not lives.get(role) and role in (proc.get("unbound") or {}):
                    row["status"] = "unbound"
                    row["reason"] = " ".join(str(proc["unbound"][role]).split())
                elif gap_lives and len(gap_lives) == len(lives.get(role, [])):
                    row["status"] = "assumed gap"
                    for l in gap_lives:
                        g = declared_gaps.pop(l)
                        assumed.append({"name": l, "side": side, "implements": e["id"],
                                        "served": sorted(_media_types(pd[side][l].get("schema"))),
                                        "reason": " ".join(g["reason"].split()),
                                        "evidence": " ".join(g["evidence"].split())})
                    row["reason"] = assumed[-1]["reason"]
                else:
                    sys.exit(f"{proc['key']}: {side} role `{role}` of {ip_key} has representation {rep} "
                             f"({fmt} {sorted(types)}), but the deployment serves {sorted(served) or 'nothing'} "
                             f"for {lives.get(role) or 'no bound input/output'}: declare it (server_side_files, "
                             "role_decompositions or format_gaps, with a reason) or fix the binding")
                rows.append(row)
        if declared_gaps:
            sys.exit(f"{proc['key']}: format_gaps {side} {sorted(declared_gaps)} match no unserved representation")
    return rows, assumed


FORMAT_CHECK_HEADER = """# Tier-3 representations served by tier 4

Generated by `scripts/generate.py` (A4.3 of the tier separation), from `scripts/profiles.yaml`, the
Implementation Profiles of `bblocks-generic-profiles` and the formats of `bblocks-data-formats`.
For each process attached to an Implementation Profile (`implementsProfile`), each role that names a
representation is compared with the media types the deployment serves on the inputs/outputs bound to
that role (`schema`, as served). A role is **served** when one of them serves a media type of the
representation's `df:Format`. Otherwise the gap is declared in `scripts/profiles.yaml`, with its
reason, and the process-type entry carries it:

- **server-side file**: the deployment takes or returns the name of a file stored on the server, with
  no media type, by design (`serverSideFiles`);
- **by reference**: the deployment takes or returns a URL of the data, not the data
  (`byReference`);
- **role decomposition**: the deployment takes the role as several inputs, none of which is the
  role (`roleDecompositions`);
- **unbound**: the deployment leaves an optional role (minOccurs 0 at tier 3) unbound, with a reason;
- **assumed gap**: the deployment exposes no media type for the role (`assumedFormatGaps`).

An undeclared gap stops the generator, and so does a declaration that no longer matches a gap.

"""


def write_format_check(rows, assumed_by_process):
    lines = [FORMAT_CHECK_HEADER,
             "## Assumed gaps", ""]
    if assumed_by_process:
        lines += ["| Process | Side | Input/output | Implementation Profile role | Served | Reason | Evidence |",
                  "|---|---|---|---|---|---|---|"]
        for pid, gaps in assumed_by_process:
            for g in gaps:
                lines.append(f"| `{pid}` | {g['side'][:-1]} | `{g['name']}` | `{g['implements'].split('/def/')[-1]}` | "
                             f"{', '.join('`'+t+'`' for t in g['served']) or '--'} | {g['reason']} | {g['evidence']} |")
    else:
        lines.append("None.")
    lines += ["", "## All roles with a representation", "",
              "| Process | Side | Role | Bound to | Format | Format media types | Served | Status |",
              "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| `{r['process'].replace(PREFIX, '')}` | {r['side'][:-1]} | `{r['role']}` | "
                     f"{', '.join('`'+l+'`' for l in r['lives']) or '--'} | `{r['format']}` | "
                     f"{', '.join('`'+t+'`' for t in r['types'])} | {', '.join('`'+t+'`' for t in r['served']) or '--'} | "
                     f"{r['status']} |")
    (ROOT / "docs" / "FORMAT-CHECK.md").write_text("\n".join(lines) + "\n")


GP_ROOT = ROOT.parent / "bblocks-generic-profiles"


def tier3_link_fields(proc, assumed):
    """The tier-4 -> tier-3 link of an entry (`implementsProfile`, the canonical relation of
    docs/tier-links.md in bblocks-generic-profiles) and the declarations that qualify how this
    deployment binds the Implementation Profile's roles."""
    if not proc.get("implementsProfile"):
        return {}
    ip = proc["implementsProfile"]
    out = {"implementsProfile": ip}
    ssf = proc.get("server_side_files")
    if ssf:
        out["serverSideFiles"] = [
            {"name": live, "side": side, "implements": f"{ip}/{side}/{role}",
             "location": " ".join(ssf["location"].split())}
            for side in ("inputs", "outputs") for live, role in (ssf.get(side) or {}).items()]
    unbound = {k: v for k, v in (proc.get("unbound") or {}).items()}
    if unbound:
        # C2 (2026-11-10): the roles this deployment leaves unbound, each with its reason, so that the
        # entry declares them (audit_planes.py reads them for an optional role with a representation).
        sides = {side: set(json.loads((GP_ROOT / "_sources" / "implementation-profile" / ip.rsplit("/", 1)[-1]
                                       / "examples" / (ip.rsplit("/", 1)[-1] + ".json")).read_text())[side])
                 for side in ("inputs", "outputs")}
        out["unboundRoles"] = [
            {"side": side, "implements": f"{ip}/{side}/{role}", "reason": " ".join(str(reason).split())}
            for side in ("inputs", "outputs") for role, reason in unbound.items() if role in sides[side]]
    fixed = proc.get("fixed_roles")
    if fixed:
        # C3 (2026-11-10): the value a deployment fixes for an optional role it leaves unbound
        out["fixedRoleValues"] = [
            {"side": side, "implements": f"{ip}/{side}/{role}", "values": f["values"], "reason": " ".join(f["reason"].split())}
            for side in ("inputs", "outputs") for role, f in (fixed.get(side) or {}).items()]
    ref = proc.get("by_reference")
    if ref:
        out["byReference"] = [
            {"name": live, "side": side, "implements": f"{ip}/{side}/{role}", "note": " ".join(ref["note"].split())}
            for side in ("inputs", "outputs") for live, role in (ref.get(side) or {}).items()]
    dec = proc.get("role_decompositions")
    if dec:
        out["roleDecompositions"] = []
        for side in ("inputs", "outputs"):
            for role, d in (dec.get(side) or {}).items():
                item = {"side": side, "implements": f"{ip}/{side}/{role}", "parts": d["parts"]}
                if d.get("selectors"):
                    item["selectors"] = d["selectors"]
                if "reproducible" in d:
                    item["reproducible"] = d["reproducible"]
                item["note"] = " ".join(d["note"].split())
                out["roleDecompositions"].append(item)
    if assumed:
        out["assumedFormatGaps"] = assumed
    return out


def correspondences(oe):
    """openEO correspondences of an entry (decision D5: apart from the meaning of the type)."""
    c = {rel: [BBLOCK_IRI + t for t in oe[rel]] for rel in ("exactMatch", "closeMatch", "relatedMatch") if oe.get(rel)}
    eq = {"level": oe["level"], "rationale": " ".join(oe["rationale"].split())}
    if oe.get("decomposition"):
        eq["decomposition"] = oe["decomposition"]
    c["openeoEquivalence"] = eq
    return c


def ogcapi_profile_schema(pd, inherited=None):
    pins = {
        "type": "object",
        "required": ["id", "inputs", "outputs"],
        "properties": {
            "id": {"const": pd["id"]},
            "inputs": {"type": "object", "required": list(pd["inputs"].keys())},
            "outputs": {"type": "object", "required": list(pd["outputs"].keys())},
        },
    }
    base = [{"$ref": "bblocks://ogc.api.processes.part1.v1.schemas.process"},
            {"$ref": "bblocks://ogc.api.processes.part2.v1.schemas.staticIndicator"}, pins]
    defs = {"processTypeEntry": {"$ref": f"bblocks://{PREFIX}process-type"}}
    if inherited:
        # deep copies: a shared object would be dumped as a YAML anchor/alias
        defs["inheritedProcessDescription"] = {"allOf": copy.deepcopy(base) + [inherited]}
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "description": (f"Profile of the live OGC API - Processes processDescription of `{pd['id']}`. "
                        "Pins the process id and the input/output names. No execute/results/"
                        "provenance $defs or examples: static processDescription only (no CWLProv-"
                        "style run record exists for a live deployed service)."),
        "allOf": base,
        "$defs": defs,
    }


def generic_profiles_identifier(iri):
    # isProfileOf expects a bblocks:// URI or a bare register-local identifier (bblocks-docs
    # "Building Block relationships") -- never a plain https:// IRI, which the postprocessor
    # treats as an already-bare identifier and prefixes as-is, producing a malformed
    # "bblocks://https://..." value. `implementsProfile` on process-type is a data property and
    # correctly holds the full IRI; this converts it to the identifier form for isProfileOf.
    if not iri.startswith(GENERIC_PROFILES_BASE):
        return iri
    return "generic-profiles." + iri[len(GENERIC_PROFILES_BASE):].replace("/", ".")


def ogcapi_bblock_json(proc, pd, src):
    depends = ["ogc.api.processes.part1.v1.schemas.process", "ogc.api.processes.part2.v1.schemas.staticIndicator",
               f"{PREFIX}process-type"]
    family = src.get("family", "OGC API - Processes")
    group = src.get("group", src.get("title", "OGC API - Processes"))
    entry = {
        "$schema": "https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/ogc/bblocks/metadata-schema.yaml",
        "name": f"Process profile: {pd['id']}",
        "abstract": (f"Process profile of the live OGC API - Processes process `{pd['id']}` "
                     "(ZOO-Project, Geonovum testbed), with a process-type entry linking to its "
                     "Implementation Profile. Static processDescription only, no execute/results/provenance."),
        "status": "under-development",
        "dateTimeAddition": f"{TODAY}T00:00:00Z",
        "dateOfLastChange": TODAY,
        "version": "0.1",
        "itemClass": "schema",
        "register": "process-profiles",
        "dependsOn": depends,
        "seeAlso": ["ogc.api.processes.part1.v1.requirements.core"],
        "conformanceClasses": [PART1_CORE],
        "scope": "dev",
        "tags": ["OSPD", "process profile", "OGC API - Processes", family, proc["workflow"]],
        "sourceSchema": "schema.yaml",
        "maturity": "development",
        "group": group,
    }
    # Implementation (instance level) is a profile of its Implementation Profile (bblocks-docs
    # "Building Block relationships": isProfileOf, not dependsOn -- there is no bblocks:// $ref
    # for it anywhere in this schema, only a plain IRI on the process-type entry's own
    # `implementsProfile` data property; isProfileOf is the metadata-level declaration of the
    # same relationship, read by the register/viewer independently of that data field. Extension
    # points (bblocks-docs "Extension points") do not apply here: that mechanism substitutes a
    # nested schema $ref throughout an inheritance chain, and this processDescription schema
    # never references generic-profiles.implementation-profile.* in the first place.
    if proc.get("implementsProfile"):
        entry["isProfileOf"] = generic_profiles_identifier(proc["implementsProfile"])
    return entry


def inherited_example(proc):
    unbound = "".join(f" `{k}` is not bound: {v}." for k, v in proc.get("unbound", {}).items())
    for side in ("inputs", "outputs"):
        for k, d in (proc.get("role_decompositions", {}).get(side) or {}).items():
            unbound += (f" `{k}` is taken as {', '.join('`'+p+'`' for p in d['parts'])}, none of which is the role: "
                        "declared in `roleDecompositions` of the process-type entry.")
    return {"title": "processDescription with its inheritance (Implementation, instance level)",
            "content": ("The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation "
                        f"(instance level) of `{proc['implementsProfile']}`: the Implementation Profile's keywords "
                        "(E) on the process and on each bound input/output, and, per footnote a, its list of "
                        "metadata references to superior profiles extended with a Table 22 `implementation` "
                        "reference to the Implementation Profile -- on the process only. Each bound input/output "
                        "keeps its Implementation Profile counterpart's reference to the Generic Profile input/output "
                        "(`generic-input`/`-output`) and adds one to that counterpart itself "
                        "(`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/"
                        "`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole "
                        "profiles. Each bound input/output also carries the `dataType` of that counterpart, a "
                        "concept of bblocks-data-types. Which deployed "
                        "input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; "
                        "inputs/outputs bound to none are the deployment's own additions (footnote b)."
                        + unbound + " Not what the deployment serves today (docs/OPEN-QUESTIONS.md "
                        "Q-TABLE21-INSTANCE)."),
            "snippets": [{"language": "json", "ref": "examples/processDescription.inherited.json",
                          "schema-ref": "#/$defs/inheritedProcessDescription"}]}


def ogcapi_examples_yaml(proc, url):
    ex = [
        {"title": "Source (referenced)",
         "content": f"The processDescription is fetched from the live service, not copied: <{url}>."},
        {"title": "processDescription",
         "content": "Live OGC API - Processes processDescription, normalised (ZOO-Project-internal fields dropped).",
         "snippets": [{"language": "json", "ref": "examples/processDescription.json"}]},
        inherited_example(proc),
        {"title": "process-type entry",
         "content": f"Registered ActivityType OWL class `{ptype_iri(proc)}` (`{PREFIX}process-type`), proposed by GeoLabs and awaiting a register decision, linking to its Implementation Profile.",
         "snippets": [{"language": "json", "ref": "examples/process-type.json", "schema-ref": "#/$defs/processTypeEntry"}]},
    ]
    return [e if not e.get("snippets")
            else {"title": e["title"], "base-uri": PROCESS_BASE, **{k: v for k, v in e.items() if k != "title"}}
            for e in ex]


def ogcapi_description_md(proc, pd, url, gp_root):
    """description.md of a live process profile: what the process is (and, for a wrapped tool such
    as OTB or SAGA, the tool's own documentation, from `tool` in profiles.yaml), what it implements,
    and how its inputs/outputs bind to that Implementation Profile."""
    ip_iri = proc["implementsProfile"]
    ip_key = ip_iri.rstrip("/").rsplit("/", 1)[-1]
    ip = json.loads((gp_root / "_sources" / "implementation-profile" / ip_key / "examples" / f"{ip_key}.json").read_text())
    parts = [f"Process profile of the live OGC API - Processes process `{pd['id']}` "
             f"(ZOO-Project, Geonovum testbed): <{url}>.", "",
             f"> {' '.join((pd.get('description') or pd.get('title') or '').split())}", "",
             "(the process's own description, as served)"]
    tool = proc.get("tool")
    if tool:
        parts += ["", "## The tool behind it", "",
                  f"[{tool['name']}]({tool['doc']}) -- {tool['documented']}.", ""]
        if tool.get("summary"):
            parts += [f"> **{tool['summary']}**", ">", f"> {' '.join(tool['excerpt'].split())}", "",
                      f"Quoted from the {tool['license']}."]
        if tool.get("description"):
            parts += [" ".join(tool["description"].split())]
        if tool.get("notes"):
            parts += ["", "On this deployment:", ""] + [f"- {n}" for n in tool["notes"]]
    ssf = proc.get("server_side_files")
    if ssf:
        parts += ["", "## Inputs and outputs passed as server-side file names", "",
                  " ".join(ssf["location"].split()), "",
                  "| Live | Side | Implementation Profile role, whose format the file has |", "|---|---|---|"]
        for side in ("inputs", "outputs"):
            for live, role in (ssf.get(side) or {}).items():
                parts.append(f"| `{live}` | {side[:-1]} | [`{role}`]({ip_iri}/{side}/{role}) |")
        parts += ["", "This deployment serves no media type for them: not a format gap. The entry declares them "
                  "in `serverSideFiles` of `process-type.json`."]
    parts += ["", "## Implementation Profile", ""] + md_binding(proc, pd, gp_root, None)
    parts += ["", "## Examples", "",
              "- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.",
              "- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at "
              "the Implementation (instance level): keywords and metadata references to its profiles, and the "
              "data type of each bound input/output.",
              "- `process-type.json`: its candidate process-type entry."]
    return "\n".join(parts) + "\n"


def md_binding(proc, pd, gp_root, why):
    """The binding of a deployed process to its Implementation Profile, as Markdown lines: which
    deployed input/output implements which role, with the role's data type; the deployment's own
    additions; role decompositions and assumed format gaps."""
    ip_iri = proc["implementsProfile"]
    ip_key = ip_iri.rstrip("/").rsplit("/", 1)[-1]
    ip = json.loads((gp_root / "_sources" / "implementation-profile" / ip_key / "examples" / f"{ip_key}.json").read_text())
    b, unbound = proc.get("bindings", {}), proc.get("unbound", {})
    dec, gaps = proc.get("role_decompositions", {}), proc.get("format_gaps", {})
    lines = [f"Implements [`{ip['prefLabel']}`]({ip_iri}) "
             f"(`{generic_profiles_identifier(ip_iri)}`, bblocks-generic-profiles)."
             + (f" {why}" if why else ""), "",
             "Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), "
             "with the data type each bound input/output inherits (`processDescription.inherited.json`):", "",
             "| Deployed | Implementation Profile | Data type |", "|---|---|---|"]
    for side in ("inputs", "outputs"):
        rev = {}
        for live, role in b.get(side, {}).items():
            rev.setdefault(role, []).append(live)
        for name, e in ip[side].items():
            lives = rev.get(name, [])
            d = (dec.get(side) or {}).get(name)
            if d:
                cell = ", ".join(f"`{p}`" for p in d["parts"]) + " (role decomposition)"
            else:
                cell = ", ".join(f"`{l}`" for l in lives) or "--"
            note = f" (unbound: {' '.join(str(unbound[name]).split())})" if not lives and not d and name in unbound else ""
            fx = ((proc.get("fixed_roles") or {}).get(side) or {}).get(name)
            if fx:
                note += f"; fixed by the deployment: {', '.join(fx['values'])}"
            lines.append(f"| {cell} | {side[:-1]} `{name}`{note} | `{e['dataType'].rsplit('/', 1)[-1]}` |")
        parts_of = {p for d in (dec.get(side) or {}).values() for p in d["parts"]}
        extra = [k for k in pd[side] if k not in b.get(side, {}) and k not in parts_of]
        if extra:
            lines.append(f"| {', '.join(f'`{k}`' for k in extra)} | -- (the deployment's own {side}, Table 21 footnote b) | -- |")
    for side in ("inputs", "outputs"):
        for name, d in (dec.get(side) or {}).items():
            lines += ["", f"**Role decomposition.** The {side[:-1]} `{name}` is taken as "
                      + ", ".join(f"`{p}`" for p in d["parts"])
                      + (" (only with " + " and ".join(f"`{c['name']}` in " + ", ".join(f"`{v}`" for v in c["values"])
                                                       for c in d["selectors"]) + ")" if d.get("selectors") else "")
                      + ": " + " ".join(d["note"].split())
                      + (" Not reproducible: the parts depend on the time of execution." if d.get("reproducible") is False else "")
                      + " Declared in `roleDecompositions` of `process-type.json`"
                      + ("; its representation is not served (`docs/FORMAT-CHECK.md`)." if ip[side][name].get("representation") else ".")]
        for live, role in ((proc.get("by_reference") or {}).get(side) or {}).items():
            lines += ["", f"**By reference.** `{live}` (role `{role}`) is a URL of the data, not the data: "
                      + " ".join(proc["by_reference"]["note"].split())
                      + " Declared in `byReference` of `process-type.json` (`docs/FORMAT-CHECK.md`)."]
        for live, g in (gaps.get(side) or {}).items():
            lines += ["", f"**Assumed format gap.** `{live}`: " + " ".join(g["reason"].split())
                      + " Evidence: " + " ".join(g["evidence"].split())
                      + " Declared in `assumedFormatGaps` of `process-type.json` (`docs/FORMAT-CHECK.md`)."]
    return lines


def generate_ogcapi_profiles(sources, roots, by_key, ogcapi_procs, gp_root, df_root, checks):
    for proc in ogcapi_procs:
        src = sources[proc["source"]["repo"]]
        raw, pd, url = load_ogcapi_process(proc, sources, roots)
        out = ROOT / "_sources" / proc["workflow"] / proc["key"]
        exd = out / "examples"
        for f in exd.glob("*.json"):
            f.unlink()
        dump_json(exd / "processDescription.json", pd)
        inherited, inherited_schema = inherited_process_description(proc, pd, gp_root)
        dump_json(exd / "processDescription.inherited.json", inherited)
        rows, assumed = format_check(proc, pd, gp_root, df_root)
        checks.append((proc, rows, assumed))
        entry = ogcapi_process_type_entry(proc, pd, src, url, by_key, assumed, parent_activity_type(proc, gp_root))
        dump_json(exd / "process-type.json", entry)
        dump_json(out / "context.jsonld", PROFILE_CONTEXT)
        dump_yaml(out / "schema.yaml", ogcapi_profile_schema(pd, inherited_schema))
        dump_yaml(out / "examples.yaml", ogcapi_examples_yaml(proc, url))
        dump_json(out / "bblock.json", ogcapi_bblock_json(proc, pd, src))
        (out / "description.md").write_text(ogcapi_description_md(proc, pd, url, gp_root))
        print(f"{bb_id(proc):60s} {'OGCAPIProcess':16s} (static processDescription only)")


def all_activity_types(gp_root):
    out = {}
    for f in sorted((gp_root / "_sources" / "activity-type").glob("*/examples/*.json")):
        at = json.loads(f.read_text())
        out[at["id"]] = at
    return out


def sync_process_type_schema(pt, gp_root):
    """Write into the otherwise hand-written process-type schema what comes from elsewhere:
    ATR_ITEM_CLASS, and the parents an entry may specialise -- acttype:ActivityType, or one of the
    activity types of bblocks-generic-profiles (an enum, so that no other value passes)."""
    path = pt / "schema.yaml"
    schema = yaml.safe_load(path.read_text())
    props = schema["allOf"][1]["properties"]
    props["itemClass"]["const"] = ATR_ITEM_CLASS
    props["subClassOf"]["enum"] = [ACTIVITY_TYPE_CLASS] + sorted(all_activity_types(gp_root))
    dump_yaml(path, schema)


def write_process_type_fixtures(pt):
    """JSON fixtures of the process-type schema, each the entry of kindgrove-steps.reproject-band
    with one defect, so that they follow the entries: a parent class outside the enum,
    a specialisation without entity type; a `byReference` entry (control) and one without
    `implements`, a literal role decomposition (control) and one without parts. The controls check
    the schema only: they do not describe the deployment of reproject-band. The schema no longer
    checks the type or classification of an amendment (decision Q5, option b, of 2026-11-11), so
    the fixtures amendment-without-classification-fail and amendment-correctional-fail are gone.
    `notAttached` (decision Q1, 2026-11-11): on the entry of kindgrove-steps.export-stac, a
    CommandLineTool attached to no profile, a control and a reason empty or missing; on
    reproject-band, `notAttached` next to `implementsProfile`."""
    base = json.loads((ROOT / "_sources/kindgrove-steps/reproject-band/examples/process-type.json").read_text())
    unattached = json.loads((ROOT / "_sources/kindgrove-steps/export-stac/examples/process-type.json").read_text())
    if "notAttached" not in unattached or "notAttached" in base:
        sys.exit("process-type fixtures: export-stac must carry notAttached and reproject-band must not")

    IP_RASTER_IN = GENERIC_PROFILES_BASE + "implementation-profile/raster-reprojection/inputs/raster"
    IP_CRS_IN = GENERIC_PROFILES_BASE + "implementation-profile/raster-reprojection/inputs/targetCRS"

    cases = {
        "arbitrary-parent-fail.json": lambda d: d.update(subClassOf="https://example.org/not-an-activity-type"),
        "specialised-without-entity-type-fail.json": lambda d: [d.pop(k) for k in ("usedEntityType", "generatedEntityType")],
        # C1 and C11 (2026-11-10): a reference to the data, and a decomposition of a literal role
        "by-reference-control.json": lambda d: d.update(byReference=[
            {"name": "band_file", "side": "inputs", "implements": IP_RASTER_IN, "note": "A URL of the GeoTIFF."}]),
        "by-reference-without-implements-fail.json": lambda d: d.update(byReference=[
            {"name": "band_file", "side": "inputs", "note": "A URL of the GeoTIFF."}]),
        "literal-decomposition-control.json": lambda d: d.update(roleDecompositions=[
            {"side": "inputs", "implements": IP_CRS_IN, "parts": ["epsg"], "reproducible": True, "note": "An EPSG code."}]),
        # C3 (2026-11-10): the value fixed for an optional role left unbound
        "unbound-role-without-reason-fail.json": lambda d: d.update(unboundRoles=[
            {"side": "inputs", "implements": IP_CRS_IN}]),
        "fixed-role-values-without-reason-fail.json": lambda d: d.update(fixedRoleValues=[
            {"side": "inputs", "implements": IP_CRS_IN, "values": ["EPSG:4326"]}]),
        "fixed-role-values-empty-reason-fail.json": lambda d: d.update(fixedRoleValues=[
            {"side": "inputs", "implements": IP_CRS_IN, "values": ["EPSG:4326"], "reason": ""}]),
        "by-reference-empty-note-fail.json": lambda d: d.update(byReference=[
            {"name": "band_file", "side": "inputs", "implements": IP_RASTER_IN, "note": ""}]),
        "fixed-role-values-empty-fail.json": lambda d: d.update(fixedRoleValues=[
            {"side": "inputs", "implements": IP_CRS_IN, "values": [], "reason": "No value."}]),
        "role-decomposition-without-parts-fail.json": lambda d: d.update(roleDecompositions=[
            {"side": "inputs", "implements": IP_CRS_IN, "parts": [], "reproducible": True, "note": "No part."}]),
    }
    for name, defect in cases.items():
        d = copy.deepcopy(base)
        defect(d)
        dump_json(pt / "tests" / name, d)
    unattached_cases = {
        "not-attached-control.json": lambda d: None,
        "not-attached-empty-reason-fail.json": lambda d: d.update(notAttached={"reason": ""}),
        "not-attached-without-reason-fail.json": lambda d: d.update(notAttached={}),
    }
    for name, defect in unattached_cases.items():
        d = copy.deepcopy(unattached)
        defect(d)
        dump_json(pt / "tests" / name, d)
    d = copy.deepcopy(base)
    d["notAttached"] = {"reason": "Not attached, yet implementsProfile is set."}
    dump_json(pt / "tests" / "not-attached-with-implements-fail.json", d)


def write_parent_closure(pt, gp_root):
    """_sources/process-type/activity-type-parents.ttl, a data resource of the process-type block,
    so in the SHACL closure of every process profile: for each activity type of
    bblocks-generic-profiles, its rdfs:subClassOf geoproc:GeoprocessingActivityType and its entity
    types, as that register states them. With it, geoproc:GeoprocessingActivityTypesShape (Activity
    Type Register) reaches a process type that specialises one of them, and pp:ProcessTypeShape
    compares the entity types. The activity types are not typed here: they are items of
    bblocks-generic-profiles, validated there, and the shapes that target acttype:ActivityType must
    not run on them in this register."""
    lines = ["# Generated by scripts/generate.py from the activity types of bblocks-generic-profiles. Do not edit.",
             "# Only what the shapes of this register need: each activity type's parent class and entity types.",
             "@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .",
             f"@prefix acttype: <{ACTTYPE_NS}> .", ""]
    for iri, at in all_activity_types(gp_root).items():
        triples = [f"rdfs:subClassOf <{at['subClassOf']}>"]
        for k in ("usedEntityType", "generatedEntityType"):
            for v in _lst(at.get(k) or []):
                triples.append(f"acttype:{k} <{v}>")
        lines.append(f"<{iri}> " + " ;\n    ".join(triples) + " .")
    (pt / "activity-type-parents.ttl").write_text("\n".join(lines) + "\n")


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources-root", type=Path, default=ROOT.parent)
    ap.add_argument("--w1", type=Path)
    ap.add_argument("--w2", type=Path)
    ap.add_argument("--w3", type=Path)
    ap.add_argument("--kindgrove-steps", type=Path)
    ap.add_argument("--eoap-cct", type=Path)
    ap.add_argument("--runs-root", type=Path,
                    help="directory holding the CWLProv research objects named in scripts/sources.yaml `runs:` "
                         "(default: --sources-root)")
    ap.add_argument("--generic-profiles", type=Path, default=ROOT.parent / "bblocks-generic-profiles",
                    help="checkout of bblocks-generic-profiles, read for the Implementation Profiles the live "
                         "processes inherit from (default: the sibling directory, as in .volumes)")
    ap.add_argument("--data-formats", type=Path, default=ROOT.parent / "bblocks-data-formats",
                    help="checkout of bblocks-data-formats, read for the formats and media types of the "
                         "Implementation Profiles' representations (A4.3; default: the sibling directory)")
    a = ap.parse_args()
    global GP_ROOT
    GP_ROOT = a.generic_profiles
    if not (a.generic_profiles / "_sources" / "implementation-profile").is_dir():
        sys.exit(f"{a.generic_profiles}: not a bblocks-generic-profiles checkout (use --generic-profiles)")
    if not (a.data_formats / "_sources" / "representation").is_dir():
        sys.exit(f"{a.data_formats}: not a bblocks-data-formats checkout (use --data-formats)")

    sources = yaml.safe_load((SCRIPTS / "sources.yaml").read_text())
    cfg = yaml.safe_load((SCRIPTS / "profiles.yaml").read_text())
    d, procs = cfg["defaults"], cfg["processes"]
    ogcapi_procs = cfg.get("ogcapi_processes", [])
    all_procs = procs + ogcapi_procs
    if (len(procs), len(ogcapi_procs)) != (POPULATIONS["cwl"], POPULATIONS["live"]):
        sys.exit(f"scripts/profiles.yaml: {len(procs)} CWL and {len(ogcapi_procs)} live processes, the register "
                 f"declares {POPULATIONS['cwl']} and {POPULATIONS['live']} (POPULATIONS, bblocks-config.yaml, README)")
    for proc in procs:
        # A4.1: every CWL process records whether it is attached to an Implementation Profile, and
        # why not when it is not; an attachment is a hypothesis checked against the signature.
        att = proc.get("tier3")
        if not att or att.get("status") not in ("attached", "not attached") or not att.get("reason"):
            sys.exit(f"{proc['key']}: `tier3: {{status: attached | not attached, reason: ...}}` is required")
        if (att["status"] == "attached") != bool(proc.get("implementsProfile")):
            sys.exit(f"{proc['key']}: tier3.status and implementsProfile disagree")
    by_key = {p["key"]: p for p in all_procs}
    if len(by_key) != len(all_procs):
        dupes = sorted({p["key"] for p in all_procs if [q["key"] for q in all_procs].count(p["key"]) > 1})
        sys.exit(f"scripts/profiles.yaml: duplicate key(s) {dupes} -- `key` must be unique across "
                 "the whole file (steps/parents references and by_key lookups are not workflow-scoped)")
    roots = {"w1": a.w1 or a.sources_root / sources["w1"]["clone"],
             "w2": a.w2 or a.sources_root / sources["w2"]["clone"],
             "w3": a.w3 or a.sources_root / sources["w3"]["clone"],
             "kindgrove_steps": a.kindgrove_steps or a.sources_root / sources["kindgrove_steps"]["clone"]}
    # Local only: scripts/sources-local.yaml (git-ignored; none in use since 2026-11-11), may point a source to
    # another local directory, e.g. a CWL generated from an unreleased commit, while sources.yaml
    # keeps the committed pin. Announced on stderr, so that a regeneration with it is not mistaken
    # for one from the pins.
    local_overrides = SCRIPTS / "sources-local.yaml"
    if local_overrides.exists():
        for key, o in (yaml.safe_load(local_overrides.read_text()) or {}).items():
            if key not in roots or not (Path(o["path"]) / sources[key]["base_path"]).is_dir():
                sys.exit(f"scripts/sources-local.yaml: {key}: unknown source or missing directory {o.get('path')}")
            roots[key] = Path(o["path"])
            print(f"LOCAL OVERRIDE {key}: {o['path']} instead of the pin of scripts/sources.yaml ({' '.join(o['note'].split())})",
                  file=sys.stderr)
    # every live-process source (sources.yaml `kind: ogcapi-process`) is cached under --sources-root
    roots.update({k: a.sources_root / v["clone"] for k, v in sources.items()
                  if isinstance(v, dict) and v.get("kind") == "ogcapi-process"})
    eoap = a.eoap_cct or a.sources_root / sources["eoap_cct"]["clone"]
    jq_path = eoap / sources["eoap_cct"]["transform"]
    # real run records: local research objects, never downloaded (like the CWL clones)
    runs_root = a.runs_root or a.sources_root
    bags = {}
    for name, r in sources.get("runs", {}).items():
        p = Path(r["bag"])
        p = p if p.is_absolute() else runs_root / p
        if not (p / "metadata" / "provenance").is_dir():
            sys.exit(f"run {name}: research object not found at {p} (see scripts/sources.yaml `runs:`, --runs-root)")
        bags[name] = load_bag(p)
        bags[name]["note"] = r.get("note", "")

    openeo_reg = a.sources_root / "bblocks-openeo" / "build" / "register.json"
    known = None
    if openeo_reg.exists():
        known = {b["itemIdentifier"] for b in json.loads(openeo_reg.read_text())["bblocks"]}

    summary, checks = [], []
    for proc in procs:
        src = sources[proc["source"]["repo"]]
        cwl_doc, cwl_el, url = load_process(proc, sources, roots)
        proc["cwl_class"] = cwl_el["class"]
        # Decision Q1: a Workflow is recognised by its steps, and only a CommandLineTool gets notAttached.
        if (cwl_el["class"] == "Workflow") != bool(proc.get("steps")):
            sys.exit(f"{proc['key']}: CWL class {cwl_el['class']} but steps {proc.get('steps')}")
        if not_attached(proc) and cwl_el["class"] != "CommandLineTool":
            sys.exit(f"{proc['key']}: notAttached is for a CommandLineTool, not a {cwl_el['class']}")
        ns = cwl_doc.get("$namespaces", {})
        raw = run_transform(cwl_doc, jq_path)
        pd, corrections = correct(raw, cwl_el, ns, proc.get("secrets"), proc.get("stac_catalog"))
        corrected = bool(corrections)

        if known:
            oe = proc["openeo"]
            ids = oe.get("exactMatch", []) + oe.get("closeMatch", []) + oe.get("relatedMatch", [])
            ids += [x for s in oe.get("decomposition", []) or [] for x in s.get("openeo", [])]
            missing = [i for i in ids if i not in known]
            if missing:
                sys.exit(f"{proc['key']}: unknown openEO identifiers {missing}")

        out = ROOT / "_sources" / proc["workflow"] / proc["key"]
        exd = out / "examples"
        for f in exd.glob("*.json"):
            f.unlink()
        job_id = f"{proc['workflow']}-{proc['key']}-0001"
        info = run_info(proc, bags)
        image = info["image"] or docker_image(cwl_el, cwl_doc)
        exe = execute_doc(proc, d)
        res = results_doc(proc, d, job_id, info)
        chain, run_id = provenance_chain(proc, pd, exe, res, info, image, d)

        dump_json(exd / "processDescription.json", pd)
        if corrected:
            dump_json(exd / "processDescription.raw.json", raw)
        dump_json(exd / "ogcapppkg.json", {
            "processDescription": {"process": {"id": pd["id"], "version": pd["version"]}},
            "executionUnit": execution_unit(url),
        })
        dump_json(exd / "execute.json", exe)
        dump_json(exd / "results.json", res)
        dump_json(exd / "provenance.json", chain)
        has_exec = False
        if cwl_el["class"] == "Workflow":
            bundle = execution_bundle(proc, pd, run_id, info, job_id, d)
            if bundle:
                dump_json(exd / "execution.json", bundle)
                has_exec = True
        else:
            parents = proc.get("parents") or []
            parent_run = f"urn:example:run:{proc['workflow']}:{parents[0]}" if parents else None
            dump_json(exd / "process-run.json", process_run(proc, pd, run_id, info, parent_run))
        inherited_schema, assumed = None, []
        if proc.get("implementsProfile"):
            inherited, inherited_schema = inherited_process_description(proc, pd, a.generic_profiles)
            dump_json(exd / "processDescription.inherited.json", inherited)
            rows, assumed = format_check(proc, pd, a.generic_profiles, a.data_formats)
            checks.append((proc, rows, assumed))
        entry = process_type_entry(proc, pd, cwl_el, src, url, by_key, assumed, parent_activity_type(proc, a.generic_profiles))
        dump_json(exd / "process-type.json", entry)
        w3c_prov_example(info, exd)

        dump_json(out / "context.jsonld", PROFILE_CONTEXT)
        dump_yaml(out / "schema.yaml", profile_schema(proc, pd, cwl_el, has_exec, inherited_schema))
        dump_yaml(out / "examples.yaml", examples_yaml(proc, cwl_el, url, corrected, has_exec))
        dump_json(out / "bblock.json", bblock_json(proc, pd, cwl_el, corrections, has_exec, by_key))
        (out / "description.md").write_text(description_md(proc, pd, cwl_el, url, src, corrections, has_exec, info, by_key, sources["eoap_cct"]["commit"], a.generic_profiles))

        summary.append({"id": bb_id(proc), "key": proc["key"], "class": cwl_el["class"], "pd_id": pd["id"],
                        "phases": proc["phases"], "openeo": proc["openeo"], "corrections": corrections,
                        "execution": has_exec, "cct": proc.get("cct", []),
                        "inputs": len(pd["inputs"]), "outputs": len(pd["outputs"]),
                        "implementsProfile": proc.get("implementsProfile")})
        print(f"{bb_id(proc):60s} {cwl_el['class']:16s} corrections={len(corrections)} exec={has_exec}")

    generate_ogcapi_profiles(sources, roots, by_key, ogcapi_procs, a.generic_profiles, a.data_formats, checks)
    write_format_check([r for _, rows, _ in checks for r in rows],
                       [(bb_id(p).replace(PREFIX, ""), g) for p, _, g in checks if g])
    write_attachments(procs, a.generic_profiles)

    # shared process-type example: reproject-image entry
    pt = ROOT / "_sources" / "process-type"
    # The substantive/clarifying row of pp:specification is quoted word for word in the block
    # description (decision Q3, 2026-11-11): stop if the two differ.
    rule = re.search(r'"(What is substantive here[^"]*)"@en', (pt / "ontology.ttl").read_text())
    if not rule or rule.group(1) not in (pt / "description.md").read_text():
        sys.exit("_sources/process-type/description.md does not quote the substantive/clarifying row of "
                 "pp:specification (ontology.ttl) word for word")
    sync_process_type_schema(pt, a.generic_profiles)
    write_process_type_fixtures(pt)
    write_parent_closure(pt, a.generic_profiles)
    dump_json(pt / "examples" / "reproject-image.json",
              json.loads((ROOT / "_sources/algae-bloom/reproject-image/examples/process-type.json").read_text()))
    dump_json(pt / "examples" / "kindgrove-mangrove.json",
              json.loads((ROOT / "_sources/kindgrove/mangrove/examples/process-type.json").read_text()))
    dump_json(pt / "examples" / "kindgrove-steps-reproject-band.json",
              json.loads((ROOT / "_sources/kindgrove-steps/reproject-band/examples/process-type.json").read_text()))
    dump_json(pt / "examples" / "raster-extract-roi.json",
              json.loads((ROOT / "_sources/raster/extract-roi/examples/process-type.json").read_text()))
    dump_yaml(pt / "examples.yaml", [
        {"title": "reproject-image (closeMatch, not attached to tier 3)", "base-uri": PROCESS_BASE,
         "snippets": [{"language": "json", "ref": "examples/reproject-image.json"}]},
        {"title": "KindGrove mangrove (none, with decomposition)", "base-uri": PROCESS_BASE,
         "snippets": [{"language": "json", "ref": "examples/kindgrove-mangrove.json"}]},
        {"title": "KindGrove steps reproject-band (CWL, attached to raster-reprojection, specialising its activity type)",
         "base-uri": PROCESS_BASE,
         "snippets": [{"language": "json", "ref": "examples/kindgrove-steps-reproject-band.json"}]},
        {"title": "OTB.ExtractROI (live, attached to raster-crop, role decomposition)", "base-uri": PROCESS_BASE,
         "snippets": [{"language": "json", "ref": "examples/raster-extract-roi.json"}]},
        {"title": "The register, its specification and its amendment action type",
         "content": "The ontology of this block, validated as data: this checks `pp:register` and `pp:specification` "
                    "against the shapes of the Registered Item Model.",
         "snippets": [{"language": "turtle", "ref": "ontology.ttl"}]},
    ])

    # README tables, one per population (A4.5), between their markers
    rows = ["| Identifier | CWL class | Phase(s) | openEO | Implementation Profile (tier 3) |",
            "|---|---|---|---|---|"]
    for s in summary:
        oe = s["openeo"]
        tgt = ", ".join(t.split("ogc.openeo.")[-1] for t in oe.get("exactMatch", []) + oe.get("closeMatch", []))
        ip = s["implementsProfile"]
        rows.append(f"| `{s['id']}` | {s['class']} | {', '.join(PHASE_LABELS[p] for p in s['phases'])} | "
                    f"{oe['level']}{(': ' + tgt) if tgt else ''} | {('`' + generic_profiles_identifier(ip) + '`') if ip else 'not attached'} |")
    live_rows = ["| Identifier | Live process | Phase(s) | Implementation Profile (tier 3) |", "|---|---|---|---|"]
    for proc in ogcapi_procs:
        live_rows.append(f"| `{bb_id(proc)}` | `{Path(proc['source']['file']).stem}` | "
                         f"{', '.join(PHASE_LABELS[p] for p in proc['phases'])} | "
                         f"`{generic_profiles_identifier(proc['implementsProfile'])}` |")
    readme = (ROOT / "README.md").read_text()
    for marker, table in (("CWL_TABLE", rows), ("LIVE_TABLE", live_rows)):
        start, end = f"<!-- {marker} -->", f"<!-- /{marker} -->"
        if readme.count(start) != 1 or readme.count(end) != 1:
            sys.exit(f"README.md: markers {start} ... {end} are required once each")
        readme = re.sub(re.escape(start) + r".*?" + re.escape(end),
                        lambda m: start + "\n" + "\n".join(table) + "\n" + end, readme, count=1, flags=re.S)
    (ROOT / "README.md").write_text(readme)
    dump_json(SCRIPTS / "generated-summary.json", summary)
    write_openeo_doc(summary)


OPENEO_HEADER = """# openEO equivalence decisions

Proposed correspondences between the process profiles and the openEO Building Blocks of
[GeoLabs/bblocks-openeo](https://github.com/GeoLabs/bblocks-openeo) (`ogc.openeo.*`, stable
processes of openeo-processes 2.0.0-rc.2). Offered for review, not settled equivalences.
Generated from `scripts/profiles.yaml` by `scripts/generate.py`.

## Criteria

| Level | Used when |
|---|---|
| **exactMatch** | same operation, same parameter semantics, same output type. None found. |
| **closeMatch** | same operation, but a different I/O model (files or URLs vs openEO data cubes), or a parameter subset/superset. |
| **none** | no single openEO process: the step is a composition (process graph), an opaque tool, or a structural helper. |

`relatedMatch` (SKOS) is used for type-level links (e.g. a bounding-box input vs
`ogc.openeo.types.bounding-box`) and for math processes used inside a callback; it never expresses
process equivalence. Composite and opaque processes carry a stage-by-stage `decomposition` in their
process-type entry. openEO `proposals/` (e.g. `load_stac`) are out of scope because
bblocks-openeo only models stable processes.

## Decisions (to be confirmed by Gérald before commit)

| # | Profile | Level | exactMatch / closeMatch | relatedMatch | Rationale (short) |
|---|---|---|---|---|---|
"""


ATTACHMENTS_HEADER = """# Attachment of the CWL processes to the tiers

Generated by `scripts/generate.py` from `tier3` in `scripts/profiles.yaml` (A4.1 of the tier
separation). Each of the {cwl} CWL processes of the OSPD reference workflows is compared with the
signatures of `bblocks-generic-profiles`: its inputs and outputs (as derived from its CWL) against the
roles of the candidate Implementation Profile (tier 3), of the Generic Profile it refines (tier 2) and
of that profile's Process Concept (tier 1).

**The rule, as applied.** A process is attached (`implementsProfile`) when the activity type of the
profile means what the process does, and every role of the Implementation Profile is accounted for:
bound to one or more of its inputs/outputs of the role's nature and within the role's cardinality
(`bindings`; the generator checks the nature), taken as several inputs declared as a role
decomposition (`role_decompositions`, for a role with a representation or a literal role), or, for
a role whose `minOccurs` is 0 at tier 3, left unbound with a reason (`unbound`, decision C2 of
2026-11-10). It may have inputs/outputs of its own (Table 21 footnote b). A process with no fitting
profile is listed as not attached, with the reason and, where one exists, the closest profile; it is
not forced. A gap in the tiers may justify a new Generic or Implementation Profile: listed as
proposals. The six profiles decided on 2026-11-10 exist in bblocks-generic-profiles (`5e5a808`);
the ten processes they serve were attached the same day.

**What the entry records (decision Q1 of 2026-11-11).** Every CWL CommandLineTool (an entry with
`plan` and no `hasStep`) has either `implementsProfile` or `notAttached` with a non-empty reason, the
reason of this table, in its `process-type.json`; never both. A Workflow (`hasStep`) carries neither:
its steps are compared with the tiers one by one. Of the {cwl} CWL processes, {clt} are
CommandLineTools, {attached} attached and {not_attached} not attached, and {workflows} are Workflows.
`audit_planes.py` checks this rule.

**The testbed exception.** The {live} live processes of the Geonovum testbed are all attached, one per
Implementation Profile (README, second table): each is the deployment from which its Implementation
Profile was written. They may in addition leave unbound a role of `minOccurs` 1 that the deployment
exposes no input for, with its reason. One does: `raster.radiometric-index` leaves `index` of
radiometric-index unbound (OTB RadiometricIndices' `list` parameter is not exposed).
`raster.extract-roi` takes `areaOfInterest` of raster-crop as a declared role decomposition, which
the rule allows, only with `mode.extent.unit` in `phy` or `lonlat`.
"""


def write_attachments(procs, gp_root):
    load = lambda tier, k: json.loads((gp_root / "_sources" / tier / k / "examples" / f"{k}.json").read_text())
    tail = lambda iri: iri.rstrip("/").rsplit("/", 1)[-1]
    workflows = sum(bool(p.get("steps")) for p in procs)
    attached = sum(bool(p.get("implementsProfile")) for p in procs if not p.get("steps"))
    lines = [ATTACHMENTS_HEADER.format(cwl=POPULATIONS["cwl"], live=POPULATIONS["live"],
                                       clt=len(procs) - workflows, attached=attached,
                                       not_attached=sum(not_attached(p) for p in procs), workflows=workflows),
             "| Process | CWL class | Status | Tier 3 Implementation Profile | Tier 2 Generic Profile | Tier 1 Process Concept | Reason |",
             "|---|---|---|---|---|---|---|"]
    proposals = []
    for proc in procs:
        att = proc["tier3"]
        t3 = t2 = t1 = "--"
        if proc.get("implementsProfile"):
            ip = load("implementation-profile", tail(proc["implementsProfile"]))
            gp = load("generic-profile", tail(ip["refinesGenericProfile"]))
            t3, t2 = f"`{tail(ip['id'])}`", f"`{tail(gp['id'])}`"
            t1 = ", ".join(f"`{tail(c)}`" for c in gp["broader"])
        reason = " ".join(att["reason"].split())
        if att.get("closest"):
            reason += f" Closest: {' '.join(att['closest'].split())}"
        if att.get("proposal"):
            text = " ".join(att["proposal"].split())
            if text not in [t for t, _ in proposals]:
                proposals.append((text, []))
            next(ps for t, ps in proposals if t == text).append(bb_id(proc).replace(PREFIX, ""))
        lines.append(f"| `{bb_id(proc).replace(PREFIX, '')}` | {proc.get('cwl_class', '')} | {att['status']} | {t3} | {t2} | {t1} | {reason} |")
    lines += ["", "## Proposals (for GeoLabs to decide; nothing created)", ""]
    lines += [f"- {t} (from {', '.join('`' + p + '`' for p in ps)})" for t, ps in proposals] or ["None."]
    (ROOT / "docs" / "ATTACHMENTS.md").write_text("\n".join(lines) + "\n")


def write_openeo_doc(summary):
    rows = []
    for i, s in enumerate(summary, 1):
        oe = s["openeo"]
        main = ", ".join("`" + t.replace("ogc.openeo.", "") + "`" for t in oe.get("exactMatch", []) + oe.get("closeMatch", [])) or "—"
        rel = ", ".join("`" + t.replace("ogc.openeo.", "") + "`" for t in oe.get("relatedMatch", [])) or "—"
        short = " ".join(oe["rationale"].split())
        short = short.split(". ")[0] + "."
        rows.append(f"| E{i:02d} | `{s['id'].replace('ospd.process-profiles.', '')}` | {oe['level']} | {main} | {rel} | {short} |")
    (ROOT / "docs" / "OPENEO-EQUIVALENCES.md").write_text(
        OPENEO_HEADER + "\n".join(rows) + "\n\nFull rationale and decompositions: each profile's `description.md` and "
        "`examples/process-type.json`.\n")


if __name__ == "__main__":
    main()
