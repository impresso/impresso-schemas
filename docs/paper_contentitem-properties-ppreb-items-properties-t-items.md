## items Type

`object` ([Details](paper_contentitem-properties-ppreb-items-properties-t-items.md))

# items Properties

| Property | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                         |
| :------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [c](#c)  | `array`   | Optional | cannot be null | [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-t-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/t/items/properties/c") |
| [s](#s)  | `integer` | Optional | cannot be null | [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-t-items-properties-s.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/t/items/properties/s") |
| [l](#l)  | `integer` | Optional | cannot be null | [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-t-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/t/items/properties/l") |

## c

Coordinates of token relative to page.

`c`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-t-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/t/items/properties/c")

### c Type

`integer[]`

### c Constraints

**maximum number of items**: the maximum number of items for this array is: `4`

**minimum number of items**: the minimum number of items for this array is: `4`

## s

offset start (relative to ft field)

`s`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-t-items-properties-s.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/t/items/properties/s")

### s Type

`integer`

## l

token length

`l`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-t-items-properties-l.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/t/items/properties/l")

### l Type

`integer`
