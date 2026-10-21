
# Process profile: OTB.RadiometricIndices (Schema)

`ospd.process-profiles.raster.radiometric-index` *v0.1*

Process profile of the live OGC API - Processes process `OTB.RadiometricIndices` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of the live OGC API - Processes process `OTB.RadiometricIndices` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices>.

> This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.

(the process's own description, as served)

## The tool behind it

[OTB RadiometricIndices](https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html) -- Orfeo ToolBox 10.0.0 CookBook (the deployed OTB version is not exposed by the service).

> **Compute radiometric indices.**
>
> This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.

Quoted from the OTB CookBook, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).

On this deployment:

- The CookBook's `-list` parameter (the indices to compute, default `ndvi`) is not exposed by the live service, hence the Implementation Profile's `index` stays unbound.
- The live `channels` input is titled "Blue channel index": the CookBook's `-channels.blue`.

## Implementation Profile

Implements [`Radiometric index`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index) (`generic-profiles.implementation-profile.radiometric-index`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `in` | input `rasters` |
| -- | input `index` (unbound: no input of the live service selects the index: OTB RadiometricIndices' `list` parameter is not exposed) |
| `out`, `channels`, `channels.green`, `channels.red`, `channels.nir`, `channels.mir`, `ram` | -- (live-only inputs, Table 21 footnote b) |
| `out` | output `raster` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.

## Examples

### Source (referenced)
The processDescription is fetched from the live service, not copied: <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices>.

### processDescription
Live OGC API - Processes processDescription, normalised (ZOO-Project-internal fields dropped).
#### json
```json
{
  "id": "OTB.RadiometricIndices",
  "title": "Compute radiometric indices.",
  "description": "This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.",
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
    "in": {
      "title": "Input image",
      "description": "Input image",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/jpeg"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "out": {
      "title": "Radiometric indices output image",
      "description": "Radiometric indices output image",
      "schema": {
        "type": "string",
        "default": "float",
        "enum": [
          "uint8",
          "uint16",
          "int16",
          "int32",
          "int32",
          "float",
          "double"
        ]
      }
    },
    "channels": {
      "title": "Blue channel index",
      "description": "Blue channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.green": {
      "title": "Green channel index",
      "description": "Green channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.red": {
      "title": "Red channel index",
      "description": "Red channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.nir": {
      "title": "NIR channel index",
      "description": "NIR channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.mir": {
      "title": "Mir channel index",
      "description": "Mir channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "ram": {
      "title": "Available memory for processing (in MB).",
      "description": "Available memory for processing (in MB).",
      "minOccurs": 0,
      "schema": {
        "type": "integer",
        "default": 256,
        "nullable": true
      }
    }
  },
  "outputs": {
    "out": {
      "title": "Radiometric indices output image",
      "description": "Radiometric indices output image",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/jpeg"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices/execution"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/radiometric-index/context.jsonld",
  "id": "OTB.RadiometricIndices",
  "title": "Compute radiometric indices.",
  "description": "This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.",
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
    "in": {
      "title": "Input image",
      "description": "Input image",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/jpeg"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "out": {
      "title": "Radiometric indices output image",
      "description": "Radiometric indices output image",
      "schema": {
        "type": "string",
        "default": "float",
        "enum": [
          "uint8",
          "uint16",
          "int16",
          "int32",
          "int32",
          "float",
          "double"
        ]
      }
    },
    "channels": {
      "title": "Blue channel index",
      "description": "Blue channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.green": {
      "title": "Green channel index",
      "description": "Green channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.red": {
      "title": "Red channel index",
      "description": "Red channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.nir": {
      "title": "NIR channel index",
      "description": "NIR channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.mir": {
      "title": "Mir channel index",
      "description": "Mir channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "ram": {
      "title": "Available memory for processing (in MB).",
      "description": "Available memory for processing (in MB).",
      "minOccurs": 0,
      "schema": {
        "type": "integer",
        "default": 256,
        "nullable": true
      }
    }
  },
  "outputs": {
    "out": {
      "title": "Radiometric indices output image",
      "description": "Radiometric indices output image",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/jpeg"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices/execution"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.RadiometricIndices> dcterms:description "This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices." ;
    dcterms:title "Compute radiometric indices." ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns4:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns3:channels [ dcterms:description "Blue channel index" ;
                    dcterms:title "Blue channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns3:channels.green [ dcterms:description "Green channel index" ;
                    dcterms:title "Green channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns3:channels.mir [ dcterms:description "Mir channel index" ;
                    dcterms:title "Mir channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns3:channels.nir [ dcterms:description "NIR channel index" ;
                    dcterms:title "NIR channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns3:channels.red [ dcterms:description "Red channel index" ;
                    dcterms:title "Red channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns3:in [ dcterms:description "Input image" ;
                    dcterms:title "Input image" ;
                    proc:schema [ ns2:oneOf [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/jpeg" ] ] ] ;
            ns3:out [ dcterms:description "Radiometric indices output image" ;
                    dcterms:title "Radiometric indices output image" ;
                    proc:schema [ proc:default "\"float\""^^rdf:JSON ;
                            proc:enum "double",
                                "float",
                                "int16",
                                "int32",
                                "uint16",
                                "uint8" ;
                            proc:type "string" ] ] ;
            ns3:ram [ dcterms:description "Available memory for processing (in MB)." ;
                    dcterms:title "Available memory for processing (in MB)." ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "256"^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "integer" ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns1:out [ dcterms:description "Radiometric indices output image" ;
                    dcterms:title "Radiometric indices output image" ;
                    proc:schema [ ns2:oneOf [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/jpeg" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/png" ] ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Which live input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the live service's own additions (footnote b). `index` is not bound: no input of the live service selects the index: OTB RadiometricIndices' `list` parameter is not exposed. Not what the live service serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
#### json
```json
{
  "id": "OTB.RadiometricIndices",
  "title": "Compute radiometric indices.",
  "description": "This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.",
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices/execution"
    }
  ],
  "keywords": [
    "raster",
    "coverage",
    "radiometric index",
    "OTB",
    "RadiometricIndices"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Radiometric index",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index"
    },
    {
      "title": "Implementation Profile: Radiometric index",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index"
    }
  ],
  "inputs": {
    "in": {
      "title": "Input image",
      "description": "Input image",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Radiometric index -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/rasters"
        },
        {
          "title": "Implementation Profile: Radiometric index -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/rasters"
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/jpeg"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "out": {
      "title": "Radiometric indices output image",
      "description": "Radiometric indices output image",
      "schema": {
        "type": "string",
        "default": "float",
        "enum": [
          "uint8",
          "uint16",
          "int16",
          "int32",
          "int32",
          "float",
          "double"
        ]
      }
    },
    "channels": {
      "title": "Blue channel index",
      "description": "Blue channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.green": {
      "title": "Green channel index",
      "description": "Green channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.red": {
      "title": "Red channel index",
      "description": "Red channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.nir": {
      "title": "NIR channel index",
      "description": "NIR channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.mir": {
      "title": "Mir channel index",
      "description": "Mir channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "ram": {
      "title": "Available memory for processing (in MB).",
      "description": "Available memory for processing (in MB).",
      "minOccurs": 0,
      "schema": {
        "type": "integer",
        "default": 256,
        "nullable": true
      }
    }
  },
  "outputs": {
    "out": {
      "title": "Radiometric indices output image",
      "description": "Radiometric indices output image",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Radiometric index -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/outputs/raster"
        },
        {
          "title": "Implementation Profile: Radiometric index -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/outputs/raster"
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/jpeg"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/radiometric-index/context.jsonld",
  "id": "OTB.RadiometricIndices",
  "title": "Compute radiometric indices.",
  "description": "This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.",
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices/execution"
    }
  ],
  "keywords": [
    "raster",
    "coverage",
    "radiometric index",
    "OTB",
    "RadiometricIndices"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Radiometric index",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index"
    },
    {
      "title": "Implementation Profile: Radiometric index",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index"
    }
  ],
  "inputs": {
    "in": {
      "title": "Input image",
      "description": "Input image",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Radiometric index -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/rasters"
        },
        {
          "title": "Implementation Profile: Radiometric index -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/rasters"
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/jpeg"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "out": {
      "title": "Radiometric indices output image",
      "description": "Radiometric indices output image",
      "schema": {
        "type": "string",
        "default": "float",
        "enum": [
          "uint8",
          "uint16",
          "int16",
          "int32",
          "int32",
          "float",
          "double"
        ]
      }
    },
    "channels": {
      "title": "Blue channel index",
      "description": "Blue channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.green": {
      "title": "Green channel index",
      "description": "Green channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.red": {
      "title": "Red channel index",
      "description": "Red channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.nir": {
      "title": "NIR channel index",
      "description": "NIR channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "channels.mir": {
      "title": "Mir channel index",
      "description": "Mir channel index",
      "schema": {
        "type": "integer",
        "default": 1
      }
    },
    "ram": {
      "title": "Available memory for processing (in MB).",
      "description": "Available memory for processing (in MB).",
      "minOccurs": 0,
      "schema": {
        "type": "integer",
        "default": 256,
        "nullable": true
      }
    }
  },
  "outputs": {
    "out": {
      "title": "Radiometric indices output image",
      "description": "Radiometric indices output image",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Radiometric index -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/outputs/raster"
        },
        {
          "title": "Implementation Profile: Radiometric index -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/outputs/raster"
        }
      ],
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/jpeg"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
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
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <http://www.iana.org/assignments/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.RadiometricIndices> dcterms:description "This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices." ;
    dcterms:subject "OTB",
        "RadiometricIndices",
        "coverage",
        "radiometric index",
        "raster" ;
    dcterms:title "Compute radiometric indices." ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns3:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns1:channels [ dcterms:description "Blue channel index" ;
                    dcterms:title "Blue channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns1:channels.green [ dcterms:description "Green channel index" ;
                    dcterms:title "Green channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns1:channels.mir [ dcterms:description "Mir channel index" ;
                    dcterms:title "Mir channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns1:channels.nir [ dcterms:description "NIR channel index" ;
                    dcterms:title "NIR channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns1:channels.red [ dcterms:description "Red channel index" ;
                    dcterms:title "Red channel index" ;
                    proc:schema [ proc:default "1"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns1:in [ dcterms:description "Input image" ;
                    dcterms:title "Input image" ;
                    proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Radiometric index -- input `rasters`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/rasters> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ],
                        [ dcterms:title "Generic Profile: Radiometric index -- input `rasters`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/rasters> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
                    proc:schema [ ns2:oneOf [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/jpeg" ] ] ] ;
            ns1:out [ dcterms:description "Radiometric indices output image" ;
                    dcterms:title "Radiometric indices output image" ;
                    proc:schema [ proc:default "\"float\""^^rdf:JSON ;
                            proc:enum "double",
                                "float",
                                "int16",
                                "int32",
                                "uint16",
                                "uint8" ;
                            proc:type "string" ] ] ;
            ns1:ram [ dcterms:description "Available memory for processing (in MB)." ;
                    dcterms:title "Available memory for processing (in MB)." ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "256"^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "integer" ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Implementation Profile: Radiometric index" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Generic Profile: Radiometric index" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns4:out [ dcterms:description "Radiometric indices output image" ;
                    dcterms:title "Radiometric indices output image" ;
                    proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:metadata [ dcterms:title "Generic Profile: Radiometric index -- output `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/outputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ],
                        [ dcterms:title "Implementation Profile: Radiometric index -- output `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/outputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output> ] ;
                    proc:schema [ ns2:oneOf [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/jpeg" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "image/png" ] ] ] ] .


```


### process-type entry
Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/radiometric-index` (`ospd.process-profiles.process-type`), status `submitted`, linking to its Implementation Profile.
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/radiometric-index",
  "type": "ProcessType",
  "prefLabel": "Compute radiometric indices.",
  "definition": "This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.raster.radiometric-index",
  "processDescription": {
    "id": "OTB.RadiometricIndices",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index",
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.ndvi"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "OTB.RadiometricIndices computes a *selectable set* of named indices (NDVI, NDWI, and many others via `channels` / `list`) from user-mapped spectral channels (`channels.red`, `channels.nir`, ...), only one of which (NDVI) has a dedicated openEO process (`ndvi`, which also expects band-role mapping via `nir`/`red` parameters). closeMatch, not exactMatch: openEO has no equivalent for the other indices this application can compute."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/radiometric-index/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/radiometric-index",
  "type": "ProcessType",
  "prefLabel": "Compute radiometric indices.",
  "definition": "This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.raster.radiometric-index",
  "processDescription": {
    "id": "OTB.RadiometricIndices",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index",
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.ndvi"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "OTB.RadiometricIndices computes a *selectable set* of named indices (NDVI, NDWI, and many others via `channels` / `list`) from user-mapped spectral channels (`channels.red`, `channels.nir`, ...), only one of which (NDVI) has a dedicated openEO process (`ndvi`, which also expects band-role mapping via `nir`/`red` parameters). closeMatch, not exactMatch: openEO has no equivalent for the other indices this application can compute."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/radiometric-index> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.ndvi> ;
    skos:definition "This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Compute radiometric indices." ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "OTB.RadiometricIndices computes a *selectable set* of named indices (NDVI, NDWI, and many others via `channels` / `list`) from user-mapped spectral channels (`channels.red`, `channels.nir`, ...), only one of which (NDVI) has a dedicated openEO process (`ndvi`, which also expects band-role mapping via `nir`/`red` parameters). closeMatch, not exactMatch: openEO has no equivalent for the other indices this application can compute." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.RadiometricIndices> ;
    pp:profile "ospd.process-profiles.raster.radiometric-index" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.RadiometricIndices> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices> ;
    pp:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Profile of the live OGC API - Processes processDescription of `OTB.RadiometricIndices`.
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
      const: OTB.RadiometricIndices
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - in
      - out
      - channels
      - channels.green
      - channels.red
      - channels.nir
      - channels.mir
      - ram
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - out
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
          const: OTB.RadiometricIndices
          x-jsonld-id: '@id'
        inputs:
          type: object
          required:
          - in
          - out
          - channels
          - channels.green
          - channels.red
          - channels.nir
          - channels.mir
          - ram
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - out
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
    - description: '`OTB.RadiometricIndices` as the Implementation (instance level)
        of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index`:
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
              const: raster
          - contains:
              const: coverage
          - contains:
              const: radiometric index
          - contains:
              const: OTB
          - contains:
              const: RadiometricIndices
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
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        inputs:
          type: object
          required:
          - in
          properties:
            in:
              required:
              - keywords
              - metadata
              properties:
                keywords:
                  allOf:
                  - contains:
                      const: raster
                  - contains:
                      const: GeoTIFF
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/rasters
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/rasters
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - out
          properties:
            out:
              required:
              - keywords
              - metadata
              properties:
                keywords:
                  allOf:
                  - contains:
                      const: raster
                  - contains:
                      const: GeoTIFF
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/outputs/raster
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/outputs/raster
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
x-bblocks-metadata:
  itemIdentifier: ospd.process-profiles.raster.radiometric-index
  register: https://geolabs.github.io/bblocks-process-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-21'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/radiometric-index/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/radiometric-index/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/radiometric-index/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/raster/radiometric-index`

