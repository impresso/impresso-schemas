## impresso\_language\_identifier\_version Type

`object` ([versionType](language_identification-properties-versiontype.md))

# impresso\_language\_identifier\_version Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                               |
| :-------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [versionType](#versiontype) | `string` | Optional | cannot be null | [Impresso Language Identification Information](language_identification-definitions-versiontype-properties-versiontype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/versionType/properties/versionType") |
| [ts](#ts)                   | `string` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-versiontype-properties-ts.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/versionType/properties/ts")                   |

## versionType

Version of tool. Either date or output of command 'git describe'

`versionType`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-definitions-versiontype-properties-versiontype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/versionType/properties/versionType")

### versionType Type

`string`

## ts

timestamp of creation of the JSON file (e.g. '2018-09-18T08:00:08+00:00')

`ts`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-definitions-versiontype-properties-ts.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/versionType/properties/ts")

### ts Type

`string`

### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|\+00:00)$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D\(Z%7C%5C%2B00%3A00\)%24 "try regular expression with regexr.com")
