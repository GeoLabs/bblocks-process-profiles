Process profile of the live OGC API - Processes process `OTB.ImageEnvelope` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope>.

> Build a vector data containing the image envelope polygon. Useful for some projection, you can set the polygon with more points with the sr parameter. This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used.

(the process's own description, as served)

## The tool behind it

[OTB ImageEnvelope](https://www.orfeo-toolbox.org/CookBook/Applications/app_ImageEnvelope.html) -- Orfeo ToolBox 10.0.0 CookBook (the deployed OTB version is not exposed by the service).

> **Extracts an image envelope.**
>
> Build a vector data containing the image envelope polygon. [...] This filter supports user-specified output projection. If no projection is defined, the standard WGS84 projection will be used.

Quoted from the OTB CookBook, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).

## Implementation Profile

Implements [`Raster extent`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent) (`generic-profiles.implementation-profile.raster-extent`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `in` | input `raster` |
| `sr`, `elev`, `elev.geoid`, `elev.default`, `proj` | -- (live-only inputs, Table 21 footnote b) |
| `out` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
