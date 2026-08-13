## items Type

`object` ([The Items Schema](ling_spacy-properties-the-sents-schema-the-items-schema.md))

# items Properties

| Property    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                   |
| :---------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sid](#sid) | `integer` | Optional | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-sid-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/sid") |
| [lg](#lg)   | `string`  | Optional | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-lg-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/lg")   |
| [tok](#tok) | `array`   | Required | cannot be null | [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok") |

## sid

Sentence ids

`sid`

* is optional

* Type: `integer` ([The Sid Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-sid-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-sid-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/sid")

### sid Type

`integer` ([The Sid Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-sid-schema.md))

### sid Examples

```json
1
```

## lg

ISO language identifier

`lg`

* is optional

* Type: `string` ([The Lg Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-lg-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-lg-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/lg")

### lg Type

`string` ([The Lg Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-lg-schema.md))

### lg Examples

```json
"de"
```

## tok

container for tokens

`tok`

* is required

* Type: `object[]` ([The Items Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema.md))

* cannot be null

* defined in: [Linguistic Annotation (spaCy)](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/ling_spacy.schema.json#/properties/sents/items/properties/tok")

### tok Type

`object[]` ([The Items Schema](ling_spacy-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema.md))
