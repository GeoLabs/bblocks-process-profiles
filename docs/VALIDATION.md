# Validation status

## Authoritative validation: passing (2026-10-06)

`./build.sh` (Docker, `ghcr.io/opengeospatial/bblocks-postprocess:latest`): **52/52 building
blocks, 0 errors**, no empty RDF graph. Supersedes the 2026-09-24 28/28 below, not a correction
of it: the `sqlmm`/`raster`/`vector` workflow groups (SQL/MM, GDAL/OTB and SAGA operations on
the Geonovum testbed, `ospd.process-profiles.{sqlmm,raster,vector}.*`) were added over several
sessions starting 2026-10-01 but never run through a full Docker build until now -- this is
their first validation, not a revalidation.

It surfaced one real, pre-existing bug, unrelated to any one session's additions: three
`profiles.yaml` entries (`raster.extent`, `raster.format-conversion`, `vector.geometry-extent`)
used `phases: [post-processing]`, a value `_sources/process-type/schema.yaml`'s `phase` enum
has never accepted (it only has `filter-configuration`/`selection-filtering`/`data-retrieval`/
`pre-processing`/`scientific-computation`/`export-aggregation`) -- a silent latent failure since
whichever commit first added it, only visible once the register was actually built end-to-end.
Fixed to `export-aggregation`, the enum value matching what all three operations are (a
terminal/summarising step: re-encoding a raster's final format, or reducing a geometry/raster to
its bounding envelope), not a judgement call specific to this addition.

Also added in this validation: four more vector operations from OGC 99-049 (Centroid, ConvexHull,
IsSimple, GetArea -> `ospd.process-profiles.sqlmm.{centroid,convex-hull,is-simple,area}`), on the
`bblocks-generic-profiles` side merging the former dedicated `geometry-extent` Generic Profile
into a new shared `unary-geometry-operation` (alongside `centroid`/`convex-hull`) and adding
`unary-spatial-predicate` (`is-simple`) and `geometry-measure` (`area`) -- see that register's own
`docs/ARCHITECTURE.md`. `bblocks-generic-profiles` itself validates separately at **41/41
building blocks, 0 errors**.

Environment note for whoever runs `scripts/generate.py` locally rather than only through
`./build.sh`: the W3C PROV-JSONLD examples (`w3c_prov_example()`) need `prov`'s own `jsonld`
serializer, which PyPI's released `prov` (2.2.0 at time of writing) does not ship -- it exists
only on the project's unreleased `main` branch, which itself requires Python >= 3.10. On a system
Python 3.9 (as `/usr/bin/python3` is on this machine), `pip install prov` resolves to 2.2.0 (no
`jsonld` serializer, `generate.py` exits) and `pip install git+https://github.com/trungdong/prov`
silently builds an empty `UNKNOWN-0.0.0` wheel instead of failing loudly (old pip's PEP 621
handling, not a `generate.py` bug) -- `./build.sh` itself is unaffected, since the Docker image
bundles its own working Python. Run `scripts/generate.py` with any Python >= 3.10 that has a
`prov` built from that branch (Homebrew's `python3.14`, if installed, already had one on this
machine).

## Authoritative validation: passing (2026-09-24)

`./build.sh` (Docker, `ghcr.io/opengeospatial/bblocks-postprocess:latest`) run on a machine with
network access: **28/28 building blocks, 227/227 example snippets, 0 errors**, 225 SHACL
validations conform, no empty RDF graph, no `file:///` IRI.

The register now covers four workflow groups. W3 Water Bodies (2026-09-23,
`docs/OPEN-QUESTIONS.md` Q-W3-RUN) added six building blocks (`water-bodies`,
`detect-water-body`, `crop`, `norm-diff`, `otsu`, `stac`) from a real `cwltool --provenance` run;
it surfaced a mapping gap neither W1 nor W2 exercises (`docs/DEVIATIONS.md` M-13: a packed
`$graph` document with more than one top-level `Workflow` always converts the *first* one,
regardless of which `element` was requested) and needed one local CWL patch to run at all (U-06:
`NetworkAccess` with no namespace prefix is not valid CWL) — both later superseded when Gérald
published a split, pre-fixed source (`GeoLabs/ogc-eo-application-package-hands-on`) adopting this
register's own split proposal byte-for-byte.

W2b KindGrove (step notebooks) (2026-09-24, `docs/OPEN-QUESTIONS.md` Q-W2B-RUN) added eight more
building blocks (`mangrove-workflow-steps`, `parse-aoi-steps`, `select-scene`, `download-band`,
`reproject-band`, `calculate-indices`, `estimate-biomass`, `export-stac`) under a new
`kindgrove-steps` workflow group, **alongside** the original `kindgrove` group, not replacing it:
a ground-up reimplementation (different tools, different Docker images, CC-BY-NC-SA-4.0 instead of
`kindgrove`'s Apache-2.0), published only as a GitHub prerelease asset (`GeoLabs/KindGrove`
`v0.0.2-rc2`), never committed to that repo's tree — the first source in this register pinned by
`release:` + `sha256:` instead of a git `commit:` (`scripts/sources.yaml`, `run_workflows.py`
`ensure_release_assets()`). It independently hit the same M-05 Directory→Collection gap as
`kindgrove.mangrove` and `water-bodies.stac` (`export-stac`, corrected the same way) and one new
generator bug: `description_md()` assumed every source had a `commit`, fixed to branch on
`release` vs `commit` when building the "pinned" text.

`eoap.cct.cwl-to-ogcprocess` (`GeoLabs/bblocks-eoap-cct`, commit `291a741`, pinned in
`scripts/sources.yaml`) now resolves CWL `format` into `contentMediaType`/`contentEncoding` and
multi-format `oneOf` itself (`docs/DEVIATIONS.md` M-01/M-02): 7 of the 10 W1 profiles are now
unmodified transform output, with 7 fewer example snippets than before (the
`processDescription.raw.json` example only exists for a `manually-corrected` profile). The
`eoap.cct.*` import collision (GP-8/Q-IMPORT) is also fixed, at its source in
`GeoLabs/bblocks-generic-provenance-profile`.

Thirteen of those snippets are the run records as **W3C PROV-JSONLD** (`examples/cwlprov.jsonld`,
validated against `ogc.ogc-utils.prov.w3c-prov-jsonld` from the experimental
`bblocks-prov-jsonld-alt` register, read as RDF through their own context): the only examples
whose PROV-O graph is cwltool's rather than this register's, and the first on which the PROV SHACL
shapes have real focus nodes (`docs/OPEN-QUESTIONS.md` Q-W3C). What the provenance-view validation
itself checks is documented under Q-PROV-SCHEMA: less than the wording suggests.

Since 2026-09-23 the run-derived examples of all 13 profiles are built from real
`cwltool --provenance` research objects (`scripts/sources.yaml` `runs:` — `w1-earth-search`,
`w1-copernicus`, `w2-pinned`; `docs/OPEN-QUESTIONS.md` Q-W1-LOG / Q-W1-COPERNICUS / Q-W2-RUN). The
CRIM run logs of 2024 are no longer read and there are no illustrative examples left. The JSON-LD contexts follow the Wf4Ever and generic-provenance vocabularies
(`wfprov:ProcessRun`, `prov:wasAssociatedWith`, `rdfs:seeAlso` links) rather than a local `pp:`
mapping; the one known residue is `outputs[].type` in the four W1 `execution` bundles, which the
processDescription's `outputs` binding turns into a `proc:type` literal.

It did not pass at first. The register was bootstrapped where the build could not run (egress
policy blocking `ghcr.io`, `registry-1.docker.io`, `pypi.org`, `*.github.io`,
`raw.githubusercontent.com`), and the first real build gave **1/14**: only `process-type` passed.
All 79 failures were the same check — `**Empty** output Turtle` — which bblocks-postprocess
hard-codes as an error and which the offline pre-check cannot see, since it does not run the
JSON-LD uplift. Cause: no profile had a JSON-LD context, so the context derived from the
`ogc.api.processes.*` annotations bound none of the properties the examples use and every
snippet uplifted to nothing. The 1–2 examples per profile that did pass only did so because
`type` happened to be the single mapped term (`[] proc:type "ProcessRun"`).

Fix, in `scripts/generate.py`: a shared `PROFILE_CONTEXT` written to every profile as
`context.jsonld` (`@vocab` re-scoped under `inputs`/`outputs`; `$defs` payloads reached through
`x-jsonld-extra-terms`), and a `base-uri` on every example. Two alternatives were measured on
the same build and rejected: splitting each profile into one building block per payload
(26/102 — the OGC API - Processes bblocks have no annotations to inherit) and inlining
`@context` in the example files (75/102 with 13 new JSON Schema failures, `propertyNames: enum`
rejects `@context`; array-rooted `provenance.json` cannot carry one). See `CLAUDE.md`.

A data bug surfaced by the fix: `scripts/profiles.yaml` had an unquoted flow-mapping value
`note: partial, no colour-ramp rendering`, parsed as a stray key that became an invalid IRI once a
`@vocab` existed. Quoted.

To run it:

```bash
./build.sh          # validate + build into build/
./view.sh           # http://localhost:9090
```

If the generic provenance profile or the Part 2 register are not published on GitHub Pages
(Q-PUB), copy `bblocks-config-local.yaml.example` to `bblocks-config-local.yaml` (git-ignored),
adjust the paths to local builds of those registers and mount them with `.volumes`
(bblocks-postprocess `url-mappings`, see
<https://ogcincubator.github.io/bblocks-docs/create/imports#local-url-mappings-for-testing>).

## Offline pre-check (done)

`scripts/validate_offline.py --deps-root DIR` resolves `bblocks://` identifiers and published
register URLs to local clones and validates with `jsonschema` (Draft 2020-12). Result at bootstrap:
**144/144 checks passed**:

- `bblocks-config.yaml`, 14 `bblock.json`, 14 `examples.yaml` against the bblocks-postprocess
  metadata schemas;
- 102 example snippets against their schema (default or `schema-ref`), with every reference
  resolved locally (no unresolved reference);
- 13 negative checks: each profile rejects the processDescription of another process.

Spot checks confirmed the resolution is real (e.g. an execution artifact without `checksum`, an
engine without `@id`, a run with `status: running`, an unknown execute input are all rejected).

Clones used (`--deps-root`): bblock-prov-schema, bblocks-wf4ever and bblocks-cwl (ogcincubator);
bblocks-ogcapi-processes, bblocks-eoap-cct, bblocks-openeo, bblocks-generic-provenance-profile,
bblock-ogcapi-processes-part2 (GeoLabs); opengeospatial/bblocks (as `bblocks`);
opengeospatial/bblocks-postprocess.

Not covered by the pre-check: JSON-LD uplift and SHACL, transforms, format assertions, doc
generation.
