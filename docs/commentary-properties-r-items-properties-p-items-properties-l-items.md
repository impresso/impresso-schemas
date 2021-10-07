## items Type

`object` ([Details](commentary-properties-r-items-properties-p-items-properties-l-items.md))

# items Properties

| Property | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                    |
| :------- | :------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [c](#c)  | `array` | Required | cannot be null | [Commmentary Page](commentary-properties-r-items-properties-p-items-properties-l-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/c") |
| [t](#t)  | `array` | Required | cannot be null | [Commmentary Page](commentary-properties-r-items-properties-p-items-properties-l-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t") |

## c

Coordinates of image-region.

`c`

*   is required

*   Type: `integer[]`

*   cannot be null

*   defined in: [Commmentary Page](commentary-properties-r-items-properties-p-items-properties-l-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/c")

### c Type

`integer[]`

### c Constraints

**minimum number of items**: the minimum number of items for this array is: `4`

## t

Tokens (as detected by the OCR engine).

`t`

*   is required

*   Type: `object[]` ([Details](commentary-properties-r-items-properties-p-items-properties-l-items-properties-t-items.md))

*   cannot be null

*   defined in: [Commmentary Page](commentary-properties-r-items-properties-p-items-properties-l-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/commentary/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t")

### t Type

`object[]` ([Details](commentary-properties-r-items-properties-p-items-properties-l-items-properties-t-items.md))
