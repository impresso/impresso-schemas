# Untitled object in Impresso Language Identification Information Schema

```txt
https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid
```

Predicted language and its probability


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                 |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [language_identification.schema.json\*](../out/language_identification.schema.json "open original schema") |

## lid Type

`object` ([Details](language_identification-definitions-lid.md))

# undefined Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :------------ | -------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [lang](#lang) | `string` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-lid-properties-lang.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/lang") |
| [prob](#prob) | `number` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-lid-properties-prob.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/prob") |

## lang

Two or three letter ISO language abbreviation, cf. <https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes> or <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>


`lang`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-definitions-lid-properties-lang.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/lang")

### lang Type

`string`

### lang Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-z]{2,3}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%2C3%7D%24 "try regular expression with regexr.com")

## prob

Probability of prediction


`prob`

-   is required
-   Type: `number`
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-definitions-lid-properties-prob.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/prob")

### prob Type

`number`

### prob Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`
