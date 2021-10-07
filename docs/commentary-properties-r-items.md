## items Type

`object` ([Details](commentary-properties-r-items.md))

# items Properties

| Property    | Type     | Required | Nullable       | Defined by                                                                                                                                                                            |
| :---------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [c](#c)     | `array`  | Required | cannot be null | [Commmentary Page](commentary-properties-r-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/c")     |
| [p](#p)     | `array`  | Required | cannot be null | [Commmentary Page](commentary-properties-r-items-properties-p.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/p")     |
| [pOf](#pof) | `string` | Optional | cannot be null | [Commmentary Page](commentary-properties-r-items-properties-pof.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/pOf") |

## c

Coordinates of image-region, following IIIF regions schema (x, y, width, height).

`c`

*   is required

*   Type: `integer[]`

*   cannot be null

*   defined in: [Commmentary Page](commentary-properties-r-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/c")

### c Type

`integer[]`

### c Constraints

**minimum number of items**: the minimum number of items for this array is: `4`

## p

Text paragraphs.

`p`

*   is required

*   Type: `object[]` ([Details](commentary-properties-r-items-properties-p-items.md))

*   cannot be null

*   defined in: [Commmentary Page](commentary-properties-r-items-properties-p.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/p")

### p Type

`object[]` ([Details](commentary-properties-r-items-properties-p-items.md))

## pOf

The canonical ID of the content item to which the page region belongs.

`pOf`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Commmentary Page](commentary-properties-r-items-properties-pof.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/pOf")

### pOf Type

`string`
