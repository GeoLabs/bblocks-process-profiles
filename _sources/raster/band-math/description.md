Process profile of the live OGC API - Processes process `OTB.BandMath` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMath>.

> This application performs a mathematical operation on several multi-band images and outputs the result into a monoband image. The given expression is computed at each pixel position. Evaluation of the mathematical formula is done by the muParser library.The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (e.g. ``im2b3`` is the pixel value in 2nd image, 3rd band)* binary operators: * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division * ``^`` raise x to the power of y * ``

(the process's own description, as served)

## The tool behind it

[OTB BandMath](https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMath.html) -- Orfeo ToolBox 10.0.0 CookBook (the deployed OTB version is not exposed by the service).

> **Outputs a monoband image which is the result of a mathematical operation on several multi-band images.**
>
> This application performs a mathematical operation on several multi-band images and outputs the result into a monoband image. The given expression is computed at each pixel position. Evaluation of the mathematical formula is done by the muParser library.

Quoted from the OTB CookBook, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).

On this deployment:

- `il` is served with `maxOccurs: 1024`, ZOO-Project's encoding of an unbounded list.
- `out` is an input on the live service (the output pixel type, OTB's `-out` type argument) as well as the output image.

## Implementation Profile

Implements [`Raster band math`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math) (`generic-profiles.implementation-profile.raster-band-math`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `il` | input `rasters` |
| `exp` | input `expression` |
| `out`, `ram` | -- (live-only inputs, Table 21 footnote b) |
| `out` | output `raster` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
