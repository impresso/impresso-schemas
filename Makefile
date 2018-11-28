



tests:
	jsonschema -i examples/topic_model_topic_description/example0.json  json/topic_model_topic_description.schema.json && printf "%s\n" OK || printf "%s\n" "FAIL"
