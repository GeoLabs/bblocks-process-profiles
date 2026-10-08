Process profile of the live OGC API - Processes process `Buffer` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Buffer>.

> This service shall return a feature collection representing the buffer of geometry InputPolygon at distance BufferDistance. The buffer of a geometry at distance d is the Polygon or MultiPolygon which contains all points within a distance d of the geometry.

(the process's own description, as served)

## Implementation Profile

Implements [`Buffer`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/buffer) (`generic-profiles.implementation-profile.buffer`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputPolygon` | input `geometry` |
| `BufferDistance` | input `distance` |
| `Result` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
