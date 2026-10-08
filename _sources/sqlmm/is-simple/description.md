Process profile of the live OGC API - Processes process `IsSimple` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/IsSimple>.

> This service shall return a true value if and only if geometry g has no anomalous geometric points, such as self intersection or self tangency. Simple curves intersect themselves only at their endpoints (only if they are also closed, see next function).

(the process's own description, as served)

## Implementation Profile

Implements [`Is simple`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/is-simple) (`generic-profiles.implementation-profile.is-simple`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputPolygon` | input `geometry` |
| `Result` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
