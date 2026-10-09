Process profile of the live OGC API - Processes process `SAGA.ta_morphometry.0` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0>.

> Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.

(the process's own description, as served)

## The tool behind it

[SAGA ta_morphometry 0 (Slope, Aspect, Curvature)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_0.html) -- SAGA 7.3.0 tool library documentation, the version deployed on the testbed (not yet exposed by its processDescription).

Tool 0 of SAGA's Terrain Analysis - Morphometry library (author O. Conrad, 2001; command line `saga_cmd ta_morphometry 0`). It computes the local morphometric parameters of an elevation grid -- slope, aspect and, depending on the chosen method, curvatures (general, profile, plan, tangential, ...) -- from a local fit of the surface; the default method is the 9 parameter 2nd order polynom of Zevenbergen & Thorne (1987).

On this deployment:

- One process, many outputs: only `SLOPE` is bound to the Implementation Profile (`slope`); `ASPECT` and the ten curvature grids are supplementary outputs of the live service (Table 21 footnote b).

## Implementation Profile

Implements [`Slope`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/slope) (`generic-profiles.implementation-profile.slope`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `ELEVATION` | input `elevation` |
| `METHOD`, `UNIT_SLOPE`, `UNIT_ASPECT` | -- (live-only inputs, Table 21 footnote b) |
| `SLOPE` | output `result` |
| `ASPECT`, `C_GENE`, `C_PROF`, `C_PLAN`, `C_TANG`, `C_LONG`, `C_CROS`, `C_MINI`, `C_MAXI`, `C_TOTA`, `C_ROTO` | -- (live-only outputs, Table 21 footnote b) |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
