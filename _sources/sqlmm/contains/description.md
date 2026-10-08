Process profile of the live OGC API - Processes process `Contains` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Contains>.

> This service shall return a true value if and only if the geometry g2 lies in the closure (boundary union interior) of geometry g1 - the inverse of Within(g1: Geometry, g2: Geometry).

(the process's own description, as served)

## Implementation Profile

Implements [`Contains`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/contains) (`generic-profiles.implementation-profile.contains`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputEntity1` | input `geometry1` |
| `InputEntity2` | input `geometry2` |
| `Result` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
