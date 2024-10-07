## Text-Reuse Passage Type

`object` ([Text-Reuse Passage](passage.md))

# Text-Reuse Passage Properties

| Property                                              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                |
| :---------------------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                             | `string`  | Required | cannot be null | [Text-Reuse Passage](passage-properties-id.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/id")                                           |
| [begin](#begin)                                       | `integer` | Required | cannot be null | [Text-Reuse Passage](passage-properties-begin.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/begin")                                     |
| [ci\_id](#ci_id)                                      | `string`  | Required | cannot be null | [Text-Reuse Passage](passage-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/ci_id")                                     |
| [cluster\_id](#cluster_id)                            | `string`  | Required | cannot be null | [Text-Reuse Passage](passage-properties-cluster_id.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/cluster_id")                           |
| [date](#date)                                         | `string`  | Required | cannot be null | [Text-Reuse Passage](passage-properties-date.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/date")                                       |
| [end](#end)                                           | `integer` | Required | cannot be null | [Text-Reuse Passage](passage-properties-end.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/end")                                         |
| [pages](#pages)                                       | `array`   | Optional | cannot be null | [Text-Reuse Passage](passage-properties-pages.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/pages")                                     |
| [cluster\_size](#cluster_size)                        | `integer` | Required | cannot be null | [Text-Reuse Passage](passage-properties-cluster_size.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/cluster_size")                       |
| [text](#text)                                         | `string`  | Required | cannot be null | [Text-Reuse Passage](passage-properties-text.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/text")                                       |
| [title](#title)                                       | `string`  | Required | cannot be null | [Text-Reuse Passage](passage-properties-title.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/title")                                     |
| [type](#type)                                         | `string`  | Optional | cannot be null | [Text-Reuse Passage](passage-properties-type.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/type")                                       |
| [cluster\_time\_delta](#cluster_time_delta)           | `integer` | Required | cannot be null | [Text-Reuse Passage](passage-properties-cluster_time_delta.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/cluster_time_delta")           |
| [cluster\_lexical\_overlap](#cluster_lexical_overlap) | `number`  | Required | cannot be null | [Text-Reuse Passage](passage-properties-cluster_lexical_overlap.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/cluster_lexical_overlap") |
| [connected\_clusters](#connected_clusters)            | `array`   | Required | cannot be null | [Text-Reuse Passage](passage-properties-connected_clusters.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/connected_clusters")           |
| [n\_connected\_clusters](#n_connected_clusters)       | `integer` | Required | cannot be null | [Text-Reuse Passage](passage-properties-n_connected_clusters.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/n_connected_clusters")       |

## id

Unique identifier for this passage.

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-id.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/id")

### id Type

`string`

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^c\d+-[a-zA-Z0-9]+-\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-[a-z]-i\d{4}@\d+:\d+$
```

[try pattern](https://regexr.com/?expression=%5Ec%5Cd%2B-%5Ba-zA-Z0-9%5D%2B-%5Cd%7B4%7D-\(0%5B1-9%5D%7C1%5B0-2%5D\)-\(0%5B1-9%5D%7C%5B12%5D%5Cd%7C3%5B01%5D\)-%5Ba-z%5D-i%5Cd%7B4%7D%40%5Cd%2B%3A%5Cd%2B%24 "try regular expression with regexr.com")

## begin

Start index of the text-reuse passage within the article

`begin`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-begin.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/begin")

### begin Type

`integer`

## ci\_id

Content-item ID this passage is from.

`ci_id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/ci_id")

### ci\_id Type

`string`

### ci\_id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-zA-Z0-9]+-\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-[a-z]-i\d{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-zA-Z0-9%5D%2B-%5Cd%7B4%7D-\(0%5B1-9%5D%7C1%5B0-2%5D\)-\(0%5B1-9%5D%7C%5B12%5D%5Cd%7C3%5B01%5D\)-%5Ba-z%5D-i%5Cd%7B4%7D%24 "try regular expression with regexr.com")

## cluster\_id

Unique identifier for this passage's cluster.

`cluster_id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-cluster_id.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/cluster_id")

### cluster\_id Type

`string`

## date

Date of publication of the issue in which the passage appears.

`date`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-date.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/date")

### date Type

`string`

### date Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Cd%7B4%7D\)-\(0%5B1-9%5D%7C1%5B0-2%5D\)-\(0%5B1-9%5D%7C%5B12%5D%5Cd%7C3%5B01%5D\)%24 "try regular expression with regexr.com")

## end

End index of the text-reuse passage within the article

`end`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-end.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/end")

### end Type

`integer`

## pages

Pages content, with id, seq and regions it corresponds to.

`pages`

*   is optional

*   Type: `array`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-pages.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/pages")

### pages Type

`array`

## cluster\_size

Number of passages in this passage's cluster.

`cluster_size`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-cluster_size.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/cluster_size")

### cluster\_size Type

`integer`

## text

Full text of the passage.

`text`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-text.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/text")

### text Type

`string`

## title

Title of the article this passage is from.

`title`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-title.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/title")

### title Type

`string`

## type

Type of the article the passage is from (Not in this release).

`type`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-type.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/type")

### type Type

`string`

## cluster\_time\_delta

Number of days between min\_date and max\_date.

`cluster_time_delta`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-cluster_time_delta.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/cluster_time_delta")

### cluster\_time\_delta Type

`integer`

## cluster\_lexical\_overlap

Computed average lexical overlap of the passages within the cluster. Note these was a mistake in the last processing and this key might be `cluster_lexial_overlap`.

`cluster_lexical_overlap`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-cluster_lexical_overlap.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/cluster_lexical_overlap")

### cluster\_lexical\_overlap Type

`number`

## connected\_clusters

List of clusters also with passages present in this content-item.

`connected_clusters`

*   is required

*   Type: `array`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-connected_clusters.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/connected_clusters")

### connected\_clusters Type

`array`

## n\_connected\_clusters

Number of connected\_clusters for this content-item.

`n_connected_clusters`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Text-Reuse Passage](passage-properties-n_connected_clusters.md "https://impresso.github.io/impresso-schemas/json/text_reuse/passage.schema.json#/properties/n_connected_clusters")

### n\_connected\_clusters Type

`integer`
