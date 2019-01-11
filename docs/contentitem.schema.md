
# Content Item Schema

```
https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json
```

A newspaper content item (e.g. article, advertisement, etc.).

| Abstract | Extensible | Status | Identifiable | Custom Properties | Additional Properties | Defined In |
|----------|------------|--------|--------------|-------------------|-----------------------|------------|
| Can be instantiated | No | Experimental | No | Forbidden | Permitted | [contentitem.schema.json](contentitem.schema.json) |

# Content Item Properties

| Property | Type | Required | Defined by |
|----------|------|----------|------------|
| [cc](#cc) | `boolean` | Optional | Content Item (this schema) |
| [d](#d) | `string` | Optional | Content Item (this schema) |
| [ft](#ft) | `string` | Optional | Content Item (this schema) |
| [id](#id) | `string` | **Required** | Content Item (this schema) |
| [lb](#lb) | `number[]` | Optional | Content Item (this schema) |
| [lg](#lg) | `string` | Optional | Content Item (this schema) |
| [olr](#olr) | `boolean` | Optional | Content Item (this schema) |
| [pb](#pb) | `number[]` | Optional | Content Item (this schema) |
| [pp](#pp) | `number[]` | Optional | Content Item (this schema) |
| [ppreb](#ppreb) | `object[]` | Optional | Content Item (this schema) |
| [rb](#rb) | `number[]` | Optional | Content Item (this schema) |
| [s3v](#s3v) | `string` | Optional | Content Item (this schema) |
| [tp](#tp) | `string` | Optional | Content Item (this schema) |
| [ts](#ts) | `string` | Optional | Content Item (this schema) |
| `*` | any | Additional | this schema *allows* additional properties |

## cc

True if image box coordinates are known to be correct, False otherwise

`cc`

* is optional
* type: `boolean`
* defined in this schema

### cc Type


`boolean`





## d

issue date (yyyy-mm-dd)

`d`

* is optional
* type: `string`
* defined in this schema

### d Type


`string`



All instances must conform to this regular expression 
(test examples [here](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7D%24)):
```regex
^[0-9]{4}-[0-9]{2}-[0-9]{2}$
```






## ft

the rebuilt fulltext

`ft`

* is optional
* type: `string`
* defined in this schema

### ft Type


`string`







## id

The unique identifier for a content item (CI)

`id`

* is **required**
* type: `string`
* defined in this schema

### id Type


`string`







## lb

text offsets of physical line breaks (relative to 'ft' field)

`lb`

* is optional
* type: `number[]`
* defined in this schema

### lb Type


Array type: `number[]`

All items must be of the type:
`number`










## lg

two letter language code

`lg`

* is optional
* type: `string`
* defined in this schema

### lg Type


`string`



All instances must conform to this regular expression 
(test examples [here](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%7D%24)):
```regex
^[a-z]{2}$
```






## olr

True if optical layout recognition was applied to the issue this content item originates from.

`olr`

* is optional
* type: `boolean`
* defined in this schema

### olr Type


`boolean`





## pb

text offsets of physical paragraph breaks  (relative to 'ft' field)

`pb`

* is optional
* type: `number[]`
* defined in this schema

### pb Type


Array type: `number[]`

All items must be of the type:
`number`










## pp

array of page numbers over which the CI spans; it's the physical page number issue-based, as we get it from the OCR.

`pp`

* is optional
* type: `number[]`
* at least `1` items in the array
* defined in this schema

### pp Type


Array type: `number[]`

All items must be of the type:
`number`










## ppreb

a list of rebuilt pages

`ppreb`

* is optional
* type: `object[]`
* defined in this schema

### ppreb Type


Array type: `object[]`

All items must be of the type:
`object` with following properties:


| Property | Type | Required |
|----------|------|----------|
| `id`| string | Optional |
| `n`| number | Optional |
| `t`| array | Optional |



#### id

canonical ID

`id`

* is optional
* type: `string`

##### id Type


`string`









#### n

page number

`n`

* is optional
* type: `number`

##### n Type


`number`









#### t

a list of tokens

`t`

* is optional
* type: `object[]`


##### t Type


Array type: `object[]`

All items must be of the type:
`object` with following properties:


| Property | Type | Required |
|----------|------|----------|
| `c`| array | Optional |
| `l`| number | Optional |
| `s`| number | Optional |



#### c

page coordinates of token

`c`

* is optional
* type: `array`* between `4` and `4` items in the array


##### c Type


Array type: `array`








#### l

token length

`l`

* is optional
* type: `number`

##### l Type


`number`









#### s

offset start (relative to ft field)

`s`

* is optional
* type: `number`

##### s Type


`number`






















## rb

text offsets of page regions (relative to 'ft' field)

`rb`

* is optional
* type: `number[]`
* defined in this schema

### rb Type


Array type: `number[]`

All items must be of the type:
`number`










## s3v

S3 version ID of the corresponding issue.json file

`s3v`

* is optional
* type: `string`
* defined in this schema

### s3v Type


`string`







## tp

content item type (e.g. 'ar' for article, 'ad' for advertisement)

`tp`

* is optional
* type: `string`
* defined in this schema

### tp Type


`string`







## ts

timestamp of creation of the JSON file (e.g. '2018-09-18T08:00:08Z')

`ts`

* is optional
* type: `string`
* defined in this schema

### ts Type


`string`



All instances must conform to this regular expression 
(test examples [here](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24)):
```regex
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```





