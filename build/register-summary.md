# OSPD Process Profiles

OGC API - Processes profiles for the deployable CWL processes of the OSPD 2026 reference
workflows (W1 Algae Bloom, W2 KindGrove mangrove biomass, W3 Water Bodies detection, W2b a
step-decomposed reimplementation of KindGrove), each linked to its CWL source, the generic
provenance profile, the EOAP CWL custom types and the openEO Building Blocks.


This register is produced by GeoLabs under OSPD 2026 (D100 Workflow Profiler, D120 OGC API
Processes Profiler). It holds one Building Block per deployable CWL process (`CommandLineTool`
or `Workflow`) identified in the workflow observability investigation.

Each process profile combines:

- a reference to the source CWL (linked by URL at a pinned commit, never copied);
- an OGC API - Processes Part 1 `processDescription` derived with the
  `eoap.cct.cwl-to-ogcprocess` mapping (deviations are documented, not hidden);
- a provenance view expressed as an instance of the generic provenance profile
  (`ogc.bbr.provenance.*`);
- a candidate process-type entry (`ospd.process-profiles.process-type`) for the OSPD
  process-type register (Activity 4);
- proposed openEO equivalences (`ogc.openeo.*`) with an explicit level
  (exactMatch / closeMatch / none) and rationale;
- a representative execution example.

All mappings are proposed correspondences offered for review, not settled equivalences.


## Building Blocks

### `ospd.process-profiles.process-type` — Process type register entry

**Type:** schema

Candidate entry for the OSPD process-type register (Activity 4), linking a process profile, its six-phase position, its provenance class and its proposed openEO equivalences.

### `ospd.process-profiles.pointcloud.point-cloud-thinning` — Process profile: SAGA.pointcloud_tools.9

**Type:** schema

Process profile of the live OGC API - Processes process `SAGA.pointcloud_tools.9` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.pointcloud.point-cloud-to-grid` — Process profile: SAGA.pointcloud_tools.4

**Type:** schema

Process profile of the live OGC API - Processes process `SAGA.pointcloud_tools.4` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.pointcloud.point-cloud-to-shapes` — Process profile: SAGA.pointcloud_tools.5

**Type:** schema

Process profile of the live OGC API - Processes process `SAGA.pointcloud_tools.5` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.raster.band-math` — Process profile: OTB.BandMath

**Type:** schema

Process profile of the live OGC API - Processes process `OTB.BandMath` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.raster.band-math-multiband` — Process profile: OTB.BandMathX

**Type:** schema

Process profile of the live OGC API - Processes process `OTB.BandMathX` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.raster.extent` — Process profile: OTB.ImageEnvelope

**Type:** schema

Process profile of the live OGC API - Processes process `OTB.ImageEnvelope` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.raster.extract-roi` — Process profile: OTB.ExtractROI

**Type:** schema

Process profile of the live OGC API - Processes process `OTB.ExtractROI` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.raster.format-conversion` — Process profile: Gdal_Translate

**Type:** schema

Process profile of the live OGC API - Processes process `Gdal_Translate` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.raster.radiometric-index` — Process profile: OTB.RadiometricIndices

**Type:** schema

Process profile of the live OGC API - Processes process `OTB.RadiometricIndices` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.raster.reprojection` — Process profile: Gdal_Warp

**Type:** schema

Process profile of the live OGC API - Processes process `Gdal_Warp` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.area` — Process profile: GetArea

**Type:** schema

Process profile of the live OGC API - Processes process `GetArea` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.buffer` — Process profile: Buffer

**Type:** schema

Process profile of the live OGC API - Processes process `Buffer` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.centroid` — Process profile: Centroid

**Type:** schema

Process profile of the live OGC API - Processes process `Centroid` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.contains` — Process profile: Contains

**Type:** schema

Process profile of the live OGC API - Processes process `Contains` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.convex-hull` — Process profile: ConvexHull

**Type:** schema

Process profile of the live OGC API - Processes process `ConvexHull` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.crosses` — Process profile: Crosses

**Type:** schema

Process profile of the live OGC API - Processes process `Crosses` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.difference` — Process profile: Difference

**Type:** schema

Process profile of the live OGC API - Processes process `Difference` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.disjoint` — Process profile: Disjoint

**Type:** schema

Process profile of the live OGC API - Processes process `Disjoint` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.equals` — Process profile: Equals

**Type:** schema

Process profile of the live OGC API - Processes process `Equals` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.intersection` — Process profile: Intersection

**Type:** schema

Process profile of the live OGC API - Processes process `Intersection` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.intersects` — Process profile: Intersects

**Type:** schema

Process profile of the live OGC API - Processes process `Intersects` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.is-simple` — Process profile: IsSimple

**Type:** schema

Process profile of the live OGC API - Processes process `IsSimple` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.symdifference` — Process profile: SymDifference

**Type:** schema

Process profile of the live OGC API - Processes process `SymDifference` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.touches` — Process profile: Touches

**Type:** schema

Process profile of the live OGC API - Processes process `Touches` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.union` — Process profile: Union

**Type:** schema

Process profile of the live OGC API - Processes process `Union` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.sqlmm.within` — Process profile: Within

**Type:** schema

Process profile of the live OGC API - Processes process `Within` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.terrain.hillshading` — Process profile: SAGA.ta_lighting.0

**Type:** schema

Process profile of the live OGC API - Processes process `SAGA.ta_lighting.0` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.terrain.slope` — Process profile: SAGA.ta_morphometry.0

**Type:** schema

Process profile of the live OGC API - Processes process `SAGA.ta_morphometry.0` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.terrain.terrain-ruggedness-index` — Process profile: SAGA.ta_morphometry.16

**Type:** schema

Process profile of the live OGC API - Processes process `SAGA.ta_morphometry.16` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.terrain.topographic-position-index` — Process profile: SAGA.ta_morphometry.18

**Type:** schema

Process profile of the live OGC API - Processes process `SAGA.ta_morphometry.18` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.vector.geometry-extent` — Process profile: SAGA.shapes_tools.19

**Type:** schema

Process profile of the live OGC API - Processes process `SAGA.shapes_tools.19` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

### `ospd.process-profiles.algae-bloom.calculate-band` — Process profile: calculate-band

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `calculate-band` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.download-band-sentinel2-product-safe` — Process profile: download-band-sentinel2-product-safe

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `download-band-sentinel2-product-safe` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.download-band-sentinel2-stac-item` — Process profile: download-band-sentinel2-stac-item

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `download-band-sentinel2-stac-item` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.plot-image` — Process profile: plot-image

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `plot-image` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.reproject-image` — Process profile: reproject-image

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `reproject-image` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.select-products-sentinel2` — Process profile: select-products-sentinel2

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `select-products-sentinel2` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.workflow-copernicus` — Process profile: algae-usecase-workflow-copernicus

**Type:** schema

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-copernicus` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.workflow-copernicus-process` — Process profile: algae-usecase-workflow-copernicus-process

**Type:** schema

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-copernicus-process` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.workflow-earth-search` — Process profile: algae-usecase-workflow-earth-search

**Type:** schema

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-earth-search` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.workflow-earth-search-process` — Process profile: algae-usecase-workflow-earth-search-process

**Type:** schema

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-earth-search-process` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove.mangrove` — Process profile: mangrove_cli

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `mangrove_cli` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove.mangrove-workflow` — Process profile: mangrove-workflow

**Type:** schema

OGC API - Processes profile of the CWL Workflow `mangrove-workflow` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove.parse-aoi` — Process profile: parse_aoi

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `parse_aoi` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove-steps.calculate-indices` — Process profile: calculate_indices

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `calculate_indices` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove-steps.download-band` — Process profile: download_band

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `download_band` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove-steps.estimate-biomass` — Process profile: estimate_biomass

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `estimate_biomass` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove-steps.export-stac` — Process profile: export_stac

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `export_stac` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps` — Process profile: mangrove-workflow-steps

**Type:** schema

OGC API - Processes profile of the CWL Workflow `mangrove-workflow-steps` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove-steps.parse-aoi-steps` — Process profile: parse_aoi

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `parse_aoi` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove-steps.reproject-band` — Process profile: reproject_band

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `reproject_band` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove-steps.select-scene` — Process profile: select_scene

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `select_scene` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.water-bodies.crop` — Process profile: crop

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `crop` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.water-bodies.detect-water-body` — Process profile: detect_water_body

**Type:** schema

OGC API - Processes profile of the CWL Workflow `detect_water_body` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.water-bodies.norm-diff` — Process profile: norm_diff

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `norm_diff` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.water-bodies.otsu` — Process profile: otsu

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `otsu` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.water-bodies.stac` — Process profile: stac

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `stac` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.water-bodies.water-bodies` — Process profile: water-bodies

**Type:** schema

OGC API - Processes profile of the CWL Workflow `water-bodies` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

