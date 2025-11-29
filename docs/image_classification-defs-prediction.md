## prediction Type

`object` ([Details](image_classification-defs-prediction.md))

all of

* [Untitled undefined type in ](image_classification-defs-prediction-allof-0.md "check type definition")

* [Untitled undefined type in ](image_classification-defs-prediction-allof-1.md "check type definition")

* [Untitled undefined type in ](image_classification-defs-prediction-allof-2.md "check type definition")

# prediction Properties

| Property                     | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                          |
| :--------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [level](#level)              | `integer` | Required | cannot be null | [Untitled schema](image_classification-defs-prediction-properties-level.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/level")             |
| [class](#class)              | `string`  | Required | cannot be null | [Untitled schema](image_classification-defs-prediction-properties-class.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/class")             |
| [confidence](#confidence)    | `number`  | Optional | cannot be null | [Untitled schema](image_classification-defs-prediction-properties-confidence.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/confidence")   |
| [pred\_number](#pred_number) | `integer` | Optional | cannot be null | [Untitled schema](image_classification-defs-prediction-properties-pred_number.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/pred_number") |
| [is\_inferred](#is_inferred) | `boolean` | Required | cannot be null | [Untitled schema](image_classification-defs-prediction-properties-is_inferred.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/is_inferred") |

## level

Level in typology V2 to which this prediction corresponds to.

`level`

* is required

* Type: `integer`

* cannot be null

* defined in: [Untitled schema](image_classification-defs-prediction-properties-level.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/level")

### level Type

`integer`

### level Constraints

**maximum**: the value of this number must smaller than or equal to: `3`

**minimum**: the value of this number must greater than or equal to: `1`

## class

Class from the Typology V2 predicted or inferred for this image content-item.

`class`

* is required

* Type: `string`

* cannot be null

* defined in: [Untitled schema](image_classification-defs-prediction-properties-class.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/class")

### class Type

`string`

### class Constraints

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

## confidence

Confidence score of the prediction - if class was assigned through predictions.

`confidence`

* is optional

* Type: `number`

* cannot be null

* defined in: [Untitled schema](image_classification-defs-prediction-properties-confidence.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/confidence")

### confidence Type

`number`

### confidence Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

## pred\_number

'Number' of the prediction in the top-3, ie. if it was the first, second or third most probable value. Not applicable if class is inferred from the typology hierarchy.

`pred_number`

* is optional

* Type: `integer`

* cannot be null

* defined in: [Untitled schema](image_classification-defs-prediction-properties-pred_number.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/pred_number")

### pred\_number Type

`integer`

### pred\_number Constraints

**maximum**: the value of this number must smaller than or equal to: `3`

**minimum**: the value of this number must greater than or equal to: `1`

## is\_inferred

True if the prediction is inferred from another level in typology (eg. 'entertainment' inferred at level 2 if level 3 is 'game'). False if the class was predicted by a model; this field cannot be true for level-3.

`is_inferred`

* is required

* Type: `boolean`

* cannot be null

* defined in: [Untitled schema](image_classification-defs-prediction-properties-is_inferred.md "https://impresso.github.io/impresso-schemas/json/image_classification/image_classification.schema.json#/$defs/prediction/properties/is_inferred")

### is\_inferred Type

`boolean`
