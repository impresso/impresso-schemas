## Newspaper Issue Type

`object` ([Newspaper Issue](issue.md))

# Newspaper Issue Properties

| Property    | Type     | Required | Nullable       | Defined by                                                                                                                                |
| :---------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)   | `string` | Required | cannot be null | [Newspaper Issue](issue-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/id")   |
| [cdt](#cdt) | `string` | Required | cannot be null | [Newspaper Issue](issue-properties-cdt.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/cdt") |
| [i](#i)     | `array`  | Required | cannot be null | [Newspaper Issue](issue-properties-i.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/i")     |
| [s](#s)     | `array`  | Optional | cannot be null | [Newspaper Issue](issue-properties-s.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s")     |
| [pp](#pp)   | `array`  | Required | cannot be null | [Newspaper Issue](issue-properties-pp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/pp")   |
| [n](#n)     | `string` | Optional | cannot be null | [Newspaper Issue](issue-properties-n.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/n")     |
| [ar](#ar)   | `string` | Required | cannot be null | [Newspaper Issue](issue-properties-ar.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/ar")   |

## id

Canonical ID of the newspaper issue (e.g. GDL-1900-01-02-a)

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/id")

### id Type

`string`

## cdt

Creation date timestamp (of the JSON file).

`cdt`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-properties-cdt.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/cdt")

### cdt Type

`string`

## i

The content items contained in the newspaper issue.

`i`

*   is required

*   Type: `object[]` ([Details](issue-properties-i-items.md))

*   cannot be null

*   defined in: [Newspaper Issue](issue-properties-i.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/i")

### i Type

`object[]` ([Details](issue-properties-i-items.md))

## s

The text style as defined in the OCR output.
Each style consists of:

*   a name (`id`)
*   a type-face (`f`)
*   a font-size (`fs`)
*   a color (`rgb`).

`s`

*   is optional

*   Type: `object[]` ([Details](issue-properties-s-items.md))

*   cannot be null

*   defined in: [Newspaper Issue](issue-properties-s.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s")

### s Type

`object[]` ([Details](issue-properties-s-items.md))

## pp

Canonical IDs of pages in the issue, without file extension (e.g. GDL-1900-01-02-a-p0004).

`pp`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [Newspaper Issue](issue-properties-pp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/pp")

### pp Type

`string[]`

## n

Notes.

`n`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-properties-n.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/n")

### n Type

`string`

## ar

Access rights. Three possible situations are defined:

1.  open public: access without NDA, user could redistribute (as defined per Terms of Use)
2.  open private: access without an NDA, user cannot redistribute (private/academic use only)
3.  closed : accessible only upon signing an NDA, user cannot redistribute

`ar`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-properties-ar.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/ar")

### ar Type

`string`

### ar Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"open_public"`  |             |
| `"open_private"` |             |
| `"closed"`       |             |

# Newspaper Issue Definitions

## Definitions group metadata

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata"}
```

| Property                 | Type     | Required | Nullable       | Defined by                                                                                                                                                                                      |
| :----------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id-1)              | `string` | Required | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/id")               |
| [l](#l)                  | `string` | Optional | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-l.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/l")                 |
| [pp](#pp-1)              | `array`  | Required | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-pp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/pp")               |
| [t](#t)                  | `string` | Optional | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-t.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/t")                 |
| [tp](#tp)                | `string` | Required | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-tp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/tp")               |
| [iiif\_link](#iiif_link) | `string` | Optional | cannot be null | [Newspaper Issue](issue-definitions-metadata-properties-iiif_link.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/iiif_link") |

### id

Content item ID (e.g. `GDL-1900-01-02-a-i0001`).

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/id")

#### id Type

`string`

### l

Language of the content item.

`l`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-l.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/l")

#### l Type

`string`

### pp

Page numbers over which the content item spans.

`pp`

*   is required

*   Type: `integer[]`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-pp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/pp")

#### pp Type

`integer[]`

### t

Title of the content item.

`t`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-t.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/t")

#### t Type

`string`

### tp

Type of the content item.

`tp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-tp.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/tp")

#### tp Type

`string`

#### tp Constraints

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

### iiif\_link

IIIF image link, depending on content item type (if `tp == image`)

`iiif_link`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata-properties-iiif_link.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/definitions/metadata/properties/iiif_link")

#### iiif\_link Type

`string`
