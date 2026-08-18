## Text Reuse Cluster Solr Document Type

`object` ([Text Reuse Cluster Solr Document](sem-5.md))

# Text Reuse Cluster Solr Document Properties

| Property                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                             |
| :---------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                           | `string`  | Required | cannot be null | [Text Reuse Cluster Solr Document](sem-5-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/id")                         |
| [min\_date\_dt](#min_date_dt)       | `string`  | Required | cannot be null | [Text Reuse Cluster Solr Document](sem-5-properties-min_date_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/min_date_dt")       |
| [max\_date\_dt](#max_date_dt)       | `string`  | Required | cannot be null | [Text Reuse Cluster Solr Document](sem-5-properties-max_date_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/max_date_dt")       |
| [cluster\_size\_l](#cluster_size_l) | `integer` | Required | cannot be null | [Text Reuse Cluster Solr Document](sem-5-properties-cluster_size_l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/cluster_size_l") |
| [day\_delta\_i](#day_delta_i)       | `integer` | Required | cannot be null | [Text Reuse Cluster Solr Document](sem-5-properties-day_delta_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/day_delta_i")       |
| [newspapers\_ss](#newspapers_ss)    | `array`   | Required | cannot be null | [Text Reuse Cluster Solr Document](sem-5-properties-newspapers_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/newspapers_ss")   |
| [passages\_ss](#passages_ss)        | `array`   | Required | cannot be null | [Text Reuse Cluster Solr Document](sem-5-properties-passages_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/passages_ss")       |
| [ci\_ids\_ss](#ci_ids_ss)           | `array`   | Required | cannot be null | [Text Reuse Cluster Solr Document](sem-5-properties-ci_ids_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/ci_ids_ss")           |
| [lex\_overlap\_d](#lex_overlap_d)   | `number`  | Required | cannot be null | [Text Reuse Cluster Solr Document](sem-5-properties-lex_overlap_d.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/lex_overlap_d")   |
| Additional Properties               | Any       | Optional | can be null    |                                                                                                                                                                                                                                        |

## id

Text reuse cluster identifier pattern

`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Text Reuse Cluster Solr Document](sem-5-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/id")

### id Type

`string`

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^tr-[a-z]+-v[0-9]+-[0-9]+-c[0-9]+$
```

[try pattern](https://regexr.com/?expression=%5Etr-%5Ba-z%5D%2B-v%5B0-9%5D%2B-%5B0-9%5D%2B-c%5B0-9%5D%2B%24 "try regular expression with regexr.com")

## min\_date\_dt

Minimum date of documents in the cluster (ISO 8601 datetime format)

`min_date_dt`

* is required

* Type: `string`

* cannot be null

* defined in: [Text Reuse Cluster Solr Document](sem-5-properties-min_date_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/min_date_dt")

### min\_date\_dt Type

`string`

### min\_date\_dt Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## max\_date\_dt

Maximum date of documents in the cluster (ISO 8601 datetime format)

`max_date_dt`

* is required

* Type: `string`

* cannot be null

* defined in: [Text Reuse Cluster Solr Document](sem-5-properties-max_date_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/max_date_dt")

### max\_date\_dt Type

`string`

### max\_date\_dt Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## cluster\_size\_l

Number of passages in the cluster

`cluster_size_l`

* is required

* Type: `integer`

* cannot be null

* defined in: [Text Reuse Cluster Solr Document](sem-5-properties-cluster_size_l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/cluster_size_l")

### cluster\_size\_l Type

`integer`

### cluster\_size\_l Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## day\_delta\_i

Number of days between min\_date and max\_date

`day_delta_i`

* is required

* Type: `integer`

* cannot be null

* defined in: [Text Reuse Cluster Solr Document](sem-5-properties-day_delta_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/day_delta_i")

### day\_delta\_i Type

`integer`

### day\_delta\_i Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## newspapers\_ss

List of newspaper IDs in the cluster

`newspapers_ss`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Text Reuse Cluster Solr Document](sem-5-properties-newspapers_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/newspapers_ss")

### newspapers\_ss Type

`string[]`

### newspapers\_ss Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## passages\_ss

List of passage identifiers (format: CI\_ID\@offset:length)

`passages_ss`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Text Reuse Cluster Solr Document](sem-5-properties-passages_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/passages_ss")

### passages\_ss Type

`string[]`

### passages\_ss Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## ci\_ids\_ss

List of content item IDs in the cluster

`ci_ids_ss`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Text Reuse Cluster Solr Document](sem-5-properties-ci_ids_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/ci_ids_ss")

### ci\_ids\_ss Type

`string[]`

### ci\_ids\_ss Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## lex\_overlap\_d

Lexical overlap percentage

`lex_overlap_d`

* is required

* Type: `number`

* cannot be null

* defined in: [Text Reuse Cluster Solr Document](sem-5-properties-lex_overlap_d.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/properties/lex_overlap_d")

### lex\_overlap\_d Type

`number`

### lex\_overlap\_d Constraints

**maximum**: the value of this number must smaller than or equal to: `100`

**minimum**: the value of this number must greater than or equal to: `0`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema

# Text Reuse Cluster Solr Document Definitions

## Definitions group clusterIdPattern

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.tr-clusters.v1.schema.json#/$defs/clusterIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
