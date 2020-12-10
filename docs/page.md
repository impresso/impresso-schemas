# Newspaper Page Schema

```txt
https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json
```

Physical representation of a newspaper page as recognized by a given OCR engine.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [page.schema.json](../out/page.schema.json "open original schema") |

## Newspaper Page Type

`object` ([Newspaper Page](page.md))

# Newspaper Page Properties

| Property      | Type      | Required | Nullable       | Defined by                                                                                                                                    |
| :------------ | --------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)     | `string`  | Required | cannot be null | [Newspaper Page](page-properties-id.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/id")     |
| [iiif](#iiif) | `string`  | Optional | cannot be null | [Newspaper Page](page-properties-iiif.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/iiif") |
| [cc](#cc)     | `boolean` | Optional | cannot be null | [Newspaper Page](page-properties-cc.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/cc")     |
| [cdt](#cdt)   | `string`  | Required | cannot be null | [Newspaper Page](page-properties-cdt.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/cdt")   |
| [r](#r)       | `array`   | Required | cannot be null | [Newspaper Page](page-properties-r.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r")       |

## id

Canonical ID of the newspaper page (e.g. GDL-1900-01-02-a-p0001)


`id`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-id.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/id")

### id Type

`string`

## iiif

URI of the IIIF Manifest of the newspaper page image.


`iiif`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-iiif.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/iiif")

### iiif Type

`string`

## cc

Flag indicating whether the legacy coordinates have been converted into IIIF-compliant ones.


`cc`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-cc.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/cc")

### cc Type

`boolean`

## cdt

Creation date timestamp (of the JSON file).


`cdt`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Newspaper Page](page-properties-cdt.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/cdt")

### cdt Type

`string`

## r

Page regions.


`r`

-   is required
-   Type: `object[]` ([Details](page-properties-r-items.md))
-   cannot be null
-   defined in: [Newspaper Page](page-properties-r.md "https&#x3A;//impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r")

### r Type

`object[]` ([Details](page-properties-r-items.md))
