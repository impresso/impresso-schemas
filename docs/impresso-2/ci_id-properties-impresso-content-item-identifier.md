## ci\_id Type

`string` ([Impresso content-item identifier](ci_id-properties-impresso-content-item-identifier.md))

## ci\_id Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Za-z][A-Za-z0-9_]*-\d{4}-\d{2}-\d{2}-[a-z]{1,2}-i[0-9]{4}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Za-z%5D%5BA-Za-z0-9_%5D*-%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D-%5Ba-z%5D%7B1%2C2%7D-i%5B0-9%5D%7B4%7D%24 "try regular expression with regexr.com")

## ci\_id Examples

```json
"GDL-1900-01-02-a-i0001"
```

```json
"GDL-1900-01-02-ab-i0001"
```
