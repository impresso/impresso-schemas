## Impresso ts property Type

`object` ([Impresso ts property](ts.md))

# Impresso ts property Properties

| Property  | Type     | Required | Nullable       | Defined by                                                                                                                                        |
| :-------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ts](#ts) | `string` | Optional | cannot be null | [Impresso ts property](timestamp.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/timestamp.v1.schema.json#/properties/ts") |

## ts

Canonical representation of a timestamp in Impresso data. Timestamps are expressed in UTC with second precision using the form `YYYY-MM-DDTHH:MM:SSZ`. This schema defines the representation of a point in time; the semantic meaning of that point, such as creation, modification, or processing time, is defined by the property that references this schema. The preferred property name for a generic processing or creation timestamp is `ts` where no more specific name is required.

`ts`

* is optional

* Type: `string` ([Impresso timestamp](timestamp.md))

* cannot be null

* defined in: [Impresso ts property](timestamp.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/timestamp.v1.schema.json#/properties/ts")

### ts Type

`string` ([Impresso timestamp](timestamp.md))

### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7DT%5Cd%7B2%7D%3A%5Cd%7B2%7D%3A%5Cd%7B2%7DZ%24 "try regular expression with regexr.com")

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

### ts Examples

```json
"2026-08-21T08:42:00Z"
```
