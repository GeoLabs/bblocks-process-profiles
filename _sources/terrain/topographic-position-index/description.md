Process profile of the live OGC API - Processes process `SAGA.ta_morphometry.18` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.18>.

> Topographic Position Index (TPI) calculation as proposed by Guisan et al. (1999). This is literally the same as the difference to the mean calculation (residual analysis) proposed by Wilson & Gallant (2000). The bandwidth parameter for distance weighting is given as percentage of the (outer) radius.

(the process's own description, as served)

## The tool behind it

[SAGA ta_morphometry 18 (Topographic Position Index)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_18.html) -- SAGA 7.3.0 tool library documentation, the version deployed on the testbed (not yet exposed by its processDescription).

Tool 18 of SAGA's Terrain Analysis - Morphometry library (author O. Conrad, 2011; command line `saga_cmd ta_morphometry 18`): the topographic position index as proposed by Guisan et al. (1999), which the documentation notes is the same as Wilson & Gallant's (2000) difference to the mean, over a neighbourhood given by a minimum and maximum radius.

## Implementation Profile

Implements [`Topographic position index`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/topographic-position-index) (`generic-profiles.implementation-profile.topographic-position-index`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `DEM` | input `elevation` |
| `STANDARD`, `RADIUS_MIN`, `RADIUS_MAX`, `DW_WEIGHTING`, `DW_IDW_POWER`, `DW_IDW_OFFSET`, `DW_BANDWIDTH` | -- (live-only inputs, Table 21 footnote b) |
| `TPI` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
