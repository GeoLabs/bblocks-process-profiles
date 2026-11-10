Process profile of **`otsu`** (CommandLineTool, W3 Water Bodies).

> Otsu binary threshold

## Source

- CWL: [otsu.cwl](https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/otsu.cwl) (pinned commit `f472585`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Scientific computation
- EOAP CWL custom types used: none
- Used by: `ospd.process-profiles.water-bodies.detect-water-body`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `raster` | File | `binary_mask_item` | File |

## Analysis

**Behaviour.** `python -m app`, `ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0`.
Computes an Otsu threshold on the input raster's histogram and writes a binary (water /
not-water) mask GeoTIFF (`otsu.tif`).

**Provenance.** One file input, one file output.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is given as a `prov:specializationOf` that Application Package --, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (ogc-eo-application-package-hands-on f472585 `water-bodies/app-pkg-multiple/water-bodies.cwl`, one CWL file per step), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main/node_otsu` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## Implementation Profile (tier 3)

Implements [`Otsu thresholding`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding) (`generic-profiles.implementation-profile.otsu-thresholding`, bblocks-generic-profiles). Signature checked against otsu-thresholding: `raster` (a single-band file) implements `raster`; `binary_mask_item` (a uint8 GeoTIFF, 1 above the threshold, 0 declared NoData) implements the output `mask`.

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `raster` | input `raster` | `raster-single-band` |
| `binary_mask_item` | output `mask` | `binary-mask` |

**Assumed format gap.** `raster`: The CWL (GeoLabs/ogc-eo-application-package-hands-on f472585, `otsu.cwl`) declares no `format` on this File, so the processDescription derived by eoap.cct.cwl-to-ogcprocess serves application/octet-stream: the deployment exposes no media type for the GeoTIFF it reads or writes. Closed upstream if the CWL declares `format: ogc:geotiff`. Evidence: Run record `water-bodies`: the `raster` inputs of node_otsu (norm_diff.tif) are single-band TIFFs with the GeoTIFF tags 33550, 33922, 34735, EPSG:32610 (observed 2026-11-10). Declared in `assumedFormatGaps` of `process-type.json` (`docs/FORMAT-CHECK.md`).

**Assumed format gap.** `binary_mask_item`: The CWL (GeoLabs/ogc-eo-application-package-hands-on f472585, `otsu.cwl`) declares no `format` on this File, so the processDescription derived by eoap.cct.cwl-to-ogcprocess serves application/octet-stream: the deployment exposes no media type for the GeoTIFF it reads or writes. Closed upstream if the CWL declares `format: ogc:geotiff`. Evidence: Run record `water-bodies`: the outputs otsu.tif are single-band TIFFs with the GeoTIFF tags 33550, 33922, 34735, EPSG:32610 (observed 2026-11-10). Declared in `assumedFormatGaps` of `process-type.json` (`docs/FORMAT-CHECK.md`).

## openEO equivalence

**Level: none.** openEO has no built-in Otsu (automatic histogram) threshold process; the closest primitive, `ogc.openeo.processes.comparison.gt`, only compares against a caller-supplied constant, not a threshold the process computes itself.


## Process type (Activity 4)

Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/otsu` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision.
