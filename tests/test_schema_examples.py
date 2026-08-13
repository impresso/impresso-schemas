"""Validate example JSON files against their schemas using jsonschema + pytest.

Each entry in CASES is a (schema_path, example_path) pair, both relative to
the repository root. Tests are fully self-contained: no shell, no network, no
external CLI tools.

Run all tests:
    python -m pytest tests/ -v

Run a single test by keyword:
    python -m pytest tests/ -v -k "canonical_issue"

Show the first failure in detail:
    python -m pytest tests/ -v -x
"""

import json
import pathlib

import pytest
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).parent.parent

# ---------------------------------------------------------------------------
# Test cases: (schema_path, example_path), both relative to repo root.
# ---------------------------------------------------------------------------
CASES = [
    # canonical/issue
    ("json/canonical/issue.schema.json", "examples/canonical_issue/example0.json"),
    ("json/canonical/issue.schema.json", "examples/canonical_issue/example1.json"),
    ("json/canonical/issue.schema.json", "examples/canonical_issue/CFCE-1996-09-08-a.json"),
    ("json/canonical/issue.schema.json", "examples/canonical_issue/SOC_CP-1939-08-02-a.json"),
    ("json/canonical/issue.schema.json", "examples/canonical_issue/SOC_TH-1941-03-30-a.json"),
    # canonical/page
    ("json/canonical/page.schema.json", "examples/canonical_page/example0.json"),
    ("json/canonical/page.schema.json", "examples/canonical_page/example1.json"),
    ("json/canonical/page.schema.json", "examples/canonical_page/example2.json"),
    ("json/canonical/page.schema.json", "examples/canonical_page/SOC_CP-1939-03-18-a-p0001.json"),
    ("json/canonical/page.schema.json", "examples/canonical_page/SOC_TH-1941-03-30-a-p0001.json"),
    # canonical/audio_record
    ("json/canonical/audio_record.schema.json", "examples/canonical_audio_record/CFCE-1996-09-08-a-r0001.json"),
    # rebuilt/paper_contentitem
    ("json/rebuilt/paper_contentitem.schema.json", "examples/paper_contentitem/example0.json"),
    ("json/rebuilt/paper_contentitem.schema.json", "examples/paper_contentitem/SOC_VS-1943-04-28-a-i0001.json"),
    # rebuilt/audio_record_contentitem
    ("json/rebuilt/audio_record_contentitem.schema.json", "examples/audio_record_contentitem/CFCE-1996-09-08-a-i0001.json"),
    ("json/rebuilt/audio_record_contentitem.schema.json", "examples/audio_record_contentitem/RDN-1950-01-12-a-i0001.json"),
    # topic_model
    ("json/topic_model/topic_description.schema.json", "examples/topic_model_topic_description/example0.json"),
    # language_identification
    ("json/language_identification/language_identification.schema.json", "examples/language_identification/example0.json"),
    ("json/language_identification/language_identification.schema.json", "examples/language_identification/example1.json"),
    ("json/language_identification/language_identification.schema.json", "examples/language_identification/example2.json"),
    # entities
    ("json/entities/entities.schema.json", "examples/entities/example0.json"),
    ("json/entities/entities.schema.json", "examples/entities/example1.json"),
    ("json/entities/entities.schema.json", "examples/entities/example2.json"),
    # versioning
    ("json/versioning/manifest.schema.json", "examples/versioning_manifest/canonical_v0-0-1.json"),
    # embeddings
    ("json/embeddings/embeddings-docs.schema.json", "examples/doc_embeddings/example0.json"),
    ("json/embeddings/embeddings-sentence.schema.json", "examples/sentence_embeddings/sentence_embeddings_example.json"),
    ("json/embeddings/embeddings-chunks.schema.json", "examples/chunk_embeddings/chunk_embeddings_example.json"),
    # text_reuse
    ("json/text_reuse/cluster.schema.json", "examples/text_reuse/tr_cluster_example.json"),
    ("json/text_reuse/passage.schema.json", "examples/text_reuse/tr_passage_example.json"),
    # image_embeddings
    ("json/image_embeddings/image_embeddings.schema.json", "examples/image_embeddings/image_embedding_example.json"),
    # visualizer
    ("json/visualizer/bbox_visualizer.schema.json", "examples/visualizer/actionfem-1927-10-15-a_bbox.json"),
    ("json/visualizer/bbox_visualizer.schema.json", "examples/visualizer/actionfem-1927-10-15-a-i0012_bbox.json"),
    ("json/visualizer/bbox_visualizer.schema.json", "examples/visualizer/actionfem-1927-10-15-a-p0001_bbox.json"),
    # image_classification
    ("json/image_classification/image_classification.schema.json", "examples/image_classification/excelsior-1912-09-13-a-i0207-classif-images.json"),
    # linguistic_annotation
    ("json/linguistic_annotation/lingproc.v2.schema.json", "examples/linguistic_annotation/example1.json"),
]


def _test_id(schema_path: str, example_path: str) -> str:
    schema_stem = pathlib.Path(schema_path).stem.replace(".schema", "")
    example_stem = pathlib.Path(example_path).stem
    return f"{schema_stem}/{example_stem}"


@pytest.mark.parametrize(
    "schema_path,example_path",
    CASES,
    ids=[_test_id(s, e) for s, e in CASES],
)
def test_validates(schema_path: str, example_path: str) -> None:
    schema = json.loads((ROOT / schema_path).read_text(encoding="utf-8"))
    instance = json.loads((ROOT / example_path).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=str)
    assert not errors, "\n\n".join(
        f"{e.json_path}: {e.message}" for e in errors
    )
