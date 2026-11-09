Process profile of the live OGC API - Processes process `OTB.ExtractROI` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ExtractROI>.

> This application extracts a Region Of Interest with user parameters. There are four mode of extraction. The standard mode allows the user to enter one point (upper left corner of the region to extract) and a size. The extent mode needs two points (upper left corner and lower right) and the radius mode need the center of the region and the radius: it will extract the rectangle containing the circle defined and limited by the image dimension. The fit mode needs a reference image or vector and the dimension of the extracted region will be the same as the extent of the reference. Different units are available such as pixel, image physical space or longitude and latitude.

(the process's own description, as served)

## The tool behind it

[OTB ExtractROI](https://www.orfeo-toolbox.org/CookBook/Applications/app_ExtractROI.html) -- Orfeo ToolBox 10.0.0 CookBook (the deployed OTB version is not exposed by the service).

> **Extract a ROI defined by the user.**
>
> This application extracts a Region Of Interest with user parameters. There are four mode of extraction. [...] The extent mode needs two points (upper left corner and lower right) [...]

Quoted from the OTB CookBook, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).

On this deployment:

- The extent mode takes the area as four numbers (`mode.extent.ulx`, `uly`, `lrx`, `lry`), not one bounding box, hence the Implementation Profile's `areaOfInterest` stays unbound.

## Implementation Profile

Implements [`Raster crop`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop) (`generic-profiles.implementation-profile.raster-crop`, bblocks-generic-profiles).

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `in` | input `raster` | `raster` |
| `mode.extent.ulx`, `mode.extent.uly`, `mode.extent.lrx`, `mode.extent.lry`, `mode.extent.unit` (role decomposition) | input `areaOfInterest` | `bounding-box` |
| `out`, `mode`, `mode.fit.im`, `mode.fit.vect`, `mode.radius.r`, `mode.radius.unitr`, `mode.radius.cx`, `mode.radius.cy`, `mode.radius.unitc`, `startx`, `starty`, `sizex`, `sizey`, `elev`, `elev.geoid`, `elev.default`, `ram` | -- (the deployment's own inputs, Table 21 footnote b) | -- |
| `out` | output `raster` | `raster` |

**Role decomposition.** The input `areaOfInterest` is taken as `mode.extent.ulx`, `mode.extent.uly`, `mode.extent.lrx`, `mode.extent.lry`, `mode.extent.unit` (with `mode` = `extent`): With `mode` set to `extent`, OTB ExtractROI takes the area of interest as the upper-left (`mode.extent.ulx`, `mode.extent.uly`) and lower-right (`mode.extent.lrx`, `mode.extent.lry`) corners, plain numbers, in the unit given by `mode.extent.unit` (`pxl`, `phy` or `lonlat`), not as one OGC API - Processes bounding box: the representation bounding-box-ogcapi-processes-bbox of the role is not served. Declared in `roleDecompositions` of `process-type.json`; its representation is not served (`docs/FORMAT-CHECK.md`).

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles, and the data type of each bound input/output.
- `process-type.json`: its candidate process-type entry.
