Process profile of the live OGC API - Processes process `GetArea` (ZOO-Project, Geonovum testbed): <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/GetArea>.

> Computes the area of a geometry

(the process's own description, as served)

## Implementation Profile

Implements [`Area`](https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/area) (`generic-profiles.implementation-profile.area`, bblocks-generic-profiles). Live inputs/outputs and the Implementation Profile's (`bindings` in `scripts/profiles.yaml`):

| Live | Implementation Profile |
|---|---|
| `InputPolygon` | input `geometry` |
| `Area` | output `result` |

## Examples

- `processDescription.json`: the processDescription as served, ZOO-Project-internal fields removed.
- `processDescription.inherited.json`: the same with what OGC 14-065r1 Table 21 has it inherit at the Implementation (instance level): keywords and metadata references to its profiles.
- `process-type.json`: its candidate process-type entry.
