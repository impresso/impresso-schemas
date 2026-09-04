## Content Item - Audio Part Schema Type

`object` ([Content Item - Audio Part Schema](content-item-7.md))

# Content Item - Audio Part Schema Properties

| Property                                   | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                            |
| :----------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [meta\_start\_time\_s](#meta_start_time_s) | `string`  | Optional | cannot be null | [Content Item - Audio Part Schema](content-item-7-properties-meta_start_time_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/meta_start_time_s") |
| [meta\_duration\_s](#meta_duration_s)      | `string`  | Optional | cannot be null | [Content Item - Audio Part Schema](content-item-7-properties-meta_duration_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/meta_duration_s")     |
| [record\_id\_ss](#record_id_ss)            | `array`   | Optional | cannot be null | [Content Item - Audio Part Schema](content-item-7-properties-record_id_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/record_id_ss")           |
| [record\_nb\_is](#record_nb_is)            | `array`   | Optional | cannot be null | [Content Item - Audio Part Schema](content-item-7-properties-record_nb_is.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/record_nb_is")           |
| [nb\_record\_i](#nb_record_i)              | `integer` | Optional | cannot be null | [Content Item - Audio Part Schema](content-item-7-properties-nb_record_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/nb_record_i")             |
| [rreb\_plain](#rreb_plain)                 | `string`  | Optional | cannot be null | [Content Item - Audio Part Schema](content-item-7-properties-rreb_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/rreb_plain")               |
| [ub\_plain](#ub_plain)                     | `string`  | Optional | cannot be null | [Content Item - Audio Part Schema](content-item-7-properties-ub_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/ub_plain")                   |
| Additional Properties                      | Any       | Optional | can be null    |                                                                                                                                                                                                                                                       |

## meta\_start\_time\_s

Start time of media in HH:MM:SS format (relative to the day of broadcast). Applies only to audio radio broadcasts.

`meta_start_time_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item - Audio Part Schema](content-item-7-properties-meta_start_time_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/meta_start_time_s")

### meta\_start\_time\_s Type

`string`

### meta\_start\_time\_s Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\d{2}:\d{2}:\d{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5Cd%7B2%7D%3A%5Cd%7B2%7D%3A%5Cd%7B2%7D%24 "try regular expression with regexr.com")

## meta\_duration\_s

Duration of the radio broadcast in HH:MM:SS format (relative to the start of the broadcast on the given broadcast day).  Applies only to audio radio broadcasts."

`meta_duration_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item - Audio Part Schema](content-item-7-properties-meta_duration_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/meta_duration_s")

### meta\_duration\_s Type

`string`

### meta\_duration\_s Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\d{2}:\d{2}:\d{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5Cd%7B2%7D%3A%5Cd%7B2%7D%3A%5Cd%7B2%7D%24 "try regular expression with regexr.com")

## record\_id\_ss

Array of record identifiers for radio broadcast segments

`record_id_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Content Item - Audio Part Schema](content-item-7-properties-record_id_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/record_id_ss")

### record\_id\_ss Type

`string[]`

## record\_nb\_is

Array of record numbers corresponding to radio broadcast segments

`record_nb_is`

* is optional

* Type: `integer[]`

* cannot be null

* defined in: [Content Item - Audio Part Schema](content-item-7-properties-record_nb_is.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/record_nb_is")

### record\_nb\_is Type

`integer[]`

## nb\_record\_i

Total number of records/segments in the radio broadcast

`nb_record_i`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Content Item - Audio Part Schema](content-item-7-properties-nb_record_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/nb_record_i")

### nb\_record\_i Type

`integer`

### nb\_record\_i Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## rreb\_plain

Audio time stamps of the audio record. Serialized JSON of radio broadcast segments as defined in <https://github.com/impresso/impresso-schemas/blob/radio-broadcast-schemas/json/rebuilt/audio_record_contentitem.schema.json>.

`rreb_plain`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item - Audio Part Schema](content-item-7-properties-rreb_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/rreb_plain")

### rreb\_plain Type

`string`

### rreb\_plain Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## ub\_plain

Utterance breaks ends offsets in content item transcript. Serialized array of integers, see 'ub' in <https://github.com/impresso/impresso-schemas/blob/radio-broadcast-schemas/json/rebuilt/audio_record_contentitem.schema.json>.

`ub_plain`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item - Audio Part Schema](content-item-7-properties-ub_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.audio.v1.schema.json#/properties/ub_plain")

### ub\_plain Type

`string`

### ub\_plain Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
