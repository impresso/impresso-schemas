## word\_prob Type

`object` ([Details](topic_description-defs-word_prob.md))

# word\_prob Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                             |
| :------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [word](#word) | `string` | Required | cannot be null | [Topic Description](topic_description-defs-word_prob-properties-word.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/$defs/word_prob/properties/word") |
| [prob](#prob) | `number` | Required | cannot be null | [Topic Description](topic_description-defs-word_prob-properties-prob.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/$defs/word_prob/properties/prob") |

## word

`word`

* is required

* Type: `string`

* cannot be null

* defined in: [Topic Description](topic_description-defs-word_prob-properties-word.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/$defs/word_prob/properties/word")

### word Type

`string`

## prob

`prob`

* is required

* Type: `number`

* cannot be null

* defined in: [Topic Description](topic_description-defs-word_prob-properties-prob.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_description.schema.json#/$defs/word_prob/properties/prob")

### prob Type

`number`

### prob Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`
