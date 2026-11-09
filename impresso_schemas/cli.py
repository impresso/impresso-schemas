"""Command-line validation for the bundled Impresso schema collection."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .registry import get_validator


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate JSON documents against one of the bundled Impresso JSON schemas."
    )
    parser.add_argument("contract_name", help="Schema name to load, e.g. issue or page")
    parser.add_argument("input_paths", nargs="*", help="JSON files to validate")
    parser.add_argument(
        "--contract-version",
        type=int,
        required=True,
        help="Explicit contract version to use, e.g. --contract-version 2",
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read JSON from standard input instead of input files",
    )
    args = parser.parse_args(argv)

    validator = get_validator(args.contract_name, args.contract_version)
    if args.stdin:
        instance = json.load(sys.stdin)
        validator.validate(instance)
        print(f"OK: {args.contract_name}")
        return 0

    if not args.input_paths:
        parser.error("Provide a JSON file path or --stdin")

    for input_path in args.input_paths:
        with Path(input_path).open("r", encoding="utf-8") as handle:
            instance = json.load(handle)
        validator.validate(instance)
        print(f"OK: {input_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
