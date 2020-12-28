




tests:
	jsonschema -i examples/newspaper_issue/example0.json  json/newspaper/issue.schema.json && $(print-test-ok) || $(print-test-failed)
	jsonschema -i examples/newspaper_issue/example1.json  json/newspaper/issue.schema.json && $(print-test-ok)|| $(print-test-failed)
	jsonschema -i examples/newspaper_page/example0.json  json/newspaper/page.schema.json && $(print-test-ok)|| $(print-test-failed)
	jsonschema -i examples/newspaper_page/example1.json  json/newspaper/page.schema.json && $(print-test-ok)|| $(print-test-failed)
	jsonschema -i examples/newspaper_page/example2.json  json/newspaper/page.schema.json && $(print-test-ok)|| $(print-test-failed)
	jsonschema -i examples/topic_model_topic_description/example0.json  json/topic_model/topic_description.schema.json && $(print-test-ok)|| $(print-test-failed)
	jsonschema -i examples/newspaper_contentitem/example0.json  json/newspaper/contentitem.schema.json && $(print-test-ok)|| $(print-test-failed)
	jsonschema -i examples/language_identification/example0.json  json/language_identification/language_identification.schema.json && $(print-test-ok)|| $(print-test-failed)
	jsonschema -i examples/language_identification/example1.json  json/language_identification/language_identification.schema.json && $(print-test-ok)|| $(print-test-failed)
	jsonschema -i examples/language_identification/example2.json  json/language_identification/language_identification.schema.json && $(print-test-ok)|| $(print-test-failed)



clean-documentation:
	rm -fv docs/*

documentation:
	# make sure to install the correct jsonschema2md tool:
	# npm install -g @adobe/jsonschema2md
	jsonschema2md -d json/newspaper/ --header false -n -v 06 -o docs  -x -  -s propTable
	jsonschema2md -d json/topic_model/ --header false -n -v 06 -o docs  -x -  -s propTable
	jsonschema2md -d json/language_identification/ --header false -n -v 06 -o docs -x -  -s propTable
	#jsonschema2md -d json/linguistic_annotation/ -n -v 06 -o docs


##########################################################################################
# Simple macros for tests
define print-test-ok
 printf "\033[92m%s\033[0m\n" "✓ Success!"
endef

define print-test-failed
 printf "\033[91m%s\033[0m\n" "✗ Failed!"
endef
