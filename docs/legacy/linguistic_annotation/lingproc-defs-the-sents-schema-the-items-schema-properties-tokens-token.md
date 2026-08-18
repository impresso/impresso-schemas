## items Type

`object` ([Token](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token.md))

# items Properties

| Property | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                              |
| :------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [t](#t)  | `string`  | Required | cannot be null | [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-t-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/t") |
| [p](#p)  | `string`  | Required | cannot be null | [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-p-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/p") |
| [o](#o)  | `integer` | Required | cannot be null | [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-o-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/o") |
| [l](#l)  | `string`  | Optional | cannot be null | [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-l-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/l") |
| [e](#e)  | `string`  | Optional | cannot be null | [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-e-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/e") |

## t

token text

`t`

* is required

* Type: `string` ([The T Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-t-schema.md))

* cannot be null

* defined in: [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-t-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/t")

### t Type

`string` ([The T Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-t-schema.md))

### t Examples

```json
"Nous"
```

## p

part-of-speech assigned to token from linguistic processing (typically UPOS or XPOS)

`p`

* is required

* Type: `string` ([The P Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-p-schema.md))

* cannot be null

* defined in: [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-p-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/p")

### p Type

`string` ([The P Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-p-schema.md))

### p Examples

```json
"PROPN"
```

## o

zero-based character offset corresponding to position in corresponding text element (t for title, ft for full text from rebuilt)

`o`

* is required

* Type: `integer` ([The O Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-o-schema.md))

* cannot be null

* defined in: [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-o-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/o")

### o Type

`integer` ([The O Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-o-schema.md))

### o Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### o Examples

```json
0
```

## l

lemma of token

`l`

* is optional

* Type: `string` ([The L Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-l-schema.md))

* cannot be null

* defined in: [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-l-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/l")

### l Type

`string` ([The L Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-l-schema.md))

### l Examples

```json
"travailler"
```

## e

named entity type as IOB tag

`e`

* is optional

* Type: `string` ([The E Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-e-schema.md))

* cannot be null

* defined in: [Linguistic Annotation v2](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-e-schema.md "https://impresso.github.io/impresso-schemas/json/linguistic_annotation/lingproc.v2.schema.json#/$defs/sents/items/properties/tokens/items/properties/e")

### e Type

`string` ([The E Schema](lingproc-defs-the-sents-schema-the-items-schema-properties-tokens-token-properties-the-e-schema.md))

### e Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[IOBES]-[A-Za-z_0-9]+$
```

[try pattern](https://regexr.com/?expression=%5E%5BIOBES%5D-%5BA-Za-z_0-9%5D%2B%24 "try regular expression with regexr.com")

### e Examples

```json
"B-LOC"
```
