Process profile of the live OGC API - Processes process `SymDifference` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SymDifference>.

> This service shall return a feature collection representing the closure of the symmetric difference of two Geometries. The symmetric difference is the set of points which lie on either InputEntity1 or InputEntity2 but not in both.

(the process's own description, as served)

## Implementation Profile

Implements [`Symmetric difference`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/symdifference) (`generic-profiles.implementation-profile.symdifference`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputEntity1` | input `geometry1` |
| `InputEntity2` | input `geometry2` |
| `Result` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
