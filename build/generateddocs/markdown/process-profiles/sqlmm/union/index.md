
# Process profile: Union (Schema)

`ospd.process-profiles.sqlmm.union` *v0.1*

Process profile of the live OGC API - Processes process `Union` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of the live OGC API - Processes process `Union` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union>.

> This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2.

(the process's own description, as served)

## Implementation Profile

Implements [`Union`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union) (`generic-profiles.implementation-profile.union`, bblocks-generic-profiles).

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `InputEntity1` | input `geometry1` | `geometry` |
| `InputEntity2` | input `geometry2` | `geometry` |
| `Result` | output `result` | `geometry` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles, and the data type of each bound input/output.
- `process-type.json`: its candidate process-type entry.

## Examples

### Source (referenced)
The processDescription is fetched from the live service, not copied: <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union>.

### processDescription
Live OGC API - Processes processDescription, normalised (ZOO-Project-internal fields dropped).
#### json
```json
{
  "id": "Union",
  "title": "Compute union. ",
  "description": "This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2.",
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
      "title": "The union of two geometries",
      "description": "The geometry representing the union of the two geometries.",
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union/execution"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/union/context.jsonld",
  "id": "Union",
  "title": "Compute union. ",
  "description": "This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2.",
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
      "title": "The union of two geometries",
      "description": "The geometry representing the union of the two geometries.",
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union/execution"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/Union> dcterms:description "This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2." ;
    dcterms:title "Compute union. " ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns4:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union/execution> ] ;
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
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "UTF-8" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ] ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "Demo" ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:Result [ dcterms:description "The geometry representing the union of the two geometries." ;
                    dcterms:title "The union of two geometries" ;
                    proc:metadata [ dcterms:title "Mon test  " ] ;
                    proc:schema [ ns1:oneOf [ proc:type "object" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "UTF-8" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ] ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Each bound input/output also carries the `dataType` of that counterpart, a concept of bblocks-data-types. Which deployed input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the deployment's own additions (footnote b). Not what the deployment serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
#### json
```json
{
  "id": "Union",
  "title": "Compute union. ",
  "description": "This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2.",
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
      "title": "Implementation Profile: Union",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union"
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union/execution"
    }
  ],
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "set operation",
    "Union"
  ],
  "inputs": {
    "InputEntity1": {
      "title": "the first geometry",
      "description": "the first geometry to compare against.",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry1"
        },
        {
          "title": "Implementation Profile: Union -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/inputs/geometry1"
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
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry2"
        },
        {
          "title": "Implementation Profile: Union -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/inputs/geometry2"
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
      "title": "The union of two geometries",
      "description": "The geometry representing the union of the two geometries.",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/outputs/result"
        },
        {
          "title": "Implementation Profile: Union -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/outputs/result"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/union/context.jsonld",
  "id": "Union",
  "title": "Compute union. ",
  "description": "This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2.",
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
      "title": "Implementation Profile: Union",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union"
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union/execution"
    }
  ],
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "set operation",
    "Union"
  ],
  "inputs": {
    "InputEntity1": {
      "title": "the first geometry",
      "description": "the first geometry to compare against.",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry1"
        },
        {
          "title": "Implementation Profile: Union -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/inputs/geometry1"
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
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry2"
        },
        {
          "title": "Implementation Profile: Union -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/inputs/geometry2"
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
      "title": "The union of two geometries",
      "description": "The geometry representing the union of the two geometries.",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial set operation -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/outputs/result"
        },
        {
          "title": "Implementation Profile: Union -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/outputs/result"
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
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/Union> dcterms:description "This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2." ;
    dcterms:subject "Union",
        "geometry",
        "set operation",
        "spatial analysis",
        "vector" ;
    dcterms:title "Compute union. " ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns4:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union/execution> ] ;
    pp:version "2.0.0" ;
    proc:inputs [ ns2:InputEntity1 [ dcterms:description "the first geometry to compare against." ;
                    dcterms:title "the first geometry" ;
                    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/geometry> ;
                    proc:keywords "geometry" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Union -- input `geometry1`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/inputs/geometry1> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ],
                        [ dcterms:title "Mon test  " ],
                        [ dcterms:title "Generic Profile: Binary spatial set operation -- input `geometry1`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry1> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
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
                    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/geometry> ;
                    proc:keywords "geometry" ;
                    proc:metadata [ dcterms:title "Generic Profile: Binary spatial set operation -- input `geometry2`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/inputs/geometry2> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ],
                        [ dcterms:title "Mon test  " ],
                        [ dcterms:title "Implementation Profile: Union -- input `geometry2`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/inputs/geometry2> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ] ;
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
    proc:metadata [ dcterms:title "Demo" ],
        [ dcterms:title "Generic Profile: Binary spatial set operation" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "Implementation Profile: Union" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Process Concept: Vector Geometry Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:Result [ dcterms:description "The geometry representing the union of the two geometries." ;
                    dcterms:title "The union of two geometries" ;
                    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/geometry> ;
                    proc:keywords "geometry" ;
                    proc:metadata [ dcterms:title "Mon test  " ],
                        [ dcterms:title "Generic Profile: Binary spatial set operation -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ],
                        [ dcterms:title "Implementation Profile: Union -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output> ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "UTF-8" ;
                                    ns1:contentMediaType "text/xml" ;
                                    ns1:contentSchema "http://fooa/gml/3.1.0/polygon.xsd" ],
                                [ proc:type "object" ] ] ] ] .


```


### process-type entry
Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision, linking to its Implementation Profile.
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/union, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Geometry, http://www.opengis.net/ont/geosparql#Geometry.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union"
    }
  ],
  "prefLabel": "Compute union.",
  "definition": "This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/union",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Geometry",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Geometry",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.sqlmm.union",
    "processDescription": {
      "id": "Union",
      "version": "2.0.0",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union",
  "correspondences": {
    "openeoEquivalence": {
      "level": "none",
      "rationale": "No openEO process for this SQL/MM set operation in the published bblocks-openeo register."
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/union/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/union, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Geometry, http://www.opengis.net/ont/geosparql#Geometry.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union"
    }
  ],
  "prefLabel": "Compute union.",
  "definition": "This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/union",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Geometry",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Geometry",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.sqlmm.union",
    "processDescription": {
      "id": "Union",
      "version": "2.0.0",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union",
  "correspondences": {
    "openeoEquivalence": {
      "level": "none",
      "rationale": "No openEO process for this SQL/MM set operation in the published bblocks-openeo register."
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

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-22T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union> ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/d5-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/specialisation-2026-11-10> a rim:RegisterAction ;
    dcterms:description "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/union, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Geometry, http://www.opengis.net/ont/geosparql#Geometry." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process/Union> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Union> ;
    pp:version "2.0.0" .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union> a owl:Class,
        pp:ProcessType,
        acttype:ActivityType ;
    rdfs:subClassOf <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/union> ;
    skos:definition "This service shall return a bag of geometry values representing a Point set union of geometry InputEntity1 with geometry InputEntity2." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Compute union." ;
    pp:deployment [ pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/Union> ;
            pp:profile "ospd.process-profiles.sqlmm.union" ;
            pp:provenanceClass wfprov:ProcessRun ] ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "none" ;
            pp:rationale "No openEO process for this SQL/MM set operation in the published bblocks-openeo register." ] ;
    pp:phase <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> ;
    acttype:generatedEntityType geo:Geometry ;
    acttype:usedEntityType geo:Geometry ;
    rim:hasAction <https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/addition>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/d5-2026-11-09>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union/actions/specialisation-2026-11-10> ;
    rim:inRegister pp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-process-profiles/def/process-type/sqlmm/union"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Profile of the live OGC API - Processes processDescription of `Union`.
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
      const: Union
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
    - $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/process/schema.yaml
    - $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/part2/v1/schemas/staticIndicator/schema.yaml
    - type: object
      required:
      - id
      - inputs
      - outputs
      properties:
        id:
          const: Union
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
    - description: '`Union` as the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union`:
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
              const: Union
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
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        inputs:
          type: object
          required:
          - InputEntity1
          - InputEntity2
          properties:
            InputEntity1:
              required:
              - dataType
              - keywords
              - metadata
              properties:
                dataType:
                  const: https://geolabs.github.io/bblocks-data-types/def/data-type/geometry
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: geometry
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/inputs/geometry1
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
            InputEntity2:
              required:
              - dataType
              - keywords
              - metadata
              properties:
                dataType:
                  const: https://geolabs.github.io/bblocks-data-types/def/data-type/geometry
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: geometry
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/inputs/geometry2
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
              - dataType
              - keywords
              - metadata
              properties:
                dataType:
                  const: https://geolabs.github.io/bblocks-data-types/def/data-type/geometry
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: geometry
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/union/outputs/result
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
  itemIdentifier: ospd.process-profiles.sqlmm.union
  register: https://geolabs.github.io/bblocks-process-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/union/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/union/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/sqlmm/union/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/sqlmm/union`

