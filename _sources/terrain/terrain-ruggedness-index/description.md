Process profile of the live OGC API - Processes process `SAGA.ta_morphometry.16` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.16>.

> References:&lt;br/&gt;Riley, S.J., De Gloria, S.D., Elliot, R. (1999): A Terrain Ruggedness that Quantifies Topographic Heterogeneity. Intermountain Journal of Science, Vol.5, No.1-4, pp.23-27. &lt;a href="http://www.fw.msu.edu/~rileysh2/Terrain%20Ruggedness%20Index.pdf"&gt;online&lt;/a&gt;.&lt;br/&gt;

(the process's own description, as served)

## The tool behind it

[SAGA ta_morphometry 16 (Terrain Ruggedness Index)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_16.html) -- SAGA 7.3.0 tool library documentation, the version deployed on the testbed (not yet exposed by its processDescription).

Tool 16 of SAGA's Terrain Analysis - Morphometry library (author O. Conrad, 2010; command line `saga_cmd ta_morphometry 16`), after Riley, De Gloria & Elliot (1999). The documentation page gives no description beyond that reference; the search radius, its shape and an optional distance weighting are the tool's own options.

## Implementation Profile

Implements [`Terrain ruggedness index`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index) (`generic-profiles.implementation-profile.terrain-ruggedness-index`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `DEM` | input `elevation` |
| `MODE`, `RADIUS`, `DW_WEIGHTING`, `DW_IDW_POWER`, `DW_IDW_OFFSET`, `DW_BANDWIDTH` | -- (live-only inputs, Table 21 footnote b) |
| `TRI` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
