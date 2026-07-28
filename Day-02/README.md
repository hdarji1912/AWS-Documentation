# 🔐 AWS IAM – Users, Groups, JSON Policies, Least Privilege & Permission Boundaries

---

# 📖 Overview

Amazon Web Services (AWS) Identity and Access Management (IAM) enables secure authentication and authorization for users, groups, applications, and AWS services.

This repository demonstrates the practical implementation of AWS IAM concepts through hands-on labs, including creating users and groups, designing custom JSON policies, enforcing the Principle of Least Privilege, implementing Permission Boundaries, and validating permissions using the IAM Policy Simulator.

The primary objective of this project is to understand how AWS securely manages identities and controls access to cloud resources using industry-standard security practices.

---

# 🎯 Learning Objectives

By completing this project, you will learn how to:

- Create IAM Users
- Create IAM Groups
- Assign users to groups
- Enable AWS Management Console access
- Create custom IAM JSON policies
- Attach policies to users and groups
- Understand IAM policy structure
- Apply the Principle of Least Privilege
- Implement Permission Boundaries
- Test permissions using different IAM users
- Validate permissions using IAM Policy Simulator
- Follow AWS Security Best Practices

---

# 🏗️ Project Architecture

```text
AWS Account
│
├── IAM Users
│      ├── DEV
│      ├── Tester
│
├── IAM Groups
│      ├── Developers
│  
│
├── Custom Policies
│      ├── S3 policy
│      ├── EC2 Start/Stop policy
│      ├── Deny IAM
│      └── Permission Boundary
│
└── AWS Resources
       ├── Amazon S3
       └── IAM
```

---

# 📂 Project Workflow

```
Create IAM Groups
        │
        ▼
Create IAM Users
        │
        ▼
Assign Users to Groups
        │
        ▼
Enable Console Access
        │
        ▼
Create JSON Policies
        │
        ▼
Attach Policies
        │
        ▼
Test User Permissions
        │
        ▼
Apply Least Privilege
        │
        ▼
Configure Permission Boundary
        │
        ▼
Validate Using Policy Simulator
```

---

# 📸 Step 1 — AWS IAM Dashboard

Navigate to the AWS Management Console and open the IAM service.

Console :
![IAM](images/console.jpg)

IAM Dashboard :
![IAM](images/iamdashboard.jpg)


---

# 👥 Step 2 — Create IAM Groups

These groups simplify permission management by assigning policies to groups instead of individual users.

![IAM group](images/iamgroup.jpg)

Create groups:

- Developers

![IAM group](images/groupname.jpg)

---

# 👤 Step 3 — Create IAM Users

![User](images/createuser.jpg)

Create the following IAM users.

| User | Group |
|-------|--------|
| DEV | Developers |

![username](images/username.jpg)

Permission to user :

![username](images/permissionsuer.jpg)

Review user :
![review](images/reviewuser.jpg)

User created :

![user created](images/usercreate.jpg)

---

# 🔑 Step 4 — Enable AWS Console Access

Enable Management Console access for each IAM user and generate a temporary password.

Users will be prompted to change the password during their first login.

![console](images/devsign.jpg)

---

# 📜 Step 5 — Create Custom JSON Policy

Policy Dashboard :
![policy](images/createpolicy.jpg)

Create a customer-managed IAM policy using JSON.

![Policy created](images/policyedit.jpg)

Example:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        }
    ]
}
```
Review Policy :
![policy](images/policyreview.jpg)

Policy created :
![policy](images/policycreated.jpg)


---

# 🧩 Understanding IAM Policy Structure

Every IAM policy contains the following components.

| Component | Description |
|------------|-------------|
| Version | IAM policy language version |
| Statement | Collection of permissions |
| Effect | Allow or Deny |
| Action | AWS API operations |
| Resource | AWS resources |
| Condition | Optional access conditions |

---

# 🔗 Step 6 — Attach Policy to IAM Group

Attach the custom IAM policy to the Developers group.
All users belonging to the Developers group automatically inherit these permissions.

Add Permission for Policy :
![policy](images/addpermission.jpg)

Attach Policy :
![policy](images/attachpolicy.jpg)

Attached Policy Check :
![policy](images/policyattached.jpg)

---
# Step -7 login test 

Loign through IAM User -- DEV :
![Signin](images/devsign.jpg)

Go to S3 Bucket and check access :
![S3](images/s3access.jpg)

Go to VPC and check access or not access :
![vpc](images/vpcnotaccess.jpg)

---
---

# 🛡️ Step 8 — Principle of Least Privilege

The Principle of Least Privilege (PoLP) ensures that users receive only the permissions required to perform their specific job responsibilities.

## Allowed

- View S3 Buckets
- Start EC2 Instances
- Stop EC2 Instances

## Denied

- Delete S3 Buckets
- Terminate EC2 Instances
- Create IAM Users
- Delete IAM Policies

---

# 🚫 Step 9 — Explicit Deny Policy

Create a policy that explicitly denies IAM access.

Example:

```json
{
    "Version":"2012-10-17",
    "Statement":[
        {
            "Effect":"Deny",
            "Action":"iam:*",
            "Resource":"*"
        }
    ]
}
```

In AWS, an explicit **Deny** always overrides an **Allow**.


---

# 🔒 Step 10 — Permission Boundaries

Permission Boundaries define the **maximum permissions** an IAM user or role can receive.

Even if additional policies are attached later, the effective permissions cannot exceed the configured boundary.


---

# 🧪 Step 11 — IAM Policy Simulator

Use the IAM Policy Simulator to validate whether specific actions are allowed or denied before deploying changes.

Test actions such as:

- Start EC2 Instance
- Stop EC2 Instance
- Create S3 Bucket
- Delete S3 Bucket
- Create IAM User

---

# 📊 Permission Evaluation Flow

```
User Request
      │
      ▼
Authentication
      │
      ▼
Identity Policy
      │
      ▼
Permission Boundary
      │
      ▼
AWS Evaluation
      │
      ├── Allow ✅
      └── Deny ❌
```

---

# 🛠️ Technologies Used

- Amazon Web Services (AWS)
- AWS IAM
- JSON Policies
- AWS Management Console
- IAM Policy Simulator
- Git
- GitHub

---

---

# 💡 AWS Security Best Practices

- Always enable MFA for privileged accounts.
- Never use the root account for daily operations.
- Grant only the permissions required for a specific role.
- Assign permissions using IAM Groups instead of individual users.
- Prefer Customer Managed Policies over Inline Policies.
- Use Permission Boundaries for delegated administration.
- Rotate credentials regularly.
- Remove unused IAM users and access keys.
- Review permissions periodically.
- Validate permissions using the IAM Policy Simulator before deployment.

---

# 🎯 Skills Demonstrated

- AWS Identity and Access Management (IAM)
- Authentication & Authorization
- IAM Users & Groups
- Customer Managed Policies
- JSON Policy Creation
- Permission Boundaries
- Principle of Least Privilege
- AWS Security Best Practices
- Access Control
- Cloud Security Fundamentals

---

# 📚 Key Takeaways

✅ Created IAM Users and Groups

✅ Managed permissions using Groups

✅ Created Custom JSON Policies

✅ Implemented Least Privilege

✅ Configured Permission Boundaries

✅ Tested IAM Permissions

✅ Used IAM Policy Simulator

✅ Followed AWS Security Best Practices

---

# ⭐ Support

If you found this repository helpful, consider giving it a **Star ⭐**.

It motivates me to continue documenting my AWS & DevOps learning journey and sharing practical cloud projects with the community.

---
**Author:** Hardik Darji  
**Role:** DevOps Engineer 🚀
