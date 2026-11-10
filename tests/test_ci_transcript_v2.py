"""Narrow v3 CI roots retain compatibility while checking generic sections."""

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
AREA = "impresso-2/solr-indexing/content-item"


@pytest.mark.imp2
@pytest.mark.parametrize("medium", ["paper", "audio"])
def test_ci_primary_text_contract(medium):
    resources = []
    for path in (ROOT / "json/impresso-2").rglob("*.schema.json"):
        schema = json.loads(path.read_text())
        resources.append((schema["$id"], Resource.from_contents(schema)))
    schema = json.loads(
        (ROOT / f"json/{AREA}/content-item.root.{medium}.v3.schema.json").read_text()
    )
    validator = Draft202012Validator(
        schema, registry=Registry().with_resources(resources)
    )
    doc = json.loads(
        (ROOT / f"examples/{AREA}/ci_{medium}.v3.example.json").read_text()
    )
    validator.validate(doc)
    for invalid in [123, ["Rubrica"]]:
        bad = copy.deepcopy(doc)
        bad["section_title_txt"] = invalid
        with pytest.raises(ValidationError):
            validator.validate(bad)
    body = doc.pop("content_txt_pt")
    with pytest.raises(ValidationError):
        validator.validate(doc)
    for field in [
        "content_txt",
        "content_txt_lb",
        *[f"content_txt_{code}" for code in ("de", "en", "es", "fr", "it", "nl", "pt")],
    ]:
        validator.validate({**doc, field: body})
