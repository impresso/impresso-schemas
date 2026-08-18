## Document Embeddings JSON Schema Type

`object` ([Document Embeddings JSON Schema](embeddings-docs.md))

all of

* [Content-item identifier property](ocr-qa-allof-content-item-identifier-property.md "check type definition")

* [Model identifier property](lingproc-allof-model-identifier-property.md "check type definition")

# Document Embeddings JSON Schema Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                            |
| :---------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ci\_type](#ci_type)    | `string`  | Optional | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-ci_type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json#/properties/ci_type")     |
| [embedding](#embedding) | Merged    | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json#/properties/embedding") |
| [size](#size)           | `integer` | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-size.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json#/properties/size")           |
| [ts](#ts)               | `string`  | Optional | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json#/properties/ts")               |

## ci\_type

Type of content item as present in the rebuilt

`ci_type`

* is optional

* Type: `string`

* cannot be null

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-ci_type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json#/properties/ci_type")

### ci\_type Type

`string`

## embedding

`embedding`

* is required

* Type: merged type ([Details](embeddings-docs-properties-embedding.md))

* cannot be null

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json#/properties/embedding")

### embedding Type

merged type ([Details](embeddings-docs-properties-embedding.md))

one (and only one) of

* [Untitled array in Document Embeddings JSON Schema](embeddings-docs-properties-embedding-oneof-0.md "check type definition")

* [Untitled array in Document Embeddings JSON Schema](embeddings-docs-properties-embedding-oneof-1.md "check type definition")

## size

The size of the embedding vectors.

`size`

* is required

* Type: `integer`

* cannot be null

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-size.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json#/properties/size")

### size Type

`integer`

## ts

Timestamp indicating when the embedding was created (e.g., '2024-10-09T09:29:02Z').

`ts`

* is optional

* Type: `string`

* cannot be null

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/document-embeddings/embeddings-docs.v1.schema.json#/properties/ts")

### ts Type

`string`

### ts Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")
