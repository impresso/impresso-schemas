## lidType Type

`object` ([lidType](language_identification-definitions-lidtype.md))

# lidType Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                   |
| :------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [lang](#lang) | `string` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-lidtype-properties-langiso639type.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lidType/properties/lang") |
| [prob](#prob) | `number` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-lidtype-properties-probtype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lidType/properties/prob")       |

## lang

Two- or three-letter ISO language abbreviation, cf. <https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes> or <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>

`lang`

*   is required

*   Type: `string` ([langISO639Type](language_identification-definitions-lidtype-properties-langiso639type.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-definitions-lidtype-properties-langiso639type.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lidType/properties/lang")

### lang Type

`string` ([langISO639Type](language_identification-definitions-lidtype-properties-langiso639type.md))

### lang Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-z]{2,3}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%2C3%7D%24 "try regular expression with regexr.com")

## prob

Probability of the prediction

`prob`

*   is required

*   Type: `number` ([probType](language_identification-definitions-lidtype-properties-probtype.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-definitions-lidtype-properties-probtype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lidType/properties/prob")

### prob Type

`number` ([probType](language_identification-definitions-lidtype-properties-probtype.md))

### prob Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`
