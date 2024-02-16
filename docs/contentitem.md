## Content Item Type

`object` ([Content Item](contentitem.md))

# Content Item Properties

| Property        | Type      | Required | Nullable       | Defined by                                                                                                                                             |
| :-------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)       | `string`  | Required | cannot be null | [Content Item](contentitem-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/id")       |
| [s3v](#s3v)     | `string`  | Optional | cannot be null | [Content Item](contentitem-properties-s3v.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/s3v")     |
| [tp](#tp)       | `string`  | Required | cannot be null | [Content Item](contentitem-properties-tp.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/tp")       |
| [cc](#cc)       | `boolean` | Optional | cannot be null | [Content Item](contentitem-properties-cc.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/cc")       |
| [olr](#olr)     | `boolean` | Required | cannot be null | [Content Item](contentitem-properties-olr.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/olr")     |
| [pp](#pp)       | `array`   | Optional | cannot be null | [Content Item](contentitem-properties-pp.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/pp")       |
| [d](#d)         | `string`  | Optional | cannot be null | [Content Item](contentitem-properties-d.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/d")         |
| [ts](#ts)       | `string`  | Required | cannot be null | [Content Item](contentitem-properties-ts.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/ts")       |
| [lg](#lg)       | `string`  | Optional | cannot be null | [Content Item](contentitem-properties-lg.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/lg")       |
| [ft](#ft)       | `string`  | Optional | cannot be null | [Content Item](contentitem-properties-ft.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/ft")       |
| [lb](#lb)       | `array`   | Optional | cannot be null | [Content Item](contentitem-properties-lb.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/lb")       |
| [pb](#pb)       | `array`   | Optional | cannot be null | [Content Item](contentitem-properties-pb.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/pb")       |
| [rb](#rb)       | `array`   | Optional | cannot be null | [Content Item](contentitem-properties-rb.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/rb")       |
| [ppreb](#ppreb) | `array`   | Optional | cannot be null | [Content Item](contentitem-properties-ppreb.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/ppreb") |

## id

The unique identifier for a content item (CI)

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-id.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/id")

### id Type

`string`

## s3v

S3 version ID of the corresponding issue.json file

`s3v`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-s3v.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/s3v")

### s3v Type

`string`

## tp

content item type (e.g. 'ar' for article, 'ad' for advertisement)

`tp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-tp.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/tp")

### tp Type

`string`

## cc

True if image box coordinates are known to be correct, False otherwise

`cc`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-cc.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/cc")

### cc Type

`boolean`

## olr

True if optical layout recognition was applied to the issue this content item originates from.

`olr`

*   is required

*   Type: `boolean`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-olr.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/olr")

### olr Type

`boolean`

## pp

array of page numbers over which the CI spans; it's the physical page number issue-based, as we get it from the OCR.

`pp`

*   is optional

*   Type: `number[]`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-pp.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/pp")

### pp Type

`number[]`

### pp Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## d

issue date (yyyy-mm-dd)

`d`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-d.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/d")

### d Type

`string`

### d Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7D%24 "try regular expression with regexr.com")

## ts

timestamp of creation of the JSON file (e.g. '2018-09-18T08:00:08Z')

`ts`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-ts.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/ts")

### ts Type

`string`

### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

## lg

two letter language code

`lg`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-lg.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/lg")

### lg Type

`string`

### lg Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-z]{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%7D%24 "try regular expression with regexr.com")

## ft

the rebuilt fulltext

`ft`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-ft.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/ft")

### ft Type

`string`

## lb

text offsets of physical line breaks (relative to 'ft' field)

`lb`

*   is optional

*   Type: `number[]`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-lb.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/lb")

### lb Type

`number[]`

## pb

text offsets of physical paragraph breaks  (relative to 'ft' field)

`pb`

*   is optional

*   Type: `number[]`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-pb.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/pb")

### pb Type

`number[]`

## rb

text offsets of page regions (relative to 'ft' field)

`rb`

*   is optional

*   Type: `number[]`

*   cannot be null

*   defined in: [Content Item](contentitem-properties-rb.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/rb")

### rb Type

`number[]`

## ppreb

a list of rebuilt pages

`ppreb`

*   is optional

*   Type: `object[]` ([Details](contentitem-properties-ppreb-items.md))

*   cannot be null

*   defined in: [Content Item](contentitem-properties-ppreb.md "https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/ppreb")

### ppreb Type

`object[]` ([Details](contentitem-properties-ppreb-items.md))
