# The Items Schema Schema

```txt
#/properties/sents/items#/properties/properties/sents/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [ling\_spacy.schema.json\*](../out/ling_spacy.schema.json "open original schema") |

## items Type

`object` ([The Items Schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema.md))

# items Properties

| Property    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                     |
| :---------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sid](#sid) | `integer` | Optional | cannot be null | [Untitled schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-sid-schema.md "#/properties/sents/items/properties/sid#/properties/properties/sents/items/properties/sid") |
| [lg](#lg)   | `string`  | Optional | cannot be null | [Untitled schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-lg-schema.md "#/properties/sents/items/properties/sid#/properties/properties/sents/items/properties/lg")   |
| [tok](#tok) | `array`   | Required | cannot be null | [Untitled schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-tok-schema.md "#/properties/sents/items/properties/tok#/properties/properties/sents/items/properties/tok") |

## sid

Sentence ids

`sid`

*   is optional

*   Type: `integer` ([The Sid Schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-sid-schema.md))

*   cannot be null

*   defined in: [Untitled schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-sid-schema.md "#/properties/sents/items/properties/sid#/properties/properties/sents/items/properties/sid")

### sid Type

`integer` ([The Sid Schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-sid-schema.md))

### sid Examples

```json
1
```

## lg

ISO language identifier

`lg`

*   is optional

*   Type: `string` ([The Lg Schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-lg-schema.md))

*   cannot be null

*   defined in: [Untitled schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-lg-schema.md "#/properties/sents/items/properties/sid#/properties/properties/sents/items/properties/lg")

### lg Type

`string` ([The Lg Schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-lg-schema.md))

### lg Examples

```json
"de"
```

## tok

container for tokens

`tok`

*   is required

*   Type: `object[]` ([The Items Schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema.md))

*   cannot be null

*   defined in: [Untitled schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-tok-schema.md "#/properties/sents/items/properties/tok#/properties/properties/sents/items/properties/tok")

### tok Type

`object[]` ([The Items Schema](ling_spacy-properties-properties-the-sents-schema-the-items-schema-properties-the-tok-schema-the-items-schema.md))
