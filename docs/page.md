## Newspaper Page Type

`object` ([Newspaper Page](page.md))

# Newspaper Page Properties

| Property                                   | Type      | Required | Nullable       | Defined by                                                                                                                                                         |
| :----------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                  | `string`  | Required | cannot be null | [Newspaper Page](page-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/id")                               |
| [iiif](#iiif)                              | `string`  | Optional | cannot be null | [Newspaper Page](page-properties-iiif.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/iiif")                           |
| [iiif\_img\_base\_uri](#iiif_img_base_uri) | `string`  | Optional | cannot be null | [Newspaper Page](page-properties-iiif_img_base_uri.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/iiif_img_base_uri") |
| [fw](#fw)                                  | `integer` | Optional | cannot be null | [Newspaper Page](page-properties-fw.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/fw")                               |
| [fh](#fh)                                  | `integer` | Optional | cannot be null | [Newspaper Page](page-properties-fh.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/fh")                               |
| [cc](#cc)                                  | `boolean` | Optional | cannot be null | [Newspaper Page](page-properties-cc.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/cc")                               |
| [cdt](#cdt)                                | `string`  | Required | cannot be null | [Newspaper Page](page-properties-cdt.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/cdt")                             |
| [r](#r)                                    | `array`   | Required | cannot be null | [Newspaper Page](page-properties-r.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r")                                 |

## id

Canonical ID of the newspaper page (e.g. GDL-1900-01-02-a-p0001)

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Page](page-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/id")

### id Type

`string`

## iiif

URI of the IIIF Manifest of the newspaper page image. Deprecated in favor of `iiif_img_base_uri` which should be used whenever it's defined, kept for backwards compatibility.

`iiif`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Page](page-properties-iiif.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/iiif")

### iiif Type

`string`

## iiif\_img\_base\_uri

Base of the IIIF image URI of the newspaper page image. Should follow format `{scheme}://{server}/{prefix}/{identifier}` and not include any suffix.

`iiif_img_base_uri`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Page](page-properties-iiif_img_base_uri.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/iiif_img_base_uri")

### iiif\_img\_base\_uri Type

`string`

## fw

Width in pixels of the facsimile corresponding to this page.

`fw`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Newspaper Page](page-properties-fw.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/fw")

### fw Type

`integer`

## fh

Height in pixels of the facsimile corresponding to this page.

`fh`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Newspaper Page](page-properties-fh.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/fh")

### fh Type

`integer`

## cc

Flag indicating whether the legacy coordinates have been converted into IIIF-compliant ones.

`cc`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Newspaper Page](page-properties-cc.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/cc")

### cc Type

`boolean`

## cdt

Creation date timestamp (of the JSON file).

`cdt`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Newspaper Page](page-properties-cdt.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/cdt")

### cdt Type

`string`

## r

Page regions.

`r`

*   is required

*   Type: `object[]` ([Details](page-properties-r-items.md))

*   cannot be null

*   defined in: [Newspaper Page](page-properties-r.md "https://impresso.github.io/impresso-schemas/json/newspaper/page.schema.json#/properties/r")

### r Type

`object[]` ([Details](page-properties-r-items.md))
