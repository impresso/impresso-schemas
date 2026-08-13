## Printed Page Type

`object` ([Printed Page](page.md))

all of

* one (and only one) of

  * [Untitled undefined type in Printed Page](page-allof-0-oneof-0.md "check type definition")

  * [Untitled undefined type in Printed Page](page-allof-0-oneof-1.md "check type definition")

* any of

  * [Untitled undefined type in Printed Page](page-allof-1-anyof-0.md "check type definition")

  * [Untitled undefined type in Printed Page](page-allof-1-anyof-1.md "check type definition")

* [Untitled undefined type in Printed Page](page-allof-2.md "check type definition")

* [Untitled undefined type in Printed Page](page-allof-3.md "check type definition")

# Printed Page Properties

| Property                                   | Type      | Required | Nullable       | Defined by                                                                                                                                                       |
| :----------------------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                  | `string`  | Required | cannot be null | [Printed Page](page-properties-id.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/id")                               |
| [iiif](#iiif)                              | `string`  | Optional | cannot be null | [Printed Page](page-properties-iiif.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/iiif")                           |
| [iiif\_img\_base\_uri](#iiif_img_base_uri) | `string`  | Optional | cannot be null | [Printed Page](page-properties-iiif_img_base_uri.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/iiif_img_base_uri") |
| [fw](#fw)                                  | `integer` | Optional | cannot be null | [Printed Page](page-properties-fw.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/fw")                               |
| [fh](#fh)                                  | `integer` | Optional | cannot be null | [Printed Page](page-properties-fh.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/fh")                               |
| [st](#st)                                  | `string`  | Optional | cannot be null | [Printed Page](page-properties-st.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/st")                               |
| [sm](#sm)                                  | `string`  | Optional | cannot be null | [Printed Page](page-properties-sm.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/sm")                               |
| [cc](#cc)                                  | `boolean` | Optional | cannot be null | [Printed Page](page-properties-cc.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/cc")                               |
| [cdt](#cdt)                                | `string`  | Optional | cannot be null | [Printed Page](page-properties-cdt.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/cdt")                             |
| [ts](#ts)                                  | `string`  | Optional | cannot be null | [Printed Page](page-properties-ts.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/ts")                               |
| [r](#r)                                    | `array`   | Required | cannot be null | [Printed Page](page-properties-r.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r")                                 |

## id

Canonical ID of the newspaper or typescript page (e.g. GDL-1900-01-02-a-p0001, or SOC\_CJ-1940-07-22-a-p0001)

`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Printed Page](page-properties-id.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/id")

### id Type

`string`

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-p[0-9]{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z%5D%5BA-Za-z0-9_%5D*-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C2%7D-p%5B0-9%5D%7B4%7D%24 "try regular expression with regexr.com")

## iiif

URI of the IIIF Manifest of the newspaper page image. Deprecated in favor of `iiif_img_base_uri` which should be used whenever it's defined, kept for backwards compatibility.

`iiif`

* is optional

* Type: `string`

* cannot be null

* defined in: [Printed Page](page-properties-iiif.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/iiif")

### iiif Type

`string`

## iiif\_img\_base\_uri

Base of the IIIF image URI of the newspaper page image. Should follow format `{scheme}://{server}/{prefix}/{identifier}` and not include any suffix.

`iiif_img_base_uri`

* is optional

* Type: `string`

* cannot be null

* defined in: [Printed Page](page-properties-iiif_img_base_uri.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/iiif_img_base_uri")

### iiif\_img\_base\_uri Type

`string`

## fw

Width in pixels of the facsimile corresponding to this page.

`fw`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Printed Page](page-properties-fw.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/fw")

### fw Type

`integer`

## fh

Height in pixels of the facsimile corresponding to this page.

`fh`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Printed Page](page-properties-fh.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/fh")

### fh Type

`integer`

## st

Type of media source. Should be a value the impresso-essentials.utils SourceType enum.

`st`

* is optional

* Type: `string`

* cannot be null

* defined in: [Printed Page](page-properties-st.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/st")

### st Type

`string`

### st Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"newspaper"`       |             |
| `"radio_broadcast"` |             |
| `"radio_magazine"`  |             |
| `"radio_schedule"`  |             |
| `"monograph"`       |             |
| `"encyclopedia"`    |             |

## sm

Source medium, format in which the media was originally produced. If `tp == radio_broadcast`, this is typically `typescript` or `audio`.

`sm`

* is optional

* Type: `string`

* cannot be null

* defined in: [Printed Page](page-properties-sm.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/sm")

### sm Type

`string`

### sm Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"print"`      |             |
| `"typescript"` |             |

## cc

Flag indicating whether the legacy coordinates have been converted into IIIF-compliant ones (or rescaled if there was the need).

`cc`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Printed Page](page-properties-cc.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/cc")

### cc Type

`boolean`

## cdt

Creation date timestamp (of the JSON file).

`cdt`

* is optional

* Type: `string`

* cannot be null

* defined in: [Printed Page](page-properties-cdt.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/cdt")

### cdt Type

`string`

## ts

Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format).

`ts`

* is optional

* Type: `string`

* cannot be null

* defined in: [Printed Page](page-properties-ts.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/ts")

### ts Type

`string`

## r

Page regions.

`r`

* is required

* Type: `object[]` ([Details](page-properties-r-items.md))

* cannot be null

* defined in: [Printed Page](page-properties-r.md "https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/properties/r")

### r Type

`object[]` ([Details](page-properties-r-items.md))

# Printed Page Definitions

## Definitions group coordinates

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json#/$defs/coordinates"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
