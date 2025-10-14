## impresso\_data Type

`object` ([Details](enrichments-properties-impresso_data.md))

# impresso\_data Properties

| Property                                       | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                               |
| :--------------------------------------------- | :------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [prepared\_data](#prepared_data)               | `array` | Required | cannot be null | [Impesso Semantic Enrichments](enrichments-properties-impresso_data-properties-prepared_data.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/impresso_data/properties/prepared_data")               |
| [semantic\_enrichments](#semantic_enrichments) | `array` | Optional | cannot be null | [Impesso Semantic Enrichments](enrichments-properties-impresso_data-properties-semantic_enrichments.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/impresso_data/properties/semantic_enrichments") |

## prepared\_data

The data stages and S3 paths corresponding to the prepared data for this CI.

`prepared_data`

*   is required

*   Type: `object[]` ([Details](enrichments-defs-impresso_s3_paths.md))

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-properties-impresso_data-properties-prepared_data.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/impresso_data/properties/prepared_data")

### prepared\_data Type

`object[]` ([Details](enrichments-defs-impresso_s3_paths.md))

## semantic\_enrichments

The semantic enrichments and their s3 paths for this CI.

`semantic_enrichments`

*   is optional

*   Type: `object[]` ([Details](enrichments-defs-impresso_s3_paths.md))

*   cannot be null

*   defined in: [Impesso Semantic Enrichments](enrichments-properties-impresso_data-properties-semantic_enrichments.md "https://impresso.github.io/impresso-schemas/json/return_card/enrichments.schema.json#/properties/impresso_data/properties/semantic_enrichments")

### semantic\_enrichments Type

`object[]` ([Details](enrichments-defs-impresso_s3_paths.md))
