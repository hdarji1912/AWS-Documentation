# ☁️ AWS Global Infrastructure & Shared Responsibility Model

> Understanding the foundation of Amazon Web Services (AWS): Global Infrastructure and the Shared Responsibility Model.

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)
![Level](https://img.shields.io/badge/Level-Beginner-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)


---

---

# 📖 Introduction

Amazon Web Services (AWS) operates one of the world's largest and most secure cloud infrastructures.

Before deploying applications, every cloud engineer should understand:

- How AWS is organized globally
- How Regions and Availability Zones work
- Why Edge Locations exist
- The AWS Global Backbone Network
- The AWS Shared Responsibility Model

These concepts form the foundation of every AWS service.

---

# 🎯 Learning Objectives

After completing this module, you should understand:

- ✅ AWS Global Infrastructure
- ✅ Regions
- ✅ Availability Zones
- ✅ Edge Locations
- ✅ Regional Edge Caches
- ✅ High Availability
- ✅ Fault Tolerance
- ✅ Low Latency
- ✅ Shared Responsibility Model
- ✅ Cloud Security Basics

---

# 🌍 AWS Global Infrastructure

AWS infrastructure consists of multiple components working together worldwide.

```

                    AWS Global Infrastructure

                             AWS
                              │
          ┌───────────────────┼────────────────────┐
          │                   │                    │
      Region A           Region B            Region C
          │                   │                    │
    ┌─────┼─────┐       ┌─────┼─────┐       ┌─────┼─────┐
    │     │     │       │     │     │       │     │     │
   AZ1   AZ2   AZ3     AZ1   AZ2   AZ3     AZ1   AZ2   AZ3

                              │

                     Edge Locations

```

Each Region contains multiple Availability Zones connected by low-latency networking.

---

# 🌎 AWS Regions

A Region is a physical geographic location where AWS has multiple data centres.

Examples:

| Region | Code |
|----------|------|
| N. Virginia | us-east-1 |
| Ohio | us-east-2 |
| Oregon | us-west-2 |
| Mumbai | ap-south-1 |
| Singapore | ap-southeast-1 |
| Frankfurt | eu-central-1 |

## Why Multiple Regions?

- Disaster Recovery
- Regulatory Compliance
- Low Latency
- Business Continuity

---

# 🏢 Availability Zones (AZs)

Each AWS Region contains multiple isolated Availability Zones.

Example:

```

Mumbai Region (ap-south-1)

├── AZ-a
├── AZ-b
└── AZ-c

```

Each AZ has:

- Independent Power
- Independent Cooling
- Independent Networking

Benefits:

- High Availability
- Fault Tolerance
- Disaster Recovery

---

# 🌐 Edge Locations

Edge Locations are smaller AWS sites located closer to end users.

Used by:

- Amazon CloudFront
- Route 53
- AWS Shield
- AWS WAF

Purpose:

- Reduce latency
- Improve performance
- Faster content delivery

---

# ⚡ Regional Edge Caches

Regional Edge Caches sit between CloudFront Edge Locations and the Origin Server.

Benefits:

- Higher cache hit ratio
- Lower latency
- Reduced load on origin servers

---

# 🔗 AWS Global Network

AWS Regions are connected using Amazon's private fibre backbone.

Benefits:

- Secure communication
- High bandwidth
- Low latency
- Global connectivity

---

# 🔐 AWS Shared Responsibility Model

AWS security responsibilities are divided between AWS and the customer.

```

              AWS Shared Responsibility Model

          AWS Responsibility
     ----------------------------
     Physical Security
     Networking
     Storage Hardware
     Data Centres
     Hypervisor
     Global Infrastructure

==============================
 Responsibility Boundary
==============================

     Customer Responsibility
     ----------------------------
     IAM Users & Roles
     MFA
     EC2 Security
     Operating System
     Applications
     Data Encryption
     Security Groups
     Network Configuration

```

---

# 🏢 AWS Responsibilities

AWS manages:

- Physical Data Centres
- Hardware
- Networking
- Storage Infrastructure
- Availability Zones
- Global Infrastructure
- Hypervisor
- Managed Service Infrastructure

AWS calls this:

> **Security OF the Cloud**

---

# 👨‍💻 Customer Responsibilities

Customers manage:

- IAM Users
- IAM Policies
- Password Policies
- MFA
- EC2 Operating Systems
- Security Groups
- NACLs
- Application Security
- Data Encryption
- S3 Bucket Permissions
- Backups

AWS calls this:

> **Security IN the Cloud**

---

# ✅ Best Practices

- Enable MFA
- Use IAM Users instead of Root Account
- Follow Least Privilege Principle
- Encrypt Sensitive Data
- Enable CloudTrail
- Enable AWS Config
- Use Security Groups
- Monitor using CloudWatch
- Rotate Access Keys
- Regularly Review IAM Permissions

---

# 🏗️ Architecture Diagram

```

                    Users
                      │
                      ▼
               AWS Edge Location
                      │
                      ▼
               AWS Region
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
      AZ-1          AZ-2          AZ-3
        │             │             │
        └─────────────┼─────────────┘
                      │
                AWS Services
     EC2 • S3 • RDS • Lambda • VPC

```

---

# 📸 Screenshots

## AWS Global Infrastructure

> Replace with your own screenshot.

```

images/
└── aws-global-infrastructure.png

```

<img src="images/aws-global-infrastructure.png" width="900">

---

## AWS Regions

```

images/
└── aws-regions.png

```

<img src="images/aws-regions.png" width="900">

---

## Availability Zones

```

images/
└── availability-zones.png

```

<img src="images/availability-zones.png" width="900">

---

## Shared Responsibility Model

```

images/
└── shared-responsibility-model.png

```

<img src="images/shared-responsibility-model.png" width="900">

---

# 💡 Key Takeaways

- AWS operates globally through multiple Regions.
- Every Region contains multiple Availability Zones.
- Edge Locations improve application performance.
- AWS Global Network provides secure connectivity.
- AWS secures the cloud infrastructure.
- Customers secure their workloads, applications, and data.
- Understanding the Shared Responsibility Model is essential for designing secure cloud solutions.

---

# 🚀 Skills Gained

- AWS Global Infrastructure
- Cloud Computing Basics
- High Availability
- Fault Tolerance
- Disaster Recovery Concepts
- AWS Networking Basics
- Cloud Security Fundamentals
- Shared Responsibility Model

---


---

## 👨‍💻 Author

**Hardik Darji**

DevOps Engineer | AWS Learner

---

⭐ If you found this repository helpful, don't forget to **Star** it!
