## items Type

`object` ([Details](entities-properties-nes-items.md))

# items Properties

| Property                               | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                         |
| :------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)                          | `string`  | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-type.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/type")                         |
| [surface](#surface)                    | `string`  | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-surface.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/surface")                   |
| [name](#name)                          | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-name.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/name")                         |
| [lOffset](#loffset)                    | `integer` | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-loffset.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/lOffset")                   |
| [rOffset](#roffset)                    | `integer` | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-roffset.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/rOffset")                   |
| [firstname](#firstname)                | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-firstname.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/firstname")               |
| [surname](#surname)                    | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-surname.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/surname")                   |
| [title](#title)                        | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-title.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/title")                       |
| [function](#function)                  | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-function.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/function")                 |
| [demonym](#demonym)                    | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-demonym.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/demonym")                   |
| [nested](#nested)                      | `boolean` | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-nested.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/nested")                     |
| [wkd\_id](#wkd_id)                     | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-wkd_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkd_id")                     |
| [wkpedia\_pagename](#wkpedia_pagename) | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-wkpedia_pagename.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkpedia_pagename") |
| [confidence](#confidence)              | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-confidence.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/confidence")             |
| [id](#id)                              | `string`  | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/id")                             |

## type

NE type

`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-type.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                      | Explanation |
| :------------------------- | :---------- |
| `"building"`               |             |
| `"loc"`                    |             |
| `"loc.add"`                |             |
| `"loc.add.elec"`           |             |
| `"loc.add.phys"`           |             |
| `"loc.adm"`                |             |
| `"loc.adm.nat"`            |             |
| `"loc.adm.reg"`            |             |
| `"loc.adm.sup"`            |             |
| `"loc.adm.town"`           |             |
| `"loc.admin.sup"`          |             |
| `"loc.fac"`                |             |
| `"loc.oro"`                |             |
| `"loc.phys"`               |             |
| `"loc.phys.astro"`         |             |
| `"loc.phys.geo"`           |             |
| `"loc.phys.hydro"`         |             |
| `"loc.unk"`                |             |
| `"org"`                    |             |
| `"org.adm"`                |             |
| `"org.ent"`                |             |
| `"org.ent.pressagency"`    |             |
| `"per"`                    |             |
| `"per.author"`             |             |
| `"pers"`                   |             |
| `"pers.coll"`              |             |
| `"pers.ind"`               |             |
| `"pers.ind.articleauthor"` |             |
| `"prod"`                   |             |
| `"prod.doctr"`             |             |
| `"prod.media"`             |             |
| `"street"`                 |             |
| `"time"`                   |             |
| `"time.date.abs"`          |             |

## surface

The (string) surface of the named entity mention, as it appears in the text

`surface`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-surface.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/surface")

### surface Type

`string`

## name

In case of a person mention, the entity component of type name.

`name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-name.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/name")

### name Type

`string`

## lOffset

The left character offset of the named entity with respect to the content item, as in the rebuilt format.

`lOffset`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-loffset.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/lOffset")

### lOffset Type

`integer`

## rOffset

The right character offset of the named entity with respect to the content item, as in the rebuilt format.

`rOffset`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-roffset.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/rOffset")

### rOffset Type

`integer`

## firstname

In case of a person mention and if available, the first name.

`firstname`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-firstname.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/firstname")

### firstname Type

`string`

## surname

In case of a person mention and if available, the surname.

`surname`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-surname.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/surname")

### surname Type

`string`

## title

In case of a person mention, the entity component of type 'title'.

`title`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-title.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/title")

### title Type

`string`

## function

In case of a person mention, the entity component of type 'function'.

`function`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-function.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/function")

### function Type

`string`

## demonym

In case of a person mention, the entity component of type 'demonym'.

`demonym`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-demonym.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/demonym")

### demonym Type

`string`

## nested

In case of a nested mention, this property should be set to true. Can be ignored if not.

`nested`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-nested.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/nested")

### nested Type

`boolean`

## wkd\_id

If exists, wikidata QID

`wkd_id`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-wkd_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkd_id")

### wkd\_id Type

`string`

## wkpedia\_pagename

If exists, wikipedia page name or, if not possible, wikipedia URL, in the language the NE recognition is made (e.g. page name 'Etats-Unis' if EL performed against French wikipedia, and 'United\_States' is against English Wikipedia.

`wkpedia_pagename`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-wkpedia_pagename.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkpedia_pagename")

### wkpedia\_pagename Type

`string`

## confidence



`confidence`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-confidence.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/confidence")

### confidence Type

`string`

### confidence Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"low"`    |             |
| `"medium"` |             |
| `"high"`   |             |

## id

The id of the named entity mention composed of the following set of values concatenated with a colon (':') : content item id + loffset + roffset + type + sys\_id (e.g. 'LLE-1989-04-04-a-i0195:56:69:person:bert-xxxx-xxxx-fr'.

`id`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/id")

### id Type

`string`
