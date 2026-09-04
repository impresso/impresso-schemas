## 3 Type

`object` ([AccessRightFields](sem-6-allof-accessrightfields.md))

# 3 Properties

| Property                                                             | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                    |
| :------------------------------------------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rights\_data\_domain\_s](#rights_data_domain_s)                     | Merged    | Required | cannot be null | [AccessRightFields](content-item-3-properties-legal-status.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_data_domain_s")                                                       |
| [rights\_copyright\_s](#rights_copyright_s)                          | Merged    | Required | cannot be null | [AccessRightFields](content-item-3-properties-copyright-status.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_copyright_s")                                                     |
| [rights\_perm\_use\_explore\_plain](#rights_perm_use_explore_plain)  | Merged    | Required | cannot be null | [AccessRightFields](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_perm_use_explore_plain")   |
| [rights\_perm\_use\_get\_tr\_plain](#rights_perm_use_get_tr_plain)   | Merged    | Required | cannot be null | [AccessRightFields](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used-1.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_perm_use_get_tr_plain")  |
| [rights\_perm\_use\_get\_img\_plain](#rights_perm_use_get_img_plain) | Merged    | Required | cannot be null | [AccessRightFields](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used-2.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_perm_use_get_img_plain") |
| [rights\_bm\_explore\_l](#rights_bm_explore_l)                       | `integer` | Required | cannot be null | [AccessRightFields](content-item-3-properties-rights_bm_explore_l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_bm_explore_l")                                                 |
| [rights\_bm\_get\_tr\_l](#rights_bm_get_tr_l)                        | `integer` | Required | cannot be null | [AccessRightFields](content-item-3-properties-rights_bm_get_tr_l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_bm_get_tr_l")                                                   |
| [rights\_bm\_get\_img\_l](#rights_bm_get_img_l)                      | `integer` | Required | cannot be null | [AccessRightFields](content-item-3-properties-rights_bm_get_img_l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_bm_get_img_l")                                                 |
| `^rights_explore_b\d+_b$`                                            | `boolean` | Optional | cannot be null | [AccessRightFields](content-item-3-patternproperties-rights_explore_bd_b.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/patternProperties/^rights_explore_b\d+_b$")                               |
| `^rights_get_tr_b\d+_b$`                                             | `boolean` | Optional | cannot be null | [AccessRightFields](content-item-3-patternproperties-rights_get_tr_bd_b.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/patternProperties/^rights_get_tr_b\d+_b$")                                 |
| `^rights_get_img_b\d+_b$`                                            | `boolean` | Optional | cannot be null | [AccessRightFields](content-item-3-patternproperties-rights_get_img_bd_b.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/patternProperties/^rights_get_img_b\d+_b$")                               |
| Additional Properties                                                | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                               |

## rights\_data\_domain\_s

Rights data domain

`rights_data_domain_s`

* is required

* Type: `string` ([Legal status](content-item-3-properties-legal-status.md))

* cannot be null

* defined in: [AccessRightFields](content-item-3-properties-legal-status.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_data_domain_s")

### rights\_data\_domain\_s Type

`string` ([Legal status](content-item-3-properties-legal-status.md))

one (and only one) of

* [Public domain](content-item-3-properties-legal-status-oneof-public-domain.md "check type definition")

* [In copyright](content-item-3-properties-legal-status-oneof-in-copyright.md "check type definition")

## rights\_copyright\_s

Copyright status of the content.

`rights_copyright_s`

* is required

* Type: `string` ([Copyright status](content-item-3-properties-copyright-status.md))

* cannot be null

* defined in: [AccessRightFields](content-item-3-properties-copyright-status.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_copyright_s")

### rights\_copyright\_s Type

`string` ([Copyright status](content-item-3-properties-copyright-status.md))

one (and only one) of

* [Public domain](content-item-3-properties-copyright-status-oneof-public-domain.md "check type definition")

* [Copyright undetermined](content-item-3-properties-copyright-status-oneof-copyright-undetermined.md "check type definition")

* [No known copyright](content-item-3-properties-copyright-status-oneof-no-known-copyright.md "check type definition")

* [EU orphan work](content-item-3-properties-copyright-status-oneof-eu-orphan-work.md "check type definition")

* [Unknown rightsholders](content-item-3-properties-copyright-status-oneof-unknown-rightsholders.md "check type definition")

* [In copyright](content-item-3-properties-copyright-status-oneof-in-copyright.md "check type definition")

## rights\_perm\_use\_explore\_plain

Permission level for exploratory use of the content (e.g. browsing, inspection, discovery).

`rights_perm_use_explore_plain`

* is required

* Type: `string` ([Permission level indicating how the content may be used.](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used.md))

* cannot be null

* defined in: [AccessRightFields](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_perm_use_explore_plain")

### rights\_perm\_use\_explore\_plain Type

`string` ([Permission level indicating how the content may be used.](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used.md))

one (and only one) of

* [Personal, Research and Educational use](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-personal-research-and-educational-use.md "check type definition")

* [Research and Educational use](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-research-and-educational-use.md "check type definition")

* [Research use](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-research-use.md "check type definition")

* [No usage restriction](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-no-usage-restriction.md "check type definition")

* [Operation not permitted](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-operation-not-permitted.md "check type definition")

## rights\_perm\_use\_get\_tr\_plain

Permission level for retrieving textual representations of the content.

`rights_perm_use_get_tr_plain`

* is required

* Type: `string` ([Permission level indicating how the content may be used.](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used-1.md))

* cannot be null

* defined in: [AccessRightFields](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used-1.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_perm_use_get_tr_plain")

### rights\_perm\_use\_get\_tr\_plain Type

`string` ([Permission level indicating how the content may be used.](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used-1.md))

one (and only one) of

* [Personal, Research and Educational use](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-personal-research-and-educational-use.md "check type definition")

* [Research and Educational use](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-research-and-educational-use.md "check type definition")

* [Research use](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-research-use.md "check type definition")

* [No usage restriction](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-no-usage-restriction.md "check type definition")

* [Operation not permitted](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-operation-not-permitted.md "check type definition")

## rights\_perm\_use\_get\_img\_plain

Permission level for retrieving image representations of the content.

`rights_perm_use_get_img_plain`

* is required

* Type: `string` ([Permission level indicating how the content may be used.](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used-2.md))

* cannot be null

* defined in: [AccessRightFields](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used-2.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_perm_use_get_img_plain")

### rights\_perm\_use\_get\_img\_plain Type

`string` ([Permission level indicating how the content may be used.](content-item-3-properties-permission-level-indicating-how-the-content-may-be-used-2.md))

one (and only one) of

* [Personal, Research and Educational use](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-personal-research-and-educational-use.md "check type definition")

* [Research and Educational use](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-research-and-educational-use.md "check type definition")

* [Research use](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-research-use.md "check type definition")

* [No usage restriction](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-no-usage-restriction.md "check type definition")

* [Operation not permitted](content-item-3-defs-permission-level-indicating-how-the-content-may-be-used-oneof-operation-not-permitted.md "check type definition")

## rights\_bm\_explore\_l

Bookmark limit for exploration.

`rights_bm_explore_l`

* is required

* Type: `integer`

* cannot be null

* defined in: [AccessRightFields](content-item-3-properties-rights_bm_explore_l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_bm_explore_l")

### rights\_bm\_explore\_l Type

`integer`

## rights\_bm\_get\_tr\_l

Bookmark limit for text retrieval.

`rights_bm_get_tr_l`

* is required

* Type: `integer`

* cannot be null

* defined in: [AccessRightFields](content-item-3-properties-rights_bm_get_tr_l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_bm_get_tr_l")

### rights\_bm\_get\_tr\_l Type

`integer`

## rights\_bm\_get\_img\_l

Bookmark limit for image retrieval.

`rights_bm_get_img_l`

* is required

* Type: `integer`

* cannot be null

* defined in: [AccessRightFields](content-item-3-properties-rights_bm_get_img_l.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/properties/rights_bm_get_img_l")

### rights\_bm\_get\_img\_l Type

`integer`

## Pattern: `^rights_explore_b\d+_b$`

Individual bitmap position for exploration rights. Field name format: rights\_explore\_b{position}\_b where position is the bit index (0-63). Only positions with value true are stored.

`^rights_explore_b\d+_b$`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [AccessRightFields](content-item-3-patternproperties-rights_explore_bd_b.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/patternProperties/^rights_explore_b\d+_b$")

### ^rights\_explore\_b\d+\_b$ Type

`boolean`

## Pattern: `^rights_get_tr_b\d+_b$`

Individual bitmap position for text retrieval rights. Field name format: rights\_get\_tr\_b{position}\_b where position is the bit index (0-63). Only positions with value true are stored.

`^rights_get_tr_b\d+_b$`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [AccessRightFields](content-item-3-patternproperties-rights_get_tr_bd_b.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/patternProperties/^rights_get_tr_b\d+_b$")

### ^rights\_get\_tr\_b\d+\_b$ Type

`boolean`

## Pattern: `^rights_get_img_b\d+_b$`

Individual bitmap position for image retrieval rights. Field name format: rights\_get\_img\_b{position}\_b where position is the bit index (0-63). Only positions with value true are stored.

`^rights_get_img_b\d+_b$`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [AccessRightFields](content-item-3-patternproperties-rights_get_img_bd_b.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/patternProperties/^rights_get_img_b\d+_b$")

### ^rights\_get\_img\_b\d+\_b$ Type

`boolean`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema

# AccessRightFields Definitions

## Definitions group permittedUse

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.access-rights.v1.schema.json#/$defs/permittedUse"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
