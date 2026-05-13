## Content Item Type

`object` ([Content Item](bbox_visualizer.md))

# Content Item Properties

| Property                                   | Type     | Required | Nullable       | Defined by                                                                                                                                                                              |
| :----------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [iiif\_img\_base\_uri](#iiif_img_base_uri) | `array`  | Optional | cannot be null | [Content Item](bbox_visualizer-properties-iiif_img_base_uri.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/iiif_img_base_uri") |
| [bboxes](#bboxes)                          | `object` | Optional | cannot be null | [Content Item](bbox_visualizer-properties-bboxes.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/bboxes")                       |

## iiif\_img\_base\_uri

The base URI of the IIIF image server. There can be multiple images as content items can span multiple pages.

`iiif_img_base_uri`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Content Item](bbox_visualizer-properties-iiif_img_base_uri.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/iiif_img_base_uri")

### iiif\_img\_base\_uri Type

`string[]`

### iiif\_img\_base\_uri Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## bboxes

Bounding boxes of the content items or pages in the IIIF image. The bounding box is defined as an array of four numbers: \[x, y, width, height]. Each page is associated with its corresponding bounding boxes.

`bboxes`

* is optional

* Type: `object` ([Details](bbox_visualizer-properties-bboxes.md))

* cannot be null

* defined in: [Content Item](bbox_visualizer-properties-bboxes.md "https://impresso.github.io/impresso-schemas/json/visualizer/bbox_visualizer.schema.json#/properties/bboxes")

### bboxes Type

`object` ([Details](bbox_visualizer-properties-bboxes.md))

### bboxes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
