# 🌐 Amazon VPC Part 2 –  NAT Gateway · Security Groups vs NACLs · VPC Endpoints · Flow Logs


![AWS](https://img.shields.io/badge/AWS-VPC-orange?logo=amazonaws)
![EC2](https://img.shields.io/badge/Amazon-EC2-orange)

---

# 📖 Overview

This project demonstrates how to build a **production-style Amazon VPC** with secure networking components from scratch.

The architecture includes:

- Public & Private Subnets
- Internet Gateway
- NAT Gateway
- Public & Private Route Tables
- EC2 Instances
- Security Groups
- Network ACLs
- Amazon S3 Gateway Endpoint
- Amazon EC2 Interface Endpoint
- AWS Systems Manager Session Manager
- Amazon CloudWatch VPC Flow Logs

The objective is to provide secure internet access for private workloads while keeping all management traffic inside the AWS network.

---

# 🏗 Architecture

![Arhchitecture](images/architecture.png)

---
## Step 1 Create VPC 

```bash
VPC

→ Create VPC

Settings
Name
devops-vpc

IPv4 CIDR
10.10.0.0/16

IPv6
None

Tenancy
Default

Click
Create VPC

```

![VPC](images/1.jpg)

---
## Step 2 Create Internet Gateway 

```bash
VPC

→ Internet Gateway

Create

Name
devops-igw

After creation

Attach to

devops-vpc

```
![VPC](images/2.jpg) 

---
## Step 3 Create Public Subnet A

```bash

VPC

Subnets

Create

Name
public-subnet-a

AZ
us-east-2a

CIDR

10.10.1.0/24

```
![VPC](images/3.jpg) 





















---


# 📌 AWS Services Used

- Amazon VPC
- Amazon EC2
- Internet Gateway
- NAT Gateway
- Elastic IP
- Route Tables
- Security Groups
- Network ACL
- Amazon S3 Gateway Endpoint
- Amazon EC2 Interface Endpoint
- AWS Systems Manager
- IAM Role
- CloudWatch Logs
- VPC Flow Logs
---

# ⭐ Outcome

Successfully designed and deployed a secure, production-inspired AWS VPC architecture with private networking, outbound internet access via NAT Gateway, VPC Endpoints for secure AWS service connectivity, Session Manager for management access, and VPC Flow Logs for monitoring and troubleshooting.
