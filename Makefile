



tests:
	jsonschema -i examples/topic_model_topic_description/example0.json  json/topic_model/topic_description.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper/rebuilt.example.json  json/newspaper/rebuilt.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"

docs-v4:
	jsonschema2md -d json/newspaper/newspaper_issue.schema.json -v 04 -o docs/
	jsonschema2md -d json/newspaper/newspaper_page.schema.json -v 04 -o docs/
	jsonschema2md -d json/newspaper/rebuilt.schema.json -v 04 -o docs/

docs-v6:
	jsonschema2md -d json/topic_model/topic_assignment.schema.json -v 06 -o docs
	jsonschema2md -d json/topic_model/topic_description.schema.json -v 06 -o docs
