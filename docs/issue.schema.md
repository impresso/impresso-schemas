
# Newspaper Issue Schema

```
issue.schema.json
```


| Abstract | Extensible | Status | Identifiable | Custom Properties | Additional Properties | Defined In |
|----------|------------|--------|--------------|-------------------|-----------------------|------------|
| Can be instantiated | Yes | Experimental | No | Forbidden | Permitted |  |

# Newspaper Issue Properties

| Property | Type | Required | Defined by |
|----------|------|----------|------------|
| [cdt](#cdt) | `string` | **Required** | Newspaper Issue (this schema) |
| [i](#i) | `object[]` | **Required** | Newspaper Issue (this schema) |
| [id](#id) | `string` | **Required** | Newspaper Issue (this schema) |
| [pp](#pp) | `string[]` | **Required** | Newspaper Issue (this schema) |
| [s](#s) | `object[]` | Optional | Newspaper Issue (this schema) |
| `*` | any | Additional | this schema *allows* additional properties |

## cdt

Creation date timestamp (of the JSON file).

`cdt`

* is **required**
* type: `string`
* defined in this schema

### cdt Type


`string`







## i

The content items contained in the newspaper issue.

`i`

* is **required**
* type: `object[]`
* defined in this schema

### i Type


Array type: `object[]`

All items must be of the type:
`object` with following properties:


| Property | Type | Required |
|----------|------|----------|
| `m`|  | **Required** |



#### m

Metadata about the content item.

`m`

* is **required**
* type: reference

##### m Type


* []() – `#/definitions/metadata`






  
A content item (e.g. article, advertisement, etc.)







## id

Canonical ID of the newspaper issue (e.g. GDL-1900-01-02-a-i0001)

`id`

* is **required**
* type: `string`
* defined in this schema

### id Type


`string`







## pp

Canonical IDs of pages in the issue, without file extension (e.g. GDL-1900-01-02-a-p0004).

`pp`

* is **required**
* type: `string[]`
* defined in this schema

### pp Type


Array type: `string[]`

All items must be of the type:
`string`










## s

The text style as defined in the OCR output. 
Each style consists of:
 - a name (`id`)
 - a type-face (`f`)
 - a font-size (`fs`)
 - a color (`rgb`).

`s`

* is optional
* type: `object[]`
* defined in this schema

### s Type


Array type: `object[]`

All items must be of the type:
`object` with following properties:


| Property | Type | Required |
|----------|------|----------|
| `f`| string | Optional |
| `fs`| number | Optional |
| `id`| integer | **Required** |
| `rgb`| array | Optional |



#### f

Font name

`f`

* is optional
* type: `string`

##### f Type


`string`









#### fs

Font size

`fs`

* is optional
* type: `number`

##### fs Type


`number`









#### id

Local ID of the style

`id`

* is **required**
* type: `integer`

##### id Type


`integer`









#### rgb

Color of the text (in RGB).

`rgb`

* is optional
* type: `integer[]`* at least `3` items in the array


##### rgb Type


Array type: `integer[]`

All items must be of the type:
`integer`

















# Newspaper Issue Definitions

| Property | Type | Group |
|----------|------|-------|
| [l](#l) | `string` | `issue.schema.json#/definitions/metadata` |
| [t](#t) | `string` | `issue.schema.json#/definitions/metadata` |
| [tp](#tp) | `enum` | `issue.schema.json#/definitions/metadata` |

## l

Language of the content item.

`l`

* is optional
* type: `string`
* defined in this schema

### l Type


`string`







## t

Title of the content item.

`t`

* is optional
* type: `string`
* defined in this schema

### t Type


`string`







## tp

Type of the content item.

`tp`

* is optional
* type: `enum`
* defined in this schema

The value of this property **must** be equal to one of the [known values below](#tp-known-values).

### tp Known Values
| Value | Description |
|-------|-------------|
| `article` |  |
| `ad` |  |



