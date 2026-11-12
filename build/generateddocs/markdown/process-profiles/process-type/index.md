
# Process type register entry (Schema)

`ospd.process-profiles.process-type` *v0.1*

Candidate ActivityType register entry for each deployed OSPD process (decision D5: one per deployed process), its meaning kept apart from its six-phase classification, its deployment, its plan and its openEO correspondences, and linked to the Implementation Profile it implements, whose operation's activity type it then specialises. Its shapes check the data type of tier-4 inputs and outputs.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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
profile's roles: `serverSideFiles`, `roleDecompositions`, `assumedFormatGaps`, `byReference`,
`unboundRoles` and `fixedRoleValues` (`docs/FORMAT-CHECK.md`). `hasStep` lists the types of a
Workflow's steps.

**Not attached (decision Q1 of 2026-11-11).** A CWL CommandLineTool (an entry with `plan` and no
`hasStep`) that implements no Implementation Profile states why in `notAttached.reason`
(`pp:notAttached`, the reason as `skos:note`), written by `scripts/generate.py` from `tier3.reason`
in `scripts/profiles.yaml` (`docs/ATTACHMENTS.md`). The schema requires a non-empty reason and
forbids `notAttached` next to `implementsProfile`; a Workflow carries neither, its steps are compared
with the tiers one by one. `tests/` holds the failing fixtures (empty reason, no reason, both fields)
and a control.

**Specialisation (decision of 2026-11-10).** A process type that implements an Implementation
Profile specialises the activity type of its operation in bblocks-generic-profiles (the
`activityType` of that profile): `subClassOf` is that activity type, and the entry declares the same
GeoSPARQL entity type(s) (`usedEntityType`, `generatedEntityType`), as decision B of phase 3 does for
the activity types. That activity type is a sub-class of `geoproc:GeoprocessingActivityType`, and the
Activity Type Register requires every registered sub-class of it, at any depth, to declare a spatial
entity type: `geoproc:GeoprocessingActivityTypesShape`, loaded through `dependsOn`, checks it. It
reaches the process types through `activity-type-parents.ttl`, a data resource of this block
generated from bblocks-generic-profiles, which states each activity type's parent class and entity
types (and does not type them, so that the shapes of activity types do not run on another
register's items). `pp:ProcessTypeShape` checks that the parent is acttype:ActivityType or one of
those activity types, and that the entity types are the parent's. A process type attached to no
Implementation Profile keeps acttype:ActivityType. Narrower entity classes, `acttype:plan` and the
`rdf:type` of runs wait for decision D8.

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

### Register actions

The entries are proposals (`invalid`, `published`), amended in place, keeping their IRIs. The
register specification (`pp:specification`, in this block's ontology) defines `pp:amendmentAction`,
the type of such an in-place change, always classified substantive or clarifying, as the
specifications of bblocks-data-types, bblocks-data-formats and bblocks-generic-profiles do. Each
entry's `hasAction` records its addition, then its amendments. What is substantive and what is
clarifying is the row of `pp:specification` for this register:

> What is substantive here (validated 2026-11-10, extended 2026-11-11). Substantive: the parent class (subClassOf) or an entity type changed; the Implementation Profile implemented (implementsProfile) added, removed or changed; a binding declaration (serverSideFiles, roleDecompositions, assumedFormatGaps, byReference, unboundRoles, fixedRoleValues) added, removed or changed; the processDescription or the plan that is deployed changed; the six-phase classification changed, or the form in which a part of the entry is stated. Clarifying: the label, a reworded definition with the same meaning, the openEO correspondences and their rationale, notes and descriptions; the statement that a process is not attached (notAttached) added, removed or changed.

`scripts/generate.py` stops if this quotation differs from the literal of the ontology. The
amendments recorded so far:

- `d5-2026-11-09` (every entry, substantive): the D5 restructuring above;
- `tier3-<date>` (each attached CWL process, substantive): `implementsProfile` added;
- `specialisation-2026-11-10` (the 43 attached processes, substantive): the parent class and entity
  types;
- declarations added to a binding (substantive): `serverSideFiles` of `raster.reprojection` and
  `raster.format-conversion`, `roleDecompositions` of `raster.extract-roi` and its restriction to
  `mode.extent.unit` in `phy` or `lonlat`; for the ten CWL processes attached on 2026-11-10, their
  `processDescription.inherited.json`, `byReference`, `roleDecompositions`, `fixedRoleValues` and
  `unboundRoles`; `unboundRoles` of `raster.radiometric-index`;
- the definition of `water-bodies.crop` (substantive: it no longer says the output is reprojected);
- the plans of 2026-11-11 (substantive): the KindGrove steps pinned on `v0.0.2-rc3`, the W3 CWL on
  `72a76ae`, with the processDescriptions derived from them, which now declare their formats;
- `not-attached-2026-11-11` (the seven CWL CommandLineTools attached to no profile, clarifying):
  `notAttached` added.

`scripts/check_actions.py` compares each entry and its processDescription files with `ea01115` and
reports every changed field that no action dated on or after the change names.

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

## Examples

### reproject-image (closeMatch, not attached to tier 3)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/tier3-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Attached to the Implementation Profile https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-resampling (implementsProfile), after checking its signature (docs/ATTACHMENTS.md).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-resampling, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/inherited-description-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "processDescription.inherited.json added with the attachment to the Implementation Profile raster-resampling: the deployed processDescription with each bound input and output linked to the role it implements (metadata, role implementation-input or implementation-output) and carrying that role's dataType; the profile schema inherits it. The deployed processDescription is unchanged.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    }
  ],
  "prefLabel": "Performs image reprojection.",
  "definition": "Performs a reprojection over image bands and returns the resulting GeoTiff.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-resampling",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.algae-bloom.reproject-image",
    "processDescription": {
      "id": "reproject-image",
      "version": "1.0.0",
      "href": "https://ospd.example.org/ogc-api/processes/reproject-image"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/reproject-image/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "reproject-image",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0",
    "cctDependencies": [],
    "candidateCctDependencies": []
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-resampling",
  "correspondences": {
    "closeMatch": [
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial"
    ],
    "openeoEquivalence": {
      "level": "closeMatch",
      "rationale": "As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place."
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/tier3-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Attached to the Implementation Profile https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-resampling (implementsProfile), after checking its signature (docs/ATTACHMENTS.md).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-resampling, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/inherited-description-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "processDescription.inherited.json added with the attachment to the Implementation Profile raster-resampling: the deployed processDescription with each bound input and output linked to the role it implements (metadata, role implementation-input or implementation-output) and carrying that role's dataType; the profile schema inherits it. The deployed processDescription is unchanged.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"
    }
  ],
  "prefLabel": "Performs image reprojection.",
  "definition": "Performs a reprojection over image bands and returns the resulting GeoTiff.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-resampling",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.algae-bloom.reproject-image",
    "processDescription": {
      "id": "reproject-image",
      "version": "1.0.0",
      "href": "https://ospd.example.org/ogc-api/processes/reproject-image"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/reproject-image/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "reproject-image",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0",
    "cctDependencies": [],
    "candidateCctDependencies": []
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-resampling",
  "correspondences": {
    "closeMatch": [
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial"
    ],
    "openeoEquivalence": {
      "level": "closeMatch",
      "rationale": "As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place."
    }
  }
}
```

#### ttl
```ttl
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix ns1: <https://w3id.org/ogc/api/processes/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-22T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image> ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/d5-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/inherited-description-2026-11-10> a rim:RegisterAction ;
    dcterms:description "processDescription.inherited.json added with the attachment to the Implementation Profile raster-resampling: the deployed processDescription with each bound input and output linked to the role it implements (metadata, role implementation-input or implementation-output) and carrying that role's dataType; the profile schema inherits it. The deployed processDescription is unchanged." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/specialisation-2026-11-10> a rim:RegisterAction ;
    dcterms:description "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-resampling, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/tier3-2026-11-10> a rim:RegisterAction ;
    dcterms:description "Attached to the Implementation Profile https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-resampling (implementsProfile), after checking its signature (docs/ATTACHMENTS.md)." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process/reproject-image> rdfs:seeAlso <https://ospd.example.org/ogc-api/processes/reproject-image> ;
    pp:version "1.0.0" .

<https://ospd.example.org/ogc-api/processes/reproject-image/package> a prov:Plan ;
    dcterms:license <https://spdx.org/licenses/CC-BY-NC-SA-4.0> ;
    pp:cwlClass "CommandLineTool" ;
    pp:cwlId "reproject-image" ;
    ns1:executionUnit [ dcterms:format "application/cwl+yaml" ;
            ns2:relation <http://www.opengis.net/def/rel/ogc/1.0/executionUnit> ;
            oa:hasTarget <https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl> ] .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image> a owl:Class,
        pp:ProcessType,
        acttype:ActivityType ;
    rdfs:subClassOf <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-resampling> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial> ;
    skos:definition "Performs a reprojection over image bands and returns the resulting GeoTiff." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Performs image reprojection." ;
    pp:deployment [ pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/reproject-image> ;
            pp:profile "ospd.process-profiles.algae-bloom.reproject-image" ;
            pp:provenanceClass <http://purl.org/wf4ever/wfprov#ProcessRun> ] ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-resampling> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place." ] ;
    pp:phase <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing> ;
    pp:plan <https://ospd.example.org/ogc-api/processes/reproject-image/package> ;
    acttype:generatedEntityType geo:Feature ;
    acttype:usedEntityType geo:Feature ;
    rim:hasAction <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/addition>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/d5-2026-11-09>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/inherited-description-2026-11-10>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/specialisation-2026-11-10>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image/actions/tier3-2026-11-10> ;
    rim:inRegister pp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```


### KindGrove mangrove (none, with decomposition)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/not-attached-2026-11-11",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "notAttached added (absent -> {reason}): the entry now states that this CommandLineTool implements no Implementation Profile, with the reason already given in docs/ATTACHMENTS.md (profiles.yaml tier3.reason). Nothing else changes: the process was not attached before and is not attached now (decision Q1 of 2026-11-11).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-11T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove"
    }
  ],
  "prefLabel": "Mangrove biomass and carbon estimation",
  "definition": "Detects mangroves from Sentinel-2 L2A vegetation indices within a bounding box and estimates above-ground biomass and carbon stock (ipython2cwl binary of the KindGrove notebook).",
  "subClassOf": "https://w3id.org/ogc/rim/activity-type/ActivityType",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering",
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing",
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.kindgrove.mangrove",
    "processDescription": {
      "id": "mangrove_cli",
      "version": "0.0.1",
      "href": "https://ospd.example.org/ogc-api/processes/mangrove_cli"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/mangrove_cli/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/GeoLabs/bblocks-eoap-cct/raw/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove_cli",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "mangrove_cli",
    "license": "https://spdx.org/licenses/Apache-2.0",
    "cctDependencies": [],
    "candidateCctDependencies": [
      "eoap.cct.bbox"
    ]
  },
  "notAttached": {
    "reason": "One opaque tool runs scene selection, band retrieval, indices, biomass and carbon estimation and STAC export. No single profile describes it; kindgrove-steps splits it into steps."
  },
  "correspondences": {
    "openeoEquivalence": {
      "level": "none",
      "rationale": "Opaque: one ipython2cwl binary running the whole notebook. No single openEO process; each notebook stage has a closeMatch (decomposition). run_udf could wrap the binary but expects a data cube in and out, which this tool does not follow (it searches and downloads its own data).",
      "decomposition": [
        {
          "stage": "STAC search, Earth-Search sentinel-2-l2a, bbox, cloud cover, last N days",
          "openeo": [
            "ogc.openeo.processes.cubes.load_collection"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "NDVI (nir-red)/(nir+red+1e-8)",
          "openeo": [
            "ogc.openeo.processes.cubes.ndvi",
            "ogc.openeo.processes.math.indices.normalized_difference"
          ],
          "level": "closeMatch",
          "note": "epsilon 1e-8 in the denominator"
        },
        {
          "stage": "NDWI (green-nir)/(green+nir+1e-8)",
          "openeo": [
            "ogc.openeo.processes.math.indices.normalized_difference"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "SAVI ((nir-red)/(nir+red+0.5))*1.5",
          "openeo": [],
          "level": "none",
          "note": "no stable process; composition of add/subtract/divide/multiply"
        },
        {
          "stage": "mangrove mask: 0.3<NDVI<0.9 and NDWI>-0.3 and SAVI>0.2",
          "openeo": [
            "ogc.openeo.processes.comparison.gt",
            "ogc.openeo.processes.comparison.lt",
            "ogc.openeo.processes.logic.and",
            "ogc.openeo.processes.cubes.mask"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "biomass = 250.5*NDVI - 75.2",
          "openeo": [
            "ogc.openeo.processes.cubes.apply",
            "ogc.openeo.processes.math.multiply",
            "ogc.openeo.processes.math.subtract"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "carbon stock and totals (IPCC carbon fraction 0.47)",
          "openeo": [
            "ogc.openeo.processes.cubes.aggregate_spatial",
            "ogc.openeo.processes.math.sum",
            "ogc.openeo.processes.math.multiply"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "export CSV + GeoTIFF",
          "openeo": [
            "ogc.openeo.processes.cubes.save_result"
          ],
          "level": "closeMatch",
          "note": "CSV summaries are not a raster format"
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/not-attached-2026-11-11",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "notAttached added (absent -> {reason}): the entry now states that this CommandLineTool implements no Implementation Profile, with the reason already given in docs/ATTACHMENTS.md (profiles.yaml tier3.reason). Nothing else changes: the process was not attached before and is not attached now (decision Q1 of 2026-11-11).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-11T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove"
    }
  ],
  "prefLabel": "Mangrove biomass and carbon estimation",
  "definition": "Detects mangroves from Sentinel-2 L2A vegetation indices within a bounding box and estimates above-ground biomass and carbon stock (ipython2cwl binary of the KindGrove notebook).",
  "subClassOf": "https://w3id.org/ogc/rim/activity-type/ActivityType",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering",
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing",
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.kindgrove.mangrove",
    "processDescription": {
      "id": "mangrove_cli",
      "version": "0.0.1",
      "href": "https://ospd.example.org/ogc-api/processes/mangrove_cli"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/mangrove_cli/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/GeoLabs/bblocks-eoap-cct/raw/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove_cli",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "mangrove_cli",
    "license": "https://spdx.org/licenses/Apache-2.0",
    "cctDependencies": [],
    "candidateCctDependencies": [
      "eoap.cct.bbox"
    ]
  },
  "notAttached": {
    "reason": "One opaque tool runs scene selection, band retrieval, indices, biomass and carbon estimation and STAC export. No single profile describes it; kindgrove-steps splits it into steps."
  },
  "correspondences": {
    "openeoEquivalence": {
      "level": "none",
      "rationale": "Opaque: one ipython2cwl binary running the whole notebook. No single openEO process; each notebook stage has a closeMatch (decomposition). run_udf could wrap the binary but expects a data cube in and out, which this tool does not follow (it searches and downloads its own data).",
      "decomposition": [
        {
          "stage": "STAC search, Earth-Search sentinel-2-l2a, bbox, cloud cover, last N days",
          "openeo": [
            "ogc.openeo.processes.cubes.load_collection"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "NDVI (nir-red)/(nir+red+1e-8)",
          "openeo": [
            "ogc.openeo.processes.cubes.ndvi",
            "ogc.openeo.processes.math.indices.normalized_difference"
          ],
          "level": "closeMatch",
          "note": "epsilon 1e-8 in the denominator"
        },
        {
          "stage": "NDWI (green-nir)/(green+nir+1e-8)",
          "openeo": [
            "ogc.openeo.processes.math.indices.normalized_difference"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "SAVI ((nir-red)/(nir+red+0.5))*1.5",
          "openeo": [],
          "level": "none",
          "note": "no stable process; composition of add/subtract/divide/multiply"
        },
        {
          "stage": "mangrove mask: 0.3<NDVI<0.9 and NDWI>-0.3 and SAVI>0.2",
          "openeo": [
            "ogc.openeo.processes.comparison.gt",
            "ogc.openeo.processes.comparison.lt",
            "ogc.openeo.processes.logic.and",
            "ogc.openeo.processes.cubes.mask"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "biomass = 250.5*NDVI - 75.2",
          "openeo": [
            "ogc.openeo.processes.cubes.apply",
            "ogc.openeo.processes.math.multiply",
            "ogc.openeo.processes.math.subtract"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "carbon stock and totals (IPCC carbon fraction 0.47)",
          "openeo": [
            "ogc.openeo.processes.cubes.aggregate_spatial",
            "ogc.openeo.processes.math.sum",
            "ogc.openeo.processes.math.multiply"
          ],
          "level": "closeMatch"
        },
        {
          "stage": "export CSV + GeoTIFF",
          "openeo": [
            "ogc.openeo.processes.cubes.save_result"
          ],
          "level": "closeMatch",
          "note": "CSV summaries are not a raster format"
        }
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/api/processes/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-22T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove> ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/d5-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/not-attached-2026-11-11> a rim:RegisterAction ;
    dcterms:description "notAttached added (absent -> {reason}): the entry now states that this CommandLineTool implements no Implementation Profile, with the reason already given in docs/ATTACHMENTS.md (profiles.yaml tier3.reason). Nothing else changes: the process was not attached before and is not attached now (decision Q1 of 2026-11-11)." ;
    prov:startedAtTime "2026-11-11T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove_cli> rdfs:seeAlso <https://ospd.example.org/ogc-api/processes/mangrove_cli> ;
    pp:version "0.0.1" .

<https://ospd.example.org/ogc-api/processes/mangrove_cli/package> a prov:Plan ;
    dcterms:license <https://spdx.org/licenses/Apache-2.0> ;
    pp:candidateCctDependency "eoap.cct.bbox" ;
    pp:cwlClass "CommandLineTool" ;
    pp:cwlId "mangrove_cli" ;
    ns1:executionUnit [ dcterms:format "application/cwl+yaml" ;
            ns2:relation <http://www.opengis.net/def/rel/ogc/1.0/executionUnit> ;
            oa:hasTarget <https://github.com/GeoLabs/bblocks-eoap-cct/raw/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove_cli> ] .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove> a owl:Class,
        pp:ProcessType,
        acttype:ActivityType ;
    rdfs:subClassOf acttype:ActivityType ;
    skos:definition "Detects mangroves from Sentinel-2 L2A vegetation indices within a bounding box and estimates above-ground biomass and carbon stock (ipython2cwl binary of the KindGrove notebook)." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Mangrove biomass and carbon estimation" ;
    pp:deployment [ pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove_cli> ;
            pp:profile "ospd.process-profiles.kindgrove.mangrove" ;
            pp:provenanceClass <http://purl.org/wf4ever/wfprov#ProcessRun> ] ;
    pp:notAttached [ skos:note "One opaque tool runs scene selection, band retrieval, indices, biomass and carbon estimation and STAC export. No single profile describes it; kindgrove-steps splits it into steps." ] ;
    pp:openeoEquivalence [ pp:decomposition ( [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.load_collection" ;
                        pp:stage "STAC search, Earth-Search sentinel-2-l2a, bbox, cloud cover, last N days" ] [ skos:note "epsilon 1e-8 in the denominator" ;
                        pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.ndvi",
                            "ogc.openeo.processes.math.indices.normalized_difference" ;
                        pp:stage "NDVI (nir-red)/(nir+red+1e-8)" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.math.indices.normalized_difference" ;
                        pp:stage "NDWI (green-nir)/(green+nir+1e-8)" ] [ skos:note "no stable process; composition of add/subtract/divide/multiply" ;
                        pp:equivalenceLevel "none" ;
                        pp:stage "SAVI ((nir-red)/(nir+red+0.5))*1.5" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.comparison.gt",
                            "ogc.openeo.processes.comparison.lt",
                            "ogc.openeo.processes.cubes.mask",
                            "ogc.openeo.processes.logic.and" ;
                        pp:stage "mangrove mask: 0.3<NDVI<0.9 and NDWI>-0.3 and SAVI>0.2" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.apply",
                            "ogc.openeo.processes.math.multiply",
                            "ogc.openeo.processes.math.subtract" ;
                        pp:stage "biomass = 250.5*NDVI - 75.2" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.aggregate_spatial",
                            "ogc.openeo.processes.math.multiply",
                            "ogc.openeo.processes.math.sum" ;
                        pp:stage "carbon stock and totals (IPCC carbon fraction 0.47)" ] [ skos:note "CSV summaries are not a raster format" ;
                        pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.save_result" ;
                        pp:stage "export CSV + GeoTIFF" ] ) ;
            pp:equivalenceLevel "none" ;
            pp:rationale "Opaque: one ipython2cwl binary running the whole notebook. No single openEO process; each notebook stage has a closeMatch (decomposition). run_udf could wrap the binary but expects a data cube in and out, which this tool does not follow (it searches and downloads its own data)." ] ;
    pp:phase <https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering> ;
    pp:plan <https://ospd.example.org/ogc-api/processes/mangrove_cli/package> ;
    rim:hasAction <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/addition>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/d5-2026-11-09>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove/actions/not-attached-2026-11-11> ;
    rim:inRegister pp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```


### KindGrove steps reproject-band (CWL, attached to raster-reprojection, specialising its activity type)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/tier3-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Attached to the Implementation Profile https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection (implementsProfile), after checking its signature (docs/ATTACHMENTS.md).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/plan-2026-11-11",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "plan: executionUnit.href moves from the v0.0.2-rc2 release of GeoLabs/KindGrove to the v0.0.2-rc3 release (mangrove-workflow-steps.cwl#reproject_band). The rc3 CWL declares the format of its Files (the ipython2cwl format annotation), so the processDescription derived from it changes: contentMediaType application/octet-stream -> image/tiff; application=geotiff (with contentEncoding binary) for the input band_file and the output reprojected_file, in processDescription.json and processDescription.inherited.json. assumedFormatGaps removed: its two gaps, band_file and reprojected_file served as application/octet-stream, are closed by the format the CWL now declares, as their reason anticipated (removed on 2026-11-10 with the corrected CWL, pinned on 2026-11-11).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-11T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    }
  ],
  "prefLabel": "Reproject a raster onto a regular grid",
  "definition": "Reprojects a raster onto a regular grid covering a bounding box.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.kindgrove-steps.reproject-band",
    "processDescription": {
      "id": "reproject_band",
      "version": "0.1.0",
      "href": "https://ospd.example.org/ogc-api/processes/reproject_band"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/reproject_band/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc3/mangrove-workflow-steps.cwl#reproject_band",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "reproject_band",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0",
    "cctDependencies": [],
    "candidateCctDependencies": [
      "eoap.cct.bbox"
    ]
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection",
  "correspondences": {
    "closeMatch": [
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial"
    ],
    "openeoEquivalence": {
      "level": "closeMatch",
      "rationale": "resample_spatial with a target `resolution` and `projection` (epsg); no explicit resampling-method parameter in the CWL (implementation default), same partial match as `algae-bloom.reproject-image`."
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/tier3-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Attached to the Implementation Profile https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection (implementsProfile), after checking its signature (docs/ATTACHMENTS.md).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/plan-2026-11-11",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "plan: executionUnit.href moves from the v0.0.2-rc2 release of GeoLabs/KindGrove to the v0.0.2-rc3 release (mangrove-workflow-steps.cwl#reproject_band). The rc3 CWL declares the format of its Files (the ipython2cwl format annotation), so the processDescription derived from it changes: contentMediaType application/octet-stream -> image/tiff; application=geotiff (with contentEncoding binary) for the input band_file and the output reprojected_file, in processDescription.json and processDescription.inherited.json. assumedFormatGaps removed: its two gaps, band_file and reprojected_file served as application/octet-stream, are closed by the format the CWL now declares, as their reason anticipated (removed on 2026-11-10 with the corrected CWL, pinned on 2026-11-11).",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-11T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"
    }
  ],
  "prefLabel": "Reproject a raster onto a regular grid",
  "definition": "Reprojects a raster onto a regular grid covering a bounding box.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.kindgrove-steps.reproject-band",
    "processDescription": {
      "id": "reproject_band",
      "version": "0.1.0",
      "href": "https://ospd.example.org/ogc-api/processes/reproject_band"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "plan": {
    "id": "https://ospd.example.org/ogc-api/processes/reproject_band/package",
    "type": "Plan",
    "executionUnit": {
      "href": "https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc3/mangrove-workflow-steps.cwl#reproject_band",
      "type": "application/cwl+yaml",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
    },
    "cwlClass": "CommandLineTool",
    "cwlId": "reproject_band",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0",
    "cctDependencies": [],
    "candidateCctDependencies": [
      "eoap.cct.bbox"
    ]
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection",
  "correspondences": {
    "closeMatch": [
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial"
    ],
    "openeoEquivalence": {
      "level": "closeMatch",
      "rationale": "resample_spatial with a target `resolution` and `projection` (epsg); no explicit resampling-method parameter in the CWL (implementation default), same partial match as `algae-bloom.reproject-image`."
    }
  }
}
```

#### ttl
```ttl
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix ns1: <https://w3id.org/ogc/api/processes/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-22T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band> ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/d5-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/plan-2026-11-11> a rim:RegisterAction ;
    dcterms:description "plan: executionUnit.href moves from the v0.0.2-rc2 release of GeoLabs/KindGrove to the v0.0.2-rc3 release (mangrove-workflow-steps.cwl#reproject_band). The rc3 CWL declares the format of its Files (the ipython2cwl format annotation), so the processDescription derived from it changes: contentMediaType application/octet-stream -> image/tiff; application=geotiff (with contentEncoding binary) for the input band_file and the output reprojected_file, in processDescription.json and processDescription.inherited.json. assumedFormatGaps removed: its two gaps, band_file and reprojected_file served as application/octet-stream, are closed by the format the CWL now declares, as their reason anticipated (removed on 2026-11-10 with the corrected CWL, pinned on 2026-11-11)." ;
    prov:startedAtTime "2026-11-11T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/specialisation-2026-11-10> a rim:RegisterAction ;
    dcterms:description "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/tier3-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Attached to the Implementation Profile https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection (implementsProfile), after checking its signature (docs/ATTACHMENTS.md)." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process/reproject_band> rdfs:seeAlso <https://ospd.example.org/ogc-api/processes/reproject_band> ;
    pp:version "0.1.0" .

<https://ospd.example.org/ogc-api/processes/reproject_band/package> a prov:Plan ;
    dcterms:license <https://spdx.org/licenses/CC-BY-NC-SA-4.0> ;
    pp:candidateCctDependency "eoap.cct.bbox" ;
    pp:cwlClass "CommandLineTool" ;
    pp:cwlId "reproject_band" ;
    ns1:executionUnit [ dcterms:format "application/cwl+yaml" ;
            ns2:relation <http://www.opengis.net/def/rel/ogc/1.0/executionUnit> ;
            oa:hasTarget <https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc3/mangrove-workflow-steps.cwl#reproject_band> ] .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band> a owl:Class,
        pp:ProcessType,
        acttype:ActivityType ;
    rdfs:subClassOf <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial> ;
    skos:definition "Reprojects a raster onto a regular grid covering a bounding box." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Reproject a raster onto a regular grid" ;
    pp:deployment [ pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/reproject_band> ;
            pp:profile "ospd.process-profiles.kindgrove-steps.reproject-band" ;
            pp:provenanceClass <http://purl.org/wf4ever/wfprov#ProcessRun> ] ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "resample_spatial with a target `resolution` and `projection` (epsg); no explicit resampling-method parameter in the CWL (implementation default), same partial match as `algae-bloom.reproject-image`." ] ;
    pp:phase <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing> ;
    pp:plan <https://ospd.example.org/ogc-api/processes/reproject_band/package> ;
    acttype:generatedEntityType geo:Feature ;
    acttype:usedEntityType geo:Feature ;
    rim:hasAction <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/addition>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/d5-2026-11-09>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/plan-2026-11-11>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/specialisation-2026-11-10>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band/actions/tier3-2026-11-09> ;
    rim:inRegister pp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/reproject-band"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```


### OTB.ExtractROI (live, attached to raster-crop, role decomposition)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/role-decomposition-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "roleDecompositions added: the role areaOfInterest of raster-crop is taken as mode.extent.ulx, uly, lrx, lry and mode.extent.unit, with mode = extent (decision of 2026-11-09); before, the role was left unbound.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-crop, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/role-decomposition-unit-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The role decomposition is restricted to mode.extent.unit in phy or lonlat, a selector instead of a part: with the default unit pxl the four numbers are pixel indices, not a bounding box.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    }
  ],
  "prefLabel": "Extract a ROI defined by the user.",
  "definition": "This application extracts a Region Of Interest with user parameters. There are four mode of extraction. The standard mode allows the user to enter one point (upper left corner of the region to extract) and a size. The extent mode needs two points (upper left corner and lower right) and the radius mode need the center of the region and the radius: it will extract the rectangle containing the circle defined and limited by the image dimension. The fit mode needs a reference image or vector and the dimension of the extracted region will be the same as the extent of the reference. Different units are available such as pixel, image physical space or longitude and latitude.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-crop",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.raster.extract-roi",
    "processDescription": {
      "id": "OTB.ExtractROI",
      "version": "1.0.0",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ExtractROI"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop",
  "roleDecompositions": [
    {
      "side": "inputs",
      "implements": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/areaOfInterest",
      "parts": [
        "mode.extent.ulx",
        "mode.extent.uly",
        "mode.extent.lrx",
        "mode.extent.lry"
      ],
      "selectors": [
        {
          "name": "mode",
          "values": [
            "extent"
          ]
        },
        {
          "name": "mode.extent.unit",
          "values": [
            "phy",
            "lonlat"
          ]
        }
      ],
      "note": "With `mode` set to `extent` and `mode.extent.unit` set to `phy` (coordinates in the image's physical space, its CRS) or `lonlat` (longitude and latitude), OTB ExtractROI takes the area of interest as the upper-left (`mode.extent.ulx`, `mode.extent.uly`) and lower-right (`mode.extent.lrx`, `mode.extent.lry`) corners, plain numbers, not as one OGC API - Processes bounding box: the representation bounding-box-ogcapi-processes-bbox of the role is not served. With the default unit `pxl` the four numbers are pixel indices, not a bounding box, and the role is not implemented."
    }
  ],
  "correspondences": {
    "closeMatch": [
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.filter_bbox"
    ],
    "openeoEquivalence": {
      "level": "closeMatch",
      "rationale": "OTB.ExtractROI's \"extent\" mode (`mode.extent.ulx/uly/lrx/lry`, two corner points) matches filter_bbox's role (spatially limit a data cube to a bounding box). Not exactMatch: three other modes have no openEO equivalent -- pixel-offset/size (\"standard\": `startx`/`starty`/ `sizex`/`sizey`), circular (\"radius\": `mode.radius.r`/`cx`/`cy`), and reference-geometry (\"fit\": `mode.fit.im`/`vect`) extraction."
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi",
  "type": [
    "ProcessType",
    "owlClass",
    "ActivityType"
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-process-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-09-22T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/d5-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/role-decomposition-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "roleDecompositions added: the role areaOfInterest of raster-crop is taken as mode.extent.ulx, uly, lrx, lry and mode.extent.unit, with mode = extent (decision of 2026-11-09); before, the role was left unbound.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/specialisation-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-crop, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    },
    {
      "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/role-decomposition-unit-2026-11-10",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The role decomposition is restricted to mode.extent.unit in phy or lonlat, a selector instead of a part: with the default unit pxl the four numbers are pixel indices, not a bounding box.",
      "proposer": "https://geolabs.github.io/bblocks-process-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"
    }
  ],
  "prefLabel": "Extract a ROI defined by the user.",
  "definition": "This application extracts a Region Of Interest with user parameters. There are four mode of extraction. The standard mode allows the user to enter one point (upper left corner of the region to extract) and a size. The extent mode needs two points (upper left corner and lower right) and the radius mode need the center of the region and the radius: it will extract the rectangle containing the circle defined and limited by the image dimension. The fit mode needs a reference image or vector and the dimension of the extracted region will be the same as the extent of the reference. Different units are available such as pixel, image physical space or longitude and latitude.",
  "subClassOf": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-crop",
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "classification": {
    "phase": [
      "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
    ]
  },
  "deployment": {
    "profile": "ospd.process-profiles.raster.extract-roi",
    "processDescription": {
      "id": "OTB.ExtractROI",
      "version": "1.0.0",
      "href": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ExtractROI"
    },
    "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun"
  },
  "implementsProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop",
  "roleDecompositions": [
    {
      "side": "inputs",
      "implements": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/areaOfInterest",
      "parts": [
        "mode.extent.ulx",
        "mode.extent.uly",
        "mode.extent.lrx",
        "mode.extent.lry"
      ],
      "selectors": [
        {
          "name": "mode",
          "values": [
            "extent"
          ]
        },
        {
          "name": "mode.extent.unit",
          "values": [
            "phy",
            "lonlat"
          ]
        }
      ],
      "note": "With `mode` set to `extent` and `mode.extent.unit` set to `phy` (coordinates in the image's physical space, its CRS) or `lonlat` (longitude and latitude), OTB ExtractROI takes the area of interest as the upper-left (`mode.extent.ulx`, `mode.extent.uly`) and lower-right (`mode.extent.lrx`, `mode.extent.lry`) corners, plain numbers, not as one OGC API - Processes bounding box: the representation bounding-box-ogcapi-processes-bbox of the role is not served. With the default unit `pxl` the four numbers are pixel indices, not a bounding box, and the role is not implemented."
    }
  ],
  "correspondences": {
    "closeMatch": [
      "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.filter_bbox"
    ],
    "openeoEquivalence": {
      "level": "closeMatch",
      "rationale": "OTB.ExtractROI's \"extent\" mode (`mode.extent.ulx/uly/lrx/lry`, two corner points) matches filter_bbox's role (spatially limit a data cube to a bounding box). Not exactMatch: three other modes have no openEO equivalent -- pixel-offset/size (\"standard\": `startx`/`starty`/ `sizex`/`sizey`), circular (\"radius\": `mode.radius.r`/`cx`/`cy`), and reference-geometry (\"fit\": `mode.fit.im`/`vect`) extraction."
    }
  }
}
```

#### ttl
```ttl
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-22T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi> ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/d5-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D5: the meaning of the type (prefLabel, definition, subClassOf) is kept apart from the rest. The six-phase position moves from skos:broader to pp:phase (classification); profile, processDescription and provenanceClass move to a node of their own (pp:deployment); the openEO correspondences are grouped apart. The plan was already a node of its own." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/role-decomposition-2026-11-09> a rim:RegisterAction ;
    dcterms:description "roleDecompositions added: the role areaOfInterest of raster-crop is taken as mode.extent.ulx, uly, lrx, lry and mode.extent.unit, with mode = extent (decision of 2026-11-09); before, the role was left unbound." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/role-decomposition-unit-2026-11-10> a rim:RegisterAction ;
    dcterms:description "The role decomposition is restricted to mode.extent.unit in phy or lonlat, a selector instead of a part: with the default unit pxl the four numbers are pixel indices, not a bounding box." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/specialisation-2026-11-10> a rim:RegisterAction ;
    dcterms:description "subClassOf changes from https://w3id.org/ogc/rim/activity-type/ActivityType to https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-crop, the activity type of the operation in bblocks-generic-profiles (decision of 2026-11-10), with the same entity type(s): http://www.opengis.net/ont/geosparql#Feature, http://www.opengis.net/ont/geosparql#Feature." ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType pp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer pp:geolabs .

<https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.ExtractROI> rdfs:seeAlso <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ExtractROI> ;
    pp:version "1.0.0" .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi> a owl:Class,
        pp:ProcessType,
        acttype:ActivityType ;
    rdfs:subClassOf <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-crop> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.filter_bbox> ;
    skos:definition "This application extracts a Region Of Interest with user parameters. There are four mode of extraction. The standard mode allows the user to enter one point (upper left corner of the region to extract) and a size. The extent mode needs two points (upper left corner and lower right) and the radius mode need the center of the region and the radius: it will extract the rectangle containing the circle defined and limited by the image dimension. The fit mode needs a reference image or vector and the dimension of the extracted region will be the same as the extent of the reference. Different units are available such as pixel, image physical space or longitude and latitude." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Extract a ROI defined by the user." ;
    pp:deployment [ pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/OTB.ExtractROI> ;
            pp:profile "ospd.process-profiles.raster.extract-roi" ;
            pp:provenanceClass <http://purl.org/wf4ever/wfprov#ProcessRun> ] ;
    pp:implementsProfile <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "OTB.ExtractROI's \"extent\" mode (`mode.extent.ulx/uly/lrx/lry`, two corner points) matches filter_bbox's role (spatially limit a data cube to a bounding box). Not exactMatch: three other modes have no openEO equivalent -- pixel-offset/size (\"standard\": `startx`/`starty`/ `sizex`/`sizey`), circular (\"radius\": `mode.radius.r`/`cx`/`cy`), and reference-geometry (\"fit\": `mode.fit.im`/`vect`) extraction." ] ;
    pp:phase <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing> ;
    pp:roleDecomposition [ skos:note "With `mode` set to `extent` and `mode.extent.unit` set to `phy` (coordinates in the image's physical space, its CRS) or `lonlat` (longitude and latitude), OTB ExtractROI takes the area of interest as the upper-left (`mode.extent.ulx`, `mode.extent.uly`) and lower-right (`mode.extent.lrx`, `mode.extent.lry`) corners, plain numbers, not as one OGC API - Processes bounding box: the representation bounding-box-ogcapi-processes-bbox of the role is not served. With the default unit `pxl` the four numbers are pixel indices, not a bounding box, and the role is not implemented." ;
            pp:implements <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/areaOfInterest> ;
            pp:part ( "mode.extent.ulx" "mode.extent.uly" "mode.extent.lrx" "mode.extent.lry" ) ;
            pp:selector [ rdf:value "lonlat",
                        "phy" ;
                    pp:liveName "mode.extent.unit" ],
                [ rdf:value "extent" ;
                    pp:liveName "mode" ] ;
            pp:side "inputs" ] ;
    acttype:generatedEntityType geo:Feature ;
    acttype:usedEntityType geo:Feature ;
    rim:hasAction <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/addition>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/d5-2026-11-09>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/role-decomposition-2026-11-09>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/role-decomposition-unit-2026-11-10>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi/actions/specialisation-2026-11-10> ;
    rim:inRegister pp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-process-profiles/def/process-type/raster/extract-roi"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```


### The register, its specification and its amendment action type
The ontology of this block, validated as data: this checks `pp:register` and `pp:specification` against the shapes of the Registered Item Model.
#### turtle
```turtle
@prefix pp:      <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix rim:     <https://w3id.org/ogc/rim/> .
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix prov:    <http://www.w3.org/ns/prov#> .
@prefix dct:     <http://purl.org/dc/terms/> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:     <http://www.w3.org/2002/07/owl#> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .

pp: a owl:Ontology ;
    owl:imports <https://w3id.org/ogc/rim/> , <https://w3id.org/ogc/rim/activity-type/> ;
    dct:title "OSPD process-type register profile" ;
    dct:description "Profiles the Registered Item Model ActivityType for deployable OSPD CWL process types. Each process-type record is a governed ActivityType item and an OWL class used as rdf:type on its PROV activity records." ;
    dct:creator "GeoLabs SARL" .

# ProcessType records are both SKOS concepts and registered ActivityType classes.
pp:ProcessType a owl:Class ;
    rdfs:subClassOf acttype:ActivityType, skos:Concept ;
    rdfs:isDefinedBy pp: ;
    rdfs:label "OSPD process type" .

pp:register a rim:Register ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-process-profiles/def/register"^^xsd:anyURI ;
    rim:functionalIdentifier "https://geolabs.github.io/bblocks-process-profiles/"^^xsd:anyURI ;
    dct:title "OSPD Process Profiles"@en ;
    dct:description "Register of deployable OSPD process profiles and their process types."@en ;
    rim:registerOwner pp:geolabs ;
    rim:registerManager pp:geolabs ;
    rim:controlBody pp:geolabs ;
    rim:hasSpecification pp:specification ;
    rim:runsOn pp:registerSystem .

# The register specification (decision of 2026-11-10), on the pattern of the specifications of
# bblocks-data-types, bblocks-data-formats and bblocks-generic-profiles. rim:definesSubstantiveChange
# and the rule for proposals are the texts validated for all the registers of this project, word for
# word. The version rule is specific to these registers and does not come from ISO 19135. The
# substantive/clarifying row for this register was validated by GeoLabs on 2026-11-10; GeoLabs
# validated its extension (byReference, unboundRoles, fixedRoleValues substantive; notAttached
# clarifying) on 2026-11-11.
# tests/specification-without-title-fail.ttl proves that rim:RegisterSpecificationShape runs, and
# examples.yaml validates this file against it.
pp:specification a rim:RegisterSpecification ;
    dct:title "OSPD Process Profiles register specification"@en ;
    dct:description
        "Scope. This register holds the Implementation (instance level) of OGC 14-065 WPS 2.0.2 §7.5: one process profile and one process type per deployed process, in two populations, the CWL processes of the OSPD reference workflows and the live processes of the Geonovum testbed. The process types are its register items (pp:ProcessType, of the item class of the Activity Type Register). The tiers above, Process Concepts, Generic and Implementation Profiles and the activity types of operations, are items of bblocks-generic-profiles, not of this register."@en ,
        "Register type. A content register, as the Registered Item Model uses the term: items carry their own name and definition, and there is no concept plane."@en ,
        "Roles. GeoLabs SARL is the register owner, the register manager and, for now, the control body. GeoLabs intends to delegate the control body role to the OGC or to an OSPD working group."@en ,
        "Identifiers. The object identifier of a process type is its IRI, https://geolabs.github.io/bblocks-process-profiles/def/process-type/<group>/<name>. These IRIs are provisional, pending a decision on the namespace of the process-type register. An object identifier never redirects; only a functional identifier may. The identifier of a published item changes only by an explicit decision."@en ,
        "Versions. An addition is an action of type addition, with no classification. A substantive change creates a new item or a new version, linked by rim:supersededBy, with an action classified substantive. A clarifying change keeps the item and its version, with an action classified clarifying. This version rule is specific to the registers of this project and does not come from ISO 19135. The classification correctional is not available. An item is retired by unpublishing it, not by deleting it."@en ,
        "What is substantive here (validated 2026-11-10, extended 2026-11-11). Substantive: the parent class (subClassOf) or an entity type changed; the Implementation Profile implemented (implementsProfile) added, removed or changed; a binding declaration (serverSideFiles, roleDecompositions, assumedFormatGaps, byReference, unboundRoles, fixedRoleValues) added, removed or changed; the processDescription or the plan that is deployed changed; the six-phase classification changed, or the form in which a part of the entry is stated. Clarifying: the label, a reworded definition with the same meaning, the openEO correspondences and their rationale, notes and descriptions; the statement that a process is not attached (notAttached) added, removed or changed."@en ,
        "Proposals. While an item is a proposal, with no control-body decision recorded, it is amended in place, with a classified `rim:RegisterAction`. The substantive rule applies once it has been accepted."@en ,
        "Amendment. pp:amendmentAction is the action type of an in-place change to a proposal, an item with no control-body decision recorded. Such an action is always classified, clarifying or substantive: it is the classified rim:RegisterAction of the rule for proposals. This type is specific to this register and will be replaced if the Registered Item Model defines one."@en ,
        "Eligibility. Process type: one deployed process, its meaning (label, definition, parent class: acttype:ActivityType, or the activity type of its operation with the same GeoSPARQL entity types when it implements an Implementation Profile), its six-phase classification, its deployment, its plan for a CWL process, and its proposed openEO correspondences. GeoLabs is the only proposer recorded so far; no criteria for other proposers have been set."@en ,
        "Commitments. No commitment to register users has been set."@en ;
    rim:definesSubstantiveChange "A change is substantive when a register user may have to change their data, profiles or processes because of it, or when it changes what an item means. Any other change to an existing item is clarifying." .

# rim:actionType is required and the Registered Item Model has no type for an in-place change of a
# proposal; it lets a register specification define further action types. Defined by
# pp:specification, specific to this register.
pp:amendmentAction a rim:RegisterActionType , skos:Concept ;
    rdfs:isDefinedBy pp: ;
    skos:prefLabel "amendment"@en ;
    skos:definition "An in-place change to a proposal, an item with no control-body decision recorded. Always classified, clarifying or substantive."@en .

pp:geolabs a prov:Organization ;
    rdfs:label "GeoLabs SARL" ;
    rdfs:seeAlso <https://www.geolabs.fr/> .

pp:registerSystem a rim:RegisterSystem ;
    rdfs:label "OGC Building Blocks register (bblocks-postprocess, GitHub Pages)" ;
    rdfs:seeAlso <https://github.com/GeoLabs/bblocks-process-profiles/> .

pp:process-type a rim:ConceptSystem, skos:ConceptScheme ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-process-profiles/def/process-type"^^xsd:anyURI ;
    dct:title "OSPD process types"@en ;
    skos:prefLabel "OSPD process types"@en ;
    dct:description "Process types that classify the deployable CWL activities recorded in provenance."@en .

# Decision D5: a process type keeps its meaning (skos:prefLabel, skos:definition, rdfs:subClassOf)
# apart from its classification, its deployment, its plan and its correspondences.

pp:phase a owl:ObjectProperty ;
    rdfs:isDefinedBy pp: ;
    rdfs:label "phase" ;
    rdfs:comment "Classification of a process type: its position in the six-phase workflow framework. Not a broader concept of the type (until 2026-11-09 it was skos:broader), and not derived from the Process Concepts of bblocks-generic-profiles, which classify operations by kind of data: the two axes are independent." ;
    rdfs:range skos:Concept .

pp:deployment a owl:ObjectProperty ;
    rdfs:isDefinedBy pp: ;
    rdfs:label "deployment" ;
    rdfs:comment "What is deployed for a process type: its process profile block (pp:profile), the processDescription it is profiled from (pp:processDescription) and the class of its run records (pp:provenanceClass). Not part of the meaning of the type." .

pp:plan a owl:ObjectProperty ;
    rdfs:isDefinedBy pp: ;
    rdfs:label "plan" ;
    rdfs:comment "The prov:Plan an activity of a CWL-sourced process type executes: its OGC Application Package. Not part of the meaning of the type; acttype:plan, the steps an activity type requires, is a different property (decision D8, pending)." ;
    rdfs:range prov:Plan .

pp:implementsProfile a owl:ObjectProperty ;
    rdfs:isDefinedBy pp: ;
    rdfs:label "implements profile" ;
    rdfs:comment "The Implementation Profile of bblocks-generic-profiles (tier 3) that the deployed process implements: the canonical tier-4 to tier-3 link. Its declaration as a sub-property of rim:relatedItem waits for decision D8." .

pp:roleDecomposition a owl:ObjectProperty ;
    rdfs:isDefinedBy pp: ;
    rdfs:label "role decomposition" ;
    rdfs:comment "An Implementation Profile role (pp:implements) that the deployment takes as several inputs or outputs (pp:part, in order), none of which carries the role's representation." .

pp:assumedFormatGap a owl:ObjectProperty ;
    rdfs:isDefinedBy pp: ;
    rdfs:label "assumed format gap" ;
    rdfs:comment "A bound input or output whose Implementation Profile representation the deployment does not serve, accepted with its reason (skos:note) and evidence (pp:evidence)." .

pp:notAttached a owl:ObjectProperty ;
    rdfs:isDefinedBy pp: ;
    rdfs:label "not attached" ;
    rdfs:comment "States that a CWL CommandLineTool implements no Implementation Profile of bblocks-generic-profiles, with the reason (skos:note); exclusive of pp:implementsProfile, and absent from a Workflow (decision Q1, 2026-11-11)." .

pp:six-phases a skos:ConceptScheme ;
    rdfs:isDefinedBy pp: ;
    skos:prefLabel "Six-phase workflow framework"@en ;
    dct:description "Positions of a process in an Earth observation workflow, from filter configuration to export, used to classify the OSPD process types (pp:phase). Provisional IRIs, as the rest of the pp: vocabulary."@en ;
    skos:hasTopConcept <https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration> ,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering> ,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval> ,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing> ,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> ,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation> .

<https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration> a skos:Concept ;
    skos:prefLabel "Filter configuration"@en ; skos:inScheme pp:six-phases ; skos:topConceptOf pp:six-phases .
<https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering> a skos:Concept ;
    skos:prefLabel "Selection / filtering"@en ; skos:inScheme pp:six-phases ; skos:topConceptOf pp:six-phases .
<https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval> a skos:Concept ;
    skos:prefLabel "Data retrieval"@en ; skos:inScheme pp:six-phases ; skos:topConceptOf pp:six-phases .
<https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing> a skos:Concept ;
    skos:prefLabel "Pre-processing"@en ; skos:inScheme pp:six-phases ; skos:topConceptOf pp:six-phases .
<https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> a skos:Concept ;
    skos:prefLabel "Scientific computation"@en ; skos:inScheme pp:six-phases ; skos:topConceptOf pp:six-phases .
<https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation> a skos:Concept ;
    skos:prefLabel "Export / aggregation"@en ; skos:inScheme pp:six-phases ; skos:topConceptOf pp:six-phases .

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Registered Process Activity Type
description: 'A candidate process-type register item which is also a class used as
  the PROV rdf:type of executions. It profiles the Registered Item Model activity-type
  schema; each entry is both an acttype:ActivityType register item and an owl:Class
  specialising acttype:ActivityType, or, when it implements an Implementation Profile,
  the activity type of its operation in bblocks-generic-profiles, with the same GeoSPARQL
  entity types.


  Decision D5: one entry per deployed process, in five parts. Its meaning is `prefLabel`,
  `definition` and `subClassOf`. Its classification (`classification`: the six-phase
  position), its deployment (`deployment`: profile block, processDescription, run
  class), its plan (`plan`) and its correspondences (`correspondences`: openEO) are
  kept apart from that meaning. `implementsProfile` links it to its Implementation
  Profile (tier 3), with the declarations that qualify the binding (`serverSideFiles`,
  `roleDecompositions`, `assumedFormatGaps`, `byReference`, `unboundRoles`, `fixedRoleValues`);
  a CWL CommandLineTool attached to no Implementation Profile states why in `notAttached`.


  What an activity of this type executes -- its plan, a `prov:Plan` -- is the OGC
  Application Package served by OGC API - Processes - Part 2 (Deploy, Replace, Undeploy)
  at `/processes/{processID}/package`, whose execution unit is the pinned CWL. A run
  of this type records the same IRI as its `qualifiedAssociation.hadPlan`. A process
  implemented natively by its server (`mutable: false`) has no Application Package
  (Part 2 serves `/package` only for dynamically deployed processes) and so no `plan`;
  `deployment.processDescription` is then the only link to what is executed.'
allOf:
- $ref: https://ogcincubator.github.io/activity-type-register/build/annotated/register/schemas/activity-types-schema/schema.yaml
- type: object
  required:
  - id
  - type
  - prefLabel
  - definition
  - inScheme
  - classification
  - deployment
  - correspondences
  - objectIdentifier
  - itemClass
  - inRegister
  - validityStatus
  - publicationStatus
  - subClassOf
  - hasAction
  properties:
    id:
      description: IRI of the process type (also used as `activityType` in provenance
        records).
      type: string
      format: uri
      x-jsonld-id: '@id'
    type:
      const:
      - ProcessType
      - owlClass
      - ActivityType
      x-jsonld-id: '@type'
    prefLabel:
      type: string
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    definition:
      type: string
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
    inScheme:
      description: IRI of the process-type register (concept scheme) this entry is
        proposed to.
      type: string
      format: uri
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
      x-jsonld-type: '@id'
    classification:
      description: 'Classification of the type, apart from its meaning (decision D5).
        `phase` (pp:phase, formerly skos:broader) is a separate axis from the Process
        Concepts of bblocks-generic-profiles: see the block description.'
      type: object
      required:
      - phase
      additionalProperties: false
      properties:
        phase:
          description: Position(s) in the six-phase workflow framework.
          type: array
          minItems: 1
          items:
            type: string
            enum:
            - https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration
            - https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering
            - https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval
            - https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing
            - https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation
            - https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation
          x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/phase
          x-jsonld-type: '@id'
      x-jsonld-id: '@nest'
    deployment:
      description: 'What is deployed (decision D5): the process profile block, the
        processDescription and the class of its run records.'
      type: object
      required:
      - profile
      - processDescription
      - provenanceClass
      additionalProperties: false
      properties:
        profile:
          description: Identifier of the process-profile Building Block.
          type: string
          x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/profile
        processDescription:
          description: The OGC API - Processes processDescription this type is profiled
            from, at `href` (the `/processes/{processID}` resource). For a CWL-sourced
            process it is the description the Application Package would deploy, under
            the illustrative host `ospd.example.org`; for a live process (e.g. a ZOO-Project
            deployment, `ospd.process-profiles.sqlmm.*`) the real one.
          type: object
          required:
          - id
          - version
          - href
          properties:
            id:
              type: string
              x-jsonld-id: '@id'
            version:
              type: string
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/version
            href:
              type: string
              format: uri
              x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
              x-jsonld-type: '@id'
            license:
              description: Of a live process; omitted, not null, when it declares
                none -- do not assume one.
              type: string
              format: uri
              x-jsonld-id: http://purl.org/dc/terms/license
              x-jsonld-type: '@id'
          x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/processDescription
        provenanceClass:
          description: Class of the run records produced by executing this process.
          type: string
          enum:
          - http://purl.org/wf4ever/wfprov#ProcessRun
          - http://purl.org/wf4ever/wfprov#WorkflowRun
          x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/provenanceClass
          x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/deployment
    plan:
      description: 'The plan (`prov:Plan`) an activity of this type executes: the
        OGC Application Package at `/processes/{processID}/package` (OGC API - Processes
        - Part 2, requirement /req/deploy-replace-undeploy/package-get-op), whose
        `executionUnit` is the pinned CWL. Present only for a CWL-sourced process.'
      type: object
      required:
      - id
      - type
      - executionUnit
      - cwlClass
      - cwlId
      properties:
        id:
          type: string
          format: uri
          pattern: /processes/[^/]+/package$
          x-jsonld-id: '@id'
        type:
          const: Plan
          x-jsonld-id: '@type'
        executionUnit:
          description: Same link as the Application Package's own `executionUnit`
            (examples/ogcapppkg.json).
          type: object
          required:
          - href
          - type
          properties:
            href:
              description: Pinned URL of the CWL document.
              type: string
              format: uri
              x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
              x-jsonld-type: '@id'
            type:
              type: string
              x-jsonld-id: http://purl.org/dc/terms/format
            rel:
              type: string
              x-jsonld-id: http://www.iana.org/assignments/relation
              x-jsonld-type: '@id'
              x-jsonld-base: http://www.iana.org/assignments/relation/
          x-jsonld-id: https://w3id.org/ogc/api/processes/executionUnit
        cwlClass:
          enum:
          - CommandLineTool
          - Workflow
          - ExpressionTool
          x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cwlClass
        cwlId:
          type: string
          x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cwlId
        license:
          type: string
          format: uri
          x-jsonld-id: http://purl.org/dc/terms/license
          x-jsonld-type: '@id'
        cctDependencies:
          description: EOAP CWL custom types used by the CWL.
          type: array
          items:
            type: string
            pattern: ^eoap\.cct\.
          x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cctDependency
        candidateCctDependencies:
          description: EOAP CWL custom types that could replace plain CWL types (not
            used by the CWL).
          type: array
          items:
            type: string
            pattern: ^eoap\.cct\.
          x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/candidateCctDependency
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/plan
    serverSideFiles:
      description: Inputs and outputs that this deployment passes as names of files
        stored on the server (relative to the ZOO-Kernel `dataPath`), not as encoded
        data, so with no media type. Each names the Implementation Profile role whose
        format the file has (`implements`).
      type: array
      minItems: 1
      items:
        type: object
        required:
        - name
        - side
        - implements
        - location
        properties:
          name:
            type: string
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/liveName
          side:
            enum:
            - inputs
            - outputs
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/side
          implements:
            type: string
            format: uri
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/implements
            x-jsonld-type: '@id'
          location:
            type: string
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/location
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/serverSideFile
    byReference:
      description: 'Bound inputs and outputs, of a role with a representation, that
        this deployment takes or returns as a URL of the data instead of the data
        (C1, 2026-11-10): the representation describes what the URL resolves to. Reported
        apart, like serverSideFiles.'
      type: array
      minItems: 1
      items:
        type: object
        required:
        - name
        - side
        - implements
        - note
        additionalProperties: false
        properties:
          name:
            type: string
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/liveName
          side:
            enum:
            - inputs
            - outputs
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/side
          implements:
            type: string
            format: uri
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/implements
            x-jsonld-type: '@id'
          note:
            type: string
            minLength: 1
            x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/byReference
    unboundRoles:
      description: 'Implementation Profile roles this deployment leaves unbound, each
        with its reason: a role of minOccurs 0 at tier 3 (C2, 2026-11-10), or, for
        a live process of the testbed, an input its deployment does not expose.'
      type: array
      minItems: 1
      items:
        type: object
        required:
        - side
        - implements
        - reason
        additionalProperties: false
        properties:
          side:
            enum:
            - inputs
            - outputs
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/side
          implements:
            type: string
            format: uri
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/implements
            x-jsonld-type: '@id'
          reason:
            type: string
            minLength: 1
            x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/unboundRole
    fixedRoleValues:
      description: 'Optional Implementation Profile roles (minOccurs 0) that this
        deployment leaves unbound because it fixes their value (C3, 2026-11-10): e.g.
        the index computed by a normalized-difference tool.'
      type: array
      minItems: 1
      items:
        type: object
        required:
        - side
        - implements
        - values
        - reason
        additionalProperties: false
        properties:
          side:
            enum:
            - inputs
            - outputs
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/side
          implements:
            type: string
            format: uri
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/implements
            x-jsonld-type: '@id'
          values:
            type: array
            minItems: 1
            items:
              type: string
            x-jsonld-id: http://www.w3.org/1999/02/22-rdf-syntax-ns#value
          reason:
            type: string
            minLength: 1
            x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/fixedRoleValue
    roleDecompositions:
      description: 'Implementation Profile roles that this deployment takes as one
        or more inputs (or outputs) none of which is the role: a role with a representation
        none of the parts carries (the bounding box of raster-crop taken by OTB.ExtractROI
        as four corner numbers), or a literal role (C11, 2026-11-10: a time interval
        given by `days_back`, or by `date` + `delta`). `reproducible` is false when
        the parts depend on the time of execution.'
      type: array
      minItems: 1
      items:
        type: object
        required:
        - side
        - implements
        - parts
        - note
        additionalProperties: false
        properties:
          side:
            enum:
            - inputs
            - outputs
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/side
          implements:
            type: string
            format: uri
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/implements
            x-jsonld-type: '@id'
          parts:
            type: array
            minItems: 1
            items:
              type: string
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/part
            x-jsonld-container: '@list'
          note:
            type: string
            x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
          selectors:
            description: 'The conditions under which the parts implement the role:
              each a deployed input and the values it must take.'
            type: array
            minItems: 1
            items:
              type: object
              required:
              - name
              - values
              additionalProperties: false
              properties:
                name:
                  type: string
                  x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/liveName
                values:
                  type: array
                  minItems: 1
                  items:
                    type: string
                  x-jsonld-id: http://www.w3.org/1999/02/22-rdf-syntax-ns#value
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/selector
          reproducible:
            type: boolean
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/reproducible
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/roleDecomposition
    assumedFormatGaps:
      description: Bound inputs and outputs whose Implementation Profile representation
        this deployment does not serve (no media type exposed), accepted with a reason
        and its evidence (A4.3, docs/FORMAT-CHECK.md).
      type: array
      minItems: 1
      items:
        type: object
        required:
        - name
        - side
        - implements
        - served
        - reason
        - evidence
        additionalProperties: false
        properties:
          name:
            type: string
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/liveName
          side:
            enum:
            - inputs
            - outputs
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/side
          implements:
            type: string
            format: uri
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/implements
            x-jsonld-type: '@id'
          served:
            type: array
            items:
              type: string
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/servedMediaType
          reason:
            type: string
            x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
          evidence:
            type: string
            x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/evidence
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/assumedFormatGap
    notAttached:
      description: A CWL CommandLineTool (an entry with `plan` and no `hasStep`) that
        implements no Implementation Profile, with the reason (decision Q1, 2026-11-11).
        Exclusive of `implementsProfile`; a Workflow carries neither. The reason holds
        at least one non-blank character (2026-11-11).
      type: object
      required:
      - reason
      additionalProperties: false
      properties:
        reason:
          type: string
          minLength: 1
          pattern: \S
          x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/notAttached
    implementsProfile:
      description: "IRI of the nearest applicable profile this process specialises,
        in the generic-profiles register -- normally an Implementation Profile (generic-profiles.implementation-profile.*,
        OGC 14-065 WPS 2.0.2 \xA77.5.3: standard data formats, still not one specific
        deployment's own choice), or a Generic Profile directly when no Implementation
        Profile exists yet. Optional: most processes have no standardised abstract
        counterpart at all. `processDescription` and `plan` (this entry's own concrete
        binding) are what further specialise it to one real, deployed process -- Implementation
        (instance level) in the same standard's terms."
      type: string
      format: uri
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/implementsProfile
      x-jsonld-type: '@id'
    hasStep:
      description: Process types of the steps of a Workflow.
      type: array
      items:
        type: string
        format: uri
      x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/hasStep
      x-jsonld-type: '@id'
    correspondences:
      description: 'Proposed correspondences with openEO (decision D5: apart from
        the meaning of the type). The SKOS mapping properties stay on the type; `openeoEquivalence`
        states the level, including `none`.'
      type: object
      required:
      - openeoEquivalence
      additionalProperties: false
      properties:
        exactMatch:
          type: array
          items:
            type: string
            format: uri
          x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
          x-jsonld-type: '@id'
        closeMatch:
          type: array
          items:
            type: string
            format: uri
          x-jsonld-id: http://www.w3.org/2004/02/skos/core#closeMatch
          x-jsonld-type: '@id'
        relatedMatch:
          type: array
          items:
            type: string
            format: uri
          x-jsonld-id: http://www.w3.org/2004/02/skos/core#relatedMatch
          x-jsonld-type: '@id'
        openeoEquivalence:
          type: object
          required:
          - level
          - rationale
          properties:
            level:
              enum:
              - exactMatch
              - closeMatch
              - none
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/equivalenceLevel
            rationale:
              type: string
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/rationale
            decomposition:
              description: Ordered correspondence of the stages of a composite or
                opaque process.
              type: array
              items:
                type: object
                required:
                - stage
                - level
                properties:
                  stage:
                    type: string
                    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/stage
                  openeo:
                    type: array
                    items:
                      type: string
                      pattern: ^ogc\.openeo\.
                    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/openeo
                  level:
                    enum:
                    - exactMatch
                    - closeMatch
                    - none
                    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/equivalenceLevel
                  note:
                    type: string
                    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/decomposition
              x-jsonld-container: '@list'
          x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/openeoEquivalence
      x-jsonld-id: '@nest'
    itemClass:
      const: https://w3id.org/ogc/rim/activity-type/activityTypeItemClass
      x-jsonld-id: https://w3id.org/ogc/rim/itemClass
      x-jsonld-type: '@id'
    inRegister:
      const: https://geolabs.github.io/bblocks-process-profiles/def/register
      x-jsonld-id: https://w3id.org/ogc/rim/inRegister
      x-jsonld-type: '@id'
    objectIdentifier:
      type: string
      format: uri
      description: The process-type entry IRI; permanently identifies this register
        item.
      x-jsonld-id: https://w3id.org/ogc/rim/objectIdentifier
      x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
    validityStatus:
      enum:
      - valid
      - invalid
      x-jsonld-id: https://w3id.org/ogc/rim/validityStatus
      x-jsonld-type: '@vocab'
    publicationStatus:
      enum:
      - published
      - unpublished
      x-jsonld-id: https://w3id.org/ogc/rim/publicationStatus
      x-jsonld-type: '@vocab'
    subClassOf:
      description: 'The parent class: acttype:ActivityType, or, for a process attached
        to an Implementation Profile, the activity type of its operation in bblocks-generic-profiles
        (decision D5, 2026-11-10). The enum is written by scripts/generate.py from
        the activity types of that register, so that no other value passes.'
      enum:
      - https://w3id.org/ogc/rim/activity-type/ActivityType
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/analytical-hillshading
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/area
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/buffer
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/centroid
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/contains
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/convex-hull
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/crosses
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/difference
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/disjoint
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/equals
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/geometry-extent
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/intersection
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/intersects
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/is-simple
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/otsu-thresholding
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-thinning
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-to-grid
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-to-shapes
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/product-selection
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/radiometric-index
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math-multiband
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-crop
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-extent
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-format-conversion
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-rendering
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-resampling
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/slope
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/symdifference
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/terrain-ruggedness-index
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/topographic-position-index
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/touches
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/union
      - https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/within
      x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#subClassOf
      x-jsonld-type: '@id'
    hasAction:
      description: 'The register actions of the entry: its addition, then each in-place
        amendment of the proposal (pp:amendmentAction, pp:specification). The schema
        requires the addition; it does not constrain the action type or the classification
        of the other actions (decision Q5, option b, of 2026-11-11: pending a decision
        common to all registers).'
      type: array
      minItems: 1
      items:
        anyOf:
        - type: object
          required:
          - id
          - type
          - actionType
          - proposer
          - startedAtTime
          - appliesTo
          properties:
            id:
              type: string
              format: uri
              x-jsonld-id: '@id'
            type:
              const: RegisterAction
              x-jsonld-id: '@type'
            actionType:
              const: addition
              x-jsonld-id: https://w3id.org/ogc/rim/actionType
              x-jsonld-type: '@vocab'
            proposer:
              const: https://geolabs.github.io/bblocks-process-profiles/def/geolabs
              x-jsonld-id: https://w3id.org/ogc/rim/proposer
              x-jsonld-type: '@id'
            startedAtTime:
              type: string
              format: date-time
              x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
            appliesTo:
              type: string
              format: uri
              x-jsonld-id: https://w3id.org/ogc/rim/appliesTo
              x-jsonld-type: '@id'
        - type: object
          required:
          - id
          - type
          - actionType
          - description
          - proposer
          - startedAtTime
          - appliesTo
          properties:
            id:
              type: string
              format: uri
              x-jsonld-id: '@id'
            type:
              const: RegisterAction
              x-jsonld-id: '@type'
            actionType:
              type: string
              x-jsonld-id: https://w3id.org/ogc/rim/actionType
              x-jsonld-type: '@vocab'
            description:
              type: string
              x-jsonld-id: http://purl.org/dc/terms/description
            proposer:
              const: https://geolabs.github.io/bblocks-process-profiles/def/geolabs
              x-jsonld-id: https://w3id.org/ogc/rim/proposer
              x-jsonld-type: '@id'
            startedAtTime:
              type: string
              format: date-time
              x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
            appliesTo:
              type: string
              format: uri
              x-jsonld-id: https://w3id.org/ogc/rim/appliesTo
              x-jsonld-type: '@id'
      contains:
        type: object
        required:
        - id
        - type
        - actionType
        - proposer
        - startedAtTime
        - appliesTo
        properties:
          id:
            type: string
            format: uri
            x-jsonld-id: '@id'
          type:
            const: RegisterAction
            x-jsonld-id: '@type'
          actionType:
            const: addition
            x-jsonld-id: https://w3id.org/ogc/rim/actionType
            x-jsonld-type: '@vocab'
          proposer:
            const: https://geolabs.github.io/bblocks-process-profiles/def/geolabs
            x-jsonld-id: https://w3id.org/ogc/rim/proposer
            x-jsonld-type: '@id'
          startedAtTime:
            type: string
            format: date-time
            x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
          appliesTo:
            type: string
            format: uri
            x-jsonld-id: https://w3id.org/ogc/rim/appliesTo
            x-jsonld-type: '@id'
      x-jsonld-id: https://w3id.org/ogc/rim/hasAction
      x-jsonld-type: '@id'
    usedEntityType:
      description: 'acttype:usedEntityType: the GeoSPARQL class(es) of the parent
        activity type, repeated (decision of 2026-11-10).'
      anyOf:
      - enum:
        - http://www.opengis.net/ont/geosparql#SpatialObject
        - http://www.opengis.net/ont/geosparql#Feature
        - http://www.opengis.net/ont/geosparql#Geometry
        - http://www.opengis.net/ont/geosparql#SpatialObjectCollection
        - http://www.opengis.net/ont/geosparql#FeatureCollection
        - http://www.opengis.net/ont/geosparql#GeometryCollection
      - type: array
        minItems: 1
        items:
          enum:
          - http://www.opengis.net/ont/geosparql#SpatialObject
          - http://www.opengis.net/ont/geosparql#Feature
          - http://www.opengis.net/ont/geosparql#Geometry
          - http://www.opengis.net/ont/geosparql#SpatialObjectCollection
          - http://www.opengis.net/ont/geosparql#FeatureCollection
          - http://www.opengis.net/ont/geosparql#GeometryCollection
      x-jsonld-id: https://w3id.org/ogc/rim/activity-type/usedEntityType
      x-jsonld-type: '@id'
    generatedEntityType:
      description: 'acttype:generatedEntityType: the GeoSPARQL class(es) of the parent
        activity type, repeated (decision of 2026-11-10).'
      anyOf:
      - enum:
        - http://www.opengis.net/ont/geosparql#SpatialObject
        - http://www.opengis.net/ont/geosparql#Feature
        - http://www.opengis.net/ont/geosparql#Geometry
        - http://www.opengis.net/ont/geosparql#SpatialObjectCollection
        - http://www.opengis.net/ont/geosparql#FeatureCollection
        - http://www.opengis.net/ont/geosparql#GeometryCollection
      - type: array
        minItems: 1
        items:
          enum:
          - http://www.opengis.net/ont/geosparql#SpatialObject
          - http://www.opengis.net/ont/geosparql#Feature
          - http://www.opengis.net/ont/geosparql#Geometry
          - http://www.opengis.net/ont/geosparql#SpatialObjectCollection
          - http://www.opengis.net/ont/geosparql#FeatureCollection
          - http://www.opengis.net/ont/geosparql#GeometryCollection
      x-jsonld-id: https://w3id.org/ogc/rim/activity-type/generatedEntityType
      x-jsonld-type: '@id'
  additionalProperties: true
  allOf:
  - not:
      required:
      - notAttached
      - implementsProfile
  - if:
      required:
      - subClassOf
      properties:
        subClassOf:
          not:
            const: https://w3id.org/ogc/rim/activity-type/ActivityType
    then:
      anyOf:
      - required:
        - usedEntityType
      - required:
        - generatedEntityType
x-jsonld-extra-terms:
  ProcessType: https://geolabs.github.io/bblocks-process-profiles/def/ProcessType
  ActivityType: https://w3id.org/ogc/rim/activity-type/ActivityType
  owlClass: http://www.w3.org/2002/07/owl#Class
  Plan: http://www.w3.org/ns/prov#Plan
  valid: https://w3id.org/ogc/rim/valid
  invalid: https://w3id.org/ogc/rim/invalid
  published: https://w3id.org/ogc/rim/published
  unpublished: https://w3id.org/ogc/rim/unpublished
  addition: https://w3id.org/ogc/rim/additionAction
  changeClassification:
    x-jsonld-id: https://w3id.org/ogc/rim/changeClassification
    x-jsonld-type: '@vocab'
  substantive: https://w3id.org/ogc/rim/substantiveChange
  clarifying: https://w3id.org/ogc/rim/clarifyingChange
x-jsonld-prefixes:
  pp: https://geolabs.github.io/bblocks-process-profiles/def/
  acttype: https://w3id.org/ogc/rim/activity-type/
  owl: http://www.w3.org/2002/07/owl#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  prov: http://www.w3.org/ns/prov#
  skos: http://www.w3.org/2004/02/skos/core#
  rim: https://w3id.org/ogc/rim/
  xsd: http://www.w3.org/2001/XMLSchema#
  dct: http://purl.org/dc/terms/
  oa: http://www.w3.org/ns/oa#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
x-bblocks-metadata:
  itemIdentifier: ospd.process-profiles.process-type
  register: https://geolabs.github.io/bblocks-process-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "Register": "rim:Register",
    "RegisterSystem": "rim:RegisterSystem",
    "RegisterSpecification": "rim:RegisterSpecification",
    "RegisterItemClass": "rim:RegisterItemClass",
    "RegisterItem": "rim:RegisterItem",
    "RegisterAction": "rim:RegisterAction",
    "Concept": "rim:Concept",
    "ConceptVersion": "rim:ConceptVersion",
    "ConceptSystem": "rim:ConceptSystem",
    "Commitment": "rim:Commitment",
    "Agent": "prov:Agent",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "label": "rdfs:label",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "runsOn": {
      "@id": "rim:runsOn",
      "@type": "@id"
    },
    "hasSpecification": {
      "@id": "rim:hasSpecification",
      "@type": "@id"
    },
    "definesSubstantiveChange": "rim:definesSubstantiveChange",
    "registerOwner": {
      "@id": "rim:registerOwner",
      "@type": "@id"
    },
    "registerManager": {
      "@id": "rim:registerManager",
      "@type": "@id"
    },
    "controlBody": {
      "@id": "rim:controlBody",
      "@type": "@id"
    },
    "registerSystemManager": {
      "@id": "rim:registerSystemManager",
      "@type": "@id"
    },
    "registerUser": {
      "@id": "rim:registerUser",
      "@type": "@id"
    },
    "hasCommitment": {
      "@id": "rim:hasCommitment",
      "@type": "@id"
    },
    "commitmentCategory": {
      "@id": "rim:commitmentCategory",
      "@type": "@vocab"
    },
    "access": "rim:accessCommitment",
    "persistence": "rim:persistenceCommitment",
    "transparency": "rim:transparencyCommitment",
    "definedIn": {
      "@id": "rim:definedIn",
      "@type": "@id"
    },
    "validatedBy": {
      "@id": "rim:validatedBy",
      "@type": "@id"
    },
    "versionOf": {
      "@id": "rim:versionOf",
      "@type": "@id"
    },
    "version": "rim:version",
    "valid": "rim:valid",
    "invalid": "rim:invalid",
    "published": "rim:published",
    "unpublished": "rim:unpublished",
    "appliesTo": {
      "@id": "rim:appliesTo",
      "@type": "@id"
    },
    "proposer": {
      "@id": "rim:proposer",
      "@type": "@id"
    },
    "actionType": {
      "@id": "rim:actionType",
      "@type": "@vocab"
    },
    "addition": "rim:additionAction",
    "publish": "rim:publishAction",
    "unpublish": "rim:unpublishAction",
    "invalidation": "rim:invalidationAction",
    "supersession": "rim:supersessionAction",
    "redaction": "rim:redactionAction",
    "deletion": "rim:deletionAction",
    "changeClassification": {
      "@id": "rim:changeClassification",
      "@type": "@vocab"
    },
    "substantive": "rim:substantiveChange",
    "clarifying": "rim:clarifyingChange",
    "correctional": "rim:correctionalChange",
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "id": "@id",
    "type": "@type",
    "objectIdentifier": {
      "@id": "rim:objectIdentifier",
      "@type": "xsd:anyURI"
    },
    "functionalIdentifier": {
      "@id": "rim:functionalIdentifier",
      "@type": "xsd:anyURI"
    },
    "itemClass": {
      "@id": "rim:itemClass",
      "@type": "@id"
    },
    "inRegister": {
      "@id": "rim:inRegister",
      "@type": "@id"
    },
    "realizes": {
      "@id": "rim:realizes",
      "@type": "@id"
    },
    "validityStatus": {
      "@id": "rim:validityStatus",
      "@type": "@vocab"
    },
    "publicationStatus": {
      "@id": "rim:publicationStatus",
      "@type": "@vocab"
    },
    "isRedacted": {
      "@id": "rim:isRedacted",
      "@type": "xsd:boolean"
    },
    "isDeleted": {
      "@id": "rim:isDeleted",
      "@type": "xsd:boolean"
    },
    "title": "dct:title",
    "description": "dct:description",
    "relatedItem": {
      "@id": "rim:relatedItem",
      "@type": "@id"
    },
    "supersededBy": {
      "@id": "rim:supersededBy",
      "@type": "@id"
    },
    "supersedes": {
      "@id": "rim:supersedes",
      "@type": "@id"
    },
    "hasAction": {
      "@id": "rim:hasAction",
      "@type": "@id"
    },
    "usedEntityType": {
      "@id": "rim:activity-type/usedEntityType",
      "@type": "@id"
    },
    "generatedEntityType": {
      "@id": "rim:activity-type/generatedEntityType",
      "@type": "@id"
    },
    "associatedAgentType": {
      "@id": "rim:activity-type/associatedAgentType",
      "@type": "@id"
    },
    "informedByActivityType": {
      "@id": "rim:activity-type/informedByActivityType",
      "@type": "@id"
    },
    "phase": {
      "@id": "pp:phase",
      "@type": "@id"
    },
    "classification": "@nest",
    "deployment": {
      "@context": {
        "profile": "pp:profile",
        "processDescription": {
          "@context": {
            "version": "pp:version",
            "href": {
              "@id": "rdfs:seeAlso",
              "@type": "@id"
            },
            "license": {
              "@id": "dct:license",
              "@type": "@id"
            }
          },
          "@id": "pp:processDescription"
        },
        "provenanceClass": {
          "@id": "pp:provenanceClass",
          "@type": "@id"
        }
      },
      "@id": "pp:deployment"
    },
    "plan": {
      "@context": {
        "executionUnit": {
          "@context": {
            "href": {
              "@id": "oa:hasTarget",
              "@type": "@id"
            },
            "type": "dct:format",
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            }
          },
          "@id": "https://w3id.org/ogc/api/processes/executionUnit"
        },
        "cwlClass": "pp:cwlClass",
        "cwlId": "pp:cwlId",
        "license": {
          "@id": "dct:license",
          "@type": "@id"
        },
        "cctDependencies": "pp:cctDependency",
        "candidateCctDependencies": "pp:candidateCctDependency"
      },
      "@id": "pp:plan"
    },
    "serverSideFiles": {
      "@context": {
        "name": "pp:liveName",
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "location": "pp:location"
      },
      "@id": "pp:serverSideFile"
    },
    "byReference": {
      "@context": {
        "name": "pp:liveName",
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "note": "skos:note"
      },
      "@id": "pp:byReference"
    },
    "unboundRoles": {
      "@context": {
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "reason": "skos:note"
      },
      "@id": "pp:unboundRole"
    },
    "fixedRoleValues": {
      "@context": {
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "values": "rdf:value",
        "reason": "skos:note"
      },
      "@id": "pp:fixedRoleValue"
    },
    "roleDecompositions": {
      "@context": {
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "parts": {
          "@id": "pp:part",
          "@container": "@list"
        },
        "note": "skos:note",
        "selectors": {
          "@context": {
            "name": "pp:liveName",
            "values": "rdf:value"
          },
          "@id": "pp:selector"
        },
        "reproducible": {
          "@id": "pp:reproducible",
          "@type": "xsd:boolean"
        }
      },
      "@id": "pp:roleDecomposition"
    },
    "assumedFormatGaps": {
      "@context": {
        "name": "pp:liveName",
        "side": "pp:side",
        "implements": {
          "@id": "pp:implements",
          "@type": "@id"
        },
        "served": "pp:servedMediaType",
        "reason": "skos:note",
        "evidence": "pp:evidence"
      },
      "@id": "pp:assumedFormatGap"
    },
    "notAttached": {
      "@context": {
        "reason": "skos:note"
      },
      "@id": "pp:notAttached"
    },
    "implementsProfile": {
      "@id": "pp:implementsProfile",
      "@type": "@id"
    },
    "hasStep": {
      "@id": "pp:hasStep",
      "@type": "@id"
    },
    "exactMatch": {
      "@id": "skos:exactMatch",
      "@type": "@id"
    },
    "closeMatch": {
      "@id": "skos:closeMatch",
      "@type": "@id"
    },
    "relatedMatch": {
      "@id": "skos:relatedMatch",
      "@type": "@id"
    },
    "openeoEquivalence": {
      "@context": {
        "level": "pp:equivalenceLevel",
        "rationale": "pp:rationale",
        "decomposition": {
          "@context": {
            "stage": "pp:stage",
            "openeo": "pp:openeo",
            "note": "skos:note"
          },
          "@id": "pp:decomposition",
          "@container": "@list"
        }
      },
      "@id": "pp:openeoEquivalence"
    },
    "correspondences": "@nest",
    "subClassOf": {
      "@id": "rdfs:subClassOf",
      "@type": "@id"
    },
    "ProcessType": "pp:ProcessType",
    "ActivityType": "rim:activity-type/ActivityType",
    "owlClass": "owl:Class",
    "Plan": "prov:Plan",
    "rim": "https://w3id.org/ogc/rim/",
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "acttype": "rim:activity-type/",
    "pp": "https://geolabs.github.io/bblocks-process-profiles/def/",
    "oa": "http://www.w3.org/ns/oa#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld)

## Sources

* [Registered Item Model](https://ogcincubator.github.io/registered-item-model/)
* [Activity Type Register](https://ogcincubator.github.io/activity-type-register/)
* [W3C PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/)
* [SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/process-type`

