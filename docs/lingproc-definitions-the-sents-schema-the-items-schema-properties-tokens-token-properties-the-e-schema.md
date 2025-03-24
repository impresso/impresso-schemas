# The E Schema Schema

```txt
https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/definitions/sents/items/properties/tokens/items/properties/e
```

named entity type as IOB tag

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [lingproc.v2.schema.json\*](../out/lingproc.v2.schema.json "open original schema") |

## e Type

`string` ([The E Schema](lingproc-definitions-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-e-schema.md))

## e Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[IOBES]-[A-Za-z_0-9]+$
```

[try pattern](https://regexr.com/?expression=%5E%5BIOBES%5D-%5BA-Za-z_0-9%5D%2B%24 "try regular expression with regexr.com")

## e Examples

```json
"B-LOC"
```
