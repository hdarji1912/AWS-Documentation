# 🌐 AWS Transit Gateway - Centralized Multi-VPC Connectivity

> A hands-on AWS networking project demonstrating how to use **AWS Transit Gateway (TGW)** to centrally connect multiple Amazon VPCs using a scalable **Hub-and-Spoke Architecture**.

---

## 📌 Project Overview

This project demonstrates how to build a centralized AWS network using **AWS Transit Gateway**. Instead of creating multiple VPC Peering connections, all VPCs are attached to a single Transit Gateway, allowing secure and scalable communication between VPCs.

The lab includes three VPCs:

- 🟢 Production VPC
- 🔵 Development VPC
- 🟠 Test VPC

Each VPC contains:

- Public Subnet
- Route Table
- Internet Gateway
- Public EC2 Instance

All VPCs are connected through a single AWS Transit Gateway.

---

# 🏗️ Architecture

![Architecture](images/architecture.png)


---

# 🎯 Objectives

- Understand AWS Transit Gateway
- Build a Hub-and-Spoke Network Architecture
- Connect multiple VPCs using Transit Gateway
- Configure VPC Attachments
- Configure Transit Gateway Route Tables
- Update VPC Route Tables
- Verify inter-VPC communication
- Test private connectivity between EC2 instances

---

# 📚 Services Used

- Amazon VPC
- AWS Transit Gateway
- Amazon EC2
- Internet Gateway
- Route Tables
- Security Groups

---

# 🏢 Architecture Components

## Production VPC

| Property | Value |
|----------|-------|
| CIDR | 10.0.0.0/16 |
| Public Subnet | 10.0.1.0/24 |
| EC2 | production-ec2 |

---

## Development VPC

| Property | Value |
|----------|-------|
| CIDR | 20.0.0.0/16 |
| Public Subnet | 20.0.1.0/24 |
| EC2 | development-ec2 |

---

## Test VPC

| Property | Value |
|----------|-------|
| CIDR | 30.0.0.0/16 |
| Public Subnet | 30.0.1.0/24 |
| EC2 | test-ec2 |

---

# 🌍 Network Topology

```
                    AWS Region

             +----------------------+
             | AWS Transit Gateway  |
             +----------+-----------+
                        |
      +-----------------+-----------------+
      |                 |                 |
      |                 |                 |
+------------+   +--------------+   +------------+
|Production  |   | Development  |   |   Test     |
|VPC         |   | VPC          |   | VPC        |
|10.0.0.0/16 |   |20.0.0.0/16   |   |30.0.0.0/16 |
+------------+   +--------------+   +------------+
      |                 |                 |
 Public EC2       Public EC2        Public EC2
```

---

# 🛠️ Implementation Steps

## Step 1

Create Production VPC

- Internet Gateway
- Public Subnet
- Route Table
- Public EC2

---

## Step 2

Create Development VPC

- Internet Gateway
- Public Subnet
- Route Table
- Public EC2

---

## Step 3

Create Test VPC

- Internet Gateway
- Public Subnet
- Route Table
- Public EC2

---

## Step 4

Create AWS Transit Gateway

Configure

- Amazon Side ASN
- Default Association
- Default Propagation
- DNS Support

---

## Step 5

Create Transit Gateway Attachments

Attach

- Production VPC
- Development VPC
- Test VPC

---

## Step 6

Update Route Tables

Production Route Table

| Destination | Target |
|------------|--------|
|10.0.0.0/16|Local|
|20.0.0.0/16|Transit Gateway|
|30.0.0.0/16|Transit Gateway|
|0.0.0.0/0|Internet Gateway|

---

Development Route Table

| Destination | Target |
|------------|--------|
|20.0.0.0/16|Local|
|10.0.0.0/16|Transit Gateway|
|30.0.0.0/16|Transit Gateway|
|0.0.0.0/0|Internet Gateway|

---

Test Route Table

| Destination | Target |
|------------|--------|
|30.0.0.0/16|Local|
|10.0.0.0/16|Transit Gateway|
|20.0.0.0/16|Transit Gateway|
|0.0.0.0/0|Internet Gateway|

---

# 🔀 Traffic Flow

```
Production EC2
      │
      ▼
Production Route Table
      │
      ▼
AWS Transit Gateway
      │
      ▼
Development Route Table
      │
      ▼
Development EC2
```

The same routing path applies for communication with the Test VPC.

---

# 🔒 Security Configuration

Security Groups allow:

- SSH (22) from your public IP
- ICMP (Ping) for connectivity testing
- Intra-VPC communication through Transit Gateway

---

# 🧪 Validation

Verify:

- Production EC2 → Development EC2
- Production EC2 → Test EC2
- Development EC2 → Test EC2

Run:

```bash
ping <Private-IP>
```

Expected Result:

```
64 bytes from ...
```

Successful replies confirm Transit Gateway routing is functioning correctly.

---

# 📊 Resources Created

| Resource | Count |
|----------|------:|
| VPC | 3 |
| Public Subnets | 3 |
| Internet Gateways | 3 |
| Route Tables | 3 |
| EC2 Instances | 3 |
| Transit Gateway | 1 |
| Transit Gateway Attachments | 3 |

---

# 📸 Screenshots

## AWS Transit Gateway

```
images/01-transit-gateway.png
```

---

## VPC Attachments

```
images/02-vpc-attachments.png
```

---

## Transit Gateway Route Table

```
images/03-tgw-route-table.png
```

---

## Production Route Table

```
images/04-production-route-table.png
```

---

## Development Route Table

```
images/05-development-route-table.png
```

---

## Test Route Table

```
images/06-test-route-table.png
```

---

## EC2 Instances

```
images/07-ec2-instances.png
```

---

## Ping Test

```
images/08-connectivity-test.png
```

---

# 📖 Key Learning Outcomes

- Understood Hub-and-Spoke networking architecture.
- Learned how AWS Transit Gateway simplifies multi-VPC connectivity.
- Configured VPC Attachments and Transit Gateway Route Tables.
- Updated VPC Route Tables for centralized routing.
- Validated secure inter-VPC communication using private IP addresses.
- Compared Transit Gateway with traditional VPC Peering.

---

# 🚀 Benefits of AWS Transit Gateway

- Centralized network management
- Scalable multi-VPC connectivity
- Reduced routing complexity
- Simplified architecture
- Supports hybrid cloud connectivity
- Enables cross-account networking with AWS Organizations
- High availability and fault tolerance

---

# 🧹 Cleanup

Delete resources in the following order:

1. Terminate EC2 Instances
2. Delete Transit Gateway Attachments
3. Delete Transit Gateway
4. Delete Route Tables
5. Delete Internet Gateways
6. Delete Subnets
7. Delete VPCs

---

# 👨‍💻 Author

**Hardik Darji**

AWS | DevOps | Cloud Computing Enthusiast

---

⭐ If you found this project helpful, consider giving the repository a **Star**!
