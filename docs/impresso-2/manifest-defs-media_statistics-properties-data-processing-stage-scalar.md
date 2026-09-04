## stage Type

`string` ([Data-processing stage scalar](manifest-defs-media_statistics-properties-data-processing-stage-scalar.md))

## stage Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                      | Explanation |
| :------------------------- | :---------- |
| `"canonical"`              |             |
| `"canonical-consolidated"` |             |
| `"rebuilt"`                |             |
| `"passim"`                 |             |
| `"emb-words"`              |             |
| `"emb-sents"`              |             |
| `"emb-docs"`               |             |
| `"emb-entities"`           |             |
| `"emb-paragraphs"`         |             |
| `"emb-images"`             |             |
| `"classif-images"`         |             |
| `"entities"`               |             |
| `"newsagencies"`           |             |
| `"langident"`              |             |
| `"lingproc"`               |             |
| `"ocrqa"`                  |             |
| `"langid-ocrqa"`           |             |
| `"textreuse"`              |             |
| `"topics"`                 |             |
| `"solr-text-ingestion"`    |             |
| `"mysql-ingestion"`        |             |

## stage Examples

```json
"canonical"
```

```json
"rebuilt"
```

```json
"langident"
```
