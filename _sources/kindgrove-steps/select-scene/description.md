Process profile of **`select_scene`** (CommandLineTool, W2b KindGrove (step notebooks)).

> Select the least cloudy Sentinel-2 L2A scene

## Source

- CWL: [mangrove-workflow-steps.cwl#select_scene](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#select_scene) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Selection / filtering
- EOAP CWL custom types used: none; candidates: `eoap.cct.bbox`
- Used by: `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `west` | float | `stac_item` | File |
| `south` | float |  |  |
| `east` | float |  |  |
| `north` | float |  |  |
| `cloud_cover_max` | float |  |  |
| `days_back` | int |  |  |
| `stac_api` | string? |  |  |
| `collection` | string? |  |  |

## Analysis

**Behaviour.** `/app/cwl/bin/steps/01_select_scene`, `ghcr.io/geolabs/kindgrove/select-scene:v0.0.2-rc2`.
Searches `stac_api`/`collection` (both defaulted to Earth Search / sentinel-2-l2a) for the
least cloudy scene intersecting the bounding box within `days_back` days of the execution
date, under `cloud_cover_max`, and writes its STAC Item as `scene_item.json`.

**CWL specifics.** `requirements: {NetworkAccess: {networkAccess: true}}` uses the dict-form
requirements syntax, where bare `NetworkAccess` validates without the `cwltool:` namespace
prefix W3's list-form syntax needed (`docs/DEVIATIONS.md` U-06) -- a different encoding of
the same cwltool extension, not a fix to the underlying non-standardness.

**Provenance.** No file input: `west`/`south`/`east`/`north`/`cloud_cover_max`/`days_back`
are literal-valued entities. The network search itself leaves no provenance trace beyond the
output STAC Item file (GP-3, GP-4, the same gap `water-bodies.crop` has).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is given as a `prov:specializationOf` that Application Package --, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main/select_scene` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## Implementation Profile (tier 3)

Implements [`Product selection`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/product-selection) (`generic-profiles.implementation-profile.product-selection`, bblocks-generic-profiles). Signature checked against product-selection: `west`, `south`, `east`, `north` implement `areaOfInterest` as a role decomposition (a bounding box in EPSG:4326, implicit); `days_back` implements `timeInterval` as a literal role decomposition, not reproducible; `collection` implements `collection`; `stac_item` (one STAC Item file) implements the output `products`. `cloud_cover_max` and `stac_api` are inputs of the deployment's own.

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `west`, `south`, `east`, `north` (role decomposition) | input `areaOfInterest` | `geometry` |
| `days_back` (role decomposition) | input `timeInterval` | `time-interval` |
| `collection` | input `collection` | `collection-identifier` |
| `cloud_cover_max`, `stac_api` | -- (the deployment's own inputs, Table 21 footnote b) | -- |
| `stac_item` | output `products` | `eo-product` |

**Role decomposition.** The input `areaOfInterest` is taken as `west`, `south`, `east`, `north`: The area of interest is taken as the four bounds of a bounding box, in EPSG:4326 (implicit: passed as the `bbox` of pystac_client, read), not as a GeoJSON geometry: the representation geometry-geojson of the role is not served. Declared in `roleDecompositions` of `process-type.json`; its representation is not served (`docs/FORMAT-CHECK.md`).

**Role decomposition.** The input `timeInterval` is taken as `days_back`: The time interval is the `days_back` days before the time of execution: the same input gives another interval on another day, so a run cannot be repeated from its inputs alone. Not reproducible: the parts depend on the time of execution. Declared in `roleDecompositions` of `process-type.json`.

**Assumed format gap.** `stac_item`: The CWL (GeoLabs/KindGrove v0.0.2-rc2, `select_scene`) declares no `format` on this File, so the processDescription derived by eoap.cct.cwl-to-ogcprocess serves application/octet-stream: the deployment exposes no media type for the STAC Item it writes. Closed upstream if the CWL declares a STAC Item format. Evidence: Run record `kindgrove-steps`: the output `stac_item` is a JSON document, `"type": "Feature"`, `stac_version` 1.1.0 (observed 2026-11-10). Declared in `assumedFormatGaps` of `process-type.json` (`docs/FORMAT-CHECK.md`).

## openEO equivalence

**Level: closeMatch.** Same filter semantics as load_collection's `spatial_extent` (west/south/east/north) and a `properties` cloud-cover filter; `days_back` is a relative time window resolved against the execution date, not an explicit `temporal_extent` -- the same non-reproducibility already documented for `kindgrove.mangrove-workflow` (Q-W2-DAYSBACK).

- `closeMatch`: `ogc.openeo.processes.cubes.load_collection`

## Process type (Activity 4)

Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/select-scene` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision.
