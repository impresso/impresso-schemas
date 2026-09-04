## 1 Type

`object` ([Model identifier property](lingproc-allof-model-identifier-property.md))

# 1 Properties

| Property               | Type     | Required | Nullable       | Defined by                                                                                                                                                                     |
| :--------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [model\_id](#model_id) | `string` | Optional | cannot be null | [Model identifier property](model-id-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/model-id.v1.schema.json#/properties/model_id") |

## model\_id

Identifier of the model or processing system that produced this output. It should include distinguishing information such as the model name, version, language, and relevant configuration, enabling transparency and traceability across processing runs. (Background: <https://docs.google.com/presentation/d/1wH4LygLcT28rvMA82k5fyEyzdX49inGkqCLnBNZsFaw/edit#slide=id.g30cf04393c4_1_46>)

`model_id`

* is optional

* Type: `string`

* cannot be null

* defined in: [Model identifier property](model-id-properties-model_id.md "https://impresso.github.io/impresso-schemas/json/impresso-2/common/model-id.v1.schema.json#/properties/model_id")

### model\_id Type

`string`

### model\_id Examples

```json
"spacy@3.6.1:de_core_news_md@3.6.0:sentencizer|tok2vec|tagger|morphologizer|lemmatizer|attribute_ruler|ner"
```
