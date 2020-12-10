# Untitled schema Schema

```txt
https://impresso.github.io/impresso-schemas/json/language_identification/language_identification.schema.json#/properties/orig_lg
```

Original language of the content item as provided by the meta data, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                 |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [language_identification.schema.json\*](../out/language_identification.schema.json "open original schema") |

## orig_lg Type

`string`

## orig_lg Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-z]{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%7D%24 "try regular expression with regexr.com")
