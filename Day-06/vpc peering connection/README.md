## 🔗AWS VPC Peering Connection

##  📖Project Overview

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
| EC2 Instance | test-ec2-instance | prod-ec2-instance |
| Security Group | test-sg | prod-sg |

---

## VPC Peering Connection Steps :

## Step 1 : Create **Test VPC**

```
Name : test-vpc
CIDR : 10.0.0.0/16
```

![vpc](images/1.jpg)

---

## Step 2 : Create **Production VPC**

```
Name : prod-vpc
CIDR : 12.0.0.0/16
```

![vpc](images/2.jpg)

## Created test and prod VPC

![vpc](images/3.jpg)

---

## Step 3 — Create Internet Gateway (Test)

![vpc](images/4.jpg)

Actions → Attach to VPC :
Select

```
test-vpc
```
Attach.


---

## Step 4 — Create Internet Gateway (Prod)

![vpc](images/5.jpg)

Actions → Attach to VPC :
Select

```
prod-vpc
```
Attach.

----

## Step 5 — Create Private Subnet (Test)

```
VPC
test-vpc

Subnet Name
test-subnet

Availability Zone
eu-north-1a

CIDR
10.0.1.0/24
```

![vpc](images/6.jpg)


---

## Step 6 — Create Private Subnet (Prod)

```
VPC
prod-vpc

Subnet Name
prod-subnet

Availability Zone
eu-north-1b

CIDR
12.0.1.0/24
```

![vpc](images/7.jpg)

## Created test and prod subnet :

![vpc](images/8.jpg)

---
## Step 7 — Create Route Table (Test)

```
Name
test-rt

VPC
test-vpc
```
create  route table :

![vpc](images/9.jpg)

Edit route table :

![vpc](images/10.jpg)

Associate subnet :

![vpc](images/11.jpg)

---
## Step 8 — Create Route Table (Prod)

```
Name
prod-rt

VPC
prod-vpc
```
create  route table :

![vpc](images/12.jpg)

Edit route table :

![vpc](images/13.jpg)

Associate subnet :

![vpc](images/14.jpg)

---

## Step 9 - Launch EC2 Instances

## Test EC2 :

```
Name
test-ec2-instance

AMI
ubuntu

Instance Type
t3.micro

Network
test-vpc

Subnet
test-subnet

Security Group
test-sg
```

![vpc](images/15.jpg)

## Production Server :


```
Name
prod-ec2-instance

AMI
ubuntu

Instance Type
t3.micro

Network
prod-vpc

Subnet
prod-subnet

Security Group
prod-sg
```

## Create Security Groups

Allow:

- SSH (22) from your IP
- HTTP (80) 

![vpc](images/16.jpg)

## Created EC2 Instance :

| Name | Subnet |
|------|--------|
| test-ec2-instance | test-subnet |
| prod-ec2-instance | prod-subnet |

![vpc](images/17.jpg)



---

## Step 10 -Create VPC Peering Connection

Fill in:

```
Name
test-prod-vpc-peering

Requester VPC
test-vpc

Accepter VPC
prod-vpc

Account
My Account

Region
Same Region

```

![vpc](images/18.jpg)

---
## Step 11 — Accept Peering Request

accepting request :
![vpc](images/19.jpg)

Request accepted :
![vpc](images/20.jpg)

---
## Step 12 - Update Route Tables

### Test Route Table

| Destination | Target |
|-------------|--------|
|12.0.0.0/16|test-prod-vpc-peering|

![vpc](images/21.jpg)

---

### Production Route Table

| Destination | Target |
|-------------|--------|
|10.0.0.0/16|test-prod-vpc-peering|

![vpc](images/22.jpg)

---

## Step 13 - Verify Connectivity

SSH into one EC2 instance and ping the private IP of the other instance.

```bash
ping 12.0.1.x
```

![vpc](images/23.jpg)

```bash
ping 10.0.1.x
```

Expected Result

```text
64 bytes from 12.0.1.x
```


![vpc](images/24.jpg)

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

AWS | DevOps Engineer

---

## ⭐ If you found this project helpful, don't forget to star the repository!
