## 1 Type

`object` ([ContentItem Core Fields (part of composed schema)](sem-6-allof-contentitem-core-fields-part-of-composed-schema.md))

# 1 Properties

| Property                                         | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                             |
| :----------------------------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                        | `string`  | Required | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-content-item-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/id")                        |
| [meta\_journal\_s](#meta_journal_s)              | `string`  | Required | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_journal_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_journal_s")             |
| [meta\_media\_alias\_s](#meta_media_alias_s)     | `string`  | Required | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-media-title-alias.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_media_alias_s")      |
| [meta\_year\_i](#meta_year_i)                    | `integer` | Required | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_year_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_year_i")                   |
| [meta\_month\_i](#meta_month_i)                  | `integer` | Required | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_month_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_month_i")                 |
| [meta\_yearmonth\_s](#meta_yearmonth_s)          | `string`  | Optional | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_yearmonth_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_yearmonth_s")         |
| [meta\_day\_i](#meta_day_i)                      | `integer` | Required | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_day_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_day_i")                     |
| [meta\_ed\_s](#meta_ed_s)                        | `string`  | Optional | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_ed_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_ed_s")                       |
| [meta\_date\_dt](#meta_date_dt)                  | `string`  | Required | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_date_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_date_dt")                 |
| [meta\_issue\_id\_s](#meta_issue_id_s)           | `string`  | Optional | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_issue_id_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_issue_id_s")           |
| [meta\_source\_type\_s](#meta_source_type_s)     | `string`  | Required | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_source_type_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_source_type_s")     |
| [meta\_source\_medium\_s](#meta_source_medium_s) | `string`  | Required | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_source_medium_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_source_medium_s") |
| [meta\_radio\_program\_s](#meta_radio_program_s) | `string`  | Optional | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-radio-program.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_radio_program_s")        |
| [meta\_radio\_channel\_s](#meta_radio_channel_s) | `string`  | Optional | cannot be null | [ContentItem Core Fields (part of composed schema)](content-item-1-properties-radio-channel.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_radio_channel_s")        |
| Additional Properties                            | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                        |

## id

Unique identifier for the content item

`id`

* is required

* Type: `string` ([Content Item ID](content-item-1-properties-content-item-id.md))

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-content-item-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/id")

### id Type

`string` ([Content Item ID](content-item-1-properties-content-item-id.md))

## meta\_journal\_s

Media title alias. Will soon be deprecated in favor of meta\_media\_s.

`meta_journal_s`

* is required

* Type: `string`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_journal_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_journal_s")

### meta\_journal\_s Type

`string`

## meta\_media\_alias\_s

Media title alias. Will soon be deprecated in favor of meta\_media\_s.

`meta_media_alias_s`

* is required

* Type: `string` ([Media Title Alias](content-item-1-properties-media-title-alias.md))

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-media-title-alias.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_media_alias_s")

### meta\_media\_alias\_s Type

`string` ([Media Title Alias](content-item-1-properties-media-title-alias.md))

## meta\_year\_i

Year of publication/broadcast

`meta_year_i`

* is required

* Type: `integer`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_year_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_year_i")

### meta\_year\_i Type

`integer`

## meta\_month\_i

Month of publication/broadcast

`meta_month_i`

* is required

* Type: `integer`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_month_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_month_i")

### meta\_month\_i Type

`integer`

### meta\_month\_i Constraints

**maximum**: the value of this number must smaller than or equal to: `12`

**minimum**: the value of this number must greater than or equal to: `1`

## meta\_yearmonth\_s

Year-month in YYYY-MM format

`meta_yearmonth_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_yearmonth_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_yearmonth_s")

### meta\_yearmonth\_s Type

`string`

### meta\_yearmonth\_s Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\d{4}-\d{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5Cd%7B4%7D-%5Cd%7B2%7D%24 "try regular expression with regexr.com")

## meta\_day\_i

Day of publication/broadcast

`meta_day_i`

* is required

* Type: `integer`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_day_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_day_i")

### meta\_day\_i Type

`integer`

### meta\_day\_i Constraints

**maximum**: the value of this number must smaller than or equal to: `31`

**minimum**: the value of this number must greater than or equal to: `1`

## meta\_ed\_s

Edition identifier

`meta_ed_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_ed_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_ed_s")

### meta\_ed\_s Type

`string`

## meta\_date\_dt

Full date and time in ISO 8601 format

`meta_date_dt`

* is required

* Type: `string`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_date_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_date_dt")

### meta\_date\_dt Type

`string`

### meta\_date\_dt Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## meta\_issue\_id\_s

Issue identifier

`meta_issue_id_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_issue_id_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_issue_id_s")

### meta\_issue\_id\_s Type

`string`

## meta\_source\_type\_s

Type of the media source. Should be a value from impresso-essentials.utils SourceType enum.

`meta_source_type_s`

* is required

* Type: `string`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_source_type_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_source_type_s")

### meta\_source\_type\_s Type

`string`

### meta\_source\_type\_s Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"newspaper"`       |             |
| `"radio_broadcast"` |             |
| `"radio_magazine"`  |             |
| `"radio_schedule"`  |             |
| `"monograph"`       |             |
| `"encyclopedia"`    |             |

## meta\_source\_medium\_s

Medium of the source (audio for audio radio broadcasts, print for newspapers, typescript for digitised radio bulletin typescripts).

`meta_source_medium_s`

* is required

* Type: `string`

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-meta_source_medium_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_source_medium_s")

### meta\_source\_medium\_s Type

`string`

### meta\_source\_medium\_s Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"audio"`      |             |
| `"print"`      |             |
| `"typescript"` |             |

## meta\_radio\_program\_s

Radio program name the broadcast belongs to. Sourced from 'radio\_program' key in additional\_metadata. Provider: RTS.

`meta_radio_program_s`

* is optional

* Type: `string` ([Radio Program](content-item-1-properties-radio-program.md))

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-radio-program.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_radio_program_s")

### meta\_radio\_program\_s Type

`string` ([Radio Program](content-item-1-properties-radio-program.md))

## meta\_radio\_channel\_s

Radio channel the broadcast was aired on. Sourced from 'radio\_channel' key in additional\_metadata. Provider: RTS.

`meta_radio_channel_s`

* is optional

* Type: `string` ([Radio Channel](content-item-1-properties-radio-channel.md))

* cannot be null

* defined in: [ContentItem Core Fields (part of composed schema)](content-item-1-properties-radio-channel.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.core.v1.schema.json#/properties/meta_radio_channel_s")

### meta\_radio\_channel\_s Type

`string` ([Radio Channel](content-item-1-properties-radio-channel.md))

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
