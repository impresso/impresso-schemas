## Document Embeddings JSON Schema Type

`object` ([Document Embeddings JSON Schema](embeddings-docs.md))

# Document Embeddings JSON Schema Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                 |
| :---------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ci\_id](#ci_id)        | `string`  | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/ci_id")         |
| [ci\_type](#ci_type)    | `string`  | Optional | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-ci_type.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/ci_type")     |
| [model\_id](#model_id)  | `string`  | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/model_id")   |
| [embedding](#embedding) | Merged    | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/embedding") |
| [size](#size)           | `integer` | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-size.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/size")           |
| [ts](#ts)               | `string`  | Optional | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-properties-ts.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/ts")               |

## ci\_id

Unique identifier for the content item.

`ci_id`

* is required

* Type: `string`

* cannot be null

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/ci_id")

### ci\_id Type

`string`

### ci\_id Examples

```json
"actionfem-1940-01-08-a-i0001"
```

## ci\_type

Type of content item as present in the rebuilt

`ci_type`

* is optional

* Type: `string`

* cannot be null

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-ci_type.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/ci_type")

### ci\_type Type

`string`

## model\_id

The ID of the model that produced this output, composed as specified in these slides: <https://docs.google.com/presentation/d/1wH4LygLcT28rvMA82k5fyEyzdX49inGkqCLnBNZsFaw/edit#slide=id.g30cf04393c4_1_46>.

`model_id`

* is required

* Type: `string`

* cannot be null

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/model_id")

### model\_id Type

`string`

## embedding



`embedding`

* is required

* Type: merged type ([Details](embeddings-docs-properties-embedding.md))

* cannot be null

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/embedding")

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

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-size.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/size")

### size Type

`integer`

## ts

Timestamp indicating when the embedding was created (e.g., '2024-10-09T09:29:02Z').

`ts`

* is optional

* Type: `string`

* cannot be null

* defined in: [Document Embeddings JSON Schema](embeddings-docs-properties-ts.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-docs.schema.json#/properties/ts")

### ts Type

`string`

### ts Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")
