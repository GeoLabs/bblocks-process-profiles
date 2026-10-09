Process profile of the live OGC API - Processes process `SAGA.ta_lighting.0` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_lighting.0>.

> This tool performs an analytical hillshade computation for an elevation grid. The 'Standard' method simply calculates the angle at which light coming from the position of the light source would hit the surface. This method can produce angles greater than 90 degree. With the second method all values are kept within the range of 0-90 degree. It can be enhanced with shadowing effects, where shadowed cells will be marked with a value of exactly 90 degree. 'Shadows Only' creates a mask for the shadowed areas and sets all other cells to no-data. 'Combined Shading' takes the values of the standard method and multiplies these with the normalized slope. 'Ambient Occlusion' is based on the concepts of Tarini et al. (2006), but only the northern half-space is considered here.

(the process's own description, as served)

## The tool behind it

[SAGA ta_lighting 0 (Analytical Hillshading)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_lighting_0.html) -- SAGA 7.3.0 tool library documentation, the version deployed on the testbed (not yet exposed by its processDescription).

Tool 0 of SAGA's Terrain Analysis - Lighting library (authors O. Conrad, V. Wichmann, 2003-2013; command line `saga_cmd ta_lighting 0`). Its standard method computes, for each cell, the angle at which light from the light source hits the surface; other methods keep the result within 0-90 degrees, add shadows or ambient occlusion.

On this deployment:

- The light source's altitude is the live input `DECLINATION`, titled "Height": degrees above the horizon (default 45); `AZIMUTH` is in degrees clockwise from north (default 315). Both are optional on the live service, a restriction of the Generic Profile's minimum the register allows.

## Implementation Profile

Implements [`Analytical hillshading`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading) (`generic-profiles.implementation-profile.analytical-hillshading`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `ELEVATION` | input `elevation` |
| `AZIMUTH` | input `azimuth` |
| `DECLINATION` | input `altitude` |
| `METHOD`, `POSITION`, `DATE_MIN`, `TIME`, `EXAGGERATION`, `UNIT`, `SHADOW`, `NDIRS`, `RADIUS` | -- (live-only inputs, Table 21 footnote b) |
| `SHADE` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
