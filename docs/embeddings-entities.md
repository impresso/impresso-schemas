## Entity Embeddings Schema Type

`object` ([Entity Embeddings Schema](embeddings-entities.md))

# Entity Embeddings Schema Properties

| Property                                           | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                            |
| :------------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wkd\_id](#wkd_id)                                 | `string` | Required | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-wkd_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/wkd_id")                                 |
| [entity\_ids](#entity_ids)                         | `array`  | Required | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-entity_ids.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/entity_ids")                         |
| [language](#language)                              | `string` | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-language.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/language")                             |
| [pagename](#pagename)                              | `string` | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-pagename.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/pagename")                             |
| [url](#url)                                        | `string` | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-url.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/url")                                       |
| [date\_of\_birth](#date_of_birth)                  | `string` | Optional | can be null    | [Entity Embeddings Schema](embeddings-entities-properties-date_of_birth.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/date_of_birth")                   |
| [date\_of\_death](#date_of_death)                  | `string` | Optional | can be null    | [Entity Embeddings Schema](embeddings-entities-properties-date_of_death.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/date_of_death")                   |
| [occupations\_titles](#occupations_titles)         | `array`  | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-occupations_titles.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/occupations_titles")         |
| [occupations\_qids](#occupations_qids)             | `array`  | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-occupations_qids.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/occupations_qids")             |
| [occupations\_urls](#occupations_urls)             | `array`  | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-occupations_urls.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/occupations_urls")             |
| [summaries](#summaries)                            | `object` | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-summaries.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/summaries")                           |
| [instances\_titles](#instances_titles)             | `array`  | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-instances_titles.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/instances_titles")             |
| [instances\_qids](#instances_qids)                 | `array`  | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-instances_qids.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/instances_qids")                 |
| [instances\_urls](#instances_urls)                 | `array`  | Optional | can be null    | [Entity Embeddings Schema](embeddings-entities-properties-instances_urls.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/instances_urls")                 |
| [contexts](#contexts)                              | `array`  | Required | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-contexts.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/contexts")                             |
| [surfaces](#surfaces)                              | `array`  | Required | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-surfaces.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/surfaces")                             |
| [ci\_ids](#ci_ids)                                 | `array`  | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-ci_ids.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/ci_ids")                                 |
| [mention\_keys](#mention_keys)                     | `array`  | Optional | cannot be null | [Entity Embeddings Schema](embeddings-entities-properties-mention_keys.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/mention_keys")                     |
| [encyclopedic\_embedding](#encyclopedic_embedding) | `array`  | Optional | can be null    | [Entity Embeddings Schema](embeddings-entities-properties-encyclopedic_embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/encyclopedic_embedding") |
| [news\_embedding](#news_embedding)                 | `array`  | Optional | can be null    | [Entity Embeddings Schema](embeddings-entities-properties-news_embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/news_embedding")                 |
| [entity\_embedding](#entity_embedding)             | `array`  | Optional | can be null    | [Entity Embeddings Schema](embeddings-entities-properties-entity_embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/entity_embedding")             |

## wkd\_id

Wikidata identifier of the entity

`wkd_id`

* is required

* Type: `string`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-wkd_id.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/wkd_id")

### wkd\_id Type

`string`

## entity\_ids

Impresso-specific entity identifiers (can be multiple across languages)

`entity_ids`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-entity_ids.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/entity_ids")

### entity\_ids Type

`string[]`

## language

Language code of the entity's main Wikipedia page

`language`

* is optional

* Type: `string`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-language.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/language")

### language Type

`string`

## pagename

Wikipedia page title of the entity

`pagename`

* is optional

* Type: `string`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-pagename.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/pagename")

### pagename Type

`string`

## url

Wikipedia URL of the entity

`url`

* is optional

* Type: `string`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-url.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/url")

### url Type

`string`

### url Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## date\_of\_birth

Date of birth if available (YYYY, YYYY-MM, or YYYY-MM-DD)

`date_of_birth`

* is optional

* Type: `string`

* can be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-date_of_birth.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/date_of_birth")

### date\_of\_birth Type

`string`

### date\_of\_birth Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(\d{4}|\d{4}-\d{2}|\d{4}-\d{2}-\d{2})$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Cd%7B4%7D%7C%5Cd%7B4%7D-%5Cd%7B2%7D%7C%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D\)%24 "try regular expression with regexr.com")

## date\_of\_death

Date of death if available (YYYY, YYYY-MM, or YYYY-MM-DD)

`date_of_death`

* is optional

* Type: `string`

* can be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-date_of_death.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/date_of_death")

### date\_of\_death Type

`string`

### date\_of\_death Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(\d{4}|\d{4}-\d{2}|\d{4}-\d{2}-\d{2})$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Cd%7B4%7D%7C%5Cd%7B4%7D-%5Cd%7B2%7D%7C%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D\)%24 "try regular expression with regexr.com")

## occupations\_titles

Titles of occupations linked to the entity

`occupations_titles`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-occupations_titles.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/occupations_titles")

### occupations\_titles Type

`string[]`

## occupations\_qids

Wikidata QIDs for occupations

`occupations_qids`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-occupations_qids.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/occupations_qids")

### occupations\_qids Type

`string[]`

## occupations\_urls

Wikipedia/Wikidata URLs for occupations

`occupations_urls`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-occupations_urls.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/occupations_urls")

### occupations\_urls Type

`string[]`

## summaries

Dictionary of language → summary text

`summaries`

* is optional

* Type: `object` ([Details](embeddings-entities-properties-summaries.md))

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-summaries.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/summaries")

### summaries Type

`object` ([Details](embeddings-entities-properties-summaries.md))

## instances\_titles

Classes or instance types of the entity

`instances_titles`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-instances_titles.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/instances_titles")

### instances\_titles Type

`string[]`

## instances\_qids

QIDs for instance classes

`instances_qids`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-instances_qids.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/instances_qids")

### instances\_qids Type

`string[]`

## instances\_urls

URLs for instance classes (if any)

`instances_urls`

* is optional

* Type: `string[]`

* can be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-instances_urls.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/instances_urls")

### instances\_urls Type

`string[]`

## contexts

Mention contexts extracted from newspapers

`contexts`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-contexts.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/contexts")

### contexts Type

`string[]`

## surfaces

Mention surfaces (unique forms found in text)

`surfaces`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-surfaces.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/surfaces")

### surfaces Type

`string[]`

## ci\_ids

Unique document IDs (ci\_id) where the entity appears

`ci_ids`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-ci_ids.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/ci_ids")

### ci\_ids Type

`string[]`

## mention\_keys

Mention-level identifiers linking surface to offsets

`mention_keys`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-mention_keys.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/mention_keys")

### mention\_keys Type

`string[]`

## encyclopedic\_embedding

Vector embedding from encyclopedic profile

`encyclopedic_embedding`

* is optional

* Type: `number[]`

* can be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-encyclopedic_embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/encyclopedic_embedding")

### encyclopedic\_embedding Type

`number[]`

## news\_embedding

Vector embedding from news contexts

`news_embedding`

* is optional

* Type: `number[]`

* can be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-news_embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/news_embedding")

### news\_embedding Type

`number[]`

## entity\_embedding

Final combined entity embedding (average of profiles)

`entity_embedding`

* is optional

* Type: `number[]`

* can be null

* defined in: [Entity Embeddings Schema](embeddings-entities-properties-entity_embedding.md "https://impresso.github.io/impresso-schemas/json/embeddings/embeddings-entities.schema.json#/properties/entity_embedding")

### entity\_embedding Type

`number[]`
