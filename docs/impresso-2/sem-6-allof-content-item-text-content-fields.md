## 4 Type

`object` ([Content Item Text Content Fields](sem-6-allof-content-item-text-content-fields.md))

one (and only one) of

* [Untitled undefined type in Content Item Text Content Fields](content-item-oneof-0.md "check type definition")

* [Untitled undefined type in Content Item Text Content Fields](content-item-oneof-1.md "check type definition")

* [Untitled undefined type in Content Item Text Content Fields](content-item-oneof-2.md "check type definition")

* [Untitled undefined type in Content Item Text Content Fields](content-item-oneof-3.md "check type definition")

* [Untitled undefined type in Content Item Text Content Fields](content-item-oneof-4.md "check type definition")

* [Untitled undefined type in Content Item Text Content Fields](content-item-oneof-5.md "check type definition")

* [Untitled undefined type in Content Item Text Content Fields](content-item-oneof-6.md "check type definition")

* [Untitled undefined type in Content Item Text Content Fields](content-item-oneof-7.md "check type definition")

# 4 Properties

| Property                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                  |
| :---------------------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [doc\_type\_s](#doc_type_s)                     | `string`  | Optional | cannot be null | [Content Item Text Content Fields](content-item-properties-doc_type_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/doc_type_s")                                  |
| [segmentation\_level\_s](#segmentation_level_s) | Merged    | Required | cannot be null | [Content Item Text Content Fields](content-item-properties-segmentation-level.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/segmentation_level_s")                |
| [item\_type\_s](#item_type_s)                   | Merged    | Required | cannot be null | [Content Item Text Content Fields](content-item-properties-item-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/item_type_s")                                  |
| [lg\_orig\_s](#lg_orig_s)                       | `string`  | Optional | cannot be null | [Content Item Text Content Fields](content-item-properties-lg_orig_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/lg_orig_s")                                    |
| [lg\_s](#lg_s)                                  | `string`  | Required | cannot be null | [Content Item Text Content Fields](content-item-properties-lg_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/lg_s")                                              |
| [content\_length\_i](#content_length_i)         | `integer` | Required | cannot be null | [Content Item Text Content Fields](content-item-properties-content_length_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/content_length_i")                      |
| [snippet\_plain](#snippet_plain)                | `string`  | Required | cannot be null | [Content Item Text Content Fields](content-item-properties-snippet_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/snippet_plain")                            |
| [title\_txt](#title_txt)                        | `string`  | Optional | cannot be null | [Content Item Text Content Fields](content-item-properties-title_txt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/title_txt")                                    |
| [content\_txt](#content_txt)                    | `string`  | Optional | cannot be null | [Content Item Text Content Fields](content-item-properties-content_txt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/content_txt")                                |
| [title\_year](#title_year)                      | `string`  | Optional | cannot be null | [Content Item Text Content Fields](content-item-properties-title_year.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/title_year")                                  |
| `^title_txt_[a-z]{2}$`                          | `string`  | Optional | cannot be null | [Content Item Text Content Fields](content-item-patternproperties-title_txt_a-z2.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/patternProperties/^title_txt_\[a-z]{2}$")     |
| `^content_txt_[a-z]{2}$`                        | `string`  | Optional | cannot be null | [Content Item Text Content Fields](content-item-patternproperties-content_txt_a-z2.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/patternProperties/^content_txt_\[a-z]{2}$") |
| Additional Properties                           | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                             |

## doc\_type\_s

Type of document, e.g., page (p) or content item (ci).

`doc_type_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-doc_type_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/doc_type_s")

### doc\_type\_s Type

`string`

### doc\_type\_s Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `"p"`  |             |
| `"ci"` |             |

## segmentation\_level\_s

Level of segmentation applied to the source facsimile from which the content item is derived.

`segmentation_level_s`

* is required

* Type: `string` ([Segmentation level](content-item-properties-segmentation-level.md))

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-segmentation-level.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/segmentation_level_s")

### segmentation\_level\_s Type

`string` ([Segmentation level](content-item-properties-segmentation-level.md))

one (and only one) of

* [No Segmentation (Page or Broadcast)](content-item-properties-segmentation-level-oneof-no-segmentation-page-or-broadcast.md "check type definition")

* [Physical Segmentation (Layout regions)](content-item-properties-segmentation-level-oneof-physical-segmentation-layout-regions.md "check type definition")

* [Logical Segmentation (Articles and editorial units)](content-item-properties-segmentation-level-oneof-logical-segmentation-articles-and-editorial-units.md "check type definition")

* [Semantic Segmentation (Thematic units)](content-item-properties-segmentation-level-oneof-semantic-segmentation-thematic-units.md "check type definition")

## item\_type\_s

Type of content item.

`item_type_s`

* is required

* Type: `string` ([Item type](content-item-properties-item-type.md))

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-item-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/item_type_s")

### item\_type\_s Type

`string` ([Item type](content-item-properties-item-type.md))

one (and only one) of

* [Article](content-item-properties-item-type-oneof-article.md "check type definition")

* [Advertisement](content-item-properties-item-type-oneof-advertisement.md "check type definition")

* [Image](content-item-properties-item-type-oneof-image.md "check type definition")

* [Table](content-item-properties-item-type-oneof-table.md "check type definition")

* [Obituary](content-item-properties-item-type-oneof-obituary.md "check type definition")

* [Weather](content-item-properties-item-type-oneof-weather.md "check type definition")

* [Chronicle](content-item-properties-item-type-oneof-chronicle.md "check type definition")

* [Radio Broadcast](content-item-properties-item-type-oneof-radio-broadcast.md "check type definition")

* [Radio Broadcast Episode](content-item-properties-item-type-oneof-radio-broadcast-episode.md "check type definition")

* [No Type Provided](content-item-properties-item-type-oneof-no-type-provided.md "check type definition")

* [Discussion](content-item-properties-item-type-oneof-discussion.md "check type definition")

* [Entretien](content-item-properties-item-type-oneof-entretien.md "check type definition")

## lg\_orig\_s

Original language of the content item.

`lg_orig_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-lg_orig_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/lg_orig_s")

### lg\_orig\_s Type

`string`

## lg\_s

Computed language of the content item.

`lg_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-lg_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/lg_s")

### lg\_s Type

`string`

## content\_length\_i

Token count of the content item (space split).

`content_length_i`

* is required

* Type: `integer`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-content_length_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/content_length_i")

### content\_length\_i Type

`integer`

## snippet\_plain

Snippet of the content item (first 150 characters).

`snippet_plain`

* is required

* Type: `string`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-snippet_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/snippet_plain")

### snippet\_plain Type

`string`

## title\_txt

Fallback title field when no language-specific title field is available.

`title_txt`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-title_txt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/title_txt")

### title\_txt Type

`string`

## content\_txt

Fallback content field when no language-specific content field is available.

`content_txt`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-content_txt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/content_txt")

### content\_txt Type

`string`

## title\_year

String composed of title + year, e.g. 'Fronde-1872' .

`title_year`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-properties-title_year.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/properties/title_year")

### title\_year Type

`string`

## Pattern: `^title_txt_[a-z]{2}$`

Title of the article in the specified language (ISO 639-1 two-letter language code)

`^title_txt_[a-z]{2}$`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-patternproperties-title_txt_a-z2.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/patternProperties/^title_txt_\[a-z]{2}$")

### ^title\_txt\_\[a-z]{2}$ Type

`string`

## Pattern: `^content_txt_[a-z]{2}$`

Full text content of the article in the specified language (ISO 639-1 two-letter language code)

`^content_txt_[a-z]{2}$`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item Text Content Fields](content-item-patternproperties-content_txt_a-z2.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.transcript.v1.schema.json#/patternProperties/^content_txt_\[a-z]{2}$")

### ^content\_txt\_\[a-z]{2}$ Type

`string`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
