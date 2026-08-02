# 🌐 AWS VPC Foundation – CIDR Planning, Public & Private Subnets, Route Tables, Internet Gateway & VPC Design Flow

> A comprehensive hands-on guide to understanding the fundamental building blocks of Amazon Virtual Private Cloud (VPC). This documentation explains how to design a secure and scalable VPC architecture using CIDR planning, public/private subnets, route tables, and an Internet Gateway.

---

# 📌 Project Objective

The objective of this documentation is to learn how Amazon VPC networking works by designing a basic network architecture from scratch.

You will learn:

- CIDR Block Planning
- Public and Private Subnets
- Route Tables
- Internet Gateway (IGW)
- End-to-End VPC Design Flow
- Best Practices for Network Design

---

# 🏗️ Architecture

![Architecture](architecture/architecture.png)

---
## Step 1 — Create Custom VPC

Create VPC :
![VPC](images/createvpc.jpg)

VPC name & IPv4 CIDR :
![VPC](images/vpcname.jpg)

VPC Created :
![VPC](images/vpccreated.jpg)

---
## Step 2 — Create Public Subnet

Public Subnet :
![VPC](images/createpublic1sub.jpg)


Enable Auto Assign Public IPv4 :
![VPC](images/editsubnet.jpg)

Public and Private Subnet :
![VPC](images/allsubnet.jpg)

---
## Step 3 — Create Internet Gateway

Create IGW :
![VPC](images/createigw.jpg)

IGW  Name:
![VPC](images/igwname.jpg)

Attach Internet Gateway :
![VPC](images/attachigw.jpg)

Attached IGW :
![VPC](images/attachedigw.jpg)

---
## Step 4 — Main Route Table

Create Main Route :
![VPC](images/publicroutename.jpg)

Set main route :
![VPC](images/setmain.jpg)


--- 
## Step 5 — Create Public Route Table

![VPC](images/publicroutename.jpg)

---
## Step 6 — Add Internet Route to public

![VPC](images/igwpublic.jpg)


---
## Step 7 — Associate Public Subnets

![VPC](images/savedpublicassociation.jpg)

---
## Step 8  — Create Private Route Table & Keep Local Route Only

![VPC](images/privatesubnet.jpg)

---
## Step 9 — Associate Private Subnets

![VPC](images/privatesubnetassociation.jpg)

---
## 





