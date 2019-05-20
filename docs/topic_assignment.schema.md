# Schema

```
https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json
```

A representation for the probabilistic assignments of the topics of a topic model to content items.

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                                   |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | ------------------------------------------------------------ |
| Can be instantiated | Yes        | Experimental | No           | Forbidden         | Permitted             | [topic_assignment.schema.json](topic_assignment.schema.json) |

# Definitions

| Property | Type     | Group                                                                                                          |
| -------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| [p](#p)  | `number` | `https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic` |
| [t](#t)  | multiple | `https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic` |

## p

Probability or proportion of topic

`p`

- is **required**
- type: `number`
- defined in this schema

### p Type

`number`

- minimum value: `0`
- maximum value: `1`

## t

Topic id

`t`

- is **required**
- type: multiple
- defined in this schema

### t Type

Either one of:

- `integer`
- `string`

# Properties

| Property                    | Type      | Required     | Nullable | Defined by                                 |
| --------------------------- | --------- | ------------ | -------- | ------------------------------------------ |
| [ci_ref](#ci_ref)           | `string`  | **Required** | No       | (this schema)                              |
| [lang](#lang)               | `string`  | **Required** | No       | (this schema)                              |
| [topic_count](#topic_count) | `integer` | **Required** | No       | (this schema)                              |
| [topic_model](#topic_model) | `string`  | **Required** | No       | (this schema)                              |
| [topics](#topics)           | reference | **Required** | No       | (this schema)                              |
| `*`                         | any       | Additional   | Yes      | this schema _allows_ additional properties |

## ci_ref

Reference to canonical content item id, typically an article

`ci_ref`

- is **required**
- type: `string`
- defined in this schema

### ci_ref Type

`string`

## lang

https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes

`lang`

- is **required**
- type: `string`
- defined in this schema

### lang Type

`string`

## topic_count

The number of topics in the topic model

`topic_count`

- is **required**
- type: `integer`
- defined in this schema

### topic_count Type

`integer`

## topic_model

internal symbolic name of the model, starts with tm

`topic_model`

- is **required**
- type: `string`
- defined in this schema

### topic_model Type

`string`

## topics

Sparse representation of topics

`topics`

- is **required**
- type: reference
- defined in this schema

### topics Type

Array type: reference

All items must be of the type:

- []() – `#/definitions/topic`
