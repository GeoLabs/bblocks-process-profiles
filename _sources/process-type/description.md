A **registered ActivityType** for each deployable process in the OSPD workflows. Each entry is both
a RIM register item and an OWL class; its IRI is the `rdf:type` carried by the PROV activities
recorded when that process executes.

## Registered Item Model

Each process-type entry is both:

- a `rim:RegisterItem` of the Activity Type Register's item class, held in the OSPD process-profiles
  register;
- an `acttype:ActivityType` and an `owl:Class` specialising `acttype:ActivityType`, so that its own
  IRI can be the RDF type of a provenance activity.

The schema profiles `ogc.register.schemas.activity-types-schema` from the
[Activity Type Register](https://ogcincubator.github.io/activity-type-register/) and, through it, the
[Registered Item Model](https://ogcincubator.github.io/registered-item-model/). Each entry has the RIM
required core (object identifier, item class, validity and publication status) and records its
addition as a `rim:RegisterAction` proposed by GeoLabs. There is no single-list `status`. A candidate
awaits a register decision, so it is `invalid` (not yet in force) and `published` (visible).

The item class is defined by the Activity Type Register and reused here: RIM permits reuse of a
register item class. The entries remain governed by this register and set `rim:inRegister` to its own
register IRI. `acttype:ActivityTypeShape`, inherited from the Activity Type Register, checks the item
class. `scripts/generate.py` holds its IRI in one constant, `ATR_ITEM_CLASS`, because upstream prepares
a rename.

## Additional classification

The link to provenance is one-way and uses plain W3C PROV: a provenance `Activity` (or a
`wfprov:ProcessRun` / `wfprov:WorkflowRun`) of this type carries the entry `id` in `activityType`.

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

## Relation to process profiles and provenance

These entries describe **deployed process types** (tier 4), not the provider-independent WPS
Implementation Profiles (tier 3) of `bblocks-generic-profiles`. They are therefore the appropriate
place to profile `acttype:ActivityType`.

The `pp:` vocabulary (`https://geolabs.github.io/bblocks-process-profiles/def/`) and the phase IRIs
are provisional, pending a decision on the process-type register namespace.
