## metadata Type

`object` ([Details](issue-definitions-metadata.md))

# metadata Properties

| Property                 | Type     | Required | Nullable       | Defined by                                                                                                                                                                                      |
| :----------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                | `string` | Required | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/id")               |
| [l](#l)                  | `string` | Optional | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-l.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/l")                 |
| [pp](#pp)                | `array`  | Required | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-pp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/pp")               |
| [t](#t)                  | `string` | Optional | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-t.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/t")                 |
| [tp](#tp)                | `string` | Required | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-tp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/tp")               |
| [iiif\_link](#iiif_link) | `string` | Optional | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-iiif_link.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/iiif_link") |

## id

Content item ID (e.g. `GDL-1900-01-02-a-i0001`).

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/id")

### id Type

`string`

## l

Language of the content item.

`l`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-l.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/l")

### l Type

`string`

## pp

Page numbers over which the content item spans.

`pp`

*   is required

*   Type: `integer[]`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-pp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/pp")

### pp Type

`integer[]`

## t

Title of the content item.

`t`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-t.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/t")

### t Type

`string`

## tp

Type of the content item.

`tp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-tp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/tp")

### tp Type

`string`

### tp Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"article"`      |             |
| `"ad"`           |             |
| `"image"`        |             |
| `"table"`        |             |
| `"death_notice"` |             |
| `"weather"`      |             |
| `"page"`         |             |

## iiif\_link

IIIF image link, depending on content item type (if `tp == image`)

`iiif_link`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-iiif_link.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/iiif_link")

### iiif\_link Type

`string`
