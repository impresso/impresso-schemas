## items Type

`object` ([Details](issue-properties-i-items.md))

# items Properties

| Property    | Type     | Required | Nullable       | Defined by                                                                                                                                                            |
| :---------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [m](#m)     | Merged   | Optional | cannot be null | [Issue](issue-defs-metadata.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/properties/i/items/properties/m")                       |
| [c](#c)     | `array`  | Optional | cannot be null | [Issue](issue-properties-i-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/properties/i/items/properties/c")     |
| [l](#l)     | `object` | Optional | cannot be null | [Issue](issue-properties-i-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/properties/i/items/properties/l")     |
| [pOf](#pof) | `string` | Optional | cannot be null | [Issue](issue-properties-i-items-properties-pof.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/properties/i/items/properties/pOf") |

## m

Metadata about the content item.

`m`

* is optional

* Type: `object` ([Details](issue-defs-metadata.md))

* cannot be null

* defined in: [Issue](issue-defs-metadata.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/properties/i/items/properties/m")

### m Type

`object` ([Details](issue-defs-metadata.md))

one (and only one) of

* [Untitled undefined type in Issue](issue-defs-metadata-oneof-0.md "check type definition")

* [Untitled undefined type in Issue](issue-defs-metadata-oneof-1.md "check type definition")

## c

Coordinates (xywh format or \[HPOS, VPOS, WIDTH, HEIGHT]) of image-region corresponding to the content-item depending on its type (if `tp == image`).

`c`

* is optional

* Type: `integer[]`

* cannot be null

* defined in: [Issue](issue-properties-i-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/properties/i/items/properties/c")

### c Type

`integer[]`

### c Constraints

**minimum number of items**: the minimum number of items for this array is: `4`

## l

Legacy sections or components of the content item in the original OCR/OLR. They are meant to enable the reassignation of Impresso CIs (and enrichments) to the original OCR/OLR files.

`l`

* is optional

* Type: `object` ([Details](issue-properties-i-items-properties-l.md))

* cannot be null

* defined in: [Issue](issue-properties-i-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/properties/i/items/properties/l")

### l Type

`object` ([Details](issue-properties-i-items-properties-l.md))

## pOf

Article/content-item to which the image is attached (if `tp == image`).

`pOf`

* is optional

* Type: `string`

* cannot be null

* defined in: [Issue](issue-properties-i-items-properties-pof.md "https://impresso.github.io/impresso-schemas/json/canonical/issue.schema.json#/properties/i/items/properties/pOf")

### pOf Type

`string`
