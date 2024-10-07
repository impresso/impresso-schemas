## Text-Reuse Cluster Type

`object` ([Text-Reuse Cluster](cluster.md))

# Text-Reuse Cluster Properties

| Property                             | Type      | Required | Nullable       | Defined by                                                                                                                                                                |
| :----------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                            | `string`  | Required | cannot be null | [Text-Reuse Cluster](cluster-properties-id.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/id")                           |
| [min\_date](#min_date)               | `string`  | Required | cannot be null | [Text-Reuse Cluster](cluster-properties-min_date.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/min_date")               |
| [max\_date](#max_date)               | `string`  | Required | cannot be null | [Text-Reuse Cluster](cluster-properties-max_date.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/max_date")               |
| [cluster\_size](#cluster_size)       | `integer` | Required | cannot be null | [Text-Reuse Cluster](cluster-properties-cluster_size.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/cluster_size")       |
| [time\_delta](#time_delta)           | `integer` | Required | cannot be null | [Text-Reuse Cluster](cluster-properties-time_delta.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/time_delta")           |
| [newspapers](#newspapers)            | `array`   | Required | cannot be null | [Text-Reuse Cluster](cluster-properties-newspapers.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/newspapers")           |
| [passages](#passages)                | `array`   | Required | cannot be null | [Text-Reuse Cluster](cluster-properties-passages.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/passages")               |
| [doc\_ids](#doc_ids)                 | `array`   | Required | cannot be null | [Text-Reuse Cluster](cluster-properties-doc_ids.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/doc_ids")                 |
| [lexical\_overlap](#lexical_overlap) | `number`  | Required | cannot be null | [Text-Reuse Cluster](cluster-properties-lexical_overlap.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/lexical_overlap") |

## id

Unique identifier for this cluster.

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Cluster](cluster-properties-id.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/id")

### id Type

`string`

## min\_date

Earliest date represented in the article passages of the cluster

`min_date`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Cluster](cluster-properties-min_date.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/min_date")

### min\_date Type

`string`

### min\_date Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Cd%7B4%7D\)-\(0%5B1-9%5D%7C1%5B0-2%5D\)-\(0%5B1-9%5D%7C%5B12%5D%5Cd%7C3%5B01%5D\)%24 "try regular expression with regexr.com")

## max\_date

Latest date represented in the article passages of the cluster

`max_date`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Cluster](cluster-properties-max_date.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/max_date")

### max\_date Type

`string`

### max\_date Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Cd%7B4%7D\)-\(0%5B1-9%5D%7C1%5B0-2%5D\)-\(0%5B1-9%5D%7C%5B12%5D%5Cd%7C3%5B01%5D\)%24 "try regular expression with regexr.com")

## cluster\_size

Number of article passages present in the cluster.

`cluster_size`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Text-Reuse Cluster](cluster-properties-cluster_size.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/cluster_size")

### cluster\_size Type

`integer`

## time\_delta

Number of days between min\_date and max\_date.

`time_delta`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Text-Reuse Cluster](cluster-properties-time_delta.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/time_delta")

### time\_delta Type

`integer`

## newspapers

List of all newspapers represented in this cluster with article passages.

`newspapers`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [Text-Reuse Cluster](cluster-properties-newspapers.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/newspapers")

### newspapers Type

`string[]`

## passages

List of all article passages composing this cluster.

`passages`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [Text-Reuse Cluster](cluster-properties-passages.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/passages")

### passages Type

`string[]`

## doc\_ids

List of all article passages composing this cluster.

`doc_ids`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [Text-Reuse Cluster](cluster-properties-doc_ids.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/doc_ids")

### doc\_ids Type

`string[]`

## lexical\_overlap

Computed average lexical overlap of the passages within the cluster.

`lexical_overlap`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Text-Reuse Cluster](cluster-properties-lexical_overlap.md "https://impresso.github.io/impresso-schemas/json/text_reuse/cluster.schema.json#/properties/lexical_overlap")

### lexical\_overlap Type

`number`
