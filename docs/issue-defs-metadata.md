## metadata Type

`object` ([Details](issue-defs-metadata.md))

one (and only one) of

*   [Untitled undefined type in Issue](issue-defs-metadata-oneof-0.md "check type definition")

*   [Untitled undefined type in Issue](issue-defs-metadata-oneof-1.md "check type definition")

# metadata Properties

| Property                                                           | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                       |
| :----------------------------------------------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                                          | `string`  | Required | cannot be null | [Issue](issue-defs-metadata-properties-id.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/id")                                                       |
| [lg](#lg)                                                          | `string`  | Optional | can be null    | [Issue](issue-defs-metadata-properties-lg.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/lg")                                                       |
| [l](#l)                                                            | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-l.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/l")                                                         |
| [consolidated\_reocr\_applied](#consolidated_reocr_applied)        | `boolean` | Optional | cannot be null | [Issue](issue-defs-metadata-properties-consolidated_reocr_applied.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_reocr_applied")       |
| [consolidated\_reocr\_run\_id](#consolidated_reocr_run_id)         | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-consolidated_reocr_run_id.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_reocr_run_id")         |
| [consolidated\_ocrqa](#consolidated_ocrqa)                         | `number`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-consolidated_ocrqa.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_ocrqa")                       |
| [consolidated\_lg](#consolidated_lg)                               | Merged    | Optional | can be null    | [Issue](issue-defs-metadata-properties-consolidated_lg.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_lg")                             |
| [consolidated\_langident\_run\_id](#consolidated_langident_run_id) | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-consolidated_langident_run_id.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_langident_run_id") |
| [pp](#pp)                                                          | `array`   | Optional | cannot be null | [Issue](issue-defs-metadata-properties-pp.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/pp")                                                       |
| [rr](#rr)                                                          | `array`   | Optional | cannot be null | [Issue](issue-defs-metadata-properties-rr.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/rr")                                                       |
| [t](#t)                                                            | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-t.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/t")                                                         |
| [tp](#tp)                                                          | `string`  | Required | cannot be null | [Issue](issue-defs-metadata-properties-tp.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/tp")                                                       |
| [iiif\_link](#iiif_link)                                           | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-iiif_link.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/iiif_link")                                         |
| [ro](#ro)                                                          | `integer` | Optional | cannot be null | [Issue](issue-defs-metadata-properties-ro.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/ro")                                                       |
| [speakers](#speakers)                                              | `array`   | Optional | cannot be null | [Issue](issue-defs-metadata-properties-speakers.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/speakers")                                           |
| [var\_t](#var_t)                                                   | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-var_t.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/var_t")                                                 |
| [archival\_note](#archival_note)                                   | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-archival_note.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/archival_note")                                 |

## id

Content item ID (e.g. `GDL-1900-01-02-a-i0001`).

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-id.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/id")

### id Type

`string`

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-i[0-9]{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z%5D%5BA-Za-z0-9_%5D*-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C2%7D-i%5B0-9%5D%7B4%7D%24 "try regular expression with regexr.com")

## lg

Language of the content item.

`lg`

*   is optional

*   Type: `string`

*   can be null

*   defined in: [Issue](issue-defs-metadata-properties-lg.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/lg")

### lg Type

`string`

## l

Language of the content item (deprecated).

`l`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-l.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/l")

### l Type

`string`

## consolidated\_reocr\_applied

True if the CI's text went through the re-OCRisation process. Only defined if `consolidated==True`.

`consolidated_reocr_applied`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-consolidated_reocr_applied.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_reocr_applied")

### consolidated\_reocr\_applied Type

`boolean`

## consolidated\_reocr\_run\_id

Run ID corresponding to the re-OCR process. Only defined if `consolidated==True` and `consolidated_re_ocr_applied==True`.

`consolidated_reocr_run_id`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-consolidated_reocr_run_id.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_reocr_run_id")

### consolidated\_reocr\_run\_id Type

`string`

## consolidated\_ocrqa

The estimated OCR quality, between 0 and 1. Only defined if `consolidated==True`.

`consolidated_ocrqa`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-consolidated_ocrqa.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_ocrqa")

### consolidated\_ocrqa Type

`number`

## consolidated\_lg

Computed language of the content item. Only defined if `consolidated==True`.

`consolidated_lg`

*   is optional

*   Type: `string` ([Details](issue-defs-metadata-properties-consolidated_lg.md))

*   can be null

*   defined in: [Issue](issue-defs-metadata-properties-consolidated_lg.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_lg")

### consolidated\_lg Type

`string` ([Details](issue-defs-metadata-properties-consolidated_lg.md))

one (and only one) of

*   [null](issue-defs-metadata-properties-consolidated_lg-oneof-null.md "check type definition")

*   [langISO639Type](issue-defs-metadata-properties-consolidated_lg-oneof-langiso639type.md "check type definition")

## consolidated\_langident\_run\_id

Run ID corresponding to the lang ID process used to obtain the `consolidated_language` value. Only defined if `consolidated==True`.

`consolidated_langident_run_id`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-consolidated_langident_run_id.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/consolidated_langident_run_id")

### consolidated\_langident\_run\_id Type

`string`

## pp

Page numbers over which the content item spans, in the case `sm` is in \[`print`, `typescript`].

`pp`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-pp.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/pp")

### pp Type

`integer[]`

## rr

Record numbers over which the content item spans, in the case `sm` is `audio`.

`rr`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-rr.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/rr")

### rr Type

`integer[]`

## t

Title of the content item.

`t`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-t.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/t")

### t Type

`string`

## tp

Type of the content item.

`tp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-tp.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/tp")

### tp Type

`string`

### tp Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                       | Explanation |
| :-------------------------- | :---------- |
| `"article"`                 |             |
| `"ad"`                      |             |
| `"image"`                   |             |
| `"table"`                   |             |
| `"death_notice"`            |             |
| `"weather"`                 |             |
| `"page"`                    |             |
| `"radio_bulletin"`          |             |
| `"radio_broadcast_episode"` |             |
| `"chronicle"`               |             |

## iiif\_link

IIIF image link, depending on content item type (if `tp == image`). Should follow the format: '{scheme}://{server}/{prefix}/{identifier}/info.json'.

`iiif_link`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-iiif_link.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/iiif_link")

### iiif\_link Type

`string`

## ro

Reading order index of the content item, for the table of contents view on the interface. If not defined, the CI number (after 'i' in the ID) should be used.

`ro`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-ro.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/ro")

### ro Type

`integer`

## speakers

List of speakers (names or IDs based on availabilities) within boradcast.

`speakers`

*   is optional

*   Type: an array of the following:`object` or `string` ([Details](issue-defs-metadata-properties-speakers-items.md))

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-speakers.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/speakers")

### speakers Type

an array of the following:`object` or `string` ([Details](issue-defs-metadata-properties-speakers-items.md))

## var\_t

Variant title of the media title this CI is from (only in the case of BL newspapers).

`var_t`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-var_t.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/var_t")

### var\_t Type

`string`

## archival\_note

Plain-text archival note or description concerning the content-item (here in the case of INA).

`archival_note`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-archival_note.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/archival_note")

### archival\_note Type

`string`
