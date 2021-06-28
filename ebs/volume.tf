resource "aws_ebs_volume" "example" {
  availability_zone = "ap-south-1a"
  size              = var.volume_storage_size

  tags = {
    Name = "Terraform-Volume"
  }
}

