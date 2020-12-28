## Untitled object in undefined Type

`object` ([Details](topic_assignment.md))

# undefined Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                             |
| :-------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ci_ref](#ci_ref)           | `string`  | Required | cannot be null | [Untitled schema](topic_assignment-properties-ci_ref.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/ci_ref")           |
| [lang](#lang)               | `string`  | Required | cannot be null | [Untitled schema](topic_assignment-properties-lang.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/lang")               |
| [topic_model](#topic_model) | `string`  | Required | cannot be null | [Untitled schema](topic_assignment-properties-topic_model.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/topic_model") |
| [topic_count](#topic_count) | `integer` | Required | cannot be null | [Untitled schema](topic_assignment-properties-topic_count.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/topic_count") |
| [topics](#topics)           | `array`   | Required | cannot be null | [Untitled schema](topic_assignment-properties-topics.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/topics")           |

## ci_ref

Reference to canonical content item id, typically an article


`ci_ref`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](topic_assignment-properties-ci_ref.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/ci_ref")

### ci_ref Type

`string`

## lang

<https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes>


`lang`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](topic_assignment-properties-lang.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/lang")

### lang Type

`string`

## topic_model

internal symbolic name of the model, starts with tm


`topic_model`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](topic_assignment-properties-topic_model.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/topic_model")

### topic_model Type

`string`

## topic_count

The number of topics in the topic model


`topic_count`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](topic_assignment-properties-topic_count.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/topic_count")

### topic_count Type

`integer`

## topics

Sparse representation of topics


`topics`

-   is required
-   Type: `object[]` ([Details](topic_assignment-properties-topics-items.md))
-   cannot be null
-   defined in: [Untitled schema](topic_assignment-properties-topics.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/properties/topics")

### topics Type

`object[]` ([Details](topic_assignment-properties-topics-items.md))

# Untitled object in undefined Definitions

## Definitions group topic

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic"}
```

| Property | Type     | Required | Nullable       | Defined by                                                                                                                                                                                             |
| :------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [p](#p)  | `number` | Required | cannot be null | [Untitled schema](topic_assignment-definitions-topic-properties-p.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic/properties/p") |
| [t](#t)  | Multiple | Required | cannot be null | [Untitled schema](topic_assignment-definitions-topic-properties-t.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic/properties/t") |

### p

Probability or proportion of topic


`p`

-   is required
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](topic_assignment-definitions-topic-properties-p.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic/properties/p")

#### p Type

`number`

#### p Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

### t

Topic id 


`t`

-   is required
-   Type: any of the folllowing: `integer` or `string` ([Details](topic_assignment-definitions-topic-properties-t.md))
-   cannot be null
-   defined in: [Untitled schema](topic_assignment-definitions-topic-properties-t.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic/properties/t")

#### t Type

any of the folllowing: `integer` or `string` ([Details](topic_assignment-definitions-topic-properties-t.md))
