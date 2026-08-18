## Content-item identifier property Type

`object` ([Content-item identifier property](content-item-id.md))

# Content-item identifier property Properties

| Property         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                         |
| :--------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ci\_id](#ci_id) | `string` | Optional | cannot be null | [Content-item identifier property](content-item-id-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/content-item-id.part.v1.schema.json#/properties/ci_id") |

## ci\_id

Canonical identifier of an Impresso content item. A content item is the processing unit representing a segmented media object, or a whole page when no finer-grained segmentation is available.

`ci_id`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content-item identifier property](content-item-id-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/content-item-id.part.v1.schema.json#/properties/ci_id")

### ci\_id Type

`string`

### ci\_id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-i[0-9]{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z%5D%5BA-Za-z0-9_%5D*-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C2%7D-i%5B0-9%5D%7B4%7D%24 "try regular expression with regexr.com")

### ci\_id Examples

```json
"GDL-1900-01-02-a-i0001"
```

```json
"GDL-1900-01-02-ab-i0001"
```
