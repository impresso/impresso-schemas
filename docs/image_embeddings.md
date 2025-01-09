## Image Embeddings JSON Schema Type

`object` ([Image Embeddings JSON Schema](image_embeddings.md))

# Image Embeddings JSON Schema Properties

| Property                   | Type      | Required | Nullable       | Defined by                                                                                                                                                                                  |
| :------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ci\_id](#ci_id)           | `string`  | Required | cannot be null | [Image Embeddings JSON Schema](image_embeddings-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/ci_id")           |
| [ts](#ts)                  | `string`  | Optional | cannot be null | [Image Embeddings JSON Schema](image_embeddings-properties-ts.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/ts")                 |
| [model\_id](#model_id)     | `string`  | Required | cannot be null | [Image Embeddings JSON Schema](image_embeddings-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/model_id")     |
| [size](#size)              | `integer` | Required | cannot be null | [Image Embeddings JSON Schema](image_embeddings-properties-size.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/size")             |
| [embedding](#embedding)    | Merged    | Required | cannot be null | [Image Embeddings JSON Schema](image_embeddings-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/embedding")   |
| [seconds](#seconds)        | `number`  | Optional | cannot be null | [Image Embeddings JSON Schema](image_embeddings-properties-seconds.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/seconds")       |
| [title\_year](#title_year) | `string`  | Optional | cannot be null | [Image Embeddings JSON Schema](image_embeddings-properties-title_year.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/title_year") |

## ci\_id

Unique identifier for the content item.

`ci_id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Image Embeddings JSON Schema](image_embeddings-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/ci_id")

### ci\_id Type

`string`

### ci\_id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-zA-Z0-9]+-\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-[a-z]-i\d{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-zA-Z0-9%5D%2B-%5Cd%7B4%7D-\(0%5B1-9%5D%7C1%5B0-2%5D\)-\(0%5B1-9%5D%7C%5B12%5D%5Cd%7C3%5B01%5D\)-%5Ba-z%5D-i%5Cd%7B4%7D%24 "try regular expression with regexr.com")

### ci\_id Examples

```json
"actionfem-1940-01-08-a-i0001"
```

## ts

Timestamp indicating when the embedding was created (e.g., '2024-10-09T09:29:02Z').

`ts`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Embeddings JSON Schema](image_embeddings-properties-ts.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/ts")

### ts Type

`string`

### ts Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## model\_id

The ID of the model that produced this output, composed as specified in these slides: <https://docs.google.com/presentation/d/1wH4LygLcT28rvMA82k5fyEyzdX49inGkqCLnBNZsFaw/edit#slide=id.g30cf04393c4_1_46>.

`model_id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Image Embeddings JSON Schema](image_embeddings-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/model_id")

### model\_id Type

`string`

### model\_id Examples

```json
"emb-images_dinov2-v0.0.1"
```

## size

The size of the embedding vector.

`size`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Image Embeddings JSON Schema](image_embeddings-properties-size.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/size")

### size Type

`integer`

## embedding



`embedding`

*   is required

*   Type: merged type ([Details](image_embeddings-properties-embedding.md))

*   cannot be null

*   defined in: [Image Embeddings JSON Schema](image_embeddings-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/embedding")

### embedding Type

merged type ([Details](image_embeddings-properties-embedding.md))

one (and only one) of

*   [Untitled array in Image Embeddings JSON Schema](image_embeddings-properties-embedding-oneof-0.md "check type definition")

## seconds

Number of seconds it took to generate the embedding for this image.

`seconds`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Image Embeddings JSON Schema](image_embeddings-properties-seconds.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/seconds")

### seconds Type

`number`

### seconds Examples

```json
0.973115
```

## title\_year

Title-year key this image emebeddings corresponds to.

`title_year`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Embeddings JSON Schema](image_embeddings-properties-title_year.md "https://impresso.github.io/impresso-schemas/json/embeddings/image_embeddings.schema.json#/properties/title_year")

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
