provider "aws" {
  region = var.region-master
  profile = "roche-elevated"
}

terraform {
  backend "s3" {
    encrypt = true
    bucket = "roche-twde-datapipeline-spike-terraform-state"
    dynamodb_table = "roche-twde-datapipeline-spike-terraform-lock"
    key = "minikube-dagster"
  }
}