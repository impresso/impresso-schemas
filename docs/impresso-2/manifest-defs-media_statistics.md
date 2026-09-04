## media\_statistics Type

`object` ([Details](manifest-defs-media_statistics.md))

any of

* [Untitled undefined type in Versioning Manifest](manifest-defs-media_statistics-anyof-0.md "check type definition")

* [Untitled undefined type in Versioning Manifest](manifest-defs-media_statistics-anyof-1.md "check type definition")

# media\_statistics Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                             |
| :-------------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [stage](#stage)                                     | `string` | Required | cannot be null | [Versioning Manifest](manifest-defs-media_statistics-properties-data-processing-stage-scalar.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/data-stage.v1.schema.json#/$defs/media_statistics/properties/stage")                               |
| [granularity](#granularity)                         | `string` | Required | cannot be null | [Versioning Manifest](manifest-defs-media_statistics-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/granularity")                       |
| [element](#element)                                 | `string` | Optional | cannot be null | [Versioning Manifest](manifest-defs-media_statistics-properties-element.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/element")                               |
| [last\_modification\_date](#last_modification_date) | `string` | Optional | cannot be null | [Versioning Manifest](manifest-defs-media_statistics-properties-last_modification_date.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/last_modification_date") |
| [media\_stats](#media_stats)                        | `object` | Optional | cannot be null | [Versioning Manifest](manifest-defs-media_statistics-properties-media_stats.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/media_stats")                       |
| [nps\_stats](#nps_stats)                            | `object` | Optional | cannot be null | [Versioning Manifest](manifest-defs-media_statistics-properties-nps_stats.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/nps_stats")                           |

## stage

Identifier of an Impresso pipeline stage that produces or consumes a versioned data release, matching `impresso_essentials.utils.DataStage`.

`stage`

* is required

* Type: `string` ([Data-processing stage scalar](manifest-defs-media_statistics-properties-data-processing-stage-scalar.md))

* cannot be null

* defined in: [Versioning Manifest](manifest-defs-media_statistics-properties-data-processing-stage-scalar.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/data-stage.v1.schema.json#/$defs/media_statistics/properties/stage")

### stage Type

`string` ([Data-processing stage scalar](manifest-defs-media_statistics-properties-data-processing-stage-scalar.md))

### stage Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                      | Explanation |
| :------------------------- | :---------- |
| `"canonical"`              |             |
| `"canonical-consolidated"` |             |
| `"rebuilt"`                |             |
| `"passim"`                 |             |
| `"emb-words"`              |             |
| `"emb-sents"`              |             |
| `"emb-docs"`               |             |
| `"emb-entities"`           |             |
| `"emb-paragraphs"`         |             |
| `"emb-images"`             |             |
| `"classif-images"`         |             |
| `"entities"`               |             |
| `"newsagencies"`           |             |
| `"langident"`              |             |
| `"lingproc"`               |             |
| `"ocrqa"`                  |             |
| `"langid-ocrqa"`           |             |
| `"textreuse"`              |             |
| `"topics"`                 |             |
| `"solr-text-ingestion"`    |             |
| `"mysql-ingestion"`        |             |

### stage Examples

```json
"canonical"
```

```json
"rebuilt"
```

```json
"langident"
```

## granularity

Granularity level according to which the statistics were computed.

`granularity`

* is required

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-defs-media_statistics-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/granularity")

### granularity Type

`string`

### granularity Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"corpus"` |             |
| `"title"`  |             |
| `"year"`   |             |

## element

Element of the data on which they were computed, based on the granularity (title-year pairs in the case of 'year').

`element`

* is optional

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-defs-media_statistics-properties-element.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/element")

### element Type

`string`

## last\_modification\_date

Date timestamp of last modification of the media statistics for this specific element.

`last_modification_date`

* is optional

* Type: `string`

* cannot be null

* defined in: [Versioning Manifest](manifest-defs-media_statistics-properties-last_modification_date.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/last_modification_date")

### last\_modification\_date Type

`string`

## media\_stats

Counts of various elements/enrichments in the data corresponding to above granularity and element. The exact keys used depend on the data stage and source type.

`media_stats`

* is optional

* Type: `object` ([Details](manifest-defs-media_statistics-properties-media_stats.md))

* cannot be null

* defined in: [Versioning Manifest](manifest-defs-media_statistics-properties-media_stats.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/media_stats")

### media\_stats Type

`object` ([Details](manifest-defs-media_statistics-properties-media_stats.md))

## nps\_stats

Counts of various elements/enrichments in newspaper data. Deprecated.

`nps_stats`

* is optional

* Type: `object` ([Details](manifest-defs-media_statistics-properties-nps_stats.md))

* cannot be null

* defined in: [Versioning Manifest](manifest-defs-media_statistics-properties-nps_stats.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/versioning/manifest.v1.schema.json#/$defs/media_statistics/properties/nps_stats")

### nps\_stats Type

`object` ([Details](manifest-defs-media_statistics-properties-nps_stats.md))
