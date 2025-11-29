## items Type

`object` ([Details](audio_record-properties-s-items-properties-u-items-properties-ss-items-properties-t-items.md))

# items Properties

| Property  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                   |
| :-------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tc](#tc) | `array`  | Required | cannot be null | [Audio Record](audio_record-defs-time_coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/t/items/properties/tc")                                                                      |
| [tx](#tx) | `string` | Required | cannot be null | [Audio Record](audio_record-properties-s-items-properties-u-items-properties-ss-items-properties-t-items-properties-tx.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/t/items/properties/tx") |

## tc

Coordinates of audio-segment in the format (start-time, duration), each in seconds.

`tc`

* is required

* Type: `number[]`

* cannot be null

* defined in: [Audio Record](audio_record-defs-time_coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/t/items/properties/tc")

### tc Type

`number[]`

### tc Constraints

**maximum number of items**: the maximum number of items for this array is: `2`

**minimum number of items**: the minimum number of items for this array is: `2`

## tx

Token surface form.

`tx`

* is required

* Type: `string`

* cannot be null

* defined in: [Audio Record](audio_record-properties-s-items-properties-u-items-properties-ss-items-properties-t-items-properties-tx.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/t/items/properties/tx")

### tx Type

`string`
