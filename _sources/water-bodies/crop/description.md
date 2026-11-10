Process profile of **`crop`** (CommandLineTool, W3 Water Bodies).

> Crop a Sentinel-2 COG band to an area of interest

## Source

- CWL: [crop.cwl](https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/crop.cwl) (pinned commit `f472585`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval
- EOAP CWL custom types used: none; candidates: `eoap.cct.bbox`, `eoap.cct.stac`, `eoap.cct.string-format`
- Used by: `ospd.process-profiles.water-bodies.detect-water-body`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `item` | string | `cropped` | File |
| `aoi` | string |  |  |
| `epsg` | string |  |  |
| `band` | string |  |  |

## Analysis

**Behaviour.** `python -m app`, `ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0`.
Reads one asset of the given STAC item directly over the network (`NetworkAccess`; no `File`
input -- `item` is a plain STAC item URL string), windowed-reads the requested `band` cropped to
`aoi`, writes one GeoTIFF (`crop_<band>.tif`). It does not reproject: `epsg` is passed to
`gdal.Translate` as `projWinSRS`, the CRS of `aoi`, not a target CRS (read, `app.py`). Observed
(run record `water-bodies`, 2026-11-10): with `epsg: "EPSG:4326"`, the four `crop_*.tif` stay
in the CRS of the asset, EPSG:32610 (UTM zone 10N), at 10 m.

**CWL specifics.** `item`, `aoi`, `epsg`, `band` are all plain strings: `item` is a STAC Item
URL (candidate `eoap.cct.stac` or `eoap.cct.string-format`), `aoi` a comma-separated bbox
(candidate `eoap.cct.bbox`, but as one string, not the object EOAP's own BBox type expects).
`band` is an unconstrained string (`green`, `nir`, ...), not an enum: any STAC asset key the
item happens to expose is accepted, so an invalid band name fails only at execution.

**Provenance.** No input is a `File`: `aoi`/`epsg`/`item`/`band` are literal-valued entities;
the network fetch itself leaves no provenance trace beyond the output file (GP-3, GP-4).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is given as a `prov:specializationOf` that Application Package --, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (ogc-eo-application-package-hands-on f472585 `water-bodies/app-pkg-multiple/water-bodies.cwl`, one CWL file per step), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main/node_crop` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## Implementation Profile (tier 3)

Implements [`Band retrieval`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval) (`generic-profiles.implementation-profile.band-retrieval`, bblocks-generic-profiles). Signature checked against band-retrieval: `item` (a STAC Item URL) implements `product`, by reference; `band` (a band common name) implements `band`; `aoi` and `epsg` (four numbers in one string, and their CRS) implement `areaOfInterest` as a role decomposition; `cropped` implements the output `raster`. It does not reproject: the output keeps the CRS of the asset.

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `item` | input `product` | `eo-product` |
| `band` | input `band` | `band-identifier` |
| `aoi`, `epsg` (role decomposition) | input `areaOfInterest` | `bounding-box` |
| `cropped` | output `raster` | `raster` |

**Role decomposition.** The input `areaOfInterest` is taken as `aoi`, `epsg`: The area of interest is taken as one string of four comma-separated numbers (`aoi`) and the identifier of their CRS (`epsg`, passed to gdal.Translate as `projWinSRS`), not as one OGC API - Processes bounding box: the representation bounding-box-ogcapi-processes-bbox of the role is not served. Declared in `roleDecompositions` of `process-type.json`; its representation is not served (`docs/FORMAT-CHECK.md`).

**By reference.** `item` (role `product`) is a URL of the data, not the data: The product is given as the URL of its STAC Item, a string, not as the STAC Item itself. Declared in `byReference` of `process-type.json` (`docs/FORMAT-CHECK.md`).

**Assumed format gap.** `cropped`: The CWL (GeoLabs/ogc-eo-application-package-hands-on f472585, `crop.cwl`) declares no `format` on this File, so the processDescription derived by eoap.cct.cwl-to-ogcprocess serves application/octet-stream: the deployment exposes no media type for the GeoTIFF it reads or writes. Closed upstream if the CWL declares `format: ogc:geotiff`. Evidence: Run record `water-bodies`: the `cropped` outputs (crop_green.tif, crop_nir.tif) are single-band TIFFs with the GeoTIFF tags 33550, 33922, 34735, EPSG:32610 (observed 2026-11-10). Declared in `assumedFormatGaps` of `process-type.json` (`docs/FORMAT-CHECK.md`).

## openEO equivalence

**Level: closeMatch.** load_collection with a spatial_extent (aoi) and a single band selected (filter_bands); the STAC item is given by URL rather than resolved by collection/date/bbox search, and the windowed COG read (no full download) is an implementation detail openEO back-ends make transparently.

- `closeMatch`: `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands`

## Process type (Activity 4)

Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision.
