



tests:
	jsonschema -i examples/topic_model_topic_description/example0.json  json/topic_model/topic_description.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
	jsonschema -i examples/newspaper/rebuilt.example.json  json/newspaper/rebuilt.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
