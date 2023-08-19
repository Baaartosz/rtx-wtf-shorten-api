terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
  required_version = ">= 1.2.0"
  backend "s3" {
    profile = "terraform"
    region  = "eu-west-2"
    bucket  = "aws-baaart-terraform-state"
    key     = "rtx-wtf-shorten"
  }
}

locals {
  project = "shorten"
}

provider "aws" {
  region  = "eu-west-2"
  profile = "terraform"
}