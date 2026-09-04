## Entity Profile Embedding Document Type

`object` ([Entity Profile Embedding Document](sem-2.md))

# Entity Profile Embedding Document Properties

| Property                                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                  |
| :--------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                            | `string` | Required | cannot be null | [Entity Profile Embedding Document](sem-2-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/id")                                         |
| [imp\_ids\_ss](#imp_ids_ss)                          | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-imp_ids_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/imp_ids_ss")                         |
| [surfaces\_ss](#surfaces_ss)                         | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-surfaces_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/surfaces_ss")                       |
| [ci\_ids\_ss](#ci_ids_ss)                            | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-ci_ids_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/ci_ids_ss")                           |
| [mention\_keys\_ss](#mention_keys_ss)                | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-mention_keys_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/mention_keys_ss")               |
| [ci\_lg\_s](#ci_lg_s)                                | `string` | Optional | can be null    | [Entity Profile Embedding Document](sem-2-properties-ci_lg_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/ci_lg_s")                               |
| [wiki\_masterlabel\_s](#wiki_masterlabel_s)          | `string` | Optional | can be null    | [Entity Profile Embedding Document](sem-2-properties-wiki_masterlabel_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wiki_masterlabel_s")         |
| [wiki\_url\_s](#wiki_url_s)                          | `string` | Optional | can be null    | [Entity Profile Embedding Document](sem-2-properties-wiki_url_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wiki_url_s")                         |
| [date\_of\_birth\_dt](#date_of_birth_dt)             | `string` | Optional | can be null    | [Entity Profile Embedding Document](sem-2-properties-date_of_birth_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/date_of_birth_dt")             |
| [date\_of\_death\_dt](#date_of_death_dt)             | `string` | Optional | can be null    | [Entity Profile Embedding Document](sem-2-properties-date_of_death_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/date_of_death_dt")             |
| [wkd\_occupations\_ss](#wkd_occupations_ss)          | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-wkd_occupations_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wkd_occupations_ss")         |
| [wkd\_occupation\_qids\_ss](#wkd_occupation_qids_ss) | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-wkd_occupation_qids_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wkd_occupation_qids_ss") |
| [wkd\_entity\_types\_ss](#wkd_entity_types_ss)       | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-wkd_entity_types_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wkd_entity_types_ss")       |
| [wiki\_summaries\_t](#wiki_summaries_t)              | `string` | Optional | can be null    | [Entity Profile Embedding Document](sem-2-properties-wiki_summaries_t.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wiki_summaries_t")             |
| [contexts\_ss](#contexts_ss)                         | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-contexts_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/contexts_ss")                       |
| [entity\_mixed\_emb\_v768](#entity_mixed_emb_v768)   | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-entity_mixed_emb_v768.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/entity_mixed_emb_v768")   |
| [entity\_encyc\_emb\_v768](#entity_encyc_emb_v768)   | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-entity_encyc_emb_v768.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/entity_encyc_emb_v768")   |
| [entity\_media\_emb\_v768](#entity_media_emb_v768)   | `array`  | Optional | cannot be null | [Entity Profile Embedding Document](sem-2-properties-entity_media_emb_v768.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/entity_media_emb_v768")   |

## id

Wikidata ID (e.g. 'Q12345').

`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/id")

### id Type

`string`

## imp\_ids\_ss

List of Impresso internal entity identifiers.

`imp_ids_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-imp_ids_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/imp_ids_ss")

### imp\_ids\_ss Type

`string[]`

## surfaces\_ss

All surface forms associated with this entity (coming from mentions).

`surfaces_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-surfaces_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/surfaces_ss")

### surfaces\_ss Type

`string[]`

## ci\_ids\_ss

List of content item (article) IDs in which this entity is mentioned.

`ci_ids_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-ci_ids_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/ci_ids_ss")

### ci\_ids\_ss Type

`string[]`

## mention\_keys\_ss

List of Impresso entity mention keys (as extracted by NER).

`mention_keys_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-mention_keys_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/mention_keys_ss")

### mention\_keys\_ss Type

`string[]`

## ci\_lg\_s

Language code of the content items in which this entity was found (would deserve more explanation here).

`ci_lg_s`

* is optional

* Type: `string`

* can be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-ci_lg_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/ci_lg_s")

### ci\_lg\_s Type

`string`

## wiki\_masterlabel\_s

Wikipedia page name, taken as canonical Wikipedia label for the entity.

`wiki_masterlabel_s`

* is optional

* Type: `string`

* can be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-wiki_masterlabel_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wiki_masterlabel_s")

### wiki\_masterlabel\_s Type

`string`

## wiki\_url\_s

Wikipedia URL (language dependent) for the entity.

`wiki_url_s`

* is optional

* Type: `string`

* can be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-wiki_url_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wiki_url_s")

### wiki\_url\_s Type

`string`

### wiki\_url\_s Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## date\_of\_birth\_dt

Date of birth (ISO 8601 format).

`date_of_birth_dt`

* is optional

* Type: `string`

* can be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-date_of_birth_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/date_of_birth_dt")

### date\_of\_birth\_dt Type

`string`

### date\_of\_birth\_dt Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## date\_of\_death\_dt

Date of death (ISO 8601 format).

`date_of_death_dt`

* is optional

* Type: `string`

* can be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-date_of_death_dt.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/date_of_death_dt")

### date\_of\_death\_dt Type

`string`

### date\_of\_death\_dt Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## wkd\_occupations\_ss

List of Wikidata human-readable occupation labels for the entity

`wkd_occupations_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-wkd_occupations_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wkd_occupations_ss")

### wkd\_occupations\_ss Type

`string[]`

## wkd\_occupation\_qids\_ss

List of Wikidata QIDs corresponding to occupations.

`wkd_occupation_qids_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-wkd_occupation_qids_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wkd_occupation_qids_ss")

### wkd\_occupation\_qids\_ss Type

`string[]`

## wkd\_entity\_types\_ss

List of Wikidata classes / types of which the entity is an instance of (expressed via <https://www.wikidata.org/wiki/Property:P31>).

`wkd_entity_types_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-wkd_entity_types_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wkd_entity_types_ss")

### wkd\_entity\_types\_ss Type

`string[]`

## wiki\_summaries\_t

Serialized JSON text blob of Wikipedia summaries in multiple languages for the entity.

`wiki_summaries_t`

* is optional

* Type: `string`

* can be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-wiki_summaries_t.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/wiki_summaries_t")

### wiki\_summaries\_t Type

`string`

## contexts\_ss

List of media-related contexts where the entity appears, in the same order as content item id list.

`contexts_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-contexts_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/contexts_ss")

### contexts\_ss Type

`string[]`

## entity\_mixed\_emb\_v768

Entiy embedding vector (combined signal from encyclopedic and media-related context).

`entity_mixed_emb_v768`

* is optional

* Type: `number[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-entity_mixed_emb_v768.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/entity_mixed_emb_v768")

### entity\_mixed\_emb\_v768 Type

`number[]`

### entity\_mixed\_emb\_v768 Constraints

**maximum number of items**: the maximum number of items for this array is: `768`

**minimum number of items**: the minimum number of items for this array is: `768`

## entity\_encyc\_emb\_v768

Entity embedding vector computed from encyclopedic text components (Wikidata/Wikipedia-based).

`entity_encyc_emb_v768`

* is optional

* Type: `number[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-entity_encyc_emb_v768.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/entity_encyc_emb_v768")

### entity\_encyc\_emb\_v768 Type

`number[]`

### entity\_encyc\_emb\_v768 Constraints

**maximum number of items**: the maximum number of items for this array is: `768`

**minimum number of items**: the minimum number of items for this array is: `768`

## entity\_media\_emb\_v768

Entity embedding vector computed from entity's mention text components (mention context windows).

`entity_media_emb_v768`

* is optional

* Type: `number[]`

* cannot be null

* defined in: [Entity Profile Embedding Document](sem-2-properties-entity_media_emb_v768.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entity-profiles.v1.schema.json#/properties/entity_media_emb_v768")

### entity\_media\_emb\_v768 Type

`number[]`

### entity\_media\_emb\_v768 Constraints

**maximum number of items**: the maximum number of items for this array is: `768`

**minimum number of items**: the minimum number of items for this array is: `768`
