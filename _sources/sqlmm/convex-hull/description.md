Process profile of the live OGC API - Processes process `ConvexHull` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/ConvexHull>.

> This service shall return a feature collection that represents the convex hull of geometry InputPolygon. The convex hull is the smallest convex polygon that contains all points of the geometry. The convex Hull for a geometry of encoding data type Point is the point itself

(the process's own description, as served)

## Implementation Profile

Implements [`Convex hull`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull) (`generic-profiles.implementation-profile.convex-hull`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputPolygon` | input `geometry` |
| `Result` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
