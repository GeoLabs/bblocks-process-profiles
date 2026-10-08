Process profile of the live OGC API - Processes process `Difference` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Difference>.

> This function shall return a bag of geometry values representing the closure of the set difference between the two geometries InputEntity1 and InputEntity2. The difference is the set of all points which lie on InputEntity1 but not on InputEntity2.

(the process's own description, as served)

## Implementation Profile

Implements [`Difference`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/difference) (`generic-profiles.implementation-profile.difference`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputEntity1` | input `geometry1` |
| `InputEntity2` | input `geometry2` |
| `Result` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
