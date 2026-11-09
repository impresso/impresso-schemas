"""Check that invalid instances are rejected for the expected reason.

Each NEL case mutates the Q30 entity of a valid example; each annotation-api
case is a small inline response. Every case names the JSON Schema keyword that
must report the error.
"""

import json
import pathlib

import pytest
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).parent.parent
NEL_SCHEMA = "json/impresso-2/semantic-enrichment/entities/entities-nel.v1.schema.json"
NEL_EXAMPLE = "examples/impresso-2/semantic-enrichment/entities/entities-nel.example1.json"


def _drop_label_fr(entity):
    del entity["label_fr"]


def _label_other_without_lg(entity):
    entity.update(label_fr=None, label_en=None, label_de=None, label_other="États-Unis")


def _label_other_with_label_en(entity):
    entity.update(label_fr=None, label_de=None, label_other="アメリカ合衆国", label_other_lg="ja")


def _labels_without_qid(entity):
    entity["wkdata_qid"] = None


NEL_INVALID_CASES = [
    ("missing_label_fr", _drop_label_fr, "required"),
    ("label_other_without_lg", _label_other_without_lg, "dependentRequired"),
    ("label_other_with_label_en", _label_other_with_label_en, "type"),
    ("labels_without_qid", _labels_without_qid, "type"),
]


@pytest.mark.parametrize(
    "mutate,keyword",
    [(m, k) for _, m, k in NEL_INVALID_CASES],
    ids=[name for name, _, _ in NEL_INVALID_CASES],
)
@pytest.mark.imp2
def test_nel_invalid_entity_is_rejected(mutate, keyword, schema_registry) -> None:
    schema = json.loads((ROOT / NEL_SCHEMA).read_text(encoding="utf-8"))
    instance = json.loads((ROOT / NEL_EXAMPLE).read_text(encoding="utf-8"))
    entity = next(e for e in instance["nes"] if e["wkdata_qid"] == "Q30")
    mutate(entity)
    validator = Draft202012Validator(schema, registry=schema_registry)
    keywords = {e.validator for e in validator.iter_errors(instance)}
    assert keyword in keywords, f"expected {keyword!r}, got {keywords or 'no errors'}"


ANNOTATION_API = "json/impresso-2/annotation-api/"
LINKED = {"ts": "2026-10-15T10:00:00Z", "sys_id": "nel", "NEL seconds": 0.1, "NER seconds": 0.0}
WITHOUT_NER_SECONDS = {k: v for k, v in LINKED.items() if k != "NER seconds"}
IMAGE_EMBEDDING = {"ts": "2026-10-15T10:00:00Z", "embedding": [0.1], "size": 1024, "model_id": "dinov2", "seconds": 0.2}
TEXT_EMBEDDING = {"ts": "2026-10-15T10:00:00Z", "sys_id": "gte", "embedding": [0.1], "vector_dimensions": 768, "text": "x"}

ANNOTATION_API_INVALID_CASES = [
    ("ner_nel_nes_object", "entities/ner-nel-response.v1.schema.json", {**LINKED, "nes": {}}, "type"),
    ("nel_nes_string", "entities/nel-response.v1.schema.json", {**LINKED, "nes": "Berlin"}, "anyOf"),
    ("ner_seconds_missing", "entities/ner-response.v1.schema.json", {**WITHOUT_NER_SECONDS, "nes": []}, "required"),
    ("embedding_response_without_seconds", "embeddings/text-embedder-response.v1.schema.json", TEXT_EMBEDDING, "required"),
    ("image_embedding_without_ci_id", "embeddings/image-embedding-response.v1.schema.json", IMAGE_EMBEDDING, "required"),
    # v2: `dimensions` only with gte; a model of the other modality is not in the enum.
    ("v2_text_dimensions_with_openclip", "v2/embeddings/text-embedding-request.v1.schema.json", {"model": "openclip", "data": "x", "dimensions": 256}, "not"),
    ("v2_text_model_dinov2", "v2/embeddings/text-embedding-request.v1.schema.json", {"model": "dinov2", "data": "x"}, "enum"),
    ("v2_image_model_gte", "v2/embeddings/image-embedding-request.v1.schema.json", {"model": "gte", "bytes_b64": "AA=="}, "enum"),
    ("v2_image_without_model", "v2/embeddings/image-embedding-request.v1.schema.json", {"bytes_b64": "AA=="}, "required"),
    ("v2_image_response_without_normalized", "v2/embeddings/image-embedding-response.v1.schema.json", {"ts": "2026-10-21T10:00:00Z", "id": "auto-0", "model_id": "emb-siglip2-v0.0.1", "embedding": [0.1], "size": 1, "seconds": 0.1}, "required"),
]


@pytest.mark.parametrize(
    "schema_name,instance,keyword",
    [(s, i, k) for _, s, i, k in ANNOTATION_API_INVALID_CASES],
    ids=[name for name, _, _, _ in ANNOTATION_API_INVALID_CASES],
)
@pytest.mark.imp2
def test_annotation_api_invalid_response_is_rejected(schema_name, instance, keyword, schema_registry) -> None:
    schema = json.loads((ROOT / ANNOTATION_API / schema_name).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, registry=schema_registry)
    keywords = {e.validator for e in validator.iter_errors(instance)}
    assert keyword in keywords, f"expected {keyword!r}, got {keywords or 'no errors'}"
