
# Process profile: OTB.BandMathX (Schema)

`ospd.process-profiles.raster.band-math-multiband` *v0.1*

Process profile of the live OGC API - Processes process `OTB.BandMathX` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of the live OGC API - Processes process `OTB.BandMathX` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX>.

> This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image: * ``im1`` a pixel from 1st input, made of n components (n bands) * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based) * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input. * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input. * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics) * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics) * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics) * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics) * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics) * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators: * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division * ``^`` raise x to the power of y * ``

(the process's own description, as served)

## The tool behind it

[OTB BandMathX](https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html) -- Orfeo ToolBox 10.0.0 CookBook (the deployed OTB version is not exposed by the service).

> **This application performs mathematical operations on several multiband images.**
>
> This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.

Quoted from the OTB CookBook, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).

On this deployment:

- `il` is served with `maxOccurs: 1024`, ZOO-Project's encoding of an unbounded list.

## Implementation Profile

Implements [`Raster band math (multi-band output)`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband) (`generic-profiles.implementation-profile.raster-band-math-multiband`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `il` | input `rasters` |
| `exp` | input `expression` |
| `out`, `incontext`, `ram` | -- (live-only inputs, Table 21 footnote b) |
| `out` | output `raster` |
| `outcontext` | -- (live-only outputs, Table 21 footnote b) |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.

## Examples

### Source (referenced)
The processDescription is fetched from the live service, not copied: <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX>.

### processDescription
Live OGC API - Processes processDescription, normalised (ZOO-Project-internal fields dropped).
#### json
```json
{
  "id": "OTB.BandMathX",
  "title": "This application performs mathematical operations on several multiband images.",
  "description": "This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image:  * ``im1`` a pixel from 1st input, made of n components (n bands)  * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based)  * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input  * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input.  * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input.  * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics)  * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics)  * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics)  * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics)  * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics)  * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators:  * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division  * ``^`` raise x to the power of y  * ``",
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
    "il": {
      "title": "Image list to perform computation on.",
      "description": "Image list to perform computation on.",
      "maxOccurs": 1024,
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
      "title": "Output image.",
      "description": "Output image.",
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
    "exp": {
      "title": "Mathematical expression to apply.",
      "description": "Mathematical expression to apply.",
      "schema": {
        "type": "string"
      }
    },
    "incontext": {
      "title": "A txt file containing user's constants and expressions.",
      "description": "A txt file containing user's constants and expressions.",
      "minOccurs": 0,
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
      "title": "Output image.",
      "description": "Output image.",
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
    "outcontext": {
      "title": "A txt file where to save user's constants and expressions.",
      "description": "A txt file where to save user's constants and expressions.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "utf-8",
            "contentMediaType": "text/xml"
          },
          {
            "type": "string",
            "contentEncoding": "utf-8",
            "contentMediaType": "text/plain"
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX/execution"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/band-math-multiband/context.jsonld",
  "id": "OTB.BandMathX",
  "title": "This application performs mathematical operations on several multiband images.",
  "description": "This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image:  * ``im1`` a pixel from 1st input, made of n components (n bands)  * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based)  * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input  * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input.  * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input.  * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics)  * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics)  * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics)  * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics)  * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics)  * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators:  * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division  * ``^`` raise x to the power of y  * ``",
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
    "il": {
      "title": "Image list to perform computation on.",
      "description": "Image list to perform computation on.",
      "maxOccurs": 1024,
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
      "title": "Output image.",
      "description": "Output image.",
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
    "exp": {
      "title": "Mathematical expression to apply.",
      "description": "Mathematical expression to apply.",
      "schema": {
        "type": "string"
      }
    },
    "incontext": {
      "title": "A txt file containing user's constants and expressions.",
      "description": "A txt file containing user's constants and expressions.",
      "minOccurs": 0,
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
      "title": "Output image.",
      "description": "Output image.",
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
    "outcontext": {
      "title": "A txt file where to save user's constants and expressions.",
      "description": "A txt file where to save user's constants and expressions.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "utf-8",
            "contentMediaType": "text/xml"
          },
          {
            "type": "string",
            "contentEncoding": "utf-8",
            "contentMediaType": "text/plain"
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX/execution"
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
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.BandMathX> dcterms:description "This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image:  * ``im1`` a pixel from 1st input, made of n components (n bands)  * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based)  * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input  * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input.  * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input.  * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics)  * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics)  * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics)  * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics)  * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics)  * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators:  * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division  * ``^`` raise x to the power of y  * ``" ;
    dcterms:title "This application performs mathematical operations on several multiband images." ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns3:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns2:exp [ dcterms:description "Mathematical expression to apply." ;
                    dcterms:title "Mathematical expression to apply." ;
                    proc:schema [ proc:type "string" ] ] ;
            ns2:il [ dcterms:description "Image list to perform computation on." ;
                    dcterms:title "Image list to perform computation on." ;
                    proc:maxOccurs 1024 ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/jpeg" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns2:incontext [ dcterms:description "A txt file containing user's constants and expressions." ;
                    dcterms:title "A txt file containing user's constants and expressions." ;
                    proc:minOccurs 0 ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/jpeg" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns2:out [ dcterms:description "Output image." ;
                    dcterms:title "Output image." ;
                    proc:schema [ proc:default "\"float\""^^rdf:JSON ;
                            proc:enum "double",
                                "float",
                                "int16",
                                "int32",
                                "uint16",
                                "uint8" ;
                            proc:type "string" ] ] ;
            ns2:ram [ dcterms:description "Available memory for processing (in MB)." ;
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
    proc:outputs [ ns4:out [ dcterms:description "Output image." ;
                    dcterms:title "Output image." ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/jpeg" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns4:outcontext [ dcterms:description "A txt file where to save user's constants and expressions." ;
                    dcterms:title "A txt file where to save user's constants and expressions." ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "utf-8" ;
                                    ns1:contentMediaType "text/plain" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "utf-8" ;
                                    ns1:contentMediaType "text/xml" ] ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Which live input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the live service's own additions (footnote b). Not what the live service serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
#### json
```json
{
  "id": "OTB.BandMathX",
  "title": "This application performs mathematical operations on several multiband images.",
  "description": "This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image:  * ``im1`` a pixel from 1st input, made of n components (n bands)  * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based)  * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input  * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input.  * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input.  * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics)  * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics)  * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics)  * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics)  * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics)  * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators:  * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division  * ``^`` raise x to the power of y  * ``",
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX/execution"
    }
  ],
  "keywords": [
    "raster",
    "coverage",
    "band math",
    "OTB",
    "BandMathX",
    "multi-band"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster band math",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math"
    },
    {
      "title": "Implementation Profile: Raster band math (multi-band output)",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    }
  ],
  "inputs": {
    "il": {
      "title": "Image list to perform computation on.",
      "description": "Image list to perform computation on.",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters"
        },
        {
          "title": "Implementation Profile: Raster band math (multi-band output) -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters"
        }
      ],
      "maxOccurs": 1024,
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
      "title": "Output image.",
      "description": "Output image.",
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
    "exp": {
      "title": "Mathematical expression to apply.",
      "description": "Mathematical expression to apply.",
      "keywords": [
        "expression"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- input `expression`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression"
        },
        {
          "title": "Implementation Profile: Raster band math (multi-band output) -- input `expression`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression"
        }
      ],
      "schema": {
        "type": "string"
      }
    },
    "incontext": {
      "title": "A txt file containing user's constants and expressions.",
      "description": "A txt file containing user's constants and expressions.",
      "minOccurs": 0,
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
      "title": "Output image.",
      "description": "Output image.",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster"
        },
        {
          "title": "Implementation Profile: Raster band math (multi-band output) -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster"
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
    "outcontext": {
      "title": "A txt file where to save user's constants and expressions.",
      "description": "A txt file where to save user's constants and expressions.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "utf-8",
            "contentMediaType": "text/xml"
          },
          {
            "type": "string",
            "contentEncoding": "utf-8",
            "contentMediaType": "text/plain"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/band-math-multiband/context.jsonld",
  "id": "OTB.BandMathX",
  "title": "This application performs mathematical operations on several multiband images.",
  "description": "This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image:  * ``im1`` a pixel from 1st input, made of n components (n bands)  * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based)  * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input  * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input.  * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input.  * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics)  * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics)  * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics)  * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics)  * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics)  * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators:  * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division  * ``^`` raise x to the power of y  * ``",
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX/execution"
    }
  ],
  "keywords": [
    "raster",
    "coverage",
    "band math",
    "OTB",
    "BandMathX",
    "multi-band"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster band math",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math"
    },
    {
      "title": "Implementation Profile: Raster band math (multi-band output)",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    }
  ],
  "inputs": {
    "il": {
      "title": "Image list to perform computation on.",
      "description": "Image list to perform computation on.",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters"
        },
        {
          "title": "Implementation Profile: Raster band math (multi-band output) -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters"
        }
      ],
      "maxOccurs": 1024,
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
      "title": "Output image.",
      "description": "Output image.",
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
    "exp": {
      "title": "Mathematical expression to apply.",
      "description": "Mathematical expression to apply.",
      "keywords": [
        "expression"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- input `expression`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression"
        },
        {
          "title": "Implementation Profile: Raster band math (multi-band output) -- input `expression`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression"
        }
      ],
      "schema": {
        "type": "string"
      }
    },
    "incontext": {
      "title": "A txt file containing user's constants and expressions.",
      "description": "A txt file containing user's constants and expressions.",
      "minOccurs": 0,
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
      "title": "Output image.",
      "description": "Output image.",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster"
        },
        {
          "title": "Implementation Profile: Raster band math (multi-band output) -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster"
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
    "outcontext": {
      "title": "A txt file where to save user's constants and expressions.",
      "description": "A txt file where to save user's constants and expressions.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "utf-8",
            "contentMediaType": "text/xml"
          },
          {
            "type": "string",
            "contentEncoding": "utf-8",
            "contentMediaType": "text/plain"
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
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.BandMathX> dcterms:description "This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image:  * ``im1`` a pixel from 1st input, made of n components (n bands)  * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based)  * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input  * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input.  * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input.  * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics)  * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics)  * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics)  * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics)  * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics)  * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators:  * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division  * ``^`` raise x to the power of y  * ``" ;
    dcterms:subject "BandMathX",
        "OTB",
        "band math",
        "coverage",
        "multi-band",
        "raster" ;
    dcterms:title "This application performs mathematical operations on several multiband images." ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns4:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns2:exp [ dcterms:description "Mathematical expression to apply." ;
                    dcterms:title "Mathematical expression to apply." ;
                    proc:keywords "expression" ;
                    proc:metadata [ dcterms:title "Generic Profile: Raster band math -- input `expression`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ],
                        [ dcterms:title "Implementation Profile: Raster band math (multi-band output) -- input `expression`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ] ;
                    proc:schema [ proc:type "string" ] ] ;
            ns2:il [ dcterms:description "Image list to perform computation on." ;
                    dcterms:title "Image list to perform computation on." ;
                    proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:maxOccurs 1024 ;
                    proc:metadata [ dcterms:title "Generic Profile: Raster band math -- input `rasters`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ],
                        [ dcterms:title "Implementation Profile: Raster band math (multi-band output) -- input `rasters`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/jpeg" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns2:incontext [ dcterms:description "A txt file containing user's constants and expressions." ;
                    dcterms:title "A txt file containing user's constants and expressions." ;
                    proc:minOccurs 0 ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/jpeg" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns2:out [ dcterms:description "Output image." ;
                    dcterms:title "Output image." ;
                    proc:schema [ proc:default "\"float\""^^rdf:JSON ;
                            proc:enum "double",
                                "float",
                                "int16",
                                "int32",
                                "uint16",
                                "uint8" ;
                            proc:type "string" ] ] ;
            ns2:ram [ dcterms:description "Available memory for processing (in MB)." ;
                    dcterms:title "Available memory for processing (in MB)." ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "256"^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "integer" ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "Implementation Profile: Raster band math (multi-band output)" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Generic Profile: Raster band math" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:out [ dcterms:description "Output image." ;
                    dcterms:title "Output image." ;
                    proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:metadata [ dcterms:title "Generic Profile: Raster band math -- output `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ],
                        [ dcterms:title "Implementation Profile: Raster band math (multi-band output) -- output `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output> ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/jpeg" ] ] ] ;
            ns3:outcontext [ dcterms:description "A txt file where to save user's constants and expressions." ;
                    dcterms:title "A txt file where to save user's constants and expressions." ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "utf-8" ;
                                    ns1:contentMediaType "text/xml" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "utf-8" ;
                                    ns1:contentMediaType "text/plain" ] ] ] ] .


```


### process-type entry
Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/band-math-multiband` (`ospd.process-profiles.process-type`), status `submitted`, linking to its Implementation Profile.
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/band-math-multiband",
  "type": "ProcessType",
  "prefLabel": "This application performs mathematical operations on several multiband images.",
  "definition": "This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image: * ``im1`` a pixel from 1st input, made of n components (n bands) * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based) * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input. * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input. * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics) * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics) * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics) * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics) * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics) * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators: * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division * ``^`` raise x to the power of y * ``",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.raster.band-math-multiband",
  "processDescription": {
    "id": "OTB.BandMathX",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "No openEO process combines several image bands via an arbitrary muParserX-style vector expression with multi-band output in the published bblocks-openeo register (array_apply is closest but applies a unary process per band, not a joint expression)."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/band-math-multiband/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/band-math-multiband",
  "type": "ProcessType",
  "prefLabel": "This application performs mathematical operations on several multiband images.",
  "definition": "This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image: * ``im1`` a pixel from 1st input, made of n components (n bands) * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based) * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input. * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input. * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics) * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics) * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics) * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics) * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics) * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators: * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division * ``^`` raise x to the power of y * ``",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.raster.band-math-multiband",
  "processDescription": {
    "id": "OTB.BandMathX",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "No openEO process combines several image bands via an arbitrary muParserX-style vector expression with multi-band output in the published bblocks-openeo register (array_apply is closest but applies a unary process per band, not a joint expression)."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/band-math-multiband> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> ;
    skos:definition "This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image: * ``im1`` a pixel from 1st input, made of n components (n bands) * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based) * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input. * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input. * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics) * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics) * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics) * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics) * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics) * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators: * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division * ``^`` raise x to the power of y * ``" ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "This application performs mathematical operations on several multiband images." ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "none" ;
            pp:rationale "No openEO process combines several image bands via an arbitrary muParserX-style vector expression with multi-band output in the published bblocks-openeo register (array_apply is closest but applies a unary process per band, not a joint expression)." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.BandMathX> ;
    pp:profile "ospd.process-profiles.raster.band-math-multiband" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.BandMathX> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX> ;
    pp:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Profile of the live OGC API - Processes processDescription of `OTB.BandMathX`.
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
      const: OTB.BandMathX
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - il
      - out
      - exp
      - incontext
      - ram
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - out
      - outcontext
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
          const: OTB.BandMathX
          x-jsonld-id: '@id'
        inputs:
          type: object
          required:
          - il
          - out
          - exp
          - incontext
          - ram
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - out
          - outcontext
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
    - description: '`OTB.BandMathX` as the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband`:
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
              const: band math
          - contains:
              const: OTB
          - contains:
              const: BandMathX
          - contains:
              const: multi-band
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
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        inputs:
          type: object
          required:
          - exp
          - il
          properties:
            il:
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
            exp:
              required:
              - keywords
              - metadata
              properties:
                keywords:
                  allOf:
                  - contains:
                      const: expression
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/band-math-multiband/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/band-math-multiband/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/band-math-multiband/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/raster/band-math-multiband`

