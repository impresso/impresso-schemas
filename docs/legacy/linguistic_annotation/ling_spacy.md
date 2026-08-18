## Linguistic Annotation (spaCy) Type

`object` ([Linguistic Annotation (spaCy)](ling_spacy.md))

# Linguistic Annotation (spaCy) Properties

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                   |
| :-------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ts](#ts)       | `string` | Required | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-ts-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/ts")       |
| [id](#id)       | `string` | Required | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-id-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/id")       |
| [sents](#sents) | `array`  | Required | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents") |

## ts

timestamp

`ts`

* is required

* Type: `string` ([The Ts Schema](ling_spacy-properties-the-ts-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-ts-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/ts")

### ts Type

`string` ([The Ts Schema](ling_spacy-properties-the-ts-schema.md))

### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

### ts Examples

```json
"2009-06-15T13:45:30"
```

## id

id of text

`id`

* is required

* Type: `string` ([The Id Schema](ling_spacy-properties-the-id-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-id-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/id")

### id Type

`string` ([The Id Schema](ling_spacy-properties-the-id-schema.md))

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E\(.*\)%24 "try regular expression with regexr.com")

### id Examples

```json
"NZZ-1794-07-26-a-i0002"
```

## sents

container for sentences (boundaries produced by spacy)

`sents`

* is required

* Type: `object[]` ([The Items Schema](ling_spacy-properties-the-sents-schema-the-items-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents")

### sents Type

`object[]` ([The Items Schema](ling_spacy-properties-the-sents-schema-the-items-schema.md))
