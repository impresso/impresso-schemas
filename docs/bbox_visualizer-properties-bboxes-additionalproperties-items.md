## items Type

`object` ([Details](bbox_visualizer-properties-bboxes-additionalproperties-items.md))

# items Properties

| Property  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                          |
| :-------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [t](#t)   | `string` | Required | can be null    | [Content Item](bbox_visualizer-properties-bboxes-additionalproperties-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/bboxes/additionalProperties/items/properties/t")   |
| [ci](#ci) | `string` | Required | can be null    | [Content Item](bbox_visualizer-properties-bboxes-additionalproperties-items-properties-ci.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/bboxes/additionalProperties/items/properties/ci") |
| [c](#c)   | `array`  | Required | cannot be null | [Content Item](bbox_visualizer-properties-bboxes-additionalproperties-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/bboxes/additionalProperties/items/properties/c")   |

## t

The type of the bounding box (article, image, etc.).

`t`

* is required

* Type: `string`

* can be null

* defined in: [Content Item](bbox_visualizer-properties-bboxes-additionalproperties-items-properties-t.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/bboxes/additionalProperties/items/properties/t")

### t Type

`string`

## ci

The content item ID that the bounding box belongs to.

`ci`

* is required

* Type: `string`

* can be null

* defined in: [Content Item](bbox_visualizer-properties-bboxes-additionalproperties-items-properties-ci.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/bboxes/additionalProperties/items/properties/ci")

### ci Type

`string`

## c

The coordinates of the bounding box in the IIIF image. The bounding box is defined as an array of four numbers: \[x, y, width, height].

`c`

* is required

* Type: `number[]`

* cannot be null

* defined in: [Content Item](bbox_visualizer-properties-bboxes-additionalproperties-items-properties-c.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/bboxes/additionalProperties/items/properties/c")

### c Type

`number[]`

### c Constraints

**maximum number of items**: the maximum number of items for this array is: `4`

**minimum number of items**: the minimum number of items for this array is: `4`
