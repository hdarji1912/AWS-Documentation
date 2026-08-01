# ☁️ AWS Organizations · OUs · SCP Guardrails · IAM Identity Center · Cross-Account Access Lab

Hands-on AWS Lab demonstrating enterprise multi-account management using AWS Organizations, Organizational Units (OUs), Service Control Policies (SCPs), IAM Identity Center (AWS SSO), Cross-Account Access, and Consolidated Billing.

---

## 📚 Topics Covered

- 🏢 AWS Organizations
- 📂 Organizational Units (OUs)
- 🛡️ Service Control Policies (SCPs)
- 👥 AWS IAM Identity Center
- 🔐 AWS STS Temporary Credentials
- 🔄 Cross-Account Access
- 💳 Consolidated Billing
- 📊 AWS Cost Explorer
- 🚧 Security Guardrails

---

## 🎯 Learning Outcomes

After completing this lab, I gained hands-on experience with:

- Creating and managing AWS Organizations.
- Organizing multiple AWS accounts using Organizational Units (OUs).
- Implementing Service Control Policies (SCPs) to enforce security and governance.
- Configuring AWS IAM Identity Center for centralized user authentication and permission management.
- Using AWS Security Token Service (STS) to obtain temporary credentials.
- Setting up secure cross-account access using IAM roles.
- Understanding AWS Consolidated Billing for centralized cost management.
- Monitoring AWS spending and resource usage with AWS Cost Explorer.
- Applying security guardrails to maintain compliance across multiple AWS accounts.

---
## Step 1 – Understand the Problem

Imagine everyone works inside one AWS account.

One AWS Account :

- Developer
- Tester
- DevOps
- Security
- Finance
- Production

Problems:

- Developer accidentally deletes Production resources.
- Testing increases Production costs.
- Everyone receives Administrator permissions.
- Difficult auditing.
- Difficult billing.
- Difficult security.

This does not scale.

## 🏗️ Architecture

![Architecture](images/architecture.png)

---
## Step 2 – Create AWS Organization

Open: 
AWS Console

↓

AWS Organizations

Click :
Create Organization

![Architecture](images/awsaccount.jpg)

AWS creates :
Root

Hierarchy :
Root

---
## Step 3 – Create Organizational Units

Create : Dev-OU , Test-OU , Prod-OU

# AWS Organization Hierarchy

![Architecture](images/awsorganization.png)

----
## Step 4 – Create AWS Accounts

Inside Organizations

Create :  CloudAdhar-Dev

![Architecture](images/createawsaccount.jpg)

Move to : Dev-OU

![Architecture](images/account.png)






















## Dev-OU SCP Attached Policies.

![Architecture](images/devou.png)


## AWS Organizations  with SCP

![Architecture](images/scp.png)

---

## S3 Bucket Permisssion 

![Architecture](images/s3.png)



