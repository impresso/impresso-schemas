
.PHONY: help tests check-python-env check-node-env clean-documentation documentation

help:
	@echo "Usage:"
	@echo "  make tests          Validate all example JSON files against their schemas"
	@echo "  make documentation  Generate Markdown docs from schemas (overwrites docs/)"
	@echo "  make clean-documentation  Remove all generated docs"
	@echo ""
	@echo "Setup:"
	@echo "  python3 -m venv .venv && source .venv/bin/activate && pip install ."
	@echo "  npm install -g @adobe/jsonschema2md"

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

tests: check-python-env
	python3 -m pytest tests/ -v

clean-documentation:
	rm -fv docs/*

documentation: check-python-env check-node-env
	jsonschema2md -d json/ --header false -n -v 2020-12 -o docs -x - -s propTable
