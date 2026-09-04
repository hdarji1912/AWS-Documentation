# AWS Day 14 — Serverless Orders Management with DynamoDB Streams

> A hands-on AWS serverless project demonstrating **DynamoDB access-pattern design, GSI, LSI, TTL, CRUD operations, DynamoDB Streams, AWS Lambda, CloudWatch Logs, and a temporary Orders Dashboard**.

---

## 📌 Project Overview

This project implements a serverless Orders Management application using AWS services.

The application demonstrates how to design a DynamoDB table around application access patterns and how database changes can automatically trigger downstream processing through DynamoDB Streams and AWS Lambda.

---

### 🏗️ Architecture Flow

![Architecture](images/architecture.png)

---

## 🎯 Project Objectives

The main objectives of this project are:

- Design a DynamoDB table using access patterns
- Create a composite primary key
- Create and use a Global Secondary Index
- Create and use a Local Secondary Index
- Perform DynamoDB GetItem
- Perform DynamoDB Query
- Perform DynamoDB Scan
- Implement CRUD operations
- Configure DynamoDB TTL
- Enable DynamoDB Streams
- Configure NEW_AND_OLD_IMAGES
- Create AWS Lambda functions
- Configure Lambda Function URL
- Connect DynamoDB Streams to Lambda
- Process INSERT, MODIFY, and REMOVE events
- Monitor Lambda execution using CloudWatch
- Build a temporary Orders Dashboard
- Validate the complete serverless event-driven architecture

---

## 1 . Select AWS Region

Login to the AWS Management Console.

Select:
```bash
US East (Ohio)
us-east-2
```

Make sure all resources are created in the same region.

---
## 2. Create DynamoDB Table

![Architecture](images/1.jpg)

---
## Global & local Secondary Index

![Architecture](images/2.jpg)

---
## 3. Enable DynamoDB Streams

![Architecture](images/3.jpg)

---
## 4. Enable DynamoDB TTL

![Architecture](images/4.jpg)

---
## 5. Create Customer and order data

![Architecture](images/5.jpg)

---
## 6. Customer GetItem

Use:

- PK = CUSTOMER#C101
- SK = PROFILE

![Architecture](images/6.jpg)

---
## 7. Customer Orders Query

Use the base table.

- Partition Key
PK = CUSTOMER#C101
- Sort Key Condition
begins_with(SK, "ORDER#")

![Architecture](images/7.jpg)

---
## 8. GSI1 Query

 Select:

- Index = GSI1

Query:

- GSI1PK = ORDER#O9003

![Architecture](images/8.jpg)

---
## 9. LSI1 Query

Select:
- Index = LSI1

Partition key:
- PK = CUSTOMER#C103
  
- Sort key condition:
begins_with(
    LSI1SK,
    "STATUS#SHIPPED#"
)

![Architecture](images/9.jpg)

---
## 10. Query vs Scan

Compared targeted Query and full-table Scan, showing lower read capacity for Query (0.5 RCU) than Scan (2.0 RCUs). This demonstrates why access-pattern-driven DynamoDB designs favor targeted Query operations over full-table Scan operations.

![Architecture](images/10.jpg)

For production applications, prefer targeted Query operations whenever possible.

---
## 11. CHECK TTL / Session Demonstration

Enabled DynamoDB TTL using the ExpiresAt attribute and created a session item with a future expiration timestamp.

![Architecture](images/11.jpg)

---
## 12. Create IAM Role for Lambda

![Architecture](images/12.jpg)

---
## 13. Create Stream Lambda + Trigger

Created a DynamoDB Stream consumer Lambda and connected it to the orders table stream. Verified that the event source mapping is enabled and active.

![Architecture](images/13.jpg)

![Architecture](images/14.jpg)

---
## 14. Modify Old/New Image and check to cloudwatch

Updated order O9002 from PAID to SHIPPED and verified the DynamoDB Stream Lambda received the MODIFY event with both the old and new images.

![Architecture](images/15.jpg)

Dynamodb table :
![Architecture](images/16.jpg)

Cloudwatch:
![Architecture](images/17.jpg)

---
## 15. Create IAM Role for oders access

![Architecture](images/18.jpg)

---
## 16. Create function for UI dashboard 

Go to:

- Lambda → Create function

Name:

- orders-day14-ui

Runtime:

- Python 3.12

Role:

- Day14Ordersaccess

Create.

---
## 17. Code 

> Use code that i have attached in application code in Day-14 github repo and Deploy the code .

---
## 18. Enable Lambda Function URL

Navigate to:

Lambda

    ↓
orders-api-day14

    ↓
Configuration

    ↓
Function URL

Click:

- Create function URL

For this temporary lab:

- Auth type = NONE

Create the Function URL.

You will receive a URL similar to:

- https://xxxxxxxx.lambda-url.us-east-2.on.aws/

---
## 19. UI Base Query

![Architecture](images/19.jpg)

---
## 20. Create UI LSI Query

UI performing a status filter query via LSI1.

![Architecture](images/20.jpg)

---
## 21. Create UI GSI Query

UI performing an order-ID search via GSI1.

![Architecture](images/21.jpg)

---
## 22. Update Status 

UI performing a status update via the API  from shipped to delivered.

![Architecture](images/22.jpg)

Cloudwatch:
![Architecture](images/23.jpg)

---
## 23. Initial State — UI Dashboard + DynamoDB 

Shows O9003 in the Orders Dashboard with status `PAID` and the corresponding DynamoDB item with `Status=PAID`  before the status update.

UI Dashboard:
![Architecture](images/24.jpg)

DynamoDB Table:
![Architecture](images/25.jpg)

---
## 24.  Event Source Mapping

Shows the DynamoDB Stream event source mapping for orders-stream-consumer-day14 with the mapping Enabled and the last processing result OK, confirming that the Stream-to-Lambda integration is active and processing events successfully.

Status : enabled

![Architecture](images/26.jpg)

---
## 25. UI — O9003 Status Update from PAID to SHIPPED

Shows O9003 being updated from PAID to SHIPPED through the application UI.

![Architecture](images/27.jpg)

---

## 26. DynamoDB — O9003 After Update

Shows the updated O9003 item in DynamoDB with Status=SHIPPED and LSI1SK=STATUS#SHIPPED#....

![Architecture](images/28.jpg)

---
## 27. CloudWatch — Stream Event

Shows the DynamoDB Stream MODIFY event processed by the consumer Lambda, with oldImage.Status=PAID changing to newImage.Status=SHIPPED for order O9003.

![Architecture](images/29.jpg)

---
## 28. UI — LSI1 and GSI1 Validation

Shows LSI1 being used with a status-prefix query to filter SHIPPED orders and GSI1 being used to search for order O9003.

![Architecture](images/30.jpg)

---
## 💡 Key Takeaways:
DynamoDB:
- DynamoDB designs should start with access patterns, not simply with a traditional relational-table mindset.

GSI:
- GSI provides an alternate partition/sort-key access pattern.

LSI:
- LSI provides an alternate sort key while keeping the same partition key.

Streams:
- DynamoDB Streams turn database changes into events:

- INSERT
- MODIFY
- REMOVE
  
Lambda:
- Lambda provides serverless processing for both API requests and asynchronous stream events.

CloudWatch:
- CloudWatch provides centralized Lambda execution and application logs.
  
---
## 🌐 Serverless Architecture

The project uses managed AWS services instead of traditional servers.

- No EC2
- No Application Server
- No Database Server
- Fully Managed AWS Services

This reduces infrastructure management and allows the application to scale automatically with demand.

---
## 🚀 Overall

The project demonstrates a fully serverless and event-driven architecture:

                         👤 User
                            │
                            ▼
                   📦 Orders Dashboard
                            │
                         HTTPS
                            │
                            ▼
                🔗 Lambda Function URL
                            │
                            ▼
                      ⚡ API Lambda
                            │
                            ▼
                   🗄️ DynamoDB Table
                            │
                  ┌─────────┴─────────┐
                  │                   │
             GSI1 / LSI1       DynamoDB Streams
                                      │
                                      ▼
                            ⚡ Stream Consumer
                                Lambda
                                      │
                                      ▼
                            📊 CloudWatch
                                Logs
                                
---

## 🧹 Cleanup

Perform cleanup only after capturing all required screenshots and evidence. The source documentation explicitly recommends completing evidence collection before cleanup.

Recommended cleanup order

1. Remove Lambda Function URL

2. Remove DynamoDB Stream
   event-source mapping

3. Delete Stream Consumer Lambda

4. Delete API Lambda

5. Delete Lambda IAM roles

6. Delete policies created
   specifically for this lab

7. Delete DynamoDB table

8. Verify TTL and Streams
   are removed with the table

9. Verify no Day-14 resources remain

---
## 👨‍💻 Author

Hardik Darji

Role: DevOps Engineer

---
## ⭐ Support This Project

If you found this project helpful or useful, please consider giving it a ⭐ **Star** on GitHub.

Your support motivates me to keep learning, building, and sharing more DevOps and AWS projects.

⭐ **Star this repository** and feel free to share it with others!
