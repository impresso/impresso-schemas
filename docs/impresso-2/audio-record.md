## Audio Record Type

`object` ([Audio Record](audio-record.md))

any of

* [Untitled undefined type in Audio Record](audio-record-anyof-0.md "check type definition")

* [Untitled undefined type in Audio Record](audio-record-anyof-1.md "check type definition")

# Audio Record Properties

| Property                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                  |
| :-------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                         | `string` | Required | cannot be null | [Audio Record](audio-record-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/id")                                           |
| [iiif\_base\_uri](#iiif_base_uri) | `string` | Required | cannot be null | [Audio Record](audio-record-properties-iiif_base_uri.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/iiif_base_uri")                     |
| [stt](#stt)                       | `string` | Required | cannot be null | [Audio Record](audio-record-properties-stt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/stt")                                         |
| [dur](#dur)                       | `string` | Required | cannot be null | [Audio Record](audio-record-properties-dur.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/dur")                                         |
| [st](#st)                         | `string` | Optional | cannot be null | [Audio Record](manifest-properties-media_list-items-properties-impresso-source-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/common/source-type.v1.schema.json#/properties/st")     |
| [sm](#sm)                         | `string` | Optional | cannot be null | [Audio Record](manifest-properties-media_list-items-properties-impresso-source-medium.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/common/source-medium.v1.schema.json#/properties/sm") |
| [cdt](#cdt)                       | `string` | Optional | cannot be null | [Audio Record](audio-record-properties-cdt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/cdt")                                         |
| [ts](#ts)                         | `string` | Optional | cannot be null | [Audio Record](audio-record-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/ts")                                           |
| [s](#s)                           | `array`  | Required | cannot be null | [Audio Record](audio-record-properties-s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/s")                                             |

## id

Canonical ID of the radio broadcast's audio record (e.g. \[INA alias]-1940-07-22-a-r0001)

`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Audio Record](audio-record-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/id")

### id Type

`string`

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-r[0-9]{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z%5D%5BA-Za-z0-9_%5D*-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C2%7D-r%5B0-9%5D%7B4%7D%24 "try regular expression with regexr.com")

## iiif\_base\_uri

Base of the IIIF manifest URI.

`iiif_base_uri`

* is required

* Type: `string`

* cannot be null

* defined in: [Audio Record](audio-record-properties-iiif_base_uri.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/iiif_base_uri")

### iiif\_base\_uri Type

`string`

## stt

Start time of the audio recording, relative to the broadcasting day date (HH:MM:SS). If not available, defaults to 00:00:00.

`stt`

* is required

* Type: `string`

* cannot be null

* defined in: [Audio Record](audio-record-properties-stt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/stt")

### stt Type

`string`

### stt Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B0-1%5D%5B0-9%5D%7C2%5B0-3%5D\)%3A%5B0-5%5D%5B0-9%5D%3A%5B0-5%5D%5B0-9%5D%24 "try regular expression with regexr.com")

## dur

Total duration of the audio broadcast, in HH:MM:SS format.

`dur`

* is required

* Type: `string`

* cannot be null

* defined in: [Audio Record](audio-record-properties-dur.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/dur")

### dur Type

`string`

### dur Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B0-1%5D%5B0-9%5D%7C2%5B0-3%5D\)%3A%5B0-5%5D%5B0-9%5D%3A%5B0-5%5D%5B0-9%5D%24 "try regular expression with regexr.com")

## st

Type of media source from which a data-preparation record originates. Value from the `impresso_essentials.utils.SourceType` enum. This schema defines the value independently of the property name that stores it; current data-preparation properties using this value are `st` (canonical, rebuilt) and `source_type` (versioning manifest).

`st`

* is optional

* Type: `string` ([Impresso source type](manifest-properties-media_list-items-properties-impresso-source-type.md))

* cannot be null

* defined in: [Audio Record](manifest-properties-media_list-items-properties-impresso-source-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/common/source-type.v1.schema.json#/properties/st")

### st Type

`string` ([Impresso source type](manifest-properties-media_list-items-properties-impresso-source-type.md))

### st Constraints

**constant**: the value of this property must be equal to:

```json
"radio_broadcast"
```

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"newspaper"`       |             |
| `"radio_broadcast"` |             |
| `"radio_magazine"`  |             |
| `"radio_schedule"`  |             |
| `"monograph"`       |             |
| `"encyclopedia"`    |             |

### st Examples

```json
"newspaper"
```

```json
"radio_broadcast"
```

## sm

Medium in which the source media of a data-preparation record was originally produced. Value from the `impresso_essentials.utils.SourceMedium` enum. This schema defines the value independently of the property name that stores it; current data-preparation properties using this value are `sm` (canonical, rebuilt) and `source_medium` (versioning manifest).

`sm`

* is optional

* Type: `string` ([Impresso source medium](manifest-properties-media_list-items-properties-impresso-source-medium.md))

* cannot be null

* defined in: [Audio Record](manifest-properties-media_list-items-properties-impresso-source-medium.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/common/source-medium.v1.schema.json#/properties/sm")

### sm Type

`string` ([Impresso source medium](manifest-properties-media_list-items-properties-impresso-source-medium.md))

### sm Constraints

**constant**: the value of this property must be equal to:

```json
"audio"
```

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"print"`      |             |
| `"typescript"` |             |
| `"audio"`      |             |

### sm Examples

```json
"print"
```

```json
"audio"
```

## cdt

Creation date timestamp (of the JSON file).

`cdt`

* is optional

* Type: `string`

* cannot be null

* defined in: [Audio Record](audio-record-properties-cdt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/cdt")

### cdt Type

`string`

## ts

Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format).

`ts`

* is optional

* Type: `string`

* cannot be null

* defined in: [Audio Record](audio-record-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/ts")

### ts Type

`string`

## s

List of audio broadcast sections.

`s`

* is required

* Type: `object[]` ([Details](audio-record-properties-s-items.md))

* cannot be null

* defined in: [Audio Record](audio-record-properties-s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/properties/s")

### s Type

`object[]` ([Details](audio-record-properties-s-items.md))

# Audio Record Definitions

## Definitions group time\_coordinates

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/impresso-2/data-preparation/canonical/audio-record.v1.schema.json#/$defs/time_coordinates"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
