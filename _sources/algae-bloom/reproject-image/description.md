Process profile of **`reproject-image`** (CommandLineTool, W1 Algae Bloom).

> Performs image reprojection.

## Source

- CWL: [reproject-image.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Pre-processing
- EOAP CWL custom types used: none
- Used by: `ospd.process-profiles.algae-bloom.workflow-earth-search-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `input_image` | File | `result` | File |
| `output_dimensions` | int[]? |  |  |
| `output_resolution` | int[]? |  |  |
| `output_name` | string |  |  |

## Analysis

**Behaviour.** `gdalwarp -ot Float32 -of GTiff [-ts w h] [-tr xres yres] <in> <name>.tiff`.
In W1 it is called once, to bring B03 from 10 m to 60 m so that it can be combined with B01
(only available at 60 m) for chlorophyll-a and turbidity. The run log reports a 1830 x 1830
output (10980 x 10980 at 10 m).

**CWL specifics.** `output_dimensions` and `output_resolution` are `int[]?` whose arity (2)
is only implied; the transform maps them to unbounded integer arrays (M-06). The label says
"reprojection" but no target CRS input exists. Docker image `ogc-ospd/algae-usecase/reproject-image`
has no tag and no registry (GP-6).

**Provenance.** Clear derivation: output `wasDerivedFrom` input band; `output_resolution` is a
parameter entity (`output_resolution`, literal array).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is given as a `prov:specializationOf` that Application Package --, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-earth-search`: earth-search variant of the pinned W1 package, `cwltool --outdir ./results --provenance ./PROV algae-usecase-workflow-earth-search.cwl example/algae-usecase-job-earth-search.yml`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; two products scattered (S2A_29SPC_20190701_1_L2A then S2A_29SPC_20190701_0_L2A). Three local deviations were needed to run the package at all, none touching the CWL (docs/DEVIATIONS.md U-03, U-04)), activity `main/reproject_b03_60m_2` (scatter iteration 2, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## Implementation Profile (tier 3)

Implements [`Raster resampling`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-resampling) (`generic-profiles.implementation-profile.raster-resampling`, bblocks-generic-profiles). Signature checked against raster-resampling: `input_image` (GeoTIFF, TIFF or JPEG 2000) implements `raster`; `output_resolution` (`-tr`, an integer pair, optional at tier 4) implements `resolution`; `result` (GeoTIFF) implements the output `raster`. `output_dimensions` (`-ts`, the other way to define the target grid) and `output_name` are inputs of the deployment's own. Not raster-reprojection: no target CRS (`-t_srs` is never passed). Not exposed: the interpolation method (gdalwarp's default) and the forced Float32 type.

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `input_image` | input `raster` | `raster` |
| `output_resolution` | input `resolution` | `grid-resolution` |
| `output_dimensions`, `output_name` | -- (the deployment's own inputs, Table 21 footnote b) | -- |
| `result` | output `raster` | `raster` |

## openEO equivalence

**Level: closeMatch.** As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place.

- `closeMatch`: `ogc.openeo.processes.cubes.resample_spatial`

## Process type (Activity 4)

Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision.
