## Content Item – Paper Support (Schema Fragment) Type

`object` ([Content Item – Paper Support (Schema Fragment)](content-item-8.md))

# Content Item – Paper Support (Schema Fragment) Properties

| Property                              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                        |
| :------------------------------------ | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [page\_nb\_is](#page_nb_is)           | `array`   | Required | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-page-numbers.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/page_nb_is")           |
| [page\_id\_ss](#page_id_ss)           | `array`   | Required | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-page-identifiers.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/page_id_ss")       |
| [nb\_pages\_i](#nb_pages_i)           | `integer` | Required | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-number-of-pages.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/nb_pages_i")        |
| [front\_b](#front_b)                  | `boolean` | Optional | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-appears-on-front-page.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/front_b")     |
| [cc\_b](#cc_b)                        | `boolean` | Required | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-converted-coordinates-legacy.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/cc_b") |
| [reading\_order\_i](#reading_order_i) | `integer` | Required | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-reading-order.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/reading_order_i")     |
| [olr\_b](#olr_b)                      | `boolean` | Optional | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-olr_b.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/olr_b")                       |
| [rc\_plains](#rc_plains)              | `array`   | Required | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-rc_plains.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/rc_plains")               |
| [lb\_plain](#lb_plain)                | `string`  | Required | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-lb_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/lb_plain")                 |
| [pb\_plain](#pb_plain)                | `string`  | Required | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-pb_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/pb_plain")                 |
| [rb\_plain](#rb_plain)                | `string`  | Required | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-rb_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/rb_plain")                 |
| [pp\_plain](#pp_plain)                | `string`  | Optional | cannot be null | [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-pp_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/pp_plain")                 |
| Additional Properties                 | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                   |

## page\_nb\_is

Page numbers on which the content item appears.

`page_nb_is`

* is required

* Type: `integer[]`

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-page-numbers.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/page_nb_is")

### page\_nb\_is Type

`integer[]`

### page\_nb\_is Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## page\_id\_ss

Identifiers of the pages on which the content item appears.

`page_id_ss`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-page-identifiers.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/page_id_ss")

### page\_id\_ss Type

`string[]`

### page\_id\_ss Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## nb\_pages\_i

Total number of distinct pages the content item spans.

`nb_pages_i`

* is required

* Type: `integer` ([Number of pages](content-item-8-properties-number-of-pages.md))

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-number-of-pages.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/nb_pages_i")

### nb\_pages\_i Type

`integer` ([Number of pages](content-item-8-properties-number-of-pages.md))

### nb\_pages\_i Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## front\_b

Indicates whether the content item appears on the front page of the issue.

`front_b`

* is optional

* Type: `boolean` ([Appears on front page](content-item-8-properties-appears-on-front-page.md))

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-appears-on-front-page.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/front_b")

### front\_b Type

`boolean` ([Appears on front page](content-item-8-properties-appears-on-front-page.md))

## cc\_b

Whether the content item has reliable coordinate information

`cc_b`

* is required

* Type: `boolean` ([Converted Coordinates (legacy)](content-item-8-properties-converted-coordinates-legacy.md))

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-converted-coordinates-legacy.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/cc_b")

### cc\_b Type

`boolean` ([Converted Coordinates (legacy)](content-item-8-properties-converted-coordinates-legacy.md))

## reading\_order\_i

Reading order position of the content item within the issue.

`reading_order_i`

* is required

* Type: `integer` ([Reading order](content-item-8-properties-reading-order.md))

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-reading-order.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/reading_order_i")

### reading\_order\_i Type

`integer` ([Reading order](content-item-8-properties-reading-order.md))

### reading\_order\_i Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## olr\_b

Whether the page where the CI originates has been processed with OLR or not.

`olr_b`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-olr_b.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/olr_b")

### olr\_b Type

`boolean`

## rc\_plains

Region coordinates (rc) in plain text format with page and coordinate information

`rc_plains`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-rc_plains.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/rc_plains")

### rc\_plains Type

`string[]`

## lb\_plain

Line boundaries (lb) in plain text format

`lb_plain`

* is required

* Type: `string`

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-lb_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/lb_plain")

### lb\_plain Type

`string`

## pb\_plain

Paragraph boundaries (pb) in plain text format

`pb_plain`

* is required

* Type: `string`

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-pb_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/pb_plain")

### pb\_plain Type

`string`

## rb\_plain

Region boundaries (rb) in plain text format

`rb_plain`

* is required

* Type: `string`

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-rb_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/rb_plain")

### rb\_plain Type

`string`

## pp\_plain

Rebuilt page information.

`pp_plain`

* is optional

* Type: `string`

* cannot be null

* defined in: [Content Item – Paper Support (Schema Fragment)](content-item-8-properties-pp_plain.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.text.paper.v1.schema.json#/properties/pp_plain")

### pp\_plain Type

`string`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
