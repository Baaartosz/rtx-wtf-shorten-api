# Terraform Makefile
.PHONY: help
default: help

makefile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
makefile_directory := $(realpath $(dir $(makefile_path)))

# Setup s3 state bucket for terraform
# AWS_PROFILE   -> AWSCLI deployment profile
# REGION 		-> AWS Region to deploy bucket to
# BUCKET_NAME  -> Name of state bucket
state-bucket: ## Setup Terraform State Bucket
state-bucket: $(foreach var,AWS_PROFILE BUCKET_NAME REGION,guard-$(var))
	@chmod +X setup-state-bucket.sh
	@./setup-state-bucket.sh $(AWS_PROFILE) $(BUCKET_NAME) $(REGION)

init: ## Initialise terraform
	terraform init

plan: ## Run a terraform plan
	terraform plan

apply: ## Run a terraform apply
	terraform apply -auto-approve=true

destroy: ## Run a terraform destroy
	terraform destroy -auto-approve=true

get: ## Update module list
	terraform get

lock: ## Update lock file
	terraform providers lock

clean: ## Clean terraform
	rm -rf $(makefile_directory)/.terraform

setup: ## Setup terraform backend
setup: clean get lock init

guard-%: # Guard for ensuring variables are provided into make tasks
	@if [ -z '${${*}}' ]; then \
		echo 'Environment Variable $* is not set.' && exit 1; \
	fi

help:
	@echo "Usage: make <target>"
	@echo
	@echo "Targets:"
	@egrep "^(.+)\:\ ##\ (.+)" $(MAKEFILE_LIST) | column -t -c 2 -s ":#"