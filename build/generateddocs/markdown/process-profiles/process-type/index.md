
# Process type register entry (Schema)

`ospd.process-profiles.process-type` *v0.1*

Candidate entry for the OSPD process-type register (Activity 4), linking a process profile, its six-phase position, its provenance class and its proposed openEO equivalences.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Schema of a **candidate process-type register entry** (OSPD Activity 4).

A process type classifies the activities recorded in provenance. The link is one-way and uses
plain W3C PROV: a provenance `Activity` (or a `wfprov:ProcessRun` / `wfprov:WorkflowRun`) of this
type carries the entry `id` in `activityType`. The entry itself is a SKOS concept:

- `phase` (→ `skos:broader`) positions the process in the six-phase framework
  (filter configuration → selection/filtering → data retrieval → pre-processing →
  scientific computation → export/aggregation);
- `exactMatch` / `closeMatch` / `relatedMatch` (→ SKOS mapping properties) point to openEO
  Building Blocks (`https://www.opengis.net/def/bblocks/ogc.openeo.*`);
- `openeoEquivalence.level` states the equivalence level explicitly, including `none`, which
  SKOS cannot express, with the rationale and, for composite or opaque processes, a
  stage-by-stage decomposition.

## Type, plan and process description are three things

The entry describes the **type** of activity. What an activity of that type executes is its
**plan** (`prov:Plan`), kept apart in `plan` with its own IRI: the OGC Application Package served
at `/processes/{processID}/package` by [OGC API - Processes - Part 2: Deploy, Replace,
Undeploy](https://docs.ogc.org/DRAFTS/20-044.html) (requirement
`/req/deploy-replace-undeploy/package-get-op`), whose `executionUnit` is the pinned CWL and which
also carries the EOAP CWL custom types the CWL uses. Every run of the type records **the same
IRI** as its `qualifiedAssociation.hadPlan` -- and `wfprov:describedByProcess` /
`describedByWorkflow`, whose `wfdesc:Workflow` range is itself a `prov:Plan` in wfprov -- so the
plan named at type level and the plan followed by each run are one resource.

`processDescription` is the third thing: the interface (`/processes/{processID}`) the type is
profiled from, which the run's input and output entities point into (`#inputs/{name}`).

A process implemented natively by its server (`mutable: false`, as on a ZOO-Project deployment)
has no Application Package: Part 2 serves `/package` only for dynamically deployed processes
(requirement `package-get-op`, C). Such an entry has no `plan`; its `processDescription.href` is
the live process.

Status values follow ISO 19135. Entries in this register are candidates: at most `submitted`.

The `pp:` vocabulary (`https://geolabs.github.io/bblocks-process-profiles/def/`) and the phase IRIs
are provisional, pending a decision on the process-type register namespace.

## Examples

### reproject-image (closeMatch)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image",
  "type": "ProcessType",
  "prefLabel": "Performs image reprojection.",
  "definition": "Performs a reprojection over image bands and returns the resulting GeoTiff.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
  ],
  "profile": "ospd.process-profiles.algae-bloom.reproject-image",
  "processDescription": {
    "id": "reproject-image",
    "version": "1.0.0",
    "href": "https://ospd.example.org/ogc-api/processes/reproject-image"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/reproject-image/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "reproject-image",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0",
    "cctDependencies": [],
    "candidateCctDependencies": []
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image",
  "type": "ProcessType",
  "prefLabel": "Performs image reprojection.",
  "definition": "Performs a reprojection over image bands and returns the resulting GeoTiff.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
  ],
  "profile": "ospd.process-profiles.algae-bloom.reproject-image",
  "processDescription": {
    "id": "reproject-image",
    "version": "1.0.0",
    "href": "https://ospd.example.org/ogc-api/processes/reproject-image"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/reproject-image/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "reproject-image",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0",
    "cctDependencies": [],
    "candidateCctDependencies": []
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place."
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <https://w3id.org/ogc/api/processes/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial> ;
    skos:definition "Performs a reprojection over image bands and returns the resulting GeoTiff." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Performs image reprojection." ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place." ] ;
    pp:plan <https://ospd.example.org/ogc-api/processes/reproject-image/package> ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/reproject-image> ;
    pp:profile "ospd.process-profiles.algae-bloom.reproject-image" ;
    pp:provenanceClass <http://purl.org/wf4ever/wfprov#ProcessRun> ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/reproject-image> rdfs:seeAlso <https://ospd.example.org/ogc-api/processes/reproject-image> ;
    pp:version "1.0.0" .

<https://ospd.example.org/ogc-api/processes/reproject-image/package> a prov:Plan ;
    dcterms:license <https://spdx.org/licenses/CC-BY-NC-SA-4.0> ;
    pp:cwlClass "CommandLineTool" ;
    pp:cwlId "reproject-image" ;
    ns2:executionUnit [ dcterms:format "application/cwl+yaml" ;
            ns1:relation <http://www.opengis.net/def/rel/ogc/1.0/executionUnit> ;
            oa:hasTarget <https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl> ] .


```


### KindGrove mangrove (none, with decomposition)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove",
  "type": "ProcessType",
  "prefLabel": "Mangrove biomass and carbon estimation",
  "definition": "Detects mangroves from Sentinel-2 L2A vegetation indices within a bounding box and estimates above-ground biomass and carbon stock (ipython2cwl binary of the KindGrove notebook).",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.kindgrove.mangrove",
  "processDescription": {
    "id": "mangrove_cli",
    "version": "0.0.1",
    "href": "https://ospd.example.org/ogc-api/processes/mangrove_cli"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/mangrove_cli/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/GeoLabs/bblocks-eoap-cct/raw/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove_cli",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "mangrove_cli",
    "license": "https://spdx.org/licenses/Apache-2.0",
    "cctDependencies": [],
    "candidateCctDependencies": [
      "eoap.cct.bbox"
    ]
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Opaque: one ipython2cwl binary running the whole notebook. No single openEO process; each notebook stage has a closeMatch (decomposition). run_udf could wrap the binary but expects a data cube in and out, which this tool does not follow (it searches and downloads its own data).",
    "decomposition": [
      {
        "stage": "STAC search, Earth-Search sentinel-2-l2a, bbox, cloud cover, last N days",
        "openeo": [
          "ogc.openeo.processes.cubes.load_collection"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "NDVI (nir-red)/(nir+red+1e-8)",
        "openeo": [
          "ogc.openeo.processes.cubes.ndvi",
          "ogc.openeo.processes.math.indices.normalized_difference"
        ],
        "level": "closeMatch",
        "note": "epsilon 1e-8 in the denominator"
      },
      {
        "stage": "NDWI (green-nir)/(green+nir+1e-8)",
        "openeo": [
          "ogc.openeo.processes.math.indices.normalized_difference"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "SAVI ((nir-red)/(nir+red+0.5))*1.5",
        "openeo": [],
        "level": "none",
        "note": "no stable process; composition of add/subtract/divide/multiply"
      },
      {
        "stage": "mangrove mask: 0.3<NDVI<0.9 and NDWI>-0.3 and SAVI>0.2",
        "openeo": [
          "ogc.openeo.processes.comparison.gt",
          "ogc.openeo.processes.comparison.lt",
          "ogc.openeo.processes.logic.and",
          "ogc.openeo.processes.cubes.mask"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "biomass = 250.5*NDVI - 75.2",
        "openeo": [
          "ogc.openeo.processes.cubes.apply",
          "ogc.openeo.processes.math.multiply",
          "ogc.openeo.processes.math.subtract"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "carbon stock and totals (IPCC carbon fraction 0.47)",
        "openeo": [
          "ogc.openeo.processes.cubes.aggregate_spatial",
          "ogc.openeo.processes.math.sum",
          "ogc.openeo.processes.math.multiply"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "export CSV + GeoTIFF",
        "openeo": [
          "ogc.openeo.processes.cubes.save_result"
        ],
        "level": "closeMatch",
        "note": "CSV summaries are not a raster format"
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove",
  "type": "ProcessType",
  "prefLabel": "Mangrove biomass and carbon estimation",
  "definition": "Detects mangroves from Sentinel-2 L2A vegetation indices within a bounding box and estimates above-ground biomass and carbon stock (ipython2cwl binary of the KindGrove notebook).",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.kindgrove.mangrove",
  "processDescription": {
    "id": "mangrove_cli",
    "version": "0.0.1",
    "href": "https://ospd.example.org/ogc-api/processes/mangrove_cli"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/mangrove_cli/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/GeoLabs/bblocks-eoap-cct/raw/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove_cli",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "mangrove_cli",
    "license": "https://spdx.org/licenses/Apache-2.0",
    "cctDependencies": [],
    "candidateCctDependencies": [
      "eoap.cct.bbox"
    ]
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Opaque: one ipython2cwl binary running the whole notebook. No single openEO process; each notebook stage has a closeMatch (decomposition). run_udf could wrap the binary but expects a data cube in and out, which this tool does not follow (it searches and downloads its own data).",
    "decomposition": [
      {
        "stage": "STAC search, Earth-Search sentinel-2-l2a, bbox, cloud cover, last N days",
        "openeo": [
          "ogc.openeo.processes.cubes.load_collection"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "NDVI (nir-red)/(nir+red+1e-8)",
        "openeo": [
          "ogc.openeo.processes.cubes.ndvi",
          "ogc.openeo.processes.math.indices.normalized_difference"
        ],
        "level": "closeMatch",
        "note": "epsilon 1e-8 in the denominator"
      },
      {
        "stage": "NDWI (green-nir)/(green+nir+1e-8)",
        "openeo": [
          "ogc.openeo.processes.math.indices.normalized_difference"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "SAVI ((nir-red)/(nir+red+0.5))*1.5",
        "openeo": [],
        "level": "none",
        "note": "no stable process; composition of add/subtract/divide/multiply"
      },
      {
        "stage": "mangrove mask: 0.3<NDVI<0.9 and NDWI>-0.3 and SAVI>0.2",
        "openeo": [
          "ogc.openeo.processes.comparison.gt",
          "ogc.openeo.processes.comparison.lt",
          "ogc.openeo.processes.logic.and",
          "ogc.openeo.processes.cubes.mask"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "biomass = 250.5*NDVI - 75.2",
        "openeo": [
          "ogc.openeo.processes.cubes.apply",
          "ogc.openeo.processes.math.multiply",
          "ogc.openeo.processes.math.subtract"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "carbon stock and totals (IPCC carbon fraction 0.47)",
        "openeo": [
          "ogc.openeo.processes.cubes.aggregate_spatial",
          "ogc.openeo.processes.math.sum",
          "ogc.openeo.processes.math.multiply"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "export CSV + GeoTIFF",
        "openeo": [
          "ogc.openeo.processes.cubes.save_result"
        ],
        "level": "closeMatch",
        "note": "CSV summaries are not a raster format"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/api/processes/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering> ;
    skos:definition "Detects mangroves from Sentinel-2 L2A vegetation indices within a bounding box and estimates above-ground biomass and carbon stock (ipython2cwl binary of the KindGrove notebook)." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Mangrove biomass and carbon estimation" ;
    pp:openeoEquivalence [ pp:decomposition ( [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.load_collection" ;
                        pp:stage "STAC search, Earth-Search sentinel-2-l2a, bbox, cloud cover, last N days" ] [ skos:note "epsilon 1e-8 in the denominator" ;
                        pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.ndvi",
                            "ogc.openeo.processes.math.indices.normalized_difference" ;
                        pp:stage "NDVI (nir-red)/(nir+red+1e-8)" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.math.indices.normalized_difference" ;
                        pp:stage "NDWI (green-nir)/(green+nir+1e-8)" ] [ skos:note "no stable process; composition of add/subtract/divide/multiply" ;
                        pp:equivalenceLevel "none" ;
                        pp:stage "SAVI ((nir-red)/(nir+red+0.5))*1.5" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.comparison.gt",
                            "ogc.openeo.processes.comparison.lt",
                            "ogc.openeo.processes.cubes.mask",
                            "ogc.openeo.processes.logic.and" ;
                        pp:stage "mangrove mask: 0.3<NDVI<0.9 and NDWI>-0.3 and SAVI>0.2" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.apply",
                            "ogc.openeo.processes.math.multiply",
                            "ogc.openeo.processes.math.subtract" ;
                        pp:stage "biomass = 250.5*NDVI - 75.2" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.aggregate_spatial",
                            "ogc.openeo.processes.math.multiply",
                            "ogc.openeo.processes.math.sum" ;
                        pp:stage "carbon stock and totals (IPCC carbon fraction 0.47)" ] [ skos:note "CSV summaries are not a raster format" ;
                        pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.save_result" ;
                        pp:stage "export CSV + GeoTIFF" ] ) ;
            pp:equivalenceLevel "none" ;
            pp:rationale "Opaque: one ipython2cwl binary running the whole notebook. No single openEO process; each notebook stage has a closeMatch (decomposition). run_udf could wrap the binary but expects a data cube in and out, which this tool does not follow (it searches and downloads its own data)." ] ;
    pp:plan <https://ospd.example.org/ogc-api/processes/mangrove_cli/package> ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove_cli> ;
    pp:profile "ospd.process-profiles.kindgrove.mangrove" ;
    pp:provenanceClass <http://purl.org/wf4ever/wfprov#ProcessRun> ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove_cli> rdfs:seeAlso <https://ospd.example.org/ogc-api/processes/mangrove_cli> ;
    pp:version "0.0.1" .

<https://ospd.example.org/ogc-api/processes/mangrove_cli/package> a prov:Plan ;
    dcterms:license <https://spdx.org/licenses/Apache-2.0> ;
    pp:candidateCctDependency "eoap.cct.bbox" ;
    pp:cwlClass "CommandLineTool" ;
    pp:cwlId "mangrove_cli" ;
    ns1:executionUnit [ dcterms:format "application/cwl+yaml" ;
            ns2:relation <http://www.opengis.net/def/rel/ogc/1.0/executionUnit> ;
            oa:hasTarget <https://github.com/GeoLabs/bblocks-eoap-cct/raw/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove_cli> ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Candidate entry for the OSPD process-type register (Activity 4). A process
  type classifies the

  activities recorded in provenance: a provenance Activity of this type carries the
  entry `id` as

  its `activityType`. The entry is modelled as a SKOS concept; openEO equivalences
  use the SKOS

  mapping properties.


  The entry describes the *type* of activity only. What an activity of this type executes
  -- its

  plan, a `prov:Plan` -- is kept apart in `plan`: the OGC Application Package served
  by OGC API -

  Processes - Part 2 (Deploy, Replace, Undeploy) at `/processes/{processID}/package`,
  whose

  execution unit is the pinned CWL. A run of this type records the same IRI as its

  `qualifiedAssociation.hadPlan`. A process implemented natively by its server (`mutable:
  false`)

  has no Application Package (Part 2 serves `/package` only for dynamically deployed
  processes)

  and so no `plan`; `processDescription` is then the only link to what is executed.

  '
type: object
required:
- id
- type
- prefLabel
- definition
- inScheme
- status
- phase
- profile
- processDescription
- provenanceClass
- openeoEquivalence
properties:
  id:
    description: IRI of the process type (also used as `activityType` in provenance
      records).
    type: string
    format: uri
    x-jsonld-id: '@id'
  type:
    const: ProcessType
    x-jsonld-id: '@type'
  prefLabel:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
  definition:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    description: IRI of the process-type register (concept scheme) this entry is proposed
      to.
    type: string
    format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status:
    description: ISO 19135 item status. Entries produced here are candidates, hence
      `submitted` at most.
    type: string
    enum:
    - submitted
    - valid
    - invalid
    - superseded
    - retired
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/status
  phase:
    description: Position(s) in the six-phase workflow framework.
    type: array
    minItems: 1
    items:
      type: string
      enum:
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
    x-jsonld-type: '@id'
  profile:
    description: Identifier of the process-profile Building Block.
    type: string
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/profile
  processDescription:
    description: The OGC API - Processes processDescription this type is profiled
      from, at `href` (the `/processes/{processID}` resource). For a CWL-sourced process
      it is the description the Application Package would deploy, under the illustrative
      host `ospd.example.org`; for a live process (e.g. a ZOO-Project deployment,
      `ospd.process-profiles.sqlmm.*`) the real one.
    type: object
    required:
    - id
    - version
    - href
    properties:
      id:
        type: string
        x-jsonld-id: '@id'
      version:
        type: string
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/version
      href:
        type: string
        format: uri
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
        x-jsonld-type: '@id'
      license:
        description: Of a live process; omitted, not null, when it declares none --
          do not assume one.
        type: string
        format: uri
        x-jsonld-id: http://purl.org/dc/terms/license
        x-jsonld-type: '@id'
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/processDescription
  plan:
    description: 'The plan (`prov:Plan`) an activity of this type executes: the OGC
      Application Package at `/processes/{processID}/package` (OGC API - Processes
      - Part 2, requirement /req/deploy-replace-undeploy/package-get-op), whose `executionUnit`
      is the pinned CWL. Present only for a CWL-sourced process.'
    type: object
    required:
    - id
    - type
    - executionUnit
    - cwlClass
    - cwlId
    properties:
      id:
        type: string
        format: uri
        pattern: /processes/[^/]+/package$
        x-jsonld-id: '@id'
      type:
        const: Plan
        x-jsonld-id: '@type'
      executionUnit:
        description: Same link as the Application Package's own `executionUnit` (examples/ogcapppkg.json).
        type: object
        required:
        - href
        - type
        properties:
          href:
            description: Pinned URL of the CWL document.
            type: string
            format: uri
            x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
            x-jsonld-type: '@id'
          type:
            type: string
            x-jsonld-id: http://purl.org/dc/terms/format
          rel:
            type: string
            x-jsonld-id: http://www.iana.org/assignments/relation
            x-jsonld-type: '@id'
            x-jsonld-base: http://www.iana.org/assignments/relation/
        x-jsonld-id: https://w3id.org/ogc/api/processes/executionUnit
      cwlClass:
        enum:
        - CommandLineTool
        - Workflow
        - ExpressionTool
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cwlClass
      cwlId:
        type: string
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cwlId
      license:
        type: string
        format: uri
        x-jsonld-id: http://purl.org/dc/terms/license
        x-jsonld-type: '@id'
      cctDependencies:
        description: EOAP CWL custom types used by the CWL.
        type: array
        items:
          type: string
          pattern: ^eoap\.cct\.
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cctDependency
      candidateCctDependencies:
        description: EOAP CWL custom types that could replace plain CWL types (not
          used by the CWL).
        type: array
        items:
          type: string
          pattern: ^eoap\.cct\.
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/candidateCctDependency
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/plan
  provenanceClass:
    description: Class of the run records produced by executing this process.
    type: string
    enum:
    - http://purl.org/wf4ever/wfprov#ProcessRun
    - http://purl.org/wf4ever/wfprov#WorkflowRun
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/provenanceClass
    x-jsonld-type: '@id'
  implementsProfile:
    description: "IRI of the nearest applicable profile this process specialises,
      in the generic-profiles register -- normally an Implementation Profile (generic-profiles.implementation-profile.*,
      OGC 14-065 WPS 2.0.2 \xA77.5.3: standard data formats, still not one specific
      deployment's own choice), or a Generic Profile directly when no Implementation
      Profile exists yet. Optional: most processes have no standardised abstract counterpart
      at all. `processDescription` and `plan` (this entry's own concrete binding)
      are what further specialise it to one real, deployed process -- Implementation
      (instance level) in the same standard's terms."
    type: string
    format: uri
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/implementsProfile
    x-jsonld-type: '@id'
  hasStep:
    description: Process types of the steps of a Workflow.
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/hasStep
    x-jsonld-type: '@id'
  exactMatch:
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
    x-jsonld-type: '@id'
  closeMatch:
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#closeMatch
    x-jsonld-type: '@id'
  relatedMatch:
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#relatedMatch
    x-jsonld-type: '@id'
  openeoEquivalence:
    type: object
    required:
    - level
    - rationale
    properties:
      level:
        enum:
        - exactMatch
        - closeMatch
        - none
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/equivalenceLevel
      rationale:
        type: string
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/rationale
      decomposition:
        description: Ordered correspondence of the stages of a composite or opaque
          process.
        type: array
        items:
          type: object
          required:
          - stage
          - level
          properties:
            stage:
              type: string
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/stage
            openeo:
              type: array
              items:
                type: string
                pattern: ^ogc\.openeo\.
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/openeo
            level:
              enum:
              - exactMatch
              - closeMatch
              - none
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/equivalenceLevel
            note:
              type: string
              x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/decomposition
        x-jsonld-container: '@list'
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/openeoEquivalence
x-jsonld-extra-terms:
  ProcessType: http://www.w3.org/2004/02/skos/core#Concept
  Plan: http://www.w3.org/ns/prov#Plan
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  prov: http://www.w3.org/ns/prov#
  pp: https://geolabs.github.io/bblocks-process-profiles/def/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  oa: http://www.w3.org/ns/oa#
x-bblocks-metadata:
  itemIdentifier: ospd.process-profiles.process-type
  register: https://geolabs.github.io/bblocks-process-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-21'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ProcessType": "skos:Concept",
    "Plan": "prov:Plan",
    "id": "@id",
    "type": "@type",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "status": "pp:status",
    "phase": {
      "@id": "skos:broader",
      "@type": "@id"
    },
    "profile": "pp:profile",
    "processDescription": {
      "@context": {
        "version": "pp:version",
        "href": {
          "@id": "rdfs:seeAlso",
          "@type": "@id"
        },
        "license": {
          "@id": "dct:license",
          "@type": "@id"
        }
      },
      "@id": "pp:processDescription"
    },
    "plan": {
      "@context": {
        "executionUnit": {
          "@context": {
            "href": {
              "@id": "oa:hasTarget",
              "@type": "@id"
            },
            "type": "dct:format",
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            }
          },
          "@id": "https://w3id.org/ogc/api/processes/executionUnit"
        },
        "cwlClass": "pp:cwlClass",
        "cwlId": "pp:cwlId",
        "license": {
          "@id": "dct:license",
          "@type": "@id"
        },
        "cctDependencies": "pp:cctDependency",
        "candidateCctDependencies": "pp:candidateCctDependency"
      },
      "@id": "pp:plan"
    },
    "provenanceClass": {
      "@id": "pp:provenanceClass",
      "@type": "@id"
    },
    "implementsProfile": {
      "@id": "pp:implementsProfile",
      "@type": "@id"
    },
    "hasStep": {
      "@id": "pp:hasStep",
      "@type": "@id"
    },
    "exactMatch": {
      "@id": "skos:exactMatch",
      "@type": "@id"
    },
    "closeMatch": {
      "@id": "skos:closeMatch",
      "@type": "@id"
    },
    "relatedMatch": {
      "@id": "skos:relatedMatch",
      "@type": "@id"
    },
    "openeoEquivalence": {
      "@context": {
        "level": "pp:equivalenceLevel",
        "rationale": "pp:rationale",
        "decomposition": {
          "@context": {
            "stage": "pp:stage",
            "openeo": "pp:openeo",
            "note": "skos:note"
          },
          "@id": "pp:decomposition",
          "@container": "@list"
        }
      },
      "@id": "pp:openeoEquivalence"
    },
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "prov": "http://www.w3.org/ns/prov#",
    "pp": "https://geolabs.github.io/bblocks-process-profiles/def/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "oa": "http://www.w3.org/ns/oa#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld)

## Sources

* [ISO 19135-1 Geographic information - Procedures for item registration](https://www.iso.org/standard/54721.html)
* [SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/process-type`

