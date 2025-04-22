## Named Entity JSON Schema Type

`object` ([Named Entity JSON Schema](entities.md))

# Named Entity JSON Schema Properties

| Property               | Type     | Required | Nullable       | Defined by                                                                                                                                               |
| :--------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ci\_id](#ci_id)       | `string` | Required | cannot be null | [Named Entity JSON Schema](entities-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/ci_id")       |
| [ci\_type](#ci_type)   | `string` | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-ci_type.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/ci_type")   |
| [ts](#ts)              | `string` | Required | cannot be null | [Named Entity JSON Schema](entities-properties-ts.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/ts")             |
| [model\_id](#model_id) | `string` | Required | cannot be null | [Named Entity JSON Schema](entities-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/model_id") |
| [nes](#nes)            | `array`  | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes")           |

## ci\_id

Impresso content item ID.

`ci_id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/ci_id")

### ci\_id Type

`string`

## ci\_type

Impresso content item type.

`ci_type`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-ci_type.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/ci_type")

### ci\_type Type

`string`

## ts

Timestamp of creation of the JSON file (e.g. '2024-05-26T09:48:01Z').

`ts`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-ts.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/ts")

### ts Type

`string`

## model\_id

An alias for the system or model that produced this output, used for transparency and traceability. It should include distinguishing elements like a base name, version, and language.

`model_id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/model_id")

### model\_id Type

`string`

## nes

The list of named entity mentions identified in the document.

`nes`

*   is required

*   Type: `object[]` ([Details](entities-properties-nes-items.md))

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes")

### nes Type

`object[]` ([Details](entities-properties-nes-items.md))

### nes Constraints

**minimum number of items**: the minimum number of items for this array is: `0`
