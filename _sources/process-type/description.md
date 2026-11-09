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

## Meaning, classification, deployment, plan and correspondences (decision D5)

One entry per deployed process. The entry keeps the **meaning** of the type apart from four other
things said about it:

| Part | Keys | RDF |
|---|---|---|
| Meaning | `prefLabel`, `definition`, `subClassOf` | `skos:prefLabel`, `skos:definition`, `rdfs:subClassOf` on the type |
| Classification | `classification.phase` | `pp:phase` on the type (JSON grouping only, `@nest`) |
| Deployment | `deployment` (`profile`, `processDescription`, `provenanceClass`) | a node of its own, `pp:deployment` |
| Plan | `plan` (CWL processes only) | a `prov:Plan` of its own, `pp:plan` |
| Correspondences | `correspondences` (`exactMatch`, `closeMatch`, `relatedMatch`, `openeoEquivalence`) | SKOS mapping properties on the type (JSON grouping only, `@nest`) |

`implementsProfile` is the link to tier 3 (the Implementation Profile of bblocks-generic-profiles
this deployment implements), with the declarations that qualify how the deployment binds that
profile's roles: `serverSideFiles`, `roleDecompositions` and `assumedFormatGaps`
(`docs/FORMAT-CHECK.md`). `hasStep` lists the types of a Workflow's steps.

**Specialisation, not done.** D5 has each type specialise the activity type of its operation in
bblocks-generic-profiles when one exists (`subClassOf`). That activity type is a sub-class of
`geoproc:GeoprocessingActivityType`, and the Activity Type Register requires every registered
sub-class of it, at any depth, to declare its own spatial `acttype:usedEntityType` or
`acttype:generatedEntityType` (`geoproc:GeoprocessingActivityTypesShape`). Which entity type a process
type declares is decision D8, still pending, so `subClassOf` stays `acttype:ActivityType` and the
`const` on `subClassOf` and `type` is kept. The operation's meaning is reached today through
`implementsProfile`, whose Implementation Profile points to its activity type.

### The six phases and the Process Concepts: two axes

`phase` (`pp:phase`, formerly `skos:broader`, which made the phases broader concepts of the type)
positions a process in the six-phase workflow framework (filter configuration, selection/filtering,
data retrieval, pre-processing, scientific computation, export/aggregation; concept scheme
`pp:six-phases` in this block's ontology). The Process Concepts of bblocks-generic-profiles classify
operations by the kind of data they process. Over the 33 attached processes (31 live, 2 CWL), measured
on 2026-11-09:

| Process Concept | Phases of its processes |
|---|---|
| Raster coverage processing | pre-processing (3), scientific computation (4), export/aggregation (2) |
| Vector geometry processing | scientific computation (16), export/aggregation (1) |
| Terrain analysis | scientific computation (4) |
| Point cloud processing | pre-processing (3) |

One concept spans up to three phases, and scientific computation holds three concepts; the first three
phases (filter configuration, selection/filtering, data retrieval) hold no attached process at all. A
phase is where a process sits in one workflow, not a kind of operation: the same reprojection is
pre-processing here and could be export elsewhere. The phases therefore stay a distinct axis, on the
deployed type, and are not linked to the Process Concepts.

### Correspondences

`exactMatch` / `closeMatch` / `relatedMatch` (SKOS mapping properties) point to openEO Building
Blocks (`https://www.opengis.net/def/bblocks/ogc.openeo.*`); `openeoEquivalence.level` states the
equivalence level explicitly, including `none`, which SKOS cannot express, with the rationale and,
for composite or opaque processes, a stage-by-stage decomposition. They are proposed
correspondences, not part of the definition of the type.

### Amendments

The entries are proposals (`invalid`, `published`) and are amended in place, keeping their IRIs.
This register defines no amendment action and has no register specification: an entry records its
addition only, so the D5 restructuring of 2026-11-09 is not recorded as an action on each entry.

## Data types at tier 4

Each process profile attached to an Implementation Profile has, in
`processDescription.inherited.json`, the `dataType` (`dct:type`) of the role each bound input or
output implements, a `dt:DataType` concept of bblocks-data-types. Two shapes of this block, inherited
by every process profile, check it: `pp:Tier4DataTypeReferenceShape` (any tier-4 `dataType` is one
concept of that register) and `pp:Tier4BoundRoleDataTypeShape` (a bound input or output carries one).
They select the inputs and outputs under `proc:inputs` / `proc:outputs`, which
`gp:DataTypeReferenceShape` does not reach. `tests/` holds a failing fixture per constraint and a
control.

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

`deployment.processDescription` is the third thing: the interface (`/processes/{processID}`) the type is
profiled from, which the run's input and output entities point into (`#inputs/{name}`).

A process implemented natively by its server (`mutable: false`, as on a ZOO-Project deployment)
has no Application Package: Part 2 serves `/package` only for dynamically deployed processes
(requirement `package-get-op`, C). Such an entry has no `plan`; its `deployment.processDescription.href`
is the live process.

## Relation to process profiles and provenance

These entries describe **deployed process types** (tier 4), not the provider-independent WPS
Implementation Profiles (tier 3) of `bblocks-generic-profiles`. They are therefore the appropriate
place to profile `acttype:ActivityType`.

The `pp:` vocabulary (`https://geolabs.github.io/bblocks-process-profiles/def/`) and the phase IRIs
are provisional, pending a decision on the process-type register namespace.
