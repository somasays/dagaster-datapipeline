data "aws_vpc" "selected" {
  id = var.vpc_id
}

module "sg" {
  source  = "./sg"
  sg-name = var.sg-name
  vpc_id  = data.aws_vpc.selected.id
}

module "ec2" {
  source                      = "./ec2"
  instance-name               = var.instance-name
  instance-type               = var.instance-type
  public_subnet               = "subnet-06a055b629a9099ed"
  vpc_security_group_ids      = module.sg.aws_sg
  associate_public_ip_address = true
}
