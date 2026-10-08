Process profile of the live OGC API - Processes process `Intersection` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection>.

> This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2.

(the process's own description, as served)

## Implementation Profile

Implements [`Intersection`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection) (`generic-profiles.implementation-profile.intersection`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputEntity1` | input `geometry1` |
| `InputEntity2` | input `geometry2` |
| `Result` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
