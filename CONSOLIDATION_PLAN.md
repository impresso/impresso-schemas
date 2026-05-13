# Schema Consolidation Plan

This document lists concrete issues to fix for a professional, coherent schema release, ordered by priority.

---

## ~~1. Fix the Makefile so `make tests` works~~ ✓ DONE

Added `SHELL := /bin/bash` to the top of the Makefile. `check-jsonschema` is expected to be installed via `pip install -r requirements.txt` in the active virtualenv, which places it on `PATH` on both macOS and Linux.

---

## ~~2. Fix two broken example files~~ ✓ DONE

Renamed `"l"` → `"lg"` in the `m` object of all items in `example0.json` (81 items) and `example1.json` (75 items). Two image items in `example1.json` had no language field at all; they received `"lg": null` (the schema type is `["string", "null"]`). Both files now pass validation.

---

## ~~3. Standardize all schemas to JSON Schema draft 2020-12~~ ✓ DONE

All schemas migrated to `"$schema": "https://json-schema.org/draft/2020-12/schema"`. Additional fixes applied during migration:

- `definitions` → `$defs` in all affected schemas, with `$ref` pointers updated to `#/$defs/`
- Fragment-only `$id` values (`"#/properties/..."`) removed from `lingproc.v2`, `embeddings-sentence`, `embeddings-chunks` (forbidden in 2020-12)
- Tuple-form `items: [...]` replaced with `prefixItems: [...]` in `language_identification`
- Trailing `#` stripped from `$schema` URIs in `embeddings-docs`, `image_embeddings`, `image_classification`

All 35 tests pass after migration.

---

## ~~4. Fix incorrect `$id` URIs~~ ✓ DONE

Corrected `$id` in 4 schemas: `image_embeddings`, `ling_spacy`, `lingproc.v2`, `entities`.

---

## ~~5. Add missing `title` and `description` to schemas~~ ✓ DONE

Added `title` to 7 schemas, fixed empty `title` in `image_classification`, added `description` to 3 schemas (`text_reuse/cluster`, `text_reuse/passage`, `versioning/manifest`).

---

## ~~6. Simplify and fix the `documentation` target~~ ✓ DONE

Replaced 13 per-directory `jsonschema2md` calls with a single:

```makefile
jsonschema2md -d json/ --header false -n -v 2020-12 -o docs -x - -s propTable
```

This resolves cross-directory `$ref` values, eliminates the duplicate `linguistic_annotation` run, and adds `ocr_qa` coverage automatically.

---

## 7. Add missing schema tests to `make tests`

The following schemas have no entry in the Makefile `tests` target:

| Schema                                              | Example file                                          | Action                        |
| --------------------------------------------------- | ----------------------------------------------------- | ----------------------------- |
| `json/topic_model/topic_assignment.schema.json`     | `examples/topic_model_topic_assignment/example0.json` | Add test                      |
| `json/topic_model/topic_assignment.v2.schema.json`  | —                                                     | Create example, then add test |
| `json/embeddings/embeddings-entities.schema.json`   | —                                                     | Create example, then add test |
| `json/linguistic_annotation/ling_spacy.schema.json` | —                                                     | Create example, then add test |
| `json/ocr_qa/ocr_qa.schema.json`                    | `examples/ocr_qa/ocr_qa_example.json`                 | Add test                      |

---

## ~~8. Remove backup files~~ ✓ DONE

Deleted `json/embeddings/embeddings-docs-backup.schema.json` and `json/entities/entities-backup.schema.json`.

---

## ~~9. Fix the duplicate test in `make tests`~~ ✓ DONE

Removed the duplicate `SOC_VS-1943-04-28-a-i0001.json` line from the Makefile `tests` target.

---

## ~~10. Fix a typo in an example filename~~ ✓ DONE

Renamed `examples/image_embeddings/image_emendding_example.json` → `image_embedding_example.json` and updated the Makefile reference.

---

## ~~11. Rewrite README.md~~ ✓ DONE

Full rewrite: lists all 22 schemas grouped by domain with docs links, correct draft (2020-12) everywhere, removed all "(todo)" entries, added Prerequisites section.

---

## ~~12. Update `.github/copilot-instructions.md`~~ ✓ DONE

Replaced the incorrect per-directory draft version table in "Adding New Schemas" step 4 with a single note: the `documentation` target runs one `jsonschema2md -d json/ -v 2020-12` call.

---

## ~~14. Modernize Python environment setup~~ ✓ DONE

Replaced frozen `requirements.txt` (2023-era pinned versions of `attrs`, `jsonschema`, `rpds-py`, etc.) with a `pyproject.toml` declaring loose lower-bound dependencies. Updated `requirements.txt` to use the same lower bounds and point users to `pip install .`. All setup docs (`README.md`, `AGENT.md`, `.github/copilot-instructions.md`) updated accordingly. Removed `Pipfile` and `Pipfile.lock`.

The pinned `rpds-py==0.13.1` (a Rust extension) lacked a prebuilt wheel for Python 3.14, causing a segfault on `import jsonschema`. The new setup lets pip resolve the latest compatible wheel for whatever Python version is in use.

---

## Summary: Recommended Execution Order

1. ~~Fix Makefile PATH (§1)~~ ✓
2. ~~Fix two broken issue examples (§2)~~ ✓
3. ~~Remove backup files (§8)~~ ✓
4. ~~Fix incorrect `$id` values (§4)~~ ✓
5. ~~Add missing `title`/`description` (§5)~~ ✓
6. ~~Migrate all schemas to draft 2020-12 (§3)~~ ✓
7. ~~Fix duplicate Makefile test and example filename typo (§9, §10)~~ ✓
8. ~~Simplify documentation target (§6)~~ ✓
9. ~~Add missing tests (§7)~~ — still pending
10. ~~Rewrite README.md (§11)~~ ✓
11. ~~Update copilot-instructions.md (§12)~~ ✓
12. ~~Modernize Python environment setup (§14)~~ ✓
13. Improve property documentation (§13) — still pending

---

## 13. Improve property documentation

Three classes of problem were found by automated audit:

### A. Placeholder titles (auto-generated "The X Schema" strings — uninformative)

These were originally generated by `jsonschema2md` and were never replaced with real descriptions.

| Schema                                               | Properties                                                                                                                                                   |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `json/linguistic_annotation/ling_spacy.schema.json`  | `ts`, `id`, `sents`, `sents[].sid`, `sents[].lg`, `sents[].tok`, `tok[].t`, `tok[].l`, `tok[].p`, `tok[].o`, `tok[].e`                                       |
| `json/linguistic_annotation/lingproc.v2.schema.json` | `ts`, `model_id`, `lid_path`, `lingproc_git`, `char_count`, `min_chars`, `max_chars`, `title_status`, `$defs/sents[].lg`, `$defs/sents[].tokens[].t/l/p/o/e` |
| `json/topic_model/topic_assignment.v2.schema.json`   | `ts`                                                                                                                                                         |

**Fix:** Replace `"title": "The X Schema"` with a real human-readable title (or remove the `title` if `description` is sufficient), and add a `description` explaining the field's meaning.

### B. Missing descriptions on top-level or structural properties

Properties that have no `description` at all, leaving validators and doc readers with no context.

| Schema                                                             | Properties                                                                                                                                                          |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `json/canonical/issue.schema.json`                                 | `i[].section_title`, `i[].section_title.title_text`, `i[].section_title.composing_ci_ids`, `i[].section_title.section_id`, `i[].section_title.heading_legacy_parts` |
| `json/rebuilt/paper_contentitem.schema.json`                       | `section_title`, `section_title.title_text`, `section_title.composing_ci_ids`, `section_title.section_id`                                                           |
| `json/embeddings/embeddings-chunks.schema.json`                    | `chunks`                                                                                                                                                            |
| `json/embeddings/embeddings-docs.schema.json`                      | `embedding`                                                                                                                                                         |
| `json/embeddings/embeddings-sentence.schema.json`                  | `sents`                                                                                                                                                             |
| `json/image_embeddings/image_embeddings.schema.json`               | `embedding`                                                                                                                                                         |
| `json/language_identification/language_identification.schema.json` | `votes`, `$defs/lidType.lang`, `$defs/lidType.prob`                                                                                                                 |
| `json/linguistic_annotation/lingproc.v2.schema.json`               | `sents`, `tsents`                                                                                                                                                   |
| `json/topic_model/topic_description.schema.json`                   | `lg`, `topic`, `topic_model`, `topic_description`, `meta`, `word_probs`, `$defs/word_prob.word`, `$defs/word_prob.prob`                                             |

**Fix:** Add a `description` string to each listed property explaining its meaning, expected format, and any domain-specific conventions (e.g. which ISO standard for language codes, what coordinate system for offsets).

### C. Opaque single-letter or abbreviated property names

These names are used across multiple schemas but are never explained in the schema itself, making the format opaque to new contributors.

| Short name         | Found in                            | Apparent meaning              |
| ------------------ | ----------------------------------- | ----------------------------- |
| `t`                | `ling_spacy`, `lingproc.v2` (token) | token text                    |
| `l`                | `ling_spacy`, `lingproc.v2` (token) | lemma                         |
| `p`                | `ling_spacy`, `lingproc.v2` (token) | part-of-speech tag            |
| `o`                | `ling_spacy`, `lingproc.v2` (token) | character offset              |
| `e`                | `ling_spacy`, `lingproc.v2` (token) | named entity tag (IOB format) |
| `lg`               | many schemas                        | ISO 639 language code         |
| `ts`               | many schemas                        | ISO 8601 processing timestamp |
| `ft`               | `rebuilt/`, `ling_spacy`            | full text                     |
| `rc`               | `rebuilt/` audio                    | related content               |
| `rr`               | `rebuilt/`                          | regions/references            |
| `ci_id` / `ci_ref` | enrichment schemas                  | content item identifier       |

**Fix:** Each of these properties needs a `description` that spells out the full meaning, e.g.:

```json
"lg": {
  "type": "string",
  "description": "ISO 639-1 language code (e.g. 'de', 'fr'). Use null if the language is unknown."
}
```

Consider also documenting the full vocabulary of abbreviations in a top-level `README` section or a `SCHEMA_CONVENTIONS.md` file for future maintainers.
