## items Type

`object` ([Details](audio-record-properties-s-items-properties-u-items-properties-ss-items.md))

# items Properties

| Property  | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                          |
| :-------- | :------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tc](#tc) | `array` | Required | cannot be null | [Audio Record](audio-record-contentitem-properties-rreb-items-properties-s-time-coordinates-scalar.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/time-coordinates.v1.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/tc")                |
| [t](#t)   | `array` | Required | cannot be null | [Audio Record](audio-record-properties-s-items-properties-u-items-properties-ss-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/t") |

## tc

Temporal span within an audio recording, in the format \[start-time, duration], each expressed in seconds.

`tc`

* is required

* Type: `array` ([Time-coordinates scalar](audio-record-contentitem-properties-rreb-items-properties-s-time-coordinates-scalar.md))

* cannot be null

* defined in: [Audio Record](audio-record-contentitem-properties-rreb-items-properties-s-time-coordinates-scalar.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/time-coordinates.v1.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/tc")

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

## t

Speech tokens (as detected by the ASR engine).

`t`

* is required

* Type: `object[]` ([Details](audio-record-properties-s-items-properties-u-items-properties-ss-items-properties-t-items.md))

* cannot be null

* defined in: [Audio Record](audio-record-properties-s-items-properties-u-items-properties-ss-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/s/items/properties/u/items/properties/ss/items/properties/t")

### t Type

`object[]` ([Details](audio-record-properties-s-items-properties-u-items-properties-ss-items-properties-t-items.md))
