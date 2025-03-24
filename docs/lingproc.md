# Untitled object in undefined Schema

```txt
https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json
```

Schema for validation of linguistic annotation as produced by spacy for newspaper data

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | Yes        | Unknown status | No           | Forbidden         | Allowed               | none                | [lingproc.v2.schema.json](../out/lingproc.v2.schema.json "open original schema") |

## Untitled object in undefined Type

`object` ([Details](lingproc.md))

# Untitled object in undefined Properties

| Property                       | Type      | Required | Nullable       | Defined by                                                                                                                                                                     |
| :----------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ts](#ts)                      | `string`  | Required | cannot be null | [Untitled schema](lingproc-properties-the-ts-schema.md "#/properties/ts#/properties/ts")                                                                                       |
| [ci\_id](#ci_id)               | `string`  | Required | cannot be null | [Untitled schema](lingproc-properties-the-content-item-id.md "#/properties/ci_id#/properties/ci_id")                                                                           |
| [sents](#sents)                | `array`   | Required | cannot be null | [Untitled schema](lingproc-properties-the-sents-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/sents")               |
| [tsents](#tsents)              | `array`   | Required | cannot be null | [Untitled schema](lingproc-properties-the-sents-schema-1.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/tsents")            |
| [model\_id](#model_id)         | `string`  | Optional | cannot be null | [Untitled schema](lingproc-properties-the-model-id-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/model_id")         |
| [lid\_path](#lid_path)         | `string`  | Optional | cannot be null | [Untitled schema](lingproc-properties-the-lid-path-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/lid_path")         |
| [lingproc\_git](#lingproc_git) | `string`  | Optional | cannot be null | [Untitled schema](lingproc-properties-the-lingproc-git-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/lingproc_git") |
| [char\_count](#char_count)     | `integer` | Required | cannot be null | [Untitled schema](lingproc-properties-the-char-count-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/char_count")     |
| [min\_chars](#min_chars)       | `integer` | Required | cannot be null | [Untitled schema](lingproc-properties-the-min-chars-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/min_chars")       |
| [max\_chars](#max_chars)       | `integer` | Required | cannot be null | [Untitled schema](lingproc-properties-the-max-chars-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/max_chars")       |
| [title\_status](#title_status) | `object`  | Optional | cannot be null | [Untitled schema](lingproc-properties-the-title-status-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status") |

## ts

timestamp

`ts`

*   is required

*   Type: `string` ([The Ts Schema](lingproc-properties-the-ts-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-ts-schema.md "#/properties/ts#/properties/ts")

### ts Type

`string` ([The Ts Schema](lingproc-properties-the-ts-schema.md))

### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

### ts Examples

```json
"2024-12-27T16:38:46Z"
```

## ci\_id

Canonical impresso id of content item

`ci_id`

*   is required

*   Type: `string` ([The content item id](lingproc-properties-the-content-item-id.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-content-item-id.md "#/properties/ci_id#/properties/ci_id")

### ci\_id Type

`string` ([The content item id](lingproc-properties-the-content-item-id.md))

### ci\_id Examples

```json
"onsjongen-1951-03-01-a-i0012"
```

## sents

container for sentences (boundaries produced by spacy)

`sents`

*   is required

*   Type: `object[]` ([The Items Schema](lingproc-definitions-the-sents-schema-the-items-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-sents-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/sents")

### sents Type

`object[]` ([The Items Schema](lingproc-definitions-the-sents-schema-the-items-schema.md))

## tsents

container for sentences (boundaries produced by spacy)

`tsents`

*   is required

*   Type: `object[]` ([The Items Schema](lingproc-definitions-the-sents-schema-the-items-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-sents-schema-1.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/tsents")

### tsents Type

`object[]` ([The Items Schema](lingproc-definitions-the-sents-schema-the-items-schema.md))

## model\_id

Model identifier according to impresso model description schema

`model_id`

*   is optional

*   Type: `string` ([The Model Id Schema](lingproc-properties-the-model-id-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-model-id-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/model_id")

### model\_id Type

`string` ([The Model Id Schema](lingproc-properties-the-model-id-schema.md))

### model\_id Examples

```json
"spacy@3.6.1:de_core_news_md@3.6.0:sentencizer|tok2vec|tagger|morphologizer|lemmatizer|attribute_ruler|ner"
```

## lid\_path

Path to language identification data

`lid_path`

*   is optional

*   Type: `string` ([The Lid Path Schema](lingproc-properties-the-lid-path-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-lid-path-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/lid_path")

### lid\_path Type

`string` ([The Lid Path Schema](lingproc-properties-the-lid-path-schema.md))

### lid\_path Examples

```json
"s3://42-processed-data-final/langident/langident_v1-4-4/onsjongen/onsjongen-1951.jsonl.bz2"
```

## lingproc\_git

Git commit describe of the linguistic processing pipeline

`lingproc_git`

*   is optional

*   Type: `string` ([The Lingproc Git Schema](lingproc-properties-the-lingproc-git-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-lingproc-git-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/lingproc_git")

### lingproc\_git Type

`string` ([The Lingproc Git Schema](lingproc-properties-the-lingproc-git-schema.md))

### lingproc\_git Examples

```json
"unknown"
```

## char\_count

Character count of the concatenated title and full text

`char_count`

*   is required

*   Type: `integer` ([The Char Count Schema](lingproc-properties-the-char-count-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-char-count-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/char_count")

### char\_count Type

`integer` ([The Char Count Schema](lingproc-properties-the-char-count-schema.md))

### char\_count Examples

```json
65
```

## min\_chars

Minimum number of characters for a valid content item (including title and full text)

`min_chars`

*   is required

*   Type: `integer` ([The Min Chars Schema](lingproc-properties-the-min-chars-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-min-chars-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/min_chars")

### min\_chars Type

`integer` ([The Min Chars Schema](lingproc-properties-the-min-chars-schema.md))

### min\_chars Examples

```json
50
```

## max\_chars

Maximum number of characters for a valid content item (including title and full text)

`max_chars`

*   is required

*   Type: `integer` ([The Max Chars Schema](lingproc-properties-the-max-chars-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-max-chars-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/max_chars")

### max\_chars Type

`integer` ([The Max Chars Schema](lingproc-properties-the-max-chars-schema.md))

### max\_chars Examples

```json
50000
```

## title\_status

Status of the title with respect to full text content based on various criteria

`title_status`

*   is optional

*   Type: `object` ([The Title Status Schema](lingproc-properties-the-title-status-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-properties-the-title-status-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status")

### title\_status Type

`object` ([The Title Status Schema](lingproc-properties-the-title-status-schema.md))

# Untitled object in undefined Definitions

## Definitions group sents

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/definitions/sents"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
