# The Ts Schema Schema

```txt
#/properties/ts#/properties/ts
```

timestamp

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [ling\_spacy.schema.json\*](../out/ling_spacy.schema.json "open original schema") |

## ts Type

`string` ([The Ts Schema](ling_spacy-properties-the-ts-schema.md))

## ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

## ts Examples

```json
"2009-06-15T13:45:30"
```
