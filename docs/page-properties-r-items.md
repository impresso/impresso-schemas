## items Type

`object` ([Details](page-properties-r-items.md))

# items Properties

| Property    | Type     | Required | Nullable       | Defined by                                                                                                                                                                 |
| :---------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [c](#c)     | `array`  | Required | cannot be null | [Printed Page](page-properties-r-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/c")     |
| [p](#p)     | `array`  | Required | cannot be null | [Printed Page](page-properties-r-items-properties-p.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p")     |
| [pOf](#pof) | `string` | Optional | can be null    | [Printed Page](page-properties-r-items-properties-pof.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/pOf") |

## c

Coordinates of bounding-box, following IIIF regions schema (\[x, y, width, height] or \[HPOS, VPOS, WIDTH, HEIGHT]).

`c`

* is required

* Type: `integer[]`

* cannot be null

* defined in: [Printed Page](page-properties-r-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/c")

### c Type

`integer[]`

### c Constraints

**maximum number of items**: the maximum number of items for this array is: `4`

**minimum number of items**: the minimum number of items for this array is: `4`

## p

Text paragraphs.

`p`

* is required

* Type: `object[]` ([Details](page-properties-r-items-properties-p-items.md))

* cannot be null

* defined in: [Printed Page](page-properties-r-items-properties-p.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/p")

### p Type

`object[]` ([Details](page-properties-r-items-properties-p-items.md))

## pOf

The canonical ID of the content item to which the page region belongs.

`pOf`

* is optional

* Type: `string`

* can be null

* defined in: [Printed Page](page-properties-r-items-properties-pof.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r/items/properties/pOf")

### pOf Type

`string`
