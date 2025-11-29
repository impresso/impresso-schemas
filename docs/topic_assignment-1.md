## Untitled object in undefined Type

`object` ([Details](topic_assignment-1.md))

# Untitled object in undefined Properties

| Property                              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                     |
| :------------------------------------ | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ci\_id](#ci_id)                      | `string`  | Required | cannot be null | [Untitled schema](topic_assignment-1-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/ci_id")                     |
| [ts](#ts)                             | `string`  | Optional | cannot be null | [Untitled schema](topic_assignment-1-properties-the-ts-schema.md "#/properties/ts#/properties/ts")                                                                                             |
| [lg](#lg)                             | `string`  | Required | cannot be null | [Untitled schema](topic_assignment-1-properties-lg.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/lg")                           |
| [topic\_model\_id](#topic_model_id)   | `string`  | Required | cannot be null | [Untitled schema](topic_assignment-1-properties-topic_model_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topic_model_id")   |
| [model\_id](#model_id)                | `string`  | Optional | cannot be null | [Untitled schema](topic_assignment-1-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/model_id")               |
| [topics\_git](#topics_git)            | `string`  | Optional | cannot be null | [Untitled schema](topic_assignment-1-properties-topics_git.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topics_git")           |
| [topic\_count](#topic_count)          | `integer` | Required | cannot be null | [Untitled schema](topic_assignment-1-properties-topic_count.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topic_count")         |
| [min\_p](#min_p)                      | `number`  | Optional | cannot be null | [Untitled schema](topic_assignment-1-properties-min_p.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/min_p")                     |
| [topics](#topics)                     | `array`   | Required | cannot be null | [Untitled schema](topic_assignment-1-properties-topics.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topics")                   |
| [lingproc\_run\_id](#lingproc_run_id) | `string`  | Optional | cannot be null | [Untitled schema](topic_assignment-1-properties-lingproc_run_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/lingproc_run_id") |
| [topics\_run\_id](#topics_run_id)     | `string`  | Optional | cannot be null | [Untitled schema](topic_assignment-1-properties-topics_run_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topics_run_id")     |

## ci\_id

Unique identifier for the content item.

`ci_id`

* is required

* Type: `string`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/ci_id")

### ci\_id Type

`string`

### ci\_id Examples

```json
"actionfem-1940-01-08-a-i0001"
```

## ts

timestamp

`ts`

* is optional

* Type: `string` ([The Ts Schema](topic_assignment-1-properties-the-ts-schema.md))

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-the-ts-schema.md "#/properties/ts#/properties/ts")

### ts Type

`string` ([The Ts Schema](topic_assignment-1-properties-the-ts-schema.md))

### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

## lg

<https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes>

`lg`

* is required

* Type: `string`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-lg.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/lg")

### lg Type

`string`

## topic\_model\_id

internal symbolic name of the model corresponding to actual model file stems and the topic names in property 't', starts with tm

`topic_model_id`

* is required

* Type: `string`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-topic_model_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topic_model_id")

### topic\_model\_id Type

`string`

## model\_id

impresso internal symbolic name of the model as part of the s3 file path

`model_id`

* is optional

* Type: `string`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/model_id")

### model\_id Type

`string`

## topics\_git

git describe of the repository code used to generate the topics

`topics_git`

* is optional

* Type: `string`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-topics_git.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topics_git")

### topics\_git Type

`string`

## topic\_count

The overall number of topics in the topic model

`topic_count`

* is required

* Type: `integer`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-topic_count.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topic_count")

### topic\_count Type

`integer`

## min\_p

The minimum proportion threshold of a topic in the document to be included in the output.

`min_p`

* is optional

* Type: `number`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-min_p.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/min_p")

### min\_p Type

`number`

### min\_p Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## topics

Sparse representation of topics

`topics`

* is required

* Type: `object[]` ([Details](topic_assignment-1-properties-topics-items.md))

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-topics.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topics")

### topics Type

`object[]` ([Details](topic_assignment-1-properties-topics-items.md))

## lingproc\_run\_id

The impresso s3 run id name of the lingproc input data for traceability.

`lingproc_run_id`

* is optional

* Type: `string`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-lingproc_run_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/lingproc_run_id")

### lingproc\_run\_id Type

`string`

## topics\_run\_id

The impresso s3 run id name of the topic processing that created this data.

`topics_run_id`

* is optional

* Type: `string`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-properties-topics_run_id.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/properties/topics_run_id")

### topics\_run\_id Type

`string`

# Untitled object in undefined Definitions

## Definitions group topic

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/definitions/topic"}
```

| Property | Type     | Required | Nullable       | Defined by                                                                                                                                                                                             |
| :------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [p](#p)  | `number` | Required | cannot be null | [Untitled schema](topic_assignment-1-definitions-topic-properties-p.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/definitions/topic/properties/p") |
| [t](#t)  | Multiple | Required | cannot be null | [Untitled schema](topic_assignment-1-definitions-topic-properties-t.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/definitions/topic/properties/t") |

### p

Probability or proportion of topic

`p`

* is required

* Type: `number`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-definitions-topic-properties-p.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/definitions/topic/properties/p")

#### p Type

`number`

#### p Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

### t

Topic id

`t`

* is required

* Type: any of the following: `integer` or `string` ([Details](topic_assignment-1-definitions-topic-properties-t.md))

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-definitions-topic-properties-t.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/definitions/topic/properties/t")

#### t Type

any of the following: `integer` or `string` ([Details](topic_assignment-1-definitions-topic-properties-t.md))
