## Image Type

`object` ([Image](content-item-6.md))

# Image Properties

| Property                                              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                        |
| :---------------------------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [linked\_ci\_s](#linked_ci_s)                         | `string`  | Optional | cannot be null | [Image](content-item-6-properties-linked-content-item-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/linked_ci_s")              |
| [reading\_order\_i](#reading_order_i)                 | `integer` | Required | cannot be null | [Image](content-item-6-properties-reading-order.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/reading_order_i")                   |
| [page\_nb\_is](#page_nb_is)                           | `array`   | Required | cannot be null | [Image](content-item-6-properties-page-numbers.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/page_nb_is")                         |
| [front\_b](#front_b)                                  | `boolean` | Required | cannot be null | [Image](content-item-6-properties-appears-on-front-page.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/front_b")                   |
| [cc\_b](#cc_b)                                        | `boolean` | Required | cannot be null | [Image](content-item-6-properties-converted-coordinates-legacy.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/cc_b")               |
| [caption\_txt](#caption_txt)                          | `string`  | Optional | cannot be null | [Image](content-item-6-properties-image-caption.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/caption_txt")                       |
| [descriptive\_keywords\_ss](#descriptive_keywords_ss) | `array`   | Optional | cannot be null | [Image](content-item-6-properties-descriptive-keywords.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/descriptive_keywords_ss")    |
| [item\_type\_s](#item_type_s)                         | `string`  | Required | cannot be null | [Image](content-item-6-properties-item-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/item_type_s")                           |
| [coords\_is](#coords_is)                              | `array`   | Required | cannot be null | [Image](content-item-6-properties-image-coordinates.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/coords_is")                     |
| [iiif\_url\_s](#iiif_url_s)                           | `string`  | Required | cannot be null | [Image](content-item-6-properties-iiif-image-url.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/iiif_url_s")                       |
| [type\_l0\_tp](#type_l0_tp)                           | Merged    | Optional | cannot be null | [Image](content-item-6-properties-visual-content.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/type_l0_tp")                       |
| [type\_l1\_tp](#type_l1_tp)                           | Merged    | Optional | cannot be null | [Image](content-item-6-properties-technique.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/type_l1_tp")                            |
| [type\_l2\_tp](#type_l2_tp)                           | Merged    | Optional | cannot be null | [Image](content-item-6-properties-communication-goal.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/type_l2_tp")                   |
| [type\_l3\_tp](#type_l3_tp)                           | Merged    | Optional | cannot be null | [Image](content-item-6-properties-visual-content-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/type_l3_tp")                  |
| [dinov2\_emb\_v1024](#dinov2_emb_v1024)               | `array`   | Required | cannot be null | [Image](content-item-6-properties-dinov2-image-embedding-1024d.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/dinov2_emb_v1024")   |
| [openclip\_emb\_v768](#openclip_emb_v768)             | `array`   | Required | cannot be null | [Image](content-item-6-properties-openclip-image-embedding-768d.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/openclip_emb_v768") |

## linked\_ci\_s

Identifier of the related content item (CI), as identified by the OLR process.

`linked_ci_s`

* is optional

* Type: `string` ([Linked Content Item ID](content-item-6-properties-linked-content-item-id.md))

* cannot be null

* defined in: [Image](content-item-6-properties-linked-content-item-id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/linked_ci_s")

### linked\_ci\_s Type

`string` ([Linked Content Item ID](content-item-6-properties-linked-content-item-id.md))

## reading\_order\_i

Reading order position of the content item within the issue.

`reading_order_i`

* is required

* Type: `integer` ([Reading order](content-item-6-properties-reading-order.md))

* cannot be null

* defined in: [Image](content-item-6-properties-reading-order.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/reading_order_i")

### reading\_order\_i Type

`integer` ([Reading order](content-item-6-properties-reading-order.md))

### reading\_order\_i Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## page\_nb\_is

Page numbers on which the content item appears.

`page_nb_is`

* is required

* Type: `integer[]`

* cannot be null

* defined in: [Image](content-item-6-properties-page-numbers.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/page_nb_is")

### page\_nb\_is Type

`integer[]`

### page\_nb\_is Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## front\_b

Indicates whether the content item appears on the front page of the issue.

`front_b`

* is required

* Type: `boolean` ([Appears on front page](content-item-6-properties-appears-on-front-page.md))

* cannot be null

* defined in: [Image](content-item-6-properties-appears-on-front-page.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/front_b")

### front\_b Type

`boolean` ([Appears on front page](content-item-6-properties-appears-on-front-page.md))

## cc\_b

Whether the content item has reliable coordinate information

`cc_b`

* is required

* Type: `boolean` ([Converted Coordinates (legacy)](content-item-6-properties-converted-coordinates-legacy.md))

* cannot be null

* defined in: [Image](content-item-6-properties-converted-coordinates-legacy.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/cc_b")

### cc\_b Type

`boolean` ([Converted Coordinates (legacy)](content-item-6-properties-converted-coordinates-legacy.md))

## caption\_txt

Original caption associated with the image.

`caption_txt`

* is optional

* Type: `string` ([Image caption](content-item-6-properties-image-caption.md))

* cannot be null

* defined in: [Image](content-item-6-properties-image-caption.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/caption_txt")

### caption\_txt Type

`string` ([Image caption](content-item-6-properties-image-caption.md))

### caption\_txt Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## descriptive\_keywords\_ss

Automatically generated descriptive keywords associated with the image.

`descriptive_keywords_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Image](content-item-6-properties-descriptive-keywords.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/descriptive_keywords_ss")

### descriptive\_keywords\_ss Type

`string[]`

### descriptive\_keywords\_ss Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## item\_type\_s

Type of content item.

`item_type_s`

* is required

* Type: `string` ([Item type](content-item-6-properties-item-type.md))

* cannot be null

* defined in: [Image](content-item-6-properties-item-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/item_type_s")

### item\_type\_s Type

`string` ([Item type](content-item-6-properties-item-type.md))

### item\_type\_s Constraints

**constant**: the value of this property must be equal to:

```json
"img"
```

## coords\_is

Bounding box of the image on the page, expressed as \[x, y, width, height] in pixel coordinates.

`coords_is`

* is required

* Type: `array` ([Image coordinates](content-item-6-properties-image-coordinates.md))

* cannot be null

* defined in: [Image](content-item-6-properties-image-coordinates.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/coords_is")

### coords\_is Type

`array` ([Image coordinates](content-item-6-properties-image-coordinates.md))

### coords\_is Constraints

**maximum number of items**: the maximum number of items for this array is: `4`

**minimum number of items**: the minimum number of items for this array is: `4`

## iiif\_url\_s

IIIF Image API URL for the image.

`iiif_url_s`

* is required

* Type: `string` ([IIIF image URL](content-item-6-properties-iiif-image-url.md))

* cannot be null

* defined in: [Image](content-item-6-properties-iiif-image-url.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/iiif_url_s")

### iiif\_url\_s Type

`string` ([IIIF image URL](content-item-6-properties-iiif-image-url.md))

### iiif\_url\_s Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## type\_l0\_tp

Whether the content is an image or not.

`type_l0_tp`

* is optional

* Type: `string` ([Visual content](content-item-6-properties-visual-content.md))

* cannot be null

* defined in: [Image](content-item-6-properties-visual-content.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/type_l0_tp")

### type\_l0\_tp Type

`string` ([Visual content](content-item-6-properties-visual-content.md))

one (and only one) of

* [Image](content-item-6-properties-visual-content-oneof-image.md "check type definition")

* [Not an image](content-item-6-properties-visual-content-oneof-not-an-image.md "check type definition")

## type\_l1\_tp

Determines if the image is a photograph.

`type_l1_tp`

* is optional

* Type: `string` ([Technique](content-item-6-properties-technique.md))

* cannot be null

* defined in: [Image](content-item-6-properties-technique.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/type_l1_tp")

### type\_l1\_tp Type

`string` ([Technique](content-item-6-properties-technique.md))

one (and only one) of

* [Photograph](content-item-6-properties-technique-oneof-photograph.md "check type definition")

* [Not a photograph](content-item-6-properties-technique-oneof-not-a-photograph.md "check type definition")

## type\_l2\_tp

Purpose or communicative function of the image.

`type_l2_tp`

* is optional

* Type: `string` ([Communication goal](content-item-6-properties-communication-goal.md))

* cannot be null

* defined in: [Image](content-item-6-properties-communication-goal.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/type_l2_tp")

### type\_l2\_tp Type

`string` ([Communication goal](content-item-6-properties-communication-goal.md))

one (and only one) of

* [Decorative](content-item-6-properties-communication-goal-oneof-decorative.md "check type definition")

* [Informative or illustrative](content-item-6-properties-communication-goal-oneof-informative-or-illustrative.md "check type definition")

* [Advertising](content-item-6-properties-communication-goal-oneof-advertising.md "check type definition")

* [Entertainment](content-item-6-properties-communication-goal-oneof-entertainment.md "check type definition")

## type\_l3\_tp

Classification of the visual content.

`type_l3_tp`

* is optional

* Type: `string` ([Visual content type](content-item-6-properties-visual-content-type.md))

* cannot be null

* defined in: [Image](content-item-6-properties-visual-content-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/type_l3_tp")

### type\_l3\_tp Type

`string` ([Visual content type](content-item-6-properties-visual-content-type.md))

one (and only one) of

* [Caricature or humoristic drawing](content-item-6-properties-visual-content-type-oneof-caricature-or-humoristic-drawing.md "check type definition")

* [Comic strip](content-item-6-properties-visual-content-type-oneof-comic-strip.md "check type definition")

* [Illustrated story](content-item-6-properties-visual-content-type-oneof-illustrated-story.md "check type definition")

* [Game](content-item-6-properties-visual-content-type-oneof-game.md "check type definition")

* [Graph](content-item-6-properties-visual-content-type-oneof-graph.md "check type definition")

* [Technical drawing](content-item-6-properties-visual-content-type-oneof-technical-drawing.md "check type definition")

* [Human representation – fashion visual](content-item-6-properties-visual-content-type-oneof-human-representation--fashion-visual.md "check type definition")

* [Human representation – portrait](content-item-6-properties-visual-content-type-oneof-human-representation--portrait.md "check type definition")

* [Human representation – scene](content-item-6-properties-visual-content-type-oneof-human-representation--scene.md "check type definition")

* [Scenery or landscape](content-item-6-properties-visual-content-type-oneof-scenery-or-landscape.md "check type definition")

* [Map – geological](content-item-6-properties-visual-content-type-oneof-map--geological.md "check type definition")

* [Map – geopolitical](content-item-6-properties-visual-content-type-oneof-map--geopolitical.md "check type definition")

* [Map – physical or roadmap](content-item-6-properties-visual-content-type-oneof-map--physical-or-roadmap.md "check type definition")

* [Map – plan](content-item-6-properties-visual-content-type-oneof-map--plan.md "check type definition")

* [Map – weather](content-item-6-properties-visual-content-type-oneof-map--weather.md "check type definition")

* [Weather infographic](content-item-6-properties-visual-content-type-oneof-weather-infographic.md "check type definition")

* [Non-figurative visual content](content-item-6-properties-visual-content-type-oneof-non-figurative-visual-content.md "check type definition")

* [Object](content-item-6-properties-visual-content-type-oneof-object.md "check type definition")

* [Ornament or illustrated title](content-item-6-properties-visual-content-type-oneof-ornament-or-illustrated-title.md "check type definition")

* [Other](content-item-6-properties-visual-content-type-oneof-other.md "check type definition")

## dinov2\_emb\_v1024

Dense vector representation of the image computed using the DINOv2 model. The vector has a fixed dimensionality of 1024.

`dinov2_emb_v1024`

* is required

* Type: `number[]`

* cannot be null

* defined in: [Image](content-item-6-properties-dinov2-image-embedding-1024d.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/dinov2_emb_v1024")

### dinov2\_emb\_v1024 Type

`number[]`

### dinov2\_emb\_v1024 Constraints

**maximum number of items**: the maximum number of items for this array is: `1024`

**minimum number of items**: the minimum number of items for this array is: `1024`

## openclip\_emb\_v768

Dense vector representation of the image computed using the OpenCLIP model. The vector has a fixed dimensionality of 768.

`openclip_emb_v768`

* is required

* Type: `number[]`

* cannot be null

* defined in: [Image](content-item-6-properties-openclip-image-embedding-768d.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.image.v1.schema.json#/properties/openclip_emb_v768")

### openclip\_emb\_v768 Type

`number[]`

### openclip\_emb\_v768 Constraints

**maximum number of items**: the maximum number of items for this array is: `768`

**minimum number of items**: the minimum number of items for this array is: `768`
