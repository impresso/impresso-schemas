# AGENT.md — Impresso Schemas

This file provides accurate, up-to-date guidance for AI agents working in this repository.

## Purpose

This repository defines and maintains JSON schemas for the [Impresso project](https://impresso-project.ch/), which processes large-scale collections of historical newspapers and broadcast data. Schemas are used to validate and document the structure of data at various pipeline stages.

---

## Repository Layout

```
json/               JSON schema files (source of truth)
examples/           Example/test JSON files, one subdirectory per schema group
docs/               Auto-generated Markdown documentation (do not edit manually)
scripts/            Utility scripts (jsonlschema.py)
Makefile            Validation (tests) and documentation (documentation) targets
requirements.txt    Python dependencies for validation
```

### Schema Directories under `json/`

| Directory                  | Description                                             | JSON Schema Draft |
| -------------------------- | ------------------------------------------------------- | ----------------- |
| `canonical/`               | Canonical newspaper formats (issue, page, audio_record) | 2020-12           |
| `rebuilt/`                 | Rebuilt content items (paper, audio record)             | 2020-12           |
| `topic_model/`             | Topic modeling (description, assignment v1/v2)          | 2020-12           |
| `language_identification/` | Language identification                                 | 2020-12           |
| `linguistic_annotation/`   | Linguistic processing (`lingproc.v2`, `ling_spacy`)     | 2020-12           |
| `entities/`                | Named entity recognition                                | 2020-12           |
| `versioning/`              | Data release manifests                                  | 2020-12           |
| `embeddings/`              | Document, sentence, chunk, entity embeddings            | 2020-12           |
| `text_reuse/`              | Text reuse clusters and passages                        | 2020-12           |
| `image_embeddings/`        | Image embedding schemas                                 | 2020-12           |
| `visualizer/`              | Bounding box visualizer schemas                         | 2020-12           |
| `image_classification/`    | Image classification schemas                            | 2020-12           |
| `ocr_qa/`                  | OCR quality assessment                                  | 2020-12           |

### Schema Files per Directory

- `json/canonical/`: `issue.schema.json`, `page.schema.json`, `audio_record.schema.json`
- `json/rebuilt/`: `paper_contentitem.schema.json`, `audio_record_contentitem.schema.json`
- `json/topic_model/`: `topic_description.schema.json`, `topic_assignment.schema.json`, `topic_assignment.v2.schema.json`
- `json/language_identification/`: `language_identification.schema.json`
- `json/linguistic_annotation/`: `lingproc.v2.schema.json`, `ling_spacy.schema.json`
- `json/entities/`: `entities.schema.json`
- `json/versioning/`: `manifest.schema.json`
- `json/embeddings/`: `embeddings-docs.schema.json`, `embeddings-sentence.schema.json`, `embeddings-chunks.schema.json`, `embeddings-entities.schema.json`
- `json/text_reuse/`: `cluster.schema.json`, `passage.schema.json`
- `json/image_embeddings/`: `image_embeddings.schema.json`
- `json/visualizer/`: `bbox_visualizer.schema.json`
- `json/image_classification/`: `image_classification.schema.json`
- `json/ocr_qa/`: `ocr_qa.schema.json`

---

## Key Commands

```bash
# Validate all examples against their schemas
make tests
# equivalent: python -m pytest tests/ -v

# Run a single test by keyword
python -m pytest tests/ -v -k "canonical_issue"

# Show full detail on first failure
python -m pytest tests/ -v -x

# Generate Markdown documentation from schemas (overwrites docs/)
make documentation

# Remove all generated docs
make clean-documentation

# Create and activate a virtualenv, then install Python dependencies
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install .

# Install Node.js doc generator
npm install -g @adobe/jsonschema2md

# All make commands must be run with the virtualenv activated
```

---

## Known Issues

### Schemas not yet tested in `make tests`

These schemas exist but have no entry in `tests/test_schema_examples.py`:

- `json/topic_model/topic_assignment.schema.json` — example exists: `examples/topic_model_topic_assignment/example0.json`
- `json/topic_model/topic_assignment.v2.schema.json` — no example yet
- `json/embeddings/embeddings-entities.schema.json` — no example yet
- `json/linguistic_annotation/ling_spacy.schema.json` — no example yet
- `json/ocr_qa/ocr_qa.schema.json` — example exists: `examples/ocr_qa/ocr_qa_example.json`

---

## Adding a New Schema

1. Create `json/<category>/<name>.schema.json` following draft 2020-12.
2. Each schema must include `$schema`, `$id` (rooted at `https://impresso.github.io/impresso-schemas/json/…`), `title`, `description`, and typed property definitions.
3. Add one or more example files under `examples/<category>/`.
4. Add a `(schema_path, example_path)` entry to `CASES` in `tests/test_schema_examples.py`.
5. Run `make tests` to confirm validation passes.
6. Run `make documentation` to regenerate `docs/`.

## Code Style

- JSON: 2-space indentation (enforced by `.editorconfig`)
- Schema files: `.schema.json` extension
- Prettier is configured (`.prettierrc`) for JSON formatting

## Dependencies

- Python 3.11+ with `jsonschema`, `check-jsonschema` (see `requirements.txt`)
- Node.js with `@adobe/jsonschema2md` for documentation generation
