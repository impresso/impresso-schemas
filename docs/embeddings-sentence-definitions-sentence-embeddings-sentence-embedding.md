## items Type

`object` ([Sentence Embedding](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding.md))

# items Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                    |
| :---------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [lg](#lg)               | `string`  | Optional | cannot be null | [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-lg.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/lg")               |
| [sent\_id](#sent_id)    | `integer` | Required | cannot be null | [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-sent_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/sent_id")     |
| [embedding](#embedding) | `array`   | Required | cannot be null | [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/embedding") |
| [size](#size)           | `integer` | Optional | cannot be null | [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-size.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/size")           |
| [o](#o)                 | `integer` | Optional | cannot be null | [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-o.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/o")                 |

## lg

the two-letter ISO language identifier produced by lingproc

`lg`

* is optional

* Type: `string`

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-lg.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/lg")

### lg Type

`string`

### lg Examples

```json
"de"
```

## sent\_id

Index of the sentence in the sentence array produced by lingproc.

`sent_id`

* is required

* Type: `integer`

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-sent_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/sent_id")

### sent\_id Type

`integer`

### sent\_id Examples

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

The vector embedding representation of the sentence.

`embedding`

* is required

* Type: `number[]`

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/embedding")

### embedding Type

`number[]`

## size

The size of the embedding vector.

`size`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-size.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/size")

### size Type

`integer`

## o

Character offset where the sentence begins in the original text.

`o`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Untitled schema](embeddings-sentence-definitions-sentence-embeddings-sentence-embedding-properties-o.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-sentence.schema.json#/definitions/sents/items/properties/o")

### o Type

`integer`
