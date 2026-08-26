## 0 Type

`object` ([Impresso ci\_id property](ocr-qa-allof-impresso-ci_id-property.md))

# 0 Properties

| Property         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                             |
| :--------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ci\_id](#ci_id) | `string` | Optional | cannot be null | [Impresso ci\_id property](ci_id-properties-impresso-content-item-identifier.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/content-item-id.v1.schema.json#/properties/ci_id") |

## ci\_id

Canonical identifier of an Impresso content item. The preferred property name for this value in Impresso schemas is `ci_id`, although other property names may be used in specific contexts. The identifier has the normative form `<media-alias>-<YYYY>-<MM>-<DD>-<edition>-i<sequence>`, where `<media-alias` identifies the media source via a short impresso-internal alias, `<YYYY>-<MM>-<DD>` is the publication date, `<edition>` identifies the edition for that date, and `<sequence>` is the four-digit content-item sequence number within the edition. This schema defines the identifier value independently of the property name under which it is stored.

`ci_id`

* is optional

* Type: `string` ([Impresso content-item identifier](ci_id-properties-impresso-content-item-identifier.md))

* cannot be null

* defined in: [Impresso ci\_id property](ci_id-properties-impresso-content-item-identifier.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/content-item-id.v1.schema.json#/properties/ci_id")

### ci\_id Type

`string` ([Impresso content-item identifier](ci_id-properties-impresso-content-item-identifier.md))

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
