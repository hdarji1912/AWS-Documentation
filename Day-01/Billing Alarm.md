# 💰 AWS Billing Alarm Setup with Amazon CloudWatch

> Learn how to configure an AWS Billing Alarm using Amazon CloudWatch and Amazon SNS to receive email notifications when your AWS estimated charges exceed a specified threshold.

![AWS](https://img.shields.io/badge/AWS-Billing%20Alarm-orange?style=for-the-badge&logo=amazonaws)
![CloudWatch](https://img.shields.io/badge/Amazon-CloudWatch-blue?style=for-the-badge&logo=amazonaws)
![SNS](https://img.shields.io/badge/Amazon-SNS-yellow?style=for-the-badge&logo=amazonaws)

---

# 📖 Overview

AWS Billing Alarm helps you monitor your AWS spending by sending email notifications whenever your estimated charges exceed a predefined threshold.

It is one of the first security and cost management best practices after creating an AWS account.

---

# 🎯 Objective

By completing this hands-on lab, you will learn how to:

- Enable CloudWatch Billing Metrics
- Create an Amazon SNS Topic
- Subscribe your email to SNS
- Create a CloudWatch Billing Alarm
- Receive email notifications when estimated charges exceed your configured threshold

---

# 🏗️ Architecture

```text
                  AWS Services
                       │
                       ▼
             Estimated AWS Charges
                       │
                       ▼
            Amazon CloudWatch Metric
                       │
                       ▼
              CloudWatch Billing Alarm
                       │
                       ▼
               Amazon SNS Topic
                       │
                       ▼
              Email Notification
```

---

# 🛠️ Prerequisites

- AWS Account
- Root User or IAM User with Billing permissions
- Verified Email Address
- Internet Connection

---

# Step 1 – Sign in to AWS Console

Log in to your AWS Account.

Search for:

```
Billing
```

Open:

```
Billing and Cost Management
```

---

# Step 2 – Enable CloudWatch Billing Alerts

From the left navigation panel:

```
Billing Preferences
```

Enable:

```
Receive CloudWatch Billing Alerts
```
![ Billing Preferences ](images/billingprefrence.jpg)

Click:

![ Billing Preferences ](images/billingprefrence1.jpg)

```
Save Preferences
```

> **Note:** This option only needs to be enabled once per AWS account.

---

# Step 3 – Open Amazon CloudWatch

Search:

```
CloudWatch
```

Navigate to:

```
CloudWatch
→ Alarms
→ Create Alarm
```

---

# Step 4 – Select Billing Metric

Click:

```
Select Metric
```

Select:

```
Billing
```

Choose:

```
Total Estimated Charge
```

Select Currency:

```
USD
```

Click:

```
Select Metric
```

---

# Step 5 – Configure Metric

Use the default settings:

| Setting | Value |
|----------|-------|
| Statistic | Maximum |
| Period | 6 Hours |

Click:

```
Next
```

---

# Step 6 – Configure Threshold

Choose:

```
Static
```

Condition:

```
Greater than
```

Threshold:

```
10
```

Meaning:

```
Estimated Charges > $10
```

Click:

```
Next
```

---

# Step 7 – Create SNS Notification

Select:

```
Create New Topic
```

Topic Name:

```
AWS-Billing-Alert
```

Email:

```
your-email@example.com
```

Click:

```
Create Topic
```

---

# Step 8 – Confirm Email Subscription

AWS will send a confirmation email.

Open your inbox.

Click:

```
Confirm Subscription
```

Without confirmation, notifications will not be delivered.

---

# Step 9 – Configure Alarm Details

Alarm Name:

```
AWS-Billing-Alarm
```

Description:

```
Alert when the estimated AWS charges exceed $10. Review the Billing Dashboard immediately and stop or terminate any unnecessary AWS resources to prevent additional costs.
```

Click:

```
Next
```

---

# Step 10 – Review and Create Alarm

Verify:

- Billing Metric
- Threshold
- SNS Topic
- Email Address
- Alarm Name

Click:

```
Create Alarm
```

---

# ✅ Expected Result

When your estimated AWS charges exceed **$10**, CloudWatch changes the alarm state to **ALARM** and Amazon SNS sends an email notification.

Example:

```
Subject:
AWS Billing Alert: Estimated Charges Exceeded $10

Message:

Your estimated AWS charges have exceeded the configured threshold of $10.

Recommended Actions

• Review your Billing Dashboard.
• Check running EC2 instances.
• Delete unused EBS volumes.
• Remove unused Elastic IPs.
• Delete idle Load Balancers.
• Delete unused NAT Gateways.
• Stop unnecessary RDS instances.

This notification is generated automatically by Amazon CloudWatch.
```

---

# 📊 Workflow

```text
AWS Resources Running
        │
        ▼
Estimated Charges Increase
        │
        ▼
CloudWatch Billing Metric
        │
        ▼
Billing Alarm Triggered
        │
        ▼
Amazon SNS
        │
        ▼
Email Notification
```

---

# 🔍 Verification

Go to:

```
CloudWatch
→ Alarms
```

Verify that your alarm status changes to:

- OK
- ALARM (when threshold is exceeded)

---

# 🛡️ Best Practices

- Enable billing alerts immediately after creating an AWS account.
- Use a low billing threshold (for example, $5 or $10).
- Confirm your SNS email subscription.
- Regularly monitor AWS Cost Explorer.
- Remove unused resources promptly.
- Enable AWS Budgets for monthly spending control.
- Review your Billing Dashboard frequently.

---

# ❗ Troubleshooting

## Billing metric is not visible

- Enable **Receive CloudWatch Billing Alerts**.
- Wait a few hours for billing metrics to become available.
- Ensure you are using the AWS Management (payer) account if your account is part of AWS Organizations.

---

## No email received

- Confirm your SNS subscription.
- Verify the email address.
- Check your Spam or Junk folder.

---

## Alarm stays in "Insufficient Data"

Billing metrics are updated periodically, not in real time.

Wait for AWS to publish the latest billing data.

---

# 📚 AWS Services Used

- AWS Billing and Cost Management
- Amazon CloudWatch
- Amazon Simple Notification Service (SNS)

---

# 💡 Key Learnings

- AWS Billing Metrics
- CloudWatch Alarms
- Amazon SNS Notifications
- Cost Monitoring
- Billing Best Practices
- Cloud Cost Optimisation

---

---

# 🧹 Cleanup

To avoid unnecessary resources:

1. Delete the CloudWatch Billing Alarm.
2. Delete the SNS Topic.
3. Remove the SNS Subscription (optional).

---

# 🎉 Conclusion

You have successfully configured an **AWS Billing Alarm** using **Amazon CloudWatch** and **Amazon SNS**. This setup helps you monitor AWS costs proactively by sending email notifications whenever your estimated charges exceed your configured threshold, allowing you to take immediate action and avoid unexpected expenses.

---

👨‍💻 Author

Hardik

DevOps Engineer| AWS Learner

## ⭐ If you found this project helpful, consider giving the repository a star!
