## items Type

`object` ([The Items Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema.md))

# items Properties

| Property | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                               |
| :------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [t](#t)  | `string`  | Required | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-t-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/t") |
| [l](#l)  | `string`  | Optional | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-l-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/l") |
| [p](#p)  | `string`  | Optional | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-p-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/p") |
| [o](#o)  | `integer` | Required | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-o-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/o") |
| [e](#e)  | `string`  | Optional | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-e-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/e") |

## t

token text

`t`

* is required

* Type: `string` ([The T Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-t-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-t-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/t")

### t Type

`string` ([The T Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-t-schema.md))

### t Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E\(.*\)%24 "try regular expression with regexr.com")

### t Examples

```json
"Kumpel"
```

## l

token lemma

`l`

* is optional

* Type: `string` ([The L Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-l-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-l-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/l")

### l Type

`string` ([The L Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-l-schema.md))

### l Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E\(.*\)%24 "try regular expression with regexr.com")

### l Examples

```json
"Kumpel"
```

## p

part-of-speech assigned to token from spacy

`p`

* is optional

* Type: `string` ([The P Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-p-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-p-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/p")

### p Type

`string` ([The P Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-p-schema.md))

### p Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E\(.*\)%24 "try regular expression with regexr.com")

### p Examples

```json
"NOUN"
```

## o

zero-based character offset corresponding to position in ft element

`o`

* is required

* Type: `integer` ([The O Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-o-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-o-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/o")

### o Type

`integer` ([The O Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-o-schema.md))

### o Examples

```json
0
```

## e

named entity type with information about position according to IOB schema

`e`

* is optional

* Type: `string` ([The E Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-e-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-e-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok/items/properties/e")

### e Type

`string` ([The E Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema-properties-the-e-schema.md))

### e Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E\(.*\)%24 "try regular expression with regexr.com")

### e Examples

```json
"B-LOC"
```
