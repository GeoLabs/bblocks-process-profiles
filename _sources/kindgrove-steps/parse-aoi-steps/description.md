Process profile of **`parse_aoi`** (CommandLineTool, W2b KindGrove (step notebooks)).

> Parse area of interest

## Source

- CWL: [mangrove-workflow-steps.cwl#parse_aoi](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#parse_aoi) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Filter configuration
- EOAP CWL custom types used: `eoap.cct.bbox`
- Used by: `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `aoi` | https://raw.githubusercontent.com/eoap/schemas/main/ogc.yaml#BBox | `west` | float |
|  |  | `south` | float |
|  |  | `east` | float |
|  |  | `north` | float |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is given as a `prov:specializationOf` that Application Package --, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main/parse_aoi` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Structural helper: unpacks an OGC BBox record into west/south/east/north floats -- no `output_dir` (unlike `kindgrove.parse-aoi`, which this profile parallels but does not replace). No openEO process does this, since openEO passes a bounding box directly.

- `relatedMatch`: `ogc.openeo.types.bounding-box`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/parse-aoi-steps` (`ospd.process-profiles.process-type`), status `submitted`.
