# Untitled string in Newspaper Issue Schema

```txt
https://impresso.github.io/impresso-schemas/json/newspaper/issue.schema.json#/properties/ar
```

Access rights. Three possible situations are defined:
1\. open public: access without NDA, user could redistribute (as defined per Terms of Use)
2\. open private: access without an NDA, user cannot redistribute (private/academic use only)
3\. closed : accessible only upon signing an NDA, user cannot redistribute


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [issue.schema.json\*](../out/issue.schema.json "open original schema") |

## ar Type

`string`

## ar Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | ----------- |
| `"open_public"`  |             |
| `"open_private"` |             |
| `"closed"`       |             |
