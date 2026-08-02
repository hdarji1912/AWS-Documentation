## Architecture Decisions

---

## 🌐 Why Separate Public and Private Subnets?

The VPC is divided into **Public** and **Private** subnets to enhance security, scalability, and network organization.

- **Public Subnets** host internet-facing resources such as EC2 web servers, Application Load Balancers (ALB), or Bastion Hosts.
- **Private Subnets** host internal resources such as application servers, databases, and backend services that should not be directly accessible from the internet.

This separation follows the **Principle of Least Privilege (PoLP)** by exposing only the resources that require public access while keeping sensitive workloads protected.

---

##  Why Use Separate Route Tables?

Separate route tables provide different routing policies for public and private subnets.

### Public Route Table

| Destination | Target |
|-------------|--------|
| 10.10.0.0/16 | Local |
| 0.0.0.0/0 | Internet Gateway (IGW) |

This allows instances in public subnets to communicate with the internet.

### Private Route Table

| Destination | Target |
|-------------|--------|
| 10.10.0.0/16 | Local |

Since there is no default route to the Internet Gateway, resources inside private subnets remain isolated from direct internet access.

This design improves security while maintaining internal communication within the VPC.

---

##  Why Deploy Resources Across Two Availability Zones?

Resources are distributed across **two Availability Zones (AZs)** to improve application reliability and fault tolerance.

### Benefits

- High Availability (HA)
- Improved fault tolerance
- Better disaster recovery
- Reduced single point of failure
- Supports future Auto Scaling and Load Balancing architectures

If one Availability Zone experiences an outage, resources in the second Availability Zone can continue serving traffic.

---

##  Why Use a /16 VPC CIDR with /24 Subnets?

The VPC uses the CIDR block **10.10.0.0/16**, providing a large private IP address space.

Each subnet uses a **/24 CIDR**, offering **256 IP addresses (251 usable in AWS)**.

### Benefits

- Simple and organized subnet planning
- Plenty of room for future expansion
- Prevents overlapping CIDR ranges
- Supports additional public and private subnets
- Easier network management

This design follows AWS networking best practices for scalable environments.

---

##  Why Keep the Main Route Table Local-Only?

The **Main Route Table** is left with only the default local route.

| Destination | Target |
|-------------|--------|
| 10.10.0.0/16 | Local |

No public or private subnets are intentionally associated with the Main Route Table.

Instead:

- Public subnets use the **Public Route Table**
- Private subnets use the **Private Route Table**

Keeping the Main Route Table local-only makes the network easier to understand, avoids accidental routing changes, and improves operational clarity.

---

## 🔒 Security Design Summary

This architecture follows AWS networking best practices by:

- Separating internet-facing and internal resources.
- Using dedicated route tables for different traffic flows.
- Deploying resources across multiple Availability Zones.
- Designing scalable CIDR blocks for future growth.
- Keeping the Main Route Table minimal and using explicit subnet associations.
- Providing secure and predictable network routing.
