# Terraform Makefile
.PHONY: help
default: help

makefile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
makefile_directory := $(realpath $(dir $(makefile_path)))

setup-state-bucket: ## Setup Terraform State Bucket
	$(MAKE) -C terraform setup-state-bucket

terraform-setup: ## Setup terraform backend
	$(MAKE) -C terraform setup

terraform-plan: ## Run a terraform plan
	$(MAKE) -C terraform plan

terraform-apply: ## Run a terraform apply
	$(MAKE) -C terraform apply

terraform-destroy: ## Run a terraform apply
	$(MAKE) -C terraform destroy

build: ## Build url shorten handler
	$(MAKE) -C url-shorten-handler build-zip

guard-%: # Guard for ensuring variables are provided into make tasks
	@if [ -z '${${*}}' ]; then \
		echo 'Environment Variable $* is not set.' && exit 1; \
	fi

help:
	@echo "Usage: make <target>"
	@echo
	@echo "Targets:"
	@egrep "^(.+)\:\ ##\ (.+)" $(MAKEFILE_LIST) | column -t -c 2 -s ":#"