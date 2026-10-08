Schema of a **candidate process-type register entry** (OSPD Activity 4).

A process type classifies the activities recorded in provenance. The link is one-way and uses
plain W3C PROV: a provenance `Activity` (or a `wfprov:ProcessRun` / `wfprov:WorkflowRun`) of this
type carries the entry `id` in `activityType`. The entry itself is a SKOS concept:

- `phase` (→ `skos:broader`) positions the process in the six-phase framework
  (filter configuration → selection/filtering → data retrieval → pre-processing →
  scientific computation → export/aggregation);
- `exactMatch` / `closeMatch` / `relatedMatch` (→ SKOS mapping properties) point to openEO
  Building Blocks (`https://www.opengis.net/def/bblocks/ogc.openeo.*`);
- `openeoEquivalence.level` states the equivalence level explicitly, including `none`, which
  SKOS cannot express, with the rationale and, for composite or opaque processes, a
  stage-by-stage decomposition.

## Type, plan and process description are three things

The entry describes the **type** of activity. What an activity of that type executes is its
**plan** (`prov:Plan`), kept apart in `plan` with its own IRI: the OGC Application Package served
at `/processes/{processID}/package` by [OGC API - Processes - Part 2: Deploy, Replace,
Undeploy](https://docs.ogc.org/DRAFTS/20-044.html) (requirement
`/req/deploy-replace-undeploy/package-get-op`), whose `executionUnit` is the pinned CWL and which
also carries the EOAP CWL custom types the CWL uses. Every run of the type records **the same
IRI** as its `qualifiedAssociation.hadPlan` -- and `wfprov:describedByProcess` /
`describedByWorkflow`, whose `wfdesc:Workflow` range is itself a `prov:Plan` in wfprov -- so the
plan named at type level and the plan followed by each run are one resource.

`processDescription` is the third thing: the interface (`/processes/{processID}`) the type is
profiled from, which the run's input and output entities point into (`#inputs/{name}`).

A process implemented natively by its server (`mutable: false`, as on a ZOO-Project deployment)
has no Application Package: Part 2 serves `/package` only for dynamically deployed processes
(requirement `package-get-op`, C). Such an entry has no `plan`; its `processDescription.href` is
the live process.

Status values follow ISO 19135. Entries in this register are candidates: at most `submitted`.

The `pp:` vocabulary (`https://geolabs.github.io/bblocks-process-profiles/def/`) and the phase IRIs
are provisional, pending a decision on the process-type register namespace.
