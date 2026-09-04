
.PHONY: help tests tests-legacy tests-imp2 check-python-env check-node-env check-prettier-env check-markdownlint-env clean-documentation clean-documentation-legacy clean-documentation-imp2 documentation documentation-legacy documentation-imp2 lint-docs lint-docs-legacy lint-docs-imp2 format format-check

LEGACY_SCHEMA_DIRS := canonical rebuilt topic_model language_identification linguistic_annotation entities versioning embeddings text_reuse image_embeddings visualizer image_classification ocr_qa

help:
	@echo "Usage:"
	@echo "  make tests-legacy   Validate legacy schemas and examples"
	@echo "  make tests-imp2     Validate Impresso 2 schemas and examples"
	@echo "  make tests          Run both validation suites"
	@echo "  make documentation-legacy  Generate legacy schema docs in docs/legacy/ (gitignored, published via CI)"
	@echo "  make documentation-imp2    Generate Impresso 2 schema docs in docs/impresso-2/ (gitignored, published via CI)"
	@echo "  make documentation  Regenerate both documentation trees locally for preview"
	@echo "  make clean-documentation  Remove all generated docs"
	@echo "  make format         Auto-format all JSON files with Prettier"
	@echo "  make format-check   Check JSON formatting without modifying files (CI)"
	@echo "  make lint-docs      Auto-fix markdown whitespace in docs/ with markdownlint"
	@echo ""
	@echo "Setup:"
	@echo "  python3 -m venv .venv && source .venv/bin/activate && pip install ."
	@echo "  npm install -g @adobe/jsonschema2md prettier markdownlint-cli"

check-python-env:
	@python3 -c "import pytest, jsonschema" 2>/dev/null || \
	  { echo "ERROR: pytest and/or jsonschema not found."; \
	    echo "       Activate your virtualenv and run: pip install ."; \
	    exit 1; }

check-node-env:
	@jsonschema2md --version 2>/dev/null || \
	  { echo "ERROR: jsonschema2md not found."; \
	    echo "       Install it with: npm install -g @adobe/jsonschema2md"; \
	    exit 1; }

check-prettier-env:
	@prettier --version 2>/dev/null || \
	  { echo "ERROR: prettier not found."; \
	    echo "       Install it with: npm install -g prettier"; \
	    exit 1; }

check-markdownlint-env:
	@markdownlint --version 2>/dev/null || \
	  { echo "ERROR: markdownlint not found."; \
	    echo "       Install it with: npm install -g markdownlint-cli"; \
	    exit 1; }

lint-docs: lint-docs-legacy lint-docs-imp2

lint-docs-legacy: check-markdownlint-env
	markdownlint --fix --disable MD013 MD024 MD041 -- "docs/legacy/**/*.md"

lint-docs-imp2: check-markdownlint-env
	markdownlint --fix --disable MD013 MD024 MD041 -- "docs/impresso-2/**/*.md"

format: check-prettier-env
	prettier --write "json/**/*.json" "examples/**/*.json"

format-check: check-prettier-env
	prettier --check "json/**/*.json" "examples/**/*.json"

tests: tests-legacy tests-imp2

tests-legacy: check-python-env
	python3 -m pytest tests/ -v -m legacy

tests-imp2: check-python-env
	python3 -m pytest tests/ -v -m imp2

clean-documentation:
	rm -rf docs

clean-documentation-legacy:
	rm -rf docs/legacy

clean-documentation-imp2:
	rm -rf docs/impresso-2

documentation: check-python-env check-node-env check-markdownlint-env clean-documentation
	$(MAKE) documentation-legacy
	$(MAKE) documentation-imp2

documentation-legacy: check-python-env check-node-env check-markdownlint-env clean-documentation-legacy
	@for schema_dir in $(LEGACY_SCHEMA_DIRS); do \
		jsonschema2md -d json/$$schema_dir --header false -n -v 2020-12 -o docs/legacy/$$schema_dir -x - -s propTable; \
	done
	$(MAKE) lint-docs-legacy

documentation-imp2: check-python-env check-node-env check-markdownlint-env clean-documentation-imp2
	jsonschema2md -d json/impresso-2/ --header false -n -v 2020-12 -o docs/impresso-2 -x - -s propTable
	$(MAKE) lint-docs-imp2
