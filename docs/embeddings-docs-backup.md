## Document Embeddings JSON Schema Type

`object` ([Document Embeddings JSON Schema](embeddings-docs-backup.md))

# Document Embeddings JSON Schema Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                                  |
| :---------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)               | `string`  | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-id-schema.md "#/properties/id#/properties/id")                      |
| [ts](#ts)               | `string`  | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-ts-schema.md "#/properties/ts#/properties/ts")                      |
| [embedder](#embedder)   | `string`  | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-embedder-schema.md "#/properties/embedder#/properties/embedder")    |
| [len](#len)             | `integer` | Optional | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-length-schema.md "#/properties/len#/properties/len")                |
| [embedding](#embedding) | `array`   | Required | cannot be null | [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-embedding-schema.md "#/properties/embedding#/properties/embedding") |

## id

The unique identifier for a content item, cf. <https://github.com/impresso/impresso-schemas/blob/master/json/newspaper/contentitem.schema.json>

`id`

*   is required

*   Type: `string` ([The Id Schema](embeddings-docs-backup-properties-the-id-schema.md))

*   cannot be null

*   defined in: [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-id-schema.md "#/properties/id#/properties/id")

### id Type

`string` ([The Id Schema](embeddings-docs-backup-properties-the-id-schema.md))

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E\(.*\)%24 "try regular expression with regexr.com")

### id Examples

```json
"actionfem-1940-01-08-a-i0001"
```

## ts

The timestamp when the embeddings were created

`ts`

*   is required

*   Type: `string` ([The Ts Schema](embeddings-docs-backup-properties-the-ts-schema.md))

*   cannot be null

*   defined in: [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-ts-schema.md "#/properties/ts#/properties/ts")

### ts Type

`string` ([The Ts Schema](embeddings-docs-backup-properties-the-ts-schema.md))

### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\+00:00|Z)$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D\(%5C%2B00%3A00%7CZ\)%24 "try regular expression with regexr.com")

### ts Examples

```json
"2024-08-29T06:42:53+00:00Z"
```

## embedder

The model or tool used to generate the embeddings

`embedder`

*   is required

*   Type: `string` ([The Embedder Schema](embeddings-docs-backup-properties-the-embedder-schema.md))

*   cannot be null

*   defined in: [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-embedder-schema.md "#/properties/embedder#/properties/embedder")

### embedder Type

`string` ([The Embedder Schema](embeddings-docs-backup-properties-the-embedder-schema.md))

### embedder Examples

```json
"Alibaba-NLP/gte-multilingual-base@f7d567e"
```

## len

The length of the document in characters.

`len`

*   is optional

*   Type: `integer` ([The Length Schema](embeddings-docs-backup-properties-the-length-schema.md))

*   cannot be null

*   defined in: [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-length-schema.md "#/properties/len#/properties/len")

### len Type

`integer` ([The Length Schema](embeddings-docs-backup-properties-the-length-schema.md))

### len Examples

```json
2976
```

## embedding

The vector embeddings of the document

`embedding`

*   is required

*   Type: `number[]` ([The Items Schema](embeddings-docs-backup-properties-the-embedding-schema-the-items-schema.md))

*   cannot be null

*   defined in: [Document Embeddings JSON Schema](embeddings-docs-backup-properties-the-embedding-schema.md "#/properties/embedding#/properties/embedding")

### embedding Type

`number[]` ([The Items Schema](embeddings-docs-backup-properties-the-embedding-schema-the-items-schema.md))
