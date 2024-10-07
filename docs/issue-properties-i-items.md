## items Type

`object` ([Details](issue-properties-i-items.md))

# items Properties

| Property | Type     | Required | Nullable       | Defined by                                                                                                                                                                  |
| :------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [m](#m)  | `object` | Required | cannot be null | [Newspaper Issue](issue-definitions-metadata.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/i/items/properties/m")            |
| [c](#c)  | `array`  | Optional | cannot be null | [Newspaper Issue](issue-properties-i-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/i/items/properties/c") |

## m

Metadata about the content item.

`m`

*   is required

*   Type: `object` ([Details](issue-definitions-metadata.md))

*   cannot be null

*   defined in: [Newspaper Issue](issue-definitions-metadata.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/i/items/properties/m")

### m Type

`object` ([Details](issue-definitions-metadata.md))

## c

Coordinates of image-region corresponding to the content-item depending on its type (if `tp == image`).

`c`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Newspaper Issue](issue-properties-i-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/i/items/properties/c")

### c Type

`integer[]`

### c Constraints

**minimum number of items**: the minimum number of items for this array is: `4`
