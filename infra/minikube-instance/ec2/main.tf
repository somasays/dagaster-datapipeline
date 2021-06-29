resource "aws_key_pair" "master-key" {
  key_name   = var.pem-key
  public_key = file("~/.ssh/id_rsa.pub")
}

data "template_file" "user_data" {
  template = file("${path.module}/user-data.sh")
}

resource "aws_instance" "simple_ec2" {
  ami                         = var.ami-id
  instance_type               = var.instance-type
  key_name                    = aws_key_pair.master-key.key_name
  associate_public_ip_address = var.associate_public_ip_address
  vpc_security_group_ids      = [var.vpc_security_group_ids]
  subnet_id                   = var.public_subnet
  user_data                   = data.template_file.user_data.rendered

  root_block_device {
    delete_on_termination = true
    encrypted             = false
    volume_size           = var.root_device_size
    volume_type           = var.root_device_type
  }

  tags = {
    Name = var.instance-name
    Owner = "Soma Sundaram Sekar"
  }
}

