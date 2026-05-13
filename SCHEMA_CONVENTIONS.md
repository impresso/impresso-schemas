# Schema Conventions

This document describes the conventions implicit in the Impresso JSON schemas.
It is the authoritative reference for naming, typing, and documenting properties
when writing or reviewing schemas in this repository.

---

## 1. Schema file requirements

Every schema file must include these root-level keywords:

| Keyword       | Requirement                                                                                                                         |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `$schema`     | `"https://json-schema.org/draft/2020-12/schema"` — always HTTPS, no trailing `#`                                                    |
| `$id`         | Canonical URL rooted at `https://impresso.github.io/impresso-schemas/json/<directory>/<filename>` — must match the actual file path |
| `title`       | Short human-readable name (not `"The X Schema"`)                                                                                    |
| `description` | One or two sentences explaining what the document represents                                                                        |
| `type`        | Always `"object"` at the root                                                                                                       |
| `required`    | List all fields that must be present for a document to be valid                                                                     |
| `properties`  | Typed, described definitions for every field                                                                                        |

Every property inside `properties` must have at minimum a `description`.

---

## 2. Property naming conventions

### 2.1 Case and separators

- Use **`snake_case`** for all multi-word property names: `model_id`, `ci_type`, `topic_model_id`.
- Do **not** use camelCase, kebab-case, or PascalCase for property names.

### 2.2 Abbreviations

Short property names are used pervasively in this repository to minimise
document size (schemas are applied to large corpora). The table below is the
**canonical vocabulary**. Use these names consistently; do not invent new
single-letter or two-letter names without updating this table.

| Name      | Full form                    | Type                            | Notes                                                                      |
| --------- | ---------------------------- | ------------------------------- | -------------------------------------------------------------------------- |
| `id`      | identifier                   | `string`                        | Canonical Impresso ID; format depends on entity type (see §4)              |
| `ci_id`   | content item identifier      | `string`                        | Preferred over `ci_ref` in new schemas (see §4.2)                          |
| `ci_ref`  | content item reference       | `string`                        | Legacy alias for `ci_id`; use `ci_id` in new schemas                       |
| `ci_type` | content item type            | `string`                        | Human-readable type string from rebuilt schema (e.g. `"article"`)          |
| `d`       | date                         | `string`                        | ISO 8601 date `YYYY-MM-DD` — publication date of the source document       |
| `e`       | entity tag                   | `string`                        | Named entity label in IOB2 format (e.g. `"B-LOC"`, `"I-PER"`, `"O"`)       |
| `ft`      | full text                    | `string`                        | The rebuilt plain-text content of the content item                         |
| `l`       | lemma                        | `string`                        | Lemma of the token (linguistic annotation schemas)                         |
| `lg`      | language                     | `string` or `["string","null"]` | ISO 639-1 two-letter code (e.g. `"de"`, `"fr"`); `null` if unknown         |
| `o`       | offset                       | `integer`                       | Zero-based character offset in the `ft` field                              |
| `olr`     | optical layout recognition   | `boolean`                       | `true` if OLR was applied to the source document                           |
| `p`       | part-of-speech / probability | `string` or `number`            | POS tag (token schemas) or probability (topic/LID schemas)                 |
| `pp`      | physical pages               | `array` of `integer`            | Physical page numbers spanned by the content item                          |
| `rc`      | radio channel                | `string` or `null`              | Radio channel name; only set when `st == "radio_broadcast"`                |
| `rp`      | radio programme              | `string` or `null`              | Radio programme name; only set when `st == "radio_broadcast"`              |
| `rr`      | regions/records              | `array`                         | Audio record numbers (`rebuilt/audio`) or region list                      |
| `s`       | start offset                 | `integer`                       | Start character offset (relative to `ft`)                                  |
| `sm`      | source medium                | `string`                        | Physical medium: `"print"`, `"typescript"`, or `"audio"`                   |
| `st`      | source type                  | `string`                        | Media type: `"newspaper"`, `"radio_broadcast"`, `"radio_magazine"`, etc.   |
| `t`       | token / topic                | `string` or `string`            | Token surface form (linguistic schemas) or topic ID string (topic schemas) |
| `tp`      | type                         | `string` or `null`              | Content item type; see §4.4 for the controlled vocabulary                  |
| `ts`      | timestamp                    | `string`                        | ISO 8601 datetime of processing: `YYYY-MM-DDTHH:MM:SSZ` (see §3.2)         |

### 2.3 Avoiding new abbreviations

Prefer full descriptive names for new properties unless the field will appear in
every document of a high-volume schema. If a short name is unavoidable, document
it in the table above before merging.

---

## 3. Value conventions

### 3.1 Language codes — `lg`, `lang`, `language`

- Use **ISO 639-1** two-letter codes (e.g. `"de"`, `"fr"`, `"en"`, `"lb"`).
- Schema type: `"string"` with pattern `^[a-z]{2,3}$`, or `["string","null"]` where unknown language is possible.
- Use `null`, not `""` or `"unk"`, when the language is genuinely unknown.
- The legacy field `lang` (present in `topic_assignment.schema.json`) is equivalent to `lg`; prefer `lg` in new schemas.

### 3.2 Timestamps — `ts`, `cdt`, `mft_generation_date`

- Format: **`YYYY-MM-DDTHH:MM:SSZ`** (UTC, Z suffix).
- Regex pattern: `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`
- Always apply this pattern in the schema definition; do not leave `ts` as a bare `"type": "string"`.
- `ts` is the processing timestamp (when the JSON was generated), not the content date.
- `d` or `cdt` carries the publication/creation date of the source document.

### 3.3 Dates — `d`, `cdt`, `min_date`, `max_date`

- Format: **`YYYY-MM-DD`** (ISO 8601 date).
- Regex pattern: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$`

### 3.4 Booleans

Use JSON `true`/`false`, never `"true"`/`"false"` strings or `0`/`1` integers.

### 3.5 Null vs absent

- Use `null` (via `["string","null"]` etc.) when the field is present but the value is unknown or not applicable.
- Omit the field entirely when it is not relevant to the document type.
- Do not use empty string `""`, `"N/A"`, or `"-"` as sentinels.

---

## 4. Identifier formats

All Impresso identifiers follow a hierarchical pattern. The separator is always `-`.

### 4.1 Issue ID

```
<media_alias>-<YYYY>-<MM>-<DD>-<edition>
```

Examples: `GDL-1900-01-02-a`, `SOC_CJ-1940-07-22-b`

Pattern: `^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}$`

### 4.2 Content item ID (`ci_id` / `id` on rebuilt/enrichment schemas)

```
<media_alias>-<YYYY>-<MM>-<DD>-<edition>-i<NNNN>
```

Examples: `GDL-1900-01-02-a-i0001`, `SOC_CJ-1940-07-22-a-i0012`

Pattern: `^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-i[0-9]{4}$`

Use `ci_id` (not `ci_ref`) in all new schemas.

### 4.3 Page ID

```
<media_alias>-<YYYY>-<MM>-<DD>-<edition>-p<NNNN>
```

Pattern: `^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-p[0-9]{4}$`

### 4.4 Audio record ID

```
<media_alias>-<YYYY>-<MM>-<DD>-<edition>-r<NNNN>
```

Pattern: `^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,3}-r[0-9]{4}$`

### 4.5 Text reuse passage ID

```
<cluster_hash>-<media_alias>-<YYYY>-<MM>-<DD>-<edition>-i<NNNN>@<start>:<end>
```

Example: `c68720283542-armeteufel-1904-08-07-a-i0010@8067:8460`

---

## 5. Controlled vocabularies

### 5.1 Content item type — `tp`

| Value                       | Meaning                                |
| --------------------------- | -------------------------------------- |
| `"article"`                 | Newspaper article                      |
| `"ad"`                      | Advertisement                          |
| `"image"`                   | Image region                           |
| `"table"`                   | Table                                  |
| `"death_notice"`            | Death notice / obituary                |
| `"weather"`                 | Weather report                         |
| `"page"`                    | Full-page item (no finer segmentation) |
| `"radio_bulletin"`          | Radio news bulletin                    |
| `"radio_broadcast_episode"` | Full radio broadcast episode           |
| `"chronicle"`               | Chronicle / column                     |
| `"chapter"`                 | Chapter (monograph)                    |
| `"discussion"`              | Discussion / debate transcript         |
| `"entertainment"`           | Entertainment listing                  |
| `null`                      | Type not determined                    |

**Note:** Older schemas use short codes (`"ar"`, `"ad"`) for `tp`. New schemas use the full English string. Document which convention applies in the schema's `description`.

### 5.2 Source type — `st`

| Value               | Meaning                   |
| ------------------- | ------------------------- |
| `"newspaper"`       | Print newspaper           |
| `"radio_broadcast"` | Radio broadcast programme |
| `"radio_magazine"`  | Radio programme guide     |
| `"radio_schedule"`  | Radio schedule document   |
| `"monograph"`       | Book or monograph         |
| `"encyclopedia"`    | Encyclopedia              |

### 5.3 Source medium — `sm`

| Value          | Meaning                         |
| -------------- | ------------------------------- |
| `"print"`      | Scanned print document (OCR)    |
| `"typescript"` | Typescript/typewritten document |
| `"audio"`      | Audio recording (ASR)           |

---

## 6. Schema structure patterns

### 6.1 Shared definitions

Use `$defs` (never `definitions`) for types reused within a single schema.
Reference them with `"$ref": "#/$defs/<name>"`.

Do **not** use cross-file `$ref` references. Each schema must be self-contained.
Shared logical types (e.g. `langISO639Type`, `probType`) are duplicated across
schemas by design — this is acceptable given the small number of schemas.

### 6.2 Arrays of typed objects

For arrays whose items follow a fixed structure, define the item schema inline or
in `$defs`, not as a bare `{}`.

```json
"tokens": {
  "type": "array",
  "description": "List of tokens in the sentence.",
  "items": { "$ref": "#/$defs/token" }
}
```

### 6.3 Tuple arrays

For arrays with positional semantics (e.g. `[start, duration]`), use
`prefixItems` (2020-12 syntax), not `items: [...]` (draft-07 syntax):

```json
"tc": {
  "type": "array",
  "description": "Audio segment coordinates as [start_seconds, duration_seconds].",
  "prefixItems": [
    { "type": "number", "description": "Start time in seconds." },
    { "type": "number", "description": "Duration in seconds." }
  ],
  "maxItems": 2
}
```

### 6.4 Optional nullable fields

When a field may be absent or its value unknown, prefer `["string", "null"]`
over making the field optional with no type:

```json
"lg": {
  "type": ["string", "null"],
  "description": "ISO 639-1 language code, or null if unknown."
}
```

Do **not** include such fields in `required`; omit them from `required` and let
`null` carry the "unknown" meaning when the field is present.

### 6.5 Fragment `$id` values are forbidden

Do not add `"$id"` to properties or `$defs` entries with fragment-only values
(e.g. `"$id": "#/properties/ts"`). This is forbidden in draft 2020-12 and was
a legacy artefact from earlier auto-generation tooling.

---

## 7. Documentation standards for properties

Every property must have a `description`. Good descriptions answer:

1. **What** the field contains (not just its name repeated).
2. **Format** or units (e.g. "seconds", "ISO 639-1", "YYYY-MM-DD").
3. **When** it is present or absent (if conditional).
4. A short **example value** in the `examples` array when the format is non-obvious.

Example of a well-documented property:

```json
"d": {
  "type": "string",
  "description": "Publication date of the issue or broadcast in YYYY-MM-DD format.",
  "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
  "examples": ["1940-07-22"]
}
```

Do **not** use placeholder titles such as `"The Ts Schema"` — these are
auto-generation artefacts and carry no information. Either write a real `title`
or omit the `title` keyword.

---

## 8. Adding a new schema — checklist

1. File path: `json/<category>/<name>.schema.json`
2. Root keywords: `$schema`, `$id`, `title`, `description`, `type`, `required`, `properties`
3. `$id` matches the file path under `https://impresso.github.io/impresso-schemas/`
4. All property names follow §2; any new abbreviations added to §2.2 table
5. All shared field names (`ts`, `lg`, `ci_id`, …) use the canonical types and patterns from §3–§5
6. No fragment `$id` on sub-properties (§6.5)
7. No `definitions` key — use `$defs`
8. Example file added under `examples/<category>/`
9. Test case added to `tests/test_schema_examples.py` `CASES` list
10. `make tests` passes
11. `make documentation` regenerates `docs/` without errors
