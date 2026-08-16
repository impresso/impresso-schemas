"""Repository-wide integrity checks for JSON Schema documents."""

from __future__ import annotations

from collections import Counter
from typing import Any, Iterator
from urllib.parse import urldefrag, urljoin

import pytest
from jsonschema import Draft202012Validator
from referencing import Registry

from conftest import PUBLISHED_SCHEMA_BASE, expected_schema_id, schema_paths


SCHEMA_PATHS = schema_paths()


def _refs(value: Any) -> Iterator[str]:
    """Yield every `$ref` value from a schema document."""
    if isinstance(value, dict):
        ref = value.get("$ref")
        if isinstance(ref, str):
            yield ref
        for nested_value in value.values():
            yield from _refs(nested_value)
    elif isinstance(value, list):
        for item in value:
            yield from _refs(item)


@pytest.mark.parametrize("schema_path", SCHEMA_PATHS, ids=lambda path: path.as_posix())
def test_schema_is_valid_draft_2020_12(schema_path, schema_documents) -> None:
    """Every schema must conform to the declared JSON Schema draft."""
    Draft202012Validator.check_schema(schema_documents[schema_path])


@pytest.mark.parametrize("schema_path", SCHEMA_PATHS, ids=lambda path: path.as_posix())
def test_schema_id_matches_repository_path(schema_path, schema_documents) -> None:
    """Every schema `$id` must be its corresponding published repository URL."""
    assert schema_documents[schema_path].get("$id") == expected_schema_id(schema_path)


def test_schema_ids_are_unique(schema_documents) -> None:
    """A schema `$id` identifies exactly one local schema."""
    schema_ids = [schema.get("$id") for schema in schema_documents.values()]
    duplicates = sorted(
        schema_id for schema_id, count in Counter(schema_ids).items() if count > 1
    )
    assert not duplicates, f"Duplicate schema $id values: {duplicates}"


def test_impresso_schema_references_resolve_locally(
    schema_documents, schema_registry: Registry
) -> None:
    """Published Impresso `$ref` targets must resolve from the local registry."""
    unresolved: list[str] = []

    for schema_path, schema in schema_documents.items():
        schema_id = schema["$id"]
        for ref in _refs(schema):
            if ref.startswith("#"):
                continue

            resolved_ref = urldefrag(urljoin(schema_id, ref)).url
            if not resolved_ref.startswith(PUBLISHED_SCHEMA_BASE):
                continue

            try:
                schema_registry.get_or_retrieve(resolved_ref)
            except Exception as error:  # pragma: no cover - assertion reports it
                unresolved.append(f"{schema_path}: {ref} ({error})")

    assert not unresolved, "Unresolved local Impresso $ref values:\n" + "\n".join(unresolved)
