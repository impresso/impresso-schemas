#!/usr/bin/python3

"""
A module to validate JSON Line files (raw or compressed) against a specified JSON schema.
This script can handle files from various sources (local, cloud storage) through smart_open,
and logs validation errors while allowing for command-line configured verbosity.
"""

__appname__ = "jsonlschema"
__author__ = "simon.clematide@uzh.ch"
__version__ = "v1.1"

import sys
import logging
import json
import jsonschema
from smart_open import open
from typing import Iterable, List, Optional
import argparse

log = logging.getLogger(__name__)


class JSONLSchemaValidator:
    """
    A class to validate JSON objects against a given JSON schema.

    Attributes:
        input_files (List[str]): A list of paths to input files containing JSON objects.
        output_writer (TextIOWrapper): A file writer object for the output file, defaults to sys.stdout if not specified.
        schema (dict): The loaded JSON schema against which JSON objects will be validated.
    """

    def __init__(
        self,
        schema: str,
        input_files: List[str],
        output_file: Optional[str] = None,
        file_format: str = "jsonl",
    ):
        """
        Initializes the JSONLSchemaValidator with a schema, input files, and an optional output file.

        Args:
            schema (str): The path to the JSON schema file.
            input_files (List[str]): A list of file paths to read the JSON objects from.
            output_file (Optional[str]): The file path to write validated JSON objects to. Writes to stdout if None.
        """
        self.input_files = input_files
        self.file_format = file_format
        self.output_writer = (
            open(output_file, mode="w", encoding="utf-8") if output_file else sys.stdout
        )
        with open(schema, encoding="utf-8") as schema_file:
            self.schema = json.load(schema_file)

    def run(self) -> None:
        """Starts the validation process."""
        self.process()

    def process(self) -> None:
        """
        Processes each JSON object from the input files, validating them against the schema.

        Invalid objects are logged and skipped.
        """
        for jo in self.next_json_object():
            try:
                jsonschema.validate(instance=jo, schema=self.schema)
            except jsonschema.exceptions.ValidationError as e:
                log.error("Validation error: %s", e.message)
                log.info("Offending JSON object ignored: %s", jo)
                continue
            print(
                json.dumps(jo, ensure_ascii=False, separators=(",", ":")),
                file=self.output_writer,
            )

    def next_json_object(self) -> Iterable[dict]:
        """Yields JSON objects based on the specified file format."""
        if self.file_format == "jsonl":
            for infile_path in self.input_files:
                with open(infile_path, encoding="utf-8") as infile:
                    for line in infile:
                        if line.strip():  # Skip empty lines
                            yield json.loads(line)
        elif self.file_format == "json":
            for infile_path in self.input_files:
                with open(infile_path, encoding="utf-8") as infile:
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
        "-v",
        "--verbose",
        default=2,
        type=int,
        metavar="LEVEL",
        help="Set verbosity level",
    )
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
    args = parser.parse_args()

    log_levels = [
        logging.CRITICAL,
        logging.ERROR,
        logging.WARNING,
        logging.INFO,
        logging.DEBUG,
    ]
    logging.basicConfig(
        level=log_levels[min(args.verbose, len(log_levels) - 1)],
        format="%(asctime)-15s %(levelname)s: %(message)s",
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
