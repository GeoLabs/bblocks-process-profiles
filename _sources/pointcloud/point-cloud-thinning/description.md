Process profile of the live OGC API - Processes process `SAGA.pointcloud_tools.9` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9>.

> This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order.

(the process's own description, as served)

## The tool behind it

[SAGA pointcloud_tools 9 (Point Cloud Thinning, Simple)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_9.html) -- SAGA 7.3.0 tool library documentation, the version deployed on the testbed (not yet exposed by its processDescription).

Tool 9 of SAGA's Shapes - Point Clouds library (author V. Wichmann, LASERDATA GmbH, 2010; command line `saga_cmd pointcloud_tools 9`). It reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.

On this deployment:

- The live service labels its LAS input and output `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` the Implementation Profile declares.
- `NUMBER` (titled "Number of Points", default 0; the documentation describes it no further) is a live-only input.

## Implementation Profile

Implements [`Point cloud thinning (simple)`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning) (`generic-profiles.implementation-profile.point-cloud-thinning`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `INPUT` | input `points` |
| `PERCENT` | input `percentage` |
| `NUMBER` | -- (live-only inputs, Table 21 footnote b) |
| `RESULT` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
