
# Process profile: OTB.ImageEnvelope (Schema)

`ospd.process-profiles.raster.extent` *v0.1*

Process profile of the live OGC API - Processes process `OTB.ImageEnvelope` (ZOO-Project, Geonovum testbed), with a process-type entry linking to its Implementation Profile. Static processDescription only, no execute/results/provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Source (referenced)
The processDescription is fetched from the live service, not copied: <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope>.

### processDescription
Live OGC API - Processes processDescription, normalised (ZOO-Project-internal fields dropped).
#### json
```json
{
  "id": "OTB.ImageEnvelope",
  "title": "Extracts an image envelope.",
  "description": "Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used.",
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
      "title": "Input image filename.",
      "description": "Input image filename.",
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
    "sr": {
      "title": "Sampling rate for image edges (in pixel).",
      "description": "Sampling rate for image edges (in pixel).",
      "schema": {
        "type": "integer",
        "default": 0,
        "nullable": true
      }
    },
    "elev": {
      "title": "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory.",
      "description": "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory.",
      "schema": {
        "type": "string",
        "nullable": true
      }
    },
    "elev.geoid": {
      "title": "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd).",
      "description": "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd).",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/octet-stream"
          }
        ]
      }
    },
    "elev.default": {
      "title": "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value.",
      "description": "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value.",
      "schema": {
        "type": "number",
        "default": 0,
        "format": "float"
      }
    },
    "proj": {
      "title": "Projection to be used to compute the envelope (default is WGS84)",
      "description": "Projection to be used to compute the envelope (default is WGS84)",
      "schema": {
        "type": "string",
        "nullable": true
      }
    }
  },
  "outputs": {
    "out": {
      "title": "Vector data file containing the envelope.",
      "description": "Vector data file containing the envelope.",
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
            "contentMediaType": "application/vnd.google-earth.kml+xml"
          },
          {
            "type": "object"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/zip"
          }
        ]
      }
    }
  },
  "mutable": false
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/extent/context.jsonld",
  "id": "OTB.ImageEnvelope",
  "title": "Extracts an image envelope.",
  "description": "Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used.",
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
      "title": "Input image filename.",
      "description": "Input image filename.",
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
    "sr": {
      "title": "Sampling rate for image edges (in pixel).",
      "description": "Sampling rate for image edges (in pixel).",
      "schema": {
        "type": "integer",
        "default": 0,
        "nullable": true
      }
    },
    "elev": {
      "title": "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory.",
      "description": "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory.",
      "schema": {
        "type": "string",
        "nullable": true
      }
    },
    "elev.geoid": {
      "title": "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd).",
      "description": "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd).",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/octet-stream"
          }
        ]
      }
    },
    "elev.default": {
      "title": "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value.",
      "description": "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value.",
      "schema": {
        "type": "number",
        "default": 0,
        "format": "float"
      }
    },
    "proj": {
      "title": "Projection to be used to compute the envelope (default is WGS84)",
      "description": "Projection to be used to compute the envelope (default is WGS84)",
      "schema": {
        "type": "string",
        "nullable": true
      }
    }
  },
  "outputs": {
    "out": {
      "title": "Vector data file containing the envelope.",
      "description": "Vector data file containing the envelope.",
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
            "contentMediaType": "application/vnd.google-earth.kml+xml"
          },
          {
            "type": "object"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/zip"
          }
        ]
      }
    }
  },
  "mutable": false
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.ImageEnvelope> dcterms:description "Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used." ;
    dcterms:title "Extracts an image envelope." ;
    pp:version "1.0.0" ;
    proc:inputs [ ns2:elev [ dcterms:description "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory." ;
                    dcterms:title "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory." ;
                    proc:schema [ proc:nullable true ;
                            proc:type "string" ] ] ;
            ns2:elev.default [ dcterms:description "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value." ;
                    dcterms:title "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value." ;
                    proc:schema [ proc:default "0"^^rdf:JSON ;
                            proc:type "number" ;
                            ns1:format "float" ] ] ;
            ns2:elev.geoid [ dcterms:description "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd)." ;
                    dcterms:title "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd)." ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/octet-stream" ] ] ] ;
            ns2:in [ dcterms:description "Input image filename." ;
                    dcterms:title "Input image filename." ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/png" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/jpeg" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "image/tiff" ] ] ] ;
            ns2:proj [ dcterms:description "Projection to be used to compute the envelope (default is WGS84)" ;
                    dcterms:title "Projection to be used to compute the envelope (default is WGS84)" ;
                    proc:schema [ proc:nullable true ;
                            proc:type "string" ] ] ;
            ns2:sr [ dcterms:description "Sampling rate for image edges (in pixel)." ;
                    dcterms:title "Sampling rate for image edges (in pixel)." ;
                    proc:schema [ proc:default "0"^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "integer" ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:out [ dcterms:description "Vector data file containing the envelope." ;
                    dcterms:title "Vector data file containing the envelope." ;
                    proc:schema [ ns1:oneOf [ proc:type "string" ;
                                    ns1:contentEncoding "utf-8" ;
                                    ns1:contentMediaType "text/xml" ],
                                [ proc:type "object" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "base64" ;
                                    ns1:contentMediaType "application/zip" ],
                                [ proc:type "string" ;
                                    ns1:contentEncoding "utf-8" ;
                                    ns1:contentMediaType "application/vnd.google-earth.kml+xml" ] ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Which live input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the live service's own additions (footnote b). Not what the live service serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
#### json
```json
{
  "id": "OTB.ImageEnvelope",
  "title": "Extracts an image envelope.",
  "description": "Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used.",
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
  "keywords": [
    "raster",
    "coverage",
    "extent",
    "OTB",
    "ImageEnvelope"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster extent",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent"
    },
    {
      "title": "Implementation Profile: Raster extent",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent"
    }
  ],
  "inputs": {
    "in": {
      "title": "Input image filename.",
      "description": "Input image filename.",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster extent -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/inputs/raster"
        },
        {
          "title": "Implementation Profile: Raster extent -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent/inputs/raster"
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
    "sr": {
      "title": "Sampling rate for image edges (in pixel).",
      "description": "Sampling rate for image edges (in pixel).",
      "schema": {
        "type": "integer",
        "default": 0,
        "nullable": true
      }
    },
    "elev": {
      "title": "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory.",
      "description": "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory.",
      "schema": {
        "type": "string",
        "nullable": true
      }
    },
    "elev.geoid": {
      "title": "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd).",
      "description": "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd).",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/octet-stream"
          }
        ]
      }
    },
    "elev.default": {
      "title": "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value.",
      "description": "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value.",
      "schema": {
        "type": "number",
        "default": 0,
        "format": "float"
      }
    },
    "proj": {
      "title": "Projection to be used to compute the envelope (default is WGS84)",
      "description": "Projection to be used to compute the envelope (default is WGS84)",
      "schema": {
        "type": "string",
        "nullable": true
      }
    }
  },
  "outputs": {
    "out": {
      "title": "Vector data file containing the envelope.",
      "description": "Vector data file containing the envelope.",
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster extent -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/outputs/result"
        },
        {
          "title": "Implementation Profile: Raster extent -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent/outputs/result"
        }
      ],
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
            "contentMediaType": "application/vnd.google-earth.kml+xml"
          },
          {
            "type": "object"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/zip"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/extent/context.jsonld",
  "id": "OTB.ImageEnvelope",
  "title": "Extracts an image envelope.",
  "description": "Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used.",
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
  "keywords": [
    "raster",
    "coverage",
    "extent",
    "OTB",
    "ImageEnvelope"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster extent",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent"
    },
    {
      "title": "Implementation Profile: Raster extent",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent"
    }
  ],
  "inputs": {
    "in": {
      "title": "Input image filename.",
      "description": "Input image filename.",
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster extent -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/inputs/raster"
        },
        {
          "title": "Implementation Profile: Raster extent -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent/inputs/raster"
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
    "sr": {
      "title": "Sampling rate for image edges (in pixel).",
      "description": "Sampling rate for image edges (in pixel).",
      "schema": {
        "type": "integer",
        "default": 0,
        "nullable": true
      }
    },
    "elev": {
      "title": "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory.",
      "description": "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory.",
      "schema": {
        "type": "string",
        "nullable": true
      }
    },
    "elev.geoid": {
      "title": "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd).",
      "description": "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd).",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/octet-stream"
          }
        ]
      }
    },
    "elev.default": {
      "title": "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value.",
      "description": "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value.",
      "schema": {
        "type": "number",
        "default": 0,
        "format": "float"
      }
    },
    "proj": {
      "title": "Projection to be used to compute the envelope (default is WGS84)",
      "description": "Projection to be used to compute the envelope (default is WGS84)",
      "schema": {
        "type": "string",
        "nullable": true
      }
    }
  },
  "outputs": {
    "out": {
      "title": "Vector data file containing the envelope.",
      "description": "Vector data file containing the envelope.",
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster extent -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/outputs/result"
        },
        {
          "title": "Implementation Profile: Raster extent -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent/outputs/result"
        }
      ],
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
            "contentMediaType": "application/vnd.google-earth.kml+xml"
          },
          {
            "type": "object"
          },
          {
            "type": "string",
            "contentEncoding": "base64",
            "contentMediaType": "application/zip"
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
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.ImageEnvelope> dcterms:description "Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used." ;
    dcterms:subject "ImageEnvelope",
        "OTB",
        "coverage",
        "extent",
        "raster" ;
    dcterms:title "Extracts an image envelope." ;
    pp:version "1.0.0" ;
    proc:inputs [ ns1:elev [ dcterms:description "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory." ;
                    dcterms:title "This parameter allows selecting a directory containing Digital Elevation Model files. Note that this directory should contain only DEM files. Unexpected behaviour might occurs if other images are found in this directory." ;
                    proc:schema [ proc:nullable true ;
                            proc:type "string" ] ] ;
            ns1:elev.default [ dcterms:description "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value." ;
                    dcterms:title "This parameter allows setting the default height above ellipsoid when there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles, and no geoid file has been set. This is also used by some application as an average elevation value." ;
                    proc:schema [ proc:default "0"^^rdf:JSON ;
                            proc:type "number" ;
                            ns2:format "float" ] ] ;
            ns1:elev.geoid [ dcterms:description "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd)." ;
                    dcterms:title "Use a geoid grid to get the height above the ellipsoid in case there is no DEM available, no coverage for some points or pixels with no_data in the DEM tiles. A version of the geoid can be found on the OTB website(https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb-data/blob/master/Input/DEM/egm96.grd)." ;
                    proc:schema [ ns2:oneOf [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "application/octet-stream" ] ] ] ;
            ns1:in [ dcterms:description "Input image filename." ;
                    dcterms:title "Input image filename." ;
                    proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:metadata [ dcterms:title "Implementation Profile: Raster extent -- input `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent/inputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ],
                        [ dcterms:title "Generic Profile: Raster extent -- input `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/inputs/raster> ;
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
            ns1:proj [ dcterms:description "Projection to be used to compute the envelope (default is WGS84)" ;
                    dcterms:title "Projection to be used to compute the envelope (default is WGS84)" ;
                    proc:schema [ proc:nullable true ;
                            proc:type "string" ] ] ;
            ns1:sr [ dcterms:description "Sampling rate for image edges (in pixel)." ;
                    dcterms:title "Sampling rate for image edges (in pixel)." ;
                    proc:schema [ proc:default "0"^^rdf:JSON ;
                            proc:nullable true ;
                            proc:type "integer" ] ] ] ;
    proc:jobControlOptions "async-execute",
        "dismiss",
        "sync-execute" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Implementation Profile: Raster extent" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Generic Profile: Raster extent" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
    proc:mutable false ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:out [ dcterms:description "Vector data file containing the envelope." ;
                    dcterms:title "Vector data file containing the envelope." ;
                    proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Generic Profile: Raster extent -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ],
                        [ dcterms:title "Implementation Profile: Raster extent -- output `result`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent/outputs/result> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output> ] ;
                    proc:schema [ ns2:oneOf [ proc:type "string" ;
                                    ns2:contentEncoding "base64" ;
                                    ns2:contentMediaType "application/zip" ],
                                [ proc:type "object" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "utf-8" ;
                                    ns2:contentMediaType "text/xml" ],
                                [ proc:type "string" ;
                                    ns2:contentEncoding "utf-8" ;
                                    ns2:contentMediaType "application/vnd.google-earth.kml+xml" ] ] ] ] .


```


### process-type entry
Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extent` (`ospd.process-profiles.process-type`), status `submitted`, linking to its Implementation Profile.
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extent",
  "type": "ProcessType",
  "prefLabel": "Extracts an image envelope.",
  "definition": "Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.raster.extent",
  "processDescription": {
    "id": "OTB.ImageEnvelope",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "No openEO process computes the bounding envelope of a raster/data cube in the published bblocks-openeo register (filter_bbox takes a bbox as input to filter by, it does not compute one as output)."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/extent/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extent",
  "type": "ProcessType",
  "prefLabel": "Extracts an image envelope.",
  "definition": "Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.raster.extent",
  "processDescription": {
    "id": "OTB.ImageEnvelope",
    "version": "1.0.0",
    "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent",
  "openeoEquivalence": {
    "level": "none",
    "rationale": "No openEO process computes the bounding envelope of a raster/data cube in the published bblocks-openeo register (filter_bbox takes a bbox as input to filter by, it does not compute one as output)."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extent> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation> ;
    skos:definition "Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Extracts an image envelope." ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "none" ;
            pp:rationale "No openEO process computes the bounding envelope of a raster/data cube in the published bblocks-openeo register (filter_bbox takes a bbox as input to filter by, it does not compute one as output)." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.ImageEnvelope> ;
    pp:profile "ospd.process-profiles.raster.extent" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.ImageEnvelope> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope> ;
    pp:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Profile of the live OGC API - Processes processDescription of `OTB.ImageEnvelope`.
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
      const: OTB.ImageEnvelope
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - in
      - sr
      - elev
      - elev.geoid
      - elev.default
      - proj
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
          const: OTB.ImageEnvelope
          x-jsonld-id: '@id'
        inputs:
          type: object
          required:
          - in
          - sr
          - elev
          - elev.geoid
          - elev.default
          - proj
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - out
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
    - description: '`OTB.ImageEnvelope` as the Implementation (instance level) of
        `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent`:
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
              const: extent
          - contains:
              const: OTB
          - contains:
              const: ImageEnvelope
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
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/inputs/raster
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent/inputs/raster
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/outputs/result
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent/outputs/result
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/extent/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/extent/schema.yaml)


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
    "minOccurs": "proc:minOccurs",
    "maxOccurs": "proc:maxOccurs",
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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/raster/extent/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/raster/extent`

