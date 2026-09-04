## Text Reuse Passage Schema Type

`object` ([Text Reuse Passage Schema](sem.md))

# Text Reuse Passage Schema Properties

| Property                                             | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                          |
| :--------------------------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [beg\_offset\_i](#beg_offset_i)                      | `integer` | Required | cannot be null | [Text Reuse Passage Schema](sem-properties-start-offset-of-tr-passage.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/beg_offset_i")             |
| [end\_offset\_i](#end_offset_i)                      | `integer` | Required | cannot be null | [Text Reuse Passage Schema](sem-properties-end-offset-of-tr-passage.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/end_offset_i")               |
| [cluster\_id\_s](#cluster_id_s)                      | `string`  | Required | cannot be null | [Text Reuse Passage Schema](sem-properties-cluster-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/cluster_id_s")                             |
| [cluster\_size\_l](#cluster_size_l)                  | `integer` | Optional | cannot be null | [Text Reuse Passage Schema](sem-properties-cluster-size.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/cluster_size_l")                         |
| [cluster\_lex\_overlap\_d](#cluster_lex_overlap_d)   | `number`  | Optional | cannot be null | [Text Reuse Passage Schema](sem-properties-cluster-lexical-overlap.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/cluster_lex_overlap_d")       |
| [cluster\_day\_delta\_i](#cluster_day_delta_i)       | `integer` | Optional | cannot be null | [Text Reuse Passage Schema](sem-properties-cluster-day-delta.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/cluster_day_delta_i")               |
| [connected\_clusters\_ss](#connected_clusters_ss)    | `array`   | Optional | cannot be null | [Text Reuse Passage Schema](sem-properties-connected-clusters.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/connected_clusters_ss")            |
| [n\_connected\_clusters\_i](#n_connected_clusters_i) | `integer` | Optional | cannot be null | [Text Reuse Passage Schema](sem-properties-number-of-connected-clusters.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/n_connected_clusters_i") |
| Additional Properties                                | Any       | Optional | can be null    |                                                                                                                                                                                                                                                     |

## beg\_offset\_i

Start character offset (index) of the TR passage, relative to the content item transcript.

`beg_offset_i`

* is required

* Type: `integer` ([Start offset of TR passage](sem-properties-start-offset-of-tr-passage.md))

* cannot be null

* defined in: [Text Reuse Passage Schema](sem-properties-start-offset-of-tr-passage.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/beg_offset_i")

### beg\_offset\_i Type

`integer` ([Start offset of TR passage](sem-properties-start-offset-of-tr-passage.md))

### beg\_offset\_i Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## end\_offset\_i

End character offset (index) of the TR passage, relative to the content item transcript.

`end_offset_i`

* is required

* Type: `integer` ([End offset of TR passage](sem-properties-end-offset-of-tr-passage.md))

* cannot be null

* defined in: [Text Reuse Passage Schema](sem-properties-end-offset-of-tr-passage.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/end_offset_i")

### end\_offset\_i Type

`integer` ([End offset of TR passage](sem-properties-end-offset-of-tr-passage.md))

### end\_offset\_i Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## cluster\_id\_s

Text reuse cluster identifier pattern

`cluster_id_s`

* is required

* Type: `string` ([Cluster ID](sem-properties-cluster-id.md))

* cannot be null

* defined in: [Text Reuse Passage Schema](sem-properties-cluster-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/cluster_id_s")

### cluster\_id\_s Type

`string` ([Cluster ID](sem-properties-cluster-id.md))

### cluster\_id\_s Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^tr-[a-z]+-v[0-9]+-[0-9]+-c[0-9]+$
```

[try pattern](https://regexr.com/?expression=%5Etr-%5Ba-z%5D%2B-v%5B0-9%5D%2B-%5B0-9%5D%2B-c%5B0-9%5D%2B%24 "try regular expression with regexr.com")

## cluster\_size\_l

Number of passages in this text reuse cluster

`cluster_size_l`

* is optional

* Type: `integer` ([Cluster size](sem-properties-cluster-size.md))

* cannot be null

* defined in: [Text Reuse Passage Schema](sem-properties-cluster-size.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/cluster_size_l")

### cluster\_size\_l Type

`integer` ([Cluster size](sem-properties-cluster-size.md))

### cluster\_size\_l Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## cluster\_lex\_overlap\_d

Lexical overlap percentage for the cluster

`cluster_lex_overlap_d`

* is optional

* Type: `number` ([Cluster lexical overlap](sem-properties-cluster-lexical-overlap.md))

* cannot be null

* defined in: [Text Reuse Passage Schema](sem-properties-cluster-lexical-overlap.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/cluster_lex_overlap_d")

### cluster\_lex\_overlap\_d Type

`number` ([Cluster lexical overlap](sem-properties-cluster-lexical-overlap.md))

### cluster\_lex\_overlap\_d Constraints

**maximum**: the value of this number must smaller than or equal to: `100`

**minimum**: the value of this number must greater than or equal to: `0`

## cluster\_day\_delta\_i

Number of days between the earliest and latest documents in the cluster

`cluster_day_delta_i`

* is optional

* Type: `integer` ([Cluster day delta](sem-properties-cluster-day-delta.md))

* cannot be null

* defined in: [Text Reuse Passage Schema](sem-properties-cluster-day-delta.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/cluster_day_delta_i")

### cluster\_day\_delta\_i Type

`integer` ([Cluster day delta](sem-properties-cluster-day-delta.md))

### cluster\_day\_delta\_i Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## connected\_clusters\_ss

List of cluster IDs that are connected to this cluster

`connected_clusters_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Text Reuse Passage Schema](sem-properties-connected-clusters.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/connected_clusters_ss")

### connected\_clusters\_ss Type

`string[]`

## n\_connected\_clusters\_i

Count of clusters connected to this cluster

`n_connected_clusters_i`

* is optional

* Type: `integer` ([Number of connected clusters](sem-properties-number-of-connected-clusters.md))

* cannot be null

* defined in: [Text Reuse Passage Schema](sem-properties-number-of-connected-clusters.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/properties/n_connected_clusters_i")

### n\_connected\_clusters\_i Type

`integer` ([Number of connected clusters](sem-properties-number-of-connected-clusters.md))

### n\_connected\_clusters\_i Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema

# Text Reuse Passage Schema Definitions

## Definitions group clusterIdPattern

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.part.tr-passages.v1.schema.json#/$defs/clusterIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
