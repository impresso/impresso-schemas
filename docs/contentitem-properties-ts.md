# Untitled string in Content Item Schema

```txt
https://impresso.github.io/impresso-schemas/json/newspaper/contentitem.schema.json#/properties/ts
```

timestamp of creation of the JSON file (e.g. '2018-09-18T08:00:08Z')


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [contentitem.schema.json\*](../out/contentitem.schema.json "open original schema") |

## ts Type

`string`

## ts Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")
