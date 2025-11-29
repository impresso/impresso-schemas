## Untitled object in undefined Type

`object` ([Details](embeddings-sentence.md))

# Untitled object in undefined Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ts](#ts)                        | `string` | Required | cannot be null | [Untitled schema](embeddings-sentence-properties-timestamp.md "#/properties/ts#/properties/ts")                                                                                                         |
| [ci\_id](#ci_id)                 | `string` | Required | cannot be null | [Untitled schema](embeddings-sentence-properties-content-item-id.md "#/properties/ci_id#/properties/ci_id")                                                                                             |
| [sents](#sents)                  | `array`  | Required | cannot be null | [Untitled schema](embeddings-sentence-properties-sentence-embeddings.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/properties/sents")                |
| [model\_id](#model_id)           | `string` | Optional | cannot be null | [Untitled schema](embeddings-sentence-properties-model-id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/properties/model_id")                        |
| [lingproc\_path](#lingproc_path) | `string` | Optional | cannot be null | [Untitled schema](embeddings-sentence-properties-linguistic-processing-path.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/properties/lingproc_path") |
| [git](#git)                      | `string` | Optional | cannot be null | [Untitled schema](embeddings-sentence-properties-git-commit.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/properties/git")                           |

## ts

Timestamp of when the embeddings were generated.

`ts`

* is required

* Type: `string` ([Timestamp](embeddings-sentence-properties-timestamp.md))

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-properties-timestamp.md "#/properties/ts#/properties/ts")

### ts Type

`string` ([Timestamp](embeddings-sentence-properties-timestamp.md))

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

Canonical impresso ID of the content item.

`ci_id`

* is required

* Type: `string` ([Content Item ID](embeddings-sentence-properties-content-item-id.md))

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-properties-content-item-id.md "#/properties/ci_id#/properties/ci_id")

### ci\_id Type

`string` ([Content Item ID](embeddings-sentence-properties-content-item-id.md))

### ci\_id Examples

```json
"onsjongen-1951-03-01-a-i0012"
```

## sents

Container for sentence-level embeddings derived from lingproc sentence segmentation

`sents`

* is required

* Type: `object[]` ([Sentence Embedding](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding.md))

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-properties-sentence-embeddings.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/properties/sents")

### sents Type

`object[]` ([Sentence Embedding](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding.md))

## model\_id

Model identifier according to impresso model description schema.

`model_id`

* is optional

* Type: `string` ([Model ID](embeddings-sentence-properties-model-id.md))

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-properties-model-id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/properties/model_id")

### model\_id Type

`string` ([Model ID](embeddings-sentence-properties-model-id.md))

### model\_id Examples

```json
"gte-multilingual-base_v1.0.0"
```

## lingproc\_path

S3 path to the lingproc output from which sentence boundaries were derived.

`lingproc_path`

* is optional

* Type: `string` ([Linguistic Processing Path](embeddings-sentence-properties-linguistic-processing-path.md))

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-properties-linguistic-processing-path.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/properties/lingproc_path")

### lingproc\_path Type

`string` ([Linguistic Processing Path](embeddings-sentence-properties-linguistic-processing-path.md))

### lingproc\_path Examples

```json
"s3://142-processed-data-final/embeddings/sentences/embeddings_gte_v1-0-0/onsjongen/onsjongen-1951-sentence-embeddings.jsonl.bz2"
```

## git

Git commit or tag of the processing pipeline used to generate the embeddings.

`git`

* is optional

* Type: `string` ([Git Commit](embeddings-sentence-properties-git-commit.md))

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-properties-git-commit.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/properties/git")

### git Type

`string` ([Git Commit](embeddings-sentence-properties-git-commit.md))

### git Examples

```json
"01fef5"
```

# Untitled object in undefined Definitions

## Definitions group sents

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
