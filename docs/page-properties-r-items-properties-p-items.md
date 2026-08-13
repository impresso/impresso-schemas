## items Type

`object` ([Details](page-properties-r-items-properties-p-items.md))

# items Properties

| Property | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                   |
| :------- | :------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [c](#c)  | `array` | Optional | cannot be null | [Printed Page](page-defs-coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p/items/properties/c")                                   |
| [l](#l)  | `array` | Required | cannot be null | [Printed Page](page-properties-r-items-properties-p-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p/items/properties/l") |

## c

Coordinates of bounding-box, following IIIF regions schema (\[x, y, width, height] or \[HPOS, VPOS, WIDTH, HEIGHT]).

`c`

* is optional

* Type: `integer[]`

* cannot be null

* defined in: [Printed Page](page-defs-coordinates.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p/items/properties/c")

### c Type

`integer[]`

### c Constraints

**maximum number of items**: the maximum number of items for this array is: `4`

**minimum number of items**: the minimum number of items for this array is: `4`

## l

Lines of text (belonging to a given paragraph)

`l`

* is required

* Type: `object[]` ([Details](page-properties-r-items-properties-p-items-properties-l-items.md))

* cannot be null

* defined in: [Printed Page](page-properties-r-items-properties-p-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p/items/properties/l")

### l Type

`object[]` ([Details](page-properties-r-items-properties-p-items-properties-l-items.md))
