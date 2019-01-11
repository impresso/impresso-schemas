
#  Schema

```
https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json
```

A representation for the probabilistic assignments of the topics of a topic model to content items.

| Abstract | Extensible | Status | Identifiable | Custom Properties | Additional Properties | Defined In |
|----------|------------|--------|--------------|-------------------|-----------------------|------------|
| Can be instantiated | Yes | Experimental | No | Forbidden | Permitted | [topic_assignment.schema.json](topic_assignment.schema.json) |

#  Properties

| Property | Type | Required | Defined by |
|----------|------|----------|------------|
| [ci_ref](#ci_ref) | `string` | **Required** |  (this schema) |
| [lang](#lang) | `string` | **Required** |  (this schema) |
| [topic_count](#topic_count) | `integer` | **Required** |  (this schema) |
| [topic_model](#topic_model) | `string` | **Required** |  (this schema) |
| [topics](#topics) | reference | **Required** |  (this schema) |
| `*` | any | Additional | this schema *allows* additional properties |

## ci_ref

Reference to canonical content item id, typically an article

`ci_ref`

* is **required**
* type: `string`
* defined in this schema

### ci_ref Type


`string`







## lang

https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes

`lang`

* is **required**
* type: `string`
* defined in this schema

### lang Type


`string`







## topic_count

The number of topics in the topic model

`topic_count`

* is **required**
* type: `integer`
* defined in this schema

### topic_count Type


`integer`







## topic_model

internal symbolic name of the model, starts with tm

`topic_model`

* is **required**
* type: `string`
* defined in this schema

### topic_model Type


`string`







## topics

Sparse representation of topics

`topics`

* is **required**
* type: reference
* defined in this schema

### topics Type


Array type: reference

All items must be of the type:
* []() – `#/definitions/topic`








#  Definitions

| Property | Type | Group |
|----------|------|-------|
| [p](#p) | `number` | `https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic` |
| [t](#t) | complex | `https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic` |

## p

Probability or proportion of topic

`p`

* is optional
* type: `number`
* defined in this schema

### p Type


`number`

* minimum value: `0`
* maximum value: `1`





## t

Topic id 

`t`

* is optional
* type: complex
* defined in this schema

### t Type

Unknown type `integer,string`.

```json
{
  "type": [
    "integer",
    "string"
  ],
  "description": "Topic id ",
  "definitiongroup": "topic",
  "simpletype": "complex"
}
```




