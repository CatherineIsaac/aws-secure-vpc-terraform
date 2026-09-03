terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region  = var.aws_region
  profile = "cloud-lab"
}

resource "aws_vpc" "security_lab" {
  cidr_block = var.vpc_cidr

  tags = {
    Name = "terraform-security-lab-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.security_lab.id
  cidr_block = var.public_subnet_cidr

  tags = {
    Name = "terraform-security-lab-public-subnet"
  }
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.security_lab.id
  cidr_block = var.private_subnet_cidr

  tags = {
    Name = "terraform-security-lab-private-subnet"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.security_lab.id

  tags = {
    Name = "terraform-security-lab-igw"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.security_lab.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "terraform-security-lab-public-rt"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.security_lab.id

  tags = {
    Name = "terraform-security-lab-private-rt"
  }
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}