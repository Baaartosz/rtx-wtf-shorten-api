include ./tests/aws.env
export

# Python Test Makefile
.PHONY: help
default: help

makefile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
makefile_directory := $(realpath $(dir $(makefile_path)))

test:## Run test
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
