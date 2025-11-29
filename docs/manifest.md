## Versioning Manifest Type

`object` ([Versioning Manifest](manifest.md))

# Versioning Manifest Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                           |
| :-------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [mft\_version](#mft_version)                  | `string` | Required | cannot be null | [Versioning Manifest](manifest-properties-mft_version.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/mft_version")                 |
| [mft\_generation\_date](#mft_generation_date) | `string` | Required | cannot be null | [Versioning Manifest](manifest-properties-mft_generation_date.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/mft_generation_date") |
| [mft\_s3\_path](#mft_s3_path)                 | `string` | Required | cannot be null | [Versioning Manifest](manifest-properties-mft_s3_path.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/mft_s3_path")                 |
| [input\_mft\_s3\_path](#input_mft_s3_path)    | `string` | Optional | can be null    | [Versioning Manifest](manifest-properties-input_mft_s3_path.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/input_mft_s3_path")     |
| [input\_mft\_git\_path](#input_mft_git_path)  | `string` | Required | can be null    | [Versioning Manifest](manifest-properties-input_mft_git_path.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/input_mft_git_path")   |
| [code\_git\_commit](#code_git_commit)         | `string` | Required | can be null    | [Versioning Manifest](manifest-properties-code_git_commit.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/code_git_commit")         |
| [media\_list](#media_list)                    | `array`  | Required | cannot be null | [Versioning Manifest](manifest-properties-media_list.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list")                   |
| [overall\_statistics](#overall_statistics)    | `array`  | Optional | cannot be null | [Versioning Manifest](manifest-properties-overall_statistics.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/overall_statistics")   |
| [notes](#notes)                               | `string` | Optional | cannot be null | [Versioning Manifest](manifest-properties-notes.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/notes")                             |

## mft\_version

Version of the manifest in format 'vM.m.p'.

`mft_version`

* is required

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-properties-mft_version.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/mft_version")

### mft\_version Type

`string`

### mft\_version Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^v([0-9]+[.]){2}[0-9]+$
```

[try pattern](https://regexr.com/?expression=%5Ev\(%5B0-9%5D%2B%5B.%5D\)%7B2%7D%5B0-9%5D%2B%24 "try regular expression with regexr.com")

## mft\_generation\_date

Creation date timestamp of this manifest.

`mft_generation_date`

* is required

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-properties-mft_generation_date.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/mft_generation_date")

### mft\_generation\_date Type

`string`

## mft\_s3\_path

S3 path to this manifest ('s3://\[stage bucket]/\[partition]/\[stage]\_vM-m-p.json').

`mft_s3_path`

* is required

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-properties-mft_s3_path.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/mft_s3_path")

### mft\_s3\_path Type

`string`

## input\_mft\_s3\_path

S3 path to manifest of the input data used for processing.

`input_mft_s3_path`

* is optional

* Type: `string`

* can be null

* defined in: [Versioning Manifest](manifest-properties-input_mft_s3_path.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/input_mft_s3_path")

### input\_mft\_s3\_path Type

`string`

## input\_mft\_git\_path

Path within impresso-data-release Git repo to manifest of input data used for processing.

`input_mft_git_path`

* is required

* Type: `string`

* can be null

* defined in: [Versioning Manifest](manifest-properties-input_mft_git_path.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/input_mft_git_path")

### input\_mft\_git\_path Type

`string`

## code\_git\_commit

Link to git commit of the code used to generate/modify the output data.

`code_git_commit`

* is required

* Type: `string`

* can be null

* defined in: [Versioning Manifest](manifest-properties-code_git_commit.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/code_git_commit")

### code\_git\_commit Type

`string`

## media\_list

List of all media collections (metadata and statistics) present in the s3 bucket versioned by this manifest.

`media_list`

* is required

* Type: `object[]` ([Details](manifest-properties-media_list-items.md))

* cannot be null

* defined in: [Versioning Manifest](manifest-properties-media_list.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list")

### media\_list Type

`object[]` ([Details](manifest-properties-media_list-items.md))

## overall\_statistics

List of statistics describing the contents of the data at the corpus level, for current format, as well as all previous upstream formats.

`overall_statistics`

* is optional

* Type: `object[]` ([Details](manifest-properties-overall_statistics-items.md))

* cannot be null

* defined in: [Versioning Manifest](manifest-properties-overall_statistics.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/overall_statistics")

### overall\_statistics Type

`object[]` ([Details](manifest-properties-overall_statistics-items.md))

### overall\_statistics Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## notes

Free text notes for any relevant information about processing.

`notes`

* is optional

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-properties-notes.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/notes")

### notes Type

`string`

# Versioning Manifest Definitions

## Definitions group media\_statistics

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics"}
```

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                           |
| :-------------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [stage](#stage)                                     | `string` | Required | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-stage.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/stage")                                   |
| [granularity](#granularity)                         | `string` | Required | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/granularity")                       |
| [element](#element)                                 | `string` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-element.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/element")                               |
| [last\_modification\_date](#last_modification_date) | `string` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-last_modification_date.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/last_modification_date") |
| [media\_stats](#media_stats)                        | `object` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-media_stats.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/media_stats")                       |
| [nps\_stats](#nps_stats)                            | `object` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats")                           |

### stage

Stage of the data for which the statistics were computed.

`stage`

* is required

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-stage.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/stage")

#### stage Type

`string`

### granularity

Granularity level according to which the statistics were computed.

`granularity`

* is required

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/granularity")

#### granularity Type

`string`

#### granularity Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"corpus"` |             |
| `"title"`  |             |
| `"year"`   |             |

### element

Element of the data on which they were computed, based on the granularity (title-year pairs in the case of 'year').

`element`

* is optional

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-element.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/element")

#### element Type

`string`

### last\_modification\_date

Date timestamp of last modification of the media statistics for this specific element.

`last_modification_date`

* is optional

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-last_modification_date.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/last_modification_date")

#### last\_modification\_date Type

`string`

### media\_stats

Counts of various elements/enrichments in the data corresponding to above granularity and element. The exact keys used depend on the data stage and source type.

`media_stats`

* is optional

* Type: `object` ([Details](manifest-definitions-media_statistics-properties-media_stats.md))

* cannot be null

* defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-media_stats.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/media_stats")

#### media\_stats Type

`object` ([Details](manifest-definitions-media_statistics-properties-media_stats.md))

### nps\_stats

Counts of various elements/enrichments in newspaper data. Deprecated.

`nps_stats`

* is optional

* Type: `object` ([Details](manifest-definitions-media_statistics-properties-nps_stats.md))

* cannot be null

* defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats")

#### nps\_stats Type

`object` ([Details](manifest-definitions-media_statistics-properties-nps_stats.md))

## Definitions group commit\_link

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/commit_link"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
