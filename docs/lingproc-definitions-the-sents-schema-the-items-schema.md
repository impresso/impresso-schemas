# The Items Schema Schema

```txt
https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/definitions/sents/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [lingproc.v2.schema.json\*](../out/lingproc.v2.schema.json "open original schema") |

## items Type

`object` ([The Items Schema](lingproc-definitions-the-sents-schema-the-items-schema.md))

# items Properties

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                       |
| :---------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [lg](#lg)         | `string` | Optional | cannot be null | [Untitled schema](lingproc-definitions-the-sents-schema-the-items-schema-properties-the-lg-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/definitions/sents/items/properties/lg") |
| [tokens](#tokens) | `array`  | Required | cannot be null | [Untitled schema](lingproc-definitions-the-sents-schema-the-items-schema-properties-tokens.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/definitions/sents/items/properties/tokens")    |

## lg

the two-letter ISO language identifier

`lg`

*   is optional

*   Type: `string` ([The Lg Schema](lingproc-definitions-the-sents-schema-the-items-schema-properties-the-lg-schema.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-definitions-the-sents-schema-the-items-schema-properties-the-lg-schema.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/definitions/sents/items/properties/lg")

### lg Type

`string` ([The Lg Schema](lingproc-definitions-the-sents-schema-the-items-schema-properties-the-lg-schema.md))

### lg Examples

```json
"de"
```

## tokens

Sequence of tokens

`tokens`

*   is required

*   Type: `object[]` ([Token](lingproc-definitions-the-sents-schema-the-items-schema-properties-tokens-token.md))

*   cannot be null

*   defined in: [Untitled schema](lingproc-definitions-the-sents-schema-the-items-schema-properties-tokens.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/definitions/sents/items/properties/tokens")

### tokens Type

`object[]` ([Token](lingproc-definitions-the-sents-schema-the-items-schema-properties-tokens-token.md))
