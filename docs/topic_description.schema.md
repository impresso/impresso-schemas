
#  Schema

```
https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json
```

A representation for each topic (=probability distribution of words) of a topic model.

| Abstract | Extensible | Status | Identifiable | Custom Properties | Additional Properties | Defined In |
|----------|------------|--------|--------------|-------------------|-----------------------|------------|
| Can be instantiated | Yes | Experimental | No | Forbidden | Permitted | [topic_description.schema.json](topic_description.schema.json) |

#  Properties

| Property | Type | Required | Defined by |
|----------|------|----------|------------|
| [lg](#lg) | `string` | Optional |  (this schema) |
| [meta](#meta) | `string` | Optional |  (this schema) |
| [topic](#topic) | `integer` | **Required** |  (this schema) |
| [topic_description](#topic_description) | `string` | Optional |  (this schema) |
| [topic_model](#topic_model) | `string` | Optional |  (this schema) |
| [word_probs](#word_probs) | reference | **Required** |  (this schema) |
| `*` | any | Additional | this schema *allows* additional properties |

## lg


`lg`

* is optional
* type: `string`
* defined in this schema

### lg Type


`string`







## meta


`meta`

* is optional
* type: `string`
* defined in this schema

### meta Type


`string`







## topic


`topic`

* is **required**
* type: `integer`
* defined in this schema

### topic Type


`integer`







## topic_description


`topic_description`

* is optional
* type: `string`
* defined in this schema

### topic_description Type


`string`







## topic_model


`topic_model`

* is optional
* type: `string`
* defined in this schema

### topic_model Type


`string`







## word_probs


`word_probs`

* is **required**
* type: reference
* defined in this schema

### word_probs Type


Array type: reference

All items must be of the type:
* []() – `#/definitions/word_prob`








#  Definitions

| Property | Type | Group |
|----------|------|-------|
| [prob](#prob) | `number` | `https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/definitions/word_prob` |
| [word](#word) | `string` | `https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/definitions/word_prob` |

## prob


`prob`

* is optional
* type: `number`
* defined in this schema

### prob Type


`number`

* minimum value: `0`
* maximum value: `1`





## word


`word`

* is optional
* type: `string`
* defined in this schema

### word Type


`string`






