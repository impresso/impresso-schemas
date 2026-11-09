# Solr indexing JSON schemas

This directory defines the JSON documents used for Solr indexing in the
[Impresso schema repository](../../../README.md). It covers content items and
separate documents for entities, aggregate mentions, topics, text reuse, and
embeddings.

Solr indexing is one stage of the wider Impresso data lifecycle:

```text
Data preparation → Text processing → Semantic enrichment → Solr indexing → Application
```

The upstream [semantic-enrichment schemas](../semantic-enrichment/) describe
processing outputs such as NER and entity-linking annotations. The schemas here
describe their Solr-facing representations, including denormalized fields on
content items. Importer code remains in `impresso-pyindexing`; this repository
provides the versioned contracts, examples, validation, and documentation.

These are **JSON Schemas**, not Solr managed schemas or `solrconfig.xml`.
They do not configure analyzers, dynamic fields, indexing, storage, copy fields,
or suggesters. Some optional properties document fields populated by Solr,
such as `entitySuggest` and `mentionSuggest`; a submitted document and a Solr
query response need not have identical shapes.

## Layout and versioning

Paths below are relative to the repository root:

```text
json/impresso-2/solr-indexing/
├── content-item/          Complete CI schemas and reusable field fragments
└── semantic-enrichments/  Entity, mention, topic, text-reuse and embedding schemas

examples/impresso-2/solr-indexing/
├── content-item/
└── semantic-enrichments/

tests/                    Schema integrity, reference and example validation
```

All schemas use JSON Schema draft 2020-12. Their published `$id` must match
their complete repository path under
`https://impresso.github.io/impresso-schemas/`.

- `*.root.*.vN.schema.json` defines a complete document.
- `*.part.*.vN.schema.json` defines fields composed into a document using
  `allOf` and `$ref`.
- Versions apply to individual contracts. A v2 root can reuse unchanged v1
  fragments; it does not require every dependency to have a v2 filename.

Older versions remain available for their existing consumers. Solr schemas
live in the Impresso 2 namespace, including their v1 files; this is distinct
from the repository's top-level legacy namespace. Select the root version
that matches the producer and consumer rather than assuming the highest
number describes every deployed index.

See [schema conventions](../../../SCHEMA_CONVENTIONS.md) for repository-wide
naming and documentation rules.

### New-representation baseline (v3)

The v3 baseline identifies Solr contracts ready for the QID-based entity and
surface/type mention representation. This is a one-time alignment: roots and
their Solr fragments start together at v3, then evolve independently. It is
not a permanent marker for whichever version is active in a deployment.

The baseline entry points are paper, audio, image, entities, mentions, topics,
text-reuse clusters, and word embeddings. All their dependencies within
`solr-indexing` use v3. Shared enums and image typology definitions outside
this directory retain their independent versions.

Text-reuse passages and entity profiles are **pending**, not part of this
baseline. Passage root/part schemas remain v1 until revised; entity profiles
need clarification of internal entity IDs and mention keys before promotion.
Earlier contracts remain available with their existing paths and identifiers.

These source schemas still use `$ref`. Self-contained exports for consumers
that cannot resolve references are generated artifacts, not separate source
contracts; v3 filenames alone do not make a schema self-contained.

### Entity/mention representation compatibility

Two representation families coexist. **Previous representation** refers to
the earlier entity/mention contracts. **QID-based entity and surface/type
mention representation** refers to the new contracts. These names identify
the data model, not a deployed environment or a repository-wide version.

| Contract | Previous representation | QID-based entity and surface/type mention representation |
| --- | --- | --- |
| Entity documents | Entities v1/v2 | Entities v3 |
| Aggregate mention documents | Mentions v1/v2 and ordinary mentions v2 | Mentions v3, shared by all five types |
| Paper/audio content-item roots | CI v1 | CI v2 and v3 |
| CI text semantic-enrichment fragment | Text semantic enrichments v1 | Baseline: text semantic enrichments v3 → entity/mention fragment v3. Earlier new-representation chain: v2 → v1. |

CI v2 already uses the new representation. CI v3 adds transcript changes and
now selects v3 fragments throughout the Solr dependency chain. The baseline
copies preserve the validation rules of their source fragments; the version
alignment itself introduces no new fields or constraints. CI roots compose
field fragments, not the separate entity or aggregate-mention document schemas.

The previous representation retains fields such as `pers_mentions`,
`pers_entities_dpfs`, and `nag_mentions`. The new representation uses QIDs,
`a1_…` surface/type aggregate IDs, and ordered occurrence fields described
below. Existing schema paths and `$id` values remain available for consumers
of either representation. “Previous” does not denote an exact snapshot of all
files before this change: shared fragments can include independent additions,
such as section metadata in transcript v1.

## Content-item schemas

The roots compose the following fragments. Names in this table omit the
`content-item.part.` prefix and version suffix for readability.

| Family | Latest entry point | Earlier entry points | Composed field groups |
| --- | --- | --- | --- |
| Paper | [v3](content-item/content-item.root.paper.v3.schema.json) | [v1](content-item/content-item.root.paper.v1.schema.json), [v2](content-item/content-item.root.paper.v2.schema.json) | Core, contextual metadata, access rights, text transcript, text semantic enrichments, paper support |
| Audio | [v3](content-item/content-item.root.audio.v3.schema.json) | [v1](content-item/content-item.root.audio.v1.schema.json), [v2](content-item/content-item.root.audio.v2.schema.json) | Core, contextual metadata, provider metadata, access rights, text transcript, text semantic enrichments, audio support |
| Image | [v3](content-item/content-item.root.image.v3.schema.json) | [v1](content-item/content-item.root.image.v1.schema.json) | Core, contextual metadata, access rights, image fields, image semantic enrichments |

“Latest” identifies the highest available root version, not deployment status.
Select the representation using the compatibility table above, and pin the
corresponding committed schema revision in the indexing application.

Paper roots cover printed and typescripted sources. Their paper-support
fragment carries page references, layout and text-region information; they
do not compose the standalone image-content fragment. Audio support carries
record references and timing/utterance structure. Provider metadata uses the
`meta_prv_` prefix for values passed through without cross-provider
harmonization. Image-specific enrichments include classification, keywords,
and embeddings.

Paper/audio v1 roots use
[text semantic enrichments v1](content-item/content-item.part.text.semantic-enrichments.v1.schema.json),
including the older entity/mention fields. Paper/audio v2 retain
[text semantic enrichments v2](content-item/content-item.part.text.semantic-enrichments.v2.schema.json)
and entity/mention fragment v1. Paper/audio v3 use
[text semantic enrichments v3](content-item/content-item.part.text.semantic-enrichments.v3.schema.json),
which retains OCR QA, topics, text-reuse cluster IDs and document embeddings,
and composes the dedicated
[entity/mention fragment v3](content-item/content-item.part.text.semantic-enrichments-entity-mentions.v3.schema.json).
Paper/audio v3 select [transcript v3](content-item/content-item.part.text.transcript.v3.schema.json),
a baseline copy of transcript v2, including Portuguese body acceptance and
string validation for generic section titles. Paper/audio v1/v2 retain
transcript v1.

### Entity and mention fields on v2/v3 content items

The type prefixes are `pers`, `loc`, `org`, `pressagency`, and
`radiostation`. In this representation `pressagency` replaces `nag`;
`time` and `prod` are excluded.

| Field family | Representation and meaning |
| --- | --- |
| `[type]_mention_surfaces_json_plain` | A JSON string encoding ordered exact occurrence surfaces |
| `[type]_mention_offsets_json_plain` | A JSON string encoding ordered body-relative `[start,length]` pairs |
| `[type]_mention_qids_json_plain` | A JSON string encoding ordered QIDs or `null` for NIL occurrences |
| `[type]_aggregate_mention_ids_ss` | Unique aggregate mention IDs present in the CI, including NIL forms |
| `[type]_mention_ner_conf_dpfs` | String-array payload representation of occurrence surfaces and NER confidence on the 0–1 scale |
| `[type]_entity_ids_dpfs` | String-array payload representation of QIDs and linked-occurrence counts within the CI/type |

The table lists body-scoped fields. Each also has a title-scoped counterpart
with `_title_` after the type, for example
`pers_title_mention_offsets_json_plain` and `pers_title_entity_ids_dpfs`.
Body offsets refer to the body text; title offsets are intended to refer to
the indexed CI title. Coordinate units and the source text must agree between
producer and consumer.

The first three fields hold serialized JSON, not native arrays in the outer
document. Decode them once. They describe the same occurrence sequence:
preserve repetitions and null positions, and omit all three together when a
type has no occurrences in that scope. Body and title sequences are separate.
Aggregate membership and entity-count payloads are not
positionally aligned occurrence lists, and confidence payload order must not
be assumed to align either.

The JSON Schema checks the outer string type; parsing, matching lengths,
validating decoded elements and checking spans against the served text
require supplemental producer/consumer checks. Individual occurrence IDs and
a separate mention-occurrence collection are outside this representation.

## Separate semantic-enrichment documents

These are distinct from enrichment fields embedded in a CI.

| Schema | Purpose |
| --- | --- |
| Entities [v1](semantic-enrichments/sem.root.entities.v1.schema.json), [v2](semantic-enrichments/sem.root.entities.v2.schema.json) | Earlier composite entity identifiers, labels, types and frequencies |
| Entities [v3](semantic-enrichments/sem.root.entities.v3.schema.json) | QID-based entity documents for `09_impresso_entities`, with labels, NER-derived type and integer counts |
| Mentions [v1](semantic-enrichments/sem.root.mentions.v1.schema.json), [v2](semantic-enrichments/sem.root.mentions.v2.schema.json), [ordinary v2](semantic-enrichments/sem.root.mentions.ordinary.v2.schema.json) | Earlier aggregate contracts, including their respective identifier rules |
| Mentions [v3](semantic-enrichments/sem.root.mentions.v3.schema.json) | Shared exact surface/type aggregates for `pers`, `loc`, `org`, `pressagency`, and `radiostation` in `08_impresso_mentions` |
| Entity profiles (pending) [v1](semantic-enrichments/sem.root.entity-profiles.v1.schema.json) | Separate entity-profile documents with encyclopedic/contextual information and embeddings |
| Topics [v3](semantic-enrichments/sem.root.topics.v3.schema.json), earlier [v1](semantic-enrichments/sem.root.topics.v1.schema.json) | Topic descriptions, model information and word probabilities |
| Text-reuse clusters [v3](semantic-enrichments/sem.root.tr-clusters.v3.schema.json), earlier [v1](semantic-enrichments/sem.root.tr-clusters.v1.schema.json) | Cluster membership and summary statistics |
| Text-reuse passages (pending) [v1](semantic-enrichments/sem.root.tr-passages.v1.schema.json) | Passage fields composed with selected CI metadata, rights, transcript and v1 text-enrichment fragments |
| Word embeddings [v3](semantic-enrichments/sem.root.wemb.v3.schema.json), earlier [v1](semantic-enrichments/sem.root.wemb.v1.schema.json) | Words, language codes and embedding vectors |

An **entity** in v3 is a Wikidata target, independent of its labels and
predicted types. `ner_entity_type_s` records one type selected from occurrence
evidence; the importer resolves ties. `content_item_count_l` is required,
while mention and per-type counts are optional. The current contract requires
a default label and `suggest_payload_s`, and permits language-specific labels
for the languages listed in its `patternProperties`.

An **aggregate mention** in v3 groups accepted occurrences with the same exact
surface and predicted type, including linked and NIL occurrences. It is not
an individual span or a document linked to one entity. The shared v3 contract
uses deterministic `a1_…` identifiers derived from `[surface,type]`; entity
QID, NIL status and body/title scope do not enter the key. Media-source types
use this same schema; there is no separate media-source mention schema.
`occurrence_count_l` and `suggest_payload_s` are required; the remaining
counts are optional.

Entity and aggregate-mention documents combine accepted body and title
annotations. Optional `scopes_ss` records their presence scopes; distinct-CI
counts use the union across scopes. Typed mention counts may overlap and
must not be summed to infer unique entity-span totals.
Entity-profile embedding documents remain a separate contract.

JSON Schema validates identifier shapes, not hash derivation, cross-document
links, or arithmetic relationships between counts. Those checks belong in
the producer and its tests. The schema keywords, including `required`, are
the validation contract; this overview does not replace them.

## Composition and validation boundaries

`allOf` validates each fragment against the **same complete document**.
Required properties from each fragment therefore apply to the composed root.

Do not set `additionalProperties: false` on a partial field fragment merely
to reject obsolete fields: it would also reject legitimate fields defined
by sibling fragments. Additional-property behavior varies across these
schemas; they are not uniformly permissive or strict.

Content-item roots declare `unevaluatedProperties: false`, but several
fragments explicitly allow additional properties. Consequently, the root
keyword alone does not guarantee rejection of every undeclared field.
Removing a field declaration likewise does not necessarily forbid it.

For offline validation, register local schemas by their `$id` and resolve
published `$ref` URLs against that registry. The repository implements this in
[tests/conftest.py](../../../tests/conftest.py); loading a root file alone
without its referenced schemas is insufficient for reliable offline validation.

## Examples and development workflow

[Examples](../../../examples/impresso-2/solr-indexing/) mirror the schema
hierarchy. The explicit mappings in
[tests/test_schema_examples.py](../../../tests/test_schema_examples.py)
determine which examples validate against which versions. Examples are
fixtures and may contain illustrative data.

- `ci_paper.v3.example.json` and `ci_audio.v3.example.json` exercise the new
  representation through paper/audio v3, including the Portuguese body field
  and generic section titles.
- `ci_paper.example.json` and `ci_typescript.example.json` exercise paper v1
  with the previous entity/mention representation.
- `ci_paper.v2.example.json` exercises paper v2 with the new entity/mention
  representation, which is retained in v3.
- The two image examples exercise both image v1 and baseline v3.
- Topic, text-reuse cluster and word-embedding examples exercise both v1 and v3.
- `ci_audio.example.json` is currently empty and excluded from example tests.
- Separate entity and mention examples cover the available registered versions.

Run commands from the repository root with the virtual environment activated:

```bash
source .venv/bin/activate
make tests-imp2
make tests
make format-check
make documentation-imp2
```

To validate only the Solr example cases:

```bash
python -m pytest tests/test_schema_examples.py -v -k 'content-item or sem.root'
```

The full suites also check Draft 2020-12 validity, unique/path-matching
identifiers, local reference resolution, and registered invalid cases.
Dependency setup is documented in the [repository README](../../../README.md).

For a new contract, add a versioned schema with a matching `$id`, preserve
existing published paths, provide corresponding examples, register their
test cases, and validate references and composition. Keep reusable fragments
within the lifecycle area where their semantics apply.

Documentation is generated from the JSON schemas into the gitignored
`docs/` tree for local preview and published by CI on pushes to `master`.
Browse the [published schema documentation](https://impresso.github.io/impresso-schemas/).
The old importer-local `validate_schemas.py` and Avro-generation workflow
are not this repository's validation interface.

### CI text contract history

Paper/audio v3 were introduced on 2026-10-20 using transcript v2 and semantic
enrichments v2. The baseline alignment selects equivalent v3 fragments.
Portuguese remains accepted among the required-body alternatives, and optional
`section_title_txt` must be a string. Legacy `content_txt_lb` and unrestricted
two-letter language patterns remain accepted. Deployment must pin a committed
schema revision; a local uncommitted checkout is not a deployable pin.
