# Impresso JSON Schemas

JSON schemas for the [Impresso project](https://impresso-project.ch/), used to define, validate, and document the structure of historical newspaper and broadcast data formats.

All schemas follow **JSON Schema draft 2020-12**. Schema `$id` URIs are rooted at `https://impresso.github.io/impresso-schemas/`.

## Schemas

### Canonical formats (`json/canonical/`)

| Schema                     | Description               | Docs                                         |
| -------------------------- | ------------------------- | -------------------------------------------- |
| `issue.schema.json`        | Newspaper issue           | [docs/issue.md](docs/issue.md)               |
| `page.schema.json`         | Newspaper page            | [docs/page.md](docs/page.md)                 |
| `audio_record.schema.json` | Radio/TV broadcast record | [docs/audio_record.md](docs/audio_record.md) |

### Rebuilt formats (`json/rebuilt/`)

| Schema                                 | Description                    | Docs                                                                 |
| -------------------------------------- | ------------------------------ | -------------------------------------------------------------------- |
| `paper_contentitem.schema.json`        | Rebuilt newspaper content item | [docs/paper_contentitem.md](docs/paper_contentitem.md)               |
| `audio_record_contentitem.schema.json` | Rebuilt broadcast content item | [docs/audio_record_contentitem.md](docs/audio_record_contentitem.md) |

### Topic modelling (`json/topic_model/`)

| Schema                            | Description                            | Docs                                                   |
| --------------------------------- | -------------------------------------- | ------------------------------------------------------ |
| `topic_assignment.schema.json`    | Topic assignment per content item (v1) | [docs/topic_assignment.md](docs/topic_assignment.md)   |
| `topic_assignment.v2.schema.json` | Topic assignment per content item (v2) | [docs/topic_assignment.md](docs/topic_assignment.md)   |
| `topic_description.schema.json`   | Topic description (words + weights)    | [docs/topic_description.md](docs/topic_description.md) |

### Language identification (`json/language_identification/`)

| Schema                                | Description                       | Docs                                                               |
| ------------------------------------- | --------------------------------- | ------------------------------------------------------------------ |
| `language_identification.schema.json` | Per-token language identification | [docs/language_identification.md](docs/language_identification.md) |

### Named entities (`json/entities/`)

| Schema                 | Description           | Docs                                 |
| ---------------------- | --------------------- | ------------------------------------ |
| `entities.schema.json` | Named entity mentions | [docs/entities.md](docs/entities.md) |

### Embeddings (`json/embeddings/`)

| Schema                            | Description               | Docs                                                       |
| --------------------------------- | ------------------------- | ---------------------------------------------------------- |
| `embeddings-docs.schema.json`     | Document-level embeddings | [docs/embeddings-docs.md](docs/embeddings-docs.md)         |
| `embeddings-sentence.schema.json` | Sentence-level embeddings | [docs/embeddings-sentence.md](docs/embeddings-sentence.md) |
| `embeddings-chunks.schema.json`   | Chunk-level embeddings    | [docs/embeddings-chunks.md](docs/embeddings-chunks.md)     |
| `embeddings-entities.schema.json` | Entity embeddings         | [docs/embeddings-entities.md](docs/embeddings-entities.md) |

### Text reuse (`json/text_reuse/`)

| Schema                | Description        | Docs                               |
| --------------------- | ------------------ | ---------------------------------- |
| `cluster.schema.json` | Text reuse cluster | [docs/cluster.md](docs/cluster.md) |
| `passage.schema.json` | Text reuse passage | [docs/passage.md](docs/passage.md) |

### Image embeddings (`json/image_embeddings/`)

| Schema                         | Description            | Docs                                                 |
| ------------------------------ | ---------------------- | ---------------------------------------------------- |
| `image_embeddings.schema.json` | Image-level embeddings | [docs/image_embeddings.md](docs/image_embeddings.md) |

### Image classification (`json/image_classification/`)

| Schema                             | Description                 | Docs                                                         |
| ---------------------------------- | --------------------------- | ------------------------------------------------------------ |
| `image_classification.schema.json` | Image classification labels | [docs/image_classification.md](docs/image_classification.md) |

### Linguistic annotation (`json/linguistic_annotation/`)

| Schema                    | Description                       | Docs                                     |
| ------------------------- | --------------------------------- | ---------------------------------------- |
| `ling_spacy.schema.json`  | spaCy-based linguistic annotation | [docs/ling_spacy.md](docs/ling_spacy.md) |
| `lingproc.v2.schema.json` | Linguistic processing v2          | [docs/lingproc.md](docs/lingproc.md)     |

### OCR quality assessment (`json/ocr_qa/`)

| Schema               | Description                   | Docs |
| -------------------- | ----------------------------- | ---- |
| `ocr_qa.schema.json` | OCR quality assessment scores | —    |

### Versioning (`json/versioning/`)

| Schema                 | Description           | Docs                                 |
| ---------------------- | --------------------- | ------------------------------------ |
| `manifest.schema.json` | Data release manifest | [docs/manifest.md](docs/manifest.md) |

### Visualizer (`json/visualizer/`)

| Schema                        | Description                    | Docs                                               |
| ----------------------------- | ------------------------------ | -------------------------------------------------- |
| `bbox_visualizer.schema.json` | Bounding box visualizer format | [docs/bbox_visualizer.md](docs/bbox_visualizer.md) |

## Repository layout

```
json/          JSON schema files, organised by data type
examples/      Example JSON files used for validation tests
docs/          Generated documentation (Markdown)
scripts/       Utility scripts
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

Validate all example files against their schemas:

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
