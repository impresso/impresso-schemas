## items Type

`object` ([Details](audio_record_contentitem-properties-rreb-items-properties-t-items.md))

# items Properties

| Property  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                              |
| :-------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tc](#tc) | `array`   | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-t-items-properties-tc.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/t/items/properties/tc") |
| [s](#s)   | `integer` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-t-items-properties-s.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/t/items/properties/s")   |
| [l](#l)   | `integer` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-t-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/t/items/properties/l")   |

## tc

Coordinates of audio-segment in the format (start-time, duration), each in seconds.

`tc`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-t-items-properties-tc.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/t/items/properties/tc")

### tc Type

`integer[]`

### tc Constraints

**maximum number of items**: the maximum number of items for this array is: `2`

**minimum number of items**: the minimum number of items for this array is: `2`

## s

offset start (relative to ft field)

`s`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-t-items-properties-s.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/t/items/properties/s")

### s Type

`integer`

## l

token length

`l`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-t-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/t/items/properties/l")

### l Type

`integer`
