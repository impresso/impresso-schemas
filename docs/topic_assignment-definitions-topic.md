# Untitled object in undefined Schema

```txt
https://impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic
```

The probability/proportion of a topic in the document


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                   |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [topic_assignment.schema.json\*](../out/topic_assignment.schema.json "open original schema") |

## topic Type

`object` ([Details](topic_assignment-definitions-topic.md))

# undefined Properties

| Property | Type     | Required | Nullable       | Defined by                                                                                                                                                                                             |
| :------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [p](#p)  | `number` | Required | cannot be null | [Untitled schema](topic_assignment-definitions-topic-properties-p.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic/properties/p") |
| [t](#t)  | Multiple | Required | cannot be null | [Untitled schema](topic_assignment-definitions-topic-properties-t.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic/properties/t") |

## p

Probability or proportion of topic


`p`

-   is required
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](topic_assignment-definitions-topic-properties-p.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic/properties/p")

### p Type

`number`

### p Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## t

Topic id 


`t`

-   is required
-   Type: any of the folllowing: `integer` or `string` ([Details](topic_assignment-definitions-topic-properties-t.md))
-   cannot be null
-   defined in: [Untitled schema](topic_assignment-definitions-topic-properties-t.md "https&#x3A;//impresso.github.io/impresso-schemas/json/topic_model/topic_assignment.schema.json#/definitions/topic/properties/t")

### t Type

any of the folllowing: `integer` or `string` ([Details](topic_assignment-definitions-topic-properties-t.md))
