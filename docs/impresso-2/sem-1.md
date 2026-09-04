## Entity Solr Document Type

`object` ([Entity Solr Document](sem-1.md))

# Entity Solr Document Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                          |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                       | `string` | Required | cannot be null | [Entity Solr Document](sem-1-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/id")                     |
| [sqlid\_s](#sqlid_s)            | `string` | Required | cannot be null | [Entity Solr Document](sem-1-properties-sqlid_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/sqlid_s")           |
| [l\_s](#l_s)                    | `string` | Required | cannot be null | [Entity Solr Document](sem-1-properties-l_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/l_s")                   |
| [t\_s](#t_s)                    | `string` | Required | cannot be null | [Entity Solr Document](sem-1-properties-t_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/t_s")                   |
| [p\_s](#p_s)                    | `string` | Required | cannot be null | [Entity Solr Document](sem-1-properties-p_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/p_s")                   |
| [article\_fq\_f](#article_fq_f) | `number` | Required | cannot be null | [Entity Solr Document](sem-1-properties-article_fq_f.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/article_fq_f") |
| [mention\_fq\_f](#mention_fq_f) | `number` | Optional | cannot be null | [Entity Solr Document](sem-1-properties-mention_fq_f.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/mention_fq_f") |
| Additional Properties           | Any      | Optional | can be null    |                                                                                                                                                                                                                     |

## id

Unique identifier of the entity.

`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Entity Solr Document](sem-1-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/id")

### id Type

`string`

## sqlid\_s

SQL-compatible identifier for the entity. Same as 'id'. Composed of run-id alias, entity-id, and master label

`sqlid_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Entity Solr Document](sem-1-properties-sqlid_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/sqlid_s")

### sqlid\_s Type

`string`

## l\_s

Language code of the entity.

`l_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Entity Solr Document](sem-1-properties-l_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/l_s")

### l\_s Type

`string`

## t\_s

Entity label or normalized textual form.

`t_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Entity Solr Document](sem-1-properties-t_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/t_s")

### t\_s Type

`string`

## p\_s

Composite identifier combining entity id and label. Composite path (original\_id|type)

`p_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Entity Solr Document](sem-1-properties-p_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/p_s")

### p\_s Type

`string`

## article\_fq\_f

Article frequency for the entity.

`article_fq_f`

* is required

* Type: `number`

* cannot be null

* defined in: [Entity Solr Document](sem-1-properties-article_fq_f.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/article_fq_f")

### article\_fq\_f Type

`number`

### article\_fq\_f Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## mention\_fq\_f

Mention frequency for the entity over the whole corpus.

`mention_fq_f`

* is optional

* Type: `number`

* cannot be null

* defined in: [Entity Solr Document](sem-1-properties-mention_fq_f.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.entities.v1.schema.json#/properties/mention_fq_f")

### mention\_fq\_f Type

`number`

### mention\_fq\_f Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
