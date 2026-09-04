# Impresso JSON Schemas

JSON schemas for the [Impresso project](https://impresso-project.ch/). They
define, validate, and document historical newspaper and broadcast data
throughout its lifecycle: from input normalisation into canonical
representations, through text processing, semantic enrichment, and indexing,
to the requirements of the Impresso web application.

All schemas follow **JSON Schema draft 2020-12**. Schema `$id` URIs are rooted
at `https://impresso.github.io/impresso-schemas/`.

```mermaid
flowchart LR
    A["Data preparation<br/>canonical representations"]
    B["Text processing"]
    C["Semantic enrichment"]
    D["Solr indexing"]
    E["Web application"]

    A --> B --> C --> D --> E
```

## Contents

- [Schema management](#schema-management)
  - [Repository layout](#repository-layout)
  - [Namespaces and versioning](#namespaces-and-versioning)
  - [Development workflow](#development-workflow)
- [Schemas](#schemas)
  - [Common schemas](#common-schemas)
  - [Data preparation](#data-preparation)
  - [Text processing](#text-processing)
  - [Semantic enrichment](#semantic-enrichment)
  - [Solr indexing](#solr-indexing)
  - [Web app](#web-app)
- [About](#about)
  - [Copyrights](#copyrights)
  - [License](#license)
  - [Impresso](#impresso)
  - [Related Publications](#related-publications)

## Schema management

### Repository layout

```text
json/                                   Schema source of truth
├── canonical/, rebuilt/                Legacy data-preparation schemas
├── versioning/, visualizer/            Legacy supporting schemas
├── language_identification/,
│   linguistic_annotation/, ocr_qa/     Legacy text-processing schemas
├── embeddings/, entities/, image_*/,
│   text_reuse/, topic_model/           Legacy semantic-enrichment schemas
└── impresso-2/                         Versioned lifecycle-based namespace
    ├── common/                         Cross-lifecycle shared definitions
    ├── data-preparation/
    │   └── common/                     Data-preparation-only fragments
    ├── text-processing/
    │   └── common/                     Text-processing-only fragments
    ├── semantic-enrichment/
    │   └── common/                     Semantic-enrichment-only fragments
    ├── solr-indexing/
    └── web-app/

examples/                               Validation fixtures
└── impresso-2/                         Mirrors json/impresso-2/
docs/                                   Generated Markdown; do not edit manually
├── legacy/                              Documentation for stable legacy schemas
└── impresso-2/                          Documentation for versioned schemas
tests/                                  Schema integrity and example validation
```

### Namespaces and versioning

The existing directories directly under `json/` are the **legacy namespace**.
Their paths and published `$id` values are stable and must not change.

New versioned contracts live under `json/impresso-2/`. They use filenames such
as `issue.v1.schema.json`; the repository path and published `$id` must match
exactly. Reserve `json/impresso-2/common/` for definitions that genuinely share
the same semantics across lifecycle areas. Reusable fragments that apply only
within one lifecycle area belong under that area, for example
`json/impresso-2/data-preparation/common/`.

Impresso 2 is an evolving contract and may not yet validate every existing
production dataset. Consumers must explicitly choose the legacy or Impresso 2
namespace and validate their data before switching.

Use `<concept>.vN.schema.json` for a standalone reusable value or object
definition. Use `<concept>.part.vN.schema.json` for an object fragment composed
into another schema through `allOf`. Do not add `shared` to filenames: its
directory already expresses its scope.

Mark a deprecated property with the JSON Schema `"deprecated": true` keyword,
not a `(deprecated)` note folded into its `description`. Keep the description
itself accurate and current (e.g. what replaces it), so tooling that reads
`deprecated` and text that reads `description` stay in sync.

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
make tests-legacy     # Validate legacy schemas, references, and examples
make tests-imp2       # Validate Impresso 2 schemas, references, and examples
make tests            # Run both validation suites
make documentation    # Regenerate docs/legacy/ and docs/impresso-2/
```

## Schemas

**legacy** links point to the stable existing namespace; **imp2** links point to the next official, versioned namespace organised by data stage area.

### Common schemas

These Impresso 2 fragments define concepts shared across lifecycle areas.

- **Content-item identifier scalar**: [`json/impresso-2/common/content-item-id.v1.schema.json`](json/impresso-2/common/content-item-id.v1.schema.json) — [docs](docs/impresso-2/content-item-id.md)
- **`ci_id` property**: [`json/impresso-2/common/ci_id.v1.schema.json`](json/impresso-2/common/ci_id.v1.schema.json) — [docs](docs/impresso-2/ci_id.md)
- **Model identifier property**: [`json/impresso-2/common/model-id.v1.schema.json`](json/impresso-2/common/model-id.v1.schema.json) — [docs](docs/impresso-2/model-id.md)
- **Timestamp scalar**: [`json/impresso-2/common/timestamp.v1.schema.json`](json/impresso-2/common/timestamp.v1.schema.json) — [docs](docs/impresso-2/timestamp.md)
- **`ts` property**: [`json/impresso-2/common/ts.v1.schema.json`](json/impresso-2/common/ts.v1.schema.json) — [docs](docs/impresso-2/ts.md)
- **Language-code scalar**: [`json/impresso-2/common/language-code.v1.schema.json`](json/impresso-2/common/language-code.v1.schema.json) — [docs](docs/impresso-2/language-code.md)
- **Probability scalar**: [`json/impresso-2/common/probability.v1.schema.json`](json/impresso-2/common/probability.v1.schema.json) — [docs](docs/impresso-2/probability.md)
- **Bounding-box scalar**: [`json/impresso-2/common/bounding-box.v1.schema.json`](json/impresso-2/common/bounding-box.v1.schema.json) — [docs](docs/impresso-2/bounding-box.md)
- **Data-processing stage scalar**: [`json/impresso-2/common/data-stage.v1.schema.json`](json/impresso-2/common/data-stage.v1.schema.json) — [docs](docs/impresso-2/data-stage.md)
- **Time-coordinates scalar**: [`json/impresso-2/common/time-coordinates.v1.schema.json`](json/impresso-2/common/time-coordinates.v1.schema.json) — [docs](docs/impresso-2/time-coordinates.md)

### Data preparation

Area-local common scalars shared by the data-preparation schemas below:

- **Source-type scalar**: [`json/impresso-2/data-preparation/common/source-type.v1.schema.json`](json/impresso-2/data-preparation/common/source-type.v1.schema.json)
- **Source-medium scalar**: [`json/impresso-2/data-preparation/common/source-medium.v1.schema.json`](json/impresso-2/data-preparation/common/source-medium.v1.schema.json)
- **Media-title variant scalar**: [`json/impresso-2/data-preparation/common/media-title-variant.v1.schema.json`](json/impresso-2/data-preparation/common/media-title-variant.v1.schema.json) — [docs](docs/impresso-2/media-title-variant.md)
- **Exact-date flag scalar**: [`json/impresso-2/data-preparation/common/is-exact-date.v1.schema.json`](json/impresso-2/data-preparation/common/is-exact-date.v1.schema.json) — [docs](docs/impresso-2/is-exact-date.md)

- **Issue**:
  - legacy: [`json/canonical/issue.schema.json`](json/canonical/issue.schema.json) — [docs](docs/legacy/canonical/issue.md)
  - imp2: [`json/impresso-2/data-preparation/canonical/issue.v1.schema.json`](json/impresso-2/data-preparation/canonical/issue.v1.schema.json) — [docs](docs/impresso-2/issue.md)
- **Page**:
  - legacy: [`json/canonical/page.schema.json`](json/canonical/page.schema.json) — [docs](docs/legacy/canonical/page.md)
  - imp2: [`json/impresso-2/data-preparation/canonical/page.v1.schema.json`](json/impresso-2/data-preparation/canonical/page.v1.schema.json) — [docs](docs/impresso-2/page.md)
- **Audio record**:
  - legacy: [`json/canonical/audio_record.schema.json`](json/canonical/audio_record.schema.json) — [docs](docs/legacy/canonical/audio_record.md)
  - imp2: [`json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json`](json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json) — [docs](docs/impresso-2/audio-record.md)
- **Paper content item**:
  - legacy: [`json/rebuilt/paper_contentitem.schema.json`](json/rebuilt/paper_contentitem.schema.json) — [docs](docs/legacy/rebuilt/paper_contentitem.md)
  - imp2: [`json/impresso-2/data-preparation/rebuilt/paper-contentitem.v1.schema.json`](json/impresso-2/data-preparation/rebuilt/paper-contentitem.v1.schema.json) — [docs](docs/impresso-2/paper-contentitem.md)
- **Audio-record content item**:
  - legacy: [`json/rebuilt/audio_record_contentitem.schema.json`](json/rebuilt/audio_record_contentitem.schema.json) — [docs](docs/legacy/rebuilt/audio_record_contentitem.md)
  - imp2: [`json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json`](json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json) — [docs](docs/impresso-2/audio-record-contentitem.md)
- **Manifest**:
  - legacy: [`json/versioning/manifest.schema.json`](json/versioning/manifest.schema.json) — [docs](docs/legacy/versioning/manifest.md)
  - imp2: [`json/impresso-2/data-preparation/versioning/manifest.v1.schema.json`](json/impresso-2/data-preparation/versioning/manifest.v1.schema.json) — [docs](docs/impresso-2/manifest.md)
- **Bounding-box visualizer**:
  - legacy: [`json/visualizer/bbox_visualizer.schema.json`](json/visualizer/bbox_visualizer.schema.json) — [docs](docs/legacy/visualizer/bbox_visualizer.md)
  - imp2: [`json/impresso-2/data-preparation/visualizer/bbox-visualizer.v1.schema.json`](json/impresso-2/data-preparation/visualizer/bbox-visualizer.v1.schema.json) — [docs](docs/impresso-2/bbox-visualizer.md)

### Text processing

- **Language identification**:
  - legacy: [`json/language_identification/language_identification.schema.json`](json/language_identification/language_identification.schema.json) — [docs](docs/legacy/language_identification/language_identification.md)
  - imp2: [`json/impresso-2/text-processing/language-identification/language-identification.v1.schema.json`](json/impresso-2/text-processing/language-identification/language-identification.v1.schema.json) — [docs](docs/impresso-2/language-identification.md)
- **Linguistic annotation (spaCy)**:
  - legacy: [`json/linguistic_annotation/ling_spacy.schema.json`](json/linguistic_annotation/ling_spacy.schema.json) — [docs](docs/legacy/linguistic_annotation/ling_spacy.md)
  - imp2: [`json/impresso-2/text-processing/linguistic-annotation/ling-spacy.v1.schema.json`](json/impresso-2/text-processing/linguistic-annotation/ling-spacy.v1.schema.json) — [docs](docs/impresso-2/ling-spacy.md)
- **Linguistic processing**:
  - legacy: [`json/linguistic_annotation/lingproc.v2.schema.json`](json/linguistic_annotation/lingproc.v2.schema.json) — [docs](docs/legacy/linguistic_annotation/lingproc.md)
  - imp2: [`json/impresso-2/text-processing/linguistic-annotation/lingproc.v1.schema.json`](json/impresso-2/text-processing/linguistic-annotation/lingproc.v1.schema.json) — [docs](docs/impresso-2/lingproc.md)
- **OCR QA**:
  - legacy: [`json/ocr_qa/ocr_qa.schema.json`](json/ocr_qa/ocr_qa.schema.json) — [docs](docs/legacy/ocr_qa/ocr_qa.md)
  - imp2: [`json/impresso-2/text-processing/ocr-qa/ocr-qa.v1.schema.json`](json/impresso-2/text-processing/ocr-qa/ocr-qa.v1.schema.json) — [docs](docs/impresso-2/ocr-qa.md)

### Semantic enrichment

- **Topic assignment**:
  - legacy v1: [`json/topic_model/topic_assignment.schema.json`](json/topic_model/topic_assignment.schema.json) — [docs](docs/legacy/topic_model/topic_assignment.md)
  - legacy v2: [`json/topic_model/topic_assignment.v2.schema.json`](json/topic_model/topic_assignment.v2.schema.json) — [docs](docs/legacy/topic_model/topic_assignment-1.md)
  - imp2: [`json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json`](json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json) — [docs](docs/impresso-2/topic-assignment.md)
- **Topic description**:
  - legacy: [`json/topic_model/topic_description.schema.json`](json/topic_model/topic_description.schema.json) — [docs](docs/legacy/topic_model/topic_description.md)
  - imp2: [`json/impresso-2/semantic-enrichment/topic-model/topic-description.v1.schema.json`](json/impresso-2/semantic-enrichment/topic-model/topic-description.v1.schema.json) — [docs](docs/impresso-2/topic-description.md)
- **Entities**:
  - legacy: [`json/entities/entities.schema.json`](json/entities/entities.schema.json) — [docs](docs/legacy/entities/entities.md)
  - imp2: [`json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json`](json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json) — [docs](docs/impresso-2/entities.md)
- **Document embeddings**:
  - legacy: [`json/embeddings/embeddings-docs.schema.json`](json/embeddings/embeddings-docs.schema.json) — [docs](docs/legacy/embeddings/embeddings-docs.md)
  - imp2: [`json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json`](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json) — [docs](docs/impresso-2/embeddings-docs.md)
- **Sentence embeddings**:
  - legacy: [`json/embeddings/embeddings-sentence.schema.json`](json/embeddings/embeddings-sentence.schema.json) — [docs](docs/legacy/embeddings/embeddings-sentence.md)
  - imp2: [`json/impresso-2/semantic-enrichment/document-embeddings/embeddings-sentence.v1.schema.json`](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-sentence.v1.schema.json) — [docs](docs/impresso-2/embeddings-sentence.md)
- **Chunk embeddings**:
  - legacy: [`json/embeddings/embeddings-chunks.schema.json`](json/embeddings/embeddings-chunks.schema.json) — [docs](docs/legacy/embeddings/embeddings-chunks.md)
  - imp2: [`json/impresso-2/semantic-enrichment/document-embeddings/embeddings-chunks.v1.schema.json`](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-chunks.v1.schema.json) — [docs](docs/impresso-2/embeddings-chunks.md)
- **Entity embeddings**:
  - legacy: [`json/embeddings/embeddings-entities.schema.json`](json/embeddings/embeddings-entities.schema.json) — [docs](docs/legacy/embeddings/embeddings-entities.md)
  - imp2: [`json/impresso-2/semantic-enrichment/document-embeddings/embeddings-entities.v1.schema.json`](json/impresso-2/semantic-enrichment/document-embeddings/embeddings-entities.v1.schema.json) — [docs](docs/impresso-2/embeddings-entities.md)
- **Text-reuse cluster**:
  - legacy: [`json/text_reuse/cluster.schema.json`](json/text_reuse/cluster.schema.json) — [docs](docs/legacy/text_reuse/cluster.md)
  - imp2: [`json/impresso-2/semantic-enrichment/text-reuse/cluster.v1.schema.json`](json/impresso-2/semantic-enrichment/text-reuse/cluster.v1.schema.json) — [docs](docs/impresso-2/cluster.md)
- **Text-reuse passage**:
  - legacy: [`json/text_reuse/passage.schema.json`](json/text_reuse/passage.schema.json) — [docs](docs/legacy/text_reuse/passage.md)
  - imp2: [`json/impresso-2/semantic-enrichment/text-reuse/passage.v1.schema.json`](json/impresso-2/semantic-enrichment/text-reuse/passage.v1.schema.json) — [docs](docs/impresso-2/passage.md)
- **Image embeddings**:
  - legacy: [`json/image_embeddings/image_embeddings.schema.json`](json/image_embeddings/image_embeddings.schema.json) — [docs](docs/legacy/image_embeddings/image_embeddings.md)
  - imp2: [`json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json`](json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json) — [docs](docs/impresso-2/image-embeddings.md)
- **Image classification**:
  - legacy: [`json/image_classification/image_classification.schema.json`](json/image_classification/image_classification.schema.json) — [docs](docs/legacy/image_classification/image_classification.md)
  - imp2: [`json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json`](json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json) — [docs](docs/impresso-2/image-classification.md)

### Solr indexing

Solr schemas are available only in the imp2 namespace.

- **Content items**:
  - **Access rights**: [`json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json) — [docs](docs/impresso-2/content-item-3.md)
  - **Contextual metadata**: [`json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.v1.schema.json) — [docs](docs/impresso-2/content-item-2.md)
  - **Provider metadata**: [`json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json) — [docs](docs/impresso-2/content-item-5.md)
  - **Core fields**: [`json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json) — [docs](docs/impresso-2/content-item-1.md)
  - **Image fields**: [`json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json) — [docs](docs/impresso-2/content-item-6.md)
  - **Audio fields**: [`json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json) — [docs](docs/impresso-2/content-item-7.md)
  - **Paper fields**: [`json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json) — [docs](docs/impresso-2/content-item-8.md)
  - **Semantic-enrichment fields**: [`json/impresso-2/solr-indexing/content-item/content-item.part.text.semantic-enrichments.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.text.semantic-enrichments.v1.schema.json) — [docs](docs/impresso-2/content-item-4.md)
  - **Transcript fields**: [`json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json) — [docs](docs/impresso-2/content-item.md)
  - **Audio root**: [`json/impresso-2/solr-indexing/content-item/content-item.root.audio.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.root.audio.v1.schema.json) — [docs](docs/impresso-2/content-item-9.md)
  - **Image root**: [`json/impresso-2/solr-indexing/content-item/content-item.root.image.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.root.image.v1.schema.json) — [docs](docs/impresso-2/content-item-10.md)
  - **Paper root**: [`json/impresso-2/solr-indexing/content-item/content-item.root.paper.v1.schema.json`](json/impresso-2/solr-indexing/content-item/content-item.root.paper.v1.schema.json) — [docs](docs/impresso-2/content-item-11.md)
- **Semantic enrichments**:
  - **Text-reuse passage fields**: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json) — [docs](docs/impresso-2/sem.md)
  - **Entities**: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json) — [docs](docs/impresso-2/sem-1.md)
  - **Entity profiles**: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json) — [docs](docs/impresso-2/sem-2.md)
  - **Mentions**: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json) — [docs](docs/impresso-2/sem-3.md)
  - **Topics**: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json) — [docs](docs/impresso-2/sem-4.md)
  - **Text-reuse clusters**: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json) — [docs](docs/impresso-2/sem-5.md)
  - **Text-reuse passages**: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-passages.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-passages.v1.schema.json) — [docs](docs/impresso-2/sem-6.md)
  - **Word embeddings**: [`json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json`](json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json) — [docs](docs/impresso-2/sem-7.md)

### Web app

No web-app schemas have been added yet.

## About

### Copyrights

Copyright (C) 2017 The _impresso_ team. Contributors include
[Simon Clematide](https://github.com/simon-clematide),
[Pauline Conti](https://github.com/piconti)
[Maud Ehrmann](https://github.com/e-maud), and
[Matteo Romanello](http://github.com/mromanello/).

### License

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version. See the
[GNU Affero General Public License](https://github.com/impresso/impresso-schemas/blob/master/LICENSE)
for details.

### Impresso

[Impresso - Media Monitoring of the Past](https://impresso-project.ch) is an
interdisciplinary research project that aims to develop and consolidate tools for
processing and exploring large collections of media archives across modalities, time,
languages and national borders. The first project (2017-2021) was funded by the Swiss
National Science Foundation under grant
No. [CRSII5_173719](http://p3.snf.ch/project-173719) and the second project (2023-2027)
by the SNSF under grant No. [CRSII5_213585](https://data.snf.ch/grants/grant/213585))
and the Luxembourg National Research Fund under grant No. 17498891.

### Related Publications

#### Impresso 2

Conti, P. I., Clematide, S., & Ehrmann, M. (2026). [Toward Interoperable and
Scalable Representations of Complex Heterogeneous Digitized Historical
Media](https://infoscience.epfl.ch/handle/20.500.14299/263437). _Proceedings
of the First Workshop on Creating Interoperable Corpora of Historical
Newspapers (PressMint 2026)_, 72–81.

<details>
<summary>BibTeX</summary>

```bibtex
@inproceedings{conti_interoperable_2026,
  title = {Toward {{Interoperable}} and {{Scalable Representations}} of {{Complex Heterogeneous Digitized Historical Media}}},
  booktitle = {Proceedings of the {{First Workshop}} on {{Creating Interoperable Corpora}} of {{Historical Newspapers}}},
  author = {Conti, Pauline Isabela and Clematide, Simon and Ehrmann, Maud},
  editor = {Ogrodniczuk, Maciej and Osenova, Petya and Wissik, Tanja},
  year = 2026,
  month = may,
  pages = {72--81},
  publisher = {ELRA Language Resources Association},
  address = {Palma de Mallorca},
  url = {https://infoscience.epfl.ch/handle/20.500.14299/263437},
  urldate = {2026-05-18},
  isbn = {978-2-493814-49-4}
}
```

</details>

#### Impresso 1

Romanello, M., Ehrmann, M., Clematide, S., & Guido, D. (2020). [The impresso
system architecture in a nutshell](https://infoscience.epfl.ch/handle/20.500.14299/175573)
[Research Report]. _EuropeanaTech Insights_.

<details>
<summary>BibTeX</summary>

```bibtex
@inproceedings{romanello_impresso_2020,
  title = {The Impresso System Architecture in a Nutshell},
  booktitle = {{{EuropeanaTech}} Insights},
  author = {Romanello, Matteo and Ehrmann, Maud and Clematide, Simon and Guido, Daniele},
  year = 2020,
  url = {https://pro.europeana.eu/page/issue-16-newspapers#the-impresso-system-architecture-in-a-nutshell},
  urldate = {2021-03-05},
  keywords = {cited},
  annotation = {https://www.semanticscholar.org/paper/The-impresso-system-architecture-in-a-nutshell-Romanello-Ehrmann/28bfc855527a1cb6dcaade90f7aac50772f00667}
}
```

</details>

Ehrmann, M., Romanello, M., Clematide, S., Ströbel, P. B., & Barman, R.
(2020). [Language Resources for Historical Newspapers: the Impresso
Collection](https://doi.org/10.5281/zenodo.4641902). In N. Calzolari,
F. Béchet, P. Blache, K. Choukri, C. Cieri, T. Declerck, S. Goggi,
H. Isahara, B. Maegaard, J. Mariani, H. Mazo, A. Moreno, J. Odijk, &
S. Piperidis (Eds.), _Proceedings of the 12th Language Resources and
Evaluation Conference_.

<details>
<summary>BibTeX</summary>

```bibtex
@inproceedings{ehrmann_language_2020,
  ids = {ehrmann-EtAl:2020:LREC,ehrmann_language_2020a,ehrmann_language_2020c},
  title = {Language {{Resources}} for {{Historical Newspapers}}: The {{Impresso Collection}}},
  shorttitle = {Language {{Resources}} for {{Historical Newspapers}}},
  booktitle = {Proceedings of the {{Twelfth Language Resources}} and {{Evaluation Conference}}},
  author = {Ehrmann, Maud and Romanello, Matteo and Clematide, Simon and Str{\"o}bel, Phillip Benjamin and Barman, Rapha{\"e}l},
  editor = {Calzolari, Nicoletta and B{\'e}chet, Fr{\'e}d{\'e}ric and Blache, Philippe and Choukri, Khalid and Cieri, Christopher and Declerck, Thierry and Goggi, Sara and Isahara, Hitoshi and Maegaard, Bente and Mariani, Joseph and Mazo, H{\'e}l{\`e}ne and Moreno, Asuncion and Odijk, Jan and Piperidis, Stelios},
  year = 2020,
  month = may,
  pages = {958--968},
  publisher = {European Language Resources Association},
  address = {Marseille, France},
  url = {https://aclanthology.org/2020.lrec-1.121},
  urldate = {2024-06-30},
  isbn = {979-10-95546-34-4},
  keywords = {cited}
}
```

</details>

---

<p align="center">
  <img src="https://github.com/impresso/impresso.github.io/blob/master/assets/images/3x1--Yellow-Impresso-Black-on-White--transparent.png?raw=true" width="350" alt="Impresso Project Logo"/>
</p>
