## Named Entity JSON Schema Type

`object` ([Named Entity JSON Schema](entities-backup.md))

# Named Entity JSON Schema Properties

| Property           | Type     | Required | Nullable       | Defined by                                                                                                                                                  |
| :----------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)          | `string` | Required | cannot be null | [Named Entity JSON Schema](entities-backup-properties-id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/id")         |
| [ts](#ts)          | `string` | Required | cannot be null | [Named Entity JSON Schema](entities-backup-properties-ts.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/ts")         |
| [sys\_id](#sys_id) | `string` | Required | cannot be null | [Named Entity JSON Schema](entities-backup-properties-sys_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/sys_id") |
| [nes](#nes)        | `array`  | Required | cannot be null | [Named Entity JSON Schema](entities-backup-properties-nes.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes")       |

## id

impresso content item id.

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-backup-properties-id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/id")

### id Type

`string`

## ts

Timestamp of creation of the JSON file (e.g. '2018-09-18T08:00:08Z')

`ts`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-backup-properties-ts.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/ts")

### ts Type

`string`

## sys\_id

An alias for the system or model that produced this output (preferably short, but still understandable), used for transparency and traceability. Should be unique and thus include elements that distinguish one model from another, such as a base name, a version, the language, e.g. bert-xxxx-xxxx-fr.

`sys_id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-backup-properties-sys_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/sys_id")

### sys\_id Type

`string`

## nes

The list of named entity mentions identified in the document

`nes`

*   is required

*   Type: `object[]` ([Details](entities-backup-properties-nes-items.md))

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-backup-properties-nes.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes")

### nes Type

`object[]` ([Details](entities-backup-properties-nes-items.md))

### nes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
