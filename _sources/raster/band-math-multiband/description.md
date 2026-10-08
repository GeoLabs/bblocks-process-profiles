Process profile of the live OGC API - Processes process `OTB.BandMathX` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX>.

> This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.The list of features and the syntax of muParserX is available at [1].As opposed to muParser (and thus the BandMath OTB-application [2]), muParserX supports vector expressions which allows outputting multi-band images.Hereafter is a brief reference of the muParserX syntaxFundamentals------------The formula can be written using:* numerical values ( 2.3, -5, 3.1e4, ...)* variables containing pixel values (please, note the indexing of inputs from 1 to N). Examples for the first input image: * ``im1`` a pixel from 1st input, made of n components (n bands) * ``im1b2`` the 2nd component of a pixel from 1st input (band index is 1-based) * ``im1b2N3x4`` a 3x4 pixels Neighbourhood of a pixel the 2nd component of a pixel from the 1st input * ``im1PhyX`` horizontal (X-axis) spacing of the 1st input. * ``im1PhyY`` vertical (Y-axis) spacing of the 1st input input. * ``im1b2Mean`` mean of the 2nd component of the 1st input (global statistics) * ``im1b2Mini`` minimum of the 2nd component of the 1st input (global statistics) * ``im1b2Maxi`` maximum of the 2nd component of the 1st input (global statistics) * ``im1b2Sum`` sum of the 2nd component of the 1st input (global statistics) * ``im1b2Var`` variance of the 2nd component of the 1st input (global statistics) * ``idxX`` and ``idxY`` are the indices of the current pixel (generic variables)* binary operators: * ``+`` addition, ``-`` subtraction, ``*`` multiplication, ``/`` division * ``^`` raise x to the power of y * ``

(the process's own description, as served)

## The tool behind it

[OTB BandMathX](https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html) -- Orfeo ToolBox 10.0.0 CookBook (the deployed OTB version is not exposed by the service).

> **This application performs mathematical operations on several multiband images.**
>
> This application performs a mathematical operation on several multi-band images and outputs the result into an image (multi- or mono-band, as opposed to the BandMath OTB-application). The mathematical formula is done by the muParserX library.

Quoted from the OTB CookBook, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).

On this deployment:

- `il` is served with `maxOccurs: 1024`, ZOO-Project's encoding of an unbounded list.

## Implementation Profile

Implements [`Raster band math (multi-band output)`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband) (`generic-profiles.implementation-profile.raster-band-math-multiband`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `il` | input `rasters` |
| `exp` | input `expression` |
| `out`, `incontext`, `ram` | -- (live-only inputs, Table 21 footnote b) |
| `out` | output `raster` |
| `outcontext` | -- (live-only outputs, Table 21 footnote b) |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
