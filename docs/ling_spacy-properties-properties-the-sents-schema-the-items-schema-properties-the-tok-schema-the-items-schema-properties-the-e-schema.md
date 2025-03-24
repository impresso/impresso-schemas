# The E Schema Schema

```txt
#/properties/sents/items/properties/tok/items/properties/ner#/properties/properties/sents/items/properties/tok/items/properties/e
```

named entity type with information about position according to IOB schema

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [ling\_spacy.schema.json\*](../out/ling_spacy.schema.json "open original schema") |

## e Type

`string` ([The E Schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-e-schema.md))

## e Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E\(.*\)%24 "try regular expression with regexr.com")

## e Examples

```json
"B-LOC"
```
