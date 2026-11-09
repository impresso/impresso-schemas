"""Runtime access to the bundled Impresso schemas.

The package intentionally ships the schema inventory with the wheel so that
applications can validate JSON documents without any network access.
"""

from .registry import get_validator, list_contracts, load_manifest, resolve_schema

__all__ = [
    "get_validator",
    "list_contracts",
    "load_manifest",
    "resolve_schema",
]
