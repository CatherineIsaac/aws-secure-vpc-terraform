# AWS Secure VPC Infrastructure with Terraform

## Overview

This project demonstrates the design, deployment, validation, and teardown of a security-focused AWS Virtual Private Cloud (VPC) using Terraform.

The environment was built using Infrastructure as Code (IaC) to create a reproducible AWS network with separate public and private subnets, controlled internet routing, restricted SSH access, and an EC2 instance for connectivity testing.

The project also includes a Python-based VPC audit script using `boto3`, combining infrastructure provisioning with basic cloud security validation.

## Architecture

The environment was deployed in the AWS `us-east-1` region using the following network design:

- **VPC:** `10.20.0.0/16`
- **Public Subnet:** `10.20.1.0/24`
- **Private Subnet:** `10.20.2.0/24`
- **Internet Gateway:** Attached to the VPC
- **Public Route:** Internet-bound traffic routed through the Internet Gateway
- **Security Group:** Inbound SSH access restricted to an authorized source
- **EC2 Instance:** Deployed in the public subnet for connectivity testing

A visual architecture diagram will be added to illustrate the network topology.

## Technologies Used

- AWS
- Terraform
- Python
- boto3
- Linux
- AWS CLI
- Git
- GitHub

## Infrastructure Components

Terraform was used to provision the AWS infrastructure required for the lab, including:

- Virtual Private Cloud (VPC)
- Public subnet
- Private subnet
- Internet Gateway
- Public route table
- Route table association
- Security group
- EC2 instance

The infrastructure is defined as code, allowing the environment to be consistently recreated and destroyed when required.

## Security Design

The project incorporates several security-focused design decisions.

### Network Segmentation

The VPC is divided into separate public and private subnets:

- `10.20.1.0/24` — Public subnet
- `10.20.2.0/24` — Private subnet

This provides a foundation for separating internet-facing resources from workloads that should remain private.

### Restricted SSH Access

Inbound SSH access to the EC2 instance was restricted rather than exposing SSH broadly to the internet.

### Controlled Internet Routing

Internet connectivity for the public subnet is provided through an Internet Gateway and an explicitly configured public route.

The private subnet is kept separate from the public internet path.

### Sensitive File Protection

Local and potentially sensitive Terraform files are excluded from version control using `.gitignore`.

Examples include:

```text
terraform.tfvars
terraform.tfstate
terraform.tfstate.backup
.terraform/
.venv/
```

Terraform state files can contain infrastructure metadata and potentially sensitive information and therefore should not be committed to a public repository.

## Infrastructure as Code Workflow

The infrastructure lifecycle was managed using Terraform.

### Initialize Terraform

```bash
terraform init
```

### Validate the Configuration

```bash
terraform validate
```

### Preview Infrastructure Changes

```bash
terraform plan
```

### Deploy the Infrastructure

```bash
terraform apply
```

### Inspect Managed Resources

```bash
terraform state list
```

### Destroy the Lab Environment

```bash
terraform destroy
```

After testing and validation, the Terraform-managed infrastructure was destroyed to prevent unnecessary AWS resource usage and costs.

## Python VPC Audit

The project also includes a Python security audit script:

```text
scripts/vpc_audit.py
```

The script uses the AWS SDK for Python (`boto3`) to programmatically inspect the AWS VPC environment.

This component demonstrates how Infrastructure as Code can be combined with Python-based security automation and validation.

## Validation and Testing

The infrastructure was deployed and tested in AWS before teardown.

Validation activities included:

- Terraform initialization
- Terraform configuration validation
- Infrastructure planning
- Successful Terraform deployment
- Verification of VPC networking resources
- Verification of public and private subnet creation
- EC2 instance deployment
- SSH connectivity testing
- Terraform state inspection
- Python-based VPC auditing
- Successful Terraform infrastructure destruction

Actual screenshots from the lab environment will be added as implementation evidence.

## Repository Structure

```text
aws-secure-vpc-terraform/
│
├── .gitignore
├── .terraform.lock.hcl
├── README.md
├── main.tf
├── outputs.tf
├── variables.tf
│
└── scripts/
    └── vpc_audit.py
```

Local Terraform state and variable files are intentionally excluded from the repository.

## Production Security Considerations

This environment was designed as a hands-on security engineering lab rather than a production architecture.

For a production deployment, I would consider additional controls such as:

- AWS Systems Manager Session Manager instead of direct SSH access where appropriate
- Private placement of workloads that do not require direct internet exposure
- VPC Flow Logs
- Centralized logging and monitoring
- AWS CloudTrail
- IAM least-privilege policies
- Encryption and centralized key management
- Multi-Availability Zone architecture
- Remote Terraform state storage and state locking
- Automated Terraform security scanning
- CI/CD security validation
- Continuous configuration and compliance monitoring

These controls would improve visibility, resilience, access management, and infrastructure security.

## Lessons Learned

This project provided practical experience with:

- AWS VPC architecture
- CIDR planning and subnetting
- Public and private subnet segmentation
- Internet Gateway configuration
- AWS route tables
- Security group configuration
- EC2 networking
- Terraform variables and outputs
- Terraform resource dependencies
- Infrastructure lifecycle management
- Secure handling of Terraform state and local configuration
- Python and `boto3` for cloud security automation
- Git-based Infrastructure as Code version control

## Project Status

**Completed**

The AWS infrastructure was successfully provisioned, validated, tested, and subsequently destroyed using Terraform.

The Terraform configuration remains in this repository so the environment can be reproduced when required.
