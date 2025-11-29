# Copilot Instructions for Impresso Schemas

This repository contains JSON schemas used in the [Impresso project](https://impresso-project.ch/) for defining, validating, and documenting the structure of various data formats related to historical newspaper and broadcast data.

## Repository Structure

- `json/` - JSON schema files organized by data type
  - `canonical/` - Schemas for canonical formats (issue, page, audio_record)
  - `rebuilt/` - Schemas for rebuilt formats (paper_contentitem, audio_record_contentitem)
  - `topic_model/` - Topic modeling schemas
  - `language_identification/` - Language identification schemas
  - `entities/` - Named entity schemas
  - `embeddings/` - Embedding schemas
  - `text_reuse/` - Text reuse detection schemas
  - `image_embeddings/` - Image embedding schemas
  - `image_classification/` - Image classification schemas
  - `linguistic_annotation/` - Linguistic annotation schemas
  - `ocr_qa/` - OCR quality assessment schemas
  - `versioning/` - Data versioning manifest schemas
  - `visualizer/` - Visualization schemas
- `examples/` - Example JSON files for validation testing
- `docs/` - Generated documentation in markdown format
- `scripts/` - Utility scripts

## Development Guidelines

### JSON Schema Standards

- All schemas follow the JSON Schema draft 2020-12 specification
- Schema files must have the `.schema.json` extension
- Each schema must include:
  - `$schema` pointing to the JSON Schema draft version
  - `$id` with the schema's canonical URL
  - `title` and `description` properties
  - Proper property definitions with types and descriptions

### Validation

Run schema validation tests with:

```bash
make tests
```

This validates all example JSON files against their corresponding schemas using `check-jsonschema`.

### Documentation

Generate documentation from schemas with:

```bash
make documentation
```

Documentation is generated using `@adobe/jsonschema2md` and outputs to the `docs/` directory.

### Code Style

- JSON files use 2-space indentation (see `.editorconfig`)
- Follow existing naming conventions for new schemas and examples
- Use descriptive property names with clear descriptions

### Adding New Schemas

1. Create the schema file in the appropriate `json/` subdirectory
2. Add example files in the corresponding `examples/` subdirectory
3. Add validation commands to the Makefile `tests` target
4. Add documentation generation to the Makefile `documentation` target with the correct JSON Schema draft version flag (`-v`). Different schema directories use different versions:
   - `06` for canonical, rebuilt, topic_model, language_identification, linguistic_annotation
   - `2020-12` for entities
   - `2024-02` for versioning
   - `2024-09` for embeddings, text_reuse
   - `2025-01` for image_embeddings, visualizer, image_classification
   - `2025-10` for linguistic_annotation (updated version)
5. Run `make tests` to validate examples against the schema
6. Run `make documentation` to generate updated docs

### Dependencies

- Python 3.11+ with `jsonschema` and `check-jsonschema` packages
- Node.js with `@adobe/jsonschema2md` for documentation generation

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Common Tasks

- **Modifying a schema**: Update the `.schema.json` file, ensure examples still validate with `make tests`
- **Adding an example**: Add JSON file to appropriate `examples/` subdirectory, add validation to Makefile
- **Updating documentation**: Run `make documentation` after schema changes
