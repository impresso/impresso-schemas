## media\_statistics Type

`object` ([Details](manifest-definitions-media_statistics.md))

any of

*   [Untitled undefined type in Versioning Manifest](manifest-definitions-media_statistics-anyof-0.md "check type definition")

*   [Untitled undefined type in Versioning Manifest](manifest-definitions-media_statistics-anyof-1.md "check type definition")

# media\_statistics Properties

| Property                     | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                     |
| :--------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [stage](#stage)              | `string` | Required | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-stage.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/stage")             |
| [granularity](#granularity)  | `string` | Required | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/granularity") |
| [element](#element)          | `string` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-element.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/element")         |
| [nps\_stats](#nps_stats)     | `object` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats")     |
| [radio\_stats](#radio_stats) | `object` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-radio_stats.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/radio_stats") |

## stage

Stage of the data for which the statistics were computed.

`stage`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-stage.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/stage")

### stage Type

`string`

## granularity

Granularity level according to which the statistics were computed.

`granularity`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/granularity")

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

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-element.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/element")

### element Type

`string`

## nps\_stats

Counts of various elements/enrichments in newspaper data corresponding to above granularity and element. The exact keys used depend on the data stage.

`nps_stats`

*   is optional

*   Type: `object` ([Details](manifest-definitions-media_statistics-properties-nps_stats.md))

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats")

### nps\_stats Type

`object` ([Details](manifest-definitions-media_statistics-properties-nps_stats.md))

## radio\_stats

Counts of various elements/enrichments in radio data corresponding to above granularity and element. The exact keys used depend on the data stage.

`radio_stats`

*   is optional

*   Type: `object` ([Details](manifest-definitions-media_statistics-properties-radio_stats.md))

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-radio_stats.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/radio_stats")

### radio\_stats Type

`object` ([Details](manifest-definitions-media_statistics-properties-radio_stats.md))
