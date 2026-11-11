# bblocks-process-profiles

OGC Building Blocks register holding **process profiles** for two populations of deployed processes:
the 27 deployable CWL processes of the OSPD 2026 reference workflows, and the 31 live processes of the
Geonovum testbed (see [Two populations](#two-populations)). Identifier prefix: `ospd.process-profiles.`

| Workflow | Source (linked, not copied) |
|---|---|
| W1 Algae Bloom | [`crim-ca/ogc-ospd-phase1@5edd4ec`](https://github.com/crim-ca/ogc-ospd-phase1/tree/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg) (CC-BY-NC-SA-4.0) |
| W2 KindGrove | [`GeoLabs/bblocks-eoap-cct@291a741`](https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl) |
| W3 Water Bodies | [`GeoLabs/ogc-eo-application-package-hands-on@f472585`](https://github.com/GeoLabs/ogc-eo-application-package-hands-on/tree/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple) (license unassigned upstream and in this fork; CC-BY-SA-4.0 assumed, see `scripts/sources.yaml` `w3`; tool images from `Terradue/ogc-eo-application-package-hands-on`) |
| W2b KindGrove (step notebooks) | [`GeoLabs/KindGrove` release `v0.0.2-rc3`](https://github.com/GeoLabs/KindGrove/releases/tag/v0.0.2-rc3) (CC-BY-NC-SA-4.0; a GitHub Release asset pinned by sha256 rather than a git commit — the CWL is never committed to the repo tree, see `scripts/sources.yaml` `kindgrove_steps`). A ground-up reimplementation added alongside `kindgrove`, not replacing it — see `docs/WORKFLOW-COMPARISON.md` |

## Two populations

The register holds two populations of deployed processes, each with its own process profile and
process-type entry. No identifier says which population a block belongs to; this section and
`bblocks-config.yaml` do (`POPULATIONS` in `scripts/generate.py` checks the counts).

| Population | Count | Source | Blocks |
|---|---|---|---|
| CWL processes of the OSPD reference workflows | 27 | CWL Application Packages (W1, W2, W3, W2b above), linked at a pinned commit or release; processDescription derived with `eoap.cct.cwl-to-ogcprocess`; examples from real `cwltool --provenance` runs | `algae-bloom.*` (10), `kindgrove.*` (3), `water-bodies.*` (6), `kindgrove-steps.*` (8) |
| Live processes of the Geonovum testbed | 31 | The processDescriptions served by the ZOO-Project instance `host1.tb.geonovum.geolabs.fr` (SQL/MM, GDAL/OTB, SAGA GIS), cached as served; static processDescription only | `sqlmm.*` (16), `raster.*` (7), `vector.*` (1), `terrain.*` (4), `pointcloud.*` (3) |

Each live process implements one Implementation Profile of
[bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles) (tier 3), one per
profile. A CWL process is attached to an Implementation Profile only when its inputs and outputs
implement that profile's signature: 12 of the 27 are, the others are listed with the reason in
[docs/ATTACHMENTS.md](docs/ATTACHMENTS.md). The representations of each attached profile are
compared with the formats the deployment serves in [docs/FORMAT-CHECK.md](docs/FORMAT-CHECK.md).

## Building blocks

### CWL processes of the OSPD reference workflows

<!-- CWL_TABLE -->
| Identifier | CWL class | Phase(s) | openEO | Implementation Profile (tier 3) |
|---|---|---|---|---|
| `ospd.process-profiles.algae-bloom.workflow-earth-search` | Workflow | Filter configuration, Selection / filtering, Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none | not attached |
| `ospd.process-profiles.algae-bloom.workflow-earth-search-process` | Workflow | Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none | not attached |
| `ospd.process-profiles.algae-bloom.workflow-copernicus` | Workflow | Filter configuration, Selection / filtering, Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none | not attached |
| `ospd.process-profiles.algae-bloom.workflow-copernicus-process` | Workflow | Data retrieval, Scientific computation, Export / aggregation | none | not attached |
| `ospd.process-profiles.algae-bloom.select-products-sentinel2` | CommandLineTool | Selection / filtering | closeMatch: processes.cubes.load_collection | `generic-profiles.implementation-profile.product-selection` |
| `ospd.process-profiles.algae-bloom.download-band-sentinel2-stac-item` | CommandLineTool | Data retrieval | closeMatch: processes.cubes.load_collection, processes.cubes.filter_bands | `generic-profiles.implementation-profile.band-retrieval` |
| `ospd.process-profiles.algae-bloom.download-band-sentinel2-product-safe` | CommandLineTool | Data retrieval | closeMatch: processes.cubes.load_collection, processes.cubes.filter_bands | not attached |
| `ospd.process-profiles.algae-bloom.reproject-image` | CommandLineTool | Pre-processing | closeMatch: processes.cubes.resample_spatial | `generic-profiles.implementation-profile.raster-resampling` |
| `ospd.process-profiles.algae-bloom.calculate-band` | CommandLineTool | Scientific computation | closeMatch: processes.cubes.reduce_dimension | `generic-profiles.implementation-profile.raster-band-math` |
| `ospd.process-profiles.algae-bloom.plot-image` | CommandLineTool | Export / aggregation | closeMatch: processes.cubes.save_result | `generic-profiles.implementation-profile.raster-rendering` |
| `ospd.process-profiles.kindgrove.mangrove-workflow` | Workflow | Filter configuration, Selection / filtering, Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none | not attached |
| `ospd.process-profiles.kindgrove.parse-aoi` | CommandLineTool | Filter configuration | none | not attached |
| `ospd.process-profiles.kindgrove.mangrove` | CommandLineTool | Selection / filtering, Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none | not attached |
| `ospd.process-profiles.water-bodies.water-bodies` | Workflow | Data retrieval, Scientific computation, Export / aggregation | none | not attached |
| `ospd.process-profiles.water-bodies.detect-water-body` | Workflow | Data retrieval, Scientific computation | none | not attached |
| `ospd.process-profiles.water-bodies.crop` | CommandLineTool | Data retrieval | closeMatch: processes.cubes.load_collection, processes.cubes.filter_bands | `generic-profiles.implementation-profile.band-retrieval` |
| `ospd.process-profiles.water-bodies.norm-diff` | CommandLineTool | Scientific computation | closeMatch: processes.math.indices.normalized_difference | `generic-profiles.implementation-profile.radiometric-index-single-band` |
| `ospd.process-profiles.water-bodies.otsu` | CommandLineTool | Scientific computation | none | `generic-profiles.implementation-profile.otsu-thresholding` |
| `ospd.process-profiles.water-bodies.stac` | CommandLineTool | Export / aggregation | closeMatch: processes.cubes.save_result | not attached |
| `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps` | Workflow | Filter configuration, Selection / filtering, Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none | not attached |
| `ospd.process-profiles.kindgrove-steps.parse-aoi-steps` | CommandLineTool | Filter configuration | none | not attached |
| `ospd.process-profiles.kindgrove-steps.select-scene` | CommandLineTool | Selection / filtering | closeMatch: processes.cubes.load_collection | `generic-profiles.implementation-profile.product-selection` |
| `ospd.process-profiles.kindgrove-steps.download-band` | CommandLineTool | Data retrieval | closeMatch: processes.cubes.load_collection, processes.cubes.filter_bands | `generic-profiles.implementation-profile.band-retrieval` |
| `ospd.process-profiles.kindgrove-steps.reproject-band` | CommandLineTool | Pre-processing | closeMatch: processes.cubes.resample_spatial | `generic-profiles.implementation-profile.raster-reprojection` |
| `ospd.process-profiles.kindgrove-steps.calculate-indices` | CommandLineTool | Scientific computation | none | `generic-profiles.implementation-profile.radiometric-index-single-band` |
| `ospd.process-profiles.kindgrove-steps.estimate-biomass` | CommandLineTool | Scientific computation | none | not attached |
| `ospd.process-profiles.kindgrove-steps.export-stac` | CommandLineTool | Export / aggregation | closeMatch: processes.cubes.save_result | not attached |
<!-- /CWL_TABLE -->

### Live processes of the Geonovum testbed

<!-- LIVE_TABLE -->
| Identifier | Live process | Phase(s) | Implementation Profile (tier 3) |
|---|---|---|---|
| `ospd.process-profiles.sqlmm.intersects` | `Intersects` | Scientific computation | `generic-profiles.implementation-profile.intersects` |
| `ospd.process-profiles.sqlmm.disjoint` | `Disjoint` | Scientific computation | `generic-profiles.implementation-profile.disjoint` |
| `ospd.process-profiles.sqlmm.contains` | `Contains` | Scientific computation | `generic-profiles.implementation-profile.contains` |
| `ospd.process-profiles.sqlmm.within` | `Within` | Scientific computation | `generic-profiles.implementation-profile.within` |
| `ospd.process-profiles.sqlmm.touches` | `Touches` | Scientific computation | `generic-profiles.implementation-profile.touches` |
| `ospd.process-profiles.sqlmm.crosses` | `Crosses` | Scientific computation | `generic-profiles.implementation-profile.crosses` |
| `ospd.process-profiles.sqlmm.equals` | `Equals` | Scientific computation | `generic-profiles.implementation-profile.equals` |
| `ospd.process-profiles.sqlmm.intersection` | `Intersection` | Scientific computation | `generic-profiles.implementation-profile.intersection` |
| `ospd.process-profiles.sqlmm.union` | `Union` | Scientific computation | `generic-profiles.implementation-profile.union` |
| `ospd.process-profiles.sqlmm.difference` | `Difference` | Scientific computation | `generic-profiles.implementation-profile.difference` |
| `ospd.process-profiles.sqlmm.symdifference` | `SymDifference` | Scientific computation | `generic-profiles.implementation-profile.symdifference` |
| `ospd.process-profiles.sqlmm.buffer` | `Buffer` | Scientific computation | `generic-profiles.implementation-profile.buffer` |
| `ospd.process-profiles.sqlmm.centroid` | `Centroid` | Scientific computation | `generic-profiles.implementation-profile.centroid` |
| `ospd.process-profiles.sqlmm.convex-hull` | `ConvexHull` | Scientific computation | `generic-profiles.implementation-profile.convex-hull` |
| `ospd.process-profiles.sqlmm.is-simple` | `IsSimple` | Scientific computation | `generic-profiles.implementation-profile.is-simple` |
| `ospd.process-profiles.sqlmm.area` | `GetArea` | Scientific computation | `generic-profiles.implementation-profile.area` |
| `ospd.process-profiles.raster.reprojection` | `Gdal_Warp` | Pre-processing | `generic-profiles.implementation-profile.raster-reprojection` |
| `ospd.process-profiles.raster.band-math` | `OTB.BandMath` | Scientific computation | `generic-profiles.implementation-profile.raster-band-math` |
| `ospd.process-profiles.raster.radiometric-index` | `OTB.RadiometricIndices` | Scientific computation | `generic-profiles.implementation-profile.radiometric-index` |
| `ospd.process-profiles.raster.extract-roi` | `OTB.ExtractROI` | Pre-processing | `generic-profiles.implementation-profile.raster-crop` |
| `ospd.process-profiles.raster.format-conversion` | `Gdal_Translate` | Export / aggregation | `generic-profiles.implementation-profile.raster-format-conversion` |
| `ospd.process-profiles.raster.band-math-multiband` | `OTB.BandMathX` | Scientific computation | `generic-profiles.implementation-profile.raster-band-math-multiband` |
| `ospd.process-profiles.raster.extent` | `OTB.ImageEnvelope` | Export / aggregation | `generic-profiles.implementation-profile.raster-extent` |
| `ospd.process-profiles.vector.geometry-extent` | `SAGA.shapes_tools.19` | Export / aggregation | `generic-profiles.implementation-profile.geometry-extent` |
| `ospd.process-profiles.terrain.slope` | `SAGA.ta_morphometry.0` | Scientific computation | `generic-profiles.implementation-profile.slope` |
| `ospd.process-profiles.terrain.terrain-ruggedness-index` | `SAGA.ta_morphometry.16` | Scientific computation | `generic-profiles.implementation-profile.terrain-ruggedness-index` |
| `ospd.process-profiles.terrain.topographic-position-index` | `SAGA.ta_morphometry.18` | Scientific computation | `generic-profiles.implementation-profile.topographic-position-index` |
| `ospd.process-profiles.terrain.hillshading` | `SAGA.ta_lighting.0` | Scientific computation | `generic-profiles.implementation-profile.analytical-hillshading` |
| `ospd.process-profiles.pointcloud.point-cloud-to-grid` | `SAGA.pointcloud_tools.4` | Pre-processing | `generic-profiles.implementation-profile.point-cloud-to-grid` |
| `ospd.process-profiles.pointcloud.point-cloud-thinning` | `SAGA.pointcloud_tools.9` | Pre-processing | `generic-profiles.implementation-profile.point-cloud-thinning` |
| `ospd.process-profiles.pointcloud.point-cloud-to-shapes` | `SAGA.pointcloud_tools.5` | Pre-processing | `generic-profiles.implementation-profile.point-cloud-to-shapes` |
<!-- /LIVE_TABLE -->

Shared: `ospd.process-profiles.process-type` — schema of a candidate process-type register entry (Activity 4).

## What each process profile contains

| Artefact | Validated against |
|---|---|
| `processDescription` (default schema) | this profile = `ogc.api.processes.part1.v1.schemas.process` + `ogc.api.processes.part2.v1.schemas.staticIndicator` + id/input/output constraints |
| raw `cwl-to-ogcprocess` output (when a manual correction was needed) | `ogc.api.processes.part1.v1.schemas.process` |
| OGC Application Package (Part 2 deploy body, `executionUnit` = link to the CWL) | `ogc.api.processes.part2.v1.schemas.ogcapppkg` |
| execute request / results | `ogc.api.processes.part1.v1.schemas.execute` / `results` |
| provenance chain | `ogc.bbr.provenance.provenance` |
| process run (CommandLineTool) | `ogc.bbr.wf4ever.wfprov.ProcessRun` (gap GP-1 in the generic profile) |
| execution bundle (Workflow) | `ogc.bbr.provenance.execution` |
| process-type entry | `ospd.process-profiles.process-type` |

## Documentation

- [docs/DEVIATIONS.md](docs/DEVIATIONS.md) — deviations from / gaps in `eoap.cct.cwl-to-ogcprocess`
- [docs/PROVENANCE-GAPS.md](docs/PROVENANCE-GAPS.md) — gaps in `bblocks-generic-provenance-profile`
- [docs/OPENEO-EQUIVALENCES.md](docs/OPENEO-EQUIVALENCES.md) — equivalence decisions and criteria
- [docs/WORKFLOW-COMPARISON.md](docs/WORKFLOW-COMPARISON.md) — structural parallels and differences across W1/W2/W3
- [docs/ATTACHMENTS.md](docs/ATTACHMENTS.md) — which CWL process implements which Implementation Profile, and why the others do not
- [docs/FORMAT-CHECK.md](docs/FORMAT-CHECK.md) — tier-3 representations against the formats served at tier 4, with the assumed gaps
- [docs/OPEN-QUESTIONS.md](docs/OPEN-QUESTIONS.md)
- [docs/VALIDATION.md](docs/VALIDATION.md) — validation status (Docker build passing, 52/52)

## Regenerating

```bash
# needs jq, python3 (pyyaml, prov>=2 for the W3C PROV-JSONLD examples), git, cwltool + Docker
python3 scripts/run_workflows.py --sources-root DIR --runs-root DIR --build-images --generate
#   clones the pinned sources (scripts/sources.yaml `repo:`/`commit:`, or downloads+checksums a
#   `release:` source) under --sources-root when missing, runs each entry under `runs:` with
#   `cwltool --provenance` (asks for the Copernicus S3 credentials, or reads
#   CDSE_S3_ACCESS_KEY / CDSE_S3_SECRET_KEY), stores the research objects under --runs-root as
#   named in `runs:`, then regenerates; --only NAME picks runs, --force replaces an existing bag,
#   --no-fetch leaves the clones/downloads alone
python3 scripts/generate.py --sources-root DIR --runs-root DIR   # regenerate only, never downloads
python3 scripts/validate_offline.py --deps-root ../   # pre-check only
./build.sh                                             # authoritative validation (Docker)
./view.sh                                              # http://localhost:9090
```

Generated files are overwritten; hand-written content lives in `scripts/profiles.yaml` and `docs/`.
The run-derived examples (times, engine, container images, output names and checksums) are read
from real `cwltool --provenance` research objects declared under `runs:` in `scripts/sources.yaml`;
those are local directories (the W1 one carries a 3.1 GB payload) and are not part of this
repository. Without them the generator stops.

## License

Apache-2.0 for this register. The W1 and W2b CWL files are CC-BY-NC-SA-4.0 and are **referenced by
URL only**.
