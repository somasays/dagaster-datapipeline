variable "instance-type" {
  type        = string
  description = "The instance type that we will use"
}

variable "instance-name" {
  type        = string
  description = "the name that we will give to our instance by setting its Tags"
}

variable "pem-key" {
  type        = string
  description = "This is the name that will be given to the key-pair used to connect to the instance"
  default     = "simple_ec2"
}

variable "public_subnet" {
  type        = string
  description = "The id of the public subnet created in the VPC module"
}

variable "vpc_security_group_ids" {
  type        = string
  description = "The id of the Security Group created in the SG module"
}

variable "associate_public_ip_address" {
  type        = string
  description = "True or False, associates a public IP address with the instance"
}

variable "ami-id" {
  type        = string
  description = "ID of the Ubuntu AMI"
  default = "ami-05f7491af5eef733a"
}

variable "root_device_type" {
  description = "Type of the root block device"
  type        = string
  default     = "gp2"
}
 
variable "root_device_size" {
  description = "Size of the root block device"
  type        = string
  default     = "150"
}