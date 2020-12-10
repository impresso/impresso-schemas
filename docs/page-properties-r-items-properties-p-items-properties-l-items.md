# Untitled object in Newspaper Page Schema

```txt
https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [page.schema.json\*](../out/page.schema.json "open original schema") |

## items Type

`object` ([Details](page-properties-r-items-properties-p-items-properties-l-items.md))

# undefined Properties

| Property | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :------- | ------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [c](#c)  | `array` | Required | cannot be null | [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-c.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/c") |
| [t](#t)  | `array` | Required | cannot be null | [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t") |

## c

Coordinates of image-region.


`c`

-   is required
-   Type: `integer[]`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-c.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/c")

### c Type

`integer[]`

### c Constraints

**minimum number of items**: the minimum number of items for this array is: `4`

## t

Tokens (as detected by the OCR engine).


`t`

-   is required
-   Type: `object[]` ([Details](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items.md))
-   cannot be null
-   defined in: [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t")

### t Type

`object[]` ([Details](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items.md))
