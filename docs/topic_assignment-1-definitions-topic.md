## topic Type

`object` ([Details](topic_assignment-1-definitions-topic.md))

# topic Properties

| Property | Type     | Required | Nullable       | Defined by                                                                                                                                                                                             |
| :------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [p](#p)  | `number` | Required | cannot be null | [Untitled schema](topic_assignment-1-definitions-topic-properties-p.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/definitions/topic/properties/p") |
| [t](#t)  | Multiple | Required | cannot be null | [Untitled schema](topic_assignment-1-definitions-topic-properties-t.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/definitions/topic/properties/t") |

## p

Probability or proportion of topic

`p`

* is required

* Type: `number`

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-definitions-topic-properties-p.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/definitions/topic/properties/p")

### p Type

`number`

### p Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## t

Topic id

`t`

* is required

* Type: any of the following: `integer` or `string` ([Details](topic_assignment-1-definitions-topic-properties-t.md))

* cannot be null

* defined in: [Untitled schema](topic_assignment-1-definitions-topic-properties-t.md "https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.v2.schema.json#/definitions/topic/properties/t")

### t Type

any of the following: `integer` or `string` ([Details](topic_assignment-1-definitions-topic-properties-t.md))
