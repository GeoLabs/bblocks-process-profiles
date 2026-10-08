Process profile of the live OGC API - Processes process `OTB.RadiometricIndices` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices>.

> This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.

(the process's own description, as served)

## The tool behind it

[OTB RadiometricIndices](https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html) -- Orfeo ToolBox 10.0.0 CookBook (the deployed OTB version is not exposed by the service).

> **Compute radiometric indices.**
>
> This application computes radiometric indices using the relevant channels of the input image. The output is a multi band image into which each channel is one of the selected indices.

Quoted from the OTB CookBook, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).

On this deployment:

- The CookBook's `-list` parameter (the indices to compute, default `ndvi`) is not exposed by the live service, hence the Implementation Profile's `index` stays unbound.
- The live `channels` input is titled "Blue channel index": the CookBook's `-channels.blue`.

## Implementation Profile

Implements [`Radiometric index`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index) (`generic-profiles.implementation-profile.radiometric-index`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `in` | input `rasters` |
| -- | input `index` (unbound: no input of the live service selects the index: OTB RadiometricIndices' `list` parameter is not exposed) |
| `out`, `channels`, `channels.green`, `channels.red`, `channels.nir`, `channels.mir`, `ram` | -- (live-only inputs, Table 21 footnote b) |
| `out` | output `raster` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
