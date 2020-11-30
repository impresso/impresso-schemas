



tests:
	jsonschema -i examples/newspaper_issue/example0.json  json/newspaper/issue.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper_issue/example1.json  json/newspaper/issue.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper_page/example0.json  json/newspaper/page.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper_page/example1.json  json/newspaper/page.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper_page/example2.json  json/newspaper/page.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/topic_model_topic_description/example0.json  json/topic_model/topic_description.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper_contentitem/example0.json  json/newspaper/contentitem.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/language_identification/example0.json  json/language_identification/language_identification.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/language_identification/example1.json  json/language_identification/language_identification.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/language_identification/example2.json  json/language_identification/language_identification.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"



clean-docs:
	rm docs/*

documentation:
	jsonschema2md -d json/newspaper/ -n -v 06 -o docs
	jsonschema2md -d json/topic_model/ -n -v 06 -o docs
	jsonschema2md -d json/language_identification/ -n -v 06 -o docs
	#jsonschema2md -d json/linguistic_annotation/ -n -v 06 -o docs
