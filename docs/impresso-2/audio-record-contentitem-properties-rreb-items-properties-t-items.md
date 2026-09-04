## items Type

`object` ([Details](audio-record-contentitem-properties-rreb-items-properties-t-items.md))

# items Properties

| Property  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                           |
| :-------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tc](#tc) | `array`   | Optional | cannot be null | [Audio Record Content Item](audio-record-contentitem-properties-rreb-items-properties-s-time-coordinates-scalar.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/time-coordinates.v1.schema.json#/properties/rreb/items/properties/t/items/properties/tc")                     |
| [s](#s)   | `integer` | Optional | cannot be null | [Audio Record Content Item](audio-record-contentitem-properties-rreb-items-properties-t-items-properties-s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json#/properties/rreb/items/properties/t/items/properties/s") |
| [l](#l)   | `integer` | Optional | cannot be null | [Audio Record Content Item](audio-record-contentitem-properties-rreb-items-properties-t-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json#/properties/rreb/items/properties/t/items/properties/l") |

## tc

Temporal span within an audio recording, in the format \[start-time, duration], each expressed in seconds.

`tc`

* is optional

* Type: `array` ([Time-coordinates scalar](audio-record-contentitem-properties-rreb-items-properties-s-time-coordinates-scalar.md))

* cannot be null

* defined in: [Audio Record Content Item](audio-record-contentitem-properties-rreb-items-properties-s-time-coordinates-scalar.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/time-coordinates.v1.schema.json#/properties/rreb/items/properties/t/items/properties/tc")

### tc Type

`array` ([Time-coordinates scalar](audio-record-contentitem-properties-rreb-items-properties-s-time-coordinates-scalar.md))

### tc Constraints

**maximum number of items**: the maximum number of items for this array is: `2`

**minimum number of items**: the minimum number of items for this array is: `2`

### tc Examples

```json
[
  12.5,
  3.2
]
```

## s

offset start (relative to ft field)

`s`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Audio Record Content Item](audio-record-contentitem-properties-rreb-items-properties-t-items-properties-s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json#/properties/rreb/items/properties/t/items/properties/s")

### s Type

`integer`

## l

token length

`l`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Audio Record Content Item](audio-record-contentitem-properties-rreb-items-properties-t-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/rebuilt/audio-record-contentitem.v1.schema.json#/properties/rreb/items/properties/t/items/properties/l")

### l Type

`integer`
