## Word Embedding Solr Document Type

`object` ([Word Embedding Solr Document](sem-7.md))

# Word Embedding Solr Document Properties

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                        |
| :---------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [word\_s](#word_s)                        | `string` | Required | cannot be null | [Word Embedding Solr Document](sem-7-properties-word_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json#/properties/word_s")                       |
| [fastText\_emb\_v100](#fasttext_emb_v100) | `array`  | Required | cannot be null | [Word Embedding Solr Document](sem-7-properties-fasttext_emb_v100.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json#/properties/fastText_emb_v100") |
| [lg\_s](#lg_s)                            | `string` | Required | cannot be null | [Word Embedding Solr Document](sem-7-properties-lg_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json#/properties/lg_s")                           |
| Additional Properties                     | Any      | Optional | can be null    |                                                                                                                                                                                                                                   |

## word\_s

The word token

`word_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Word Embedding Solr Document](sem-7-properties-word_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json#/properties/word_s")

### word\_s Type

`string`

### word\_s Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## fastText\_emb\_v100

FastText embedding vector with 100 dimensions

`fastText_emb_v100`

* is required

* Type: `number[]`

* cannot be null

* defined in: [Word Embedding Solr Document](sem-7-properties-fasttext_emb_v100.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json#/properties/fastText_emb_v100")

### fastText\_emb\_v100 Type

`number[]`

### fastText\_emb\_v100 Constraints

**maximum number of items**: the maximum number of items for this array is: `100`

**minimum number of items**: the minimum number of items for this array is: `100`

## lg\_s

Language code (ISO lowercase)

`lg_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Word Embedding Solr Document](sem-7-properties-lg_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.wemb.v1.schema.json#/properties/lg_s")

### lg\_s Type

`string`

### lg\_s Constraints

**maximum length**: the maximum number of characters for this string is: `3`

**minimum length**: the minimum number of characters for this string is: `2`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
