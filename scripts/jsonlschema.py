#!/usr/bin/env python3

"""
A module to validate JSON Line files (raw or compressed) against a specified JSON
schema. This script can handle files from various sources (local, cloud storage) through
smart_open, and logs validation errors while allowing for command-line configured
verbosity.

In cases of validation errors, the offending JSON object is logged and skipped. The
script exits with a non-zero status if any validation errors are encountered.
"""

__author__ = "simon.clematide@uzh.ch"
__version__ = "v1.1"

import argparse
import json
import logging
import sys
from typing import Iterable, List, Optional

import jsonschema
import smart_open

log = logging.getLogger(__name__)


class JSONLSchemaValidator:
    """
    A class to validate JSON objects against a given JSON schema.

    Attributes:
        input_files (List[str]): A list of paths to input files containing JSON objects.

        output_writer (TextIOWrapper): A file writer object for the output file,
            defaults to sys.stdout if not specified.

        schema (dict): The loaded JSON schema against which JSON objects will be
        validated.
    """

    def __init__(
        self,
        schema: str,
        input_files: List[str],
        output_file: Optional[str] = None,
        file_format: str = "jsonl",
    ):
        """
        Initializes the JSONLSchemaValidator with a schema, input files, and an optional
        output file.

        Args:
            schema (str): The path to the JSON schema file.
            input_files (List[str]): A list of file paths to read the JSON objects from.
            output_file (Optional[str]): The file path to write validated JSON objects
                to. Writes to stdout if None.
        """

        self.input_files = input_files
        self.file_format = file_format
        self.validation_errors = 0
        self.output_writer = (
            smart_open.open(output_file, mode="w", encoding="utf-8")
            if output_file
            else sys.stdout
        )
        with smart_open.open(schema, encoding="utf-8") as schema_file:
            self.schema = json.load(schema_file)

    def run(self) -> None:
        """Starts the validation process."""

        self.process()
        if self.validation_errors > 0:
            log.error("Validation errors encountered: %d", self.validation_errors)
            sys.exit(1)

    def process(self) -> None:
        """
        Processes each JSON object from the input files, validating them against the
        schema.

        Invalid objects are logged and skipped.
        """

        for jo in self.next_json_object():
            try:
                jsonschema.validate(instance=jo, schema=self.schema)
            except jsonschema.exceptions.ValidationError as e:
                log.error("Validation error: %s", e.message)
                log.info("Offending JSON object ignored: %s", jo)
                self.validation_errors += 1
                continue
            print(
                json.dumps(jo, ensure_ascii=False, separators=(",", ":")),
                file=self.output_writer,
            )

    def next_json_object(self) -> Iterable[dict]:
        """Yields JSON objects based on the specified file format."""

        if self.file_format == "jsonl":
            for infile_path in self.input_files:
                with smart_open.open(infile_path, encoding="utf-8") as infile:
                    for line in infile:
                        if line.strip():  # Skip empty lines
                            yield json.loads(line)
        elif self.file_format == "json":
            for infile_path in self.input_files:
                with smart_open.open(infile_path, encoding="utf-8") as infile:
                    data = json.load(infile)
                    if isinstance(data, list):
                        for item in data:
                            yield item
                    else:
                        yield data


def main():
    """
    Parses command-line arguments and initiates JSON line file validation.
    """
    parser = argparse.ArgumentParser(
        description="Validate JSON Lines files against a schema."
    )
    parser.add_argument("--schema", help="Path to JSON schema file", required=True)
    parser.add_argument("-l", "--logfile", help="Write log to FILE", metavar="FILE")

    parser.add_argument(
        "-o", "--output-file", help="Output file (defaults to stdout if not specified)"
    )
    parser.add_argument("-i", "--input-files", nargs="+", help="Input JSON Lines files")
    parser.add_argument(
        "--file-format",
        choices=["json", "jsonl"],
        help="File format (jsonl or json)",
        default="jsonl",
    )
    parser.add_argument(
        "--level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level. Default: %(default)s",
    )
    args = parser.parse_args()

    to_logging_level = {
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
    }
    logging.basicConfig(
        level=to_logging_level[args.level],
        format="%(asctime)-15s %(levelname)-8s: %(message)s",
        force=True,
    )
    if args.input_files and args.input_files[0].endswith(".json"):
        args.file_format = "json"
        log.info("File format set to JSON")

    validator = JSONLSchemaValidator(
        schema=args.schema,
        input_files=args.input_files or [],
        output_file=args.output_file,
        file_format=args.file_format,
    )
    validator.run()


if __name__ == "__main__":
    main()
