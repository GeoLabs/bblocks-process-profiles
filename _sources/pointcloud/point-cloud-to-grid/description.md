Process profile of the live OGC API - Processes process `SAGA.pointcloud_tools.4` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.4>.

> Point Cloud to Grid

(the process's own description, as served)

## The tool behind it

[SAGA pointcloud_tools 4 (Point Cloud to Grid)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_4.html) -- SAGA 7.3.0 tool library documentation, the version deployed on the testbed (not yet exposed by its processDescription).

Tool 4 of SAGA's Shapes - Point Clouds library (author O. Conrad, 2009; command line `saga_cmd pointcloud_tools 4`). It writes the points falling in each cell of a grid of the given cell size to that cell, aggregated as the first, last or mean value, or the lowest or highest z.

On this deployment:

- The live service labels its LAS input `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` the Implementation Profile declares.
- `COUNT` (points per cell) and `GRIDS` (attributes) are supplementary outputs (Table 21 footnote b).

## Implementation Profile

Implements [`Point cloud to grid`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid) (`generic-profiles.implementation-profile.point-cloud-to-grid`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `POINTS` | input `points` |
| `CELLSIZE` | input `cellSize` |
| `OUTPUT`, `AGGREGATION` | -- (live-only inputs, Table 21 footnote b) |
| `GRID` | output `result` |
| `COUNT`, `GRIDS` | -- (live-only outputs, Table 21 footnote b) |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
