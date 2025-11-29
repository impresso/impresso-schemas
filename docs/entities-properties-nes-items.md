## items Type

`object` ([Details](entities-properties-nes-items.md))

# items Properties

| Property                               | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                         |
| :------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)                          | `string`  | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-type.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/type")                         |
| [surface](#surface)                    | `string`  | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-surface.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/surface")                   |
| [lOffset](#loffset)                    | `integer` | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-loffset.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/lOffset")                   |
| [rOffset](#roffset)                    | `integer` | Required | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-roffset.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/rOffset")                   |
| [confidence\_ner](#confidence_ner)     | `number`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-confidence_ner.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/confidence_ner")     |
| [confidence\_nel](#confidence_nel)     | `number`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-confidence_nel.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/confidence_nel")     |
| [wkd\_id](#wkd_id)                     | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-wkd_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkd_id")                     |
| [wkpedia\_pagename](#wkpedia_pagename) | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-wkpedia_pagename.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkpedia_pagename") |
| [wkpedia\_url](#wkpedia_url)           | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-wkpedia_url.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkpedia_url")           |
| [name](#name)                          | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-name.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/name")                         |
| [title](#title)                        | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-title.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/title")                       |
| [function](#function)                  | `string`  | Optional | cannot be null | [Named Entity JSON Schema](entities-properties-nes-items-properties-function.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/function")                 |

## type

NE type (coarse-grained and fine-grained).

`type`

* is required

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-type.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                               | Explanation |
| :---------------------------------- | :---------- |
| `"comp.demonym"`                    |             |
| `"comp.function"`                   |             |
| `"comp.name"`                       |             |
| `"comp.qualifier"`                  |             |
| `"comp.title"`                      |             |
| `"loc"`                             |             |
| `"loc.add.elec"`                    |             |
| `"loc.add.phys"`                    |             |
| `"loc.adm.nat"`                     |             |
| `"loc.adm.reg"`                     |             |
| `"loc.adm.sup"`                     |             |
| `"loc.adm.town"`                    |             |
| `"loc.fac"`                         |             |
| `"loc.oro"`                         |             |
| `"loc.phys.astro"`                  |             |
| `"loc.phys.geo"`                    |             |
| `"loc.phys.hydro"`                  |             |
| `"loc.unk"`                         |             |
| `"org"`                             |             |
| `"org.adm"`                         |             |
| `"org.ent"`                         |             |
| `"org.ent.pressagency"`             |             |
| `"pers"`                            |             |
| `"pers.coll"`                       |             |
| `"pers.ind"`                        |             |
| `"pers.ind.articleauthor"`          |             |
| `"prod"`                            |             |
| `"prod.doctr"`                      |             |
| `"prod.media"`                      |             |
| `"time"`                            |             |
| `"time.date.abs"`                   |             |
| `"time.hour.abs"`                   |             |
| `"org.ent.pressagency.Reuters"`     |             |
| `"org.ent.pressagency.Stefani"`     |             |
| `"org.ent.pressagency.Extel"`       |             |
| `"org.ent.pressagency.Havas"`       |             |
| `"org.ent.pressagency.Xinhua"`      |             |
| `"org.ent.pressagency.Domei"`       |             |
| `"org.ent.pressagency.Belga"`       |             |
| `"org.ent.pressagency.CTK"`         |             |
| `"org.ent.pressagency.ANSA"`        |             |
| `"org.ent.pressagency.DNB"`         |             |
| `"pers.ind.articleauthor"`          |             |
| `"org.ent.pressagency.Wolff"`       |             |
| `"org.ent.pressagency.unk"`         |             |
| `"org.ent.pressagency.UP-UPI"`      |             |
| `"org.ent.pressagency.ATS-SDA"`     |             |
| `"org.ent.pressagency.DPA"`         |             |
| `"org.ent.pressagency.AFP"`         |             |
| `"pers.ind.articleauthor"`          |             |
| `"org.ent.pressagency.Kipa"`        |             |
| `"org.ent.pressagency.ag"`          |             |
| `"org.ent.pressagency.Extel"`       |             |
| `"org.ent.pressagency.ATS-SDA"`     |             |
| `"org.ent.pressagency.Havas"`       |             |
| `"org.ent.pressagency.Reuters"`     |             |
| `"org.ent.pressagency.Xinhua"`      |             |
| `"org.ent.pressagency.AP"`          |             |
| `"org.ent.pressagency.APA"`         |             |
| `"org.ent.pressagency.ANSA"`        |             |
| `"org.ent.pressagency.DDP-DAPD"`    |             |
| `"org.ent.pressagency.TASS"`        |             |
| `"org.ent.pressagency.Europapress"` |             |
| `"org.ent.pressagency.SPK-SMP"`     |             |
| `"unk"`                             |             |

## surface

The surface form of the named entity mention, as it appears in the text.

`surface`

* is required

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-surface.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/surface")

### surface Type

`string`

## lOffset

The left character offset of the named entity with respect to the content item.

`lOffset`

* is required

* Type: `integer`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-loffset.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/lOffset")

### lOffset Type

`integer`

## rOffset

The right character offset of the named entity with respect to the content item.

`rOffset`

* is required

* Type: `integer`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-roffset.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/rOffset")

### rOffset Type

`integer`

## confidence\_ner

Confidence score of the Named Entity Recognition process.

`confidence_ner`

* is optional

* Type: `number`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-confidence_ner.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/confidence_ner")

### confidence\_ner Type

`number`

## confidence\_nel

Confidence score of the Named Entity Linking process.

`confidence_nel`

* is optional

* Type: `number`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-confidence_nel.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/confidence_nel")

### confidence\_nel Type

`number`

## wkd\_id

Wikidata QID if available.

`wkd_id`

* is optional

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-wkd_id.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkd_id")

### wkd\_id Type

`string`

## wkpedia\_pagename

Wikipedia page name, i.e. the last part of the wikipedia URL (e.g.  United\_States)

`wkpedia_pagename`

* is optional

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-wkpedia_pagename.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkpedia_pagename")

### wkpedia\_pagename Type

`string`

## wkpedia\_url

Wikipedia page URL, e.g. <https://en.wikipedia.org/wiki/United_States>

`wkpedia_url`

* is optional

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-wkpedia_url.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/wkpedia_url")

### wkpedia\_url Type

`string`

## name

In case of a person mention, the entity component of type 'name', as defined in the Impresso HIPE NE Annotation guidelines (<https://zenodo.org/records/3585750>).

`name`

* is optional

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-name.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/name")

### name Type

`string`

## title

In case of a person mention, the entity component of type 'title', as defined in the Impresso HIPE NE Annotation guidelines (<https://zenodo.org/records/3585750>).

`title`

* is optional

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-title.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/title")

### title Type

`string`

## function

In case of a person mention, the entity component of type 'function', as defined in the Impresso HIPE NE Annotation guidelines (<https://zenodo.org/records/3585750>).

`function`

* is optional

* Type: `string`

* cannot be null

* defined in: [Named Entity JSON Schema](entities-properties-nes-items-properties-function.md "https://impresso.github.io/impresso-schemas/json/entities.schema.json#/properties/nes/items/properties/function")

### function Type

`string`
