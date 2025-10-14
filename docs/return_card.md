## Data Return Card Type

`object` ([Data Return Card](return_card.md))

# Data Return Card Properties

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                 |
| :---------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ci\_id](#ci_id)                                | `string` | Required | cannot be null | [Data Return Card](return_card-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/ci_id")                               |
| [issue\_id](#issue_id)                          | `string` | Required | cannot be null | [Data Return Card](return_card-properties-issue_id.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/issue_id")                         |
| [timestamp](#timestamp)                         | `string` | Required | cannot be null | [Data Return Card](return_card-properties-timestamp.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/timestamp")                       |
| [partner\_institution](#partner_institution)    | `string` | Required | cannot be null | [Data Return Card](return_card-properties-partner_institution.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/partner_institution")   |
| [institution\_data\_ids](#institution_data_ids) | `array`  | Required | cannot be null | [Data Return Card](return_card-properties-institution_data_ids.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/institution_data_ids") |

## ci\_id

Impresso canonical ID of the content-item (e.g. `GDL-1900-01-02-a-i0001`)

`ci_id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/ci_id")

### ci\_id Type

`string`

### ci\_id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-i[0-9]{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z%5D%5BA-Za-z0-9_%5D*-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C2%7D-i%5B0-9%5D%7B4%7D%24 "try regular expression with regexr.com")

## issue\_id

Impresso canonical ID of the issue to which this issue belongs (e.g. `GDL-1900-01-02-a`)

`issue_id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-properties-issue_id.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/issue_id")

### issue\_id Type

`string`

### issue\_id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z%5D%5BA-Za-z0-9_%5D*-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C2%7D%24 "try regular expression with regexr.com")

## timestamp

Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format).

`timestamp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-properties-timestamp.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/timestamp")

### timestamp Type

`string`

### timestamp Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

## partner\_institution

Internal alias corresponding to the partner institution this CI comes from.

`partner_institution`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-properties-partner_institution.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/partner_institution")

### partner\_institution Type

`string`

## institution\_data\_ids

The legacy institution IDs corresponding to this content-item.

`institution_data_ids`

*   is required

*   Type: `object[]` ([Details](return_card-properties-institution_data_ids-items.md))

*   cannot be null

*   defined in: [Data Return Card](return_card-properties-institution_data_ids.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/properties/institution_data_ids")

### institution\_data\_ids Type

`object[]` ([Details](return_card-properties-institution_data_ids-items.md))

# Data Return Card Definitions

## Definitions group institution\_data\_id

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id"}
```

| Property                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                            |
| :-------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                               | Multiple  | Required | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-id.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/id")                             |
| [granularity](#granularity)             | `string`  | Required | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/granularity")           |
| [is\_primary](#is_primary)              | `boolean` | Optional | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-is_primary.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_primary")             |
| [is\_permanent](#is_permanent)          | `boolean` | Required | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-is_permanent.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_permanent")         |
| [is\_public\_facing](#is_public_facing) | `boolean` | Required | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-is_public_facing.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_public_facing") |
| [corresp\_url](#corresp_url)            | `string`  | Optional | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-corresp_url.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/corresp_url")           |
| [notes](#notes)                         | `string`  | Optional | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-notes.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/notes")                       |

### id

Legacy or institution identifier linked to the CI.

`id`

*   is required

*   Type: any of the following: `string` or `integer` or `number` ([Details](return_card-defs-institution_data_id-properties-id.md))

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-id.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/id")

#### id Type

any of the following: `string` or `integer` or `number` ([Details](return_card-defs-institution_data_id-properties-id.md))

### granularity

Granularity level this identifier corresponds to. At least one ID must be issue-level

`granularity`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/granularity")

#### granularity Type

`string`

#### granularity Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"media_title"`  |             |
| `"issue"`        |             |
| `"page"`         |             |
| `"audio"`        |             |
| `"support"`      |             |
| `"sub-page"`     |             |
| `"article"`      |             |
| `"content-item"` |             |

### is\_primary

Whether the identifier is used as primary or anchor identifier by the insitution.

`is_primary`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-is_primary.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_primary")

#### is\_primary Type

`boolean`

### is\_permanent

Whether the identifier is stable and/or permanent (eg. ark ID).

`is_permanent`

*   is required

*   Type: `boolean`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-is_permanent.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_permanent")

#### is\_permanent Type

`boolean`

### is\_public\_facing

Whether the identifier is public facing, ie. if it is present in an insitution URL which could be used.

`is_public_facing`

*   is required

*   Type: `boolean`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-is_public_facing.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_public_facing")

#### is\_public\_facing Type

`boolean`

### corresp\_url

URL containing or using this identifier linking to the piece of content corresponding to this CI in the institution portal or interface.

`corresp_url`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-corresp_url.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/corresp_url")

#### corresp\_url Type

`string`

### notes

Notes, description or useful information relating to this identifier.

`notes`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-notes.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/notes")

#### notes Type

`string`
