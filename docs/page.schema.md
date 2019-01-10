
# Newspaper Page Schema

```
page.schema.json
```


| Abstract | Extensible | Status | Identifiable | Custom Properties | Additional Properties | Defined In |
|----------|------------|--------|--------------|-------------------|-----------------------|------------|
| Can be instantiated | No | Experimental | No | Forbidden | Permitted |  |

# Newspaper Page Properties

| Property | Type | Required | Defined by |
|----------|------|----------|------------|
| [cc](#cc) | `boolean` | Optional | Newspaper Page (this schema) |
| [cdt](#cdt) | `string` | **Required** | Newspaper Page (this schema) |
| [id](#id) | `string` | **Required** | Newspaper Page (this schema) |
| [r](#r) | `object[]` | **Required** | Newspaper Page (this schema) |
| `*` | any | Additional | this schema *allows* additional properties |

## cc

Flag indicating whether the legacy coordinates have been converted into IIIF-compliant ones.

`cc`

* is optional
* type: `boolean`
* defined in this schema

### cc Type


`boolean`





## cdt

Creation date timestamp (of the JSON file).

`cdt`

* is **required**
* type: `string`
* defined in this schema

### cdt Type


`string`







## id

Canonical ID of the newspaper page (e.g. GDL-1900-01-02-a-p0001)

`id`

* is **required**
* type: `string`
* defined in this schema

### id Type


`string`







## r

Page regions.

`r`

* is **required**
* type: `object[]`
* defined in this schema

### r Type


Array type: `object[]`

All items must be of the type:
`object` with following properties:


| Property | Type | Required |
|----------|------|----------|
| `c`| array | **Required** |
| `p`| array | **Required** |
| `pOf`| string | Optional |



#### c

Coordinates of image-region.

`c`

* is **required**
* type: `integer[]`* at least `4` items in the array


##### c Type


Array type: `integer[]`

All items must be of the type:
`integer`












#### p

Text paragraphs.

`p`

* is **required**
* type: `object[]`


##### p Type


Array type: `object[]`

All items must be of the type:
`object` with following properties:


| Property | Type | Required |
|----------|------|----------|
| `l`| array | **Required** |



#### l

Lines of text (belonging to a given paragraph)

`l`

* is **required**
* type: `object[]`


##### l Type


Array type: `object[]`

All items must be of the type:
`object` with following properties:


| Property | Type | Required |
|----------|------|----------|
| `c`| array | **Required** |
| `t`| array | **Required** |



#### c

Coordinates of image-region.

`c`

* is **required**
* type: `integer[]`* at least `4` items in the array


##### c Type


Array type: `integer[]`

All items must be of the type:
`integer`












#### t

Tokens (as detected by the OCR engine).

`t`

* is **required**
* type: `object[]`


##### t Type


Array type: `object[]`

All items must be of the type:
`object` with following properties:


| Property | Type | Required |
|----------|------|----------|
| `c`| array | **Required** |
| `s`| integer | Optional |
| `tx`| string | **Required** |



#### c

Coordinates of image-region.

`c`

* is **required**
* type: `integer[]`* at least `4` items in the array


##### c Type


Array type: `integer[]`

All items must be of the type:
`integer`












#### s

A style ID as defined in issue.schema.json/s

`s`

* is optional
* type: `integer`

##### s Type


`integer`









#### tx

Token surface form.

`tx`

* is **required**
* type: `string`

##### tx Type


`string`
































#### pOf

The canonical ID of the content item to which the page region belongs.

`pOf`

* is optional
* type: `string`

##### pOf Type


`string`









  
Page region.






