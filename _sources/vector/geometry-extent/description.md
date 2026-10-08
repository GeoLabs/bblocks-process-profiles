Process profile of the live OGC API - Processes process `SAGA.shapes_tools.19` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.shapes_tools.19>.

> Get Shapes Extents

(the process's own description, as served)

## The tool behind it

[SAGA shapes_tools 19 (Get Shapes Extents)](https://saga-gis.sourceforge.io/saga_tool_doc/9.4.0/shapes_tools_19.html) -- SAGA 9.4.0 tool library documentation (the deployed SAGA version is not exposed by the service).

Tool 19 of SAGA's Shapes - Tools library (author O. Conrad, 2008; command line `saga_cmd shapes_tools 19`). It builds the extent (bounding rectangle) of the input shapes as polygons -- one for all shapes, one per shape (the default), or one per part of each shape, as chosen by its `OUTPUT` option. The documentation page itself only gives the title.

On this deployment:

- The live `OUTPUT` input is that option (`all shapes`, `each shape`, `each shape's part`); it is a live-only input, not part of the Implementation Profile.

## Implementation Profile

Implements [`Geometry extent`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/geometry-extent) (`generic-profiles.implementation-profile.geometry-extent`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `SHAPES` | input `geometry` |
| `OUTPUT` | -- (live-only inputs, Table 21 footnote b) |
| `EXTENTS` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
