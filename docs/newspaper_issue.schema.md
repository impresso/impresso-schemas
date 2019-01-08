
#  Schema

```
IssueSchema
```


| Abstract | Extensible | Status | Identifiable | Custom Properties | Additional Properties | Defined In |
|----------|------------|--------|--------------|-------------------|-----------------------|------------|
| Can be instantiated | Yes | Experimental | No | Forbidden | Permitted |  |

#  Properties

| Property | Type | Required | Defined by |
|----------|------|----------|------------|
| [cdt](#cdt) | `string` | **Required** |  (this schema) |
| [i](#i) | reference | **Required** |  (this schema) |
| [id](#id) | `string` | **Required** |  (this schema) |
| [pp](#pp) | `string[]` | **Required** |  (this schema) |
| [s](#s) | reference | Optional |  (this schema) |
| `*` | any | Additional | this schema *allows* additional properties |

## cdt

Creation date timestamp (of the JSON file)

`cdt`

* is **required**
* type: `string`
* defined in this schema

### cdt Type


`string`







## i

The content items contained in the newspaper issue

`i`

* is **required**
* type: reference
* defined in this schema

### i Type


Array type: reference

All items must be of the type:
* []() – `#/definitions/item`








## id


`id`

* is **required**
* type: `string`
* defined in this schema

### id Type


`string`







## pp


`pp`

* is **required**
* type: `string[]`
* defined in this schema

### pp Type


Array type: `string[]`

All items must be of the type:
`string`










## s


`s`

* is optional
* type: reference
* defined in this schema

### s Type


Array type: reference

All items must be of the type:
* []() – `#/definitions/style`








#  Definitions

| Property | Type | Group |
|----------|------|-------|
| [f](#f) | `string` | `IssueSchema#/definitions/style` |
| [fs](#fs) | `number` | `IssueSchema#/definitions/style` |
| [l](#l) | `string` | `IssueSchema#/definitions/metadata` |
| [m](#m) | reference | `IssueSchema#/definitions/item` |
| [rgb](#rgb) | reference | `IssueSchema#/definitions/style` |
| [t](#t) | `string` | `IssueSchema#/definitions/metadata` |
| [tp](#tp) | `string` | `IssueSchema#/definitions/metadata` |

## f


`f`

* is optional
* type: `string`
* defined in this schema

### f Type


`string`







## fs


`fs`

* is optional
* type: `number`
* defined in this schema

### fs Type


`number`







## l


`l`

* is optional
* type: `string`
* defined in this schema

### l Type


`string`







## m


`m`

* is optional
* type: reference
* defined in this schema

### m Type


* []() – `#/definitions/metadata`





## rgb


`rgb`

* is optional
* type: reference
* defined in this schema

### rgb Type


* []() – `#/definitions/rgbColor`





## t


`t`

* is optional
* type: `string`
* defined in this schema

### t Type


`string`







## tp


`tp`

* is optional
* type: `string`
* defined in this schema

### tp Type


`string`






