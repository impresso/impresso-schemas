## ts Type

`string` ([The Ts Schema](embeddings-docs-backup-properties-the-ts-schema.md))

## ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\+00:00|Z)$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D\(%5C%2B00%3A00%7CZ\)%24 "try regular expression with regexr.com")

## ts Examples

```json
"2024-08-29T06:42:53+00:00Z"
```
