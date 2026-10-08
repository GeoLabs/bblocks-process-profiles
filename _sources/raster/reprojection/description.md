Process profile of the live OGC API - Processes process `Gdal_Warp` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Warp>.

> The gdalwarp utility is an image mosaicing, reprojection and warping utility. The program can reproject to any supported projection, and can also apply GCPs stored with the image if the image is "raw" with control information.

(the process's own description, as served)

## Implementation Profile

Implements [`Raster reprojection`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection) (`generic-profiles.implementation-profile.raster-reprojection`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputDSN` | input `raster` |
| `t_srs` | input `targetCRS` |
| `Format`, `OutputDSN`, `s_srs`, `tps`, `geoloc`, `rpc`, `r`, `order`, `te` | -- (live-only inputs, Table 21 footnote b) |
| `Result` | output `raster` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
