## Audio Record Content Item Type

`object` ([Audio Record Content Item](audio_record_contentitem.md))

# Audio Record Content Item Properties

| Property         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                  |
| :--------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)        | `string` | Required | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-id.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/id")       |
| [ts](#ts)        | `string` | Required | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-ts.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/ts")       |
| [d](#d)          | `string` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-d.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/d")         |
| [st](#st)        | `string` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-st.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/st")       |
| [sm](#sm)        | `string` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-sm.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/sm")       |
| [tp](#tp)        | `string` | Required | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-tp.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/tp")       |
| [lg](#lg)        | `string` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-lg.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/lg")       |
| [stt](#stt)      | `string` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-stt.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/stt")     |
| [dur](#dur)      | `string` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-dur.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/dur")     |
| [rc](#rc)        | `string` | Optional | can be null    | [Audio Record Content Item](audio_record_contentitem-properties-rc.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rc")       |
| [rp](#rp)        | `string` | Optional | can be null    | [Audio Record Content Item](audio_record_contentitem-properties-rp.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rp")       |
| [var\_t](#var_t) | `string` | Optional | can be null    | [Audio Record Content Item](audio_record_contentitem-properties-var_t.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/var_t") |
| [title](#title)  | `string` | Optional | can be null    | [Audio Record Content Item](audio_record_contentitem-properties-title.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/title") |
| [rr](#rr)        | `array`  | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-rr.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rr")       |
| [ft](#ft)        | `string` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-ft.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/ft")       |
| [sb](#sb)        | `array`  | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-sb.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/sb")       |
| [ub](#ub)        | `array`  | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-ub.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/ub")       |
| [ssb](#ssb)      | `array`  | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-ssb.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/ssb")     |
| [rreb](#rreb)    | `array`  | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-rreb.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb")   |

## id

The unique identifier for the content-item (CI), only 1 CI per radio broadcast audio record

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-id.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/id")

### id Type

`string`

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z_]+-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-i[0-9]{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z_%5D%2B-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C2%7D-i%5B0-9%5D%7B4%7D%24 "try regular expression with regexr.com")

## ts

timestamp of creation of the JSON file (in '%Y-%m-%dT%H:%M:%SZ' format e.g. '2018-09-18T08:00:08Z')

`ts`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-ts.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/ts")

### ts Type

`string`

### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

## d

Date of publication of radio broadcast (yyyy-mm-dd)

`d`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-d.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/d")

### d Type

`string`

### d Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7D%24 "try regular expression with regexr.com")

## st

Type of media source. Should be a value the impresso-essentials.utils SourceType enum.

`st`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-st.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/st")

### st Type

`string`

### st Constraints

**constant**: the value of this property must be equal to:

```json
"radio_broadcast"
```

## sm

Source medium, format in which the media was originally produced, here should be image-based.

`sm`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-sm.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/sm")

### sm Type

`string`

### sm Constraints

**constant**: the value of this property must be equal to:

```json
"audio"
```

## tp

content-item type (e.g. 'ar' for article, 'ad' for advertisement)

`tp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-tp.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/tp")

### tp Type

`string`

## lg

two letter language code

`lg`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-lg.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/lg")

### lg Type

`string`

### lg Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-z]{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%7D%24 "try regular expression with regexr.com")

## stt

Audio record's start time (of day) if exists or is available (00:00:00 otherwise), in HH:MM:SS format.

`stt`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-stt.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/stt")

### stt Type

`string`

### stt Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B0-1%5D%5B0-9%5D%7C2%5B0-3%5D\)%3A%5B0-5%5D%5B0-9%5D%3A%5B0-5%5D%5B0-9%5D%24 "try regular expression with regexr.com")

## dur

Duration of the entire audio boradcast, in HH:MM:SS format.

`dur`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-dur.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/dur")

### dur Type

`string`

### dur Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B0-1%5D%5B0-9%5D%7C2%5B0-3%5D\)%3A%5B0-5%5D%5B0-9%5D%3A%5B0-5%5D%5B0-9%5D%24 "try regular expression with regexr.com")

## rc

Radio channel, if known/defined.

`rc`

*   is optional

*   Type: `string`

*   can be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-rc.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rc")

### rc Type

`string`

## rp

Radio program, if known/defined.

`rp`

*   is optional

*   Type: `string`

*   can be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-rp.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rp")

### rp Type

`string`

## var\_t

Variant 'full' title of the media in the case it's defined in the CI metadata

`var_t`

*   is optional

*   Type: `string`

*   can be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-var_t.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/var_t")

### var\_t Type

`string`

## title

radio broadcast content-item title.

`title`

*   is optional

*   Type: `string`

*   can be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-title.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/title")

### title Type

`string`

## rr

array of audio record numbers over which the CI spans, for now always \[1].

`rr`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-rr.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rr")

### rr Type

`integer[]`

### rr Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## ft

the rebuilt fulltext

`ft`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-ft.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/ft")

### ft Type

`string`

## sb

text offsets of broadcast sections (relative to 'ft' field)

`sb`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-sb.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/sb")

### sb Type

`integer[]`

### sb Constraints

**constant**: the value of this property must be equal to:

```json
[
  1
]
```

## ub

text offsets of utterances (relative to 'ft' field)

`ub`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-ub.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/ub")

### ub Type

`integer[]`

## ssb

text offsets of speech segments (relative to 'ft' field)

`ssb`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-ssb.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/ssb")

### ssb Type

`integer[]`

## rreb

a list of rebuilt records

`rreb`

*   is optional

*   Type: `object[]` ([Details](audio_record_contentitem-properties-rreb-items.md))

*   cannot be null

*   defined in: [Audio Record Content Item](audio_record_contentitem-properties-rreb.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb")

### rreb Type

`object[]` ([Details](audio_record_contentitem-properties-rreb-items.md))
