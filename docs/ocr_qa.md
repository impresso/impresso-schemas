## OCR-QA JSON Schema Type

`object` ([OCR-QA JSON Schema](ocr_qa.md))

# OCR-QA JSON Schema Properties

| Property           | Type     | Required | Nullable       | Defined by                                                                                                                                        |
| :----------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ci\_ref](#ci_ref) | `string` | Required | cannot be null | [OCR-QA JSON Schema](ocr_qa-properties-ci_ref.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ci_ref") |
| [ocrqa](#ocrqa)    | `number` | Required | cannot be null | [OCR-QA JSON Schema](ocr_qa-properties-ocrqa.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ocrqa")   |

## ci\_ref

Reference to canonical content item id, typically an article

`ci_ref`

* is required

* Type: `string`

* cannot be null

* defined in: [OCR-QA JSON Schema](ocr_qa-properties-ci_ref.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ci_ref")

### ci\_ref Type

`string`

## ocrqa

The estimated OCR quality, between 0 and 1

`ocrqa`

* is required

* Type: `number`

* cannot be null

* defined in: [OCR-QA JSON Schema](ocr_qa-properties-ocrqa.md "https://impresso.github.io/impresso-schemas/json/ocr_qa/ocr_qa.schema.json#/properties/ocrqa")

### ocrqa Type

`number`
