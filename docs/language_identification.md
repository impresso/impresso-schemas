# Untitled object in undefined Schema

```txt
https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json
```

A representation for the language identifications of various models per content item.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                               |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------------------------------------------- |
| Can be instantiated | Yes        | Unknown status | No           | Forbidden         | Allowed               | none                | [language_identification.schema.json](../out/language_identification.schema.json "open original schema") |

## Untitled object in undefined Type

`object` ([Details](language_identification.md))

# undefined Properties

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                     |
| :---------------------------------------- | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tp](#tp)                                 | `string`  | Required | cannot be null | [Untitled schema](language_identification-properties-tp.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/tp")                                 |
| [id](#id)                                 | `string`  | Required | cannot be null | [Untitled schema](language_identification-properties-id.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/id")                                 |
| [len](#len)                               | `integer` | Required | cannot be null | [Untitled schema](language_identification-properties-len.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/len")                               |
| [orig_lg](#orig_lg)                       | `string`  | Required | can be null    | [Untitled schema](language_identification-properties-orig_lg.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/orig_lg")                       |
| [alphabetical_ratio](#alphabetical_ratio) | `number`  | Optional | cannot be null | [Untitled schema](language_identification-properties-alphabetical_ratio.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/alphabetical_ratio") |
| [langdetect](#langdetect)                 | `array`   | Optional | cannot be null | [Untitled schema](language_identification-properties-langdetect.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langdetect")                 |
| [langid](#langid)                         | `array`   | Optional | cannot be null | [Untitled schema](language_identification-properties-langid.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langid")                         |
| [impresso_ft](#impresso_ft)               | `array`   | Optional | cannot be null | [Untitled schema](language_identification-properties-impresso_ft.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_ft")               |
| [wp_ft](#wp_ft)                           | `array`   | Optional | cannot be null | [Untitled schema](language_identification-properties-wp_ft.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/wp_ft")                           |

## tp

Type of the content item, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>


`tp`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](language_identification-properties-tp.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/tp")

### tp Type

`string`

## id

Canonical ID of the newspaper issue (e.g. GDL-1900-01-02-a), cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>


`id`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](language_identification-properties-id.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/id")

### id Type

`string`

## len

Length of content item


`len`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](language_identification-properties-len.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/len")

### len Type

`integer`

## orig_lg

Original language of the content item as provided by the meta data, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>


`orig_lg`

-   is required
-   Type: `string`
-   can be null
-   defined in: [Untitled schema](language_identification-properties-orig_lg.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/orig_lg")

### orig_lg Type

`string`

### orig_lg Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-z]{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%7D%24 "try regular expression with regexr.com")

## alphabetical_ratio

Ratio of alphabetical characters (letters) wtr to text length of content item


`alphabetical_ratio`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](language_identification-properties-alphabetical_ratio.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/alphabetical_ratio")

### alphabetical_ratio Type

`number`

## langdetect

List of predicted languages using Langdetect, sorted by probability


`langdetect`

-   is optional
-   Type: `object[]` ([Details](language_identification-properties-langdetect-items.md))
-   cannot be null
-   defined in: [Untitled schema](language_identification-properties-langdetect.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langdetect")

### langdetect Type

`object[]` ([Details](language_identification-properties-langdetect-items.md))

## langid

List of predicted languages using Langid, sorted by probability


`langid`

-   is optional
-   Type: `object[]` ([Details](language_identification-properties-langid-items.md))
-   cannot be null
-   defined in: [Untitled schema](language_identification-properties-langid.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/langid")

### langid Type

`object[]` ([Details](language_identification-properties-langid-items.md))

## impresso_ft

List of predicted languages using a FastText model trained on Impresso articles, sorted by probability


`impresso_ft`

-   is optional
-   Type: `object[]` ([Details](language_identification-properties-impresso_ft-items.md))
-   cannot be null
-   defined in: [Untitled schema](language_identification-properties-impresso_ft.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/impresso_ft")

### impresso_ft Type

`object[]` ([Details](language_identification-properties-impresso_ft-items.md))

## wp_ft

List of predicted languages using a FastText model trained on Wikipedia, sorted by probability


`wp_ft`

-   is optional
-   Type: `object[]` ([Details](language_identification-properties-wp_ft-items.md))
-   cannot be null
-   defined in: [Untitled schema](language_identification-properties-wp_ft.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/wp_ft")

### wp_ft Type

`object[]` ([Details](language_identification-properties-wp_ft-items.md))

# Untitled object in undefined Definitions

## Definitions group lid

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid"}
```

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                         |
| :------------ | -------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [lang](#lang) | `string` | Required | cannot be null | [Untitled schema](language_identification-definitions-lid-properties-lang.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/lang") |
| [prob](#prob) | `number` | Required | cannot be null | [Untitled schema](language_identification-definitions-lid-properties-prob.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/prob") |

### lang

<https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes>


`lang`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](language_identification-definitions-lid-properties-lang.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/lang")

#### lang Type

`string`

#### lang Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-z]{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%7D%24 "try regular expression with regexr.com")

### prob

Probability of prediction


`prob`

-   is required
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](language_identification-definitions-lid-properties-prob.md "https&#x3A;//impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/prob")

#### prob Type

`number`
