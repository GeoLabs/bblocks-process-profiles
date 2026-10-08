Process profile of the live OGC API - Processes process `Crosses` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Crosses>.

> This service shall return a true value if and only if the geometries g1 and g2 share some but neither is containe in the other, and the dimension of the intersection is less than that of both of the geometries.

(the process's own description, as served)

## Implementation Profile

Implements [`Crosses`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/crosses) (`generic-profiles.implementation-profile.crosses`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputEntity1` | input `geometry1` |
| `InputEntity2` | input `geometry2` |
| `Result` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
