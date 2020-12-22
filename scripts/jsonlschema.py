#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Validate a jsonline file (raw or compressed) against a schema
"""

__appname__ = "jsonlschema"
__author__  = "simon.clematide@uzh.ch"
__version__ = "v1.0"


import sys
import logging
import json
from jsonschema import validate
from smart_open import open
from typing import Iterable
log = logging.getLogger(__name__)

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


class JSONLSchemaValidator(object):

    def __init__(self, schema, input_files, output_file=None):
        self.input_files = input_files
        self.output_writer = open(output_file, mode="w", encoding="utf-8") if output_file is not None else sys.stdout
        self.schema = json.load(open(schema,encoding="utf-8"))

    def run(self) -> None:

        try:
            self.process()
        except:
            self.output_writer.close()


    def process(self) -> None:
        for jo in self.next_json_object():
            validate(instance=jo, schema=self.schema)
            print(json.dumps(jo,ensure_ascii=False,separators=(",", ":")),file=self.output_writer)



    def next_json_object(self) -> Iterable[dict]:
        """Yield each json object.

        :return: Iterator over json objects.
        :rtype: Iterable[dict]

        """

        for infile in self.input_files:
            with open(infile, encoding="utf-8") as infile:
                for line in infile:
                    yield json.loads(line)




if __name__ == '__main__':
    import argparse
    description = ""
    epilog = ""
    parser = argparse.ArgumentParser(description=description, epilog=epilog)
    parser.add_argument('-l', '--logfile', dest='logfile',
                      help='write log to FILE', metavar='FILE')
    parser.add_argument('-v', '--verbose', dest='verbose',default=2,type=int, metavar="LEVEL",
                      help='set verbosity level: 0=CRITICAL, 1=ERROR, 2=WARNING, 3=INFO 4=DEBUG (default %(default)s)')

    parser.add_argument(
        "-o",
        "--output-file",
        default="/dev/stdout",
        help="Output file, writing to stdout if not specified",
    )

    parser.add_argument(
        "-i",
        "--input-files",
        metavar="JSONL",
        nargs="*",
        help="Input files, reading from stdin if not provided",
    )
    parser.add_argument(
        "schema",
        metavar="SCHEMA",
        help="path to schema",
    )

    arguments = parser.parse_args()

    log_levels = [logging.CRITICAL, logging.ERROR, logging.WARNING,
                  logging.INFO, logging.DEBUG]
    logging.basicConfig(level=log_levels[arguments.verbose],
                        format='%(asctime)-15s %(levelname)s: %(message)s')


    jsonl_schema_validator_args = {
        "schema",
        "output_file",
        "input_files",
    }
    # launching application ...
    JSONLSchemaValidator(
        **{k: v for k, v in vars(arguments).items() if k in jsonl_schema_validator_args}
    ).run()
