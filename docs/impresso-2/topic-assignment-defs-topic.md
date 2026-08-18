## topic Type

`object` ([Details](topic-assignment-defs-topic.md))

# topic Properties

| Property | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                 |
| :------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [p](#p)  | `number` | Required | cannot be null | [Topic Assignment v2](topic-assignment-defs-topic-properties-p.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json#/$defs/topic/properties/p") |
| [t](#t)  | Multiple | Required | cannot be null | [Topic Assignment v2](topic-assignment-defs-topic-properties-t.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json#/$defs/topic/properties/t") |

## p

Probability or proportion of topic

`p`

* is required

* Type: `number`

* cannot be null

* defined in: [Topic Assignment v2](topic-assignment-defs-topic-properties-p.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json#/$defs/topic/properties/p")

### p Type

`number`

### p Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## t

Topic id

`t`

* is required

* Type: any of the following: `integer` or `string` ([Details](topic-assignment-defs-topic-properties-t.md))

* cannot be null

* defined in: [Topic Assignment v2](topic-assignment-defs-topic-properties-t.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/topic-model/topic-assignment.v1.schema.json#/$defs/topic/properties/t")

### t Type

any of the following: `integer` or `string` ([Details](topic-assignment-defs-topic-properties-t.md))
