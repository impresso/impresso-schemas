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


ANNOTATION_API = "json/impresso-2/annotation-api/entities/"
LINKED = {"ts": "2026-10-15T10:00:00Z", "sys_id": "nel", "NEL seconds": 0.1, "NER seconds": 0.0}

ANNOTATION_API_INVALID_CASES = [
    ("ner_nel_nes_object", "ner-nel-response.v1.schema.json", {**LINKED, "nes": {}}, "type"),
    ("nel_nes_string", "nel-response.v1.schema.json", {**LINKED, "nes": "Berlin"}, "anyOf"),
    ("ner_seconds_not_number", "ner-response.v1.schema.json", {**LINKED, "nes": [], "NER seconds": "0.1"}, "type"),
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
