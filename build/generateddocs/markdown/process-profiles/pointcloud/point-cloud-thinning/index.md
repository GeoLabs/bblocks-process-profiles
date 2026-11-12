
# Process profile: SAGA.pointcloud_tools.9 (Schema)

`ospd.process-profiles.pointcloud.point-cloud-thinning` *v0.1*

Process profile of the live OGC API - Processes process `SAGA.pointcloud_tools.9` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of the live OGC API - Processes process `SAGA.pointcloud_tools.9` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9>.

> This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order.

(the process's own description, as served)

## The tool behind it

[SAGA pointcloud_tools 9 (Point Cloud Thinning, Simple)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_9.html) -- SAGA 7.3.0 tool library documentation, the version deployed on the testbed (not yet exposed by its processDescription).

Tool 9 of SAGA's Shapes - Point Clouds library (author V. Wichmann, LASERDATA GmbH, 2010; command line `saga_cmd pointcloud_tools 9`). It reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.

On this deployment:

- The live service labels its LAS input and output `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` the Implementation Profile declares.
- `NUMBER` (titled "Number of Points", default 0; the documentation describes it no further) is a live-only input.

## Implementation Profile

Implements [`Point cloud thinning (simple)`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning) (`generic-profiles.implementation-profile.point-cloud-thinning`, bblocks-generic-profiles).

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `INPUT` | input `points` | `point-cloud` |
| `PERCENT` | input `percentage` | `number` |
| `NUMBER` | -- (the deployment's own inputs, Table 21 footnote b) | -- |
| `RESULT` | output `result` | `point-cloud` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles, and the data type of each bound input/output.
- `process-type.json`: its candidate process-type entry.

## Examples

### Source (referenced)
The processDescription is fetched from the live service, not copied: <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9>.

### processDescription
Live OGC API - Processes processDescription, normalised (ZOO-Project-internal fields dropped).
#### json
```json
{
  "id": "SAGA.pointcloud_tools.9",
  "title": "Point Cloud Thinning (Simple)",
  "description": "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order. ",
  "version": "1.0.0",
  "jobControlOptions": [
    "sync-execute",
    "async-execute",
    "dismiss"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ],
  "inputs": {
    "INPUT": {
      "title": "Points",
      "description": "Points",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-lasf"
          }
        ]
      }
    },
    "PERCENT": {
      "title": "Percent",
      "description": "Reduce the number of points to this percentage.",
      "minOccurs": 0,
      "schema": {
        "type": "number",
        "default": 50,
        "format": "float",
        "minimum": 0,
        "maximum": 100,
        "nullable": true
      }
    },
    "NUMBER": {
      "title": "Number of Points",
      "description": "Number of Points",
      "minOccurs": 0,
      "schema": {
        "type": "integer",
        "default": 0,
        "nullable": true
      }
    }
  },
  "outputs": {
    "RESULT": {
      "title": "Thinned Points",
      "description": "Thinned Points",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-lasf"
          }
        ]
      }
    }
  },
  "mutable": false,
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9/execution"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/pointcloud/point-cloud-thinning/context.jsonld",
  "id": "SAGA.pointcloud_tools.9",
  "title": "Point Cloud Thinning (Simple)",
  "description": "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order. ",
  "version": "1.0.0",
  "jobControlOptions": [
    "sync-execute",
    "async-execute",
    "dismiss"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ],
  "inputs": {
    "INPUT": {
      "title": "Points",
      "description": "Points",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-lasf"
          }
        ]
      }
    },
    "PERCENT": {
      "title": "Percent",
      "description": "Reduce the number of points to this percentage.",
      "minOccurs": 0,
      "schema": {
        "type": "number",
        "default": 50,
        "format": "float",
        "minimum": 0,
        "maximum": 100,
        "nullable": true
      }
    },
    "NUMBER": {
      "title": "Number of Points",
      "description": "Number of Points",
      "minOccurs": 0,
      "schema": {
        "type": "integer",
        "default": 0,
        "nullable": true
      }
    }
  },
  "outputs": {
    "RESULT": {
      "title": "Thinned Points",
      "description": "Thinned Points",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-lasf"
          }
        ]
      }
    }
  },
  "mutable": false,
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9/execution"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/SAGA.pointcloud_tools.9> dcterms:description "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order. " ;
    dcterms:title "Point Cloud Thinning (Simple)" ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns4:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns3:INPUT [ dcterms:description "Points" ;
                    dcterms:title "Points" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-lasf" ] ] ] ;
            ns3:NUMBER [ dcterms:description "Number of Points" ;
                    dcterms:title "Number of Points" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "0"^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "integer" ] ] ;
            ns3:PERCENT [ dcterms:description "Reduce the number of points to this percentage." ;
                    dcterms:title "Percent" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "50"^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "number" ;
                            ns1:format "float" ;
                            ns1:maximum 100 ;
                            ns1:minimum 0 ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns2:RESULT [ dcterms:description "Thinned Points" ;
                    dcterms:title "Thinned Points" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-lasf" ] ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Each bound input/output also carries the `dataType` of that counterpart, a concept of bblocks-data-types. Which deployed input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the deployment's own additions (footnote b). Not what the deployment serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
#### json
```json
{
  "id": "SAGA.pointcloud_tools.9",
  "title": "Point Cloud Thinning (Simple)",
  "description": "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order. ",
  "version": "1.0.0",
  "jobControlOptions": [
    "sync-execute",
    "async-execute",
    "dismiss"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ],
  "mutable": false,
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9/execution"
    }
  ],
  "keywords": [
    "point cloud",
    "thinning"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    },
    {
      "title": "Generic Profile: Point cloud thinning",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning"
    },
    {
      "title": "Implementation Profile: Point cloud thinning (simple)",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning"
    }
  ],
  "inputs": {
    "INPUT": {
      "title": "Points",
      "description": "Points",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud",
      "keywords": [
        "point cloud"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points"
        },
        {
          "title": "Implementation Profile: Point cloud thinning (simple) -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/points"
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-lasf"
          }
        ]
      }
    },
    "PERCENT": {
      "title": "Percent",
      "description": "Reduce the number of points to this percentage.",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/number",
      "keywords": [
        "percentage"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- input `percentage`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage"
        },
        {
          "title": "Implementation Profile: Point cloud thinning (simple) -- input `percentage`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/percentage"
        }
      ],
      "minOccurs": 0,
      "schema": {
        "type": "number",
        "default": 50,
        "format": "float",
        "minimum": 0,
        "maximum": 100,
        "nullable": true
      }
    },
    "NUMBER": {
      "title": "Number of Points",
      "description": "Number of Points",
      "minOccurs": 0,
      "schema": {
        "type": "integer",
        "default": 0,
        "nullable": true
      }
    }
  },
  "outputs": {
    "RESULT": {
      "title": "Thinned Points",
      "description": "Thinned Points",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud",
      "keywords": [
        "point cloud"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result"
        },
        {
          "title": "Implementation Profile: Point cloud thinning (simple) -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/outputs/result"
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-lasf"
          }
        ]
      }
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/pointcloud/point-cloud-thinning/context.jsonld",
  "id": "SAGA.pointcloud_tools.9",
  "title": "Point Cloud Thinning (Simple)",
  "description": "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order. ",
  "version": "1.0.0",
  "jobControlOptions": [
    "sync-execute",
    "async-execute",
    "dismiss"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ],
  "mutable": false,
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9/execution"
    }
  ],
  "keywords": [
    "point cloud",
    "thinning"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    },
    {
      "title": "Generic Profile: Point cloud thinning",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning"
    },
    {
      "title": "Implementation Profile: Point cloud thinning (simple)",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning"
    }
  ],
  "inputs": {
    "INPUT": {
      "title": "Points",
      "description": "Points",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud",
      "keywords": [
        "point cloud"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points"
        },
        {
          "title": "Implementation Profile: Point cloud thinning (simple) -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/points"
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-lasf"
          }
        ]
      }
    },
    "PERCENT": {
      "title": "Percent",
      "description": "Reduce the number of points to this percentage.",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/number",
      "keywords": [
        "percentage"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- input `percentage`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage"
        },
        {
          "title": "Implementation Profile: Point cloud thinning (simple) -- input `percentage`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/percentage"
        }
      ],
      "minOccurs": 0,
      "schema": {
        "type": "number",
        "default": 50,
        "format": "float",
        "minimum": 0,
        "maximum": 100,
        "nullable": true
      }
    },
    "NUMBER": {
      "title": "Number of Points",
      "description": "Number of Points",
      "minOccurs": 0,
      "schema": {
        "type": "integer",
        "default": 0,
        "nullable": true
      }
    }
  },
  "outputs": {
    "RESULT": {
      "title": "Thinned Points",
      "description": "Thinned Points",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud",
      "keywords": [
        "point cloud"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result"
        },
        {
          "title": "Implementation Profile: Point cloud thinning (simple) -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/outputs/result"
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-lasf"
          }
        ]
      }
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <http://www.iana.org/assignments/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/SAGA.pointcloud_tools.9> dcterms:description "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order. " ;
    dcterms:subject "point cloud",
        "thinning" ;
    dcterms:title "Point Cloud Thinning (Simple)" ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns3:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns4:INPUT [ dcterms:description "Points" ;
                    dcterms:title "Points" ;
                    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud> ;
                    proc:keywords "point cloud" ;
                    proc:metadata [ dcterms:title "Generic Profile: Point cloud thinning -- input `points`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ],
                        [ dcterms:title "Implementation Profile: Point cloud thinning (simple) -- input `points`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/points> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ] ;
                    proc:schema [ ns2:oneOf [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "application/x-ogc-lasf" ] ] ] ;
            ns4:NUMBER [ dcterms:description "Number of Points" ;
                    dcterms:title "Number of Points" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "0"^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "integer" ] ] ;
            ns4:PERCENT [ dcterms:description "Reduce the number of points to this percentage." ;
                    dcterms:title "Percent" ;
                    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/number> ;
                    proc:keywords "percentage" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Point cloud thinning (simple) -- input `percentage`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/percentage> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ],
                        [ dcterms:title "Generic Profile: Point cloud thinning -- input `percentage`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "50"^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "number" ;
                            ns2:format "float" ;
                            ns2:maximum 100 ;
                            ns2:minimum 0 ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud thinning" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "Implementation Profile: Point cloud thinning (simple)" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Process Concept: Point Cloud Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns1:RESULT [ dcterms:description "Thinned Points" ;
                    dcterms:title "Thinned Points" ;
                    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud> ;
                    proc:keywords "point cloud" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Point cloud thinning (simple) -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output> ],
                        [ dcterms:title "Generic Profile: Point cloud thinning -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
                    proc:schema [ ns2:oneOf [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "application/x-ogc-lasf" ] ] ] ] .


```


### process-type entry
Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision, linking to its Implementation Profile.
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-thinning, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning"
    }
  ],
  "prefLabel": "Point Cloud Thinning (Simple)",
  "definition": "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-thinning",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.pointcloud.point-cloud-thinning",
    "processDescription": {
      "id": "SAGA.pointcloud_tools.9",
      "version": "1.0.0",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning",
  "correspondences": {
    "openeoEquivalence": {
      "level": "none",
      "rationale": "No openEO process handles point clouds in the published bblocks-openeo register."
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/pointcloud/point-cloud-thinning/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-thinning, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning"
    }
  ],
  "prefLabel": "Point Cloud Thinning (Simple)",
  "definition": "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-thinning",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.pointcloud.point-cloud-thinning",
    "processDescription": {
      "id": "SAGA.pointcloud_tools.9",
      "version": "1.0.0",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning",
  "correspondences": {
    "openeoEquivalence": {
      "level": "none",
      "rationale": "No openEO process handles point clouds in the published bblocks-openeo register."
    }
  }
}
```

#### ttl
```ttl
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-22T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning> ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/d5-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/specialisation-2026-11-10> a rim:RegisterAction ;
    dcterms:description "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-thinning, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process/SAGA.pointcloud_tools.9> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9> ;
    pp:version "1.0.0" .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning> a owl:Class,
        pp:ProcessType,
        acttype:ActivityType ;
    rdfs:subClassOf <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-thinning> ;
    skos:definition "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Point Cloud Thinning (Simple)" ;
    pp:deployment [ pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/SAGA.pointcloud_tools.9> ;
            pp:profile "ospd.process-profiles.pointcloud.point-cloud-thinning" ;
            pp:provenanceClass wfprov:ProcessRun ] ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "none" ;
            pp:rationale "No openEO process handles point clouds in the published bblocks-openeo register." ] ;
    pp:phase <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing> ;
    acttype:generatedEntityType geo:Feature ;
    acttype:usedEntityType geo:Feature ;
    rim:hasAction <https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/addition>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/d5-2026-11-09>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning/actions/specialisation-2026-11-10> ;
    rim:inRegister pp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-process-profiles/def/process-type/pointcloud/point-cloud-thinning"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Profile of the live OGC API - Processes processDescription of `SAGA.pointcloud_tools.9`.
  Pins the process id and the input/output names. No execute/results/provenance $defs
  or examples: static processDescription only (no CWLProv-style run record exists
  for a live deployed service).'
allOf:
- $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/process/schema.yaml
- $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/part2/v1/schemas/staticIndicator/schema.yaml
- type: object
  required:
  - id
  - inputs
  - outputs
  properties:
    id:
      const: SAGA.pointcloud_tools.9
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - INPUT
      - PERCENT
      - NUMBER
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - RESULT
      x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
$defs:
  processTypeEntry:
    $ref: https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.yaml
  inheritedProcessDescription:
    allOf:
    - $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/process/schema.yaml
    - $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/part2/v1/schemas/staticIndicator/schema.yaml
    - type: object
      required:
      - id
      - inputs
      - outputs
      properties:
        id:
          const: SAGA.pointcloud_tools.9
          x-jsonld-id: '@id'
        inputs:
          type: object
          required:
          - INPUT
          - PERCENT
          - NUMBER
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - RESULT
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
    - description: '`SAGA.pointcloud_tools.9` as the Implementation (instance level)
        of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning`:
        Table 21 keywords (E) and footnote-a metadata references (Table 22 roles)
        inherited from its Implementation Profile.'
      type: object
      required:
      - keywords
      - metadata
      properties:
        keywords:
          allOf:
          - contains:
              const: point cloud
          - contains:
              const: thinning
          x-jsonld-id: http://purl.org/dc/terms/subject
        metadata:
          allOf:
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/concept
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        inputs:
          type: object
          required:
          - INPUT
          - PERCENT
          properties:
            INPUT:
              required:
              - dataType
              - keywords
              - metadata
              properties:
                dataType:
                  const: https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: point cloud
                  x-jsonld-id: http://purl.org/dc/terms/subject
                metadata:
                  allOf:
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/points
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
            PERCENT:
              required:
              - dataType
              - keywords
              - metadata
              properties:
                dataType:
                  const: https://geolabs.github.io/bblocks-data-types/def/data-type/number
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: percentage
                  x-jsonld-id: http://purl.org/dc/terms/subject
                metadata:
                  allOf:
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/percentage
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
                minOccurs:
                  type: integer
                  minimum: 0
                  maximum: 1
                  x-jsonld-id: https://w3id.org/ogc/api/processes/minOccurs
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - RESULT
          properties:
            RESULT:
              required:
              - dataType
              - keywords
              - metadata
              properties:
                dataType:
                  const: https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: point cloud
                  x-jsonld-id: http://purl.org/dc/terms/subject
                metadata:
                  allOf:
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/outputs/result
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
x-jsonld-extra-terms:
  type: '@type'
  ProcessRun: http://purl.org/wf4ever/wfprov#ProcessRun
  WorkflowRun: http://purl.org/wf4ever/wfprov#WorkflowRun
  WorkflowEngine: http://purl.org/wf4ever/wfprov#WorkflowEngine
  Artifact: http://purl.org/wf4ever/wfprov#Artifact
  ProcessType: https://geolabs.github.io/bblocks-process-profiles/def/ProcessType
  ActivityType: https://w3id.org/ogc/rim/activity-type/ActivityType
  owlClass: http://www.w3.org/2002/07/owl#Class
  subClassOf:
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#subClassOf
    x-jsonld-type: '@id'
  title: http://purl.org/dc/terms/title
  description: http://purl.org/dc/terms/description
  keywords: http://purl.org/dc/terms/subject
  version: https://geolabs.github.io/bblocks-process-profiles/def/version
  mutable: https://w3id.org/ogc/api/processes/mutable
  jobControlOptions: https://w3id.org/ogc/api/processes/jobControlOptions
  minOccurs: https://w3id.org/ogc/api/processes/minOccurs
  maxOccurs: https://w3id.org/ogc/api/processes/maxOccurs
  outputTransmission: https://w3id.org/ogc/api/processes/outputTransmission
  metadata:
    x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    x-jsonld-context:
      href:
        '@id': https://w3id.org/ogc/api/processes/href
        '@type': '@id'
  role:
    x-jsonld-id: https://w3id.org/ogc/api/processes/role
    x-jsonld-type: '@id'
  dataType:
    x-jsonld-id: http://purl.org/dc/terms/type
    x-jsonld-type: '@id'
  usedEntityType:
    x-jsonld-id: https://w3id.org/ogc/rim/activity-type/usedEntityType
    x-jsonld-type: '@id'
  generatedEntityType:
    x-jsonld-id: https://w3id.org/ogc/rim/activity-type/generatedEntityType
    x-jsonld-type: '@id'
  changeClassification:
    x-jsonld-id: https://w3id.org/ogc/rim/changeClassification
    x-jsonld-type: '@vocab'
  substantive: https://w3id.org/ogc/rim/substantiveChange
  clarifying: https://w3id.org/ogc/rim/clarifyingChange
  links:
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    x-jsonld-context:
      href:
        '@id': http://www.w3.org/ns/oa#hasTarget
        '@type': '@id'
      rel:
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
        '@context':
          '@base': http://www.iana.org/assignments/relation/
      type: http://purl.org/dc/terms/type
      title: http://www.w3.org/2000/01/rdf-schema#label
  response: https://w3id.org/ogc/api/processes/response
  executionUnit:
    x-jsonld-id: https://w3id.org/ogc/api/processes/executionUnit
    x-jsonld-context:
      href:
        '@id': http://www.w3.org/ns/oa#hasTarget
        '@type': '@id'
      rel:
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
        '@context':
          '@base': http://www.iana.org/assignments/relation/
      type: http://purl.org/dc/terms/format
  processDescription:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/processDescription
    x-jsonld-context:
      href:
        '@id': http://www.w3.org/2000/01/rdf-schema#seeAlso
        '@type': '@id'
      license:
        '@id': http://purl.org/dc/terms/license
        '@type': '@id'
  result: https://geolabs.github.io/bblocks-process-profiles/def/result
  engine: https://geolabs.github.io/bblocks-process-profiles/def/engine
  run: https://geolabs.github.io/bblocks-process-profiles/def/run
  provType:
    x-jsonld-id: '@type'
    x-jsonld-type: '@vocab'
  provName: http://www.w3.org/2000/01/rdf-schema#label
  activityType:
    x-jsonld-id: '@type'
    x-jsonld-type: '@id'
  entityType:
    x-jsonld-id: '@type'
    x-jsonld-type: '@id'
  used:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
  wasAssociatedWith:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  wasGeneratedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
    x-jsonld-type: '@id'
  wasDerivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
  wasAttributedTo:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
    x-jsonld-type: '@id'
  qualifiedAssociation: http://www.w3.org/ns/prov#qualifiedAssociation
  agent:
    x-jsonld-id: http://www.w3.org/ns/prov#agent
    x-jsonld-type: '@id'
  hadPlan:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
    x-jsonld-type: '@id'
  specializationOf:
    x-jsonld-id: http://www.w3.org/ns/prov#specializationOf
    x-jsonld-type: '@id'
  startedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  endedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  value: http://www.w3.org/1999/02/22-rdf-syntax-ns#value
  describedByProcess:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#describedByProcess
    x-jsonld-type: '@id'
  describedByWorkflow:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#describedByWorkflow
    x-jsonld-type: '@id'
  usedInput:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#usedInput
    x-jsonld-type: '@id'
  wasEnactedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  wasPartOfWorkflowRun:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#wasPartOfWorkflowRun
    x-jsonld-type: '@id'
  hadSubProcessRun:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#hadSubProcessRun
    x-jsonld-type: '@id'
  wasOutputFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#generated
    x-jsonld-type: '@id'
  objectIdentifier:
    x-jsonld-id: https://w3id.org/ogc/rim/objectIdentifier
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  itemClass:
    x-jsonld-id: https://w3id.org/ogc/rim/itemClass
    x-jsonld-type: '@id'
  inRegister:
    x-jsonld-id: https://w3id.org/ogc/rim/inRegister
    x-jsonld-type: '@id'
  validityStatus:
    x-jsonld-id: https://w3id.org/ogc/rim/validityStatus
    x-jsonld-type: '@vocab'
  publicationStatus:
    x-jsonld-id: https://w3id.org/ogc/rim/publicationStatus
    x-jsonld-type: '@vocab'
  invalid: https://w3id.org/ogc/rim/invalid
  published: https://w3id.org/ogc/rim/published
  hasAction:
    x-jsonld-id: https://w3id.org/ogc/rim/hasAction
    x-jsonld-type: '@id'
  RegisterAction: https://w3id.org/ogc/rim/RegisterAction
  actionType:
    x-jsonld-id: https://w3id.org/ogc/rim/actionType
    x-jsonld-type: '@vocab'
  addition: https://w3id.org/ogc/rim/additionAction
  proposer:
    x-jsonld-id: https://w3id.org/ogc/rim/proposer
    x-jsonld-type: '@id'
  appliesTo:
    x-jsonld-id: https://w3id.org/ogc/rim/appliesTo
    x-jsonld-type: '@id'
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://geolabs.github.io/bblocks-process-profiles/def/status
  classification: '@nest'
  correspondences: '@nest'
  phase:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/phase
    x-jsonld-type: '@id'
  deployment: https://geolabs.github.io/bblocks-process-profiles/def/deployment
  profile: https://geolabs.github.io/bblocks-process-profiles/def/profile
  plan:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/plan
    x-jsonld-context:
      license:
        '@id': http://purl.org/dc/terms/license
        '@type': '@id'
  Plan: http://www.w3.org/ns/prov#Plan
  cwlClass: https://geolabs.github.io/bblocks-process-profiles/def/cwlClass
  cwlId: https://geolabs.github.io/bblocks-process-profiles/def/cwlId
  provenanceClass:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/provenanceClass
    x-jsonld-type: '@id'
  implementsProfile:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/implementsProfile
    x-jsonld-type: '@id'
  cctDependencies: https://geolabs.github.io/bblocks-process-profiles/def/cctDependency
  candidateCctDependencies: https://geolabs.github.io/bblocks-process-profiles/def/candidateCctDependency
  hasStep:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/hasStep
    x-jsonld-type: '@id'
  exactMatch:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
    x-jsonld-type: '@id'
  closeMatch:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#closeMatch
    x-jsonld-type: '@id'
  relatedMatch:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#relatedMatch
    x-jsonld-type: '@id'
  openeoEquivalence: https://geolabs.github.io/bblocks-process-profiles/def/openeoEquivalence
  level: https://geolabs.github.io/bblocks-process-profiles/def/equivalenceLevel
  rationale: https://geolabs.github.io/bblocks-process-profiles/def/rationale
  decomposition:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/decomposition
    x-jsonld-container: '@list'
  stage: https://geolabs.github.io/bblocks-process-profiles/def/stage
  openeo: https://geolabs.github.io/bblocks-process-profiles/def/openeo
  note: http://www.w3.org/2004/02/skos/core#note
  serverSideFiles:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/serverSideFile
    x-jsonld-context:
      name: https://geolabs.github.io/bblocks-process-profiles/def/liveName
      side: https://geolabs.github.io/bblocks-process-profiles/def/side
      implements:
        '@id': https://geolabs.github.io/bblocks-process-profiles/def/implements
        '@type': '@id'
      location: https://geolabs.github.io/bblocks-process-profiles/def/location
  roleDecompositions:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/roleDecomposition
    x-jsonld-context:
      side: https://geolabs.github.io/bblocks-process-profiles/def/side
      implements:
        '@id': https://geolabs.github.io/bblocks-process-profiles/def/implements
        '@type': '@id'
      parts:
        '@id': https://geolabs.github.io/bblocks-process-profiles/def/part
        '@container': '@list'
      selectors:
        '@id': https://geolabs.github.io/bblocks-process-profiles/def/selector
        '@context':
          name: https://geolabs.github.io/bblocks-process-profiles/def/liveName
          values: http://www.w3.org/1999/02/22-rdf-syntax-ns#value
      reproducible:
        '@id': https://geolabs.github.io/bblocks-process-profiles/def/reproducible
        '@type': http://www.w3.org/2001/XMLSchema#boolean
      note: http://www.w3.org/2004/02/skos/core#note
  unboundRoles:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/unboundRole
    x-jsonld-context:
      side: https://geolabs.github.io/bblocks-process-profiles/def/side
      implements:
        '@id': https://geolabs.github.io/bblocks-process-profiles/def/implements
        '@type': '@id'
      reason: http://www.w3.org/2004/02/skos/core#note
  fixedRoleValues:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/fixedRoleValue
    x-jsonld-context:
      side: https://geolabs.github.io/bblocks-process-profiles/def/side
      implements:
        '@id': https://geolabs.github.io/bblocks-process-profiles/def/implements
        '@type': '@id'
      values: http://www.w3.org/1999/02/22-rdf-syntax-ns#value
      reason: http://www.w3.org/2004/02/skos/core#note
  byReference:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/byReference
    x-jsonld-context:
      name: https://geolabs.github.io/bblocks-process-profiles/def/liveName
      side: https://geolabs.github.io/bblocks-process-profiles/def/side
      implements:
        '@id': https://geolabs.github.io/bblocks-process-profiles/def/implements
        '@type': '@id'
      note: http://www.w3.org/2004/02/skos/core#note
  notAttached:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/notAttached
    x-jsonld-context:
      reason: http://www.w3.org/2004/02/skos/core#note
  assumedFormatGaps:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/assumedFormatGap
    x-jsonld-context:
      name: https://geolabs.github.io/bblocks-process-profiles/def/liveName
      side: https://geolabs.github.io/bblocks-process-profiles/def/side
      implements:
        '@id': https://geolabs.github.io/bblocks-process-profiles/def/implements
        '@type': '@id'
      served: https://geolabs.github.io/bblocks-process-profiles/def/servedMediaType
      reason: http://www.w3.org/2004/02/skos/core#note
      evidence: https://geolabs.github.io/bblocks-process-profiles/def/evidence
x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/
x-jsonld-prefixes:
  wfprov: http://purl.org/wf4ever/wfprov#
  pp: https://geolabs.github.io/bblocks-process-profiles/def/
  acttype: https://w3id.org/ogc/rim/activity-type/
  owl: http://www.w3.org/2002/07/owl#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  proc: https://w3id.org/ogc/api/processes/
  rim: https://w3id.org/ogc/rim/
  oa: http://www.w3.org/ns/oa#
  prov: http://www.w3.org/ns/prov#
  xsd: http://www.w3.org/2001/XMLSchema#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  skos: http://www.w3.org/2004/02/skos/core#
x-bblocks-metadata:
  itemIdentifier: ospd.process-profiles.pointcloud.point-cloud-thinning
  register: https://geolabs.github.io/bblocks-process-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/pointcloud/point-cloud-thinning/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/pointcloud/point-cloud-thinning/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://geolabs.github.io/bblocks-process-profiles/def/",
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-process-profiles/def/input/",
        "schema": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/schema/"
          },
          "@id": "proc:schema"
        },
        "keywords": "proc:keywords",
        "type": "proc:type"
      },
      "@id": "proc:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-process-profiles/def/output/",
        "schema": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/schema/"
          },
          "@id": "proc:schema"
        },
        "keywords": "proc:keywords",
        "type": "proc:type"
      },
      "@id": "proc:outputs"
    },
    "id": "@id",
    "type": "@type",
    "ProcessRun": "wfprov:ProcessRun",
    "WorkflowRun": "wfprov:WorkflowRun",
    "WorkflowEngine": "wfprov:WorkflowEngine",
    "Artifact": "wfprov:Artifact",
    "ProcessType": "pp:ProcessType",
    "ActivityType": "acttype:ActivityType",
    "owlClass": "owl:Class",
    "subClassOf": {
      "@id": "rdfs:subClassOf",
      "@type": "@id"
    },
    "title": "dct:title",
    "description": "dct:description",
    "keywords": "dct:subject",
    "version": "pp:version",
    "mutable": "proc:mutable",
    "jobControlOptions": "proc:jobControlOptions",
    "minOccurs": "proc:minOccurs",
    "maxOccurs": "proc:maxOccurs",
    "outputTransmission": "proc:outputTransmission",
    "metadata": {
      "@id": "proc:metadata",
      "@context": {
        "href": {
          "@id": "proc:href",
          "@type": "@id"
        }
      }
    },
    "role": {
      "@id": "proc:role",
      "@type": "@id"
    },
    "dataType": {
      "@id": "dct:type",
      "@type": "@id"
    },
    "usedEntityType": {
      "@id": "acttype:usedEntityType",
      "@type": "@id"
    },
    "generatedEntityType": {
      "@id": "acttype:generatedEntityType",
      "@type": "@id"
    },
    "changeClassification": {
      "@id": "rim:changeClassification",
      "@type": "@vocab"
    },
    "substantive": "rim:substantiveChange",
    "clarifying": "rim:clarifyingChange",
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": {
          "@id": "oa:hasTarget",
          "@type": "@id"
        },
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "title": "rdfs:label"
      }
    },
    "response": "proc:response",
    "executionUnit": {
      "@id": "proc:executionUnit",
      "@context": {
        "href": {
          "@id": "oa:hasTarget",
          "@type": "@id"
        },
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:format"
      }
    },
    "processDescription": {
      "@id": "pp:processDescription",
      "@context": {
        "href": {
          "@id": "rdfs:seeAlso",
          "@type": "@id"
        },
        "license": {
          "@id": "dct:license",
          "@type": "@id"
        }
      }
    },
    "result": "pp:result",
    "engine": "pp:engine",
    "run": "pp:run",
    "provType": {
      "@id": "@type",
      "@type": "@vocab"
    },
    "provName": "rdfs:label",
    "activityType": {
      "@id": "@type",
      "@type": "@id"
    },
    "entityType": {
      "@id": "@type",
      "@type": "@id"
    },
    "used": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "qualifiedAssociation": "prov:qualifiedAssociation",
    "agent": {
      "@id": "prov:agent",
      "@type": "@id"
    },
    "hadPlan": {
      "@id": "prov:hadPlan",
      "@type": "@id"
    },
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "rdf:value",
    "describedByProcess": {
      "@id": "wfprov:describedByProcess",
      "@type": "@id"
    },
    "describedByWorkflow": {
      "@id": "wfprov:describedByWorkflow",
      "@type": "@id"
    },
    "usedInput": {
      "@id": "wfprov:usedInput",
      "@type": "@id"
    },
    "wasEnactedBy": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasPartOfWorkflowRun": {
      "@id": "wfprov:wasPartOfWorkflowRun",
      "@type": "@id"
    },
    "hadSubProcessRun": {
      "@id": "wfprov:hadSubProcessRun",
      "@type": "@id"
    },
    "wasOutputFrom": {
      "@id": "prov:generated",
      "@type": "@id"
    },
    "objectIdentifier": {
      "@id": "rim:objectIdentifier",
      "@type": "xsd:anyURI"
    },
    "itemClass": {
      "@id": "rim:itemClass",
      "@type": "@id"
    },
    "inRegister": {
      "@id": "rim:inRegister",
      "@type": "@id"
    },
    "validityStatus": {
      "@id": "rim:validityStatus",
      "@type": "@vocab"
    },
    "publicationStatus": {
      "@id": "rim:publicationStatus",
      "@type": "@vocab"
    },
    "invalid": "rim:invalid",
    "published": "rim:published",
    "hasAction": {
      "@id": "rim:hasAction",
      "@type": "@id"
    },
    "RegisterAction": "rim:RegisterAction",
    "actionType": {
      "@id": "rim:actionType",
      "@type": "@vocab"
    },
    "addition": "rim:additionAction",
    "proposer": {
      "@id": "rim:proposer",
      "@type": "@id"
    },
    "appliesTo": {
      "@id": "rim:appliesTo",
      "@type": "@id"
    },
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "status": "pp:status",
    "classification": "@nest",
    "correspondences": "@nest",
    "phase": {
      "@id": "pp:phase",
      "@type": "@id"
    },
    "deployment": "pp:deployment",
    "profile": "pp:profile",
    "plan": {
      "@id": "pp:plan",
      "@context": {
        "license": {
          "@id": "dct:license",
          "@type": "@id"
        }
      }
    },
    "Plan": "prov:Plan",
    "cwlClass": "pp:cwlClass",
    "cwlId": "pp:cwlId",
    "provenanceClass": {
      "@id": "pp:provenanceClass",
      "@type": "@id"
    },
    "implementsProfile": {
      "@id": "pp:implementsProfile",
      "@type": "@id"
    },
    "cctDependencies": "pp:cctDependency",
    "candidateCctDependencies": "pp:candidateCctDependency",
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
    "openeoEquivalence": "pp:openeoEquivalence",
    "level": "pp:equivalenceLevel",
    "rationale": "pp:rationale",
    "decomposition": {
      "@id": "pp:decomposition",
      "@container": "@list"
    },
    "stage": "pp:stage",
    "openeo": "pp:openeo",
    "note": "skos:note",
    "serverSideFiles": {
      "@id": "pp:serverSideFile",
      "@context": {
        "name": "pp:liveName",
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "location": "pp:location"
      }
    },
    "roleDecompositions": {
      "@id": "pp:roleDecomposition",
      "@context": {
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "parts": {
          "@id": "pp:part",
          "@container": "@list"
        },
        "selectors": {
          "@id": "pp:selector",
          "@context": {
            "name": "pp:liveName",
            "values": "rdf:value"
          }
        },
        "reproducible": {
          "@id": "pp:reproducible",
          "@type": "xsd:boolean"
        }
      }
    },
    "unboundRoles": {
      "@id": "pp:unboundRole",
      "@context": {
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "reason": "skos:note"
      }
    },
    "fixedRoleValues": {
      "@id": "pp:fixedRoleValue",
      "@context": {
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "values": "rdf:value",
        "reason": "skos:note"
      }
    },
    "byReference": {
      "@id": "pp:byReference",
      "@context": {
        "name": "pp:liveName",
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        }
      }
    },
    "notAttached": {
      "@id": "pp:notAttached",
      "@context": {
        "reason": "skos:note"
      }
    },
    "assumedFormatGaps": {
      "@id": "pp:assumedFormatGap",
      "@context": {
        "name": "pp:liveName",
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "served": "pp:servedMediaType",
        "reason": "skos:note",
        "evidence": "pp:evidence"
      }
    },
    "nullable": "proc:nullable",
    "$ref": {
      "@id": "proc:ref",
      "@type": "@id"
    },
    "default": {
      "@id": "proc:default",
      "@type": "@json"
    },
    "enum": {
      "@id": "proc:enum",
      "@container": "@set"
    },
    "dct": "http://purl.org/dc/terms/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "wfprov": "http://purl.org/wf4ever/wfprov#",
    "pp": "https://geolabs.github.io/bblocks-process-profiles/def/",
    "acttype": "rim:activity-type/",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rim": "https://w3id.org/ogc/rim/",
    "oa": "http://www.w3.org/ns/oa#",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/pointcloud/point-cloud-thinning/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/pointcloud/point-cloud-thinning`

