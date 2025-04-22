## items Type

`object` ([Details](audio_record-properties-s-items-properties-u-items-properties-ss-items.md))

# items Properties

| Property  | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                           |
| :-------- | :------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tc](#tc) | `array` | Required | cannot be null | [Audio Record](audio_record-defs-time_coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/tc")                                                 |
| [t](#t)   | `array` | Required | cannot be null | [Audio Record](audio_record-properties-s-items-properties-u-items-properties-ss-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/t") |

## tc

Coordinates of audio-segment in the format (start-time, duration), each in seconds.

`tc`

*   is required

*   Type: `integer[]`

*   cannot be null

*   defined in: [Audio Record](audio_record-defs-time_coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/tc")

### tc Type

`integer[]`

### tc Constraints

**maximum number of items**: the maximum number of items for this array is: `2`

**minimum number of items**: the minimum number of items for this array is: `2`

## t

Speech tokens (as detected by the ASR engine).

`t`

*   is required

*   Type: `object[]` ([Details](audio_record-properties-s-items-properties-u-items-properties-ss-items-properties-t-items.md))

*   cannot be null

*   defined in: [Audio Record](audio_record-properties-s-items-properties-u-items-properties-ss-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/t")

### t Type

`object[]` ([Details](audio_record-properties-s-items-properties-u-items-properties-ss-items-properties-t-items.md))
