
# Process profile: SAGA.ta_morphometry.0 (Schema)

`ospd.process-profiles.terrain.slope` *v0.1*

Process profile of the live OGC API - Processes process `SAGA.ta_morphometry.0` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of the live OGC API - Processes process `SAGA.ta_morphometry.0` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0>.

> Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.

(the process's own description, as served)

## The tool behind it

[SAGA ta_morphometry 0 (Slope, Aspect, Curvature)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_0.html) -- SAGA 7.3.0 tool library documentation, the version deployed on the testbed (not yet exposed by its processDescription).

Tool 0 of SAGA's Terrain Analysis - Morphometry library (author O. Conrad, 2001; command line `saga_cmd ta_morphometry 0`). It computes the local morphometric parameters of an elevation grid -- slope, aspect and, depending on the chosen method, curvatures (general, profile, plan, tangential, ...) -- from a local fit of the surface; the default method is the 9 parameter 2nd order polynom of Zevenbergen & Thorne (1987).

On this deployment:

- One process, many outputs: only `SLOPE` is bound to the Implementation Profile (`slope`); `ASPECT` and the ten curvature grids are supplementary outputs of the live service (Table 21 footnote b).

## Implementation Profile

Implements [`Slope`](https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope) (`generic-profiles.implementation-profile.slope`, bblocks-generic-profiles).

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `ELEVATION` | input `elevation` | `elevation-model` |
| `METHOD`, `UNIT_SLOPE`, `UNIT_ASPECT` | -- (the deployment's own inputs, Table 21 footnote b) | -- |
| `SLOPE` | output `result` | `raster-single-band` |
| `ASPECT`, `C_GENE`, `C_PROF`, `C_PLAN`, `C_TANG`, `C_LONG`, `C_CROS`, `C_MINI`, `C_MAXI`, `C_TOTA`, `C_ROTO` | -- (the deployment's own outputs, Table 21 footnote b) | -- |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles, and the data type of each bound input/output.
- `process-type.json`: its candidate process-type entry.

## Examples

### Source (referenced)
The processDescription is fetched from the live service, not copied: <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0>.

### processDescription
Live OGC API - Processes processDescription, normalised (ZOO-Project-internal fields dropped).
#### json
```json
{
  "id": "SAGA.ta_morphometry.0",
  "title": "Slope, Aspect, Curvature",
  "description": "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.",
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
    "ELEVATION": {
      "title": "Elevation",
      "description": "Elevation",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "METHOD": {
      "title": "Method",
      "description": "Method",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
        "enum": [
          "maximum slope (Travis et al. 1975)",
          "maximum triangle slope (Tarboton 1997)",
          "least squares fitted plane (Horn 1981",
          " Costa-Cabral & Burgess 1996)",
          "6 parameter 2nd order polynom (Evans 1979)",
          "6 parameter 2nd order polynom (Heerdegen & Beran 1982)",
          "6 parameter 2nd order polynom (Bauer",
          " Rohdenburg",
          " Bork 1985)",
          "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
          "10 parameter 3rd order polynom (Haralick 1983)"
        ],
        "nullable": true
      }
    },
    "UNIT_SLOPE": {
      "title": "Slope Units",
      "description": "Slope Units",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "radians",
        "enum": [
          "radians",
          "degree",
          "percent"
        ],
        "nullable": true
      }
    },
    "UNIT_ASPECT": {
      "title": "Aspect Units",
      "description": "Aspect Units",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "radians",
        "enum": [
          "radians",
          "degree"
        ],
        "nullable": true
      }
    }
  },
  "outputs": {
    "SLOPE": {
      "title": "Slope",
      "description": "Slope",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "ASPECT": {
      "title": "Aspect",
      "description": "Aspect",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_GENE": {
      "title": "General Curvature",
      "description": "General Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_PROF": {
      "title": "Profile Curvature",
      "description": "Profile Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_PLAN": {
      "title": "Plan Curvature",
      "description": "Plan Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_TANG": {
      "title": "Tangential Curvature",
      "description": "Tangential Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_LONG": {
      "title": "Longitudinal Curvature",
      "description": "Zevenbergen & Thorne (1987) refer to this as profile curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_CROS": {
      "title": "Cross-Sectional Curvature",
      "description": "Zevenbergen & Thorne (1987) refer to this as plan curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_MINI": {
      "title": "Minimal Curvature",
      "description": "Minimal Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_MAXI": {
      "title": "Maximal Curvature",
      "description": "Maximal Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_TOTA": {
      "title": "Total Curvature",
      "description": "Total Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_ROTO": {
      "title": "Flow Line Curvature",
      "description": "Flow Line Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0/execution"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/context.jsonld",
  "id": "SAGA.ta_morphometry.0",
  "title": "Slope, Aspect, Curvature",
  "description": "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.",
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
    "ELEVATION": {
      "title": "Elevation",
      "description": "Elevation",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "METHOD": {
      "title": "Method",
      "description": "Method",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
        "enum": [
          "maximum slope (Travis et al. 1975)",
          "maximum triangle slope (Tarboton 1997)",
          "least squares fitted plane (Horn 1981",
          " Costa-Cabral & Burgess 1996)",
          "6 parameter 2nd order polynom (Evans 1979)",
          "6 parameter 2nd order polynom (Heerdegen & Beran 1982)",
          "6 parameter 2nd order polynom (Bauer",
          " Rohdenburg",
          " Bork 1985)",
          "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
          "10 parameter 3rd order polynom (Haralick 1983)"
        ],
        "nullable": true
      }
    },
    "UNIT_SLOPE": {
      "title": "Slope Units",
      "description": "Slope Units",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "radians",
        "enum": [
          "radians",
          "degree",
          "percent"
        ],
        "nullable": true
      }
    },
    "UNIT_ASPECT": {
      "title": "Aspect Units",
      "description": "Aspect Units",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "radians",
        "enum": [
          "radians",
          "degree"
        ],
        "nullable": true
      }
    }
  },
  "outputs": {
    "SLOPE": {
      "title": "Slope",
      "description": "Slope",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "ASPECT": {
      "title": "Aspect",
      "description": "Aspect",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_GENE": {
      "title": "General Curvature",
      "description": "General Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_PROF": {
      "title": "Profile Curvature",
      "description": "Profile Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_PLAN": {
      "title": "Plan Curvature",
      "description": "Plan Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_TANG": {
      "title": "Tangential Curvature",
      "description": "Tangential Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_LONG": {
      "title": "Longitudinal Curvature",
      "description": "Zevenbergen & Thorne (1987) refer to this as profile curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_CROS": {
      "title": "Cross-Sectional Curvature",
      "description": "Zevenbergen & Thorne (1987) refer to this as plan curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_MINI": {
      "title": "Minimal Curvature",
      "description": "Minimal Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_MAXI": {
      "title": "Maximal Curvature",
      "description": "Maximal Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_TOTA": {
      "title": "Total Curvature",
      "description": "Total Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_ROTO": {
      "title": "Flow Line Curvature",
      "description": "Flow Line Curvature",
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0/execution"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://w3id.org/geolabs/ospd/process-profiles/input/> .
@prefix ns3: <https://w3id.org/geolabs/ospd/process-profiles/output/> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://w3id.org/geolabs/ospd/process-profiles/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/geolabs/ospd/process-profiles/process/terrain/SAGA.ta_morphometry.0> dcterms:description "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated." ;
    dcterms:title "Slope, Aspect, Curvature" ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns4:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns2:ELEVATION [ dcterms:description "Elevation" ;
                    dcterms:title "Elevation" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ] ] ] ;
            ns2:METHOD [ dcterms:description "Method" ;
                    dcterms:title "Method" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)\""^^rdf:JSON ;
                            proc:enum " Bork 1985)",
                                " Costa-Cabral & Burgess 1996)",
                                " Rohdenburg",
                                "10 parameter 3rd order polynom (Haralick 1983)",
                                "6 parameter 2nd order polynom (Bauer",
                                "6 parameter 2nd order polynom (Evans 1979)",
                                "6 parameter 2nd order polynom (Heerdegen & Beran 1982)",
                                "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
                                "least squares fitted plane (Horn 1981",
                                "maximum slope (Travis et al. 1975)",
                                "maximum triangle slope (Tarboton 1997)" ;
                            proc:nullable true ;
                            proc:type "string" ] ] ;
            ns2:UNIT_ASPECT [ dcterms:description "Aspect Units" ;
                    dcterms:title "Aspect Units" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"radians\""^^rdf:JSON ;
                            proc:enum "degree",
                                "radians" ;
                            proc:nullable true ;
                            proc:type "string" ] ] ;
            ns2:UNIT_SLOPE [ dcterms:description "Slope Units" ;
                    dcterms:title "Slope Units" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"radians\""^^rdf:JSON ;
                            proc:enum "degree",
                                "percent",
                                "radians" ;
                            proc:nullable true ;
                            proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:ASPECT [ dcterms:description "Aspect" ;
                    dcterms:title "Aspect" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_CROS [ dcterms:description "Zevenbergen & Thorne (1987) refer to this as plan curvature" ;
                    dcterms:title "Cross-Sectional Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ] ] ] ;
            ns3:C_GENE [ dcterms:description "General Curvature" ;
                    dcterms:title "General Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ] ] ] ;
            ns3:C_LONG [ dcterms:description "Zevenbergen & Thorne (1987) refer to this as profile curvature" ;
                    dcterms:title "Longitudinal Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_MAXI [ dcterms:description "Maximal Curvature" ;
                    dcterms:title "Maximal Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_MINI [ dcterms:description "Minimal Curvature" ;
                    dcterms:title "Minimal Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ] ] ] ;
            ns3:C_PLAN [ dcterms:description "Plan Curvature" ;
                    dcterms:title "Plan Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_PROF [ dcterms:description "Profile Curvature" ;
                    dcterms:title "Profile Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns3:C_ROTO [ dcterms:description "Flow Line Curvature" ;
                    dcterms:title "Flow Line Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ] ] ] ;
            ns3:C_TANG [ dcterms:description "Tangential Curvature" ;
                    dcterms:title "Tangential Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ] ] ] ;
            ns3:C_TOTA [ dcterms:description "Total Curvature" ;
                    dcterms:title "Total Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns3:SLOPE [ dcterms:description "Slope" ;
                    dcterms:title "Slope" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Each bound input/output also carries the `dataType` of that counterpart, a concept of bblocks-data-types. Which deployed input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the deployment's own additions (footnote b). Not what the deployment serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
#### json
```json
{
  "id": "SAGA.ta_morphometry.0",
  "title": "Slope, Aspect, Curvature",
  "description": "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.",
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0/execution"
    }
  ],
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "derivative",
    "Slope"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis"
    },
    {
      "title": "Generic Profile: Terrain derivative",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative"
    },
    {
      "title": "Implementation Profile: Slope",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope"
    }
  ],
  "inputs": {
    "ELEVATION": {
      "title": "Elevation",
      "description": "Elevation",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/elevation-model",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-png"
      ],
      "keywords": [
        "elevation"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Terrain derivative -- input `elevation`",
          "role": "https://w3id.org/geolabs/ospd/generic-profiles/role/generic-input",
          "href": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative/inputs/elevation"
        },
        {
          "title": "Implementation Profile: Slope -- input `elevation`",
          "role": "https://w3id.org/geolabs/ospd/generic-profiles/role/implementation-input",
          "href": "https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope/inputs/elevation"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "METHOD": {
      "title": "Method",
      "description": "Method",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
        "enum": [
          "maximum slope (Travis et al. 1975)",
          "maximum triangle slope (Tarboton 1997)",
          "least squares fitted plane (Horn 1981",
          " Costa-Cabral & Burgess 1996)",
          "6 parameter 2nd order polynom (Evans 1979)",
          "6 parameter 2nd order polynom (Heerdegen & Beran 1982)",
          "6 parameter 2nd order polynom (Bauer",
          " Rohdenburg",
          " Bork 1985)",
          "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
          "10 parameter 3rd order polynom (Haralick 1983)"
        ],
        "nullable": true
      }
    },
    "UNIT_SLOPE": {
      "title": "Slope Units",
      "description": "Slope Units",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "radians",
        "enum": [
          "radians",
          "degree",
          "percent"
        ],
        "nullable": true
      }
    },
    "UNIT_ASPECT": {
      "title": "Aspect Units",
      "description": "Aspect Units",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "radians",
        "enum": [
          "radians",
          "degree"
        ],
        "nullable": true
      }
    }
  },
  "outputs": {
    "SLOPE": {
      "title": "Slope",
      "description": "Slope",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Terrain derivative -- output `result`",
          "role": "https://w3id.org/geolabs/ospd/generic-profiles/role/generic-output",
          "href": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative/outputs/result"
        },
        {
          "title": "Implementation Profile: Slope -- output `result`",
          "role": "https://w3id.org/geolabs/ospd/generic-profiles/role/implementation-output",
          "href": "https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope/outputs/result"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "ASPECT": {
      "title": "Aspect",
      "description": "Aspect",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_GENE": {
      "title": "General Curvature",
      "description": "General Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_PROF": {
      "title": "Profile Curvature",
      "description": "Profile Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_PLAN": {
      "title": "Plan Curvature",
      "description": "Plan Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_TANG": {
      "title": "Tangential Curvature",
      "description": "Tangential Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_LONG": {
      "title": "Longitudinal Curvature",
      "description": "Zevenbergen & Thorne (1987) refer to this as profile curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_CROS": {
      "title": "Cross-Sectional Curvature",
      "description": "Zevenbergen & Thorne (1987) refer to this as plan curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_MINI": {
      "title": "Minimal Curvature",
      "description": "Minimal Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_MAXI": {
      "title": "Maximal Curvature",
      "description": "Maximal Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_TOTA": {
      "title": "Total Curvature",
      "description": "Total Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_ROTO": {
      "title": "Flow Line Curvature",
      "description": "Flow Line Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/context.jsonld",
  "id": "SAGA.ta_morphometry.0",
  "title": "Slope, Aspect, Curvature",
  "description": "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.",
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
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0/execution"
    }
  ],
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "derivative",
    "Slope"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis"
    },
    {
      "title": "Generic Profile: Terrain derivative",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative"
    },
    {
      "title": "Implementation Profile: Slope",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope"
    }
  ],
  "inputs": {
    "ELEVATION": {
      "title": "Elevation",
      "description": "Elevation",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/elevation-model",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-png"
      ],
      "keywords": [
        "elevation"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Terrain derivative -- input `elevation`",
          "role": "https://w3id.org/geolabs/ospd/generic-profiles/role/generic-input",
          "href": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative/inputs/elevation"
        },
        {
          "title": "Implementation Profile: Slope -- input `elevation`",
          "role": "https://w3id.org/geolabs/ospd/generic-profiles/role/implementation-input",
          "href": "https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope/inputs/elevation"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "METHOD": {
      "title": "Method",
      "description": "Method",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
        "enum": [
          "maximum slope (Travis et al. 1975)",
          "maximum triangle slope (Tarboton 1997)",
          "least squares fitted plane (Horn 1981",
          " Costa-Cabral & Burgess 1996)",
          "6 parameter 2nd order polynom (Evans 1979)",
          "6 parameter 2nd order polynom (Heerdegen & Beran 1982)",
          "6 parameter 2nd order polynom (Bauer",
          " Rohdenburg",
          " Bork 1985)",
          "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
          "10 parameter 3rd order polynom (Haralick 1983)"
        ],
        "nullable": true
      }
    },
    "UNIT_SLOPE": {
      "title": "Slope Units",
      "description": "Slope Units",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "radians",
        "enum": [
          "radians",
          "degree",
          "percent"
        ],
        "nullable": true
      }
    },
    "UNIT_ASPECT": {
      "title": "Aspect Units",
      "description": "Aspect Units",
      "minOccurs": 0,
      "schema": {
        "type": "string",
        "default": "radians",
        "enum": [
          "radians",
          "degree"
        ],
        "nullable": true
      }
    }
  },
  "outputs": {
    "SLOPE": {
      "title": "Slope",
      "description": "Slope",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Terrain derivative -- output `result`",
          "role": "https://w3id.org/geolabs/ospd/generic-profiles/role/generic-output",
          "href": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative/outputs/result"
        },
        {
          "title": "Implementation Profile: Slope -- output `result`",
          "role": "https://w3id.org/geolabs/ospd/generic-profiles/role/implementation-output",
          "href": "https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope/outputs/result"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "ASPECT": {
      "title": "Aspect",
      "description": "Aspect",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_GENE": {
      "title": "General Curvature",
      "description": "General Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_PROF": {
      "title": "Profile Curvature",
      "description": "Profile Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_PLAN": {
      "title": "Plan Curvature",
      "description": "Plan Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_TANG": {
      "title": "Tangential Curvature",
      "description": "Tangential Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_LONG": {
      "title": "Longitudinal Curvature",
      "description": "Zevenbergen & Thorne (1987) refer to this as profile curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_CROS": {
      "title": "Cross-Sectional Curvature",
      "description": "Zevenbergen & Thorne (1987) refer to this as plan curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_MINI": {
      "title": "Minimal Curvature",
      "description": "Minimal Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_MAXI": {
      "title": "Maximal Curvature",
      "description": "Maximal Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_TOTA": {
      "title": "Total Curvature",
      "description": "Total Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "image/png"
          }
        ]
      }
    },
    "C_ROTO": {
      "title": "Flow Line Curvature",
      "description": "Flow Line Curvature",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff",
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png"
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
            "contentMediaType": "application/x-ogc-envi"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/x-ogc-aaigrid"
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
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://w3id.org/geolabs/ospd/generic-profiles/> .
@prefix ns3: <https://w3id.org/geolabs/ospd/process-profiles/output/> .
@prefix ns4: <https://w3id.org/geolabs/ospd/process-profiles/input/> .
@prefix ns5: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://w3id.org/geolabs/ospd/process-profiles/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/geolabs/ospd/process-profiles/process/terrain/SAGA.ta_morphometry.0> dcterms:description "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated." ;
    dcterms:subject "Slope",
        "derivative",
        "elevation",
        "raster",
        "terrain" ;
    dcterms:title "Slope, Aspect, Curvature" ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns5:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns4:ELEVATION [ dcterms:description "Elevation" ;
                    dcterms:title "Elevation" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/elevation-model> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-png> ;
                    proc:keywords "elevation" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Slope -- input `elevation`" ;
                            proc:href <https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope/inputs/elevation> ;
                            proc:role <https://w3id.org/geolabs/ospd/generic-profiles/role/implementation-input> ],
                        [ dcterms:title "Generic Profile: Terrain derivative -- input `elevation`" ;
                            proc:href <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative/inputs/elevation> ;
                            proc:role <https://w3id.org/geolabs/ospd/generic-profiles/role/generic-input> ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns4:METHOD [ dcterms:description "Method" ;
                    dcterms:title "Method" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)\""^^rdf:JSON ;
                            proc:enum " Bork 1985)",
                                " Costa-Cabral & Burgess 1996)",
                                " Rohdenburg",
                                "10 parameter 3rd order polynom (Haralick 1983)",
                                "6 parameter 2nd order polynom (Bauer",
                                "6 parameter 2nd order polynom (Evans 1979)",
                                "6 parameter 2nd order polynom (Heerdegen & Beran 1982)",
                                "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)",
                                "least squares fitted plane (Horn 1981",
                                "maximum slope (Travis et al. 1975)",
                                "maximum triangle slope (Tarboton 1997)" ;
                            proc:nullable true ;
                            proc:type "string" ] ] ;
            ns4:UNIT_ASPECT [ dcterms:description "Aspect Units" ;
                    dcterms:title "Aspect Units" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"radians\""^^rdf:JSON ;
                            proc:enum "degree",
                                "radians" ;
                            proc:nullable true ;
                            proc:type "string" ] ] ;
            ns4:UNIT_SLOPE [ dcterms:description "Slope Units" ;
                    dcterms:title "Slope Units" ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"radians\""^^rdf:JSON ;
                            proc:enum "degree",
                                "percent",
                                "radians" ;
                            proc:nullable true ;
                            proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "Implementation Profile: Slope" ;
            proc:href <https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Generic Profile: Terrain derivative" ;
            proc:href <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "Process Concept: Terrain Analysis" ;
            proc:href <https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:ASPECT [ dcterms:description "Aspect" ;
                    dcterms:title "Aspect" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns3:C_CROS [ dcterms:description "Zevenbergen & Thorne (1987) refer to this as plan curvature" ;
                    dcterms:title "Cross-Sectional Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_GENE [ dcterms:description "General Curvature" ;
                    dcterms:title "General Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ] ] ] ;
            ns3:C_LONG [ dcterms:description "Zevenbergen & Thorne (1987) refer to this as profile curvature" ;
                    dcterms:title "Longitudinal Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ] ] ] ;
            ns3:C_MAXI [ dcterms:description "Maximal Curvature" ;
                    dcterms:title "Maximal Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_MINI [ dcterms:description "Minimal Curvature" ;
                    dcterms:title "Minimal Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_PLAN [ dcterms:description "Plan Curvature" ;
                    dcterms:title "Plan Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ] ] ] ;
            ns3:C_PROF [ dcterms:description "Profile Curvature" ;
                    dcterms:title "Profile Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_ROTO [ dcterms:description "Flow Line Curvature" ;
                    dcterms:title "Flow Line Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_TANG [ dcterms:description "Tangential Curvature" ;
                    dcterms:title "Tangential Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ] ] ] ;
            ns3:C_TOTA [ dcterms:description "Total Curvature" ;
                    dcterms:title "Total Curvature" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ] ] ] ;
            ns3:SLOPE [ dcterms:description "Slope" ;
                    dcterms:title "Slope" ;
                    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
                    ns2:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff>,
                        <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png> ;
                    proc:keywords "raster" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Slope -- output `result`" ;
                            proc:href <https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope/outputs/result> ;
                            proc:role <https://w3id.org/geolabs/ospd/generic-profiles/role/implementation-output> ],
                        [ dcterms:title "Generic Profile: Terrain derivative -- output `result`" ;
                            proc:href <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative/outputs/result> ;
                            proc:role <https://w3id.org/geolabs/ospd/generic-profiles/role/generic-output> ] ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ] ] ] ] .


```


### process-type entry
Registered ActivityType OWL class `https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision, linking to its Implementation Profile.
#### json
```json
{
  "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope",
  "sameAs": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://w3id.org/geolabs/ospd/process-profiles/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/process-profiles/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/process-profiles/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://w3id.org/geolabs/ospd/generic-profiles/activity-type/slope, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/identifier-2026-11-17",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/process-profiles/amendmentAction",
      "changeClassification": "clarifying",
      "affectedProperty": "https://w3id.org/ogc/rim/objectIdentifier",
      "description": "The object identifier of this item moves from https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope to https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-17T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/representation-2026-11-18",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/process-profiles/amendmentAction",
      "changeClassification": "substantive",
      "description": "processDescription: in processDescription.inherited.json, each input and output that has a data type now names its representations (representation), the df:Representation items of bblocks-data-formats that realize that data type in a format the deployment declares (decision of 2026-11-18); the inputs/outputs of the deployment's own output ASPECT, output C_GENE, output C_PROF, output C_PLAN, output C_TANG, output C_LONG, output C_CROS, output C_MINI, output C_MAXI, output C_TOTA, output C_ROTO get a dataType (profiles.yaml data_types). Classified substantive: the form in which a part of the entry is stated changes.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-18T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    }
  ],
  "prefLabel": "Slope, Aspect, Curvature",
  "definition": "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.",
  "subClassOf": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/slope",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://w3id.org/geolabs/ospd/process-profiles/process-type",
  "classification": {
    "phase": [
      "https://w3id.org/geolabs/ospd/process-profiles/phase/scientific-computation"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.terrain.slope",
    "processDescription": {
      "id": "SAGA.ta_morphometry.0",
      "version": "1.0.0",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "implementsProfile": "https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope",
  "correspondences": {
    "openeoEquivalence": {
      "level": "none",
      "rationale": "No openEO process computes terrain slope in the published bblocks-openeo register."
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/context.jsonld",
  "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope",
  "sameAs": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://w3id.org/geolabs/ospd/process-profiles/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/process-profiles/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/process-profiles/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://w3id.org/geolabs/ospd/generic-profiles/activity-type/slope, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/identifier-2026-11-17",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/process-profiles/amendmentAction",
      "changeClassification": "clarifying",
      "affectedProperty": "https://w3id.org/ogc/rim/objectIdentifier",
      "description": "The object identifier of this item moves from https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope to https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-17T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/representation-2026-11-18",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/process-profiles/amendmentAction",
      "changeClassification": "substantive",
      "description": "processDescription: in processDescription.inherited.json, each input and output that has a data type now names its representations (representation), the df:Representation items of bblocks-data-formats that realize that data type in a format the deployment declares (decision of 2026-11-18); the inputs/outputs of the deployment's own output ASPECT, output C_GENE, output C_PROF, output C_PLAN, output C_TANG, output C_LONG, output C_CROS, output C_MINI, output C_MAXI, output C_TOTA, output C_ROTO get a dataType (profiles.yaml data_types). Classified substantive: the form in which a part of the entry is stated changes.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-18T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"
    }
  ],
  "prefLabel": "Slope, Aspect, Curvature",
  "definition": "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.",
  "subClassOf": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/slope",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://w3id.org/geolabs/ospd/process-profiles/process-type",
  "classification": {
    "phase": [
      "https://w3id.org/geolabs/ospd/process-profiles/phase/scientific-computation"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.terrain.slope",
    "processDescription": {
      "id": "SAGA.ta_morphometry.0",
      "version": "1.0.0",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "implementsProfile": "https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope",
  "correspondences": {
    "openeoEquivalence": {
      "level": "none",
      "rationale": "No openEO process computes terrain slope in the published bblocks-openeo register."
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
@prefix pp: <https://w3id.org/geolabs/ospd/process-profiles/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-22T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope> ;
    rim:proposer <https://w3id.org/geolabs/ospd/org/geolabs> .

<https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/d5-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer <https://w3id.org/geolabs/ospd/org/geolabs> .

<https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/identifier-2026-11-17> a rim:RegisterAction ;
    dcterms:description "The object identifier of this item moves from https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope to https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes." ;
    prov:startedAtTime "2026-11-17T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:affectedProperty rim:objectIdentifier ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer <https://w3id.org/geolabs/ospd/org/geolabs> .

<https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/representation-2026-11-18> a rim:RegisterAction ;
    dcterms:description "processDescription: in processDescription.inherited.json, each input and output that has a data type now names its representations (representation), the df:Representation items of bblocks-data-formats that realize that data type in a format the deployment declares (decision of 2026-11-18); the inputs/outputs of the deployment's own output ASPECT, output C_GENE, output C_PROF, output C_PLAN, output C_TANG, output C_LONG, output C_CROS, output C_MINI, output C_MAXI, output C_TOTA, output C_ROTO get a dataType (profiles.yaml data_types). Classified substantive: the form in which a part of the entry is stated changes." ;
    prov:startedAtTime "2026-11-18T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer <https://w3id.org/geolabs/ospd/org/geolabs> .

<https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/specialisation-2026-11-10> a rim:RegisterAction ;
    dcterms:description "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://w3id.org/geolabs/ospd/generic-profiles/activity-type/slope, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer <https://w3id.org/geolabs/ospd/org/geolabs> .

<https://w3id.org/geolabs/ospd/process-profiles/process/terrain/SAGA.ta_morphometry.0> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0> ;
    pp:version "1.0.0" .

<https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope> a owl:Class,
        pp:ProcessType,
        acttype:ActivityType ;
    rdfs:subClassOf <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/slope> ;
    owl:sameAs <https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope> ;
    skos:definition "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Slope, Aspect, Curvature" ;
    pp:deployment [ pp:processDescription <https://w3id.org/geolabs/ospd/process-profiles/process/terrain/SAGA.ta_morphometry.0> ;
            pp:profile "ospd.process-profiles.terrain.slope" ;
            pp:provenanceClass wfprov:ProcessRun ] ;
    pp:implementsProfile <https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "none" ;
            pp:rationale "No openEO process computes terrain slope in the published bblocks-openeo register." ] ;
    pp:phase <https://w3id.org/geolabs/ospd/process-profiles/phase/scientific-computation> ;
    acttype:generatedEntityType geo:Feature ;
    acttype:usedEntityType geo:Feature ;
    rim:hasAction <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/addition>,
        <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/d5-2026-11-09>,
        <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/identifier-2026-11-17>,
        <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/representation-2026-11-18>,
        <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope/actions/specialisation-2026-11-10> ;
    rim:inRegister pp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/slope"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Profile of the live OGC API - Processes processDescription of `SAGA.ta_morphometry.0`.
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
      const: SAGA.ta_morphometry.0
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - ELEVATION
      - METHOD
      - UNIT_SLOPE
      - UNIT_ASPECT
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://w3id.org/geolabs/ospd/process-profiles/input/
    outputs:
      type: object
      required:
      - SLOPE
      - ASPECT
      - C_GENE
      - C_PROF
      - C_PLAN
      - C_TANG
      - C_LONG
      - C_CROS
      - C_MINI
      - C_MAXI
      - C_TOTA
      - C_ROTO
      x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
      x-jsonld-vocab: https://w3id.org/geolabs/ospd/process-profiles/output/
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
          const: SAGA.ta_morphometry.0
          x-jsonld-id: '@id'
        inputs:
          type: object
          required:
          - ELEVATION
          - METHOD
          - UNIT_SLOPE
          - UNIT_ASPECT
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://w3id.org/geolabs/ospd/process-profiles/input/
        outputs:
          type: object
          required:
          - SLOPE
          - ASPECT
          - C_GENE
          - C_PROF
          - C_PLAN
          - C_TANG
          - C_LONG
          - C_CROS
          - C_MINI
          - C_MAXI
          - C_TOTA
          - C_ROTO
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://w3id.org/geolabs/ospd/process-profiles/output/
    - description: '`SAGA.ta_morphometry.0` as the Implementation (instance level)
        of `https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope`:
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
              const: terrain
          - contains:
              const: elevation
          - contains:
              const: raster
          - contains:
              const: derivative
          - contains:
              const: Slope
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
                  const: https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
                href:
                  const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation
                href:
                  const: https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        inputs:
          type: object
          required:
          - ELEVATION
          properties:
            ELEVATION:
              required:
              - dataType
              - keywords
              - metadata
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/elevation-model
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: elevation
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
                          const: https://w3id.org/geolabs/ospd/generic-profiles/role/generic-input
                        href:
                          const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative/inputs/elevation
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://w3id.org/geolabs/ospd/generic-profiles/role/implementation-input
                        href:
                          const: https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope/inputs/elevation
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://w3id.org/geolabs/ospd/process-profiles/input/
        outputs:
          type: object
          required:
          - ASPECT
          - C_CROS
          - C_GENE
          - C_LONG
          - C_MAXI
          - C_MINI
          - C_PLAN
          - C_PROF
          - C_ROTO
          - C_TANG
          - C_TOTA
          - SLOPE
          properties:
            SLOPE:
              required:
              - dataType
              - keywords
              - metadata
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: raster
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
                          const: https://w3id.org/geolabs/ospd/generic-profiles/role/generic-output
                        href:
                          const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/terrain-derivative/outputs/result
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://w3id.org/geolabs/ospd/generic-profiles/role/implementation-output
                        href:
                          const: https://w3id.org/geolabs/ospd/generic-profiles/implementation-profile/slope/outputs/result
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            ASPECT:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_GENE:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_PROF:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_PLAN:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_TANG:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_LONG:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_CROS:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_MINI:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_MAXI:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_TOTA:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
            C_ROTO:
              required:
              - dataType
              - representation
              properties:
                dataType:
                  const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                representation:
                  const:
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-aaigrid
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-envi
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
                  - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-png
                  x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
                  x-jsonld-type: '@id'
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://w3id.org/geolabs/ospd/process-profiles/output/
x-jsonld-extra-terms:
  type: '@type'
  ProcessRun: http://purl.org/wf4ever/wfprov#ProcessRun
  WorkflowRun: http://purl.org/wf4ever/wfprov#WorkflowRun
  WorkflowEngine: http://purl.org/wf4ever/wfprov#WorkflowEngine
  Artifact: http://purl.org/wf4ever/wfprov#Artifact
  ProcessType: https://w3id.org/geolabs/ospd/process-profiles/ProcessType
  ActivityType: https://w3id.org/ogc/rim/activity-type/ActivityType
  owlClass: http://www.w3.org/2002/07/owl#Class
  subClassOf:
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#subClassOf
    x-jsonld-type: '@id'
  title: http://purl.org/dc/terms/title
  description: http://purl.org/dc/terms/description
  keywords: http://purl.org/dc/terms/subject
  version: https://w3id.org/geolabs/ospd/process-profiles/version
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
  representation:
    x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/representation
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
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/processDescription
    x-jsonld-context:
      href:
        '@id': http://www.w3.org/2000/01/rdf-schema#seeAlso
        '@type': '@id'
      license:
        '@id': http://purl.org/dc/terms/license
        '@type': '@id'
  result: https://w3id.org/geolabs/ospd/process-profiles/result
  engine: https://w3id.org/geolabs/ospd/process-profiles/engine
  run: https://w3id.org/geolabs/ospd/process-profiles/run
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
  agentType:
    x-jsonld-id: '@type'
    x-jsonld-type: '@id'
  Activity: http://www.w3.org/ns/prov#Activity
  Entity: http://www.w3.org/ns/prov#Entity
  Agent: http://www.w3.org/ns/prov#Agent
  SoftwareAgent: http://www.w3.org/ns/prov#SoftwareAgent
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
  affectedProperty:
    x-jsonld-id: https://w3id.org/ogc/rim/affectedProperty
    x-jsonld-type: '@id'
  sameAs:
    x-jsonld-id: http://www.w3.org/2002/07/owl#sameAs
    x-jsonld-type: '@id'
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://w3id.org/geolabs/ospd/process-profiles/status
  classification: '@nest'
  correspondences: '@nest'
  phase:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/phase
    x-jsonld-type: '@id'
  deployment: https://w3id.org/geolabs/ospd/process-profiles/deployment
  profile: https://w3id.org/geolabs/ospd/process-profiles/profile
  plan:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/plan
    x-jsonld-context:
      license:
        '@id': http://purl.org/dc/terms/license
        '@type': '@id'
  Plan: http://www.w3.org/ns/prov#Plan
  cwlClass: https://w3id.org/geolabs/ospd/process-profiles/cwlClass
  cwlId: https://w3id.org/geolabs/ospd/process-profiles/cwlId
  provenanceClass:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/provenanceClass
    x-jsonld-type: '@id'
  implementsProfile:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/implementsProfile
    x-jsonld-type: '@id'
  cctDependencies: https://w3id.org/geolabs/ospd/process-profiles/cctDependency
  candidateCctDependencies: https://w3id.org/geolabs/ospd/process-profiles/candidateCctDependency
  hasStep:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/hasStep
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
  openeoEquivalence: https://w3id.org/geolabs/ospd/process-profiles/openeoEquivalence
  level: https://w3id.org/geolabs/ospd/process-profiles/equivalenceLevel
  rationale: https://w3id.org/geolabs/ospd/process-profiles/rationale
  decomposition:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/decomposition
    x-jsonld-container: '@list'
  stage: https://w3id.org/geolabs/ospd/process-profiles/stage
  openeo: https://w3id.org/geolabs/ospd/process-profiles/openeo
  note: http://www.w3.org/2004/02/skos/core#note
  serverSideFiles:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/serverSideFile
    x-jsonld-context:
      name: https://w3id.org/geolabs/ospd/process-profiles/liveName
      side: https://w3id.org/geolabs/ospd/process-profiles/side
      implements:
        '@id': https://w3id.org/geolabs/ospd/process-profiles/implements
        '@type': '@id'
      location: https://w3id.org/geolabs/ospd/process-profiles/location
  roleDecompositions:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/roleDecomposition
    x-jsonld-context:
      side: https://w3id.org/geolabs/ospd/process-profiles/side
      implements:
        '@id': https://w3id.org/geolabs/ospd/process-profiles/implements
        '@type': '@id'
      parts:
        '@id': https://w3id.org/geolabs/ospd/process-profiles/part
        '@container': '@list'
      selectors:
        '@id': https://w3id.org/geolabs/ospd/process-profiles/selector
        '@context':
          name: https://w3id.org/geolabs/ospd/process-profiles/liveName
          values: http://www.w3.org/1999/02/22-rdf-syntax-ns#value
      reproducible:
        '@id': https://w3id.org/geolabs/ospd/process-profiles/reproducible
        '@type': http://www.w3.org/2001/XMLSchema#boolean
      note: http://www.w3.org/2004/02/skos/core#note
  unboundRoles:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/unboundRole
    x-jsonld-context:
      side: https://w3id.org/geolabs/ospd/process-profiles/side
      implements:
        '@id': https://w3id.org/geolabs/ospd/process-profiles/implements
        '@type': '@id'
      reason: http://www.w3.org/2004/02/skos/core#note
  fixedRoleValues:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/fixedRoleValue
    x-jsonld-context:
      side: https://w3id.org/geolabs/ospd/process-profiles/side
      implements:
        '@id': https://w3id.org/geolabs/ospd/process-profiles/implements
        '@type': '@id'
      values: http://www.w3.org/1999/02/22-rdf-syntax-ns#value
      reason: http://www.w3.org/2004/02/skos/core#note
  byReference:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/byReference
    x-jsonld-context:
      name: https://w3id.org/geolabs/ospd/process-profiles/liveName
      side: https://w3id.org/geolabs/ospd/process-profiles/side
      implements:
        '@id': https://w3id.org/geolabs/ospd/process-profiles/implements
        '@type': '@id'
      note: http://www.w3.org/2004/02/skos/core#note
  notAttached:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/notAttached
    x-jsonld-context:
      reason: http://www.w3.org/2004/02/skos/core#note
  assumedFormatGaps:
    x-jsonld-id: https://w3id.org/geolabs/ospd/process-profiles/assumedFormatGap
    x-jsonld-context:
      name: https://w3id.org/geolabs/ospd/process-profiles/liveName
      side: https://w3id.org/geolabs/ospd/process-profiles/side
      implements:
        '@id': https://w3id.org/geolabs/ospd/process-profiles/implements
        '@type': '@id'
      served: https://w3id.org/geolabs/ospd/process-profiles/servedMediaType
      reason: http://www.w3.org/2004/02/skos/core#note
      evidence: https://w3id.org/geolabs/ospd/process-profiles/evidence
x-jsonld-vocab: https://w3id.org/geolabs/ospd/process-profiles/
x-jsonld-prefixes:
  wfprov: http://purl.org/wf4ever/wfprov#
  pp: https://w3id.org/geolabs/ospd/process-profiles/
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
  itemIdentifier: ospd.process-profiles.terrain.slope
  register: https://geolabs.github.io/bblocks-process-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-25'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/geolabs/ospd/process-profiles/",
    "inputs": {
      "@context": {
        "@vocab": "https://w3id.org/geolabs/ospd/process-profiles/input/",
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
        "@vocab": "https://w3id.org/geolabs/ospd/process-profiles/output/",
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
    "representation": {
      "@id": "https://w3id.org/geolabs/ospd/generic-profiles/representation",
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
    "agentType": {
      "@id": "@type",
      "@type": "@id"
    },
    "Activity": "prov:Activity",
    "Entity": "prov:Entity",
    "Agent": "prov:Agent",
    "SoftwareAgent": "prov:SoftwareAgent",
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
    "affectedProperty": {
      "@id": "rim:affectedProperty",
      "@type": "@id"
    },
    "sameAs": {
      "@id": "owl:sameAs",
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
    "pp": "https://w3id.org/geolabs/ospd/process-profiles/",
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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/terrain/slope`

