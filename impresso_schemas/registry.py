"""Offline schema registry for the bundled Impresso schema collection."""

from __future__ import annotations

import json
import re
from importlib import resources
from typing import Any

from jsonschema.validators import validator_for
from referencing import Registry, Resource

_PACKAGE_NAME = "impresso_schemas"
_SCHEMA_ROOT = "json"


def _root_package() -> resources.abc.Traversable:
    return resources.files(_PACKAGE_NAME)


def _schema_root() -> tuple[resources.abc.Traversable, str]:
    """Return the schema directory traversable and its relative root name.

    When running from an installed package/wheel, schemas are bundled inside
    `impresso_schemas/json`. When running from an editable/source checkout
    where `json/` lives at the repository root, fallback to `root.parent / 'json'`.
    """
    root = _root_package()
    schema_dir = root / _SCHEMA_ROOT
    if schema_dir.exists():
        return schema_dir, _SCHEMA_ROOT

    # Fallback to repository root for development checkouts
    repo_schema_dir = root.parent / _SCHEMA_ROOT
    if repo_schema_dir.exists():
        return repo_schema_dir, _SCHEMA_ROOT

    return schema_dir, _SCHEMA_ROOT


def _iter_schemas(
    entry: resources.abc.Traversable, prefix: str = ""
) -> list[tuple[str, resources.abc.Traversable]]:
    """Recursively collect schema files with their forward-slash relative path.

    This avoids calling `.relative_to(...)` and `.as_posix()` which raise
    AttributeError on string paths in zip-backed Traversable implementations.
    """
    results: list[tuple[str, resources.abc.Traversable]] = []
    if entry.is_file():
        if entry.name.endswith(".schema.json"):
            results.append((prefix, entry))
    elif entry.is_dir():
        for child in sorted(entry.iterdir(), key=lambda item: item.name):
            child_prefix = f"{prefix}/{child.name}" if prefix else child.name
            results.extend(_iter_schemas(child, child_prefix))
    return results


def _schema_files() -> list[tuple[str, resources.abc.Traversable]]:
    """Return sorted list of (relative_path, traversable) tuples for all schemas."""
    schema_dir, root_name = _schema_root()
    return _iter_schemas(schema_dir, root_name)


def _canonical_id_for(relative_path: str) -> str:
    return f"https://impresso.github.io/impresso-schemas/{relative_path}"


def _normalize_name(name: str) -> str:
    """Normalize contract names for lookup.

    Unknown names must not be fuzzy-matched or fallback via suffix matching.
    """
    value = name.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    aliases = {
        "solr_content_item_paper": "paper_contentitem",
        "solr_content_item_audio": "audio_record_contentitem",
        "paper_contentitem": "paper_contentitem",
        "audio_record_contentitem": "audio_record_contentitem",
        "paper": "paper_contentitem",
        "audio": "audio_record_contentitem",
        "issue": "issue",
        "page": "page",
        "audio_record": "audio_record",
    }
    return aliases.get(normalized, normalized)


def _version_from_name(schema_name: str) -> int:
    match = re.search(r"(?<![a-z0-9])v(\d+)$", schema_name, flags=re.IGNORECASE)
    if match:
        return int(match.group(1))
    if re.search(r"\.v\d+$", schema_name, flags=re.IGNORECASE):
        return int(schema_name.rsplit("v", 1)[-1])
    return 1


def _contract_name_from_schema_path(schema_path: str) -> str:
    name = schema_path.rsplit("/", 1)[-1]
    stem = name.removesuffix(".schema.json")
    if re.search(r"\.v\d+$", stem, flags=re.IGNORECASE):
        base, _ = stem.rsplit(".v", 1)
        return base
    return stem


def load_manifest() -> dict[str, Any]:
    """Return a snapshot of the bundled inventory and recommended selections."""

    contracts: list[dict[str, Any]] = []
    for relative, _ in _schema_files():
        file_name = relative.rsplit("/", 1)[-1]
        stem = file_name.removesuffix(".schema.json")
        contracts.append(
            {
                "name": _contract_name_from_schema_path(relative),
                "version": _version_from_name(stem),
                "canonical_id": _canonical_id_for(relative),
                "path": relative,
                "kind": relative.split("/", 2)[1] if "/" in relative else "root",
            }
        )

    by_name: dict[str, list[dict[str, Any]]] = {}
    for item in contracts:
        by_name.setdefault(item["name"], []).append(item)

    return {
        "collection_version": "0.1.0",
        "available_contracts": [
            {
                "name": contract["name"],
                "version": contract["version"],
                "canonical_id": contract["canonical_id"],
                "path": contract["path"],
            }
            for contract in sorted(contracts, key=lambda item: (item["name"], item["version"]))
        ],
        "recommended_contracts": sorted(
            {item["name"] for item in contracts if item["name"] in {"issue", "page", "audio_record", "paper_contentitem", "audio_record_contentitem"}}
        ),
        "contracts_by_name": {
            name: sorted(items, key=lambda item: item["version"]) for name, items in sorted(by_name.items())
        },
    }


def list_contracts() -> list[dict[str, Any]]:
    return load_manifest()["available_contracts"]


def resolve_schema(name: str, contract_version: int | None = None) -> tuple[str, dict[str, Any]]:
    """Resolve a contract name and explicit version to a bundled schema."""

    if contract_version is None:
        raise ValueError(
            "An explicit contract_version is required. "
            "Do not default to the latest bundled schema in production."
        )

    manifest = load_manifest()
    target = _normalize_name(name)
    matches = []

    for contract in manifest["available_contracts"]:
        if _normalize_name(contract["name"]) == target:
            matches.append(contract)

    if not matches:
        raise ValueError(
            f"Unknown schema contract '{name}'. Available contracts: "
            + ", ".join(sorted({item["name"] for item in manifest["available_contracts"]}))
        )

    selected = next((item for item in matches if item["version"] == contract_version), None)
    if selected is None:
        available_versions = sorted({item["version"] for item in matches})
        raise ValueError(
            f"Schema contract '{name}' is unavailable for version {contract_version}. "
            f"Available versions: {available_versions}"
        )

    schema_file = next(entry for rel, entry in _schema_files() if rel == selected["path"])
    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    return selected["canonical_id"], schema


def _offline_registry() -> Registry:
    """Return an offline registry for all bundled schema resources."""

    resources_by_url: dict[str, Any] = {}
    for relative, schema_file in _schema_files():
        canonical_id = _canonical_id_for(relative)
        resources_by_url[canonical_id] = json.loads(schema_file.read_text(encoding="utf-8"))

    def retrieve(url: str) -> Resource:
        if url not in resources_by_url:
            raise LookupError(f"Unknown canonical schema URL: {url}")
        return Resource.from_contents(resources_by_url[url])

    return Registry(retrieve=retrieve)


def get_validator(name: str, contract_version: int | None = None):
    """Return a JSON Schema validator configured with the offline registry."""

    _, schema = resolve_schema(name, contract_version)
    validator_cls = validator_for(schema)
    return validator_cls(schema, registry=_offline_registry())
