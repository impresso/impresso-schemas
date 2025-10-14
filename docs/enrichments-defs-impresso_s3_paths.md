## impresso\_s3\_paths Type

`object` ([Details](enrichments-defs-impresso_s3_paths.md))

# impresso\_s3\_paths Properties

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                              |
| :------------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [datastage\_name](#datastage_name)                | `string` | Optional | cannot be null | [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-datastage_name.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/datastage_name")               |
| [datastage\_schema\_link](#datastage_schema_link) | `string` | Optional | cannot be null | [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-datastage_schema_link.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/datastage_schema_link") |
| [s3\_path](#s3_path)                              | Multiple | Optional | cannot be null | [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-s3_path.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/s3_path")                             |

## datastage\_name

Name of the data stage or enrichment linked.

`datastage_name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-datastage_name.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/datastage_name")

### datastage\_name Type

`string`

### datastage\_name Constraints

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

## datastage\_schema\_link

GitHub Link to the datastage's JSON schema.

`datastage_schema_link`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-datastage_schema_link.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/datastage_schema_link")

### datastage\_schema\_link Type

`string`

## s3\_path

S3 URL (or list of urls) to the data or enrichment with this CI (e.g. `s3://112-canonical-final/LeTemps/GDL/issues/GDL-1900-issues.jsonl.bz2` for canonical issues).

`s3_path`

*   is optional

*   Type: any of the following: `string` or `array` ([Details](enrichments-defs-impresso_s3_paths-properties-s3_path.md))

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-defs-impresso_s3_paths-properties-s3_path.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/$defs/impresso_s3_paths/properties/s3_path")

### s3\_path Type

any of the following: `string` or `array` ([Details](enrichments-defs-impresso_s3_paths-properties-s3_path.md))
