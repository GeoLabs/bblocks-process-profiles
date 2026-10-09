
# Process profile: Intersection (Schema)

`ospd.process-profiles.sqlmm.intersection` *v0.1*

Process profile of the live OGC API - Processes process `Intersection` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of the live OGC API - Processes process `Intersection` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection>.

> This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2.

(the process's own description, as served)

## Implementation Profile

Implements [`Intersection`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection) (`generic-profiles.implementation-profile.intersection`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputEntity1` | input `geometry1` |
| `InputEntity2` | input `geometry2` |
| `Result` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.

## Examples

### Source (referenced)
The processDescription is fetched from the live service, not copied: <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection>.

### processDescription
Live OGC API - Processes processDescription, normalised (ZOO-Project-internal fields dropped).
#### json
```json
{
  "id": "Intersection",
  "title": "Compute intersection. ",
  "description": "This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2.",
  "version": "2.0.0",
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
    "InputEntity1": {
      "title": "the first geometry",
      "description": "the first geometry to compare against.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          }
        ]
      },
      "metadata": [
        {
          "title": "Mon test  "
        }
      ]
    },
    "InputEntity2": {
      "title": "the other geometry",
      "description": "the other geometry to compare against.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          }
        ]
      },
      "metadata": [
        {
          "title": "Mon test  "
        }
      ]
    }
  },
  "outputs": {
    "Result": {
      "title": "Intersection of geometries",
      "description": "A new geometry representing the intersection or NULL if there is no intersection or an error occurs.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "object"
          }
        ]
      },
      "metadata": [
        {
          "title": "Mon test  "
        }
      ]
    }
  },
  "mutable": false,
  "metadata": [
    {
      "title": "Demo"
    }
  ],
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection/execution"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/intersection/context.jsonld",
  "id": "Intersection",
  "title": "Compute intersection. ",
  "description": "This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2.",
  "version": "2.0.0",
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
    "InputEntity1": {
      "title": "the first geometry",
      "description": "the first geometry to compare against.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          }
        ]
      },
      "metadata": [
        {
          "title": "Mon test  "
        }
      ]
    },
    "InputEntity2": {
      "title": "the other geometry",
      "description": "the other geometry to compare against.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          }
        ]
      },
      "metadata": [
        {
          "title": "Mon test  "
        }
      ]
    }
  },
  "outputs": {
    "Result": {
      "title": "Intersection of geometries",
      "description": "A new geometry representing the intersection or NULL if there is no intersection or an error occurs.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "object"
          }
        ]
      },
      "metadata": [
        {
          "title": "Mon test  "
        }
      ]
    }
  },
  "mutable": false,
  "metadata": [
    {
      "title": "Demo"
    }
  ],
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection/execution"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns3: <http://www.iana.org/assignments/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/Intersection> dcterms:description "This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2." ;
    dcterms:title "Compute intersection. " ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns3:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection/execution> ] ;
    pp:version "2.0.0" ;
    proc:inputs [ ns2:InputEntity1 [ dcterms:description "the first geometry to compare against." ;
                    dcterms:title "the first geometry" ;
                    proc:metadata [ dcterms:title "Mon test  " ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "UTF-8" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ] ] ] ;
            ns2:InputEntity2 [ dcterms:description "the other geometry to compare against." ;
                    dcterms:title "the other geometry" ;
                    proc:metadata [ dcterms:title "Mon test  " ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "UTF-8" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ] ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "Demo" ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns4:Result [ dcterms:description "A new geometry representing the intersection or NULL if there is no intersection or an error occurs." ;
                    dcterms:title "Intersection of geometries" ;
                    proc:metadata [ dcterms:title "Mon test  " ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "UTF-8" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ],
                                [ proc:type "object" ] ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Which live input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the live service's own additions (footnote b). Not what the live service serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
#### json
```json
{
  "id": "Intersection",
  "title": "Compute intersection. ",
  "description": "This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2.",
  "version": "2.0.0",
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
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Binary spatial set operation",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation"
    },
    {
      "title": "Implementation Profile: Intersection",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection"
    },
    {
      "title": "Demo"
    }
  ],
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection/execution"
    }
  ],
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "set operation",
    "Intersection",
    "ST_Intersection"
  ],
  "inputs": {
    "InputEntity1": {
      "title": "the first geometry",
      "description": "the first geometry to compare against.",
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry1"
        },
        {
          "title": "Implementation Profile: Intersection -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/inputs/geometry1"
        },
        {
          "title": "Mon test  "
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          }
        ]
      }
    },
    "InputEntity2": {
      "title": "the other geometry",
      "description": "the other geometry to compare against.",
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry2"
        },
        {
          "title": "Implementation Profile: Intersection -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/inputs/geometry2"
        },
        {
          "title": "Mon test  "
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          }
        ]
      }
    }
  },
  "outputs": {
    "Result": {
      "title": "Intersection of geometries",
      "description": "A new geometry representing the intersection or NULL if there is no intersection or an error occurs.",
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/outputs/result"
        },
        {
          "title": "Implementation Profile: Intersection -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/outputs/result"
        },
        {
          "title": "Mon test  "
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "object"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/intersection/context.jsonld",
  "id": "Intersection",
  "title": "Compute intersection. ",
  "description": "This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2.",
  "version": "2.0.0",
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
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Binary spatial set operation",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation"
    },
    {
      "title": "Implementation Profile: Intersection",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection"
    },
    {
      "title": "Demo"
    }
  ],
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection/execution"
    }
  ],
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "set operation",
    "Intersection",
    "ST_Intersection"
  ],
  "inputs": {
    "InputEntity1": {
      "title": "the first geometry",
      "description": "the first geometry to compare against.",
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry1"
        },
        {
          "title": "Implementation Profile: Intersection -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/inputs/geometry1"
        },
        {
          "title": "Mon test  "
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          }
        ]
      }
    },
    "InputEntity2": {
      "title": "the other geometry",
      "description": "the other geometry to compare against.",
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry2"
        },
        {
          "title": "Implementation Profile: Intersection -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/inputs/geometry2"
        },
        {
          "title": "Mon test  "
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          }
        ]
      }
    }
  },
  "outputs": {
    "Result": {
      "title": "Intersection of geometries",
      "description": "A new geometry representing the intersection or NULL if there is no intersection or an error occurs.",
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/outputs/result"
        },
        {
          "title": "Implementation Profile: Intersection -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/outputs/result"
        },
        {
          "title": "Mon test  "
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "UTF-8",
            "contentMediaType": "text/xml",
            "contentSchema": "http://fooa/gml/3.1.0/polygon.xsd"
          },
          {
            "type": "object"
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
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/Intersection> dcterms:description "This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2." ;
    dcterms:subject "Intersection",
        "ST_Intersection",
        "geometry",
        "set operation",
        "spatial analysis",
        "vector" ;
    dcterms:title "Compute intersection. " ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection/execution> ] ;
    pp:version "2.0.0" ;
    proc:inputs [ ns4:InputEntity1 [ dcterms:description "the first geometry to compare against." ;
                    dcterms:title "the first geometry" ;
                    proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Mon test  " ],
                        [ dcterms:title "Generic Profile: Binary spatial set operation -- input `geometry1`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry1> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ],
                        [ dcterms:title "Implementation Profile: Intersection -- input `geometry1`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/inputs/geometry1> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "UTF-8" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ] ] ] ;
            ns4:InputEntity2 [ dcterms:description "the other geometry to compare against." ;
                    dcterms:title "the other geometry" ;
                    proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Intersection -- input `geometry2`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/inputs/geometry2> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ],
                        [ dcterms:title "Mon test  " ],
                        [ dcterms:title "Generic Profile: Binary spatial set operation -- input `geometry2`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry2> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "UTF-8" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ] ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "Implementation Profile: Intersection" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Generic Profile: Binary spatial set operation" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "Process Concept: Vector Geometry Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Demo" ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:Result [ dcterms:description "A new geometry representing the intersection or NULL if there is no intersection or an error occurs." ;
                    dcterms:title "Intersection of geometries" ;
                    proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Mon test  " ],
                        [ dcterms:title "Implementation Profile: Intersection -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output> ],
                        [ dcterms:title "Generic Profile: Binary spatial set operation -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "UTF-8" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ],
                                [ proc:type "object" ] ] ] ] .


```


### process-type entry
Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/intersection` (`ospd.process-profiles.process-type`), status `submitted`, linking to its Implementation Profile.
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/intersection",
  "type": "ProcessType",
  "prefLabel": "Compute intersection.",
  "definition": "This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.sqlmm.intersection",
  "processDescription": {
    "id": "Intersection",
    "version": "2.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "No openEO process for this SQL/MM set operation in the published bblocks-openeo register."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/intersection/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/intersection",
  "type": "ProcessType",
  "prefLabel": "Compute intersection.",
  "definition": "This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.sqlmm.intersection",
  "processDescription": {
    "id": "Intersection",
    "version": "2.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "No openEO process for this SQL/MM set operation in the published bblocks-openeo register."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/intersection> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> ;
    skos:definition "This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Compute intersection." ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "none" ;
            pp:rationale "No openEO process for this SQL/MM set operation in the published bblocks-openeo register." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/Intersection> ;
    pp:profile "ospd.process-profiles.sqlmm.intersection" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/Intersection> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection> ;
    pp:version "2.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Profile of the live OGC API - Processes processDescription of `Intersection`.
  Pins the process id and the input/output names. No execute/results/provenance $defs
  or examples: static processDescription only (no CWLProv-style run record exists
  for a live deployed service).'
allOf:
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/process/schema.yaml
- $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/v2/schemas/staticIndicator/schema.yaml
- type: object
  required:
  - id
  - inputs
  - outputs
  properties:
    id:
      const: Intersection
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - InputEntity1
      - InputEntity2
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - Result
      x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
$defs:
  processTypeEntry:
    $ref: https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.yaml
  inheritedProcessDescription:
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/process/schema.yaml
    - $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/v2/schemas/staticIndicator/schema.yaml
    - type: object
      required:
      - id
      - inputs
      - outputs
      properties:
        id:
          const: Intersection
          x-jsonld-id: '@id'
        inputs:
          type: object
          required:
          - InputEntity1
          - InputEntity2
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - Result
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
    - description: '`Intersection` as the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection`:
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
              const: vector
          - contains:
              const: geometry
          - contains:
              const: spatial analysis
          - contains:
              const: set operation
          - contains:
              const: Intersection
          - contains:
              const: ST_Intersection
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
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        inputs:
          type: object
          required:
          - InputEntity1
          - InputEntity2
          properties:
            InputEntity1:
              required:
              - keywords
              - metadata
              properties:
                keywords:
                  allOf:
                  - contains:
                      const: geometry
                  - contains:
                      const: GML
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry1
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/inputs/geometry1
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
            InputEntity2:
              required:
              - keywords
              - metadata
              properties:
                keywords:
                  allOf:
                  - contains:
                      const: geometry
                  - contains:
                      const: GML
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry2
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/inputs/geometry2
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - Result
          properties:
            Result:
              required:
              - keywords
              - metadata
              properties:
                keywords:
                  allOf:
                  - contains:
                      const: geometry
                  - contains:
                      const: GML
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/outputs/result
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection/outputs/result
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
x-jsonld-extra-terms:
  type: '@type'
  ProcessRun: http://purl.org/wf4ever/wfprov#ProcessRun
  WorkflowRun: http://purl.org/wf4ever/wfprov#WorkflowRun
  WorkflowEngine: http://purl.org/wf4ever/wfprov#WorkflowEngine
  Artifact: http://purl.org/wf4ever/wfprov#Artifact
  ProcessType: http://www.w3.org/2004/02/skos/core#Concept
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
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://geolabs.github.io/bblocks-process-profiles/def/status
  phase:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
    x-jsonld-type: '@id'
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
x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/
x-jsonld-prefixes:
  wfprov: http://purl.org/wf4ever/wfprov#
  skos: http://www.w3.org/2004/02/skos/core#
  dct: http://purl.org/dc/terms/
  pp: https://geolabs.github.io/bblocks-process-profiles/def/
  proc: https://w3id.org/ogc/api/processes/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  oa: http://www.w3.org/ns/oa#
  prov: http://www.w3.org/ns/prov#
  xsd: http://www.w3.org/2001/XMLSchema#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/intersection/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/intersection/schema.yaml)


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
    "ProcessType": "skos:Concept",
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
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "pp": "https://geolabs.github.io/bblocks-process-profiles/def/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/intersection/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/sqlmm/intersection`

