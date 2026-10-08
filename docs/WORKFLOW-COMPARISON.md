# Structural comparison across the reference workflows

Each workflow was profiled independently, from its own CWL and its own run record. This note
pulls out where they turn out to share shape and where they genuinely don't — grounded in
`scripts/profiles.yaml`'s `phases`/`openeo` fields and `docs/DEVIATIONS.md`, not asserted.

## Phase coverage

Which of the six phases (`docs/OPENEO-EQUIVALENCES.md`'s criteria, `pp:phase/*`) each workflow's
own tools exercise, read from `scripts/profiles.yaml`:

| Phase | W1 Algae Bloom | W2 KindGrove | W3 Water Bodies | W2b KindGrove (steps) |
|---|---|---|---|---|
| Filter configuration | `select-products-sentinel2`'s inputs (toi/cloud-cover) are given directly to the workflow, no dedicated tool | `parse-aoi` | — | `parse-aoi-steps` |
| Selection / filtering | `select-products-sentinel2` (STAC search by aoi/date/cloud-cover) | `mangrove` (folds selection into the opaque tool) | — | `select-scene` |
| Data retrieval | `download-band-sentinel2-stac-item`, `download-band-sentinel2-product-safe` | `mangrove` | `crop` | `download-band` |
| Pre-processing | `reproject-image` | `mangrove` | — | `reproject-band` |
| Scientific computation | `calculate-band` | `mangrove` | `norm-diff`, `otsu` | `calculate-indices`, `estimate-biomass` |
| Export / aggregation | `plot-image` | `mangrove` | `stac` | `export-stac` |

W3 has **no Filter configuration, Selection / filtering or Pre-processing tool**: `stac_items` is
a caller-supplied list of STAC item URLs (no search phase — contrast W1's `select-products-sentinel2`,
a dedicated STAC-search tool), and `crop` folds reprojection into the same windowed read that
fetches the band (contrast W1, where fetch and reprojection are two separate tools, below). This
isn't a gap in the profiling: the source CWL genuinely has no step doing either.

W2b's own CWL `doc:` says it is deliberately "aligned on the steps of the OSPD W1 Algae Bloom
workflow" — the table bears that out: it is the only one of the four besides W1 itself to give
every phase its own dedicated tool, in the same order, with the same `download → reproject`
split W1 uses and W3 doesn't.

## Matching roles, different design choices

Three roles recur across W1 and W3 with the same openEO `closeMatch` pair, but a different CWL
decomposition:

| Role | W1 tool | W3 tool | Shared openEO closeMatch | What differs |
|---|---|---|---|---|
| Fetch one band of one item | `download-band-sentinel2-stac-item` / `-product-safe` | `crop` | `processes.cubes.load_collection`, `processes.cubes.filter_bands` | W1 splits fetch (this tool) from reprojection (`reproject-image`, closeMatch `resample_spatial`, its own tool); W3's `crop` does both in one windowed COG read — no separate reprojection tool exists in the CWL |
| Derive a raster from input bands | `calculate-band` | `norm-diff` | both closeMatch a band-math openEO process, but not the *same* one | `calculate-band` is generic — an arbitrary `gdal_calc.py` expression over up to 26 bands (`A`..`Z`), so it maps to the generic `processes.cubes.reduce_dimension` with a callback. `norm-diff` computes one fixed formula, `(A-B)/(A+B)`, over exactly two bands, so it maps to the *named* `processes.math.indices.normalized_difference` — a tighter match despite doing less. Which index it computes (NDWI here, NDVI in `kindgrove.mangrove`) is the caller's band order, not the tool |
| Package the final output | `plot-image` | `stac` | `processes.cubes.save_result` | Different output modality: `plot-image` renders a GeoTIFF **and** a PNG for visual inspection (closeMatch also pulls in `math.clip`/`math.linear_scale_range` for the render); `stac` writes a re-publishable STAC Catalog (one Item per input identifier). The STAC-Catalog case is the one that needed the Directory→Catalog correction below — `plot-image`'s output is a plain file, not a Directory, so it never hits that gap |

## A structural novelty W3 introduces

W1 scatters once, over STAC products found by `select-products-sentinel2` (flat scatter, one
level). W3's `water-bodies` workflow scatters over `stac_items` (caller-supplied, no search), and
its `detect_water_body` sub-workflow independently scatters `crop` over `bands` — a **nested**
scatter neither W1 nor W2 exercises. It's not just a deeper pipeline: it surfaced two real gaps
that a flat, single-Workflow document never would have —

- `docs/DEVIATIONS.md` **M-13**: the eoap-cct transform always converts the *first* `Workflow` of
  a packed `$graph`, silently ignoring which one was actually requested, harmless when a document
  packs one Workflow (W1, W2) and wrong the moment it packs two (`water-bodies` + `detect_water_body`).
  Sidestepped at the source since: the pinned W3 source now splits into one CWL file per step (the
  same layout as W1), so no profile needs `element:` any more — the generator's own defence against
  M-13 stays in the code for a future packed source, just isn't exercised by this one any more;
- `scripts/generate.py`'s `bag_activity()` needed no change for it (one representative activity per
  profile was always enough), but the CWLProv bundle-naming scheme it decodes (iteration `_N`
  suffixes on both the bundle file and, for a non-`main` leaf, the step name) was only exercised
  end-to-end by this workflow's two independent scatter dimensions.

## A gap three independently-run STAC-writing tools share

`docs/DEVIATIONS.md` **M-05** (`Directory` output always mapped to a STAC Collection, never a
Catalog) was found on `kindgrove.mangrove` and corrected there first. `water-bodies.stac` hit the
*same* gap independently — its own run record shows the same `"type": "Catalog"` shape — and got
the same correction (`generate.py`'s `STAC_CATALOG_SCHEMA`, `profiles.yaml`'s `stac_catalog`
hint) applied to it separately, not inherited or assumed. `kindgrove-steps.export-stac` then hit it
a *third* time, independently of both: three unrelated Application Packages (KindGrove's
`mangrove_cli`, the EO Application Package Hands-On's `stac` tool, and now GeoLabs' own
step-decomposed `export_stac`, written from scratch rather than adapted from either of the other
two) independently choosing to write a Catalog rather than a Collection is a real signal about how
EO Application Packages commonly implement "write STAC output", not a coincidence worth ignoring
if this pattern keeps recurring in future workflows added to this register.

## Same domain problem, two implementations: `kindgrove` and `kindgrove-steps`

`kindgrove-steps` is not a repackaging of `kindgrove` the way W3's split source is a repackaging
of its own earlier packed form (`docs/DEVIATIONS.md` M-13's own history): it is a *different*
Application Package solving the same problem (mangrove above-ground biomass and carbon stock from
Sentinel-2), built independently, with its own tools and Docker images. Both are kept in the
register side by side, under different `workflow:` keys, neither replacing the other:

| | `kindgrove` | `kindgrove-steps` |
|---|---|---|
| Granularity | one opaque `mangrove` tool, everything inside it | 6 CommandLineTools, one per notebook |
| License | Apache-2.0 | CC-BY-NC-SA-4.0 |
| Docker images | one ipython2cwl binary | `ghcr.io/geolabs/kindgrove/<step>:v0.0.2-rc2`, one per step |
| Source pin | git commit (`bblocks-eoap-cct`) | GitHub Release asset + sha256 (`GeoLabs/KindGrove`, no commit — the CWL is never committed to that repo's tree) |
| Status | stable, pinned commit | explicitly a prerelease (`v0.0.2-rc2`) |
| Vegetation indices | opaque (inside `mangrove`) | NDVI (closeMatch `ogc.openeo.processes.cubes.ndvi`), NDWI (closeMatch `normalized_difference`), SAVI (no openEO process in this register) all computed by one tool, `calculate-indices` |
| Biomass model | opaque | still opaque in `estimate-biomass` (`biomass = biomass_slope * ndvi + biomass_intercept`, then `* carbon_fraction`) — the regression itself is visible in the execute inputs even though the openEO mapping stays `none` |

Because `kindgrove-steps` exposes each stage as its own profile, it gives the process-type register
(Activity 4) six new, independently reusable process types for mangrove biomass work that
`kindgrove.mangrove`'s single opaque tool could never offer — the practical benefit of a decomposed
Application Package the D100/D120 profiling work is meant to surface. Its prerelease status is why
it sits alongside `kindgrove`, not in place of it: once (and if) it stabilises, `sources.yaml`'s
`kindgrove_steps` entry moves from `release:` to `commit:` the same way any other source would.
