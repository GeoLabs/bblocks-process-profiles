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
