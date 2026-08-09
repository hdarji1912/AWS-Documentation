## Day 7: Secure NGINX Golden Image Pipeline – Build, Test & Automate on AWS

---

📌 Project Overview

This project demonstrates two approaches for creating a secure and repeatable NGINX Golden AMI on AWS:

- Manual Golden AMI Creation
- Automated Golden AMI Creation using Amazon EC2 Image Builder

The manual implementation establishes the baseline configuration and security controls. The same baseline is then automated using EC2 Image Builder to provide repeatable image creation, testing, versioning, and distribution.

The project is implemented in the AWS US East (Ohio) – us-east-2 Region.
---

## 🎯 Objectives

By completing this project, the following objectives are achieved:

- Build an Amazon Linux 2023 EC2 instance as an NGINX builder.
- Install and configure NGINX.
- Enforce IMDSv2.
- Enable secure administration through AWS Systems Manager Session Manager.
- Avoid inbound SSH access.
- Create a reusable Golden AMI.
-Launch a test EC2 instance from the Golden AMI.
- Validate NGINX without using User Data on the test instance.
- Automate AMI creation using EC2 Image Builder.
- Create reusable Image Builder components.
- Implement automated image testing.
- Configure Image Builder infrastructure.
- Configure AMI distribution.
- Generate a versioned Golden AMI.
- Validate the generated AMI independently.
- Clean up AWS resources after the lab.

---
## 🏗️ Architecture

Manual Golden AMI Architecture
![Architecture](images/architecture.png)

---
## Part 1 — Manual Golden AMI Creation

The manual workflow was completed using an Ubuntu-based NGINX EC2 instance as the image source. The instance was securely managed through AWS Systems Manager Session Manager with IMDSv2 enforced.

## Step 1 — Create VPC

Create:
![vpc](images/1.jpg)

---
## Step 2 — Create Internet Gateway & Attach to VPC

![vpc](images/2.jpg)

---
## Step 3 — Create Public Subnets A & B

Public Subnet A :
![vpc](images/3.jpg)

Public Subnet B :
![vpc](images/4.jpg)

---
## Step 4 — Create Public Route Table

Navigate to:

VPC
→ Route Tables
→ Create route table

![vpc](images/5.jpg)

Associate Route Table
![vpc](images/6.jpg)

---
## Step 5 — Create Security Group

Navigate to:

EC2
→ Security Groups
→ Create security group

![vpc](images/7.jpg)

---
## Step 6 — Create EC2 IAM Role

Navigate to:

IAM
→ Roles
→ Create role

![vpc](images/8.jpg)

---
## Step 7 — Launch Builder EC2 - Use Security Group and IAM Role 

Navigate to:

EC2
→ Instances
→ Launch instance

Under:

Advanced details
→ User data

Add:
```bash

#!/bin/bash

sudo apt update -y

sudo apt install -y nginx curl

sudo systemctl enable nginx
sudo systemctl start nginx

echo "<h1>NGINX Golden AMI - devops-nginx-builder-01</h1>" \
> /var/www/html/index.html
```
Launch the instance.

![vpc](images/9.jpg)

---
## Step 8 - Verify Builder EC2 

Wait until:

```bash
Instance state:
Running

Status checks:
3/3 checks passed
```

Verify through public IP address :
> hhtp://18.225.55.174

![vpc](images/10.jpg)

---
## Step 9 — Connect Using Session Manager

Navigate to:

EC2
→ Instances
→ ec2-ami-builder-01
→ Connect
→ Session Manager
→ Connect

![vpc](images/11.jpg)

> You should receive a terminal without using SSH.

## Verify NGINX

Run:
```bash
systemctl status nginx

Expected:
Active: active (running)
```

![vpc](images/12.jpg)

## Validate IMDSv2

Run:
```bash
curl -sS -o /dev/null \
-w 'IMDSv1 HTTP status: %{http_code}\n' \
--max-time 3 \
http://169.254.169.254/latest/meta-data/instance-id

Expected:

IMDSv1 HTTP status: 401
```

## Generate IMDSv2 Token

Run:
```bash
TOKEN=$(curl -sS -X PUT \
-H "X-aws-ec2-metadata-token-ttl-seconds: 21600" \
http://169.254.169.254/latest/api/token)
```
## Retrieve Instance ID

Run:
```bash
curl -sS \
-H "X-aws-ec2-metadata-token: $TOKEN" \
http://169.254.169.254/latest/meta-data/instance-id

Expected:
i-xxxxxxxxxxxxxxxxx
```

## Retrieve Availability Zone
Run :
```bash
curl -sS \
-H "X-aws-ec2-metadata-token: $TOKEN" \
http://169.254.169.254/latest/meta-data/placement/availability-zone

Expected:
us-east-2a
```

![vpc](images/13.jpg)

---

## Step 10 — Create Manual Golden AMI

Navigate to:

EC2
→ Instances
→ ec2-ami-builder-01

Select:

Actions
→ Image and templates
→ Create image

![vpc](images/14.jpg)

##  Verify Golden AMI

Navigate to:

EC2
→ AMIs

Find:
```bash
nginx-ami

Wait until:

Status:
Available
```

Created AMI :
![vpc](images/15.jpg)

---
## Step 11 — Launch Test EC2

Select:
nginx-ami

Choose:
Launch instance from AMI

```bash
Name:
ec2-ami-test

Configure:
VPC:
devops--vpc

Subnet:
public-subnet-A

Security Group:
nginx-public-sg

IAM Role:
ec2-ssm-role

Metadata:
IMDSv2 only
```
launch instance 

![vpc](images/16.jpg)

---
## Step 12 — Validate Test EC2 

Connect using:
Session Manager

![vpc](images/17.jpg)

Check NGINX:
```bash
sudo systemctl status nginx

Test application:
curl -I http://localhost
```

![vpc](images/18.jpg)

---
## Part 2 — EC2 Image Builder Automation

The second phase was implemented using Amazon EC2 Image Builder to automate the complete NGINX image lifecycle, from software installation through image validation and AMI publication.

Resources created:

- Image Builder IAM Role -> devops-imagebuilder-role
- Build Component ->  devops-nginx-build-component
- Test Component -> devops-nginx-test-component
- Image Recipe -> devops-nginx-golden-recipe
- Infrastructure Configuration -> devops-imagebuilder-infra
- Distribution Configuration -> devops-nginx-golden-distribution
- Image Pipeline -> devops-nginx-golden-pipeline

Validation: Successfully created the Ubuntu-based EC2 Image Builder components and configuration, executed the automated image pipeline, completed the build and test phases, generated a versioned NGINX Golden AMI, and validated the generated AMI by launching a test EC2 instance without User Data. NGINX, its configuration, and the required image baseline were successfully verified on the test instance.



