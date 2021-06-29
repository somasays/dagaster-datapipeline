resource "aws_iam_role" "minikube_default_role" {
  name = "minikube_default_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = "sts:AssumeRole"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy_attachment" "minikube_attach_role_ssm_managed_instance" {
  name = "minikube_attach_role_ssm_managed_instance"
  roles = [aws_iam_role.minikube_default_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

resource "aws_iam_instance_profile" "ssm_minikube_access_profile" {
  name = "ssm_minikube_access_profile"
  role = aws_iam_role.minikube_default_role.name
}