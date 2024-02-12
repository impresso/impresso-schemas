## 0 Type

`object` ([Details](language_identification-properties-votes-items-0.md))

# 0 Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [lang](#lang) | `string` | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-votes-items-0-properties-langiso639type.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/votes/items/0/properties/lang") |
| [vote](#vote) | `number` | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-votes-items-0-properties-vote.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/votes/items/0/properties/vote")           |

## lang

Two- or three-letter ISO language abbreviation, cf. <https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes> or <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>

`lang`

*   is required

*   Type: `string` ([langISO639Type](language_identification-properties-votes-items-0-properties-langiso639type.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-votes-items-0-properties-langiso639type.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/votes/items/0/properties/lang")

### lang Type

`string` ([langISO639Type](language_identification-properties-votes-items-0-properties-langiso639type.md))

### lang Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-z]{2,3}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%2C3%7D%24 "try regular expression with regexr.com")

## vote



`vote`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-votes-items-0-properties-vote.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/votes/items/0/properties/vote")

### vote Type

`number`
