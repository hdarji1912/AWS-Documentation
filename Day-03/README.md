# 🔐 AWS IAM Trust Policy & Permission Policy with STS AssumeRole
Learn the difference between IAM Trust Policy and Permission Policy by performing a complete hands-on lab using AWS Security Token Service (STS) AssumeRole.

This lab demonstrates how an IAM User can securely assume an IAM Role to obtain temporary credentials and access AWS resources following the Principle of Least Privilege (PoLP).
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

---
# Hands-on Implementation

# Step 1 — Create an Amazon S3 Bucket

Navigate to :

AWS Console

↓

Amazon S3

↓

Create Bucket

![Bucket](images/bucketinitial.jpg)

Bucket Name :

![Bucket](images/bucketname.jpg)

Bucket Generated :

![Bucket](images/bucketgenerate.jpg)

Upload File to Bucket :

![Bucket](images/bucketupload.jpg)

File Inserting to Bucket :

![Bucket](images/bkfileupload.jpg)

File Uploading Pending to Bucket :

![Bucket](images/bkfileuploading.jpg)

File Uploaded Successfully in the Bucket :

![Bucket](images/bkfileuploaded.jpg)

---

# Step 2 — Create IAM User

Navigate to :
---
IAM

↓

Users

↓

Create User
---

IAM Dashboard :

![user](images/iamuser.jpg)

Create User :

![user](images/iamusercreate.jpg)

IAM User Name :

![user](images/username.jpg)

Created IAM user :

![user](images/iamusercreated.jpg)

--- 
 Do not attach any S3 permissions.
---
---

# Step 3 — Generate Access Keys

Open :

IAM

↓

developer

↓

Security Credentials

↓

Create Access Key

![Access key ](images/userkeyaccess.jpg)

Create Access Key :

![Access key ](images/accesskeycreate.jpg)

Access Key : 

![Access key ](images/accesskeygenerate.jpg)

# Best practice don't show access key . But I have hide my Secret key so no problem .

---
# Step 4 — Launch EC2 instance 

launch Instance :

![EC2 ](images/launche2.jpg)

Successfully Launch Instance :

![EC2 ](images/ec2launced.jpg)

EC2 connect to local via SSH :

![EC2 ](images/ec2connect.jpg)

Successfully SSH to local :

![EC2 ](images/sshtolocal.jpg)

---

# Step 5 — Configure AWS CLI

AWS CLI Download :

![AWS ](images/awscli.jpg)

# Verify 

aws sts get-caller-identity :

![AWS ](images/stscall.jpg)

---
# Step 6 — Verify User Has No S3 Access

Run -- aws s3 ls  

![AWS ](images/accessdenied.jpg)

# Expected  -- AccessDenied
This confirms that the IAM User has no direct S3 permissions.

---

# Step 7 — Create IAM Role

Navigate to :

IAM

↓

Roles

↓

Create Role

IAM Dashboard :

![IAM](images/iamdashboard.jpg)

Create Role :

![IAM](images/iamrole.jpg)

---
## Step 8 – Configure the Trust Policy

The **Trust Policy** defines **who is allowed to assume the IAM Role**.

Replace the default trust policy with the following JSON:

# Trust Policy :
![Trust Policy](images/roletrustpolicy.jpg)

### Example

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<ACCOUNT-ID>:user/developer"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

> **Replace** `<ACCOUNT-ID>` with your AWS Account ID.

---
# Step 9 — Attach Permission Policy

The **Permission Policy** defines **what actions the IAM Role is allowed to perform** after it has been assumed.

Attach the following inline policy to the IAM Role.

## Permission Policy

![Permission Policy](images/permissionpolicy.jpg)

### Example

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::my-demo-bucket-12345"
    },
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-demo-bucket-12345/*"
    }
  ]
}
```
---
# Step -10 Successfully Created Role

Created Role :

![IAM](images/rolecreated.jpg)

---
# Step 11 — Allow IAM User to Assume Role

Attach this policy to the developer IAM User:

![IAM](images/devinlinepolicy.jpg)

### Example

```json
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Action":"sts:AssumeRole",
      "Resource":"arn:aws:iam::<ACCOUNT-ID>:role/S3ReadOnlyRole"
    }
  ]
}
```
---
# Step 12 — Copy Role ARN

### Example

```bash
arn:aws:iam::123456789012:role/S3ReadOnlyRole

```
![IAM](images/arn.jpg)

---
# Step 13 — Assume the IAM Role Using AWS STS

Run the following AWS CLI command to assume the IAM Role and obtain temporary security credentials.

```bash
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/S3ReadOnlyRole \
  --role-session-name DemoSession
```

> **Replace** `123456789012` with your AWS Account ID and `S3ReadOnlyRole` with your IAM Role name.

### Expected Output

```json
{
  "Credentials": {
    "AccessKeyId": "ASIA****************",
    "SecretAccessKey": "********************************",
    "SessionToken": "********************************",
    "Expiration": "2026-07-31T12:30:00Z"
  },
  "AssumedRoleUser": {
    "Arn": "arn:aws:sts::123456789012:assumed-role/S3ReadOnlyRole/DemoSession"
  }
}
```

📷 ** Assume Role STS **

![IAM](images/assumerole.jpg)


```text
images/sts-assume-role-output.png
```
---
# Step 14 — Export Temporary Credentials

```bash
export AWS_ACCESS_KEY_ID=ASIA...

export AWS_SECRET_ACCESS_KEY=...

export AWS_SESSION_TOKEN=...
```
---
# Step 15 — Verify Assumed Identity

Verify 
```bash
aws sts get-caller-identity
```
![IAM](images/stscall.jpg)

Expected :
```json
{
"Arn":"arn:aws:sts::123456789012:assumed-role/S3ReadOnlyRole/DemoSession"
}
```
---
# Step 16 — Access the S3 Bucket

```bash
aws s3 ls s3://my-demo-bucket-12345
```
Expected :

```bash
hello.txt
```
---
# Step 17 — Download Object

![S3](images/awsa3download.jpg)
```bash
aws s3 cp s3://my-demo-bucket-12345/hello.txt .
```

View the file

```bash
cat hello.txt
```
---

# Step 18 — Verify Least Privilege

Attempt to upload a file.

```bash
aws s3 cp upload.txt s3://my-demo-bucket-12345/
```
![S3](images/polp.jpg)

Expected

```text
AccessDenied
```

This confirms that the role only has read permissions.

---

# 🔄 Complete STS AssumeRole Workflow

IAM User

     |
     ▼
     
Permission to call sts:AssumeRole

     │
     ▼
     
AWS STS

     │
     ▼
     
Checks Trust Policy

     │
     ▼
     
Issues Temporary Credentials

     │
     ▼
     
Permission Policy Evaluated

     │
     ▼
     
Access Amazon S3


---

# 🚨 Troubleshooting

| Error                            | Cause                               | Solution                                          |
| -------------------------------- | ----------------------------------- | ------------------------------------------------- |
| AccessDenied while assuming role | Missing `sts:AssumeRole` permission | Attach AssumeRole policy to IAM User              |
| AccessDenied after assuming role | Missing S3 permissions              | Verify Permission Policy                          |
| InvalidClientTokenId             | Invalid or expired credentials      | Reconfigure AWS CLI or export new STS credentials |
| ExpiredToken                     | Session expired                     | Run `aws sts assume-role` again                   |
| NoSuchBucket                     | Incorrect bucket name               | Verify bucket name and Region                     |

---

# 🎯 Key Takeaways

After completing this hands-on lab, you have successfully:

- ✅ Understood the difference between **IAM Trust Policies** and **IAM Permission Policies**.
- ✅ Learned how **AWS Security Token Service (STS)** generates temporary security credentials.
- ✅ Created an **IAM User** without direct access to Amazon S3.
- ✅ Created an **IAM Role** with a custom **Trust Policy**.
- ✅ Attached a **Permission Policy** to define the actions the IAM Role can perform.
- ✅ Granted the IAM User permission to assume the IAM Role using `sts:AssumeRole`.
- ✅ Assumed the IAM Role using the AWS CLI and received temporary STS credentials.
- ✅ Verified the assumed identity using the `aws sts get-caller-identity` command.
- ✅ Accessed an Amazon S3 bucket using temporary credentials instead of long-term access keys.
- ✅ Implemented the **Principle of Least Privilege (PoLP)** by allowing only the minimum required permissions.
- ✅ Gained practical experience with AWS IAM Roles, Trust Policies, Permission Policies, and STS AssumeRole.
- ✅ Built a real-world IAM authentication and authorization workflow commonly used in production AWS environments.

---

# 👨‍💻 Author

**Hardik Darji**
---

⭐ If you found this project helpful, consider giving this repository a star!





