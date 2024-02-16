## Impresso Language Identification Information Type

`object` ([Impresso Language Identification Information](language_identification.md))

# Impresso Language Identification Information Properties

| Property                                                                         | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                        |
| :------------------------------------------------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                                                        | `string`  | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-id.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/id")                                            |
| [orig\_lg](#orig_lg)                                                             | Merged    | Required | can be null    | [Impresso Language Identification Information](language_identification-properties-orig_lg.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/orig_lg")                                  |
| [lg](#lg)                                                                        | Merged    | Required | can be null    | [Impresso Language Identification Information](language_identification-properties-lg.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/lg")                                            |
| [lg\_decision](#lg_decision)                                                     | `string`  | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-lg_decision.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/lg_decision")                          |
| [tp](#tp)                                                                        | `string`  | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-tp.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/tp")                                            |
| [len](#len)                                                                      | `integer` | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-len.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/len")                                          |
| [impresso\_language\_identifier\_version](#impresso_language_identifier_version) | `object`  | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-versiontype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_language_identifier_version") |
| [language\_identifier\_version](#language_identifier_version)                    | `object`  | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-versiontype-1.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/language_identifier_version")        |
| [alphabetical\_ratio](#alphabetical_ratio)                                       | `number`  | Optional | can be null    | [Impresso Language Identification Information](language_identification-properties-alphabetical_ratio.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/alphabetical_ratio")            |
| [langdetect](#langdetect)                                                        | `array`   | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-langdetect.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langdetect")                            |
| [langid](#langid)                                                                | `array`   | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-langid.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langid")                                    |
| [impresso\_ft](#impresso_ft)                                                     | `array`   | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-impresso_ft.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_ft")                          |
| [wp\_ft](#wp_ft)                                                                 | `array`   | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-wp_ft.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/wp_ft")                                      |
| [votes](#votes)                                                                  | `array`   | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-votes.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/votes")                                      |

## id

The unique identifier for a content item, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-id.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/id")

### id Type

`string`

## orig\_lg

Original language of the content item as provided by the metadata, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>

`orig_lg`

*   is required

*   Type: `string` ([Details](language_identification-properties-orig_lg.md))

*   can be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-orig_lg.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/orig_lg")

### orig\_lg Type

`string` ([Details](language_identification-properties-orig_lg.md))

one (and only one) of

*   [null](language_identification-properties-orig_lg-oneof-null.md "check type definition")

*   [langISO639Type](language_identification-properties-orig_lg-oneof-langiso639type.md "check type definition")

## lg

Computed language of the content item, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>

`lg`

*   is required

*   Type: `string` ([Details](language_identification-properties-lg.md))

*   can be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-lg.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/lg")

### lg Type

`string` ([Details](language_identification-properties-lg.md))

one (and only one) of

*   [null](language_identification-properties-lg-oneof-null.md "check type definition")

*   [langISO639Type](language_identification-properties-lg-oneof-langiso639type.md "check type definition")

## lg\_decision

An identifier for the decision strategy applied to the content item: 'all' = all LID systems/info agree; 'all-but-impresso-ft' = all LID except impresso\_ft agree on a language other than de/fr; 'dominant-by-len' = the most frequent language of the ensemble decisions is selected because there are too few characters; 'dominant-by-lowvote' = the most frequent language of the ensemble decisions is selected because there are too few votes; 'voting' = the language with the highest vote count is selected

`lg_decision`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-lg_decision.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/lg_decision")

### lg\_decision Type

`string`

### lg\_decision Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation |
| :---------------------- | :---------- |
| `"all"`                 |             |
| `"all-but-impresso-ft"` |             |
| `"voting"`              |             |
| `"dominant-by-len"`     |             |
| `"dominant-by-lowvote"` |             |

## tp

Type of the content item, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>

`tp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-tp.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/tp")

### tp Type

`string`

## len

Number of characters of content item

`len`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-len.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/len")

### len Type

`integer`

### len Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## impresso\_language\_identifier\_version

Administrative information on tool version and data creation time.

`impresso_language_identifier_version`

*   is optional

*   Type: `object` ([versionType](language_identification-properties-versiontype.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-versiontype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_language_identifier_version")

### impresso\_language\_identifier\_version Type

`object` ([versionType](language_identification-properties-versiontype.md))

## language\_identifier\_version

Administrative information on tool version and data creation time.

`language_identifier_version`

*   is optional

*   Type: `object` ([versionType](language_identification-properties-versiontype-1.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-versiontype-1.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/language_identifier_version")

### language\_identifier\_version Type

`object` ([versionType](language_identification-properties-versiontype-1.md))

## alphabetical\_ratio

Ratio of alphabetical characters (Unicode letter class matched by \w) w\.r.t. text length of content item

`alphabetical_ratio`

*   is optional

*   Type: `number`

*   can be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-alphabetical_ratio.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/alphabetical_ratio")

### alphabetical\_ratio Type

`number`

### alphabetical\_ratio Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## langdetect

List of predicted languages using Langdetect, sorted by probability

`langdetect`

*   is optional

*   Type: `object[]` ([lidType](language_identification-properties-langdetect-lidtype.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-langdetect.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langdetect")

### langdetect Type

`object[]` ([lidType](language_identification-properties-langdetect-lidtype.md))

## langid

List of predicted languages using Langid, sorted by probability

`langid`

*   is optional

*   Type: `object[]` ([lidType](language_identification-properties-langid-lidtype.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-langid.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langid")

### langid Type

`object[]` ([lidType](language_identification-properties-langid-lidtype.md))

## impresso\_ft

List of predicted languages using a FastText model trained on Impresso articles, sorted by probability

`impresso_ft`

*   is optional

*   Type: `object[]` ([lidType](language_identification-properties-impresso_ft-lidtype.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-impresso_ft.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_ft")

### impresso\_ft Type

`object[]` ([lidType](language_identification-properties-impresso_ft-lidtype.md))

## wp\_ft

List of predicted languages using a FastText model trained on Wikipedia, sorted by probability

`wp_ft`

*   is optional

*   Type: `object[]` ([lidType](language_identification-properties-wp_ft-lidtype.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-wp_ft.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/wp_ft")

### wp\_ft Type

`object[]` ([lidType](language_identification-properties-wp_ft-lidtype.md))

## votes



`votes`

*   is optional

*   Type: an array where each item follows the corresponding schema in the following list:

    1.  [Untitled object in Impresso Language Identification Information](language_identification-properties-votes-items-0.md "check type definition")

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-properties-votes.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/votes")

### votes Type

an array where each item follows the corresponding schema in the following list:

1.  [Untitled object in Impresso Language Identification Information](language_identification-properties-votes-items-0.md "check type definition")

# Impresso Language Identification Information Definitions

## Definitions group lidType

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lidType"}
```

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                   |
| :------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [lang](#lang) | `string` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-lidtype-properties-langiso639type.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lidType/properties/lang") |
| [prob](#prob) | `number` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-lidtype-properties-probtype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lidType/properties/prob")       |

### lang

Two- or three-letter ISO language abbreviation, cf. <https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes> or <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>

`lang`

*   is required

*   Type: `string` ([langISO639Type](language_identification-definitions-lidtype-properties-langiso639type.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-definitions-lidtype-properties-langiso639type.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lidType/properties/lang")

#### lang Type

`string` ([langISO639Type](language_identification-definitions-lidtype-properties-langiso639type.md))

#### lang Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-z]{2,3}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%2C3%7D%24 "try regular expression with regexr.com")

### prob

Probability of the prediction

`prob`

*   is required

*   Type: `number` ([probType](language_identification-definitions-lidtype-properties-probtype.md))

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-definitions-lidtype-properties-probtype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lidType/properties/prob")

#### prob Type

`number` ([probType](language_identification-definitions-lidtype-properties-probtype.md))

#### prob Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## Definitions group langISO639Type

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/langISO639Type"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group probType

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/probType"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group versionType

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/versionType"}
```

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                               |
| :-------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [versionType](#versiontype) | `string` | Optional | cannot be null | [Impresso Language Identification Information](language_identification-definitions-versiontype-properties-versiontype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/versionType/properties/versionType") |
| [ts](#ts)                   | `string` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-versiontype-properties-ts.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/versionType/properties/ts")                   |

### versionType

Version of tool. Either date or output of command 'git describe'

`versionType`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-definitions-versiontype-properties-versiontype.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/versionType/properties/versionType")

#### versionType Type

`string`

### ts

timestamp of creation of the JSON file (e.g. '2018-09-18T08:00:08+00:00')

`ts`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Impresso Language Identification Information](language_identification-definitions-versiontype-properties-ts.md "https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/versionType/properties/ts")

#### ts Type

`string`

#### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|\+00:00)$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D\(Z%7C%5C%2B00%3A00\)%24 "try regular expression with regexr.com")
