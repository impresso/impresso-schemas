# Impresso Language Identification Information Schema

```txt
https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json
```

A representation for informations relevant to impresso's content item language recognition. This defines the output of the following impresso NLP component. <https://github.com/impresso/impresso-language-identification> 


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                               |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------------------------------------------- |
| Can be instantiated | Yes        | Unknown status | No           | Forbidden         | Allowed               | none                | [language_identification.schema.json](../out/language_identification.schema.json "open original schema") |

## Impresso Language Identification Information Type

`object` ([Impresso Language Identification Information](language_identification.md))

# Impresso Language Identification Information Properties

| Property                                                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                      |
| :------------------------------------------------------------ | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                                                     | `string`  | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-id.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/id")                                                     |
| [orig_lg](#orig_lg)                                           | Merged    | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-orig_lg.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/orig_lg")                                           |
| [lg](#lg)                                                     | Merged    | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-lg.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/lg")                                                     |
| [lg_decision](#lg_decision)                                   | `string`  | Optional | can be null    | [Impresso Language Identification Information](language_identification-properties-lg_decision.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/lg_decision")                                   |
| [tp](#tp)                                                     | `string`  | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-tp.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/tp")                                                     |
| [len](#len)                                                   | `integer` | Required | cannot be null | [Impresso Language Identification Information](language_identification-properties-len.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/len")                                                   |
| [impresso_language_identifier](#impresso_language_identifier) | `object`  | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-impresso_language_identifier.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_language_identifier") |
| [language_identifier](#language_identifier)                   | `object`  | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-language_identifier.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/language_identifier")                   |
| [alphabetical_ratio](#alphabetical_ratio)                     | `number`  | Optional | can be null    | [Impresso Language Identification Information](language_identification-properties-alphabetical_ratio.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/alphabetical_ratio")                     |
| [langdetect](#langdetect)                                     | `array`   | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-langdetect.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langdetect")                                     |
| [langid](#langid)                                             | `array`   | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-langid.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langid")                                             |
| [impresso_ft](#impresso_ft)                                   | `array`   | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-impresso_ft.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_ft")                                   |
| [wp_ft](#wp_ft)                                               | `array`   | Optional | cannot be null | [Impresso Language Identification Information](language_identification-properties-wp_ft.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/wp_ft")                                               |

## id

The unique identifier for a content item, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>


`id`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-id.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/id")

### id Type

`string`

## orig_lg

Original language of the content item as provided by the meta data, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>


`orig_lg`

-   is required
-   Type: merged type ([Details](language_identification-properties-orig_lg.md))
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-orig_lg.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/orig_lg")

### orig_lg Type

merged type ([Details](language_identification-properties-orig_lg.md))

one (and only one) of

-   [Untitled null in Impresso Language Identification Information](language_identification-properties-orig_lg-oneof-0.md "check type definition")
-   [Untitled string in Impresso Language Identification Information](language_identification-properties-orig_lg-oneof-1.md "check type definition")

## lg

Computed language of the content item, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>


`lg`

-   is required
-   Type: merged type ([Details](language_identification-properties-lg.md))
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-lg.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/lg")

### lg Type

merged type ([Details](language_identification-properties-lg.md))

one (and only one) of

-   [Untitled null in Impresso Language Identification Information](language_identification-properties-lg-oneof-0.md "check type definition")
-   [Untitled string in Impresso Language Identification Information](language_identification-properties-lg-oneof-1.md "check type definition")

## lg_decision

An identifier for the decision strategy applied to the content item: 'all' 


`lg_decision`

-   is optional
-   Type: `string`
-   can be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-lg_decision.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/lg_decision")

### lg_decision Type

`string`

## tp

Type of the content item, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>


`tp`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-tp.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/tp")

### tp Type

`string`

## len

Number of characters of content item


`len`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-len.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/len")

### len Type

`integer`

### len Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## impresso_language_identifier

Version information of used impresso language identifier script and file creation timestamp


`impresso_language_identifier`

-   is optional
-   Type: `object` ([Details](language_identification-properties-impresso_language_identifier.md))
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-impresso_language_identifier.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_language_identifier")

### impresso_language_identifier Type

`object` ([Details](language_identification-properties-impresso_language_identifier.md))

## language_identifier

Version information of underlying language identifier script and file creation timestamp


`language_identifier`

-   is optional
-   Type: `object` ([Details](language_identification-properties-language_identifier.md))
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-language_identifier.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/language_identifier")

### language_identifier Type

`object` ([Details](language_identification-properties-language_identifier.md))

## alphabetical_ratio

Ratio of alphabetical characters (letters) wtr to text length of content item


`alphabetical_ratio`

-   is optional
-   Type: `number`
-   can be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-alphabetical_ratio.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/alphabetical_ratio")

### alphabetical_ratio Type

`number`

### alphabetical_ratio Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## langdetect

List of predicted languages using Langdetect, sorted by probability


`langdetect`

-   is optional
-   Type: `object[]` ([Details](language_identification-properties-langdetect-items.md))
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-langdetect.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langdetect")

### langdetect Type

`object[]` ([Details](language_identification-properties-langdetect-items.md))

## langid

List of predicted languages using Langid, sorted by probability


`langid`

-   is optional
-   Type: `object[]` ([Details](language_identification-properties-langid-items.md))
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-langid.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langid")

### langid Type

`object[]` ([Details](language_identification-properties-langid-items.md))

## impresso_ft

List of predicted languages using a FastText model trained on Impresso articles, sorted by probability


`impresso_ft`

-   is optional
-   Type: `object[]` ([Details](language_identification-properties-impresso_ft-items.md))
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-impresso_ft.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_ft")

### impresso_ft Type

`object[]` ([Details](language_identification-properties-impresso_ft-items.md))

## wp_ft

List of predicted languages using a FastText model trained on Wikipedia, sorted by probability


`wp_ft`

-   is optional
-   Type: `object[]` ([Details](language_identification-properties-wp_ft-items.md))
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-properties-wp_ft.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/wp_ft")

### wp_ft Type

`object[]` ([Details](language_identification-properties-wp_ft-items.md))

# Impresso Language Identification Information Definitions

## Definitions group lid

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid"}
```

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :------------ | -------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [lang](#lang) | `string` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-lid-properties-lang.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/lang") |
| [prob](#prob) | `number` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-lid-properties-prob.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/prob") |

### lang

Two or three letter ISO language abbreviation, cf. <https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes> or <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>


`lang`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-definitions-lid-properties-lang.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/lang")

#### lang Type

`string`

#### lang Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-z]{2,3}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%2C3%7D%24 "try regular expression with regexr.com")

### prob

Probability of prediction


`prob`

-   is required
-   Type: `number`
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-definitions-lid-properties-prob.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/prob")

#### prob Type

`number`

#### prob Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## Definitions group lang

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lang"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | ---- | -------- | -------- | :--------- |

## Definitions group prob

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/prob"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | ---- | -------- | -------- | :--------- |

## Definitions group version

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/version"}
```

| Property            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                    |
| :------------------ | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [version](#version) | `string` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-version-properties-version.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/version/properties/version") |
| [ts](#ts)           | `string` | Required | cannot be null | [Impresso Language Identification Information](language_identification-definitions-version-properties-ts.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/version/properties/ts")           |

### version

Version of tool. Either date or output of command 'git describe'


`version`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-definitions-version-properties-version.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/version/properties/version")

#### version Type

`string`

### ts

timestamp of creation of the JSON file (e.g. '2018-09-18T08:00:08+')


`ts`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Impresso Language Identification Information](language_identification-definitions-version-properties-ts.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/version/properties/ts")

#### ts Type

`string`

#### ts Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|\+00:00)$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D(Z%7C%5C%2B00%3A00)%24 "try regular expression with regexr.com")
