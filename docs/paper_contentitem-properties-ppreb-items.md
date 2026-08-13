## items Type

`object` ([Details](paper_contentitem-properties-ppreb-items.md))

# items Properties

| Property  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                     |
| :-------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id) | `string`  | Optional | cannot be null | [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-id.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/id") |
| [n](#n)   | `integer` | Optional | cannot be null | [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-n.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/n")   |
| [t](#t)   | `array`   | Optional | cannot be null | [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/t")   |
| [r](#r)   | `array`   | Optional | cannot be null | [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-r.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/r")   |

## id

Page canonical ID

`id`

* is optional

* Type: `string`

* cannot be null

* defined in: [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-id.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/id")

### id Type

`string`

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z_]+-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-p[0-9]{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z_%5D%2B-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C2%7D-p%5B0-9%5D%7B4%7D%24 "try regular expression with regexr.com")

## n

page number

`n`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-n.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/n")

### n Type

`integer`

## t

List of tokens

`t`

* is optional

* Type: `object[]` ([Details](paper_contentitem-properties-ppreb-items-properties-t-items.md))

* cannot be null

* defined in: [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/t")

### t Type

`object[]` ([Details](paper_contentitem-properties-ppreb-items-properties-t-items.md))

## r

List of region coordinates.

`r`

* is optional

* Type: `integer[][]`

* cannot be null

* defined in: [Paper Content Item](paper_contentitem-properties-ppreb-items-properties-r.md "https://impresso.github.io/impresso-schemas/json/rebuilt/paper_contentitem.schema.json#/properties/ppreb/items/properties/r")

### r Type

`integer[][]`
