import json
import subprocess
import sys
from pathlib import Path

import pytest

from impresso_schemas import get_validator, list_contracts, load_manifest

ROOT = Path(__file__).parent.parent


def test_manifest_lists_bundled_contracts() -> None:
    manifest = load_manifest()
    assert manifest["collection_version"] == "0.1.0"
    assert "issue" in {contract["name"] for contract in manifest["available_contracts"]}
    assert "issue" in manifest["recommended_contracts"]


def test_get_validator_requires_explicit_version() -> None:
    with pytest.raises(ValueError, match="explicit contract_version"):
        get_validator("issue")

    validator = get_validator("issue", contract_version=1)
    payload = json.loads((ROOT / "examples/canonical_issue/example0.json").read_text(encoding="utf-8"))
    assert validator.is_valid(payload)

    with pytest.raises(ValueError, match="unavailable for version 99"):
        get_validator("issue", contract_version=99)

    with pytest.raises(ValueError, match="Unknown schema contract 'not_an_issue'"):
        get_validator("not_an_issue", contract_version=1)


def test_jsonlschema_cli_available() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "jsonlschema",
            "--help",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "Validate JSON Lines files against a schema" in result.stdout


def test_cli_validates_example_file() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "impresso_schemas",
            "--contract-version",
            "1",
            "issue",
            str(ROOT / "examples/canonical_issue/example0.json"),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "OK:" in result.stdout
