## OCR Quality Assessment Schema Type

`object` ([OCR Quality Assessment Schema](ocr_qa.md))

# OCR Quality Assessment Schema Properties

| Property                                         | Type      | Required | Nullable       | Defined by                                                                                                                                                                               |
| :----------------------------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ci\_id](#ci_id)                                 | `string`  | Required | cannot be null | [OCR Quality Assessment Schema](ocr_qa-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ci_id")                               |
| [ocrqa](#ocrqa)                                  | `number`  | Required | can be null    | [OCR Quality Assessment Schema](ocr_qa-properties-ocrqa.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ocrqa")                               |
| [ts](#ts)                                        | `string`  | Optional | cannot be null | [OCR Quality Assessment Schema](ocr_qa-properties-timestamp.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ts")                              |
| [lg](#lg)                                        | `string`  | Optional | cannot be null | [OCR Quality Assessment Schema](ocr_qa-properties-lg.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/lg")                                     |
| [bloom](#bloom)                                  | `string`  | Optional | cannot be null | [OCR Quality Assessment Schema](ocr_qa-properties-bloom.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/bloom")                               |
| [subtokens](#subtokens)                          | `integer` | Optional | cannot be null | [OCR Quality Assessment Schema](ocr_qa-properties-subtokens.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/subtokens")                       |
| [timestamp](#timestamp)                          | `string`  | Optional | cannot be null | [OCR Quality Assessment Schema](ocr_qa-properties-timestamp-1.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/timestamp")                     |
| [git\_version](#git_version)                     | `string`  | Optional | cannot be null | [OCR Quality Assessment Schema](ocr_qa-properties-git_version.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/git_version")                   |
| [subtoken\_char\_ratio](#subtoken_char_ratio)    | `number`  | Optional | cannot be null | [OCR Quality Assessment Schema](ocr_qa-properties-subtoken_char_ratio.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/subtoken_char_ratio")   |
| [ocrqa\_unk\_type\_ratio](#ocrqa_unk_type_ratio) | `number`  | Optional | cannot be null | [OCR Quality Assessment Schema](ocr_qa-properties-ocrqa_unk_type_ratio.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ocrqa_unk_type_ratio") |
| Additional Properties                            | Any       | Optional | can be null    |                                                                                                                                                                                          |

## ci\_id

Globally unique string identifier referencing the content item, typically corresponding to an article or a full page if no OLR is available.

`ci_id`

* is required

* Type: `string`

* cannot be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-ci_id.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ci_id")

### ci\_id Type

`string`

## ocrqa

Estimated OCR quality score, expressed as a decimal value between 0.0 (poor) and 1.0 (excellent). Value must be between 0.0 and 1.0, inclusive. May be null if the text is too short to assess.

`ocrqa`

* is required

* Type: `number`

* can be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-ocrqa.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ocrqa")

### ocrqa Type

`number`

### ocrqa Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## ts

ISO 8601 formatted timestamp indicating when the OCR quality assessment was performed. This is the primary field for recording assessment time.

`ts`

* is optional

* Type: `string` ([Timestamp](ocr_qa-properties-timestamp.md))

* cannot be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-timestamp.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ts")

### ts Type

`string` ([Timestamp](ocr_qa-properties-timestamp.md))

### ts Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

### ts Examples

```json
"2024-12-27T16:38:46Z"
```

## lg

ISO 639-1 two-letter language code of the content item (e.g., 'de' for German, 'fr' for French).

`lg`

* is optional

* Type: `string`

* cannot be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-lg.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/lg")

### lg Type

`string`

### lg Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-z]{2}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z%5D%7B2%7D%24 "try regular expression with regexr.com")

### lg Examples

```json
"de"
```

```json
"fr"
```

```json
"en"
```

## bloom

Reference to the Bloom filter dictionary used for lexical matching. Typically a Hugging Face Hub reference (e.g., 'hf://impresso-project/...') or a local file path.

`bloom`

* is optional

* Type: `string`

* cannot be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-bloom.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/bloom")

### bloom Type

`string`

### bloom Examples

```json
"hf://impresso-project/OCR-quality-assessment-unigram/ocrqa-wp_v1.0.6-de.bloom"
```

## subtokens

Number of subtokens (word-level tokens) identified in the content item during OCR quality assessment.

`subtokens`

* is optional

* Type: `integer`

* cannot be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-subtokens.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/subtokens")

### subtokens Type

`integer`

### subtokens Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### subtokens Examples

```json
11
```

```json
1272
```

```json
811
```

## timestamp

(Deprecated) ISO 8601 formatted timestamp indicating when the OCR quality assessment was performed. Use 'ts' for consistency with other impresso schemas.

`timestamp`

* is optional

* Type: `string`

* cannot be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-timestamp-1.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/timestamp")

### timestamp Type

`string`

### timestamp Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D-%5B0-9%5D%7B2%7DT%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7D%3A%5B0-9%5D%7B2%7DZ%24 "try regular expression with regexr.com")

### timestamp Examples

```json
"2025-09-10T14:26:38Z"
```

## git\_version

Git commit hash of the OCR quality assessment codebase version used for processing, supporting reproducibility and version tracking.

`git_version`

* is optional

* Type: `string`

* cannot be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-git_version.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/git_version")

### git\_version Type

`string`

### git\_version Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-fA-F]{7,40}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-fA-F%5D%7B7%2C40%7D%24 "try regular expression with regexr.com")

### git\_version Examples

```json
"7f70279"
```

## subtoken\_char\_ratio

Ratio of subtokens to characters in the content item, providing insight into text density and tokenization characteristics.

`subtoken_char_ratio`

* is optional

* Type: `number`

* cannot be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-subtoken_char_ratio.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/subtoken_char_ratio")

### subtoken\_char\_ratio Type

`number`

### subtoken\_char\_ratio Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### subtoken\_char\_ratio Examples

```json
0.175
```

```json
0.151
```

```json
0.182
```

## ocrqa\_unk\_type\_ratio

Ratio of recognized unique subtoken types to all unique subtoken types, measuring the proportion of unique words found in the Bloom filter dictionary.

`ocrqa_unk_type_ratio`

* is optional

* Type: `number`

* cannot be null

* defined in: [OCR Quality Assessment Schema](ocr_qa-properties-ocrqa_unk_type_ratio.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ocrqa_unk_type_ratio")

### ocrqa\_unk\_type\_ratio Type

`number`

### ocrqa\_unk\_type\_ratio Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

### ocrqa\_unk\_type\_ratio Examples

```json
1
```

```json
0.96
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
