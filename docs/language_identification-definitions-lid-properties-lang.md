# Untitled string in Impresso Language Identification Information Schema

```txt
https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/definitions/lid/properties/lang
```

Two or three letter ISO language abbreviation, cf. <https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes> or <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                 |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [language_identification.schema.json\*](../out/language_identification.schema.json "open original schema") |

## lang Type

`string`

## lang Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-z]{2,3}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%2C3%7D%24 "try regular expression with regexr.com")
