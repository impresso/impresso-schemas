## Image Classification Type

`object` ([Image Classification](image-classification.md))

all of

* [Content-item identifier property](ocr-qa-allof-content-item-identifier-property.md "check type definition")

* [Model identifier property](lingproc-allof-model-identifier-property.md "check type definition")

# Image Classification Properties

| Property                                   | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                              |
| :----------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ts](#ts)                                  | `string` | Required | cannot be null | [Image Classification](image-classification-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/properties/ts")                                 |
| [level1\_predictions](#level1_predictions) | `array`  | Optional | cannot be null | [Image Classification](image-classification-properties-level1_predictions.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/properties/level1_predictions") |
| [level2\_predictions](#level2_predictions) | `array`  | Optional | cannot be null | [Image Classification](image-classification-properties-level2_predictions.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/properties/level2_predictions") |
| [level3\_predictions](#level3_predictions) | `array`  | Required | cannot be null | [Image Classification](image-classification-properties-level3_predictions.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/properties/level3_predictions") |

## ts

Timestamp indicating when the embedding was created (e.g., '2024-10-09T09:29:02Z').

`ts`

* is required

* Type: `string`

* cannot be null

* defined in: [Image Classification](image-classification-properties-ts.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/properties/ts")

### ts Type

`string`

### ts Constraints

**date time**: the string must be a date time string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## level1\_predictions

List of top-k predictions for level 1 for this image CI, (we will use k=3).

`level1_predictions`

* is optional

* Type: `object[]` ([Details](image-classification-properties-level1_predictions-items.md))

* cannot be null

* defined in: [Image Classification](image-classification-properties-level1_predictions.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/properties/level1_predictions")

### level1\_predictions Type

`object[]` ([Details](image-classification-properties-level1_predictions-items.md))

## level2\_predictions

List of top-k predictions for level 2 for this image CI, (we will use k=3).

`level2_predictions`

* is optional

* Type: `object[]` ([Details](image-classification-properties-level2_predictions-items.md))

* cannot be null

* defined in: [Image Classification](image-classification-properties-level2_predictions.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/properties/level2_predictions")

### level2\_predictions Type

`object[]` ([Details](image-classification-properties-level2_predictions-items.md))

## level3\_predictions

List of top-k predictions for level 3 for this image CI, (we will use k=3).

`level3_predictions`

* is required

* Type: `object[]` ([Details](image-classification-properties-level3_predictions-items.md))

* cannot be null

* defined in: [Image Classification](image-classification-properties-level3_predictions.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/properties/level3_predictions")

### level3\_predictions Type

`object[]` ([Details](image-classification-properties-level3_predictions-items.md))

# Image Classification Definitions

## Definitions group prediction

Reference this group by using

```json
{"$ref":"https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction"}
```

| Property                     | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :--------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [level](#level)              | `integer` | Required | cannot be null | [Image Classification](image-classification-defs-prediction-properties-level.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/level")             |
| [class](#class)              | `string`  | Required | cannot be null | [Image Classification](image-classification-defs-prediction-properties-class.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/class")             |
| [confidence](#confidence)    | `number`  | Optional | cannot be null | [Image Classification](image-classification-defs-prediction-properties-confidence.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/confidence")   |
| [pred\_number](#pred_number) | `integer` | Optional | cannot be null | [Image Classification](image-classification-defs-prediction-properties-pred_number.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/pred_number") |
| [is\_inferred](#is_inferred) | `boolean` | Required | cannot be null | [Image Classification](image-classification-defs-prediction-properties-is_inferred.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/is_inferred") |

### level

Level in typology V2 to which this prediction corresponds to.

`level`

* is required

* Type: `integer`

* cannot be null

* defined in: [Image Classification](image-classification-defs-prediction-properties-level.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/level")

#### level Type

`integer`

#### level Constraints

**maximum**: the value of this number must smaller than or equal to: `3`

**minimum**: the value of this number must greater than or equal to: `1`

### class

Class from the Typology V2 predicted or inferred for this image content-item.

`class`

* is required

* Type: `string`

* cannot be null

* defined in: [Image Classification](image-classification-defs-prediction-properties-class.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/class")

#### class Type

`string`

#### class Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                             | Explanation |
| :-------------------------------- | :---------- |
| `"image"`                         |             |
| `"not_image"`                     |             |
| `"photograph"`                    |             |
| `"not_photograph"`                |             |
| `"decorative"`                    |             |
| `"informative_or_illustrative"`   |             |
| `"advertising"`                   |             |
| `"entertainment"`                 |             |
| `"caricature_humoristic_drawing"` |             |
| `"comic_strip"`                   |             |
| `"illustrated_story"`             |             |
| `"game"`                          |             |
| `"graph"`                         |             |
| `"technical_drawing"`             |             |
| `"human_rep_fashion_visual"`      |             |
| `"human_rep_portrait"`            |             |
| `"human_rep_scene"`               |             |
| `"scenery_landscape"`             |             |
| `"map_geological"`                |             |
| `"map_geopolitical"`              |             |
| `"map_physical_or_roadmap"`       |             |
| `"map_plan"`                      |             |
| `"map_weather"`                   |             |
| `"weather_infographic"`           |             |
| `"non_figurative_visual_content"` |             |
| `"object"`                        |             |
| `"ornament_illustrated_title"`    |             |
| `"other"`                         |             |

### confidence

Confidence score of the prediction - if class was assigned through predictions.

`confidence`

* is optional

* Type: `number`

* cannot be null

* defined in: [Image Classification](image-classification-defs-prediction-properties-confidence.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/confidence")

#### confidence Type

`number`

#### confidence Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

### pred\_number

'Number' of the prediction in the top-3, ie. if it was the first, second or third most probable value. Not applicable if class is inferred from the typology hierarchy.

`pred_number`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Image Classification](image-classification-defs-prediction-properties-pred_number.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/pred_number")

#### pred\_number Type

`integer`

#### pred\_number Constraints

**maximum**: the value of this number must smaller than or equal to: `3`

**minimum**: the value of this number must greater than or equal to: `1`

### is\_inferred

True if the prediction is inferred from another level in typology (eg. 'entertainment' inferred at level 2 if level 3 is 'game'). False if the class was predicted by a model; this field cannot be true for level-3.

`is_inferred`

* is required

* Type: `boolean`

* cannot be null

* defined in: [Image Classification](image-classification-defs-prediction-properties-is_inferred.md "https://impresso.github.io/impresso-schemas/json/impresso-2/semantic-enrichment/image-classification/image-classification.v1.schema.json#/$defs/prediction/properties/is_inferred")

#### is\_inferred Type

`boolean`
