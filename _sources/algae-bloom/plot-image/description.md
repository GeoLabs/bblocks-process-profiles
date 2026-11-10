Process profile of **`plot-image`** (CommandLineTool, W1 Algae Bloom).

> Plots an image with colors.

## Source

- CWL: [plot-image.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/plot-image.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Export / aggregation
- EOAP CWL custom types used: none
- Used by: `ospd.process-profiles.algae-bloom.workflow-earth-search-process`, `ospd.process-profiles.algae-bloom.workflow-copernicus-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `input_image` | File | `output_file` | File |
| `color_scale` | string | `output_plot` | File |
| `output_name` | string? |  |  |
| `plot_name` | string? |  |  |
| `plot_title` | string? |  |  |
| `clip_min` | float? |  |  |
| `clip_max` | float? |  |  |

## Analysis

**Behaviour.** Python/GDAL + matplotlib: applies binned colour scales to a single-band
image, writes a colourised GeoTIFF (`<output_name>.tif`) and a PNG figure (`<plot_name>.png`).

**CWL specifics.** `color_scale` is a JSON array serialised in a `string` (a structured value
hidden in a literal: could be typed as an array of `[number, [r,g,b]]` in the
processDescription, but CWL cannot declare it). Outputs are globbed with
`$(runtime.outdir)/*.tif` / `*.png`, so any extra file would break the step. Output formats
`ogc:geotiff` and `iana:image/png` are resolved by the transform to their respective
media types (M-01, fixed 2026-09-23 in `eoap.cct.cwl-to-ogcprocess` itself).

**`output_file` is not a GeoTIFF.** It is declared `ogc:geotiff`, but the 9 `*_color.tif` of
the two W1 runs (`results/`, `results1/`) are RGBA TIFFs (4 samples) carrying none of the
GeoTIFF tags 33550, 33922, 34735; the `calculate-band` outputs of the same runs
(`*_<indicator>.tiff`) carry them (observed 2026-11-10). An upstream defect of the CRIM CWL or of
its tool (docs/OPEN-QUESTIONS.md Q-PLOT-GEOTIFF), not corrected here.

**Provenance.** Two outputs derived from one input; `color_scale` is the parameter that
makes the rendering reproducible.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is given as a `prov:specializationOf` that Application Package --, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-earth-search`: earth-search variant of the pinned W1 package, `cwltool --outdir ./results --provenance ./PROV algae-usecase-workflow-earth-search.cwl example/algae-usecase-job-earth-search.yml`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; two products scattered (S2A_29SPC_20190701_1_L2A then S2A_29SPC_20190701_0_L2A). Three local deviations were needed to run the package at all, none touching the CWL (docs/DEVIATIONS.md U-03, U-04)), activity `main/plot_turbidity_2` (scatter iteration 2, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## Implementation Profile (tier 3)

Implements [`Raster rendering`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-rendering) (`generic-profiles.implementation-profile.raster-rendering`, bblocks-generic-profiles). Signature checked against raster-rendering: `input_image` (GeoTIFF, TIFF or JPEG 2000) implements `raster`; `color_scale` (a JSON array of value bins and colours, in a string) implements `colourMap`; `output_plot` (PNG) implements the output `image`. `output_file`, the coloured RGBA TIFF on the input grid (declared GeoTIFF but not georeferenced, Q-PLOT-GEOTIFF), is an output of the deployment's own, as are `output_name`, `plot_name`, `plot_title`, `clip_min` and `clip_max`.

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `input_image` | input `raster` | `raster` |
| `color_scale` | input `colourMap` | `colour-map` |
| `output_name`, `plot_name`, `plot_title`, `clip_min`, `clip_max` | -- (the deployment's own inputs, Table 21 footnote b) | -- |
| `output_plot` | output `image` | `rendered-image` |
| `output_file` | -- (the deployment's own outputs, Table 21 footnote b) | -- |

## openEO equivalence

**Level: closeMatch.** Partial: the export part (GeoTIFF + PNG) corresponds to save_result with a GTiff or PNG format; `clip_min`/`clip_max` correspond to math.clip. The colour mapping (`color_scale` bins) and the matplotlib figure (title, colour bar) have no stable openEO process (colour maps are back-end-specific format options).

- `closeMatch`: `ogc.openeo.processes.cubes.save_result`
- `relatedMatch`: `ogc.openeo.processes.math.clip`, `ogc.openeo.processes.math.linear_scale_range`

## Process type (Activity 4)

Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision.
