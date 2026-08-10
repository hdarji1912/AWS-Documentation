## Day 8: AWS Storage Architecture — EBS Persistence, EFS & Disaster Recovery

---
## 📌 Lab Overview

This lab provides practical experience with AWS storage services and demonstrates how to design persistent, highly available, and recoverable storage architectures.

The lab covers:

- Amazon EBS gp3 persistent storage
- EBS encryption with AWS KMS
- UUID-based persistent mounting
- EBS volume expansion
- Amazon EBS Snapshots
- Cross-Region Snapshot Copy
- Amazon Data Lifecycle Manager (DLM)
- EBS disaster recovery
- EC2 Placement Groups
- Amazon EFS shared storage
- EFS Mount Targets
- NFS security configuration
- Fast Snapshot Restore
- io2 Multi-Attach
- EC2 Instance Store
- Storage persistence and recovery testing
- Resource cleanup


---
## 🌎 AWS Regions

This lab uses two regions.

Purpose           |	Region	      |    Region Code
Primary           |	N. California	|    us-west-1
Disaster Recovery	| Frankfurt     |	   eu-central-1

Make sure you switch AWS Console regions when performing regional operations.

---
## Part 1 – Amazon EBS Persistence

##  🏗️ Architecture

![Architecture](images/ebs.png)

---

## Step 1: Switch to the Primary Region

Open the AWS Management Console.

Select:
US West (N. California)

Region:
us-west-1

---
## Step 2: Create a Security Group

Navigate to:

EC2
→ Security Groups
→ Create security group

![vpc](images/1.jpg)

---
## Step 3: Launch the Storage EC2 Instance

Navigate to:

EC2
→ Instances
→ Launch Instance

![vpc](images/2.jpg)

EC2 Volume:

![vpc](images/3.jpg)

---
## Step 4: Create an EBS gp3 Volume

Navigate to:

EC2
→ Elastic Block Store
→ Volumes
→ Create volume


---
## Step 5: Attach the EBS Volume

Select the newly created volume.

Choose:

Actions
→ Attach volume

Select:
ec2-storage-lab-01

Confirm the Availability Zone matches the EC2 instance.

![vpc](images/4.jpg)

