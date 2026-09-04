## Topic Solr Document Type

`object` ([Topic Solr Document](sem-4.md))

# Topic Solr Document Properties

| Property                                              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                             |
| :---------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                             | `string`  | Required | cannot be null | [Topic Solr Document](sem-4-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/id")                                           |
| [lg\_s](#lg_s)                                        | `string`  | Required | cannot be null | [Topic Solr Document](sem-4-properties-lg_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/lg_s")                                       |
| [tp\_model\_s](#tp_model_s)                           | `string`  | Required | cannot be null | [Topic Solr Document](sem-4-properties-tp_model_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/tp_model_s")                           |
| [tp\_nb\_i](#tp_nb_i)                                 | `integer` | Required | cannot be null | [Topic Solr Document](sem-4-properties-tp_nb_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/tp_nb_i")                                 |
| [word\_probs\_dpf](#word_probs_dpf)                   | `string`  | Required | cannot be null | [Topic Solr Document](sem-4-properties-word_probs_dpf.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/word_probs_dpf")                   |
| [topic\_suggest](#topic_suggest)                      | `string`  | Required | cannot be null | [Topic Solr Document](sem-4-properties-topic_suggest.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/topic_suggest")                     |
| [tp\_desc\_s](#tp_desc_s)                             | `string`  | Optional | cannot be null | [Topic Solr Document](sem-4-properties-tp_desc_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/tp_desc_s")                             |
| [tp\_meta\_s](#tp_meta_s)                             | `string`  | Optional | cannot be null | [Topic Solr Document](sem-4-properties-tp_meta_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/tp_meta_s")                             |
| [topic\_type\_s](#topic_type_s)                       | `string`  | Optional | cannot be null | [Topic Solr Document](sem-4-properties-topic_type_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/topic_type_s")                       |
| [label\_short\_s](#label_short_s)                     | `string`  | Optional | cannot be null | [Topic Solr Document](sem-4-properties-label_short_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/label_short_s")                     |
| [label\_long\_txt\_en](#label_long_txt_en)            | `string`  | Optional | cannot be null | [Topic Solr Document](sem-4-properties-label_long_txt_en.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/label_long_txt_en")             |
| [confidence\_s](#confidence_s)                        | `string`  | Optional | cannot be null | [Topic Solr Document](sem-4-properties-confidence_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/confidence_s")                       |
| [representative\_terms\_ss](#representative_terms_ss) | `array`   | Optional | cannot be null | [Topic Solr Document](sem-4-properties-representative_terms_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/representative_terms_ss") |
| [generated\_by\_s](#generated_by_s)                   | `string`  | Optional | cannot be null | [Topic Solr Document](sem-4-properties-generated_by_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/generated_by_s")                   |
| Additional Properties                                 | Any       | Optional | can be null    |                                                                                                                                                                                                                                        |

## id

Unique identifier for the topic (format: model\_id\_tp{number}\_{lang})

`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/id")

### id Type

`string`

### id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^tm-[a-z]{2}-[a-z]+-v[0-9]+\.[0-9]+_tp[0-9]+_[a-z]{2}$
```

[try pattern](https://regexr.com/?expression=%5Etm-%5Ba-z%5D%7B2%7D-%5Ba-z%5D%2B-v%5B0-9%5D%2B%5C.%5B0-9%5D%2B_tp%5B0-9%5D%2B_%5Ba-z%5D%7B2%7D%24 "try regular expression with regexr.com")

## lg\_s

Language code (ISO lowercase)

`lg_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-lg_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/lg_s")

### lg\_s Type

`string`

### lg\_s Constraints

**maximum length**: the maximum number of characters for this string is: `2`

**minimum length**: the minimum number of characters for this string is: `2`

## tp\_model\_s

Topic model identifier

`tp_model_s`

* is required

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-tp_model_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/tp_model_s")

### tp\_model\_s Type

`string`

### tp\_model\_s Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^tm-[a-z]{2}-[a-z]+-v[0-9]+\.[0-9]+$
```

[try pattern](https://regexr.com/?expression=%5Etm-%5Ba-z%5D%7B2%7D-%5Ba-z%5D%2B-v%5B0-9%5D%2B%5C.%5B0-9%5D%2B%24 "try regular expression with regexr.com")

## tp\_nb\_i

Topic number (integer field)

`tp_nb_i`

* is required

* Type: `integer`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-tp_nb_i.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/tp_nb_i")

### tp\_nb\_i Type

`integer`

### tp\_nb\_i Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## word\_probs\_dpf

Word probabilities in DPFS format (space-separated pairs of 'word|probability')

`word_probs_dpf`

* is required

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-word_probs_dpf.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/word_probs_dpf")

### word\_probs\_dpf Type

`string`

### word\_probs\_dpf Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## topic\_suggest

Space-separated list of topic words for suggestion/autocomplete

`topic_suggest`

* is required

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-topic_suggest.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/topic_suggest")

### topic\_suggest Type

`string`

### topic\_suggest Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## tp\_desc\_s

Optional topic description

`tp_desc_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-tp_desc_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/tp_desc_s")

### tp\_desc\_s Type

`string`

## tp\_meta\_s

Optional topic metadata

`tp_meta_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-tp_meta_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/tp_meta_s")

### tp\_meta\_s Type

`string`

## topic\_type\_s

Topic category assigned by the label-generation model (e.g. 'advertisement', 'legal\_administrative') — topic labels v3. Optional: absent on pre-v3 topic-description-only documents.

`topic_type_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-topic_type_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/topic_type_s")

### topic\_type\_s Type

`string`

## label\_short\_s

Short human-readable topic label — topic labels v3. Optional: absent on pre-v3 topic-description-only documents.

`label_short_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-label_short_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/label_short_s")

### label\_short\_s Type

`string`

## label\_long\_txt\_en

Long-form English topic label/description, analyzed text — topic labels v3. Optional: absent on pre-v3 topic-description-only documents.

`label_long_txt_en`

* is optional

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-label_long_txt_en.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/label_long_txt_en")

### label\_long\_txt\_en Type

`string`

## confidence\_s

Confidence level of the generated label — topic labels v3. Optional: absent on pre-v3 topic-description-only documents.

`confidence_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-confidence_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/confidence_s")

### confidence\_s Type

`string`

### confidence\_s Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"high"`   |             |
| `"medium"` |             |
| `"low"`    |             |

## representative\_terms\_ss

Representative terms backing the generated topic label — topic labels v3. Optional: absent on pre-v3 topic-description-only documents.

`representative_terms_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-representative_terms_ss.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/representative_terms_ss")

### representative\_terms\_ss Type

`string[]`

## generated\_by\_s

Attribution for the topic-label generation process (e.g. 'OpenAI') — topic labels v3. Optional: absent on pre-v3 topic-description-only documents.

`generated_by_s`

* is optional

* Type: `string`

* cannot be null

* defined in: [Topic Solr Document](sem-4-properties-generated_by_s.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/semantic-enrichments/sem.root.topics.v1.schema.json#/properties/generated_by_s")

### generated\_by\_s Type

`string`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
