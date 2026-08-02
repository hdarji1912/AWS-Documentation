## CIDR Plan

This document outlines the IPv4 addressing scheme used for the **AWS Two-Tier VPC Architecture**.

---

# 🌐 VPC CIDR

| Resource | CIDR Block | Total IPv4 Addresses | Usable IPv4 Addresses |
|----------|------------|---------------------:|----------------------:|
| devops-vpc | 10.0.0.0/16 | 65,536 | 65,531 |

> **Note:** AWS reserves **5 IPv4 addresses** in every subnet. Therefore, a `/16` network provides **65,531 usable IPv4 addresses**.

---

# 🏗️ Subnet CIDRs

| Subnet Name | Availability Zone | CIDR Block | Total IPv4 Addresses | Usable IPv4 Addresses |
|-------------|-------------------|------------|---------------------:|----------------------:|
| Public Subnet 1 | us-east-2a | 10.0.1.0/24 | 256 | 251 |
| Private Subnet 1 | us-east-2a | 10.0.11.0/24 | 256 | 251 |
| Public Subnet 2 | us-east-2b | 10.0.2.0/24 | 256 | 251 |
| Private Subnet 2 | us-east-2b |10.0.12.0/24 | 256 | 251 |

---

# 📌 AWS Reserved IPv4 Addresses

AWS automatically reserves **five IPv4 addresses** in every subnet.

| Address | Purpose |
|---------|---------|
| x.x.x.0 | Network Address |
| x.x.x.1 | VPC Router |
| x.x.x.2 | Amazon Provided DNS |
| x.x.x.3 | Reserved for Future Use |
| x.x.x.255 | Network Broadcast Address *(Broadcast traffic is not supported in AWS VPC)* |

---

# 📍 Example: Public Subnet A (10.10.1.0/24)

| Address | Purpose |
|---------|---------|
| 10.10.1.0 | Network Address |
| 10.10.1.1 | VPC Router |
| 10.10.1.2 | Amazon DNS |
| 10.10.1.3 | Reserved |
| 10.10.1.255 | Broadcast Address *(Reserved by AWS)* |

---

# ✅ CIDR Validation

The network design has been validated with the following checks:

- ✅ VPC CIDR block: **10.0.0.0/16**
- ✅ All subnet CIDRs are contained within the VPC CIDR.
- ✅ No subnet CIDR blocks overlap.
- ✅ Each subnet uses a **/24** CIDR block.
- ✅ Each subnet provides **251 usable IPv4 addresses**.
- ✅ The VPC provides **65,531 usable IPv4 addresses**.
- ✅ Public and Private subnets are distributed across two Availability Zones.
- ✅ The CIDR plan supports future subnet expansion without overlapping existing networks.

---

# 🧮 CIDR Calculation Formula

### Total IPv4 Addresses

```text
Total Addresses = 2^(32 − Prefix Length)
```

Example:

```text
/16 = 2^(32−16)
     = 65,536 Addresses
```

```text
/24 = 2^(32−24)
     = 256 Addresses
```

---

### Usable IPv4 Addresses in AWS

```text
Usable Addresses = Total Addresses − 5
```

Examples:

| CIDR | Total Addresses | AWS Reserved | Usable Addresses |
|------|----------------:|-------------:|-----------------:|
| /16 | 65,536 | 5 | 65,531 |
| /24 | 256 | 5 | 251 |

---
