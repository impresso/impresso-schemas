## Provider Contextual Metadata Fields Type

`object` ([Provider Contextual Metadata Fields](content-item-5.md))

# Provider Contextual Metadata Fields Properties

| Property                                                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                   |
| :------------------------------------------------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [meta\_prv\_production\_type\_s](#meta_prv_production_type_s)             | `string`  | Optional | cannot be null | [Provider Contextual Metadata Fields](content-item-5-properties-production-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_production_type_s")            |
| [meta\_prv\_recording\_place\_s](#meta_prv_recording_place_s)             | `string`  | Optional | cannot be null | [Provider Contextual Metadata Fields](content-item-5-properties-recording-place.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_recording_place_s")            |
| [meta\_prv\_live\_b](#meta_prv_live_b)                                    | `boolean` | Optional | cannot be null | [Provider Contextual Metadata Fields](content-item-5-properties-live-broadcast.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_live_b")                        |
| [meta\_prv\_geo\_descriptors\_ss](#meta_prv_geo_descriptors_ss)           | `array`   | Optional | cannot be null | [Provider Contextual Metadata Fields](content-item-5-properties-geographical-descriptors.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_geo_descriptors_ss")  |
| [meta\_prv\_thematic\_descriptors\_ss](#meta_prv_thematic_descriptors_ss) | `array`   | Optional | cannot be null | [Provider Contextual Metadata Fields](content-item-5-properties-thematic-descriptors.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_thematic_descriptors_ss") |
| [meta\_prv\_participants\_ss](#meta_prv_participants_ss)                  | `array`   | Optional | cannot be null | [Provider Contextual Metadata Fields](content-item-5-properties-participants.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_participants_ss")                 |
| Additional Properties                                                     | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                              |

## meta\_prv\_production\_type\_s

Production type of the broadcast (e.g. 'Production propre'). Sourced from 'production\_type' key in additional\_metadata. Provider: RTS.

`meta_prv_production_type_s`

* is optional

* Type: `string` ([Production Type](content-item-5-properties-production-type.md))

* cannot be null

* defined in: [Provider Contextual Metadata Fields](content-item-5-properties-production-type.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_production_type_s")

### meta\_prv\_production\_type\_s Type

`string` ([Production Type](content-item-5-properties-production-type.md))

## meta\_prv\_recording\_place\_s

Place where the broadcast was recorded. Sourced from 'recording\_place' key in additional\_metadata. Provider: RTS.

`meta_prv_recording_place_s`

* is optional

* Type: `string` ([Recording Place](content-item-5-properties-recording-place.md))

* cannot be null

* defined in: [Provider Contextual Metadata Fields](content-item-5-properties-recording-place.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_recording_place_s")

### meta\_prv\_recording\_place\_s Type

`string` ([Recording Place](content-item-5-properties-recording-place.md))

## meta\_prv\_live\_b

Whether the broadcast was live. Derived from 'live' key in additional\_metadata. Provider: RTS.

`meta_prv_live_b`

* is optional

* Type: `boolean` ([Live Broadcast](content-item-5-properties-live-broadcast.md))

* cannot be null

* defined in: [Provider Contextual Metadata Fields](content-item-5-properties-live-broadcast.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_live_b")

### meta\_prv\_live\_b Type

`boolean` ([Live Broadcast](content-item-5-properties-live-broadcast.md))

## meta\_prv\_geo\_descriptors\_ss

Geographical descriptors associated with the broadcast content (e.g. countries, cities). Sourced from 'geographical\_descriptors' key in additional\_metadata. Provider: RTS.

`meta_prv_geo_descriptors_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Provider Contextual Metadata Fields](content-item-5-properties-geographical-descriptors.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_geo_descriptors_ss")

### meta\_prv\_geo\_descriptors\_ss Type

`string[]`

## meta\_prv\_thematic\_descriptors\_ss

Thematic descriptors categorising the broadcast content (e.g. topics, themes). Sourced from 'thematical\_descriptors' key in additional\_metadata. Provider: RTS.

`meta_prv_thematic_descriptors_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Provider Contextual Metadata Fields](content-item-5-properties-thematic-descriptors.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_thematic_descriptors_ss")

### meta\_prv\_thematic\_descriptors\_ss Type

`string[]`

## meta\_prv\_participants\_ss

Participants in the broadcast, including role and affiliation where available. Sourced from 'participants' key in additional\_metadata. Provider: RTS.

`meta_prv_participants_ss`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Provider Contextual Metadata Fields](content-item-5-properties-participants.md "https://impresso.github.io/impresso-schemas/json/impresso-2/solr-indexing/content-item/content-item.part.contextual-metadata.provider.v1.schema.json#/properties/meta_prv_participants_ss")

### meta\_prv\_participants\_ss Type

`string[]`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
