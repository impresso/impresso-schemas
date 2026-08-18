## Entity Mention Solr Document Type

`object` ([Entity Mention Solr Document](sem-3.md))

# Entity Mention Solr Document Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :-------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [l\_s](#l_s)          | `string` | Required | cannot be null | [Entity Mention Solr Document](sem-3-properties-l_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json#/properties/l_s")   |
| [t\_s](#t_s)          | `string` | Required | cannot be null | [Entity Mention Solr Document](sem-3-properties-t_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json#/properties/t_s")   |
| [fq\_f](#fq_f)        | `number` | Required | cannot be null | [Entity Mention Solr Document](sem-3-properties-fq_f.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json#/properties/fq_f") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                             |

## l\_s

The label/surface form of the entity mention

`l_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Entity Mention Solr Document](sem-3-properties-l_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json#/properties/l_s")

### l\_s Type

`string`

### l\_s Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## t\_s

Type of the entity (e.g., 'pers' for person, 'loc' for location, 'org' for organization)

`t_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Entity Mention Solr Document](sem-3-properties-t_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json#/properties/t_s")

### t\_s Type

`string`

### t\_s Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"pers"` |             |
| `"loc"`  |             |
| `"org"`  |             |

## fq\_f

Frequency of the mention (as float)

`fq_f`

* is required

* Type: `number`

* cannot be null

* defined in: [Entity Mention Solr Document](sem-3-properties-fq_f.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.mentions.v1.schema.json#/properties/fq_f")

### fq\_f Type

`number`

### fq\_f Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
