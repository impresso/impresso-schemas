## Untitled object in undefined Type

`object` ([Details](topic_description.md))

# Untitled object in undefined Properties

| Property                                 | Type      | Required | Nullable       | Defined by                                                                                                                                                                                      |
| :--------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [lg](#lg)                                | `string`  | Optional | cannot be null | [Untitled schema](topic_description-properties-lg.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/lg")                               |
| [topic](#topic)                          | `integer` | Required | cannot be null | [Untitled schema](topic_description-properties-topic.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/topic")                         |
| [topic\_model](#topic_model)             | `string`  | Optional | cannot be null | [Untitled schema](topic_description-properties-topic_model.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/topic_model")             |
| [topic\_description](#topic_description) | `string`  | Optional | cannot be null | [Untitled schema](topic_description-properties-topic_description.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/topic_description") |
| [meta](#meta)                            | `string`  | Optional | cannot be null | [Untitled schema](topic_description-properties-meta.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/meta")                           |
| [word\_probs](#word_probs)               | `array`   | Required | cannot be null | [Untitled schema](topic_description-properties-word_probs.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/word_probs")               |

## lg



`lg`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](topic_description-properties-lg.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/lg")

### lg Type

`string`

## topic



`topic`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Untitled schema](topic_description-properties-topic.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/topic")

### topic Type

`integer`

## topic\_model



`topic_model`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](topic_description-properties-topic_model.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/topic_model")

### topic\_model Type

`string`

## topic\_description



`topic_description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](topic_description-properties-topic_description.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/topic_description")

### topic\_description Type

`string`

## meta



`meta`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](topic_description-properties-meta.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/meta")

### meta Type

`string`

## word\_probs



`word_probs`

*   is required

*   Type: `object[]` ([Details](topic_description-properties-word_probs-items.md))

*   cannot be null

*   defined in: [Untitled schema](topic_description-properties-word_probs.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/properties/word_probs")

### word\_probs Type

`object[]` ([Details](topic_description-properties-word_probs-items.md))

# Untitled object in undefined Definitions

## Definitions group word\_prob

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/definitions/word_prob"}
```

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                        |
| :------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [word](#word) | `string` | Required | cannot be null | [Untitled schema](topic_description-definitions-word_prob-properties-word.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/definitions/word_prob/properties/word") |
| [prob](#prob) | `number` | Required | cannot be null | [Untitled schema](topic_description-definitions-word_prob-properties-prob.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/definitions/word_prob/properties/prob") |

### word



`word`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](topic_description-definitions-word_prob-properties-word.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/definitions/word_prob/properties/word")

#### word Type

`string`

### prob



`prob`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](topic_description-definitions-word_prob-properties-prob.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/definitions/word_prob/properties/prob")

#### prob Type

`number`

#### prob Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`
