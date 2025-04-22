## items Type

`object` ([Details](audio_record-properties-s-items.md))

# items Properties

| Property    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                 |
| :---------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tc](#tc)   | `array`  | Required | cannot be null | [Audio Record](audio_record-properties-s-items-properties-tc.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/tc")   |
| [u](#u)     | `array`  | Required | cannot be null | [Audio Record](audio_record-properties-s-items-properties-u.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u")     |
| [pOf](#pof) | `string` | Optional | cannot be null | [Audio Record](audio_record-properties-s-items-properties-pof.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/pOf") |

## tc

Coordinates of audio-segment in the format (start-time, duration), each in seconds.

`tc`

*   is required

*   Type: `integer[]`

*   cannot be null

*   defined in: [Audio Record](audio_record-properties-s-items-properties-tc.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/tc")

### tc Type

`integer[]`

### tc Constraints

**maximum number of items**: the maximum number of items for this array is: `2`

**minimum number of items**: the minimum number of items for this array is: `2`

## u

Speech utterances (consecutive same-speaker speech segments).

`u`

*   is required

*   Type: `object[]` ([Details](audio_record-properties-s-items-properties-u-items.md))

*   cannot be null

*   defined in: [Audio Record](audio_record-properties-s-items-properties-u.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/u")

### u Type

`object[]` ([Details](audio_record-properties-s-items-properties-u-items.md))

## pOf

The canonical ID of the content item to which the utterance belongs.

`pOf`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record](audio_record-properties-s-items-properties-pof.md "https://impresso.github.io/impresso-schemas/json/canonical/audio_record.schema.json#/properties/s/items/properties/pOf")

### pOf Type

`string`
