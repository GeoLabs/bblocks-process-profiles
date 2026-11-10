Process profile of **`water-bodies`** (Workflow, W3 Water Bodies).

> Water bodies detection based on NDWI and otsu threshold

## Source

- CWL: [water-bodies.cwl](https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/664d242f70e1fb870599bf06858daa7ce5a50ddb/water-bodies/app-pkg-multiple/water-bodies.cwl) (pinned commit `664d242`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval → Scientific computation → Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.bbox`, `eoap.cct.string-format`
- Steps (profiles): `ospd.process-profiles.water-bodies.detect-water-body`, `ospd.process-profiles.water-bodies.stac`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `aoi` | string | `stac` | Directory |
| `epsg` | string |  |  |
| `stac_items` | string[] |  |  |
| `bands` | string[] |  |  |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-05 outputs.stac: the Directory output is a STAC Catalog written by the tool itself (run record: `catalog.json` with one Item), not the Collection assumed by the transform

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is given as a `prov:specializationOf` that Application Package --, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (ogc-eo-application-package-hands-on f472585 `water-bodies/app-pkg-multiple/water-bodies.cwl`, one CWL file per step), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## Implementation Profile (tier 3)

Not attached to an Implementation Profile of bblocks-generic-profiles: A composite Workflow: catalogue search, data retrieval and processing chained into one application. No Generic Profile describes a whole application, and none should: its steps are compared with the tiers one by one.

The attachment of each CWL process is listed in `docs/ATTACHMENTS.md`.

## openEO equivalence

**Level: none.** Composite: a CWL Workflow scattering a per-item sub-workflow over the STAC item list, then aggregating the results into one STAC catalog. The openEO equivalent would be a user-defined process graph, which has no Building Block of its own; the correspondence is carried by the steps.


| Stage | openEO | Level | Note |
|---|---|---|---|
| node_water_bodies (detect_water_body, scatter over stac_items) | — | none | see osc.process-profiles.water-bodies.detect-water-body |
| node_stac | `ogc.openeo.processes.cubes.save_result` | closeMatch |  |

## Process type (Activity 4)

Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/water-bodies` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision.
