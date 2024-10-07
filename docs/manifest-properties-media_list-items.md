## items Type

`object` ([Details](manifest-properties-media_list-items.md))

# items Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                         |
| :-------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [media\_title](#media_title)                        | `string` | Required | cannot be null | [Versioning Manifest](manifest-properties-media_list-items-properties-media_title.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/media_title")                       |
| [last\_modification\_date](#last_modification_date) | `string` | Required | cannot be null | [Versioning Manifest](manifest-properties-media_list-items-properties-last_modification_date.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/last_modification_date") |
| [update\_type](#update_type)                        | `string` | Required | can be null    | [Versioning Manifest](manifest-properties-media_list-items-properties-update_type.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/update_type")                       |
| [update\_level](#update_level)                      | `string` | Required | can be null    | [Versioning Manifest](manifest-properties-media_list-items-properties-update_level.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/update_level")                     |
| [updated\_years](#updated_years)                    | `array`  | Required | cannot be null | [Versioning Manifest](manifest-properties-media_list-items-properties-updated_years.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/updated_years")                   |
| [updated\_fields](#updated_fields)                  | `array`  | Required | cannot be null | [Versioning Manifest](manifest-properties-media_list-items-properties-updated_fields.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/updated_fields")                 |
| [code\_git\_commit](#code_git_commit)               | `string` | Required | can be null    | [Versioning Manifest](manifest-properties-media_list-items-properties-code_git_commit.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/code_git_commit")               |
| [media\_statistics](#media_statistics)              | `array`  | Required | cannot be null | [Versioning Manifest](manifest-properties-media_list-items-properties-media_statistics.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/media_statistics")             |

## media\_title

Internal alias of newspaper newspaper (or program for radio).

`media_title`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-properties-media_list-items-properties-media_title.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/media_title")

### media\_title Type

`string`

## last\_modification\_date

Date timestamp of last modification of this specific media.

`last_modification_date`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-properties-media_list-items-properties-last_modification_date.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/last_modification_date")

### last\_modification\_date Type

`string`

## update\_type

Type of update made to the data.

`update_type`

*   is required

*   Type: `string`

*   can be null

*   defined in: [Versioning Manifest](manifest-properties-media_list-items-properties-update_type.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/update_type")

### update\_type Type

`string`

### update\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"addition"`     |             |
| `"modification"` |             |
| `null`           |             |

## update\_level

How much this media was updated (only a few issues, years or entire media title).

`update_level`

*   is required

*   Type: `string`

*   can be null

*   defined in: [Versioning Manifest](manifest-properties-media_list-items-properties-update_level.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/update_level")

### update\_level Type

`string`

### update\_level Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"title"` |             |
| `"year"`  |             |
| `null`    |             |

## updated\_years

List of years which were updated. Empty if entire media title was re-ingested or patched.

`updated_years`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-properties-media_list-items-properties-updated_years.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/updated_years")

### updated\_years Type

`string[]`

## updated\_fields

List of (json output) properties which were updated. Empty if all properties were modified or re-ingested.

`updated_fields`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [Versioning Manifest](manifest-properties-media_list-items-properties-updated_fields.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/updated_fields")

### updated\_fields Type

`string[]`

## code\_git\_commit

Link to git commit of the code used to generate/modify the output data.

`code_git_commit`

*   is required

*   Type: `string`

*   can be null

*   defined in: [Versioning Manifest](manifest-properties-media_list-items-properties-code_git_commit.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/code_git_commit")

### code\_git\_commit Type

`string`

## media\_statistics

List of statistics describing the contents of the data. The first element is at title level, the following ones are yearly.

`media_statistics`

*   is required

*   Type: `object[]` ([Details](manifest-definitions-media_statistics.md))

*   cannot be null

*   defined in: [Versioning Manifest](manifest-properties-media_list-items-properties-media_statistics.md "https://impresso.github.io/impresso-schemas/json/versioning/manifest.schema.json#/properties/media_list/items/properties/media_statistics")

### media\_statistics Type

`object[]` ([Details](manifest-definitions-media_statistics.md))

### media\_statistics Constraints

**minimum number of items**: the minimum number of items for this array is: `2`
