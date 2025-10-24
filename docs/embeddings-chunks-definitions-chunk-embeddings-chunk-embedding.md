## items Type

`object` ([Chunk Embedding](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding.md))

# items Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                           |
| :---------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [lg](#lg)               | `string`  | Optional | cannot be null | [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-lg.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/lg")               |
| [chunk\_id](#chunk_id)  | `integer` | Required | cannot be null | [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-chunk_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/chunk_id")   |
| [embedding](#embedding) | `array`   | Required | cannot be null | [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/embedding") |
| [size](#size)           | `integer` | Optional | cannot be null | [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-size.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/size")           |
| [o](#o)                 | `integer` | Optional | cannot be null | [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-o.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/o")                 |

## lg

the two-letter ISO language identifier produced by lingproc

`lg`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-lg.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/lg")

### lg Type

`string`

### lg Examples

```json
"de"
```

## chunk\_id

Index of the chunk in the chunk array produced by chonkie, based on lingproc segmentation.

`chunk_id`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-chunk_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/chunk_id")

### chunk\_id Type

`integer`

### chunk\_id Examples

```json
0
```

```json
1
```

```json
2
```

## embedding

The vector embedding representation of the chunk.

`embedding`

*   is required

*   Type: `number[]`

*   cannot be null

*   defined in: [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/embedding")

### embedding Type

`number[]`

## size

The size of the embedding vector.

`size`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-size.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/size")

### size Type

`integer`

## o

Character offset where the chunk begins in the original text.

`o`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Untitled schema](embeddings-chunks-definitions-chunk-embeddings-chunk-embedding-properties-o.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-chunks.schema.json#/definitions/chunks/items/properties/o")

### o Type

`integer`
