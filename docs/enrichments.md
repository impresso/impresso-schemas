## Impesso Semantic Enrichments Type

`object` ([Impesso Semantic Enrichments](enrichments.md))

# Impesso Semantic Enrichments Properties

| Property                                     | Type     | Required | Nullable       | Defined by                                                                                                                                                                                           |
| :------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [alias\_year\_key](#alias_year_key)          | `string` | Required | cannot be null | [Impesso Semantic Enrichments](enrichments-properties-alias_year_key.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/alias_year_key")           |
| [timestamp](#timestamp)                      | `string` | Required | cannot be null | [Impesso Semantic Enrichments](enrichments-properties-timestamp.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/timestamp")                     |
| [partner\_institution](#partner_institution) | `string` | Required | cannot be null | [Impesso Semantic Enrichments](enrichments-properties-partner_institution.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/partner_institution") |
| [impresso\_data](#impresso_data)             | `object` | Required | cannot be null | [Impesso Semantic Enrichments](enrichments-properties-impresso_data.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/impresso_data")             |

## alias\_year\_key

Impresso alias and year to which these enrichments correspnd (eg. `GDL-1900`)

`alias_year_key`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-properties-alias_year_key.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/alias_year_key")

### alias\_year\_key Type

`string`

### alias\_year\_key Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z][A-Za-z0-9_]*-\d{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z%5D%5BA-Za-z0-9_%5D*-%5Cd%7B4%7D%24 "try regular expression with regexr.com")

## timestamp

Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format).

`timestamp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-properties-timestamp.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/timestamp")

### timestamp Type

`string`

### timestamp Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

## partner\_institution

Internal alias corresponding to the partner institution this CI comes from.

`partner_institution`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-properties-partner_institution.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/partner_institution")

### partner\_institution Type

`string`

## impresso\_data

All the S3 paths to the corresponding objects and enrichments in the Impresso data.

`impresso_data`

*   is required

*   Type: `object` ([Details](enrichments-properties-impresso_data.md))

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-properties-impresso_data.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/impresso_data")

### impresso\_data Type

`object` ([Details](enrichments-properties-impresso_data.md))

# Impesso Semantic Enrichments Definitions

## Definitions group impresso\_s3\_paths

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths"}
```

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                              |
| :------------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [datastage\_name](#datastage_name)                | `string` | Optional | cannot be null | [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-datastage_name.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/datastage_name")               |
| [datastage\_schema\_link](#datastage_schema_link) | `string` | Optional | cannot be null | [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-datastage_schema_link.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/datastage_schema_link") |
| [s3\_path](#s3_path)                              | Multiple | Optional | cannot be null | [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-s3_path.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/s3_path")                             |

### datastage\_name

Name of the data stage or enrichment linked.

`datastage_name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-datastage_name.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/datastage_name")

#### datastage\_name Type

`string`

#### datastage\_name Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation |
| :--------------------- | :---------- |
| `"canonical-issues"`   |             |
| `"canonical-pages"`    |             |
| `"canonical-audios"`   |             |
| `"rebuilt"`            |             |
| `"emb-words"`          |             |
| `"emb-docs"`           |             |
| `"emb-entities"`       |             |
| `"emb-sents"`          |             |
| `"emb-images-clip"`    |             |
| `"emb-images-dino"`    |             |
| `"entities"`           |             |
| `"newsagencies"`       |             |
| `"langident"`          |             |
| `"lingproc"`           |             |
| `"ocrqa"`              |             |
| `"textreuse-passages"` |             |
| `"textreuse-clusters"` |             |
| `"textreuse-index"`    |             |
| `"topic-assignments"`  |             |
| `"topics"`             |             |

### datastage\_schema\_link

GitHub Link to the datastage's JSON schema.

`datastage_schema_link`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-datastage_schema_link.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/datastage_schema_link")

#### datastage\_schema\_link Type

`string`

### s3\_path

S3 URL (or list of urls) to the data or enrichment with this CI (e.g. `s3://112-canonical-final/LeTemps/GDL/issues/GDL-1900-issues.jsonl.bz2` for canonical issues).

`s3_path`

*   is optional

*   Type: any of the following: `string` or `array` ([Details](enrichments-defs-impresso_s3_paths-properties-s3_path.md))

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-s3_path.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/s3_path")

#### s3\_path Type

any of the following: `string` or `array` ([Details](enrichments-defs-impresso_s3_paths-properties-s3_path.md))
