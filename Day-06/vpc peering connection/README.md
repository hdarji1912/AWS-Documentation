## AWS VPC Peering Connection

## 📌 Project Overview

This project demonstrates how to establish secure private communication between two Amazon Virtual Private Clouds (VPCs) using **AWS VPC Peering**. The implementation enables EC2 instances in separate VPCs to communicate over the AWS private network without traversing the public internet.

The lab includes the creation of two VPCs, private subnets, route tables, security groups, Internet Gateways, EC2 instances, and a VPC Peering Connection.

---

# 🎯 Objectives

- Create two isolated VPCs
- Configure private subnets
- Launch EC2 instances in each VPC
- Create and accept a VPC Peering Connection
- Update route tables for inter-VPC communication
- Configure Security Groups
- Verify connectivity using private IP addresses

---

## 🌐 Network Architecture


![Architecture](images/architecture.png)


---

# 📋 Architecture Details

| Resource | Test Environment | Production Environment |
|----------|------------------|------------------------|
| VPC | test-vpc | prod-vpc |
| CIDR | 10.0.0.0/16 | 12.0.0.0/16 |
| Subnet | test-subnet | prod-subnet |
| Subnet CIDR | 10.0.1.0/24 | 12.0.1.0/24 |
| Route Table | test-rt | prod-rt |
| Internet Gateway | test-igw | prod-igw |
| EC2 Instance | test-server | prod-server |
| Security Group | test-sg | prod-sg |

---

# 🚀 Deployment Steps

## Step 1

Create **Test VPC**

```
Name : test-vpc
CIDR : 10.0.0.0/16
```

![vpc](images/1.jpg)

---

## Step 2

Create **Production VPC**

```
Name : prod-vpc
CIDR : 12.0.0.0/16
```

![vpc](images/2.jpg)

## Created test and prod VPC

![vpc](images/3.jpg)

---

## Step 3

Create Internet Gateways

| Name |
|------|
| test-igw |
| prod-igw |

Attach each Internet Gateway to its respective VPC.

📷 Screenshot

```
images/03-internet-gateway.png
```

---

## Step 4

Create Private Subnets

| Name | CIDR |
|------|------|
| test-private-subnet-1a | 10.0.1.0/24 |
| prod-private-subnet-1a | 12.0.1.0/24 |

📷 Screenshot

```
images/04-private-subnets.png
```

---

## Step 5

Create Route Tables

| Name |
|------|
| test-private-rt |
| prod-private-rt |

Associate each route table with its private subnet.

📷 Screenshot

```
images/05-route-table.png
```

---

## Step 6

Launch EC2 Instances

| Name | Subnet |
|------|--------|
| test-server | test-private-subnet-1a |
| prod-server | prod-private-subnet-1a |

📷 Screenshot

```
images/06-ec2.png
```

---

## Step 7

Create Security Groups

Allow:

- SSH (22) from your IP
- ICMP from the opposite VPC CIDR

📷 Screenshot

```
images/07-security-group.png
```

---

## Step 8

Create VPC Peering Connection

```
Name

test-prod-vpc-peering
```

Requester

```
test-vpc
```

Accepter

```
prod-vpc
```

Accept the request.

📷 Screenshot

```
images/08-vpc-peering.png
```

---

## Step 9

Update Route Tables

### Test Route Table

| Destination | Target |
|-------------|--------|
|10.0.0.0/16|Local|
|12.0.0.0/16|test-prod-vpc-peering|

---

### Production Route Table

| Destination | Target |
|-------------|--------|
|12.0.0.0/16|Local|
|10.0.0.0/16|test-prod-vpc-peering|

📷 Screenshot

```
images/09-route-update.png
```

---

## Step 10

Verify Connectivity

SSH into one EC2 instance and ping the private IP of the other instance.

```bash
ping 12.0.1.x
```

```bash
ping 10.0.1.x
```

Expected Result

```text
64 bytes from 12.0.1.x
```

📷 Screenshot

```
images/10-connectivity-test.png
```

---

# 🔒 Security Considerations

- Communication remains on the AWS private backbone.
- No VPN or Internet Gateway is required for inter-VPC communication.
- Security Groups control inbound and outbound traffic.
- Route Tables explicitly define peering routes.
- VPC Peering does not support transitive routing.

---

# ⚠️ Limitations of VPC Peering

- No transitive routing.
- Overlapping CIDR blocks are not supported.
- No edge-to-edge routing.
- Peering connections are non-hierarchical.
- Route tables must be updated manually.

---

# ✅ Verification Checklist

- [x] Test VPC created
- [x] Production VPC created
- [x] Internet Gateways attached
- [x] Private Subnets created
- [x] Route Tables configured
- [x] Security Groups configured
- [x] EC2 instances launched
- [x] VPC Peering Connection created
- [x] Peering request accepted
- [x] Routes updated
- [x] Connectivity verified

---

# 📚 Key Learnings

- Amazon VPC architecture
- CIDR planning
- VPC Peering concepts
- Route Table configuration
- Security Group management
- Private networking in AWS
- EC2 communication across VPCs
- AWS networking best practices

---

# 🛠️ AWS Services Used

- Amazon VPC
- VPC Peering Connection
- Amazon EC2
- Internet Gateway
- Route Tables
- Security Groups
- Private Subnets
  
---
# 🧹 Cleanup

Delete the resources in the following order:

1. Terminate EC2 Instances
2. Delete VPC Peering Connection
3. Delete Security Groups
4. Delete Route Tables
5. Delete Subnets
6. Detach and Delete Internet Gateways
7. Delete VPCs

---

# 👨‍💻 Author

**Hardik Darji**

AWS | DevOps | Cloud Engineer

---

## ⭐ If you found this project helpful, don't forget to star the repository!
