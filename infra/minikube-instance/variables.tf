variable "region-master" {
  type    = string
  default = "eu-central-1"
}

variable "vpc_id" {}

variable "owner" {
  type        = string
  description = "The name that we will give to our VPC"
  default     = "Roche-TW-Team"
}

# SG Variables

variable "sg-name" {
  type        = string
  description = "The name that we will give to our Security Group"
  default     = "dagster-test-sg"
}

# EC2 variables

variable "instance-name" {
  type        = string
  description = "The name that we will give to our instance"
  default     = "dagster-test-instance"
}

variable "instance-type" {
  type        = string
  description = "The instance type that we will use"
  default     = "t3a.xlarge"
}

variable "ami-id" {
  type        = string
  description = "ID of the Ubuntu AMI"
  default = "ami-05f7491af5eef733a"
}



