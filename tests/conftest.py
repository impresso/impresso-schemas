"""Shared fixtures and helpers for JSON Schema tests.

Schemas may use published Impresso URLs in ``$ref`` values. The test suite must
validate those references without downloading schemas from GitHub Pages, both so
tests work offline and so they exercise the schema files in the current
checkout. ``schema_registry`` therefore registers every local schema under its
``$id``. Example tests pass this registry to ``Draft202012Validator``; integrity
tests use the same registry to confirm that each repository-local reference can
be resolved.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

ROOT = Path(__file__).parent.parent
SCHEMA_ROOT = ROOT / "json"
PUBLISHED_SCHEMA_BASE = "https://impresso.github.io/impresso-schemas/"


def schema_paths() -> list[Path]:
    """Return every repository schema in deterministic order."""
    return sorted(SCHEMA_ROOT.rglob("*.schema.json"))


def expected_schema_id(path: Path) -> str:
    """Return the published URL that corresponds to a repository schema path."""
    return PUBLISHED_SCHEMA_BASE + path.relative_to(ROOT).as_posix()


def load_schema(path: Path) -> dict[str, Any]:
    """Load one JSON Schema document from disk."""
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def schema_documents() -> dict[Path, dict[str, Any]]:
    """Load every schema once for the test session."""
    return {path: load_schema(path) for path in schema_paths()}


@pytest.fixture(scope="session")
def schema_registry(schema_documents: dict[Path, dict[str, Any]]) -> Registry:
    """Register every local schema by its `$id` for offline `$ref` resolution."""
    resources: list[tuple[str, Resource[dict[str, Any]]]] = []
    for path, schema in schema_documents.items():
        schema_id = schema.get("$id")
        if not isinstance(schema_id, str):
            raise ValueError(f"Schema missing string $id: {path}")
        resources.append(
            (
                schema_id,
                Resource.from_contents(
                    schema,
                    default_specification=DRAFT202012,
                ),
            )
        )
    return Registry().with_resources(resources)
