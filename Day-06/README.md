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

# 🗺 Network Design

## Region

```
us-east-2
```

## VPC

```
10.10.0.0/16
```

## Subnets

| Subnet | Availability Zone | CIDR |
|----------|-------------------|------------|
| Public-A | us-east-2a | 10.10.1.0/24 |
| Public-B | us-east-2b | 10.10.2.0/24 |
| Private-A | us-east-2a | 10.10.11.0/24 |
| Private-B | us-east-2b | 10.10.12.0/24 |

---

# 🏛 Architecture Components

## Internet Gateway

Provides internet connectivity for resources in public subnets.

---

## NAT Gateway

Allows private EC2 instances to access the internet without exposing them to inbound internet traffic.

---

## Route Tables

### Public Route Table

| Destination | Target |
|--------------|-----------|
|10.10.0.0/16|Local|
|0.0.0.0/0|Internet Gateway|

### Private Route Table

| Destination | Target |
|--------------|-----------|
|10.10.0.0/16|Local|
|0.0.0.0/0|NAT Gateway|

---

## EC2 Instances

### Public EC2

Purpose

- Apache Web Server
- Internet Accessible

### Private EC2

Purpose

- Backend Server
- No Public IP
- Managed using Session Manager

---

## Security Groups

### Web Security Group

Inbound

- HTTP (80)
- SSH (22)

### Private Security Group

Inbound

- HTTPS (443)
- Internal VPC Communication

---

## Network ACL

Custom subnet-level firewall used to demonstrate:

- HTTP Allow
- HTTP Deny
- Traffic Recovery

---

## Amazon S3 Gateway Endpoint

Provides private connectivity between the VPC and Amazon S3.

Benefits

- No Internet Gateway required
- No NAT data processing charges
- Secure AWS Backbone Network

---

## Amazon EC2 Interface Endpoint

Provides private API connectivity to EC2 services.

Benefits

- Uses Private DNS
- No Internet Access Required
- Secure AWS Backbone Communication

---

## AWS Systems Manager

Used for secure shell access to private EC2 instances.

Benefits

- No Bastion Host
- No Public IP
- No SSH Keys

---

## VPC Flow Logs

Captures network traffic for auditing and troubleshooting.

Destination

```
Amazon CloudWatch Logs
```

---

# 🚀 Deployment Steps

## Step 1

Create VPC

## Step 2

Attach Internet Gateway

## Step 3

Create Public & Private Subnets

## Step 4

Create Route Tables

## Step 5

Launch Public EC2

## Step 6

Allocate Elastic IP

## Step 7

Create NAT Gateway

## Step 8

Launch Private EC2

## Step 9

Configure Session Manager

## Step 10

Create Security Groups

## Step 11

Create Network ACL

## Step 12

Create S3 Gateway Endpoint

## Step 13

Create EC2 Interface Endpoint

## Step 14

Enable VPC Flow Logs

---

# ✅ Validation

✔ Public EC2 accessible from browser

✔ Private EC2 has no Public IP

✔ Session Manager working

✔ Internet connectivity through NAT Gateway

✔ AWS CLI working

✔ HTTP traffic allowed by Security Group

✔ HTTP blocked by NACL

✔ HTTP restored after removing deny rule

✔ Amazon S3 reachable through Gateway Endpoint

✔ EC2 API resolved using Interface Endpoint

✔ CloudWatch recorded ACCEPT traffic

✔ CloudWatch recorded REJECT traffic

---

# 📷 Screenshots

## 1. NAT Gateway

```
images/01_NAT_Gateway.png
```

---

## 2. Private Route Table

```
images/02_Private_Route_Table.png
```

---

## 3. Public Route Table

```
images/03_Public_Route_Table.png
```

---

## 4. Public EC2

```
images/04_Public_EC2.png
```

---

## 5. Private EC2

```
images/05_Private_EC2.png
```

---

## 6. Session Manager

```
images/06_Session_Manager.png
```

---

## 7. Internet Connectivity

```
images/07_Curl_Test.png
```

---

## 8. AWS CLI Identity

```
images/08_STS_Get_Caller_Identity.png
```

---

## 9. Web Security Group

```
images/09_Web_Security_Group.png
```

---

## 10. Web Server Running

```
images/10_Web_Server.png
```

---

## 11. Custom Network ACL

```
images/11_Custom_NACL.png
```

---

## 12. HTTP Blocked

```
images/12_HTTP_Blocked.png
```

---

## 13. HTTP Restored

```
images/13_HTTP_Restored.png
```

---

## 14. Amazon S3 Gateway Endpoint

```
images/14_S3_Gateway_Endpoint.png
```

---

## 15. Prefix List Route

```
images/15_Prefix_List_Route.png
```

---

## 16. Amazon S3 Validation

```
images/16_S3_List_Buckets.png
```

---

## 17. EC2 Interface Endpoint

```
images/17_Interface_Endpoint.png
```

---

## 18. Private DNS

```
images/18_Private_DNS.png
```

---

## 19. VPC Flow Logs

```
images/19_VPC_Flow_Logs.png
```

---

## 20. REJECT Traffic

```
images/20_REJECT.png
```

---

## 21. ACCEPT Traffic

```
images/21_ACCEPT.png
```

---

## 22. AWS Resource Map

```
images/22_Architecture.png
```

---

# 💡 Key Learnings

- Designing a highly available VPC architecture
- Public vs Private subnet routing
- NAT Gateway implementation
- Security Groups vs Network ACLs
- Secure private connectivity using VPC Endpoints
- Managing EC2 without SSH using Session Manager
- Monitoring network traffic with VPC Flow Logs
- Reducing NAT Gateway costs using S3 Gateway Endpoints

---

# 🧹 Cleanup

Delete resources in the following order:

1. Terminate EC2 Instances
2. Delete Interface Endpoint
3. Delete NAT Gateway
4. Release Elastic IP
5. Delete S3 Gateway Endpoint
6. Delete VPC Flow Logs
7. Delete CloudWatch Log Group
8. Restore Original NACL Association
9. Delete Custom NACL
10. Delete Security Groups
11. Delete Route Tables
12. Delete Internet Gateway
13. Delete Subnets
14. Delete VPC

---

# 📚 References

- AWS VPC Documentation
- Amazon EC2 Documentation
- AWS Systems Manager
- Amazon VPC Endpoints
- Amazon CloudWatch Logs

---

# ⭐ Outcome

Successfully designed and deployed a secure, production-inspired AWS VPC architecture with private networking, outbound internet access via NAT Gateway, VPC Endpoints for secure AWS service connectivity, Session Manager for management access, and VPC Flow Logs for monitoring and troubleshooting.
