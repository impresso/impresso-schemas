# Common Schema Consolidation and Modularisation Plan

## Purpose

This plan coordinates the deliberate design of reusable Impresso 2 schema
definitions. The objective is not merely to remove duplicated JSON Schema
snippets. Each shared definition must document one stable Impresso concept,
with agreed semantics, validation rules, examples, ownership, and adoption
rules.

This is a staged design and migration effort. It requires discussion with the
teams that produce and consume the data before further common fragments are
introduced.

## Current state

The Impresso 2 namespace has two cross-lifecycle object fragments under
`json/impresso-2/common/`:

| Fragment | Shared property | Current consumers |
| --- | --- | ---: |
| `content-item-id.part.v1.schema.json` | `ci_id` | 12 |
| `model-id.part.v1.schema.json` | `model_id` | 6 |

Both are object fragments composed through `allOf`. Each consuming schema keeps
its own `required` list, so requiredness remains local to the document contract.

The content-item fragment has also introduced an intentional Impresso 2 field
change: selected copied schemas now use `ci_id` where their legacy counterpart
uses `id`.

The Solr schemas already have a separate, mature modular structure under
`json/impresso-2/solr-indexing/`. They remain Solr-local: JSON Schema `$ref`
can share validation rules but cannot define the transformation between a
pipeline representation and Solr fields such as `lg_s`.

Some semantic-enrichment schemas are expected to disappear, including chunk
and sentence embeddings; entity embeddings are also planned for removal. Do
not extend those schemas with new shared fragments.

## Compatibility and adoption status

Impresso 2 schemas are an evolving contract and are **not yet asserted to
validate every existing production dataset**. In particular, current rebuilt
data may still contain `id` where the Impresso 2 rebuilt schemas now require
`ci_id`.

This creates an intentional transition gap between legacy data contracts and
the new namespace. It has consequences for all producer and consumer code:

- A consumer must select the legacy or Impresso 2 schema explicitly; it must
  not silently substitute one for the other.
- Existing producer output must be validated against the selected contract
  before a consumer switches namespaces.
- If the data shape changes, producer updates, a documented adapter, or a
  versioned migration are required. A `$ref` alone does not transform `id` into
  `ci_id`.
- A schema/example test proves the fixture, not the full production corpus.
  Representative real-data validation is required before adoption.

Legacy schemas, paths, and `$id` values remain stable throughout this work.

## Design principles

1. **Semantics before reuse.** Extract a definition only after its meaning and
   lifecycle role are agreed, not because two fields have the same spelling.
2. **Narrowest useful scope.** Use the root `common/` directory only when a
   concept is genuinely shared across lifecycle areas. Keep reuse limited to
   one lifecycle area under `<lifecycle-area>/common/`.
3. **One canonical property name per concept.** When a common object fragment
   defines a property name, new Impresso 2 contracts use that name. Existing
   deviations require an explicit compatibility decision.
4. **No hidden contract tightening.** Do not add a pattern, enum, requiredness,
   or nullability constraint until representative data and consumers support
   it.
5. **Keep serialisations separate.** Solr and future web-app schemas may share
   a semantic primitive only when their value contract is identical. Their
   field names and object structures remain local.
6. **Version deliberately.** A change that invalidates previously valid data or
   changes semantics creates a new fragment version and requires a consumer
   adoption plan.

## Target modular structure

```text
json/impresso-2/
├── common/                                  Cross-lifecycle concepts only
│   ├── content-item-id.part.v1.schema.json
│   └── model-id.part.v1.schema.json
├── data-preparation/
│   └── common/                              Data-preparation-only fragments
├── text-processing/
│   └── common/                              Text-processing-only fragments
├── semantic-enrichment/
│   └── common/                              Semantic-enrichment-only fragments
├── solr-indexing/                           Solr-specific parts remain local
└── web-app/                                 Future web-app-specific parts
```

Naming rules:

- `<concept>.vN.schema.json` — standalone reusable scalar or object.
- `<concept>.part.vN.schema.json` — object fragment composed through `allOf`.
- Do not use `shared` in filenames; directory location states the reuse scope.

## Workstream 1: Build the evidence base

Before proposing another fragment, create a maintained common-schema register.
It may start as `COMMON-SCHEMA-REGISTER.md` and should record one row per
candidate concept.

For every candidate, collect:

- current schema paths, property paths, and lifecycle areas;
- whether the property is supplied directly, through `$defs`, or through an
  `allOf` fragment;
- actual type, nullability, requiredness, pattern, enum, default, and examples;
- descriptions and their semantic differences;
- representative real data from each producer;
- producers, consumers, and any storage or serialisation mappings;
- legacy equivalent, Impresso 2 equivalent, and migration status;
- decision, owner, review date, and follow-up issue.

The inventory must resolve cross-file fragments. A simple scan of root
`properties` is insufficient after modularisation because `ci_id` and
`model_id` are now contributed through `allOf`.

## Workstream 2: Define each concept

For each shortlisted definition, prepare a concept card and review it with the
relevant producers and consumers.

Each card must state:

- canonical concept and canonical property name;
- plain-language definition and lifecycle meaning;
- scope: root `common/` or one lifecycle area's `common/` directory;
- JSON type, nullability, requiredness policy, pattern/enum, and examples;
- positive and negative validation examples;
- aliases or legacy field names and their mapping rules;
- source schema owners and downstream consumers;
- compatibility impact and versioning decision.

Only after approval should a concept become a shared schema fragment.

### Collaboration and issue workflow

Use one design issue for each shortlisted concept. The collaborator responsible
for the affected producer or consumer prepares the concept card in that issue,
using the register as evidence. Relevant producers and consumers then review
the proposed meaning, scope, constraints, examples, compatibility impact, and
ownership.

For a small, already-agreed concept, the approved card and implementation may
remain in one issue and one pull request. For cross-lifecycle concepts (for
example timestamps, language codes, or provenance), keep design approval and
implementation in separate issues: no schema change begins until the card is
approved. An implementation issue must link to the approved design issue and
record the exact consumer schemas it may change.

### Concept-card example: embedding vector record

This illustrative card is deliberately unresolved. It shows the level of
decision required before extracting a semantic-enrichment-local fragment.

| Card element | Draft content |
| --- | --- |
| Status | Draft for discussion |
| Scope | `json/impresso-2/semantic-enrichment/common/` |
| Proposed schema | `embedding-vector.part.v1.schema.json` |
| Meaning | Numeric vector representation produced for one input unit by an embedding model. The fragment defines only the vector payload and its declared dimensionality. |
| Proposed properties | `embedding`: numeric vector; `size`: number of dimensions in each vector. |
| Separate concepts | `ci_id` and `model_id` remain root-common fragments. `ts` remains outside this card until timestamp semantics are agreed. |
| Candidate consumers | `document-embeddings/embeddings-docs.v1.schema.json` and `image-embeddings/image-embeddings.v1.schema.json` |
| Compatibility | No field renaming proposed: both consumers already expose `embedding` and `size`. Validate real output before adding constraints such as `minimum: 1` or a vector-length consistency rule. |

Current evidence identifies a material difference: document embeddings permit a
single numeric vector **or** a list of vectors, while image embeddings permit
only one vector. The card must resolve whether a shared fragment covers only a
single vector, permits both forms, or leaves multi-vector document output
local. It must also confirm that `size` means vector dimensionality in both
schemas, name the responsible owners, and include positive and negative
examples before implementation.

## Candidate backlog for review

The following are discussion candidates, not an instruction to extract them
now.

| Scope | Candidate | Why it may be reusable | Questions to resolve first |
| --- | --- | --- | --- |
| Root `common/` | `ts` / generated timestamp | Present across data preparation, text processing, and semantic enrichment | Does it always mean generation time? Must it be UTC `Z`, any RFC 3339 offset, or an unconstrained date-time? |
| Root `common/` | Language code | Used in several lifecycle areas | ISO 639-1 vs 639-2/3, nullable values, original vs computed language, and code-list governance differ today. |
| Root `common/` | Processing provenance | Model, code revision, run path, and generated timestamp recur conceptually | Agree a stable provenance vocabulary before creating a multi-property fragment. |
| Data preparation | Source metadata | `st`, `sm`, and related media metadata recur in canonical and rebuilt schemas | Agree common source-type and source-medium enumerations, and how radio-specific metadata is grouped. |
| Data preparation | Rebuilt content-item metadata | Paper and audio rebuilt schemas duplicate several fields | Decide which fields truly apply to both supports and how the `ci_id` transition affects actual data. |
| Semantic enrichment | Embedding record metadata | Document and image embeddings share `ci_id`, `model_id`, vector size, and timestamp concepts | Decide whether vector shape, dimensionality, and modality are one contract or separate ones. |
| Text processing | Language-identification and annotation provenance | Tool/version metadata appears in several outputs | Resolve the current mix of version objects, paths, and model identifiers. |
| Solr indexing | Existing Solr parts | Already modularised | Keep Solr-specific unless an agreed value-level primitive has exactly the same semantics. |

## Workstream 3: Validate real data and consumer impact

For every proposed or changed Impresso 2 contract:

1. Select representative samples from every active producer, including older
   and recent outputs, media types, and known edge cases.
2. Validate the samples against both the legacy and proposed Impresso 2 schema.
3. Classify every difference as one of:
   - expected legacy-only shape;
   - intentional Impresso 2 migration;
   - producer defect or stale data;
   - schema defect;
   - undecided.
4. Record the result in the common-schema register and migration mapping.
5. Inventory consumer code to identify which namespace each consumer imports or
   resolves by URL.
6. For each consumer switch, choose one route explicitly:
   - continue using the legacy schema;
   - update producer and consumer together for Impresso 2;
   - introduce and test a documented adapter;
   - defer the switch.

No consumer should move to Impresso 2 based solely on path availability or a
passing fixture test.

## Workstream 4: Incremental implementation

Implement one approved concept at a time.

1. Add the fragment with a complete `$schema`, path-matching `$id`, title,
   description, validation rules, and examples.
2. Update only the approved consumer schemas. Use `allOf` for a named object
   property fragment; keep document-specific requiredness local unless it is
   explicitly part of the shared contract.
3. Update valid and invalid examples, and register every applicable example in
   `tests/test_schema_examples.py`.
4. Add targeted negative tests when a new pattern, enum, or nullability rule is
   introduced.
5. Update the common-schema register, `MIGRATION-MAPPING.md`, README, and
   conventions with the decision and adoption implications.
6. Run `make tests`, `git diff --check`, and formatting/documentation commands
   available in the development environment.
7. Stop for review before beginning the next concept.

## Test and documentation requirements

For a shared fragment, tests must establish both that the fragment resolves
locally and that each registered consumer validates a representative document.
Where possible, add a fixture that fails specifically when the common rule is
violated.

Generated schema documentation is not enough. The source description must be
understandable without implementation context, and the common-schema register
must document semantic choices, aliases, and adoption status.

## Delivery checkpoints

| Checkpoint | Deliverable | Review question |
| --- | --- | --- |
| 1. Inventory | Resolved property matrix and initial register | Which candidates are truly the same concept? |
| 2. Compatibility | Real-data validation and consumer map | Which Impresso 2 changes are safe, and who must migrate? |
| 3. Concept approval | Reviewed concept cards | Are name, semantics, validation, examples, and scope agreed? |
| 4. Pilot | One approved fragment and affected fixtures | Does modularisation preserve the intended contract? |
| 5. Adoption | Producer/consumer migration decision | Can a consumer safely select the Impresso 2 namespace? |
| 6. Release | Updated mapping, docs, and test evidence | Is the fragment stable enough for reuse? |

## Issue planning after review

After this plan and the first inventory are approved, create bounded issues for:

1. common-schema register and resolved property-inventory tooling;
2. real-data compatibility audit for rebuilt and content-item consumers;
3. consumer namespace/import inventory;
4. one issue per approved semantic concept or lifecycle-local fragment;
5. producer/adaptor migration work for each intentional shape change;
6. retirement of chunk, sentence, and entity embedding schemas where confirmed.

Do not create extraction issues from the candidate backlog until the concept and
compatibility checkpoints have been completed.
