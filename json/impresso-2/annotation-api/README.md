# Annotation API schemas

Request and response bodies of the public annotation API at
`https://impresso-annotation.epfl.ch`, served by impresso-serve. The schemas
describe impresso-serve's response models. The server sends every key a
response schema declares, with `null` when there is no value, so all of them
are required. Parity with the previous TorchServe and Django backend is
checked by impresso-serve's `test-parity` job, not here. The client is the
Impresso middle layer (IML), which generates its types from these schemas.

This is not `../public-api/`, which describes the IML's own public API.

## Endpoints

All endpoints are `POST /api/<name>/`, with the trailing slash.

| Endpoint | Request | Response |
| -------- | ------- | -------- |
| `text-embedder` | [`text-embedder-request.v1`](embeddings/text-embedder-request.v1.schema.json) | [`text-embedder-response.v1`](embeddings/text-embedder-response.v1.schema.json) |
| `ner` | [`ner-request.v1`](entities/ner-request.v1.schema.json) | [`ner-response.v1`](entities/ner-response.v1.schema.json) |
| `nel` | [`nel-request.v1`](entities/nel-request.v1.schema.json) | [`nel-response.v1`](entities/nel-response.v1.schema.json) |
| `ner-nel` | [`ner-request.v1`](entities/ner-request.v1.schema.json) | [`ner-nel-response.v1`](entities/ner-nel-response.v1.schema.json) |
| `dinov2` | [`image-embedding-request.v1`](embeddings/image-embedding-request.v1.schema.json) | [`image-embedding-response.v1`](embeddings/image-embedding-response.v1.schema.json) |
| `openclip-image` | [`image-embedding-request.v1`](embeddings/image-embedding-request.v1.schema.json) | [`image-embedding-response.v1`](embeddings/image-embedding-response.v1.schema.json) |
| `openclip-text` | [`openclip-text-request.v1`](embeddings/openclip-text-request.v1.schema.json) | [`openclip-text-response.v1`](embeddings/openclip-text-response.v1.schema.json) |
| `image-classification` | [`image-classification-request.v1`](image-classification/image-classification-request.v1.schema.json) | [`image-classification-response.v1`](image-classification/image-classification-response.v1.schema.json) |

The NER and NEL entities are defined once, in
[`ner-entity.v1`](entities/ner-entity.v1.schema.json) and
[`nel-entity.v1`](entities/nel-entity.v1.schema.json).

## Image input

The image endpoints accept three forms. The request schemas describe only the
JSON form.

- JSON: `dinov2` and `openclip-image` take one of `bytes_b64`, `bytes`
  (base64), `path` or `url`, plus an optional `id`. `image-classification`
  takes `bytes_b64` or `bytes` only, plus an optional `ci_id` or `id`.
- Multipart: the image in a `file` field.
- Raw: the image bytes as the request body.

The response `ci_id` is the client's id. Otherwise it is `auto-0` for raw,
multipart and base64 `bytes` input, and `null` for `bytes_b64`, `path` and
`url` input on the embedding endpoints. On `image-classification` it is always
a string (`auto-0` when no id is given). It is not an Impresso content-item id.

## NEL response shapes

`nes` in the `nel` response is:

- a list, when the request has `entities` or no `[START] … [END]` marker;
- a single entity, in the marker form (`type` is `""` and `confidence_ner` is
  `null`);
- an empty object `{}`, in the marker form when the marker is malformed or
  nothing is linked.

`ner` and `ner-nel` always return a list, `[]` when nothing is found.

## Status codes

Clients should treat any status other than 200 as a failure. Error bodies are
not part of the contract and have no schema.

| Status | Body | When |
| ------ | ---- | ---- |
| 200 | The response schema | Success |
| 400 | `{"error": str}` | Image endpoints: no image, invalid base64, or an undecodable image |
| 422 | `{"detail": [...]}` | The JSON body fails request validation |
| 503 | `{"detail": str}` | The model is not deployed on this instance |
| 500 | Plain text | Unhandled server error |
| 502, 504 | HTML (nginx) | Backend unreachable or timed out |

## v2 embeddings

Version 2 has one route per input type, with the model as a request field.
The v1 routes above are unchanged. Both v2 routes are `POST`, with the
trailing slash.

| Endpoint | Models | Request | Response |
| -------- | ------ | ------- | -------- |
| `/api/v2/embeddings/text/` | `gte`, `openclip`, `siglip2` | [`text-embedding-request.v1`](v2/embeddings/text-embedding-request.v1.schema.json) | [`text-embedding-response.v1`](v2/embeddings/text-embedding-response.v1.schema.json) |
| `/api/v2/embeddings/image/` | `dinov2`, `openclip`, `siglip2` | [`image-embedding-request.v1`](v2/embeddings/image-embedding-request.v1.schema.json) | [`image-embedding-response.v1`](v2/embeddings/image-embedding-response.v1.schema.json) |

- `model` is required. The `openclip` and `siglip2` text and image embeddings
  share one space, so a text vector can be compared with an image vector of
  the same model.
- `normalize` (default `true`) returns the L2-normalised vector. `false`
  returns the raw model output.
- `dimensions` (`gte` only, 1 to 768) keeps the leading values of the vector.
  The cut comes first, so with `normalize` the cut vector is re-normalised.
  `dimensions` with another model is rejected with 422.
- Values are rounded to 5 decimals.
- `model_id` is the model's slug. The image slugs are the `model_id` of the
  batch image-embeddings records: `emb-images_dinov2-v0.0.1`,
  `emb-images_openclip-v0.0.1`, `emb-siglip2-v0.0.1`. The text slugs are
  `emb-docs_gte-v0.0.1`, `emb-texts_openclip-v0.0.1` and
  `emb-texts_siglip2-v0.0.1`. A new slug is issued whenever a model revision
  changes.
- The image route takes the image as JSON `bytes_b64`, or as a multipart
  `file` field with `model`, `normalize` and `id` as form fields. It does not
  take the raw request body, `path` or `url`. The response `id` is the request
  `id`, otherwise `auto-0`.
- Status codes: 422 when a field fails validation (an unknown or missing
  `model`, a misplaced `dimensions`, a JSON body without `bytes_b64`), in both
  the JSON and the multipart form; 400 for a multipart form without `file`, a
  raw body, invalid base64 or an image that cannot be decoded; 503 when the
  model is not deployed. The other codes are as in the table above.

## v2 entities

The v2 entity routes take the same requests and return the same envelope as
their v1 routes, including the NEL marker form. Only the entities differ:
they are the entities of the batch NER and NEL records
([`entities-ner.v1`](../semantic-enrichment/entities/entities-ner.v1.schema.json),
[`entities-nel.v1`](../semantic-enrichment/entities/entities-nel.v1.schema.json)),
with no v1 key.

| Endpoint | Request | Response |
| -------- | ------- | -------- |
| `/api/v2/entities/ner/` | [`ner-request.v1`](v2/entities/ner-request.v1.schema.json) | [`ner-response.v1`](v2/entities/ner-response.v1.schema.json) |
| `/api/v2/entities/nel/` | [`nel-request.v1`](v2/entities/nel-request.v1.schema.json) | [`nel-response.v1`](v2/entities/nel-response.v1.schema.json) |
| `/api/v2/entities/ner-nel/` | [`ner-request.v1`](v2/entities/ner-request.v1.schema.json) | [`ner-nel-response.v1`](v2/entities/ner-nel-response.v1.schema.json) |

- NER entities: `type`, `surface`, `lOffset`, `rOffset`, `confidence_ner`,
  `confidence_ner_entity`, `confidence_ner_type`.
- NEL entities add `confidence_nel`, `confidence_margin`, `wkdata_qid`,
  `wkpedia_lg`, `wkpedia_pagename`, `label_fr`, `label_en`, `label_de`,
  `label_other`, `label_other_lg`, `type_ner_original` and `nel_unlink`.
- `wkdata_qid`, `wkpedia_lg`, `wkpedia_pagename` and the three labels are
  always sent, null when empty. Every other key is left out when it has no
  value, as in the batch records. `nel_unlink` is present only when a
  validation rule removed a link, and `type_ner_original` only when linking
  changed `type`.
- Not in v2: `index`, `scope`, `wkd_pred`, `function`, `name`, `title`, and the
  v1 names `wkd_id`, `wkpedia_url`, `entity_confidence`, `type_confidence`,
  `confidence_nel_normalized`. The Wikipedia URL is
  `https://<wkpedia_lg>.wikipedia.org/wiki/<wkpedia_pagename>`.
- Two differences from the batch entity, for input the batch never sees: `type`
  is any string (`""` in the marker form; on `/nel/`, the type the client sent),
  and `confidence_ner` is optional (absent in the marker form, or when a `/nel/`
  request entity has none).

## v2 image classification

`POST /api/v2/image-classification/` is the same endpoint as
`/api/image-classification/`, under the v2 prefix: same input forms, same
response ([`image-classification-request.v1`](v2/image-classification/image-classification-request.v1.schema.json),
[`image-classification-response.v1`](v2/image-classification/image-classification-response.v1.schema.json)).
The v1 route never had a TorchServe version and already answers the batch
image-classification record, so the two routes give the same answer. With it,
every v1 route has a v2 counterpart.

## Conventions

The v1 routes return exactly the keys of the previous TorchServe backend, and
that set is frozen. New fields, such as the linking pipeline's `wkdata_qid`,
`wkpedia_lg` and Wikidata labels, are served by the v2 routes only. Within a
version the contract only grows by adding keys, so `additionalProperties` is
left open.

Two v1 values differ from the TorchServe backend while the keys stay the same.
`confidence_nel` and `confidence_nel_normalized` both carry the length-normalised
link score, where TorchServe sent the raw sequence likelihood in
`confidence_nel`. `function`, `name` and `title` are always null, because the
current NER model does not produce person components.

These wire names are frozen and are exceptions to the repository conventions
(snake_case, no empty-string sentinels): `"NER seconds"`, `"NEL seconds"`,
`lOffset`, `rOffset`, and the empty `type` (`""`).
