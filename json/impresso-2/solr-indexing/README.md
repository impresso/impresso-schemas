# Impresso Solr JSON Schemas

This directory contains JSON Schema definitions for all data types indexed in the Impresso Solr collections. The schemas ensure data consistency, enable validation, and serve as documentation for the data model.

## 📁 Directory Structure

```
schemas/
├── json/                           # JSON Schema definitions
│   ├── content-item/              # Content item schemas (articles, audio, images)
│   └── semantic-enrichments/      # Semantic enrichment schemas (entities, topics, etc.)
├── examples/                       # Example documents matching each schema
├── scripts/                        # Validation and generation tools
│   └── validate_schemas.py        # Schema validation script
├── avro/                          # Avro schemas (future)
└── README.md                      # This file
```

## 🎯 Overview

The schemas are organized into two main categories:

### 1. Content Items (`json/content-item/`)
Schemas for the primary content indexed in Solr - newspaper articles, audio transcripts, and images.

### 2. Semantic Enrichments (`json/semantic-enrichments/`)
Schemas for annotations and enrichments applied to content items - entities, topics, text reuse, etc.

---

## 📋 Content Item Schemas

Content item schemas use a **modular design** - they are split into multiple parts that are composed into root schemas for different media types.

### Modular Schema Parts

| Schema File | Description |
|------------|-------------|
| `content-item.part.core.schema.json` | Core fields present in all content items (id, title, date, newspaper) |
| `content-item.part.access-rights.schema.json` | Access rights and licensing information |
| `content-item.part.contextual-metadata.schema.json` | Metadata about context (issue, page numbers) |
| `content-item.part.image.schema.json` | Image-specific fields (IIIF manifests, coordinates, OCR quality) |
| `content-item.part.text.paper.schema.json` | Text fields for newspaper articles |
| `content-item.part.text.audio.schema.json` | Audio stream-structural fields (timing, records, utterance breaks) |
| `content-item.part.text.transcript.schema.json` | Transcript structure for audio/video |
| `content-item.part.text.semantic-enrichments.schema.json` | Links to semantic annotations (entities, topics, etc.) |
| `content-item.part.contextual-metadata.provider.schema.json` | Provider-verbatim metadata fields (`meta_prv_` prefix) — not harmonised by Impresso |

### Root Schemas (Composite)

These schemas compose the modular parts into complete schemas for each media type:

| Root Schema | Composes | Description |
|------------|----------|-------------|
| `content-item.root.paper.schema.json` | core + access-rights + contextual-metadata + text.paper + image + semantic-enrichments | Complete schema for newspaper articles |
| `content-item.root.audio.schema.json` | core + access-rights + contextual-metadata + text.audio + text.transcript + semantic-enrichments + **contextual-metadata.provider** | Complete schema for audio content |
| `content-item.root.image.schema.json` | core + access-rights + image | Complete schema for standalone images |

### How Schema Composition Works

The root schemas reference the part schemas using `$ref`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://impresso-project.ch/schemas/json/content-item/content-item.root.paper.schema.json",
  "allOf": [
    { "$ref": "content-item.part.core.schema.json" },
    { "$ref": "content-item.part.access-rights.schema.json" },
    { "$ref": "content-item.part.text.paper.schema.json" },
    ...
  ]
}
```

**Benefits of Modular Design:**
- ✅ Reuse common schemas across media types
- ✅ Easier maintenance (change once, applies everywhere)
- ✅ Clear separation of concerns
- ✅ Can validate individual parts independently

---

## 🏷️ Semantic Enrichment Schemas

These schemas define standalone documents for various semantic annotations that enrich the content items.

### Root Schemas (Standalone)

| Schema File | Solr Collection | Description |
|------------|-----------------|-------------|
| `sem.root.entities.schema.json` | `12_impresso_entity_profiles` | Entity profile documents (persons, locations, organizations) |
| `sem.root.mentions.schema.json` | `13_impresso_entity_mentions` | Entity mention documents linking entities to content items |
| `sem.root.topics.schema.json` | `02_impresso_topics` | Topic classification documents |
| `sem.root.tr-clusters.schema.json` | `04_impresso_tr_clusters` | Text reuse cluster documents |
| `sem.root.tr-passages.schema.json` | `05_impresso_tr_passages` | Text reuse passage documents |
| `sem.root.wemb.schema.json` | `06_impresso_word_embeddings` | Word embedding documents |
| `sem.root.entity-profiles.schema.json` | `12_impresso_entity_profiles` | Extended entity profile schema |

### Modular Parts

| Schema File | Description |
|------------|-------------|
| `sem.part.tr-passages.schema.json` | Shared text reuse passage properties |

---

## 📝 Example Documents

The `examples/` directory contains real-world example documents that validate against each schema:

### Content Item Examples

| Example File | Schema | Description |
|-------------|--------|-------------|
| `ci_paper.example.json` | `content-item.root.paper` | Sample newspaper article |
| `ci_audio.example.json` | `content-item.root.audio` | Sample audio transcript |
| `ci_image.example.json` | `content-item.root.image` | Sample image document |
| `ci_typescript.example.json` | `content-item.root.audio` | Sample typescript document |

### Semantic Enrichment Examples

| Example File | Schema | Description |
|-------------|--------|-------------|
| `sem_entities.example.json` | `sem.root.entities` | Sample entity document |
| `sem_mentions.example.json` | `sem.root.mentions` | Sample mention document |
| `sem_topics.example.json` | `sem.root.topics` | Sample topic document |
| `sem_tr-clusters.example.json` | `sem.root.tr-clusters` | Sample text reuse cluster |
| `sem_tr-passages.example.json` | `sem.root.tr-passages` | Sample text reuse passage |
| `sem_wemb.example.json` | `sem.root.wemb` | Sample word embedding |

---

## 🔧 Validation Script

The `validate_schemas.py` script provides comprehensive validation capabilities.

### Features

1. **Schema Validation**: Validates that JSON schemas themselves are well-formed
2. **Example Validation**: Validates example documents against their schemas
3. **Cross-Reference Resolution**: Resolves `$ref` references between modular schemas
4. **Avro Generation**: Converts JSON schemas to Avro format (experimental)

### Usage

```bash
cd impresso_solr/schemas/scripts

# Validate all schemas
python validate_schemas.py --schema --data all

# Validate specific dataset
python validate_schemas.py --schema --example --data ci-paper

# Validate only examples
python validate_schemas.py --example --data all

# Generate Avro schemas
python validate_schemas.py --schema --avro --data ci-paper
```

### Available Datasets

**Content Items:**
- `ci-paper` - Newspaper articles
- `ci-audio` - Audio/transcript documents  
- `ci-image` - Image documents

**Semantic Enrichments:**
- `topics` - Topic classifications
- `entities` - Entity profiles
- `mentions` - Entity mentions
- `tr-passages` - Text reuse passages
- `tr-clusters` - Text reuse clusters
- `wemb` - Word embeddings

**Special:**
- `all` - Validate all datasets

### Command-Line Options

```
--schema          Validate JSON schemas are well-formed
--example         Validate examples against schemas
--avro            Generate Avro schemas from JSON schemas
--data TYPE       Dataset to validate (ci-paper, topics, all, etc.)
```

---

## 🎨 Schema Design Principles

### 1. **Modular Architecture**
- Split schemas into reusable parts
- Compose complete schemas from parts using `$ref`
- Enables code reuse and easier maintenance

### 2. **Permissive by Default**
- All schemas use `"additionalProperties": true`
- Allows flexibility for future fields
- Easier evolution without breaking changes

### 3. **Clear Documentation**
- Every property includes a `description` field
- Examples illustrate expected values
- Consistent naming conventions

### 4. **Validation Levels**

| Level | Description |
|-------|-------------|
| **Required** | Fields that must be present (e.g., `id`, `title`) |
| **Optional** | Fields that may or may not be present |
| **Nullable** | Fields that can be `null` when present |

### 5. **JSON Schema 2020-12**
All schemas use the `2020-12` specification for modern features and better tooling support.

---

## 🔍 Schema Reference Guide

### Common Field Patterns

#### Identifier Fields
```json
"id": {
  "type": "string",
  "description": "Unique identifier for the document",
  "pattern": "^[A-Z]+-\\d{4}-\\d{2}-\\d{2}-[a-z]-[ip]\\d+"
}
```

#### Date Fields
```json
"date": {
  "type": "string",
  "description": "Publication date in ISO 8601 format",
  "format": "date"
}
```

#### Multi-language Text Fields
```json
"title": {
  "type": "string",
  "description": "Title of the content item"
},
"lg": {
  "type": "string",
  "description": "Language code (ISO 639-1)",
  "pattern": "^[a-z]{2}$"
}
```

#### Array of References
```json
"entity_ids": {
  "type": "array",
  "items": {"type": "string"},
  "description": "List of entity IDs mentioned in this document"
}
```

---

## 📚 Usage in Code

### Validating Documents Before Indexing

The schemas are used during the Solr indexing process to validate documents:

```python
from impresso_solr.schemas.helpers.schema_validators import validate_jsonschema_partition

# Validate a partition of documents
bag_validated = bag_docs.map_partitions(
    validate_jsonschema_partition,
    data_type='text',  # or 'topics', 'entities', etc.
    mode='log'         # Log errors but don't raise
)
```

### Loading Schemas Programmatically

```python
from pathlib import Path
import json

# Load a schema
schema_dir = Path("impresso_solr/schemas/json/content-item")
with open(schema_dir / "content-item.root.paper.schema.json") as f:
    schema = json.load(f)

# Validate a document
import jsonschema
jsonschema.validate(document, schema)
```

---

## 🚀 Future Work

### Planned Enhancements

1. **Avro Schemas**
   - Complete conversion from JSON Schema to Avro
   - Enable efficient binary serialization
   - Better integration with data pipelines

2. **Schema Registry**
   - Central repository for schema versions
   - Schema evolution tracking
   - Backward/forward compatibility checks

3. **Automated Testing**
   - CI/CD integration for schema validation
   - Regression tests for schema changes
   - Performance benchmarks

4. **Documentation Generation**
   - Auto-generate HTML documentation from schemas
   - Interactive schema explorer
   - Field statistics and usage examples

---

## 🤝 Contributing

When adding or modifying schemas:

1. **Update the schema** in `json/` directory
2. **Add/update examples** in `examples/` directory
3. **Run validation** to ensure everything passes:
   ```bash
   python scripts/validate_schemas.py --schema --example --data all
   ```
4. **Update this README** if structure changes
5. **Document breaking changes** in commit messages

### Schema Naming Conventions

- **Part schemas**: `{category}.part.{name}.schema.json`
- **Root schemas**: `{category}.root.{type}.schema.json`
- **Examples**: `{category}_{type}.example.json`

Where:
- `{category}` = `content-item` or `sem` (semantic enrichment)
- `{name}` = descriptive name of the schema part
- `{type}` = media type or enrichment type

---

## 📞 Contact & Support

- **Schema Issues**: Open an issue in the repository
- **Questions**: Contact the Impresso development team
- **Documentation**: See the main project README

---

## 📄 License

These schemas are part of the Impresso project. See the main project LICENSE file for details.

---

**Last Updated**: January 2026
**Schema Version**: 1.0
**Maintainer**: Impresso Development Team
