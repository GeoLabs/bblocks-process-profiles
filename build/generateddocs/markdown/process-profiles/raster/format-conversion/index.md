
# Process profile: Gdal_Translate (Schema)

`ospd.process-profiles.raster.format-conversion` *v0.1*

Process profile of the live OGC API - Processes process `Gdal_Translate` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of the live OGC API - Processes process `Gdal_Translate` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate>.

> http://www.gdal.org/gdal_translate.html

(the process's own description, as served)

## Implementation Profile

Implements [`Raster format conversion`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion) (`generic-profiles.implementation-profile.raster-format-conversion`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputDSN` | input `raster` |
| `Format` | input `targetFormat` |
| `GCP`, `OutputDSN` | -- (live-only inputs, Table 21 footnote b) |
| `Result` | output `raster` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.

## Examples

### Source (referenced)
The processDescription is fetched from the live service, not copied: <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate>.

### processDescription
Live OGC API - Processes processDescription, normalised (ZOO-Project-internal fields dropped).
#### json
```json
{
  "id": "Gdal_Translate",
  "title": "Convert raster data from one format to another. ",
  "description": "http://www.gdal.org/gdal_translate.html",
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
    "Format": {
      "title": "Format of the output data",
      "description": "Select the output format by usig short name of the format (use gda-config --formats for list of available formats on your platform).",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "GTiff",
        "nullable": true
      }
    },
    "GCP": {
      "title": "Ground Point Control",
      "description": "Ground Point Control in the form : pixel,line,eating,northing(,elev).",
      "minOccurs": 0,
      "maxOccurs": "unbounded",
      "schema": {
        "type": "string",
        "nullable": true
      }
    },
    "InputDSN": {
      "title": "The input data source name",
      "description": "The input data source name to use as source for convertion.",
      "schema": {
        "type": "string"
      }
    },
    "OutputDSN": {
      "title": "The output data source name",
      "description": "The output data source name to use as source for convertion.",
      "schema": {
        "type": "string"
      }
    }
  },
  "outputs": {
    "Result": {
      "title": "The resulting converted file",
      "description": "The file name resulting of the convertion",
      "schema": {
        "type": "string"
      }
    }
  },
  "mutable": false,
  "metadata": [
    {
      "title": "My Demo"
    }
  ],
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate/execution"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/format-conversion/context.jsonld",
  "id": "Gdal_Translate",
  "title": "Convert raster data from one format to another. ",
  "description": "http://www.gdal.org/gdal_translate.html",
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
    "Format": {
      "title": "Format of the output data",
      "description": "Select the output format by usig short name of the format (use gda-config --formats for list of available formats on your platform).",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "GTiff",
        "nullable": true
      }
    },
    "GCP": {
      "title": "Ground Point Control",
      "description": "Ground Point Control in the form : pixel,line,eating,northing(,elev).",
      "minOccurs": 0,
      "maxOccurs": "unbounded",
      "schema": {
        "type": "string",
        "nullable": true
      }
    },
    "InputDSN": {
      "title": "The input data source name",
      "description": "The input data source name to use as source for convertion.",
      "schema": {
        "type": "string"
      }
    },
    "OutputDSN": {
      "title": "The output data source name",
      "description": "The output data source name to use as source for convertion.",
      "schema": {
        "type": "string"
      }
    }
  },
  "outputs": {
    "Result": {
      "title": "The resulting converted file",
      "description": "The file name resulting of the convertion",
      "schema": {
        "type": "string"
      }
    }
  },
  "mutable": false,
  "metadata": [
    {
      "title": "My Demo"
    }
  ],
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate/execution"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns3: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/Gdal_Translate> dcterms:description "http://www.gdal.org/gdal_translate.html" ;
    dcterms:title "Convert raster data from one format to another. " ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns3:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns1:Format [ dcterms:description "Select the output format by usig short name of the format (use gda-config --formats for list of available formats on your platform)." ;
                    dcterms:title "Format of the output data" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"GTiff\""^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "string" ] ] ;
            ns1:GCP [ dcterms:description "Ground Point Control in the form : pixel,line,eating,northing(,elev)." ;
                    dcterms:title "Ground Point Control" ;
                    proc:maxOccurs "unbounded" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:nullable true ;
                            proc:type "string" ] ] ;
            ns1:InputDSN [ dcterms:description "The input data source name to use as source for convertion." ;
                    dcterms:title "The input data source name" ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:OutputDSN [ dcterms:description "The output data source name to use as source for convertion." ;
                    dcterms:title "The output data source name" ;
                    proc:schema [ proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "My Demo" ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns2:Result [ dcterms:description "The file name resulting of the convertion" ;
                    dcterms:title "The resulting converted file" ;
                    proc:schema [ proc:type "string" ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Which live input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the live service's own additions (footnote b). Not what the live service serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
#### json
```json
{
  "id": "Gdal_Translate",
  "title": "Convert raster data from one format to another. ",
  "description": "http://www.gdal.org/gdal_translate.html",
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
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster format conversion",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion"
    },
    {
      "title": "Implementation Profile: Raster format conversion",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion"
    },
    {
      "title": "My Demo"
    }
  ],
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate/execution"
    }
  ],
  "keywords": [
    "raster",
    "coverage",
    "format conversion",
    "GDAL",
    "gdal_translate"
  ],
  "inputs": {
    "Format": {
      "title": "Format of the output data",
      "description": "Select the output format by usig short name of the format (use gda-config --formats for list of available formats on your platform).",
      "keywords": [
        "format"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster format conversion -- input `targetFormat`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/targetFormat"
        },
        {
          "title": "Implementation Profile: Raster format conversion -- input `targetFormat`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/inputs/targetFormat"
        }
      ],
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "GTiff",
        "nullable": true
      }
    },
    "GCP": {
      "title": "Ground Point Control",
      "description": "Ground Point Control in the form : pixel,line,eating,northing(,elev).",
      "minOccurs": 0,
      "maxOccurs": "unbounded",
      "schema": {
        "type": "string",
        "nullable": true
      }
    },
    "InputDSN": {
      "title": "The input data source name",
      "description": "The input data source name to use as source for convertion.",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster format conversion -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/raster"
        },
        {
          "title": "Implementation Profile: Raster format conversion -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/inputs/raster"
        }
      ],
      "schema": {
        "type": "string"
      }
    },
    "OutputDSN": {
      "title": "The output data source name",
      "description": "The output data source name to use as source for convertion.",
      "schema": {
        "type": "string"
      }
    }
  },
  "outputs": {
    "Result": {
      "title": "The resulting converted file",
      "description": "The file name resulting of the convertion",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster format conversion -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/outputs/raster"
        },
        {
          "title": "Implementation Profile: Raster format conversion -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/outputs/raster"
        }
      ],
      "schema": {
        "type": "string"
      }
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/format-conversion/context.jsonld",
  "id": "Gdal_Translate",
  "title": "Convert raster data from one format to another. ",
  "description": "http://www.gdal.org/gdal_translate.html",
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
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster format conversion",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion"
    },
    {
      "title": "Implementation Profile: Raster format conversion",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion"
    },
    {
      "title": "My Demo"
    }
  ],
  "links": [
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "type": "application/json",
      "title": "Execute End Point",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate/execution"
    }
  ],
  "keywords": [
    "raster",
    "coverage",
    "format conversion",
    "GDAL",
    "gdal_translate"
  ],
  "inputs": {
    "Format": {
      "title": "Format of the output data",
      "description": "Select the output format by usig short name of the format (use gda-config --formats for list of available formats on your platform).",
      "keywords": [
        "format"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster format conversion -- input `targetFormat`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/targetFormat"
        },
        {
          "title": "Implementation Profile: Raster format conversion -- input `targetFormat`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/inputs/targetFormat"
        }
      ],
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "GTiff",
        "nullable": true
      }
    },
    "GCP": {
      "title": "Ground Point Control",
      "description": "Ground Point Control in the form : pixel,line,eating,northing(,elev).",
      "minOccurs": 0,
      "maxOccurs": "unbounded",
      "schema": {
        "type": "string",
        "nullable": true
      }
    },
    "InputDSN": {
      "title": "The input data source name",
      "description": "The input data source name to use as source for convertion.",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster format conversion -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/raster"
        },
        {
          "title": "Implementation Profile: Raster format conversion -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/inputs/raster"
        }
      ],
      "schema": {
        "type": "string"
      }
    },
    "OutputDSN": {
      "title": "The output data source name",
      "description": "The output data source name to use as source for convertion.",
      "schema": {
        "type": "string"
      }
    }
  },
  "outputs": {
    "Result": {
      "title": "The resulting converted file",
      "description": "The file name resulting of the convertion",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster format conversion -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/outputs/raster"
        },
        {
          "title": "Implementation Profile: Raster format conversion -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/outputs/raster"
        }
      ],
      "schema": {
        "type": "string"
      }
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/Gdal_Translate> dcterms:description "http://www.gdal.org/gdal_translate.html" ;
    dcterms:subject "GDAL",
        "coverage",
        "format conversion",
        "gdal_translate",
        "raster" ;
    dcterms:title "Convert raster data from one format to another. " ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns2:Format [ dcterms:description "Select the output format by usig short name of the format (use gda-config --formats for list of available formats on your platform)." ;
                    dcterms:title "Format of the output data" ;
                    proc:keywords "format" ;
                    proc:metadata [ dcterms:title "Generic Profile: Raster format conversion -- input `targetFormat`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/targetFormat> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ],
                        [ dcterms:title "Implementation Profile: Raster format conversion -- input `targetFormat`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/inputs/targetFormat> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ] ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"GTiff\""^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "string" ] ] ;
            ns2:GCP [ dcterms:description "Ground Point Control in the form : pixel,line,eating,northing(,elev)." ;
                    dcterms:title "Ground Point Control" ;
                    proc:maxOccurs "unbounded" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:nullable true ;
                            proc:type "string" ] ] ;
            ns2:InputDSN [ dcterms:description "The input data source name to use as source for convertion." ;
                    dcterms:title "The input data source name" ;
                    proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Raster format conversion -- input `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/inputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ],
                        [ dcterms:title "Generic Profile: Raster format conversion -- input `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
                    proc:schema [ proc:type "string" ] ] ;
            ns2:OutputDSN [ dcterms:description "The output data source name to use as source for convertion." ;
                    dcterms:title "The output data source name" ;
                    proc:schema [ proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "Implementation Profile: Raster format conversion" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Generic Profile: Raster format conversion" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "My Demo" ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:Result [ dcterms:description "The file name resulting of the convertion" ;
                    dcterms:title "The resulting converted file" ;
                    proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Raster format conversion -- output `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/outputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output> ],
                        [ dcterms:title "Generic Profile: Raster format conversion -- output `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/outputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
                    proc:schema [ proc:type "string" ] ] ] .


```


### process-type entry
Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/format-conversion` (`ospd.process-profiles.process-type`), status `submitted`, linking to its Implementation Profile.
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/format-conversion",
  "type": "ProcessType",
  "prefLabel": "Convert raster data from one format to another.",
  "definition": "http://www.gdal.org/gdal_translate.html",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.raster.format-conversion",
  "processDescription": {
    "id": "Gdal_Translate",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion",
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.save_result"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "Gdal_Translate re-encodes a raster into another format (`Format`) without changing its content -- the same role save_result's `format` parameter plays when terminating an openEO process graph. Not exactMatch: save_result is a cube-terminal process (no further chaining downstream), while Gdal_Translate is an ordinary mid-pipeline step; `GCP` (ground control point) handling has no openEO equivalent either."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/format-conversion/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/format-conversion",
  "type": "ProcessType",
  "prefLabel": "Convert raster data from one format to another.",
  "definition": "http://www.gdal.org/gdal_translate.html",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.raster.format-conversion",
  "processDescription": {
    "id": "Gdal_Translate",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion",
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.save_result"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "Gdal_Translate re-encodes a raster into another format (`Format`) without changing its content -- the same role save_result's `format` parameter plays when terminating an openEO process graph. Not exactMatch: save_result is a cube-terminal process (no further chaining downstream), while Gdal_Translate is an ordinary mid-pipeline step; `GCP` (ground control point) handling has no openEO equivalent either."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/format-conversion> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.save_result> ;
    skos:definition "http://www.gdal.org/gdal_translate.html" ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Convert raster data from one format to another." ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "Gdal_Translate re-encodes a raster into another format (`Format`) without changing its content -- the same role save_result's `format` parameter plays when terminating an openEO process graph. Not exactMatch: save_result is a cube-terminal process (no further chaining downstream), while Gdal_Translate is an ordinary mid-pipeline step; `GCP` (ground control point) handling has no openEO equivalent either." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/Gdal_Translate> ;
    pp:profile "ospd.process-profiles.raster.format-conversion" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/Gdal_Translate> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate> ;
    pp:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Profile of the live OGC API - Processes processDescription of `Gdal_Translate`.
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
      const: Gdal_Translate
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - Format
      - GCP
      - InputDSN
      - OutputDSN
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
          const: Gdal_Translate
          x-jsonld-id: '@id'
        inputs:
          type: object
          required:
          - Format
          - GCP
          - InputDSN
          - OutputDSN
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - Result
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
    - description: '`Gdal_Translate` as the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion`:
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
              const: format conversion
          - contains:
              const: GDAL
          - contains:
              const: gdal_translate
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
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        inputs:
          type: object
          required:
          - Format
          - InputDSN
          properties:
            Format:
              required:
              - keywords
              - metadata
              properties:
                keywords:
                  allOf:
                  - contains:
                      const: format
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/targetFormat
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/inputs/targetFormat
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
                minOccurs:
                  type: integer
                  minimum: 0
                  maximum: 1
                  x-jsonld-id: https://w3id.org/ogc/api/processes/minOccurs
            InputDSN:
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/raster
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/inputs/raster
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/outputs/raster
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/outputs/raster
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/format-conversion/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/format-conversion/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/format-conversion/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/raster/format-conversion`

