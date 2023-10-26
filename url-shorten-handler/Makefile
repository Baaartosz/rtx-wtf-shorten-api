# Python Lambda Makefile
.PHONY: help
default: help

makefile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
makefile_directory := $(realpath $(dir $(makefile_path)))
artifact_name := "url-shorten-handler.zip"

## Useful for importing project folders which are shared between the main poetry project
## -> poetry self add poetry-multiproject-plugin
build-zip: ## Build Artifact Zip
	poetry build -f wheel
	poetry run pip install -q         \
		--upgrade 			           \
		--only-binary :all:             \
		--platform manylinux2014_x86_64 \
		--target package dist/*.whl
	rm $(artifact_name) || echo "Code artifact not found"
	cd package && zip -rq ../$(artifact_name) . -x "*.pyc" -x "*dist-info*" -x "*/__pycache__/*"
	rm -r dist/ package/

test: ## Run pytests
	poetry run pytest

setup-env: ## Setup poetry environment
	poetry env use 3.11
	poetry lock; poetry install;

guard-%: # Guard for ensuring variables are provided into make tasks
	@if [ -z '${${*}}' ]; then \
		echo 'Environment Variable $* is not set.' && exit 1; \
	fi

help:
	@echo "Usage: make <target>"
	@echo
	@echo "Targets:"
	@egrep "^(.+)\:\ ##\ (.+)" $(MAKEFILE_LIST) | column -t -c 2 -s ":#"
