## metadata Type

`object` ([Details](issue-defs-metadata.md))

one (and only one) of

*   [Untitled undefined type in Issue](issue-defs-metadata-oneof-0.md "check type definition")

*   [Untitled undefined type in Issue](issue-defs-metadata-oneof-1.md "check type definition")

# metadata Properties

| Property                         | Type      | Required | Nullable       | Defined by                                                                                                                                                                       |
| :------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                        | `string`  | Required | cannot be null | [Issue](issue-defs-metadata-properties-id.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/id")                       |
| [lg](#lg)                        | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-lg.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/lg")                       |
| [l](#l)                          | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-l.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/l")                         |
| [pp](#pp)                        | `array`   | Optional | cannot be null | [Issue](issue-defs-metadata-properties-pp.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/pp")                       |
| [rr](#rr)                        | `array`   | Optional | cannot be null | [Issue](issue-defs-metadata-properties-rr.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/rr")                       |
| [t](#t)                          | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-t.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/t")                         |
| [tp](#tp)                        | `string`  | Required | cannot be null | [Issue](issue-defs-metadata-properties-tp.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/tp")                       |
| [iiif\_link](#iiif_link)         | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-iiif_link.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/iiif_link")         |
| [ro](#ro)                        | `integer` | Optional | cannot be null | [Issue](issue-defs-metadata-properties-ro.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/ro")                       |
| [speakers](#speakers)            | `array`   | Optional | cannot be null | [Issue](issue-defs-metadata-properties-speakers.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/speakers")           |
| [var\_t](#var_t)                 | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-var_t.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/var_t")                 |
| [archival\_note](#archival_note) | `string`  | Optional | cannot be null | [Issue](issue-defs-metadata-properties-archival_note.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/archival_note") |

## id

Content item ID (e.g. `GDL-1900-01-02-a-i0001`).

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Issue](issue-defs-metadata-properties-id.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/$defs/metadata/properties/id")

### id Type

`string`

## lg

Language of the content item.

`lg`

*   is optional

*   Type: `string`

*   cannot be null

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
