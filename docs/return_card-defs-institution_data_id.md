## institution\_data\_id Type

`object` ([Details](return_card-defs-institution_data_id.md))

# institution\_data\_id Properties

| Property                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                            |
| :-------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                               | Multiple  | Required | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-id.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/id")                             |
| [granularity](#granularity)             | `string`  | Required | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/granularity")           |
| [is\_primary](#is_primary)              | `boolean` | Optional | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-is_primary.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_primary")             |
| [is\_permanent](#is_permanent)          | `boolean` | Required | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-is_permanent.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_permanent")         |
| [is\_public\_facing](#is_public_facing) | `boolean` | Required | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-is_public_facing.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_public_facing") |
| [corresp\_url](#corresp_url)            | `string`  | Optional | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-corresp_url.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/corresp_url")           |
| [notes](#notes)                         | `string`  | Optional | cannot be null | [Data Return Card](return_card-defs-institution_data_id-properties-notes.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/notes")                       |

## id

Legacy or institution identifier linked to the CI.

`id`

*   is required

*   Type: any of the following: `string` or `integer` or `number` ([Details](return_card-defs-institution_data_id-properties-id.md))

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-id.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/id")

### id Type

any of the following: `string` or `integer` or `number` ([Details](return_card-defs-institution_data_id-properties-id.md))

## granularity

Granularity level this identifier corresponds to. At least one ID must be issue-level

`granularity`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-granularity.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/granularity")

### granularity Type

`string`

### granularity Constraints

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

## is\_primary

Whether the identifier is used as primary or anchor identifier by the insitution.

`is_primary`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-is_primary.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_primary")

### is\_primary Type

`boolean`

## is\_permanent

Whether the identifier is stable and/or permanent (eg. ark ID).

`is_permanent`

*   is required

*   Type: `boolean`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-is_permanent.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_permanent")

### is\_permanent Type

`boolean`

## is\_public\_facing

Whether the identifier is public facing, ie. if it is present in an insitution URL which could be used.

`is_public_facing`

*   is required

*   Type: `boolean`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-is_public_facing.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/is_public_facing")

### is\_public\_facing Type

`boolean`

## corresp\_url

URL containing or using this identifier linking to the piece of content corresponding to this CI in the institution portal or interface.

`corresp_url`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-corresp_url.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/corresp_url")

### corresp\_url Type

`string`

## notes

Notes, description or useful information relating to this identifier.

`notes`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Data Return Card](return_card-defs-institution_data_id-properties-notes.md "https://impresso.github.io/impresso-schemas/json/return_card/return_card.schema.json#/$defs/institution_data_id/properties/notes")

### notes Type

`string`
