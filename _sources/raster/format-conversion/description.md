Process profile of the live OGC API - Processes process `Gdal_Translate` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate>.

> http://www.gdal.org/gdal_translate.html

(the process's own description, as served)

## The tool behind it

[GDAL gdal_translate](https://gdal.org/programs/gdal_translate.html) -- GDAL documentation, current version (the deployed GDAL version is not exposed by the service).

Converts raster data between formats. Cited until 2026-11-09 as a source of the Implementation Profile raster-format-conversion of bblocks-generic-profiles, which no longer names tools (decision D4).

## Inputs and outputs passed as server-side file names

A file name, relative to the directory set by `dataPath` in the `[main]` section of the ZOO-Kernel main.cfg of the server: the file is stored on the server, and the process reads or writes it there. Its format is the representation of the Implementation Profile role it implements (GeoTIFF for raster).

| Live | Side | Implementation Profile role, whose format the file has |
|---|---|---|
| `InputDSN` | input | [`raster`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/inputs/raster) |
| `Result` | output | [`raster`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-format-conversion/outputs/raster) |

This deployment serves no media type for them: not a format gap. The entry declares them in `serverSideFiles` of `process-type.json`.

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
