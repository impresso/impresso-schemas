

tests:
    # see existing validators here: https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#
	check-jsonschema --schemafile json/canonical/issue.schema.json  examples/newspaper_issue/example0.json && $(print-test-ok) || $(print-test-failed)
	check-jsonschema --schemafile json/canonical/issue.schema.json  examples/newspaper_issue/example1.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/canonical/page.schema.json  examples/newspaper_page/example0.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/canonical/page.schema.json  examples/newspaper_page/example1.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/canonical/page.schema.json  examples/newspaper_page/example2.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/topic_model/topic_description.schema.json  examples/topic_model_topic_description/example0.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/rebuilt/paper_contentitem.schema.json  examples/newspaper_contentitem/example0.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/language_identification/language_identification.schema.json  examples/language_identification/example0.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/language_identification/language_identification.schema.json  examples/language_identification/example1.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/language_identification/language_identification.schema.json  examples/language_identification/example2.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/entities/entities.schema.json  examples/entities/example0.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/entities/entities.schema.json  examples/entities/example1.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/entities/entities.schema.json  examples/entities/example2.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/versioning/manifest.schema.json  examples/versioning_manifest/canonical_v0-0-1.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/embeddings/embeddings-docs.schema.json  examples/doc_embeddings/example0.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/text_reuse/cluster.schema.json  examples/text_reuse/tr_cluster_example.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/text_reuse/passage.schema.json  examples/text_reuse/tr_passage_example.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/image_embeddings/image_embeddings.schema.json  examples/image_embeddings/image_emendding_example.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/visualizer/bbox_visualizer.schema.json  examples/visualizer/actionfem-1927-10-15-a_bbox.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/visualizer/bbox_visualizer.schema.json  examples/visualizer/actionfem-1927-10-15-a-i0012_bbox.json && $(print-test-ok)|| $(print-test-failed)
	check-jsonschema --schemafile json/visualizer/bbox_visualizer.schema.json  examples/visualizer/actionfem-1927-10-15-a-p0001_bbox.json && $(print-test-ok)|| $(print-test-failed)


clean-documentation:
	rm -fv docs/*

documentation:
	# make sure to install the correct jsonschema2md tool:
	# npm install -g @adobe/jsonschema2md. also: https://www.npmjs.com/package/@adobe/jsonschema2md
	jsonschema2md -d json/canonical/ --header false -n -v 06 -o docs  -x -  -s propTable
	jsonschema2md -d json/rebuilt/ --header false -n -v 06 -o docs  -x -  -s propTable
	jsonschema2md -d json/topic_model/ --header false -n -v 06 -o docs  -x -  -s propTable
	jsonschema2md -d json/language_identification/ --header false -n -v 06 -o docs -x -  -s propTable
	jsonschema2md -d json/entities/ --header false -n -v 2020-12 -o docs -x -  -s propTable
	jsonschema2md -d json/embeddings/ --header false -n -v 2024-09 -o docs -x -  -s propTable
	jsonschema2md -d json/linguistic_annotation/ -n -v 06 -o docs
	jsonschema2md -d json/versioning/ --header false -n -v 2024-02 -o docs -x -  -s propTable
	jsonschema2md -d json/text_reuse/ --header false -n -v 2024-09 -o docs -x -  -s propTable
	jsonschema2md -d json/image_embeddings/ --header false -n -v 2025-01 -o docs -x -  -s propTable
	jsonschema2md -d json/visualizer/ --header false -n -v 2025-01 -o docs -x -  -s propTable


##########################################################################################
# Simple macros for tests
define print-test-ok
 printf "\033[92m%s\033[0m\n" "✓ Success!"
endef

define print-test-failed
 printf "\033[91m%s\033[0m\n" "✗ Failed!"
endef
