# JSON schemas
This directory contains JSON schemas for the various models exposed by the Impresso Public API.

## Structure

**NOTE** Schemas in this folder are used in the Open API schema. OAS [JSON Schema](https://swagger.io/docs/specification/data-models/) is based on JSON Schema Draft 5, but has some differences. While we convert the schemas automatically to fit the OAS specification, one thing we don't do due to complexity is dereferencing the `definitions` section, which is not supported by OAS. 

This means that schemas in `schemas` directory *must not use definitions section*. If something has to be referenced - it should go to a dedicated file.

## Folder structure

- entities/ - representation of Impresso domain entities as they served by the public API. 
- requests/ - API requests
- responses/ - API responses
