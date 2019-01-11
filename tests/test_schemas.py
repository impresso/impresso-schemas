#!/usr/bin/env python
# coding: utf-8 

import python_jsonschema_objects as pjs
import pkg_resources
import os
import json


# note: pjs is insensitive to json shcema versions
def test_get_issue_schema():

    schema_path = "../json/newspaper/issue.schema.json"
    example_path = "../examples/newspaper_issue/example0.json"

    # loading the schema
    with open(os.path.join(schema_path), 'r') as f:
        json_schema = json.load(f)
    builder = pjs.ObjectBuilder(json_schema)
    IssueSchema = builder.build_classes().NewspaperIssue

    # loading and validating the issue
    with open(os.path.join(example_path), 'r') as f:
        json_example = json.load(f)
    issue = IssueSchema(**json_example)
    t = issue.validate()
    assert t is True
    #print(issue.serialize())
