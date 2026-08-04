# 🧹 Cleanup Guide

## 📌 Objective

This guide explains how to safely delete all AWS resources created during the **Amazon VPC Part 1** hands-on lab.

Deleting resources after completing the lab helps:

- Prevent unnecessary AWS charges
- Keep your AWS account organized
- Avoid reaching AWS service limits
- Prepare for future networking labs

---

# ⚠️ Important

AWS resources have dependencies. Always delete resources in the correct order to avoid errors such as:

- DependencyViolation
- Resource is in use
- Cannot delete attached resource

---

# 🗑️ Resources to Delete

The following resources were created during this lab:

| Resource Type | Resource Name |
|---------------|---------------|
| VPC | `devops-vpc` |
| Internet Gateway | `devops-igw` |
| Public Route Table | `public-rt` |
| Private Route Table | `private-rt` |
| Main Route Table | `main-rt-local` |
| Public Subnet A | `public-subnet-1a` |
| Private Subnet A | `private-subnet-1a` |
| Public Subnet B | `public-subnet-1b` |
| Private Subnet B | `private-subnet-1b` |

---

# Step 1 — Remove Route Table Associations

Navigate to:

```text
AWS Console
→ VPC
→ Route Tables
```

### Public Route Table

1. Select **public-rt**
2. Open the **Subnet Associations** tab.
3. Click **Edit subnet associations**.
4. Uncheck:
   - public-subnet-1a
   - public-subnet-1b
5. Save changes.

### Private Route Table

1. Select **private-rt**
2. Open the **Subnet Associations** tab.
3. Click **Edit subnet associations**.
4. Uncheck:
   - private-subnet-1a
   - private-subnet-1b
5. Save changes.

---

# Step 2 — Delete Custom Route Tables

Navigate to:

```text
VPC
→ Route Tables
```

Delete the following route tables:

- `public-rt`
- `private-rt`

> **Note:** The **main-rt-local** (Main Route Table) is automatically deleted when the VPC is deleted and cannot be deleted separately.

---

# Step 3 — Delete Subnets

Navigate to:

```text
VPC
→ Subnets
```

Delete the following subnets:

- `public-subnet-1a`
- `private-subnet-1a`
- `public-subnet-1b`
- `private-subnet-1b`

Verify that all four subnets have been removed.

---

# Step 4 — Detach Internet Gateway

Navigate to:

```text
VPC
→ Internet Gateways
```

Select:

```text
devops-igw
```

Choose:

```text
Actions
→ Detach Internet Gateway
```

Select the VPC:

```text
devops-vpc
```

Confirm the detachment.

---

# Step 5 — Delete Internet Gateway

After detaching the Internet Gateway:

1. Select **devops-igw**
2. Click **Actions**
3. Choose **Delete Internet Gateway**
4. Confirm deletion.

---

# Step 6 — Delete VPC

Navigate to:

```text
VPC
→ Your VPCs
```

Select:

```text
devops-vpc
```

Click:

```text
Actions
→ Delete VPC
```

Confirm the deletion.

---

# ✅ Cleanup Verification

Ensure the following resources no longer exist:

| Resource | Status |
|----------|--------|
| VPC | ✅ Deleted |
| Internet Gateway | ✅ Deleted |
| Public Route Table | ✅ Deleted |
| Private Route Table | ✅ Deleted |
| Public Subnet A | ✅ Deleted |
| Private Subnet A | ✅ Deleted |
| Public Subnet B | ✅ Deleted |
| Private Subnet B | ✅ Deleted |

---

# 📋 Cleanup Order

```text
1. Remove Route Table Associations
        ↓
2. Delete public-rt
        ↓
3. Delete private-rt
        ↓
4. Delete public-subnet-1a
        ↓
5. Delete private-subnet-1a
        ↓
6. Delete public-subnet-1b
        ↓
7. Delete private-subnet-1b
        ↓
8. Detach devops-igw
        ↓
9. Delete devops-igw
        ↓
10. Delete devops-vpc
```

---

# 🎯 Result

All networking resources created during this Amazon VPC Part 1 lab have been successfully removed. Your AWS account is now clean and ready for the next hands-on exercise.
