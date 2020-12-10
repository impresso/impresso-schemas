# Untitled object in Newspaper Issue Schema

```txt
https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s/items
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [issue.schema.json\*](../out/issue.schema.json "open original schema") |

## items Type

`object` ([Details](issue-properties-s-items.md))

# undefined Properties

| Property    | Type      | Required | Nullable       | Defined by                                                                                                                                                                           |
| :---------- | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rgb](#rgb) | `array`   | Optional | cannot be null | [Newspaper Issue](issue-properties-s-items-properties-rgb.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s/items/properties/rgb") |
| [f](#f)     | `string`  | Optional | cannot be null | [Newspaper Issue](issue-properties-s-items-properties-f.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s/items/properties/f")     |
| [fs](#fs)   | `number`  | Optional | cannot be null | [Newspaper Issue](issue-properties-s-items-properties-fs.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s/items/properties/fs")   |
| [id](#id)   | `integer` | Required | cannot be null | [Newspaper Issue](issue-properties-s-items-properties-id.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s/items/properties/id")   |

## rgb

Color of the text (in RGB).


`rgb`

-   is optional
-   Type: `integer[]`
-   cannot be null
-   defined in: [Newspaper Issue](issue-properties-s-items-properties-rgb.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s/items/properties/rgb")

### rgb Type

`integer[]`

### rgb Constraints

**minimum number of items**: the minimum number of items for this array is: `3`

## f

Font name


`f`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Newspaper Issue](issue-properties-s-items-properties-f.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s/items/properties/f")

### f Type

`string`

## fs

Font size


`fs`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Newspaper Issue](issue-properties-s-items-properties-fs.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s/items/properties/fs")

### fs Type

`number`

## id

Local ID of the style


`id`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [Newspaper Issue](issue-properties-s-items-properties-id.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/s/items/properties/id")

### id Type

`integer`
