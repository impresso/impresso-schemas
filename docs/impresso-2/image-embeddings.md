## Image Embeddings JSON Schema Type

`object` ([Image Embeddings JSON Schema](image-embeddings.md))

all of

* [Content-item identifier property](ocr-qa-allof-content-item-identifier-property.md "check type definition")

* [Model identifier property](lingproc-allof-model-identifier-property.md "check type definition")

# Image Embeddings JSON Schema Properties

| Property                   | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                          |
| :------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ts](#ts)                  | `string`  | Optional | cannot be null | [Image Embeddings JSON Schema](image-embeddings-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/ts")                 |
| [size](#size)              | `integer` | Required | cannot be null | [Image Embeddings JSON Schema](image-embeddings-properties-size.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/size")             |
| [embedding](#embedding)    | Merged    | Required | cannot be null | [Image Embeddings JSON Schema](image-embeddings-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/embedding")   |
| [seconds](#seconds)        | `number`  | Optional | cannot be null | [Image Embeddings JSON Schema](image-embeddings-properties-seconds.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/seconds")       |
| [title\_year](#title_year) | `string`  | Optional | cannot be null | [Image Embeddings JSON Schema](image-embeddings-properties-title_year.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/title_year") |

## ts

Timestamp indicating when the embedding was created (e.g., '2024-10-09T09:29:02Z').

`ts`

* is optional

* Type: `string`

* cannot be null

* defined in: [Image Embeddings JSON Schema](image-embeddings-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/ts")

### ts Type

`string`

### ts Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## size

The size of the embedding vector.

`size`

* is required

* Type: `integer`

* cannot be null

* defined in: [Image Embeddings JSON Schema](image-embeddings-properties-size.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/size")

### size Type

`integer`

## embedding

`embedding`

* is required

* Type: merged type ([Details](image-embeddings-properties-embedding.md))

* cannot be null

* defined in: [Image Embeddings JSON Schema](image-embeddings-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/embedding")

### embedding Type

merged type ([Details](image-embeddings-properties-embedding.md))

one (and only one) of

* [Untitled array in Image Embeddings JSON Schema](image-embeddings-properties-embedding-oneof-0.md "check type definition")

## seconds

Number of seconds it took to generate the embedding for this image.

`seconds`

* is optional

* Type: `number`

* cannot be null

* defined in: [Image Embeddings JSON Schema](image-embeddings-properties-seconds.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/seconds")

### seconds Type

`number`

### seconds Examples

```json
0.973115
```

## title\_year

Title-year key this image embeddings corresponds to.

`title_year`

* is optional

* Type: `string`

* cannot be null

* defined in: [Image Embeddings JSON Schema](image-embeddings-properties-title_year.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-embeddings/image-embeddings.v1.schema.json#/properties/title_year")

### title\_year Type

`string`

### title\_year Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-zA-Z0-9]+-\d{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-zA-Z0-9%5D%2B-%5Cd%7B4%7D%24 "try regular expression with regexr.com")

### title\_year Examples

```json
"actionfem-1940"
```
