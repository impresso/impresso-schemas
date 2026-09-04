## Impresso timestamp Type

`string` ([Impresso timestamp](timestamp.md))

## Impresso timestamp Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7DT%5Cd%7B2%7D%3A%5Cd%7B2%7D%3A%5Cd%7B2%7DZ%24 "try regular expression with regexr.com")

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## Impresso timestamp Examples

```json
"2026-08-21T08:42:00Z"
```
