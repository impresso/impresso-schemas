## items Type

`object` ([Details](page-properties-r-items-properties-p-items-properties-l-items.md))

# items Properties

| Property | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                         |
| :------- | :------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [c](#c)  | `array` | Required | cannot be null | [Printed Page](page-defs-coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/c")                                                      |
| [t](#t)  | `array` | Required | cannot be null | [Printed Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t") |

## c

Coordinates of bounding-box, following IIIF regions schema (\[x, y, width, height] or \[HPOS, VPOS, WIDTH, HEIGHT]).

`c`

* is required

* Type: `integer[]`

* cannot be null

* defined in: [Printed Page](page-defs-coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/c")

### c Type

`integer[]`

### c Constraints

**maximum number of items**: the maximum number of items for this array is: `4`

**minimum number of items**: the minimum number of items for this array is: `4`

## t

Tokens (as detected by the OCR engine).

`t`

* is required

* Type: `object[]` ([Details](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items.md))

* cannot be null

* defined in: [Printed Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t")

### t Type

`object[]` ([Details](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items.md))
