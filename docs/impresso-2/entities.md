## Named Entity JSON Schema Type

`object` ([Named Entity JSON Schema](entities.md))

all of

* [Impresso ci_id property](ocr-qa-allof-impresso-ci_id-property.md "check type definition")

* [Model identifier property](lingproc-allof-model-identifier-property.md "check type definition")

# Named Entity JSON Schema Properties

| Property             | Type     | Required | Nullable       | Defined by                                                                                                                                                                                        |
| :------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ci\_type](#ci_type) | `string` | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-ci_type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json#/properties/ci_type") |
| [ts](#ts)            | `string` | Required | cannot be null | [Named Entity JSON Schema](entities-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json#/properties/ts")           |
| [nes](#nes)          | `array`  | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json#/properties/nes")         |
| [tnes](#tnes)        | `array`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-tnes.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json#/properties/tnes")       |

## ci\_type

Impresso content item type.

`ci_type`

* is optional

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-ci_type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json#/properties/ci_type")

### ci\_type Type

`string`

## ts

Timestamp of creation of the JSON file (e.g. '2024-05-26T09:48:01Z').

`ts`

* is required

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json#/properties/ts")

### ts Type

`string`

## nes

A list of entities.

`nes`

* is required

* Type: `object[]` ([Details](entities-defs-namedentitylist-items.md))

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json#/properties/nes")

### nes Type

`object[]` ([Details](entities-defs-namedentitylist-items.md))

### nes Constraints

**minimum number of items**: the minimum number of items for this array is: `0`

## tnes

A list of entities.

`tnes`

* is optional

* Type: `object[]` ([Details](entities-defs-namedentitylist-items.md))

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-tnes.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json#/properties/tnes")

### tnes Type

`object[]` ([Details](entities-defs-namedentitylist-items.md))

### tnes Constraints

**minimum number of items**: the minimum number of items for this array is: `0`

# Named Entity JSON Schema Definitions

## Definitions group namedEntityList

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/entities/entities.v1.schema.json#/$defs/namedEntityList"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
