## items Type

`object` ([Details](audio_record_contentitem-properties-rreb-items.md))

# items Properties

| Property  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                        |
| :-------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id) | `string`  | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-id.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/id") |
| [n](#n)   | `integer` | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-n.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/n")   |
| [t](#t)   | `array`   | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/t")   |
| [s](#s)   | `array`   | Optional | cannot be null | [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-s.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/s")   |

## id

audio record canonical ID

`id`

* is optional

* Type: `string`

* cannot be null

* defined in: [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-id.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/id")

### id Type

`string`

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,3}-r[0-9]{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z%5D%5BA-Za-z0-9_%5D*-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C3%7D-r%5B0-9%5D%7B4%7D%24 "try regular expression with regexr.com")

## n

audio record number

`n`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-n.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/n")

### n Type

`integer`

### n Constraints

**constant**: the value of this property must be equal to:

```json
1
```

## t

a list of tokens

`t`

* is optional

* Type: `object[]` ([Details](audio_record_contentitem-properties-rreb-items-properties-t-items.md))

* cannot be null

* defined in: [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/t")

### t Type

`object[]` ([Details](audio_record_contentitem-properties-rreb-items-properties-t-items.md))

## s

List of sections time coordinates.

`s`

* is optional

* Type: unknown\[]

* cannot be null

* defined in: [Audio Record Content Item](audio_record_contentitem-properties-rreb-items-properties-s.md "https://impresso.github.io/impresso-schemas/json/rebuilt/audio_record_contentitem.schema.json#/properties/rreb/items/properties/s")

### s Type

unknown\[]
