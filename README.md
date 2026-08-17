# Impresso JSON Schemas

JSON schemas for the [Impresso project](https://impresso-project.ch/), used to
define, validate, and document the structure of historical newspaper and
broadcast data formats.

All schemas follow **JSON Schema draft 2020-12**. Schema `$id` URIs are rooted
at `https://impresso.github.io/impresso-schemas/`.

## Contents

- [Schema management](#schema-management)
  - [Repository layout](#repository-layout)
  - [Namespaces and versioning](#namespaces-and-versioning)
  - [Development workflow](#development-workflow)
- [Schemas](#schemas)
  - [Data preparation](#data-preparation)
  - [Text preprocessing](#text-preprocessing)
  - [Semantic enrichment](#semantic-enrichment)
  - [Solr indexing](#solr-indexing)
  - [Web app](#web-app)
- [Project](#project)
- [License](#license)

## Schema management

### Repository layout

```text
json/                                   Schema source of truth
├── canonical/, rebuilt/                Legacy data-preparation schemas
├── versioning/, visualizer/            Legacy supporting schemas
├── language_identification/,
│   linguistic_annotation/, ocr_qa/     Legacy text-preprocessing schemas
├── embeddings/, entities/, image_*/,
│   text_reuse/, topic_model/           Legacy semantic-enrichment schemas
└── impresso-2/                         Versioned lifecycle-based namespace
    ├── data-preparation/
    ├── text-preprocessing/
    ├── semantic-enrichment/
    ├── solr-indexing/
    └── web-app/

examples/                               Validation fixtures
└── impresso-2/                         Mirrors json/impresso-2/
docs/                                   Generated Markdown; do not edit manually
tests/                                  Schema integrity and example validation
```

### Namespaces and versioning

The existing directories directly under `json/` are the **legacy namespace**.
Their paths and published `$id` values are stable and must not change.

New versioned contracts live under `json/impresso-2/`. They use filenames such
as `issue.v1.schema.json`; the repository path and published `$id` must match
exactly. Reserve `json/impresso-2/common/` for definitions that genuinely share
the same semantics across lifecycle areas.

Examples for a versioned schema mirror its schema directory. For example:

```text
json/impresso-2/solr-indexing/content-item/content-item.root.paper.v1.schema.json
examples/impresso-2/solr-indexing/content-item/ci_paper.example.json
```

### Development workflow

Create and activate a virtual environment, then install the Python package:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install .
```

Install the documentation and formatting tools:

```bash
npm install -g @adobe/jsonschema2md prettier markdownlint-cli
```

Before submitting changes, run:

```bash
make format-check     # Check JSON formatting
make tests            # Validate schemas, references, and registered examples
make documentation    # Regenerate and lint docs/
```

## Schemas

**legacy** links point to the stable existing namespace; **imp2** links point
to the versioned, lifecycle-based namespace.

### Data preparation

- Issue:
  - legacy: [`json/canonical/issue.schema.json`](json/canonical/issue.schema.json) — [docs](docs/issue-1.md)
  - imp2: [`json/impresso-2/data-preparation/canonical/issue.v1.schema.json`](json/impresso-2/data-preparation/canonical/issue.v1.schema.json) — [docs](docs/issue.md)
- Page:
  - legacy: [`json/canonical/page.schema.json`](json/canonical/page.schema.json) — [docs](docs/page-1.md)
  - imp2: [`json/impresso-2/data-preparation/canonical/page.v1.schema.json`](json/impresso-2/data-preparation/canonical/page.v1.schema.json) — [docs](docs/page.md)
- Audio record:
  - legacy: [`json/canonical/audio_record.schema.json`](json/canonical/audio_record.schema.json) — [docs](docs/audio_record.md)
  - imp2: [`json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json`](json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json) — [docs](docs/audio-record.md)
- Paper content item:
  - legacy: [`json/rebuilt/paper_contentitem.schema.json`](json/rebuilt/paper_contentitem.schema.json) — [docs](docs/paper_contentitem.md)
  - imp2: [`json/impresso-2/data-preparation/rebuilt/paper-contentitem.v1.schema.json`](json/impresso-2/data-preparation/rebuilt/paper-contentitem.v1.schema.json) — [docs](docs/paper-contentitem.md)
- Audio-record content item:
  - legacy: [`json/rebuilt/audio_record_contentitem.schema.json`](json/rebuilt/audio_record_contentitem.schema.json) — [docs](docs/audio_record_contentitem.md)
  - imp2: [`json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json`](json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json) — [docs](docs/audio-record-contentitem.md)
- Manifest:
  - legacy: [`json/versioning/manifest.schema.json`](json/versioning/manifest.schema.json) — [docs](docs/manifest.md)
  - imp2: [`json/impresso-2/data-preparation/versioning/manifest.v1.schema.json`](json/impresso-2/data-preparation/versioning/manifest.v1.schema.json) — [docs](docs/manifest-1.md)
- Bounding-box visualizer:
  - legacy: [`json/visualizer/bbox_visualizer.schema.json`](json/visualizer/bbox_visualizer.schema.json) — [docs](docs/bbox_visualizer.md)
  - imp2: [`json/impresso-2/data-preparation/visualizer/bbox-visualizer.v1.schema.json`](json/impresso-2/data-preparation/visualizer/bbox-visualizer.v1.schema.json) — [docs](docs/bbox-visualizer.md)

### Text preprocessing

- Language identification:
  - legacy: [`json/language_identification/language_identification.schema.json`](json/language_identification/language_identification.schema.json) — [docs](docs/language_identification.md)
  - imp2: [`json/impresso-2/text-preprocessing/language-identification/language-identification.v1.schema.json`](json/impresso-2/text-preprocessing/language-identification/language-identification.v1.schema.json) — [docs](docs/language-identification.md)
- Linguistic annotation (spaCy):
  - legacy: [`json/linguistic_annotation/ling_spacy.schema.json`](json/linguistic_annotation/ling_spacy.schema.json) — [docs](docs/ling_spacy.md)
  - imp2: [`json/impresso-2/text-preprocessing/linguistic-annotation/ling-spacy.v1.schema.json`](json/impresso-2/text-preprocessing/linguistic-annotation/ling-spacy.v1.schema.json) — [docs](docs/ling-spacy.md)
- Linguistic processing:
  - legacy: [`json/linguistic_annotation/lingproc.v2.schema.json`](json/linguistic_annotation/lingproc.v2.schema.json) — [docs](docs/lingproc.md)
  - imp2: [`json/impresso-2/text-preprocessing/linguistic-annotation/lingproc.v1.schema.json`](json/impresso-2/text-preprocessing/linguistic-annotation/lingproc.v1.schema.json) — [docs](docs/lingproc-1.md)
- OCR QA:
  - legacy: [`json/ocr_qa/ocr_qa.schema.json`](json/ocr_qa/ocr_qa.schema.json) — [docs](docs/ocr_qa.md)
  - imp2: [`json/impresso-2/text-preprocessing/ocr-qa/ocr-qa.v1.schema.json`](json/impresso-2/text-preprocessing/ocr-qa/ocr-qa.v1.schema.json) — [docs](docs/ocr-qa.md)

### Semantic enrichment

- Topic assignment:
  - legacy v1: [`json/topic_model/topic_assignment.schema.json`](json/topic_model/topic_assignment.schema.json) — [docs](docs/topic_assignment.md)
  - legacy v2: [`json/topic_model/topic_assignment.v2.schema.json`](json/topic_model/topic_assignment.v2.schema.json) — [docs](docs/topic_assignment-1.md)
  - imp2: [`json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json`](json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json) — [docs](docs/topic-assignment.md)
- Topic description:
  - legacy: [`json/topic_model/topic_description.schema.json`](json/topic_model/topic_description.schema.json) — [docs](docs/topic_description.md)
  - imp2: [`json/impresso-2/semantic-enrichment/topic-model/topic-description.v1.schema.json`](json/impresso-2/semantic-enrichment/topic-model/topic-description.v1.schema.json) — [docs](docs/topic-description.md)
- Entities:
  - legacy: [`json/entities/entities.schema.json`](json/entities/entities.schema.json) — [docs](docs/entities-1.md)
  - imp2: [`json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json`](json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json) — [docs](docs/entities.md)
- Document embeddings:
  - legacy: [`json/embeddings/embeddings-docs.schema.json`](json/embeddings/embeddings-docs.schema.json) — [docs](docs/embeddings-docs-1.md)
  - imp2: [`json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json`](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json) — [docs](docs/embeddings-docs.md)
- Sentence embeddings:
  - legacy: [`json/embeddings/embeddings-sentence.schema.json`](json/embeddings/embeddings-sentence.schema.json) — [docs](docs/embeddings-sentence-1.md)
  - imp2: [`json/impresso-2/semantic-enrichment/document-embeddings/embeddings-sentence.v1.schema.json`](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-sentence.v1.schema.json) — [docs](docs/embeddings-sentence.md)
- Chunk embeddings:
  - legacy: [`json/embeddings/embeddings-chunks.schema.json`](json/embeddings/embeddings-chunks.schema.json) — [docs](docs/embeddings-chunks-1.md)
  - imp2: [`json/impresso-2/semantic-enrichment/document-embeddings/embeddings-chunks.v1.schema.json`](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-chunks.v1.schema.json) — [docs](docs/embeddings-chunks.md)
- Entity embeddings:
  - legacy: [`json/embeddings/embeddings-entities.schema.json`](json/embeddings/embeddings-entities.schema.json) — [docs](docs/embeddings-entities-1.md)
  - imp2: [`json/impresso-2/semantic-enrichment/document-embeddings/embeddings-entities.v1.schema.json`](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-entities.v1.schema.json) — [docs](docs/embeddings-entities.md)
- Text-reuse cluster:
  - legacy: [`json/text_reuse/cluster.schema.json`](json/text_reuse/cluster.schema.json) — [docs](docs/cluster.md)
  - imp2: [`json/impresso-2/semantic-enrichment/text-reuse/cluster.v1.schema.json`](json/impresso-2/semantic-enrichment/text-reuse/cluster.v1.schema.json) — [docs](docs/cluster-1.md)
- Text-reuse passage:
  - legacy: [`json/text_reuse/passage.schema.json`](json/text_reuse/passage.schema.json) — [docs](docs/passage.md)
  - imp2: [`json/impresso-2/semantic-enrichment/text-reuse/passage.v1.schema.json`](json/impresso-2/semantic-enrichment/text-reuse/passage.v1.schema.json) — [docs](docs/passage-1.md)
- Image embeddings:
  - legacy: [`json/image_embeddings/image_embeddings.schema.json`](json/image_embeddings/image_embeddings.schema.json) — [docs](docs/image_embeddings.md)
  - imp2: [`json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json`](json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json) — [docs](docs/image-embeddings.md)
- Image classification:
  - legacy: [`json/image_classification/image_classification.schema.json`](json/image_classification/image_classification.schema.json) — [docs](docs/image_classification.md)
  - imp2: [`json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json`](json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json) — [docs](docs/image-classification.md)

### Solr indexing

Solr schemas are currently available only in the imp2 namespace.

- Content items:
  - Access rights: [`json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json) — [docs](docs/content-item-3.md)
  - Contextual metadata: [`json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.v1.schema.json) — [docs](docs/content-item-2.md)
  - Provider metadata: [`json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json) — [docs](docs/content-item-5.md)
  - Core fields: [`json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json) — [docs](docs/content-item-1.md)
  - Image fields: [`json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json) — [docs](docs/content-item-6.md)
  - Audio fields: [`json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json) — [docs](docs/content-item-7.md)
  - Paper fields: [`json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json) — [docs](docs/content-item-8.md)
  - Semantic-enrichment fields: [`json/impresso-2/solr-indexing/content-item/content-item.part.text.semantic-enrichments.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.text.semantic-enrichments.v1.schema.json) — [docs](docs/content-item-4.md)
  - Transcript fields: [`json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json) — [docs](docs/content-item.md)
  - Audio root: [`json/impresso-2/solr-indexing/content-item/content-item.root.audio.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.root.audio.v1.schema.json) — [docs](docs/content-item-9.md)
  - Image root: [`json/impresso-2/solr-indexing/content-item/content-item.root.image.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.root.image.v1.schema.json) — [docs](docs/content-item-10.md)
  - Paper root: [`json/impresso-2/solr-indexing/content-item/content-item.root.paper.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.root.paper.v1.schema.json) — [docs](docs/content-item-11.md)
- Semantic enrichments:
  - Text-reuse passage fields: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json) — [docs](docs/sem.md)
  - Entities: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json) — [docs](docs/sem-1.md)
  - Entity profiles: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json) — [docs](docs/sem-2.md)
  - Mentions: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json) — [docs](docs/sem-3.md)
  - Topics: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json) — [docs](docs/sem-4.md)
  - Text-reuse clusters: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json) — [docs](docs/sem-5.md)
  - Text-reuse passages: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-passages.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-passages.v1.schema.json) — [docs](docs/sem-6.md)
  - Word embeddings: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json) — [docs](docs/sem-7.md)

### Web app

No web-app schemas have been added yet.

## Project

The _impresso - Media Monitoring of the Past_ project is funded by the Swiss
National Science Foundation (SNSF) under grant number
[CRSII5_173719](http://p3.snf.ch/project-173719) (Sinergia program). The
project develops tools to process and explore large-scale collections of
historical newspapers. More information is available at the
[Impresso website](https://impresso-project.ch/).

## License

Copyright (C) 2026 The _impresso_ team. Contributors include
[Simon Clematide](https://github.com/simon-clematide),
[Maud Ehrmann](https://github.com/e-maud),
[Matteo Romanello](http://github.com/mromanello/), and Pauline Conti.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version. See the
[GNU Affero General Public License](https://github.com/impresso/impresso-schemas/blob/master/LICENSE)
for details.
