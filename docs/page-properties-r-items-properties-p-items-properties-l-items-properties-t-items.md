# Untitled object in Newspaper Page Schema

```txt
https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [page.schema.json\*](../out/page.schema.json "open original schema") |

## items Type

`object` ([Details](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items.md))

# undefined Properties

| Property  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                        |
| :-------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [c](#c)   | `array`   | Required | cannot be null | [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-c.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/c")   |
| [tx](#tx) | `string`  | Required | cannot be null | [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-tx.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/tx") |
| [s](#s)   | `integer` | Optional | cannot be null | [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-s.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/s")   |
| [gn](#gn) | `boolean` | Optional | cannot be null | [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-gn.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/gn") |
| [hy](#hy) | `boolean` | Optional | cannot be null | [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-hy.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/hy") |
| [nf](#nf) | `string`  | Optional | cannot be null | [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-nf.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/nf") |

## c

Coordinates of image-region.


`c`

-   is required
-   Type: `integer[]`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-c.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/c")

### c Type

`integer[]`

### c Constraints

**minimum number of items**: the minimum number of items for this array is: `4`

## tx

Token surface form.


`tx`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-tx.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/tx")

### tx Type

`string`

## s

A style ID as defined in issue.schema.json/s


`s`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-s.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/s")

### s Type

`integer`

## gn

Indicates whether the token is/should be followed by a whitespace. `gn==true` means no white space is required (`gn` stands for 'glue next'). When not specified it is assumed to be `false`.


`gn`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-gn.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/gn")

### gn Type

`boolean`

## hy

Indicates whether the token constitutes the former part of a hyphenated word (including hyphen). When not specified it is assumed to be `false`.


`hy`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-hy.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/hy")

### hy Type

`boolean`

## nf

It is specified on the latter part(s) of a hyphenated word, and contains its normalized (dehyphenated) form.


`nf`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-r-items-properties-p-items-properties-l-items-properties-t-items-properties-nf.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r/items/properties/p/items/properties/l/items/properties/t/items/properties/nf")

### nf Type

`string`
