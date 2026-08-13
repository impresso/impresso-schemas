## items Type

`object` ([The Items Schema](lingproc-defs-the-sents-schema-the-items-schema.md))

# items Properties

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                        |
| :---------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [lg](#lg)         | `string` | Optional | cannot be null | [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-the-lg-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/lg")         |
| [tp](#tp)         | `string` | Optional | cannot be null | [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-the-content-item-type.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tp") |
| [tokens](#tokens) | `array`  | Required | cannot be null | [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens")            |

## lg

the two-letter ISO language identifier

`lg`

* is optional

* Type: `string` ([The Lg Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-the-lg-schema.md))

* cannot be null

* defined in: [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-the-lg-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/lg")

### lg Type

`string` ([The Lg Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-the-lg-schema.md))

### lg Examples

```json
"de"
```

## tp

Type of content item, e.g. 'ar' (article), 'img' (image), etc.

`tp`

* is optional

* Type: `string` ([The Content Item Type](lingproc-defs-the-sents-schema-the-items-schema-properties-the-content-item-type.md))

* cannot be null

* defined in: [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-the-content-item-type.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tp")

### tp Type

`string` ([The Content Item Type](lingproc-defs-the-sents-schema-the-items-schema-properties-the-content-item-type.md))

### tp Examples

```json
"ar"
```

## tokens

Sequence of tokens

`tokens`

* is required

* Type: `object[]` ([Token](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token.md))

* cannot be null

* defined in: [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens")

### tokens Type

`object[]` ([Token](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token.md))
