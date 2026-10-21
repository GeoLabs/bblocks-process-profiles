
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

Implements [`Slope`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope) (`generic-profiles.implementation-profile.slope`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `ELEVATION` | input `elevation` |
| `METHOD`, `UNIT_SLOPE`, `UNIT_ASPECT` | -- (live-only inputs, Table 21 footnote b) |
| `SLOPE` | output `result` |
| `ASPECT`, `C_GENE`, `C_PROF`, `C_PLAN`, `C_TANG`, `C_LONG`, `C_CROS`, `C_MINI`, `C_MAXI`, `C_TOTA`, `C_ROTO` | -- (live-only outputs, Table 21 footnote b) |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
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
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns3: <http://www.iana.org/assignments/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/SAGA.ta_morphometry.0> dcterms:description "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated." ;
    dcterms:title "Slope, Aspect, Curvature" ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns3:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns4:ELEVATION [ dcterms:description "Elevation" ;
                    dcterms:title "Elevation" ;
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
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns2:ASPECT [ dcterms:description "Aspect" ;
                    dcterms:title "Aspect" ;
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
            ns2:C_CROS [ dcterms:description "Zevenbergen & Thorne (1987) refer to this as plan curvature" ;
                    dcterms:title "Cross-Sectional Curvature" ;
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
            ns2:C_GENE [ dcterms:description "General Curvature" ;
                    dcterms:title "General Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ] ] ] ;
            ns2:C_LONG [ dcterms:description "Zevenbergen & Thorne (1987) refer to this as profile curvature" ;
                    dcterms:title "Longitudinal Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ] ] ] ;
            ns2:C_MAXI [ dcterms:description "Maximal Curvature" ;
                    dcterms:title "Maximal Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns2:C_MINI [ dcterms:description "Minimal Curvature" ;
                    dcterms:title "Minimal Curvature" ;
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
            ns2:C_PLAN [ dcterms:description "Plan Curvature" ;
                    dcterms:title "Plan Curvature" ;
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
            ns2:C_PROF [ dcterms:description "Profile Curvature" ;
                    dcterms:title "Profile Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ] ] ] ;
            ns2:C_ROTO [ dcterms:description "Flow Line Curvature" ;
                    dcterms:title "Flow Line Curvature" ;
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
            ns2:C_TANG [ dcterms:description "Tangential Curvature" ;
                    dcterms:title "Tangential Curvature" ;
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
            ns2:C_TOTA [ dcterms:description "Total Curvature" ;
                    dcterms:title "Total Curvature" ;
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
            ns2:SLOPE [ dcterms:description "Slope" ;
                    dcterms:title "Slope" ;
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
                                    ns1:contentMediaType "image/png" ] ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Which live input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the live service's own additions (footnote b). Not what the live service serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
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
    "Slope",
    "ta_morphometry"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
    },
    {
      "title": "Generic Profile: Terrain derivative",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative"
    },
    {
      "title": "Implementation Profile: Slope",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope"
    }
  ],
  "inputs": {
    "ELEVATION": {
      "title": "Elevation",
      "description": "Elevation",
      "keywords": [
        "elevation",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Terrain derivative -- input `elevation`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation"
        },
        {
          "title": "Implementation Profile: Slope -- input `elevation`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope/inputs/elevation"
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
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Terrain derivative -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result"
        },
        {
          "title": "Implementation Profile: Slope -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope/outputs/result"
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
    "Slope",
    "ta_morphometry"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
    },
    {
      "title": "Generic Profile: Terrain derivative",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative"
    },
    {
      "title": "Implementation Profile: Slope",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope"
    }
  ],
  "inputs": {
    "ELEVATION": {
      "title": "Elevation",
      "description": "Elevation",
      "keywords": [
        "elevation",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Terrain derivative -- input `elevation`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation"
        },
        {
          "title": "Implementation Profile: Slope -- input `elevation`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope/inputs/elevation"
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
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Terrain derivative -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result"
        },
        {
          "title": "Implementation Profile: Slope -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope/outputs/result"
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

<https://geolabs.github.io/bblocks-process-profiles/def/process/SAGA.ta_morphometry.0> dcterms:description "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated." ;
    dcterms:subject "Slope",
        "derivative",
        "elevation",
        "raster",
        "ta_morphometry",
        "terrain" ;
    dcterms:title "Slope, Aspect, Curvature" ;
    rdfs:seeAlso [ rdfs:label "Execute End Point" ;
            dcterms:type "application/json" ;
            ns4:relation <http://www.opengis.net/def/rel/ogc/1.0/execute> ;
            oa:hasTarget <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0/execution> ] ;
    pp:version "1.0.0" ;
    proc:inputs [ ns2:ELEVATION [ dcterms:description "Elevation" ;
                    dcterms:title "Elevation" ;
                    proc:keywords "GeoTIFF",
                        "elevation" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Slope -- input `elevation`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope/inputs/elevation> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ],
                        [ dcterms:title "Generic Profile: Terrain derivative -- input `elevation`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
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
    proc:metadata [ dcterms:title "Generic Profile: Terrain derivative" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "Implementation Profile: Slope" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Process Concept: Terrain Analysis" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:ASPECT [ dcterms:description "Aspect" ;
                    dcterms:title "Aspect" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:C_CROS [ dcterms:description "Zevenbergen & Thorne (1987) refer to this as plan curvature" ;
                    dcterms:title "Cross-Sectional Curvature" ;
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
            ns3:C_GENE [ dcterms:description "General Curvature" ;
                    dcterms:title "General Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ] ] ] ;
            ns3:C_LONG [ dcterms:description "Zevenbergen & Thorne (1987) refer to this as profile curvature" ;
                    dcterms:title "Longitudinal Curvature" ;
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
            ns3:C_MAXI [ dcterms:description "Maximal Curvature" ;
                    dcterms:title "Maximal Curvature" ;
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
            ns3:C_MINI [ dcterms:description "Minimal Curvature" ;
                    dcterms:title "Minimal Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ] ] ] ;
            ns3:C_PLAN [ dcterms:description "Plan Curvature" ;
                    dcterms:title "Plan Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns3:C_PROF [ dcterms:description "Profile Curvature" ;
                    dcterms:title "Profile Curvature" ;
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
            ns3:C_ROTO [ dcterms:description "Flow Line Curvature" ;
                    dcterms:title "Flow Line Curvature" ;
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
            ns3:C_TANG [ dcterms:description "Tangential Curvature" ;
                    dcterms:title "Tangential Curvature" ;
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
            ns3:C_TOTA [ dcterms:description "Total Curvature" ;
                    dcterms:title "Total Curvature" ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-envi" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/x-ogc-aaigrid" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns3:SLOPE [ dcterms:description "Slope" ;
                    dcterms:title "Slope" ;
                    proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Slope -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output> ],
                        [ dcterms:title "Generic Profile: Terrain derivative -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
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
Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope` (`ospd.process-profiles.process-type`), status `submitted`, linking to its Implementation Profile.
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope",
  "type": "ProcessType",
  "prefLabel": "Slope, Aspect, Curvature",
  "definition": "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.terrain.slope",
  "processDescription": {
    "id": "SAGA.ta_morphometry.0",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "No openEO process computes terrain slope in the published bblocks-openeo register."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope",
  "type": "ProcessType",
  "prefLabel": "Slope, Aspect, Curvature",
  "definition": "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.terrain.slope",
  "processDescription": {
    "id": "SAGA.ta_morphometry.0",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "No openEO process computes terrain slope in the published bblocks-openeo register."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/terrain/slope> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> ;
    skos:definition "Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Slope, Aspect, Curvature" ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "none" ;
            pp:rationale "No openEO process computes terrain slope in the published bblocks-openeo register." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/SAGA.ta_morphometry.0> ;
    pp:profile "ospd.process-profiles.terrain.slope" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/SAGA.ta_morphometry.0> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0> ;
    pp:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Profile of the live OGC API - Processes processDescription of `SAGA.ta_morphometry.0`.
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
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
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
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
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
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
    - description: '`SAGA.ta_morphometry.0` as the Implementation (instance level)
        of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope`:
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
          - contains:
              const: ta_morphometry
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
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        inputs:
          type: object
          required:
          - ELEVATION
          properties:
            ELEVATION:
              required:
              - keywords
              - metadata
              properties:
                keywords:
                  allOf:
                  - contains:
                      const: elevation
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope/inputs/elevation
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - SLOPE
          properties:
            SLOPE:
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope/outputs/result
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
  itemIdentifier: ospd.process-profiles.terrain.slope
  register: https://geolabs.github.io/bblocks-process-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-21'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/terrain/slope/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/terrain/slope`

