Process profile of the live OGC API - Processes process `Intersection` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersection>.

> This function SHALL return a bag of geometry values representing the Point set intersection of geometry InputEntity1 and geometry InputEntity2.

(the process's own description, as served)

## Implementation Profile

Implements [`Intersection`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersection) (`generic-profiles.implementation-profile.intersection`, bblocks-generic-profiles).

Deployed inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`), with the data type each bound input/output inherits (`processDescription.inherited.json`):

| Deployed | Implementation Profile | Data type |
|---|---|---|
| `InputEntity1` | input `geometry1` | `geometry` |
| `InputEntity2` | input `geometry2` | `geometry` |
| `Result` | output `result` | `geometry` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles, and the data type of each bound input/output.
- `process-type.json`: its candidate process-type entry.
