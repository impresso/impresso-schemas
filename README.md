# Impresso JSON Schemas

JSON schemas for the [Impresso project](https://impresso-project.ch/), used to define, validate, and document the structure of historical newspaper and broadcast data formats.

All schemas follow **JSON Schema draft 2020-12**. Schema `$id` URIs are rooted at `https://impresso.github.io/impresso-schemas/`.

## Contents

- [Data preparation](#data-preparation)
- [Text preprocessing](#text-preprocessing)
- [Semantic enrichment](#semantic-enrichment)
- [Solr indexing](#solr-indexing)
- [Web app](#web-app)
- [Repository layout](#repository-layout)
- [Validation](#validation)
- [Documentation](#documentation)

In the tables below, **legacy** links point to the stable, existing namespace;
**Impresso 2** links point to the versioned lifecycle-based namespace.

## Data preparation

| Schema files | Description | Links |
| --- | --- | --- |
| `canonical/issue.schema.json`<br>`data-preparation/canonical/issue.v1.schema.json` | Newspaper issue | [schema legacy](json/canonical/issue.schema.json) · [schema Impresso 2](json/impresso-2/data-preparation/canonical/issue.v1.schema.json)<br>[docs legacy](docs/issue-1.md) · [docs Impresso 2](docs/issue.md) |
| `canonical/page.schema.json`<br>`data-preparation/canonical/page.v1.schema.json` | Newspaper page | [schema legacy](json/canonical/page.schema.json) · [schema Impresso 2](json/impresso-2/data-preparation/canonical/page.v1.schema.json)<br>[docs legacy](docs/page-1.md) · [docs Impresso 2](docs/page.md) |
| `canonical/audio_record.schema.json`<br>`data-preparation/canonical/audio-record.v1.schema.json` | Radio or TV broadcast record | [schema legacy](json/canonical/audio_record.schema.json) · [schema Impresso 2](json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json)<br>[docs legacy](docs/audio_record.md) · [docs Impresso 2](docs/audio-record.md) |
| `rebuilt/paper_contentitem.schema.json`<br>`data-preparation/rebuilt/paper-contentitem.v1.schema.json` | Rebuilt newspaper content item | [schema legacy](json/rebuilt/paper_contentitem.schema.json) · [schema Impresso 2](json/impresso-2/data-preparation/rebuilt/paper-contentitem.v1.schema.json)<br>[docs legacy](docs/paper_contentitem.md) · [docs Impresso 2](docs/paper-contentitem.md) |
| `rebuilt/audio_record_contentitem.schema.json`<br>`data-preparation/rebuilt/audio-record-contentitem.v1.schema.json` | Rebuilt broadcast content item | [schema legacy](json/rebuilt/audio_record_contentitem.schema.json) · [schema Impresso 2](json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json)<br>[docs legacy](docs/audio_record_contentitem.md) · [docs Impresso 2](docs/audio-record-contentitem.md) |
| `versioning/manifest.schema.json`<br>`data-preparation/versioning/manifest.v1.schema.json` | Data release manifest | [schema legacy](json/versioning/manifest.schema.json) · [schema Impresso 2](json/impresso-2/data-preparation/versioning/manifest.v1.schema.json)<br>[docs legacy](docs/manifest.md) · [docs Impresso 2](docs/manifest-1.md) |
| `visualizer/bbox_visualizer.schema.json`<br>`data-preparation/visualizer/bbox-visualizer.v1.schema.json` | Bounding-box visualisation data | [schema legacy](json/visualizer/bbox_visualizer.schema.json) · [schema Impresso 2](json/impresso-2/data-preparation/visualizer/bbox-visualizer.v1.schema.json)<br>[docs legacy](docs/bbox_visualizer.md) · [docs Impresso 2](docs/bbox-visualizer.md) |

## Text preprocessing

| Schema files | Description | Links |
| --- | --- | --- |
| `language_identification/language_identification.schema.json`<br>`text-preprocessing/language-identification/language-identification.v1.schema.json` | Per-token language identification | [schema legacy](json/language_identification/language_identification.schema.json) · [schema Impresso 2](json/impresso-2/text-preprocessing/language-identification/language-identification.v1.schema.json)<br>[docs legacy](docs/language_identification.md) · [docs Impresso 2](docs/language-identification.md) |
| `linguistic_annotation/ling_spacy.schema.json`<br>`text-preprocessing/linguistic-annotation/ling-spacy.v1.schema.json` | spaCy-based linguistic annotation | [schema legacy](json/linguistic_annotation/ling_spacy.schema.json) · [schema Impresso 2](json/impresso-2/text-preprocessing/linguistic-annotation/ling-spacy.v1.schema.json)<br>[docs legacy](docs/ling_spacy.md) · [docs Impresso 2](docs/ling-spacy.md) |
| `linguistic_annotation/lingproc.v2.schema.json`<br>`text-preprocessing/linguistic-annotation/lingproc.v1.schema.json` | Linguistic processing | [schema legacy](json/linguistic_annotation/lingproc.v2.schema.json) · [schema Impresso 2](json/impresso-2/text-preprocessing/linguistic-annotation/lingproc.v1.schema.json)<br>[docs legacy](docs/lingproc.md) · [docs Impresso 2](docs/lingproc-1.md) |
| `ocr_qa/ocr_qa.schema.json`<br>`text-preprocessing/ocr-qa/ocr-qa.v1.schema.json` | OCR quality-assessment scores | [schema legacy](json/ocr_qa/ocr_qa.schema.json) · [schema Impresso 2](json/impresso-2/text-preprocessing/ocr-qa/ocr-qa.v1.schema.json)<br>[docs legacy](docs/ocr_qa.md) · [docs Impresso 2](docs/ocr-qa.md) |

## Semantic enrichment

| Schema files | Description | Links |
| --- | --- | --- |
| `topic_model/topic_assignment.schema.json`<br>`topic_model/topic_assignment.v2.schema.json`<br>`semantic-enrichment/topic-model/topic-assignment.v1.schema.json` | Topic assignment per content item | [schema legacy v1](json/topic_model/topic_assignment.schema.json) · [schema legacy v2](json/topic_model/topic_assignment.v2.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json)<br>[docs legacy v1](docs/topic_assignment.md) · [docs legacy v2](docs/topic_assignment-1.md) · [docs Impresso 2](docs/topic-assignment.md) |
| `topic_model/topic_description.schema.json`<br>`semantic-enrichment/topic-model/topic-description.v1.schema.json` | Topic description with words and weights | [schema legacy](json/topic_model/topic_description.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/topic-model/topic-description.v1.schema.json)<br>[docs legacy](docs/topic_description.md) · [docs Impresso 2](docs/topic-description.md) |
| `entities/entities.schema.json`<br>`semantic-enrichment/entities/entities.v1.schema.json` | Named-entity mentions | [schema legacy](json/entities/entities.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json)<br>[docs legacy](docs/entities-1.md) · [docs Impresso 2](docs/entities.md) |
| `embeddings/embeddings-docs.schema.json`<br>`semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json` | Document-level embeddings | [schema legacy](json/embeddings/embeddings-docs.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json)<br>[docs legacy](docs/embeddings-docs-1.md) · [docs Impresso 2](docs/embeddings-docs.md) |
| `embeddings/embeddings-sentence.schema.json`<br>`semantic-enrichment/document-embeddings/embeddings-sentence.v1.schema.json` | Sentence-level embeddings | [schema legacy](json/embeddings/embeddings-sentence.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-sentence.v1.schema.json)<br>[docs legacy](docs/embeddings-sentence-1.md) · [docs Impresso 2](docs/embeddings-sentence.md) |
| `embeddings/embeddings-chunks.schema.json`<br>`semantic-enrichment/document-embeddings/embeddings-chunks.v1.schema.json` | Chunk-level embeddings | [schema legacy](json/embeddings/embeddings-chunks.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-chunks.v1.schema.json)<br>[docs legacy](docs/embeddings-chunks-1.md) · [docs Impresso 2](docs/embeddings-chunks.md) |
| `embeddings/embeddings-entities.schema.json`<br>`semantic-enrichment/document-embeddings/embeddings-entities.v1.schema.json` | Entity embeddings | [schema legacy](json/embeddings/embeddings-entities.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-entities.v1.schema.json)<br>[docs legacy](docs/embeddings-entities-1.md) · [docs Impresso 2](docs/embeddings-entities.md) |
| `text_reuse/cluster.schema.json`<br>`semantic-enrichment/text-reuse/cluster.v1.schema.json` | Text-reuse cluster | [schema legacy](json/text_reuse/cluster.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/text-reuse/cluster.v1.schema.json)<br>[docs legacy](docs/cluster.md) · [docs Impresso 2](docs/cluster-1.md) |
| `text_reuse/passage.schema.json`<br>`semantic-enrichment/text-reuse/passage.v1.schema.json` | Text-reuse passage | [schema legacy](json/text_reuse/passage.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/text-reuse/passage.v1.schema.json)<br>[docs legacy](docs/passage.md) · [docs Impresso 2](docs/passage-1.md) |
| `image_embeddings/image_embeddings.schema.json`<br>`semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json` | Image-level embeddings | [schema legacy](json/image_embeddings/image_embeddings.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json)<br>[docs legacy](docs/image_embeddings.md) · [docs Impresso 2](docs/image-embeddings.md) |
| `image_classification/image_classification.schema.json`<br>`semantic-enrichment/image-classification/image-classification.v1.schema.json` | Image-classification labels | [schema legacy](json/image_classification/image_classification.schema.json) · [schema Impresso 2](json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json)<br>[docs legacy](docs/image_classification.md) · [docs Impresso 2](docs/image-classification.md) |

## Solr indexing

Solr schemas are currently available only in the Impresso 2 namespace.

| Schema file | Description | Links |
| --- | --- | --- |
| `content-item.part.access-rights.v1.schema.json` | Shared access-right fields | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json) · [docs Impresso 2](docs/content-item-3.md) |
| `content-item.part.contextual-metadata.provider.v1.schema.json` | Shared provider metadata | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json) · [docs Impresso 2](docs/content-item-5.md) |
| `content-item.part.contextual-metadata.v1.schema.json` | Shared contextual metadata | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.v1.schema.json) · [docs Impresso 2](docs/content-item-2.md) |
| `content-item.part.core.v1.schema.json` | Shared core content-item fields | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json) · [docs Impresso 2](docs/content-item-1.md) |
| `content-item.part.image.v1.schema.json` | Image content-item fields | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json) · [docs Impresso 2](docs/content-item-6.md) |
| `content-item.part.text.audio.v1.schema.json` | Audio transcript content-item fields | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json) · [docs Impresso 2](docs/content-item-7.md) |
| `content-item.part.text.paper.v1.schema.json` | Newspaper content-item fields | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json) · [docs Impresso 2](docs/content-item-8.md) |
| `content-item.part.text.semantic-enrichments.v1.schema.json` | Semantic-enrichment fields on content items | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.part.text.semantic-enrichments.v1.schema.json) · [docs Impresso 2](docs/content-item-4.md) |
| `content-item.part.text.transcript.v1.schema.json` | Transcript content-item fields | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json) · [docs Impresso 2](docs/content-item.md) |
| `content-item.root.audio.v1.schema.json` | Audio content-item document | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.root.audio.v1.schema.json) · [docs Impresso 2](docs/content-item-9.md) |
| `content-item.root.image.v1.schema.json` | Image content-item document | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.root.image.v1.schema.json) · [docs Impresso 2](docs/content-item-10.md) |
| `content-item.root.paper.v1.schema.json` | Newspaper content-item document | [schema Impresso 2](json/impresso-2/solr-indexing/content-item/content-item.root.paper.v1.schema.json) · [docs Impresso 2](docs/content-item-11.md) |
| `sem.part.tr-passages.v1.schema.json` | Shared text-reuse passage fields | [schema Impresso 2](json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json) · [docs Impresso 2](docs/sem.md) |
| `sem.root.entities.v1.schema.json` | Entity document | [schema Impresso 2](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json) · [docs Impresso 2](docs/sem-1.md) |
| `sem.root.entity-profiles.v1.schema.json` | Entity-profile embedding document | [schema Impresso 2](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json) · [docs Impresso 2](docs/sem-2.md) |
| `sem.root.mentions.v1.schema.json` | Entity-mention document | [schema Impresso 2](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json) · [docs Impresso 2](docs/sem-3.md) |
| `sem.root.topics.v1.schema.json` | Topic document | [schema Impresso 2](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json) · [docs Impresso 2](docs/sem-4.md) |
| `sem.root.tr-clusters.v1.schema.json` | Text-reuse cluster document | [schema Impresso 2](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json) · [docs Impresso 2](docs/sem-5.md) |
| `sem.root.tr-passages.v1.schema.json` | Text-reuse passage document | [schema Impresso 2](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-passages.v1.schema.json) · [docs Impresso 2](docs/sem-6.md) |
| `sem.root.wemb.v1.schema.json` | Word-embedding document | [schema Impresso 2](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json) · [docs Impresso 2](docs/sem-7.md) |

## Web app

No web-app schemas have been added yet.

## Repository layout

```
json/          Schema source of truth
  impresso-2/  Versioned schemas organised by lifecycle area
examples/      Example JSON files used for validation tests
  impresso-2/  Mirrors json/impresso-2/ for versioned schemas
docs/          Generated documentation (Markdown)
scripts/       Utility scripts
```

### Schema namespaces

The existing directories directly under `json/` are the **legacy namespace**.
Their paths and `$id` values are published and remain unchanged for backwards
compatibility.

New versioned contracts live under `json/impresso-2/`, organised by lifecycle
area:

```
json/impresso-2/
├── data-preparation/
├── text-preprocessing/
├── semantic-enrichment/
├── solr-indexing/
└── web-app/
```

Schemas in this namespace use versioned filenames such as
`issue.v1.schema.json`. Their `$id` must exactly match their repository path
below `https://impresso.github.io/impresso-schemas/`. The `common/` directory is
reserved for genuinely cross-lifecycle definitions and is added only when such
sharing is needed.

Examples for a versioned schema mirror its schema directory. For example:

```
json/impresso-2/solr-indexing/content-item/content-item.root.paper.v1.schema.json
examples/impresso-2/solr-indexing/content-item/ci_paper.example.json
```

## Prerequisites

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install .
```

**Node.js** — install the documentation generator globally:

```bash
npm install -g @adobe/jsonschema2md
```

All `make` commands must be run with the virtualenv activated.

## Formatting

Before submitting changes, format all JSON files with [Prettier](https://prettier.io/):

```bash
make format
```

To check formatting without modifying files (e.g. in CI):

```bash
make format-check
```

## Validation

`make tests` validates schema correctness, path-to-`$id` consistency, local
`$ref` resolution, and the registered legacy and Impresso 2 examples:

```bash
make tests
```

## Documentation

Regenerate Markdown documentation from schemas:

```bash
make documentation
```

Documentation is generated by [`@adobe/jsonschema2md`](https://github.com/adobe/jsonschema2md) and written to `docs/`.

## Project

The _impresso - Media Monitoring of the Past_ project is funded by the Swiss National Science Foundation (SNSF) under grant number [CRSII5_173719](http://p3.snf.ch/project-173719) (Sinergia program). The project develops tools to process and explore large-scale collections of historical newspapers. More information at https://impresso-project.ch.

## License

Copyright (C) 2026 The _impresso_ team. Contributors include: [Simon Clematide](https://github.com/simon-clematide), [Maud Ehrmann](https://github.com/e-maud), and [Matteo Romanello](http://github.com/mromanello/).

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. See the [GNU Affero General Public License](https://github.com/impresso/impresso-schemas/blob/master/LICENSE) for details.
