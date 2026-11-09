# Schema migration mapping

This table records the non-breaking migration into `json/impresso-2/`.
Legacy schemas remain unchanged and published at their existing URLs.

## Transition status and consumer adoption

The Impresso 2 namespace is still being consolidated. Its schemas are not yet
asserted to validate every existing production dataset. For example, current
rebuilt data may still use `id`, whereas the Impresso 2 rebuilt schemas require
`ci_id`.

Consumers must select the legacy or Impresso 2 namespace explicitly. They must
not treat the presence of an Impresso 2 schema as evidence that existing data
or consumer code can switch without changes. Before adoption, validate
representative producer output against the selected contract and decide whether
to update the producer, consumer, or a documented adapter. JSON Schema `$ref`
shares validation rules; it does not transform data between representations.

For each migrated legacy schema family, the Impresso 2 `v1` contract is based
on the latest stable legacy contract. Earlier legacy versions remain available
only in the legacy namespace.

## Legacy schemas to Impresso 2

| Legacy source | Impresso 2 contract |
| --- | --- |
| `json/canonical/audio_record.schema.json` | `json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json` |
| `json/canonical/issue.schema.json` | `json/impresso-2/data-preparation/canonical/issue.v1.schema.json` |
| `json/canonical/page.schema.json` | `json/impresso-2/data-preparation/canonical/page.v1.schema.json` |
| `json/rebuilt/audio_record_contentitem.schema.json` | `json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json` |
| `json/rebuilt/paper_contentitem.schema.json` | `json/impresso-2/data-preparation/rebuilt/paper-contentitem.v1.schema.json` |
| `json/versioning/manifest.schema.json` | `json/impresso-2/data-preparation/versioning/manifest.v1.schema.json` |
| `json/visualizer/bbox_visualizer.schema.json` | `json/impresso-2/data-preparation/visualizer/bbox-visualizer.v1.schema.json` |
| `json/language_identification/language_identification.schema.json` | `json/impresso-2/text-processing/language-identification/language-identification.v1.schema.json` |
| `json/linguistic_annotation/ling_spacy.schema.json` | `json/impresso-2/text-processing/linguistic-annotation/ling-spacy.v1.schema.json` |
| `json/linguistic_annotation/lingproc.v2.schema.json` | `json/impresso-2/text-processing/linguistic-annotation/lingproc.v1.schema.json` |
| `json/ocr_qa/ocr_qa.schema.json` | `json/impresso-2/text-processing/ocr-qa/ocr-qa.v1.schema.json` |
| `json/embeddings/embeddings-chunks.schema.json` | `json/impresso-2/semantic-enrichment/document-embeddings/embeddings-chunks.v1.schema.json` |
| `json/embeddings/embeddings-docs.schema.json` | `json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json` |
| `json/embeddings/embeddings-entities.schema.json` | `json/impresso-2/semantic-enrichment/document-embeddings/embeddings-entities.v1.schema.json` |
| `json/embeddings/embeddings-sentence.schema.json` | `json/impresso-2/semantic-enrichment/document-embeddings/embeddings-sentence.v1.schema.json` |
| `json/entities/entities.schema.json` | `json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json` |
| `json/image_classification/image_classification.schema.json` | `json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json` |
| `json/image_embeddings/image_embeddings.schema.json` | `json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json` |
| `json/text_reuse/cluster.schema.json` | `json/impresso-2/semantic-enrichment/text-reuse/cluster.v1.schema.json` |
| `json/text_reuse/passage.schema.json` | `json/impresso-2/semantic-enrichment/text-reuse/passage.v1.schema.json` |
| `json/topic_model/topic_assignment.v2.schema.json` | `json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json` |
| `json/topic_model/topic_description.schema.json` | `json/impresso-2/semantic-enrichment/topic-model/topic-description.v1.schema.json` |

The earlier legacy `json/topic_model/topic_assignment.schema.json` is retained
at its original path; it has no separate Impresso 2 copy.

## Solr schemas to Impresso 2

The Solr schemas are migrated from `impresso-pyindexing` and stay there during
the transition. They are versioned in the new namespace as follows:

| Legacy source area in `impresso-pyindexing` | Impresso 2 destination | Schemas |
| --- | --- | ---: |
| `impresso_solr/schemas/json/content-item/` | `json/impresso-2/solr-indexing/content-item/` | 12 |
| `impresso_solr/schemas/json/semantic-enrichments/` | `json/impresso-2/solr-indexing/semantic-enrichments/` | 8 |

All new Solr files use a `*.v1.schema.json` name and `$id`; their cross-file
`$ref` values target the corresponding versioned Impresso 2 `$id` URLs.

## Examples

Legacy examples remain unchanged. Their copies mirror the directory hierarchy
under `json/impresso-2/` exactly.

```text
json/impresso-2/<lifecycle-area>/<schema-group>/<schema>.v1.schema.json
examples/impresso-2/<lifecycle-area>/<schema-group>/<schema>.<example>.json
```

When several schemas share a directory, the example filename starts with the
schema name to avoid collisions. Solr example names already identify their
document type, so they are retained unchanged. For example:

```text
examples/impresso-2/data-preparation/canonical/issue.example0.json
examples/impresso-2/data-preparation/canonical/page.example0.json
examples/impresso-2/solr-indexing/content-item/ci_paper.example.json
```

The empty audio example is retained at
`solr-indexing/content-item/ci_audio.example.json`, but is intentionally
excluded from the valid-example test matrix until it is populated.
Language-identification `example0-invalid.json` is retained as an expected-invalid
fixture. The copied topic-assignment example is retained for reference but is
not yet a valid-example test case. The OCR-QA example is registered and
validated against the current Impresso 2 contract.
