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

AWS Organization Hierarchy

![Architecture](images/awsorganization.png)

----
## Step 4 – Create AWS Accounts

Inside Organizations

Create :  CloudAdhar-Dev

![Architecture](images/createawsaccount.jpg)

Move to : Dev-OU

![Architecture](images/account.png)

---
## Step 5 – Understand the Management Account

The Management Account should not run workloads.

![Architecture](images/awsmanagementaccount.jpg)

It is only used for:

- AWS Organizations
- SCP Management
- Billing
- Cost Explorer
- Identity Center
- Central Governance

Never deploy production applications here.
---

## Step 6 – Enable IAM Identity Center

Go to :
IAM Identity Center

Click :
Enable

AWS creates :
Identity Store

↓

Access Portal

↓

Permission Set Service

# AWS Access Portal

![Architecture](images/accessportal.png)

---

## Step 7 – Login  

Open :

AWS Access Portal

Choose :

CloudAdhar-Dev

Click :

Management Console

Now you're inside the Dev account.

---

## Step 8 – Verify STS Session

Open CloudShell. 

Run
```bash
aws sts get-caller-identity
```

Example :
```json
{
 "Account":"123456789012",

 "Arn":"arn:aws:sts::123456789012:assumed-role/AWSReservedSSO_CloudAdhar-Admin_xxxxx/cloudadhar-demo"
}
```
![Architecture](images/devlogin.png)

Notice : assumed-role

That means you are not using long-term IAM user credentials.

You're using temporary STS credentials.

---
## Step 9 – Create an S3 Bucket without SCP

Generated a unique Amazon S3 bucket name and successfully created the bucket while the member account was under the Root of the AWS Organization.

Run in cloudshell: 
```bash
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

BUCKET="cloudadhar-before-scp-${ACCOUNT_ID}-$(date +%s)"

aws s3api create-bucket \
--bucket "$BUCKET" \
--region ap-south-1 \
--create-bucket-configuration LocationConstraint=ap-south-1
```
Result :

Bucket Created

Reason :

Permission Set

↓

AdministratorAccess

↓

No SCP

↓

Allowed

# S3 Bucket creted without SCP

![Architecture](images/cloudshell.png)

## Deleted the Test Bucket

```bash

aws s3api delete-bucket --bucket "$BUCKET" --region "$AWS_REGION"

aws s3api head-bucket --bucket "$BUCKET"
```
# S3 Bucket Deleted

![Architecture](images/s3cloudshell.png)

---
## Step 10 – Create an SCP

Management Account 

Go to

Organizations

↓

Policies

↓

Service Control Policies

create policy :

![Architecture](images/servicepolicy.jpg)

# Create New Policy :

![Architecture](images/createnewpolicy.jpg)

## Example :

```json
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"DenyS3BucketCreation",
      "Effect":"Deny",
      "Action":"s3:CreateBucket",
      "Resource":"*"
    }
  ]
}
```

## AWS Organizations  with SCP

![Architecture](images/scp.png)

---
