## items Type

`object` ([Details](audio_record-properties-s-items-properties-u-items.md))

# items Properties

| Property            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                               |
| :------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tc](#tc)           | `array`  | Required | cannot be null | [Audio Record](audio_record-defs-time_coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/tc")                                         |
| [speaker](#speaker) | `string` | Optional | cannot be null | [Audio Record](audio_record-properties-s-items-properties-u-items-properties-speaker.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/speaker") |
| [ss](#ss)           | `array`  | Required | cannot be null | [Audio Record](audio_record-properties-s-items-properties-u-items-properties-ss.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss")           |

## tc

Coordinates of audio-segment in the format (start-time, duration), each in seconds.

`tc`

*   is required

*   Type: `number[]`

*   cannot be null

*   defined in: [Audio Record](audio_record-defs-time_coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/tc")

### tc Type

`number[]`

### tc Constraints

**maximum number of items**: the maximum number of items for this array is: `2`

**minimum number of items**: the minimum number of items for this array is: `2`

## speaker

Speaker id or name for this utterance.

`speaker`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record](audio_record-properties-s-items-properties-u-items-properties-speaker.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/speaker")

### speaker Type

`string`

## ss

list of speech segments.

`ss`

*   is required

*   Type: `object[]` ([Details](audio_record-properties-s-items-properties-u-items-properties-ss-items.md))

*   cannot be null

*   defined in: [Audio Record](audio_record-properties-s-items-properties-u-items-properties-ss.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u/items/properties/ss")

### ss Type

`object[]` ([Details](audio_record-properties-s-items-properties-u-items-properties-ss-items.md))
