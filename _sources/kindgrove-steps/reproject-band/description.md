Process profile of **`reproject_band`** (CommandLineTool, W2b KindGrove (step notebooks)).

> Reproject a raster onto a regular grid

## Source

- CWL: [mangrove-workflow-steps.cwl#reproject_band](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#reproject_band) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Pre-processing
- EOAP CWL custom types used: none; candidates: `eoap.cct.bbox`
- Used by: `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `band_file` | File | `reprojected_file` | File |
| `west` | float |  |  |
| `south` | float |  |  |
| `east` | float |  |  |
| `north` | float |  |  |
| `epsg` | int? |  |  |
| `resolution` | float? |  |  |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is given as a `prov:specializationOf` that Application Package --, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main/reproject_band` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## Implementation Profile (tier 3)

Implements [`Raster reprojection`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection) (`generic-profiles.implementation-profile.raster-reprojection`, bblocks-generic-profiles). Signature checked against raster-reprojection: `band_file` implements `raster`, `epsg` (an EPSG code, default 4326) implements `targetCRS`, `reprojected_file` implements the output `raster`; `west`, `south`, `east`, `north` (extent of the target grid) and `resolution` are inputs of the deployment's own. Its CWL declares no `format`: an assumed format gap.

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `band_file` | input `raster` | `raster` |
| `epsg` | input `targetCRS` | `coordinate-reference-system` |
| `west`, `south`, `east`, `north`, `resolution` | -- (the deployment's own inputs, Table 21 footnote b) | -- |
| `reprojected_file` | output `raster` | `raster` |

**Assumed format gap.** `band_file`: The CWL (GeoLabs/KindGrove v0.0.2-rc2, `reproject_band`) declares no `format` on this File, so the processDescription derived by eoap.cct.cwl-to-ogcprocess serves application/octet-stream: the deployment exposes no media type for the GeoTIFF it reads and writes. Closed upstream if the CWL declares `format: ogc:geotiff`. Evidence: Run record `kindgrove-steps` (scripts/sources.yaml): the three band_file inputs (red.tif, green.tif, nir.tif) and the three reprojected_file outputs (red_4326.tif, green_4326.tif, nir_4326.tif), the files of runs/kindgrove-steps/ro/data/ that primary.cwlprov.provn links to them by specializationOf (lines 157-268), are TIFF files (magic number 49 49 2a 00) carrying the GeoTIFF tags GeoKeyDirectory (34735), ModelTiepoint (33922) and ModelPixelScale (33550), observed 2026-11-10. Declared in `assumedFormatGaps` of `process-type.json` (`docs/FORMAT-CHECK.md`).

**Assumed format gap.** `reprojected_file`: The CWL (GeoLabs/KindGrove v0.0.2-rc2, `reproject_band`) declares no `format` on this File, so the processDescription derived by eoap.cct.cwl-to-ogcprocess serves application/octet-stream: the deployment exposes no media type for the GeoTIFF it reads and writes. Closed upstream if the CWL declares `format: ogc:geotiff`. Evidence: Run record `kindgrove-steps` (scripts/sources.yaml): the three band_file inputs (red.tif, green.tif, nir.tif) and the three reprojected_file outputs (red_4326.tif, green_4326.tif, nir_4326.tif), the files of runs/kindgrove-steps/ro/data/ that primary.cwlprov.provn links to them by specializationOf (lines 157-268), are TIFF files (magic number 49 49 2a 00) carrying the GeoTIFF tags GeoKeyDirectory (34735), ModelTiepoint (33922) and ModelPixelScale (33550), observed 2026-11-10. Declared in `assumedFormatGaps` of `process-type.json` (`docs/FORMAT-CHECK.md`).

## openEO equivalence

**Level: closeMatch.** resample_spatial with a target `resolution` and `projection` (epsg); no explicit resampling-method parameter in the CWL (implementation default), same partial match as `algae-bloom.reproject-image`.

- `closeMatch`: `ogc.openeo.processes.cubes.resample_spatial`

## Process type (Activity 4)

Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision.
