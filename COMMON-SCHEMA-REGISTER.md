# Common-schema register

**Status:** initial inventory, 2026-08-18.  This register records observed
properties and schema fragments in the current `json/impresso-2/` namespace.
It is evidence for discussion; a candidate is **not** approval to extract or
change a contract.

## Contents

- [Scope and reading guide](#scope-and-reading-guide)
- [Cross-lifecycle register](#cross-lifecycle-register)
- [Data preparation](#data-preparation)
- [Text processing](#text-processing)
- [Semantic enrichment](#semantic-enrichment)
- [Solr indexing](#solr-indexing)
- [Example and test coverage](#example-and-test-coverage)
- [Next review actions](#next-review-actions)

## Scope and reading guide

The inventory covers every schema and current example under `json/impresso-2/`
and `examples/impresso-2/`. It resolves the two root `allOf` fragments, so a
property supplied by a fragment is not mistaken for absent merely because it
does not appear in the consumer's local `properties` object.

Status labels:

- **Done** — an implemented root `common/` fragment, with current consumers.
- **Candidate** — a repeated concept that needs a concept card, real-data
  check, and owner review before extraction.
- **Local candidate** — potential reuse within one lifecycle area only.
- **Do not extract** — deliberately local, deprecated, retiring, or materially
  different despite a similar name.

Requiredness is local to each consumer. A root object fragment may define a
property and its value rules without making it required everywhere.

## Cross-lifecycle register

| Status | Concept / proposed scope | Observed schema properties and consumers | Evidence and decision needed |
| --- | --- | --- | --- |
| **Done** | `content-item-id.part.v1` — `common/` | `ci_id` through `allOf` in rebuilt paper/audio; language identification; linguistic annotation (`lingproc`, `ling-spacy`); OCR QA; document, image, entity, and image-classification enrichment; text-reuse passage; topic assignment. | One canonical `ci_id` name and content-item pattern. Consumer schemas retain their own `required` entries. The planned chunk/sentence/entity-embedding retirement is excluded from further adoption. |
| **Done** | `model-id.part.v1` — `common/` | `model_id` through `allOf` in `lingproc`, document embeddings, entities, image embeddings, image classification, and topic assignment. | Shared meaning is the producing model/system identifier. It is required in four current consumers and optional in `lingproc` and topic assignment. Confirm the final model-description convention and examples with producers. |
| **Candidate** | Processing timestamp — `common/` | `ts` occurs in canonical issue/page/audio-record; rebuilt paper/audio; OCR QA; linguistic annotation; entities; document/image embeddings; image classification; topic assignment; sentence/chunk embeddings. | Same broad meaning (output generation time), but validation differs: strict UTC pattern, `format: date-time`, and bare strings all occur. `cdt`, `timestamp`, `mft_generation_date`, and dates are not automatically aliases. Agree exact meaning and RFC 3339/UTC policy first. |
| **Candidate** | Language-code value — `common/` | `lg` in rebuilt, OCR QA, language identification, topic assignment, and topic description; `orig_lg`/`lg_original` are related but distinct; `language` occurs in retiring entity embeddings. | Present code rules differ: two-letter, two-or-three-letter, nullable, references to local `$defs`, and unconstrained strings. Establish vocabulary, unknown-value policy, and the distinction between source, predicted, and model language before sharing a scalar definition. |
| **Candidate** | Processing provenance vocabulary — `common/` | `git_version`, `lingproc_git`, `topics_git`, `git`, paths, and run identifiers occur across text processing and semantic enrichment. | These fields are not yet one object or one naming convention. Define their semantics and relationship to `model_id` before designing a provenance fragment. |

## Data preparation

### Data-preparation schema and example inventory

| Area | Schemas reviewed | Current examples | Reuse observations |
| --- | --- | --- | --- |
| Canonical | `canonical/issue.v1`, `canonical/page.v1`, `canonical/audio-record.v1` | 5 issue, 5 page, 1 audio-record | Issue/page/audio share source fields in differing subsets. They represent different canonical objects, so identifier and structural fields remain type-specific. |
| Rebuilt | `rebuilt/paper-contentitem.v1`, `rebuilt/audio-record-contentitem.v1` | 2 paper, 2 audio | Both consume the done `ci_id` fragment and have substantial source, publication, consolidation, and text metadata overlap. |
| Versioning | `versioning/manifest.v1` | 1 manifest | Manifest release metadata is not a content-item representation. Keep local until a broader release/provenance vocabulary is defined. |
| Visualizer | `visualizer/bbox-visualizer.v1` | 3 bounding-box files | IIIF image bases and bounding boxes are visual-quality inputs. Keep local; their shape differs from canonical page regions. |

### Local candidates: `data-preparation/common/`

| Status | Concept | Current occurrences | Why it is not extracted yet |
| --- | --- | --- | --- |
| **Local candidate** | Source metadata | `st`, `sm`, `rc`, `rp`, `media_title_variant`, and related fields in canonical issue/audio/page and rebuilt paper/audio. | The source type/medium enums and nullability differ. `rc`/`rp` are conditionally meaningful for radio; media-title semantics need an agreed object boundary. |
| **Local candidate** | Publication-date metadata | `d` and `is_exact_date` in rebuilt; `cdt` and `is_exact_date` in canonical issue; `cdt` in canonical page/audio. | `d` is a source publication/broadcast date; `cdt` is a file creation date. They must not be combined merely because both are dates. |
| **Local candidate** | Consolidation metadata | `consolidated`, `consolidated_ocrqa`, `lg_original`, and related fields in rebuilt paper/audio; a related subset in canonical issue. | The producer stage and fields are not identical. Resolve whether this is a source-state concept, derived quality metadata, or two separate fragments. |
| **Local candidate** | Rebuilt textual offsets | Paper `ft`, `rb`, `pb`, `lb`, `ppreb`; audio `ft`, `sb`, `ub`, `ssb`, `rreb`. | Both are offsets into rebuilt full text, but support-specific segmentation structures differ. A shared offset primitive may later be useful; do not force a common rebuilt object now. |
| **Do not extract** | Canonical IDs and document structures | `id`, `i`, `r`, `s`, page image dimensions, audio sections. | These identify and describe different entities (issue, page, audio record), not a single reusable property. |

## Text processing

### Text-processing schema and example inventory

| Area | Schemas reviewed | Current examples | Reuse observations |
| --- | --- | --- | --- |
| Language identification | `language-identification/language-identification.v1` | 3 valid, 1 invalid | Consumes `ci_id`. Its `lg`, `orig_lg`, prediction lists, decision strategy, and version objects are language-identification-specific. |
| Linguistic annotation | `linguistic-annotation/lingproc.v1`, `linguistic-annotation/ling-spacy.v1` | 1 `lingproc` example; no registered `ling-spacy` example | Both consume `ci_id`; `lingproc` also consumes `model_id`. Sentence structures are related but not identical. |
| OCR QA | `ocr-qa/ocr-qa.v1` | 1 example | Consumes `ci_id`; uses `lg`, `ts`, a Bloom dictionary reference, code revision, and OCR-quality metrics. |

### Local candidates: `text-processing/common/`

| Status | Concept | Current occurrences | Why it is not extracted yet |
| --- | --- | --- | --- |
| **Local candidate** | Text-processing run provenance | `lingproc_git`, `lid_path`, and `model_id` in `lingproc`; LID version objects; `git_version` and `bloom` in OCR QA. | All support traceability but name different artefacts: code revision, input path, model/system, and lexical resource. Agree a vocabulary before grouping. |
| **Candidate** | Language-code value | `lg` in OCR QA and LID; `orig_lg` in LID. | Also occurs across other lifecycle areas, so assess at root scope. LID distinguishes predicted from source language; OCR QA currently requires a strict two-letter code. |
| **Candidate** | Processing timestamp | `ts` in OCR QA and both annotation schemas. | Also cross-lifecycle; assess at root scope rather than extracting a text-only fragment. |
| **Do not extract** | Deprecated `timestamp` | OCR QA only. | Explicitly deprecated in favour of `ts`; retain only for compatibility until a removal decision is made. |
| **Do not extract** | Sentence/annotation payloads | `sents`, `tsents`, linguistic token fields. | Payload structures encode specific processing output and differ between `lingproc` and spaCy. |

## Semantic enrichment

### Semantic-enrichment schema and example inventory

| Area | Schemas reviewed | Current examples | Reuse observations |
| --- | --- | --- | --- |
| Entities | `entities/entities.v1` | 3 | Consumes `ci_id` and `model_id`; has its own named-entity payload. |
| Document embeddings | `embeddings-docs.v1`, `embeddings-sentence.v1`, `embeddings-chunks.v1`, `embeddings-entities.v1` | 1 document, 1 sentence, 1 chunk; none for entity embeddings | Document embeddings consume both done fragments. Sentence/chunk/entity embeddings are planned for removal and must not receive new shared fragments. |
| Image embeddings | `image-embeddings/image-embeddings.v1` | 1 | Consumes both done fragments; overlaps with document embedding record metadata. |
| Image classification | `image-classification/image-classification.v1` | 1 | Consumes both done fragments; predictions are classification-specific. |
| Text reuse | `text-reuse/cluster.v1`, `text-reuse/passage.v1` | 1 cluster, 1 passage | Passage consumes `ci_id`; cluster/passage use a separate text-reuse identifier and date range vocabulary. |
| Topic model | `topic-assignment.v1`, `topic-description.v1` | Topic description: 2; topic assignment: 1 fixture, not registered as a valid test case | Assignment consumes both done fragments; topic description is a model-level description, not a content-item output. |

### Local candidates: `semantic-enrichment/common/`

| Status | Concept | Current occurrences | Why it is not extracted yet |
| --- | --- | --- | --- |
| **Local candidate** | Embedding vector record | Document and image embeddings both require `embedding` and `size`; both use a `date-time` `ts` and the two done fragments. | Document embeddings permit a one-dimensional vector or a list of vectors; image embeddings permit only one vector. Decide whether a common numeric-vector primitive is useful and whether `size` has the same meaning in both. |
| **Local candidate** | Enrichment run provenance | `model_id`, `ts`, `git`, `lingproc_path`, topic run IDs, and topic Git fields. | `model_id` is already shared. The remaining provenance fields have divergent names and granularity. |
| **Candidate** | Language-code value | Topic assignment/description `lg`; retiring entity embeddings `language`. | This is a root candidate, but topic schemas currently do not constrain the code like rebuilt/OCR QA do. |
| **Candidate** | Processing timestamp | Entity, embedding, classification, and topic outputs use `ts`. | This is a root candidate; compare strict patterns and `format: date-time` before standardising. |
| **Do not extract** | Sentence, chunk, and entity embedding metadata | `embeddings-sentence`, `embeddings-chunks`, `embeddings-entities`. | These schema families are planned for removal. Do not extend their current local `ci_id`, `model_id`, `git`, or path definitions. |
| **Do not extract** | Text-reuse identifiers and dates | Passage `id`, `cluster_id`, `date`; cluster `id`, `min_date`, `max_date`. | Similar date strings do not imply one semantic role. These fields are specific to text-reuse outputs. |

## Solr indexing

| Area | Schemas reviewed | Current examples | Reuse observation |
| --- | --- | --- | --- |
| Content items | Three root schemas (`paper`, `image`, `audio`) and nine Solr-local parts for core fields, contextual metadata, rights, images, and support-specific text. | Paper/typescript and image examples are registered; the audio fixture is intentionally excluded. | The roots compose local parts through `$ref`; the field names and document shape are index-specific. |
| Semantic enrichments | Seven root schemas and one text-reuse-passage part. | Six examples are registered (entities, mentions, topics, text-reuse clusters/passages, word embeddings); entity profiles has no fixture. | Text-reuse passages compose Solr-local and content-item parts. The other root contracts describe independent indexed documents. |

| Status | Scope | Decision |
| --- | --- | --- |
| **Do not extract in this inventory** | `solr-indexing/content-item/` and `solr-indexing/semantic-enrichments/` | Solr has its own modular parts and `$ref` structure. Its fields are an indexing serialisation (for example `lg_s`), not a direct common document representation. Keep its parts Solr-local unless a future review establishes an identical value-level primitive and an explicit consumer need. |

## Example and test coverage

All listed examples were reviewed as the current fixture set. Registration below
refers to `tests/test_schema_examples.py`; a file can exist without being a
valid registered test case.

| Lifecycle area | Coverage observation | Follow-up relevance |
| --- | --- | --- |
| Data preparation | Canonical, rebuilt, manifest, and visualizer Impresso 2 examples are registered. | Fixtures are evidence for schema behaviour, not proof that all production data has migrated (notably rebuilt `id` versus `ci_id`). |
| Text processing | LID has valid and invalid fixtures; `lingproc` and OCR QA have registered valid fixtures; `ling-spacy` currently has no registered example. | Add a representative spaCy fixture before changing its contract further. |
| Semantic enrichment | Entities, document/sentence/chunk embeddings, text reuse, image embedding/classification, and topic description have registered fixtures. | Topic assignment has an example but no registered valid test. Entity embeddings have no example and are planned for removal. |
| Solr indexing | Content-item and semantic-enrichment fixtures are registered, except the intentionally empty audio fixture. | Validate Solr as its own serialisation; do not use these fixtures to infer direct cross-stage property equivalence. |

## Next review actions

1. Confirm the scope and candidate grouping in this register with the schema
   owners, especially `ts`, `lg`, source metadata, and provenance.
2. For each retained candidate, create a concept card with semantics, value
   constraints, aliases, examples, producer/consumer owners, and compatibility
   impact.
3. Run representative real-data validation before changing shared rules. Record
   the rebuilt `id` to `ci_id` transition and any other observed mismatch in
   `MIGRATION-MAPPING.md`.
4. Create bounded implementation issues only after a concept card is approved;
   do not extract fields solely because their names repeat.
