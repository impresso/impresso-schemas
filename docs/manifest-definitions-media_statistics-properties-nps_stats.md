## nps\_stats Type

`object` ([Details](manifest-definitions-media_statistics-properties-nps_stats.md))

# nps\_stats Properties

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                           |
| :---------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [titles](#titles)                         | `integer` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-titles.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/titles")                       |
| [issues](#issues)                         | `integer` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-issues.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/issues")                       |
| [pages](#pages)                           | `integer` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-pages.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/pages")                         |
| [content\_items\_out](#content_items_out) | `integer` | Required | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-content_items_out.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/content_items_out") |
| [content\_items\_in](#content_items_in)   | `integer` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-content_items_in.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/content_items_in")   |
| [images](#images)                         | `integer` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-images.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/images")                       |
| [ne\_entites](#ne_entites)                | `integer` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-ne_entites.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/ne_entites")               |
| [ne\_mentions](#ne_mentions)              | `integer` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-ne_mentions.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/ne_mentions")             |
| [ne\_links](#ne_links)                    | `integer` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-ne_links.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/ne_links")                   |
| [topics](#topics)                         | `integer` | Optional | cannot be null | [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-topics.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/topics")                       |

## titles

Number of newspaper titles included in the data.

`titles`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-titles.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/titles")

### titles Type

`integer`

## issues

Number of issues present in the data.

`issues`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-issues.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/issues")

### issues Type

`integer`

## pages

Number of pages present in the data.

`pages`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-pages.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/pages")

### pages Type

`integer`

## content\_items\_out

Number of content-items present in the (output) data.

`content_items_out`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-content_items_out.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/content_items_out")

### content\_items\_out Type

`integer`

## content\_items\_in

Number of content-items present in the input data used for processing and included in count. Used to track loss of data within a processing step.

`content_items_in`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-content_items_in.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/content_items_in")

### content\_items\_in Type

`integer`

## images

Number of images present in the data.

`images`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-images.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/images")

### images Type

`integer`

## ne\_entites

Number of unique named entities present in the data.

`ne_entites`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-ne_entites.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/ne_entites")

### ne\_entites Type

`integer`

## ne\_mentions

Number of named-entity mentions present in the data.

`ne_mentions`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-ne_mentions.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/ne_mentions")

### ne\_mentions Type

`integer`

## ne\_links

Number of named-entity links present in the data.

`ne_links`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-ne_links.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/ne_links")

### ne\_links Type

`integer`

## topics

Number of topics extracted from the data.

`topics`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-definitions-media_statistics-properties-nps_stats-properties-topics.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/definitions/media_statistics/properties/nps_stats/properties/topics")

### topics Type

`integer`
