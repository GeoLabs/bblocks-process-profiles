
# Process profile: crop (Schema)

`ospd.process-profiles.water-bodies.crop` *v0.1*

OGC API - Processes profile of the CWL CommandLineTool `crop` (W3 Water Bodies), with its provenance view, process-type entry and openEO equivalence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of **`crop`** (CommandLineTool, W3 Water Bodies).

> Crop a Sentinel-2 COG band to an area of interest

## Source

- CWL: [crop.cwl](https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/72a76ae1d5ff7e2ea67cf3fd05082893b359afa0/water-bodies/app-pkg-multiple/crop.cwl) (pinned commit `72a76ae`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval
- EOAP CWL custom types used: none; candidates: `eoap.cct.bbox`, `eoap.cct.stac`, `eoap.cct.string-format`
- Used by: `ospd.process-profiles.water-bodies.detect-water-body`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `item` | string | `cropped` | File |
| `aoi` | string |  |  |
| `epsg` | string |  |  |
| `band` | string |  |  |

## Analysis

**Behaviour.** `python -m app`, `ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0`.
Reads one asset of the given STAC item directly over the network (`NetworkAccess`; no `File`
input -- `item` is a plain STAC item URL string), windowed-reads the requested `band` cropped to
`aoi`, writes one GeoTIFF (`crop_<band>.tif`). It does not reproject: `epsg` is passed to
`gdal.Translate` as `projWinSRS`, the CRS of `aoi`, not a target CRS (read, `app.py`). Observed
(run record `water-bodies`, 2026-11-10): with `epsg: "EPSG:4326"`, the four `crop_*.tif` stay
in the CRS of the asset, EPSG:32610 (UTM zone 10N), at 10 m.

**CWL specifics.** `item`, `aoi`, `epsg`, `band` are all plain strings: `item` is a STAC Item
URL (candidate `eoap.cct.stac` or `eoap.cct.string-format`), `aoi` a comma-separated bbox
(candidate `eoap.cct.bbox`, but as one string, not the object EOAP's own BBox type expects).
`band` is an unconstrained string (`green`, `nir`, ...), not an enum: any STAC asset key the
item happens to expose is accepted, so an invalid band name fails only at execution.

**Provenance.** No input is a `File`: `aoi`/`epsg`/`item`/`band` are literal-valued entities;
the network fetch itself leaves no provenance trace beyond the output file (GP-3, GP-4).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the process's Application Package (`/processes/{id}/package`, OGC API - Processes - Part 2), the same plan as the process-type entry's own `plan` -- the plan as the engine's own CWLProv graph names it (its run-local `arcp:` copy in the research object) is given as a `prov:specializationOf` that Application Package --, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (ogc-eo-application-package-hands-on f472585 `water-bodies/app-pkg-multiple/water-bodies.cwl`, one CWL file per step), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main/node_crop` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## Implementation Profile (tier 3)

Implements [`Band retrieval`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval) (`generic-profiles.implementation-profile.band-retrieval`, bblocks-generic-profiles). Signature checked against band-retrieval: `item` (a STAC Item URL) implements `product`, by reference; `band` (a band common name) implements `band`; `aoi` and `epsg` (four numbers in one string, and their CRS) implement `areaOfInterest` as a role decomposition; `cropped` implements the output `raster`. It does not reproject: the output keeps the CRS of the asset.

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `item` | input `product` | `eo-product` |
| `band` | input `band` | `band-identifier` |
| `aoi`, `epsg` (role decomposition) | input `areaOfInterest` | `bounding-box` |
| `cropped` | output `raster` | `raster` |

**Role decomposition.** The input `areaOfInterest` is taken as `aoi`, `epsg`: The area of interest is taken as one string of four comma-separated numbers (`aoi`) and the identifier of their CRS (`epsg`, passed to gdal.Translate as `projWinSRS`), not as one OGC API - Processes bounding box: the representation bounding-box-ogcapi-processes-bbox of the role is not served. Declared in `roleDecompositions` of `process-type.json`; its representation is not served (`docs/FORMAT-CHECK.md`).

**By reference.** `item` (role `product`) is a URL of the data, not the data: The product is given as the URL of its STAC Item, a string, not as the STAC Item itself. Declared in `byReference` of `process-type.json` (`docs/FORMAT-CHECK.md`).

## openEO equivalence

**Level: closeMatch.** load_collection with a spatial_extent (aoi) and a single band selected (filter_bands); the STAC item is given by URL rather than resolved by collection/date/bbox search, and the windowed COG read (no full download) is an implementation detail openEO back-ends make transparently.

- `closeMatch`: `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands`

## Process type (Activity 4)

Registered ActivityType OWL class `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop` (`ospd.process-profiles.process-type`), proposed by GeoLabs and awaiting a register decision.

## Examples

### Source CWL (referenced)
The CWL CommandLineTool is referenced, not copied: <https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/72a76ae1d5ff7e2ea67cf3fd05082893b359afa0/water-bodies/app-pkg-multiple/crop.cwl>.

### processDescription
OGC API - Processes processDescription derived from the CWL.
#### json
```json
{
  "id": "crop",
  "version": "1.4.1",
  "title": "crop",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "crop"
    },
    {
      "role": "https://schema.org/description",
      "value": "Process converted from CWL"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.4.1"
    }
  ],
  "inputs": {
    "item": {
      "title": "item",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "aoi",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "epsg": {
      "title": "epsg",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "band": {
      "title": "band",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "cropped": {
      "title": "cropped",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "image/tiff; application=geotiff",
        "contentEncoding": "binary"
      }
    }
  },
  "jobControlOptions": [
    "async-execute"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/context.jsonld",
  "id": "crop",
  "version": "1.4.1",
  "title": "crop",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "crop"
    },
    {
      "role": "https://schema.org/description",
      "value": "Process converted from CWL"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.4.1"
    }
  ],
  "inputs": {
    "item": {
      "title": "item",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "aoi",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "epsg": {
      "title": "epsg",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "band": {
      "title": "band",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "cropped": {
      "title": "cropped",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "image/tiff; application=geotiff",
        "contentEncoding": "binary"
      }
    }
  },
  "jobControlOptions": [
    "async-execute"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ]
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
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/crop> dcterms:description "Process converted from CWL" ;
    dcterms:title "crop" ;
    pp:version "1.4.1" ;
    proc:inputs [ ns1:aoi [ dcterms:description "" ;
                    dcterms:title "aoi" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:band [ dcterms:description "" ;
                    dcterms:title "band" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:epsg [ dcterms:description "" ;
                    dcterms:title "epsg" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:item [ dcterms:description "" ;
                    dcterms:title "item" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "crop" ;
            proc:role schema:name ],
        [ rdf:value "Process converted from CWL" ;
            proc:role schema:description ],
        [ rdf:value "1.4.1" ;
            proc:role schema:softwareVersion ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:cropped [ dcterms:description "" ;
                    dcterms:title "cropped" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentEncoding "binary" ;
                            ns2:contentMediaType "image/tiff; application=geotiff" ] ] ] .


```


### processDescription with its inheritance (Implementation, instance level)
The same processDescription as OGC 14-065r1 Table 21 wants it at the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval`: the Implementation Profile's keywords (E) on the process and on each bound input/output, and, per footnote a, its list of metadata references to superior profiles extended with a Table 22 `implementation` reference to the Implementation Profile -- on the process only. Each bound input/output keeps its Implementation Profile counterpart's reference to the Generic Profile input/output (`generic-input`/`-output`) and adds one to that counterpart itself (`<Implementation Profile>/inputs/<name>`, `/outputs/<name>`, `implementation-input`/`-output`): roles defined by bblocks-generic-profiles, since Table 22 only names whole profiles. Each bound input/output also carries the `dataType` of that counterpart, a concept of bblocks-data-types. Which deployed input/output is which Implementation Profile one is `bindings` in scripts/profiles.yaml; inputs/outputs bound to none are the deployment's own additions (footnote b). `areaOfInterest` is taken as `aoi`, `epsg`, none of which is the role: declared in `roleDecompositions` of the process-type entry. Not what the deployment serves today (docs/OPEN-QUESTIONS.md Q-TABLE21-INSTANCE).
#### json
```json
{
  "id": "crop",
  "version": "1.4.1",
  "title": "crop",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "title": "Process Concept: Data Discovery and Access",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access"
    },
    {
      "title": "Generic Profile: Band retrieval",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval"
    },
    {
      "title": "Implementation Profile: Band retrieval",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval"
    },
    {
      "role": "https://schema.org/name",
      "value": "crop"
    },
    {
      "role": "https://schema.org/description",
      "value": "Process converted from CWL"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.4.1"
    }
  ],
  "jobControlOptions": [
    "async-execute"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ],
  "keywords": [
    "product",
    "band",
    "retrieval"
  ],
  "inputs": {
    "item": {
      "title": "item",
      "description": "",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product",
      "keywords": [
        "product"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Band retrieval -- input `product`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/product"
        },
        {
          "title": "Implementation Profile: Band retrieval -- input `product`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/product"
        }
      ],
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "aoi",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "epsg": {
      "title": "epsg",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "band": {
      "title": "band",
      "description": "",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier",
      "keywords": [
        "band"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Band retrieval -- input `band`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/band"
        },
        {
          "title": "Implementation Profile: Band retrieval -- input `band`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/band"
        }
      ],
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "cropped": {
      "title": "cropped",
      "description": "",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Band retrieval -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/outputs/raster"
        },
        {
          "title": "Implementation Profile: Band retrieval -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/outputs/raster"
        }
      ],
      "schema": {
        "type": "string",
        "contentMediaType": "image/tiff; application=geotiff",
        "contentEncoding": "binary"
      }
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/context.jsonld",
  "id": "crop",
  "version": "1.4.1",
  "title": "crop",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "title": "Process Concept: Data Discovery and Access",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access"
    },
    {
      "title": "Generic Profile: Band retrieval",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval"
    },
    {
      "title": "Implementation Profile: Band retrieval",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval"
    },
    {
      "role": "https://schema.org/name",
      "value": "crop"
    },
    {
      "role": "https://schema.org/description",
      "value": "Process converted from CWL"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.4.1"
    }
  ],
  "jobControlOptions": [
    "async-execute"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ],
  "keywords": [
    "product",
    "band",
    "retrieval"
  ],
  "inputs": {
    "item": {
      "title": "item",
      "description": "",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product",
      "keywords": [
        "product"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Band retrieval -- input `product`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/product"
        },
        {
          "title": "Implementation Profile: Band retrieval -- input `product`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/product"
        }
      ],
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "aoi",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "epsg": {
      "title": "epsg",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "band": {
      "title": "band",
      "description": "",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier",
      "keywords": [
        "band"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Band retrieval -- input `band`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/band"
        },
        {
          "title": "Implementation Profile: Band retrieval -- input `band`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/band"
        }
      ],
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "cropped": {
      "title": "cropped",
      "description": "",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Band retrieval -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/outputs/raster"
        },
        {
          "title": "Implementation Profile: Band retrieval -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/outputs/raster"
        }
      ],
      "schema": {
        "type": "string",
        "contentMediaType": "image/tiff; application=geotiff",
        "contentEncoding": "binary"
      }
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns3: <https://w3id.org/ogc/api/schema/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/crop> dcterms:description "Process converted from CWL" ;
    dcterms:subject "band",
        "product",
        "retrieval" ;
    dcterms:title "crop" ;
    pp:version "1.4.1" ;
    proc:inputs [ ns1:aoi [ dcterms:description "" ;
                    dcterms:title "aoi" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:band [ dcterms:description "" ;
                    dcterms:title "band" ;
                    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier> ;
                    proc:keywords "band" ;
                    proc:maxOccurs 1 ;
                    proc:metadata [ dcterms:title "Implementation Profile: Band retrieval -- input `band`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/band> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ],
                        [ dcterms:title "Generic Profile: Band retrieval -- input `band`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/band> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:epsg [ dcterms:description "" ;
                    dcterms:title "epsg" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:item [ dcterms:description "" ;
                    dcterms:title "item" ;
                    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product> ;
                    proc:keywords "product" ;
                    proc:maxOccurs 1 ;
                    proc:metadata [ dcterms:title "Implementation Profile: Band retrieval -- input `product`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/product> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input> ],
                        [ dcterms:title "Generic Profile: Band retrieval -- input `product`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/product> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "crop" ;
            proc:role schema:name ],
        [ rdf:value "1.4.1" ;
            proc:role schema:softwareVersion ],
        [ dcterms:title "Implementation Profile: Band retrieval" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation> ],
        [ dcterms:title "Generic Profile: Band retrieval" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "Process Concept: Data Discovery and Access" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ rdf:value "Process converted from CWL" ;
            proc:role schema:description ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns2:cropped [ dcterms:description "" ;
                    dcterms:title "cropped" ;
                    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/raster> ;
                    proc:keywords "raster" ;
                    proc:metadata [ dcterms:title "Generic Profile: Band retrieval -- output `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/outputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ],
                        [ dcterms:title "Implementation Profile: Band retrieval -- output `raster`" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/outputs/raster> ;
                            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output> ] ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/tiff; application=geotiff" ] ] ] .


```


### OGC Application Package (deploy)
Part 2 deploy body: the execution unit is a link to the pinned CWL.
#### json
```json
{
  "processDescription": {
    "process": {
      "id": "crop",
      "version": "1.4.1"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/72a76ae1d5ff7e2ea67cf3fd05082893b359afa0/water-bodies/app-pkg-multiple/crop.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/context.jsonld",
  "processDescription": {
    "process": {
      "id": "crop",
      "version": "1.4.1"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/72a76ae1d5ff7e2ea67cf3fd05082893b359afa0/water-bodies/app-pkg-multiple/crop.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/crop> pp:version "1.4.1" .

[] pp:processDescription [ pp:process <https://geolabs.github.io/bblocks-process-profiles/def/process/crop> ] ;
    proc:executionUnit [ dcterms:format "application/cwl+yaml" ;
            ns1:relation <http://www.opengis.net/def/rel/ogc/1.0/executionUnit> ;
            oa:hasTarget <https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/72a76ae1d5ff7e2ea67cf3fd05082893b359afa0/water-bodies/app-pkg-multiple/crop.cwl> ] .


```


### Execute request
#### json
```json
{
  "inputs": {
    "item": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A",
    "aoi": "-121.399,39.834,-120.74,40.472",
    "epsg": "EPSG:4326",
    "band": "green"
  },
  "response": "document"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/context.jsonld",
  "inputs": {
    "item": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A",
    "aoi": "-121.399,39.834,-120.74,40.472",
    "epsg": "EPSG:4326",
    "band": "green"
  },
  "response": "document"
}
```

#### ttl
```ttl
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

[] proc:inputs [ ns1:aoi "-121.399,39.834,-120.74,40.472" ;
            ns1:band "green" ;
            ns1:epsg "EPSG:4326" ;
            ns1:item "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A" ] ;
    proc:response "document" .


```


### Results
#### json
```json
{
  "cropped": {
    "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-crop-0001/results/crop_green.tif",
    "type": "image/tiff; application=geotiff"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/context.jsonld",
  "cropped": {
    "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-crop-0001/results/crop_green.tif",
    "type": "image/tiff; application=geotiff"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .

[] pp:cropped [ pp:href "https://ospd.example.org/ogc-api/jobs/water-bodies-crop-0001/results/crop_green.tif" ] .


```


### Provenance view (generic provenance profile)
W3C PROV chain validated against `ogc.bbr.provenance.provenance`.
#### json
```json
[
  {
    "id": "urn:example:run:water-bodies:crop",
    "provType": "prov:Activity",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop",
    "startedAtTime": "2026-09-23T20:09:38Z",
    "used": [
      "urn:example:entity:crop:in:item",
      "urn:example:entity:crop:in:aoi",
      "urn:example:entity:crop:in:epsg",
      "urn:example:entity:crop:in:band"
    ],
    "wasAssociatedWith": [
      "urn:example:engine:cwltool-3.1.20260108082145",
      "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
    ],
    "qualifiedAssociation": [
      {
        "agent": "urn:example:engine:cwltool-3.1.20260108082145",
        "hadPlan": "https://ospd.example.org/ogc-api/processes/crop/package"
      }
    ],
    "endedAtTime": "2026-09-23T20:11:25Z"
  },
  {
    "id": "urn:example:entity:crop:in:item",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/crop#inputs/item",
    "value": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A"
  },
  {
    "id": "urn:example:entity:crop:in:aoi",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/crop#inputs/aoi",
    "value": "-121.399,39.834,-120.74,40.472"
  },
  {
    "id": "urn:example:entity:crop:in:epsg",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/crop#inputs/epsg",
    "value": "EPSG:4326"
  },
  {
    "id": "urn:example:entity:crop:in:band",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/crop#inputs/band",
    "value": "green"
  },
  {
    "id": "urn:example:entity:crop:out:cropped",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/crop#outputs/cropped",
    "wasGeneratedBy": "urn:example:run:water-bodies:crop",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-crop-0001/results/crop_green.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:engine:cwltool-3.1.20260108082145",
    "provType": "prov:SoftwareAgent",
    "name": "cwltool 3.1.20260108082145"
  },
  {
    "id": "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0",
    "provType": "prov:SoftwareAgent",
    "name": "container image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
  },
  {
    "id": "https://ospd.example.org/ogc-api/processes/crop/package",
    "provType": "prov:Plan"
  },
  {
    "id": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop",
    "provType": "prov:Plan",
    "specializationOf": "https://ospd.example.org/ogc-api/processes/crop/package"
  }
]

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/context.jsonld",
  "@graph": [
    {
      "id": "urn:example:run:water-bodies:crop",
      "provType": "prov:Activity",
      "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop",
      "startedAtTime": "2026-09-23T20:09:38Z",
      "used": [
        "urn:example:entity:crop:in:item",
        "urn:example:entity:crop:in:aoi",
        "urn:example:entity:crop:in:epsg",
        "urn:example:entity:crop:in:band"
      ],
      "wasAssociatedWith": [
        "urn:example:engine:cwltool-3.1.20260108082145",
        "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
      ],
      "qualifiedAssociation": [
        {
          "agent": "urn:example:engine:cwltool-3.1.20260108082145",
          "hadPlan": "https://ospd.example.org/ogc-api/processes/crop/package"
        }
      ],
      "endedAtTime": "2026-09-23T20:11:25Z"
    },
    {
      "id": "urn:example:entity:crop:in:item",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/crop#inputs/item",
      "value": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A"
    },
    {
      "id": "urn:example:entity:crop:in:aoi",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/crop#inputs/aoi",
      "value": "-121.399,39.834,-120.74,40.472"
    },
    {
      "id": "urn:example:entity:crop:in:epsg",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/crop#inputs/epsg",
      "value": "EPSG:4326"
    },
    {
      "id": "urn:example:entity:crop:in:band",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/crop#inputs/band",
      "value": "green"
    },
    {
      "id": "urn:example:entity:crop:out:cropped",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/crop#outputs/cropped",
      "wasGeneratedBy": "urn:example:run:water-bodies:crop",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-crop-0001/results/crop_green.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:engine:cwltool-3.1.20260108082145",
      "provType": "prov:SoftwareAgent",
      "name": "cwltool 3.1.20260108082145"
    },
    {
      "id": "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0",
      "provType": "prov:SoftwareAgent",
      "name": "container image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
    },
    {
      "id": "https://ospd.example.org/ogc-api/processes/crop/package",
      "provType": "prov:Plan"
    },
    {
      "id": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop",
      "provType": "prov:Plan",
      "specializationOf": "https://ospd.example.org/ogc-api/processes/crop/package"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop> a prov:Plan ;
    prov:specializationOf <https://ospd.example.org/ogc-api/processes/crop/package> .

<urn:example:entity:crop:out:cropped> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/crop#outputs/cropped> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/water-bodies-crop-0001/results/crop_green.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:water-bodies:crop> .

<urn:example:entity:crop:in:aoi> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/crop#inputs/aoi> ;
    rdf:value "-121.399,39.834,-120.74,40.472" .

<urn:example:entity:crop:in:band> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/crop#inputs/band> ;
    rdf:value "green" .

<urn:example:entity:crop:in:epsg> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/crop#inputs/epsg> ;
    rdf:value "EPSG:4326" .

<urn:example:entity:crop:in:item> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/crop#inputs/item> ;
    rdf:value "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A" .

<urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0> a prov:SoftwareAgent ;
    pp:name "container image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0" .

<urn:example:run:water-bodies:crop> a prov:Activity,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    prov:endedAtTime "2026-09-23T20:11:25+00:00"^^xsd:dateTime ;
    prov:qualifiedAssociation [ prov:agent <urn:example:engine:cwltool-3.1.20260108082145> ;
            prov:hadPlan <https://ospd.example.org/ogc-api/processes/crop/package> ] ;
    prov:startedAtTime "2026-09-23T20:09:38+00:00"^^xsd:dateTime ;
    prov:used <urn:example:entity:crop:in:aoi>,
        <urn:example:entity:crop:in:band>,
        <urn:example:entity:crop:in:epsg>,
        <urn:example:entity:crop:in:item> ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145>,
        <urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0> .

<https://ospd.example.org/ogc-api/processes/crop/package> a prov:Plan .

<urn:example:engine:cwltool-3.1.20260108082145> a prov:SoftwareAgent ;
    pp:name "cwltool 3.1.20260108082145" .


```


### Process run (wfprov:ProcessRun, gap GP-1)
#### json
```json
{
  "id": "urn:example:run:water-bodies:crop",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/crop/package",
  "usedInput": [
    {
      "id": "urn:example:entity:crop:in:item"
    },
    {
      "id": "urn:example:entity:crop:in:aoi"
    },
    {
      "id": "urn:example:entity:crop:in:epsg"
    },
    {
      "id": "urn:example:entity:crop:in:band"
    }
  ],
  "startedAtTime": "2026-09-23T20:09:38Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:water-bodies:detect-water-body"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/context.jsonld",
  "id": "urn:example:run:water-bodies:crop",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/crop/package",
  "usedInput": [
    {
      "id": "urn:example:entity:crop:in:item"
    },
    {
      "id": "urn:example:entity:crop:in:aoi"
    },
    {
      "id": "urn:example:entity:crop:in:epsg"
    },
    {
      "id": "urn:example:entity:crop:in:band"
    }
  ],
  "startedAtTime": "2026-09-23T20:09:38Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:water-bodies:detect-water-body"
}
```

#### ttl
```ttl
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:example:run:water-bodies:crop> a wfprov:ProcessRun,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    wfprov:describedByProcess <https://ospd.example.org/ogc-api/processes/crop/package> ;
    wfprov:usedInput <urn:example:entity:crop:in:aoi>,
        <urn:example:entity:crop:in:band>,
        <urn:example:entity:crop:in:epsg>,
        <urn:example:entity:crop:in:item> ;
    wfprov:wasPartOfWorkflowRun <urn:example:run:water-bodies:detect-water-body> ;
    prov:startedAtTime "2026-09-23T20:09:38+00:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> .


```


### Process-type register entry (Activity 4)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/tier3-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Attached to the Implementation Profile https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval (implementsProfile), after checking its signature (docs/ATTACHMENTS.md).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/definition-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "definition: \"Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item, cropped to the area of interest and reprojected to the requested CRS.\" -> \"Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item, cropped to the area of interest, whose CRS is given by `epsg`; the output keeps the CRS of the asset.\" The tool does not reproject: epsg is passed to gdal.Translate as projWinSRS, the CRS of aoi (read, app.py), and the four crop_*.tif of the run record water-bodies stay in EPSG:32610 (observed 2026-11-10). Substantive: it changes what the item means.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/inherited-description-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "processDescription.inherited.json added with the attachment to the Implementation Profile band-retrieval: the deployed processDescription with each bound input and output linked to the role it implements (metadata, role implementation-input or implementation-output) and carrying that role's dataType; the profile schema inherits it. The deployed processDescription is unchanged.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/by-reference-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "byReference added: the input item implements the role product of band-retrieval as the URL of a STAC Item, not the Item itself (decision C1 of 2026-11-10).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/role-decompositions-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "roleDecompositions added: the role areaOfInterest of band-retrieval is taken as the two inputs aoi (four numbers in one string) and epsg (their CRS), neither of which carries its representation.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/plan-2026-11-11",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "plan: executionUnit.href moves from GeoLabs/ogc-eo-application-package-hands-on f472585 to 72a76ae, pushed on 2026-11-11 (water-bodies/app-pkg-multiple/crop.cwl). The 72a76ae CWL declares the format of its Files, so the processDescription derived from it changes: contentMediaType application/octet-stream -> image/tiff; application=geotiff (with contentEncoding binary) for the output cropped, in processDescription.json and processDescription.inherited.json. The assumedFormatGaps recorded at the attachment on 2026-11-10 for cropped were removed the same day, when the corrected CWL served these formats; the entry has none.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-11T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    }
  ],
  "prefLabel": "Crop a Sentinel-2 COG band to an area of interest",
  "definition": "Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item, cropped to the area of interest, whose CRS is given by `epsg`; the output keeps the CRS of the asset.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.water-bodies.crop",
    "processDescription": {
      "id": "crop",
      "version": "1.4.1",
      "href": "https://ospd.example.org/ogc-api/processes/crop"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/crop/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/72a76ae1d5ff7e2ea67cf3fd05082893b359afa0/water-bodies/app-pkg-multiple/crop.cwl",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "crop",
    "license": "https://spdx.org/licenses/CC-BY-SA-4.0",
    "cctDependencies": [],
    "candidateCctDependencies": [
      "eoap.cct.bbox",
      "eoap.cct.stac",
      "eoap.cct.string-format"
    ]
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval",
  "byReference": [
    {
      "name": "item",
      "side": "inputs",
      "implements": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/product",
      "note": "The product is given as the URL of its STAC Item, a string, not as the STAC Item itself."
    }
  ],
  "roleDecompositions": [
    {
      "side": "inputs",
      "implements": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/areaOfInterest",
      "parts": [
        "aoi",
        "epsg"
      ],
      "note": "The area of interest is taken as one string of four comma-separated numbers (`aoi`) and the identifier of their CRS (`epsg`, passed to gdal.Translate as `projWinSRS`), not as one OGC API - Processes bounding box: the representation bounding-box-ogcapi-processes-bbox of the role is not served."
    }
  ],
  "correspondences": {
    "closeMatch": [
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.load_collection",
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.filter_bands"
    ],
    "openeoEquivalence": {
      "level": "closeMatch",
      "rationale": "load_collection with a spatial_extent (aoi) and a single band selected (filter_bands); the STAC item is given by URL rather than resolved by collection/date/bbox search, and the windowed COG read (no full download) is an implementation detail openEO back-ends make transparently."
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/tier3-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Attached to the Implementation Profile https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval (implementsProfile), after checking its signature (docs/ATTACHMENTS.md).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/definition-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "definition: \"Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item, cropped to the area of interest and reprojected to the requested CRS.\" -> \"Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item, cropped to the area of interest, whose CRS is given by `epsg`; the output keeps the CRS of the asset.\" The tool does not reproject: epsg is passed to gdal.Translate as projWinSRS, the CRS of aoi (read, app.py), and the four crop_*.tif of the run record water-bodies stay in EPSG:32610 (observed 2026-11-10). Substantive: it changes what the item means.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/inherited-description-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "processDescription.inherited.json added with the attachment to the Implementation Profile band-retrieval: the deployed processDescription with each bound input and output linked to the role it implements (metadata, role implementation-input or implementation-output) and carrying that role's dataType; the profile schema inherits it. The deployed processDescription is unchanged.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/by-reference-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "byReference added: the input item implements the role product of band-retrieval as the URL of a STAC Item, not the Item itself (decision C1 of 2026-11-10).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/role-decompositions-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "roleDecompositions added: the role areaOfInterest of band-retrieval is taken as the two inputs aoi (four numbers in one string) and epsg (their CRS), neither of which carries its representation.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/plan-2026-11-11",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "plan: executionUnit.href moves from GeoLabs/ogc-eo-application-package-hands-on f472585 to 72a76ae, pushed on 2026-11-11 (water-bodies/app-pkg-multiple/crop.cwl). The 72a76ae CWL declares the format of its Files, so the processDescription derived from it changes: contentMediaType application/octet-stream -> image/tiff; application=geotiff (with contentEncoding binary) for the output cropped, in processDescription.json and processDescription.inherited.json. The assumedFormatGaps recorded at the attachment on 2026-11-10 for cropped were removed the same day, when the corrected CWL served these formats; the entry has none.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-11T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"
    }
  ],
  "prefLabel": "Crop a Sentinel-2 COG band to an area of interest",
  "definition": "Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item, cropped to the area of interest, whose CRS is given by `epsg`; the output keeps the CRS of the asset.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.water-bodies.crop",
    "processDescription": {
      "id": "crop",
      "version": "1.4.1",
      "href": "https://ospd.example.org/ogc-api/processes/crop"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/crop/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/72a76ae1d5ff7e2ea67cf3fd05082893b359afa0/water-bodies/app-pkg-multiple/crop.cwl",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "crop",
    "license": "https://spdx.org/licenses/CC-BY-SA-4.0",
    "cctDependencies": [],
    "candidateCctDependencies": [
      "eoap.cct.bbox",
      "eoap.cct.stac",
      "eoap.cct.string-format"
    ]
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval",
  "byReference": [
    {
      "name": "item",
      "side": "inputs",
      "implements": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/product",
      "note": "The product is given as the URL of its STAC Item, a string, not as the STAC Item itself."
    }
  ],
  "roleDecompositions": [
    {
      "side": "inputs",
      "implements": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/areaOfInterest",
      "parts": [
        "aoi",
        "epsg"
      ],
      "note": "The area of interest is taken as one string of four comma-separated numbers (`aoi`) and the identifier of their CRS (`epsg`, passed to gdal.Translate as `projWinSRS`), not as one OGC API - Processes bounding box: the representation bounding-box-ogcapi-processes-bbox of the role is not served."
    }
  ],
  "correspondences": {
    "closeMatch": [
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.load_collection",
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.filter_bands"
    ],
    "openeoEquivalence": {
      "level": "closeMatch",
      "rationale": "load_collection with a spatial_extent (aoi) and a single band selected (filter_bands); the STAC item is given by URL rather than resolved by collection/date/bbox search, and the windowed COG read (no full download) is an implementation detail openEO back-ends make transparently."
    }
  }
}
```

#### ttl
```ttl
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-22T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/by-reference-2026-11-10> a rim:RegisterAction ;
    dcterms:description "byReference added: the input item implements the role product of band-retrieval as the URL of a STAC Item, not the Item itself (decision C1 of 2026-11-10)." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/d5-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/definition-2026-11-10> a rim:RegisterAction ;
    dcterms:description "definition: \"Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item, cropped to the area of interest and reprojected to the requested CRS.\" -> \"Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item, cropped to the area of interest, whose CRS is given by `epsg`; the output keeps the CRS of the asset.\" The tool does not reproject: epsg is passed to gdal.Translate as projWinSRS, the CRS of aoi (read, app.py), and the four crop_*.tif of the run record water-bodies stay in EPSG:32610 (observed 2026-11-10). Substantive: it changes what the item means." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/inherited-description-2026-11-10> a rim:RegisterAction ;
    dcterms:description "processDescription.inherited.json added with the attachment to the Implementation Profile band-retrieval: the deployed processDescription with each bound input and output linked to the role it implements (metadata, role implementation-input or implementation-output) and carrying that role's dataType; the profile schema inherits it. The deployed processDescription is unchanged." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/plan-2026-11-11> a rim:RegisterAction ;
    dcterms:description "plan: executionUnit.href moves from GeoLabs/ogc-eo-application-package-hands-on f472585 to 72a76ae, pushed on 2026-11-11 (water-bodies/app-pkg-multiple/crop.cwl). The 72a76ae CWL declares the format of its Files, so the processDescription derived from it changes: contentMediaType application/octet-stream -> image/tiff; application=geotiff (with contentEncoding binary) for the output cropped, in processDescription.json and processDescription.inherited.json. The assumedFormatGaps recorded at the attachment on 2026-11-10 for cropped were removed the same day, when the corrected CWL served these formats; the entry has none." ;
    prov:startedAtTime "2026-11-11T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/role-decompositions-2026-11-10> a rim:RegisterAction ;
    dcterms:description "roleDecompositions added: the role areaOfInterest of band-retrieval is taken as the two inputs aoi (four numbers in one string) and epsg (their CRS), neither of which carries its representation." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/specialisation-2026-11-10> a rim:RegisterAction ;
    dcterms:description "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/tier3-2026-11-10> a rim:RegisterAction ;
    dcterms:description "Attached to the Implementation Profile https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval (implementsProfile), after checking its signature (docs/ATTACHMENTS.md)." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process/crop> rdfs:seeAlso <https://ospd.example.org/ogc-api/processes/crop> ;
    pp:version "1.4.1" .

<https://ospd.example.org/ogc-api/processes/crop/package> a prov:Plan ;
    dcterms:license <https://spdx.org/licenses/CC-BY-SA-4.0> ;
    pp:candidateCctDependency "eoap.cct.bbox",
        "eoap.cct.stac",
        "eoap.cct.string-format" ;
    pp:cwlClass "CommandLineTool" ;
    pp:cwlId "crop" ;
    proc:executionUnit [ dcterms:format "application/cwl+yaml" ;
            ns1:relation <http://www.opengis.net/def/rel/ogc/1.0/executionUnit> ;
            oa:hasTarget <https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/72a76ae1d5ff7e2ea67cf3fd05082893b359afa0/water-bodies/app-pkg-multiple/crop.cwl> ] .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop> a owl:Class,
        pp:ProcessType,
        acttype:ActivityType ;
    rdfs:subClassOf <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.filter_bands>,
        <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.load_collection> ;
    skos:definition "Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item, cropped to the area of interest, whose CRS is given by `epsg`; the output keeps the CRS of the asset." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Crop a Sentinel-2 COG band to an area of interest" ;
    pp:byReference [ skos:note "The product is given as the URL of its STAC Item, a string, not as the STAC Item itself." ;
            pp:implements <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/product> ;
            pp:liveName "item" ;
            pp:side "inputs" ] ;
    pp:deployment [ pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/crop> ;
            pp:profile "ospd.process-profiles.water-bodies.crop" ;
            pp:provenanceClass wfprov:ProcessRun ] ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "load_collection with a spatial_extent (aoi) and a single band selected (filter_bands); the STAC item is given by URL rather than resolved by collection/date/bbox search, and the windowed COG read (no full download) is an implementation detail openEO back-ends make transparently." ] ;
    pp:phase <https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval> ;
    pp:plan <https://ospd.example.org/ogc-api/processes/crop/package> ;
    pp:roleDecomposition [ skos:note "The area of interest is taken as one string of four comma-separated numbers (`aoi`) and the identifier of their CRS (`epsg`, passed to gdal.Translate as `projWinSRS`), not as one OGC API - Processes bounding box: the representation bounding-box-ogcapi-processes-bbox of the role is not served." ;
            pp:implements <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/areaOfInterest> ;
            pp:part ( "aoi" "epsg" ) ;
            pp:side "inputs" ] ;
    acttype:generatedEntityType geo:Feature ;
    acttype:usedEntityType geo:Feature ;
    rim:hasAction <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/addition>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/by-reference-2026-11-10>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/d5-2026-11-09>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/definition-2026-11-10>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/inherited-description-2026-11-10>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/plan-2026-11-11>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/role-decompositions-2026-11-10>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/specialisation-2026-11-10>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop/actions/tier3-2026-11-10> ;
    rim:inRegister pp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```


### Run record, W3C PROV-JSONLD (cwltool CWLProv bundle)
The CWLProv bundle of the run record that holds this profile's activity, re-serialised as PROV-JSONLD by the `prov` library (mentions of nested bundles rewritten as `specializationOf` + `prov:asInBundle`, see that block's notes), validated against `ogc.ogc-utils.prov.w3c-prov-jsonld` and read as RDF through its own context: the PROV-O graph here is the engine's, not this register's provenance view.
#### jsonld
```jsonld
{
  "@context": [
    {
      "wfprov": "http://purl.org/wf4ever/wfprov#",
      "wfdesc": "http://purl.org/wf4ever/wfdesc#",
      "cwlprov": "https://w3id.org/cwl/prov#",
      "foaf": "http://xmlns.com/foaf/0.1/",
      "schema": "http://schema.org/",
      "orcid": "https://orcid.org/",
      "id": "urn:uuid:",
      "data": "urn:hash::sha1:",
      "sha256": "nih:sha-256;",
      "researchobject": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/",
      "metadata": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/",
      "provenance": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/provenance/",
      "wf": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#",
      "input": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/primary-job.json#",
      "wf4ever": "http://purl.org/wf4ever/wf4ever#"
    },
    "https://openprovenance.org/prov-jsonld/context.jsonld"
  ],
  "@graph": [
    {
      "@type": "Agent",
      "@id": "id:1851e03b-b5dd-458e-b892-800c846451b6"
    },
    {
      "@type": "Agent",
      "@id": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "type": [
        "prov:SoftwareAgent",
        "wfprov:WorkflowEngine"
      ],
      "label": [
        {
          "@value": "cwltool 3.1.20260108082145"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:8bbef2fa-3721-4f50-b27c-1d641100a89f",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:c2b78598-db7e-4ab3-89eb-621c7b5c9bd6",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:87ca5fb7-8991-4f4e-b107-8b30f9be5eea",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:887634a3-fcfa-4422-aaa1-8949fd8db10b",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0"
        }
      ]
    },
    {
      "@type": "Start",
      "activity": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "starter": "id:1851e03b-b5dd-458e-b892-800c846451b6",
      "time": "2026-09-23T22:09:36.483674"
    },
    {
      "@type": "Start",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "starter": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "time": "2026-09-23T22:09:36.483742"
    },
    {
      "@type": "Start",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "starter": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:09:38.001367"
    },
    {
      "@type": "Start",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "starter": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:11:25.771051"
    },
    {
      "@type": "Start",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "starter": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:14.484903"
    },
    {
      "@type": "Start",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "starter": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:35.950035"
    },
    {
      "@type": "Activity",
      "@id": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "startTime": "2026-09-23T22:09:36.483701",
      "type": [
        "wfprov:WorkflowRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/node_crop"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/node_crop_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/node_normalized_difference"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/node_otsu"
        }
      ]
    },
    {
      "@type": "Association",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main"
    },
    {
      "@type": "Association",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/node_crop"
    },
    {
      "@type": "Association",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "agent": "id:8bbef2fa-3721-4f50-b27c-1d641100a89f"
    },
    {
      "@type": "Association",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/node_crop_2"
    },
    {
      "@type": "Association",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "agent": "id:c2b78598-db7e-4ab3-89eb-621c7b5c9bd6"
    },
    {
      "@type": "Association",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/node_normalized_difference"
    },
    {
      "@type": "Association",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "agent": "id:87ca5fb7-8991-4f4e-b107-8b30f9be5eea"
    },
    {
      "@type": "Association",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/node_otsu"
    },
    {
      "@type": "Association",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "agent": "id:887634a3-fcfa-4422-aaa1-8949fd8db10b"
    },
    {
      "@type": "Entity",
      "@id": "wf:main",
      "type": [
        "wfdesc:Workflow",
        "prov:Plan"
      ],
      "label": [
        {
          "@value": "Prospective provenance"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main",
      "wfdesc:hasSubProcess": [
        {
          "@value": "wf:main/node_crop",
          "@type": "xsd:QName"
        }
      ],
      "label": [
        {
          "@value": "Prospective provenance"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main",
      "wfdesc:hasSubProcess": [
        {
          "@value": "wf:main/node_normalized_difference",
          "@type": "xsd:QName"
        }
      ],
      "label": [
        {
          "@value": "Prospective provenance"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main",
      "wfdesc:hasSubProcess": [
        {
          "@value": "wf:main/node_otsu",
          "@type": "xsd:QName"
        }
      ],
      "label": [
        {
          "@value": "Prospective provenance"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/node_crop",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/node_normalized_difference",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/node_otsu",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "-121.399,39.834,-120.74,40.472"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "-121.399,39.834,-120.74,40.472"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "-121.399,39.834,-120.74,40.472"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "green"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "green"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "nir"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "nir"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:1f7549f8-4403-44f2-a435-f95a32edb9de",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "EPSG:4326"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "EPSG:4326"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "EPSG:4326"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:69255dfb77442b710fb7caf4fe2c555a8a8ca404",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "crop_green.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "crop_green"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:2d6eb0dc351bd77d3f5b06672ed012ef5dec508f",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:42580139-e758-4dbe-8ca8-7a114f7abf7f",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "crop_nir.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "crop_nir"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:eb53f504-eecb-4585-8e33-f7afdbbf816a",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ea91fcdd6f24b5105718011ca77810e4b6763c09",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:740c294a-a5f9-49be-b685-970f3eec0666",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "norm_diff.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "norm_diff"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:8cb131413518c30be6ba485ea61764491444cde5",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "otsu.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "otsu"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tif"
        }
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "entity": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "time": "2026-09-23T22:09:37.997833",
      "role": [
        "wf:main/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "entity": "id:1f7549f8-4403-44f2-a435-f95a32edb9de",
      "time": "2026-09-23T22:09:37.998964",
      "role": [
        "wf:main/bands"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "entity": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "time": "2026-09-23T22:09:37.999442",
      "role": [
        "wf:main/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "entity": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "time": "2026-09-23T22:09:38.074291",
      "role": [
        "wf:main/node_crop/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "entity": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c",
      "time": "2026-09-23T22:09:38.074835",
      "role": [
        "wf:main/node_crop/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "entity": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "time": "2026-09-23T22:09:38.075291",
      "role": [
        "wf:main/node_crop/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "entity": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2",
      "time": "2026-09-23T22:09:38.075873",
      "role": [
        "wf:main/node_crop/item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "entity": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "time": "2026-09-23T22:11:25.786582",
      "role": [
        "wf:main/node_crop_2/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "entity": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd",
      "time": "2026-09-23T22:11:25.787372",
      "role": [
        "wf:main/node_crop_2/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "entity": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "time": "2026-09-23T22:11:25.787927",
      "role": [
        "wf:main/node_crop_2/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "entity": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2",
      "time": "2026-09-23T22:11:25.788461",
      "role": [
        "wf:main/node_crop_2/item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "entity": "id:eb53f504-eecb-4585-8e33-f7afdbbf816a",
      "time": "2026-09-23T22:14:14.589864",
      "role": [
        "wf:main/node_normalized_difference/rasters"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "entity": "id:740c294a-a5f9-49be-b685-970f3eec0666",
      "time": "2026-09-23T22:14:36.026698",
      "role": [
        "wf:main/node_otsu/raster"
      ]
    },
    {
      "@type": "Membership",
      "collection": "id:1f7549f8-4403-44f2-a435-f95a32edb9de",
      "entity": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c"
    },
    {
      "@type": "Membership",
      "collection": "id:1f7549f8-4403-44f2-a435-f95a32edb9de",
      "entity": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd"
    },
    {
      "@type": "Membership",
      "collection": "id:eb53f504-eecb-4585-8e33-f7afdbbf816a",
      "entity": "id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e"
    },
    {
      "@type": "Membership",
      "collection": "id:eb53f504-eecb-4585-8e33-f7afdbbf816a",
      "entity": "id:42580139-e758-4dbe-8ca8-7a114f7abf7f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e",
      "generalEntity": "data:69255dfb77442b710fb7caf4fe2c555a8a8ca404"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:42580139-e758-4dbe-8ca8-7a114f7abf7f",
      "generalEntity": "data:2d6eb0dc351bd77d3f5b06672ed012ef5dec508f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:740c294a-a5f9-49be-b685-970f3eec0666",
      "generalEntity": "data:ea91fcdd6f24b5105718011ca77810e4b6763c09"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019",
      "generalEntity": "data:8cb131413518c30be6ba485ea61764491444cde5"
    },
    {
      "@type": "Generation",
      "entity": "id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "time": "2026-09-23T22:11:25.695199",
      "role": [
        "wf:main/node_crop/cropped"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:42580139-e758-4dbe-8ca8-7a114f7abf7f",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "time": "2026-09-23T22:14:14.382819",
      "role": [
        "wf:main/node_crop_2/cropped"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:740c294a-a5f9-49be-b685-970f3eec0666",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "time": "2026-09-23T22:14:35.757198",
      "role": [
        "wf:main/node_normalized_difference/ndwi"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "time": "2026-09-23T22:14:43.705762",
      "role": [
        "wf:main/node_otsu/binary_mask_item"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:43.709003",
      "role": [
        "wf:main/workflow%20node_water_bodies/detected_water_body"
      ]
    },
    {
      "@type": "End",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "ender": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:11:25.695175"
    },
    {
      "@type": "End",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "ender": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:14.382774"
    },
    {
      "@type": "End",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "ender": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:35.757176"
    },
    {
      "@type": "End",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "ender": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:43.705752"
    },
    {
      "@type": "End",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "ender": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "time": "2026-09-23T22:14:43.709126"
    }
  ]
}
```

#### ttl
```ttl
@prefix cwlprov: <https://w3id.org/cwl/prov#> .
@prefix data: <urn:hash::sha1:> .
@prefix id: <urn:uuid:> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix provext: <https://openprovenance.org/ns/provext#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix wf: <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#> .
@prefix wf4ever: <http://purl.org/wf4ever/wf4ever#> .
@prefix wfdesc: <http://purl.org/wf4ever/wfdesc#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

id:5fa19808-d14c-4c01-8bd1-05a7a8845019 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ;
            prov:atTime "2026-09-23T22:14:43.709003"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/workflow%20node_water_bodies/detected_water_body> ],
        [ a prov:Generation ;
            prov:activity id:6d7920a6-ee35-4701-88be-68838b9ba10b ;
            prov:atTime "2026-09-23T22:14:43.705762"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_otsu/binary_mask_item> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:8cb131413518c30be6ba485ea61764491444cde5 ] ;
    cwlprov:basename "otsu.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "otsu" .

wf:main a wfdesc:Workflow,
        prov:Entity,
        prov:Plan ;
    rdfs:label "Prospective provenance" ;
    wfdesc:hasSubProcess "wf:main/node_crop"^^xsd:QName,
        "wf:main/node_normalized_difference"^^xsd:QName,
        "wf:main/node_otsu"^^xsd:QName .

<arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_normalized_difference> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_otsu> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

data:2d6eb0dc351bd77d3f5b06672ed012ef5dec508f a wfprov:Artifact,
        prov:Entity .

data:69255dfb77442b710fb7caf4fe2c555a8a8ca404 a wfprov:Artifact,
        prov:Entity .

data:8cb131413518c30be6ba485ea61764491444cde5 a wfprov:Artifact,
        prov:Entity .

data:ea91fcdd6f24b5105718011ca77810e4b6763c09 a wfprov:Artifact,
        prov:Entity .

id:1851e03b-b5dd-458e-b892-800c846451b6 a prov:Agent .

id:1f7549f8-4403-44f2-a435-f95a32edb9de a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c ],
        [ a provext:Membership ;
            provext:member data:ba936cb0e062bea4078e8b56371ca8fe054093dd ] .

id:42580139-e758-4dbe-8ca8-7a114f7abf7f a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5 ;
            prov:atTime "2026-09-23T22:14:14.382819"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/cropped> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:2d6eb0dc351bd77d3f5b06672ed012ef5dec508f ] ;
    cwlprov:basename "crop_nir.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "crop_nir" .

id:6d7920a6-ee35-4701-88be-68838b9ba10b a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/node_otsu" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:887634a3-fcfa-4422-aaa1-8949fd8db10b ],
        [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_otsu> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:14:43.705752"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:14:35.950035"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:14:36.026698"^^xsd:dateTime ;
            prov:entity id:740c294a-a5f9-49be-b685-970f3eec0666 ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_otsu/raster> ] .

id:740c294a-a5f9-49be-b685-970f3eec0666 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:f960d24b-dcbf-4c16-88ce-ad7029487e59 ;
            prov:atTime "2026-09-23T22:14:35.757198"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_normalized_difference/ndwi> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:ea91fcdd6f24b5105718011ca77810e4b6763c09 ] ;
    cwlprov:basename "norm_diff.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "norm_diff" .

id:87ca5fb7-8991-4f4e-b107-8b30f9be5eea a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0" ;
    cwlprov:image "ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0" .

id:887634a3-fcfa-4422-aaa1-8949fd8db10b a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0" ;
    cwlprov:image "ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0" .

id:8bbef2fa-3721-4f50-b27c-1d641100a89f a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0" ;
    cwlprov:image "ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0" .

id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/node_crop" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:8bbef2fa-3721-4f50-b27c-1d641100a89f ],
        [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:11:25.695175"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:09:38.001367"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:38.075291"^^xsd:dateTime ;
            prov:entity data:9d1fba832b03655b5b73ff964bc74d4543bf904a ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:38.075873"^^xsd:dateTime ;
            prov:entity data:5f0002427ab880579cf6a5a5c704bd399f3310f2 ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/item> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:38.074835"^^xsd:dateTime ;
            prov:entity data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:38.074291"^^xsd:dateTime ;
            prov:entity data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/aoi> ] .

id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32 ;
            prov:atTime "2026-09-23T22:11:25.695199"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/cropped> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:69255dfb77442b710fb7caf4fe2c555a8a8ca404 ] ;
    cwlprov:basename "crop_green.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "crop_green" .

id:c2b78598-db7e-4ab3-89eb-621c7b5c9bd6 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0" ;
    cwlprov:image "ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0" .

id:eb53f504-eecb-4585-8e33-f7afdbbf816a a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:42580139-e758-4dbe-8ca8-7a114f7abf7f ],
        [ a provext:Membership ;
            provext:member id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e ] .

id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/node_crop_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2> ],
        [ a prov:Association ;
            prov:agent id:c2b78598-db7e-4ab3-89eb-621c7b5c9bd6 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:14:14.382774"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:11:25.771051"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:11:25.787372"^^xsd:dateTime ;
            prov:entity data:ba936cb0e062bea4078e8b56371ca8fe054093dd ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:11:25.788461"^^xsd:dateTime ;
            prov:entity data:5f0002427ab880579cf6a5a5c704bd399f3310f2 ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/item> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:11:25.787927"^^xsd:dateTime ;
            prov:entity data:9d1fba832b03655b5b73ff964bc74d4543bf904a ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:11:25.786582"^^xsd:dateTime ;
            prov:entity data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/aoi> ] .

id:f960d24b-dcbf-4c16-88ce-ad7029487e59 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/node_normalized_difference" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:87ca5fb7-8991-4f4e-b107-8b30f9be5eea ],
        [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_normalized_difference> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:14:35.757176"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:14:14.484903"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:14:14.589864"^^xsd:dateTime ;
            prov:entity id:eb53f504-eecb-4585-8e33-f7afdbbf816a ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_normalized_difference/rasters> ] .

data:5f0002427ab880579cf6a5a5c704bd399f3310f2 a wfprov:Artifact,
        prov:Entity ;
    prov:value "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A" .

data:ba936cb0e062bea4078e8b56371ca8fe054093dd a wfprov:Artifact,
        prov:Entity ;
    prov:value "nir" .

data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c a wfprov:Artifact,
        prov:Entity ;
    prov:value "green" .

data:9d1fba832b03655b5b73ff964bc74d4543bf904a a wfprov:Artifact,
        prov:Entity ;
    prov:value "EPSG:4326" .

data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad a wfprov:Artifact,
        prov:Entity ;
    prov:value "-121.399,39.834,-120.74,40.472" .

id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c a wfprov:WorkflowEngine,
        prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "cwltool 3.1.20260108082145" ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:09:36.483674"^^xsd:dateTime ;
            prov:hadActivity id:1851e03b-b5dd-458e-b892-800c846451b6 ] .

id:006f10ba-bce7-4602-bc25-46f0ca2c5724 a wfprov:WorkflowRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan wf:main ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:14:43.709126"^^xsd:dateTime ;
            prov:hadActivity id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:09:36.483742"^^xsd:dateTime ;
            prov:hadActivity id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.999442"^^xsd:dateTime ;
            prov:entity data:9d1fba832b03655b5b73ff964bc74d4543bf904a ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.997833"^^xsd:dateTime ;
            prov:entity data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.998964"^^xsd:dateTime ;
            prov:entity id:1f7549f8-4403-44f2-a435-f95a32edb9de ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/bands> ] ;
    prov:startedAtTime "2026-09-23T22:09:36.483701"^^xsd:dateTime .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Profile of the OGC API - Processes processDescription of `crop` (CWL
  CommandLineTool). Pins the process id and the input/output names; the input/output
  schemas are those derived from the CWL.
allOf:
- $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/process/schema.yaml
- $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/part2/v1/schemas/staticIndicator/schema.yaml
- type: object
  required:
  - id
  - version
  - inputs
  - outputs
  properties:
    id:
      const: crop
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - item
      - aoi
      - epsg
      - band
      propertyNames:
        enum:
        - item
        - aoi
        - epsg
        - band
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - cropped
      propertyNames:
        enum:
        - cropped
      x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
$defs:
  rawProcessDescription:
    $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/process/schema.yaml
  applicationPackage:
    $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/part2/v1/schemas/ogcapppkg/schema.yaml
  provenance:
    $ref: https://geolabs.github.io/bblocks-generic-provenance-profile/build/annotated/bbr/provenance/provenance/schema.yaml
  processTypeEntry:
    $ref: https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.yaml
  w3cProvJsonLd:
    $ref: https://ogcincubator.github.io/bblocks-prov-jsonld-alt/build/annotated/ogc-utils/prov/w3c-prov-jsonld/schema.yaml
  execute:
    description: Execute request for this process. Built on the processDescription
      input schemas and on ogc.api.processes.part1.v1.schemas.link / qualifiedInputValue,
      because ogc.api.processes.part1.v1.schemas.execute rejects plain strings and
      numbers (upstream issue U-01).
    type: object
    required:
    - inputs
    properties:
      inputs:
        type: object
        required:
        - item
        - aoi
        - epsg
        - band
        propertyNames:
          enum:
          - item
          - aoi
          - epsg
          - band
        additionalProperties:
          anyOf:
          - $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/link/schema.yaml
          - $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/qualifiedInputValue/schema.yaml
          - type:
            - string
            - number
            - integer
            - boolean
            - array
            - object
        x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
        x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
      outputs:
        type: object
        propertyNames:
          enum:
          - cropped
        x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
        x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
      response:
        enum:
        - raw
        - document
        x-jsonld-id: https://w3id.org/ogc/api/processes/response
  results:
    description: Results document (response=document) for this process (see U-01).
    type: object
    propertyNames:
      enum:
      - cropped
    additionalProperties:
      anyOf:
      - $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/link/schema.yaml
      - type: array
        items:
          $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/link/schema.yaml
      - type:
        - string
        - number
        - integer
        - boolean
        - array
        - object
  processRun:
    $ref: https://ogcincubator.github.io/bblocks-wf4ever/build/annotated/bbr/wf4ever/wfprov/ProcessRun/schema.yaml
  inheritedProcessDescription:
    allOf:
    - $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/process/schema.yaml
    - $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/part2/v1/schemas/staticIndicator/schema.yaml
    - type: object
      required:
      - id
      - version
      - inputs
      - outputs
      properties:
        id:
          const: crop
          x-jsonld-id: '@id'
        inputs:
          type: object
          required:
          - item
          - aoi
          - epsg
          - band
          propertyNames:
            enum:
            - item
            - aoi
            - epsg
            - band
          x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
        outputs:
          type: object
          required:
          - cropped
          propertyNames:
            enum:
            - cropped
          x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
          x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
    - description: '`crop` as the Implementation (instance level) of `https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval`:
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
              const: product
          - contains:
              const: band
          - contains:
              const: retrieval
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
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval
          - contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: http://www.opengis.net/spec/wps/2.0/def/process-profile/implementation
                href:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        inputs:
          type: object
          required:
          - band
          - item
          properties:
            item:
              required:
              - dataType
              - keywords
              - metadata
              properties:
                dataType:
                  const: https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: product
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/product
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/product
                  x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
                minOccurs:
                  type: integer
                  minimum: 0
                  maximum: 1
                  x-jsonld-id: https://w3id.org/ogc/api/processes/minOccurs
            band:
              required:
              - dataType
              - keywords
              - metadata
              properties:
                dataType:
                  const: https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier
                  x-jsonld-id: http://purl.org/dc/terms/type
                  x-jsonld-type: '@id'
                keywords:
                  allOf:
                  - contains:
                      const: band
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/band
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/inputs/band
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
          - cropped
          properties:
            cropped:
              required:
              - dataType
              - keywords
              - metadata
              properties:
                dataType:
                  const: https://geolabs.github.io/bblocks-data-types/def/data-type/raster
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
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/outputs/raster
                  - contains:
                      type: object
                      required:
                      - role
                      - href
                      properties:
                        role:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output
                        href:
                          const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/band-retrieval/outputs/raster
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
  itemIdentifier: ospd.process-profiles.water-bodies.crop
  register: https://geolabs.github.io/bblocks-process-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/crop/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/water-bodies/crop`

