



tests:
	jsonschema -i examples/topic_model_topic_description/example0.json  json/topic_model/topic_description.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper_contentitem/example0.json  json/newspaper/contentitem.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper_issue/example0.json  json/newspaper/issue.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper_page/example0.json  json/newspaper/page.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper_page/example1.json  json/newspaper/page.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"

clean-docs:
	rm docs/*

docs-v4:
	jsonschema2md -d json/newspaper/issue.schema.json -v 04 -o docs/
	jsonschema2md -d json/newspaper/page.schema.json -v 04 -o docs/
	jsonschema2md -d json/newspaper/contentitem.schema.json -v 04 -o docs/

docs-v6:
	jsonschema2md -d json/topic_model/topic_assignment.schema.json -v 06 -o docs
	jsonschema2md -d json/topic_model/topic_description.schema.json -v 06 -o docs
