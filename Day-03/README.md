# 🔐 AWS IAM Trust Policy & Permission Policy with STS AssumeRole

Learn the difference between IAM Trust Policy and Permission Policy by performing a complete hands-on lab using AWS Security Token Service (STS) AssumeRole.
---
This lab demonstrates how an IAM User can securely assume an IAM Role to obtain temporary credentials and access AWS resources following the Principle of Least Privilege (PoLP).
---

# 🎯 Lab Objectives

After completing this lab, you will understand how to:

Create IAM Users and IAM Roles
Configure Trust Policies
Configure Permission Policies
Generate temporary credentials using AWS STS
Assume an IAM Role
Access Amazon S3 using temporary credentials
Understand the complete AssumeRole workflow
---

# 📌 Introduction

AWS Identity and Access Management (IAM) provides secure access to AWS resources.

One of the most important concepts in IAM is understanding the difference between:

Trust Policy
Permission Policy

These two policies work together when an IAM Role is assumed using AWS Security Token Service (STS).

In this hands-on lab, you'll configure both policies from scratch and use temporary credentials to securely access an Amazon S3 bucket.

---
# 🏗️ Architecture

![Architecture](images/architecture1.png)


