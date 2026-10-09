Process profile of the live OGC API - Processes process `SAGA.pointcloud_tools.5` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.5>.

> Point Cloud to Shapes

(the process's own description, as served)

## The tool behind it

[SAGA pointcloud_tools 5 (Point Cloud to Shapes)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_5.html) -- SAGA 7.3.0 tool library documentation, the version deployed on the testbed (not yet exposed by its processDescription).

Tool 5 of SAGA's Shapes - Point Clouds library (author O. Conrad, 2009; command line `saga_cmd pointcloud_tools 5`): converts a point cloud to a shapes layer of points. The documentation page gives the title only.

On this deployment:

- The live service labels its LAS input `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` the Implementation Profile declares.

## Implementation Profile

Implements [`Point cloud to shapes`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes) (`generic-profiles.implementation-profile.point-cloud-to-shapes`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `POINTS` | input `points` |
| `SHAPES` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
