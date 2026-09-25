## 🚀 AWS Day 17 — Event-Driven Architecture with SQS, SNS & EventBridge

---
## 📌 Project Overview

This project demonstrates AWS messaging, event-driven architecture, scheduling, and real-time streaming using Amazon SQS, SNS, EventBridge, Kinesis Data Streams, Data Firehose, and Amazon S3.

The project is implemented in:

```text
AWS Region: US East (Ohio)
Region Code: us-east-2
```
---
# ☁️ AWS Services Used

* Amazon SQS
* Amazon SNS
* Amazon EventBridge
* EventBridge Scheduler
* Amazon Kinesis Data Streams
* Amazon Data Firehose
* Amazon S3
* Amazon MQ — Review
* Amazon MSK — Review
---

# 🏗️ Architecture

![architecture](images/architecture1.png)

---

# 📋 Resource Names

| Resource         | Name                                         |
| ---------------- | -------------------------------------------- |
| SQS DLQ          | `aws-day17-orders-dlq`                       |
| Standard SQS     | `aws-day17-orders-standard`                  |
| FIFO SQS         | `aws-day17-orders-fifo.fifo`                 |
| Priority SQS     | `aws-day17-priority-orders`                  |
| SNS Topic        | `aws-day17-orders-topic`                     |
| EventBridge Bus  | `aws-day17-orders-bus`                       |
| EventBridge Rule | `aws-day17-high-value-orders-rule`           |
| Scheduler        | `aws-day17-payment-reminder`                 |
| Kinesis Stream   | `aws-day17-clickstream`                      |
| Firehose         | `aws-day17-clickstream-firehose`             |
| S3 Bucket        | `aws-day17-streaming-<ACCOUNT-ID>-us-east-2` |

> Replace `<ACCOUNT-ID>` with your AWS account ID when creating the S3 bucket.

---

# 📨 Part A — Amazon SQS

## 1. SQS Dead-Letter Queue

Created the Standard DLQ aws-day17-orders-dlq with 30-second visibility timeout, 14-day message retention, and SSE-SQS encryption.

![AWS](images/1.jpg)

---
# 2. Standard SQS Queue

Created aws-day17-orders-standard with a 30-second visibility timeout, 4-day message retention, 20-second long polling, and SSE-SQS encryption.

![AWS](images/2.jpg)

---
## 3. Standard Queue DLQ Configuration

Configured aws-day17-orders-standard to use aws-day17-orders-dlq as its Dead-Letter Queue, with a maximum receive count of 3.

![AWS](images/3.jpg)

---
## 4. SQS Visibility Timeout Test

Sent a test message and polled it without deleting it to demonstrate the visibility timeout. The message became in flight, remained temporarily invisible during the 30-second visibility timeout, and became visible again after the timeout expired.

![AWS](images/4.jpg)

![AWS](images/5.jpg)

![AWS](images/6.jpg)

![AWS](images/7.jpg)

---
## 5. SQS DLQ and Redrive

Repeatedly received the test message without deleting it, observed the receive count increase, verified that the message moved to the DLQ after exceeding the configured maximum receive count, and successfully redrove the message back to the source queue.

![AWS](images/8.jpg)

![AWS](images/9.jpg)

![AWS](images/10.jpg)

![AWS](images/11.jpg)

---
## 6. FIFO Queue Configuration

Created aws-day17-orders-fifo.fifo with FIFO ordering, 120-second visibility timeout, and content-based deduplication disabled.

![AWS](images/12.jpg)

---
## 7. FIFO Ordering Test

- Sent Payment received and Order shipped messages using the same Message Group ID (order-O-2001).
  
- The first poll received "Payment received" from the FIFO queue. While the message remained in flight, subsequent polling did not release "Order shipped".
  
- After the visibility timeout expired, the newly received Payment received message was successfully deleted using its current receipt handle.
  
- The next poll then released "Order shipped", confirming that FIFO ordering was maintained within the same message group.


![AWS](images/13.jpg)

![AWS](images/14.jpg)

![AWS](images/15.jpg)

![AWS](images/16.jpg)

---
## 8. Create the Priority Queue

Created the Standard priority queue aws-day17-priority-orders with a 30-second visibility timeout, 4-day message retention, 20-second receive message wait time, and SSE-SQS encryption. Added the project tag and created the queue.

![AWS](images/17.jpg)

---
## Part B — Amazon SNS

## 9. SNS Topic and Subscriptions

Created the SNS topic aws-day17-orders-topic and configured subscriptions for both the Standard orders queue and Priority orders queue.

![AWS](images/18.jpg)

---
## 10. SNS HIGH-Priority Filter

Configured the Priority queue subscription with a message attribute filter allowing only messages where priority = HIGH.

![AWS](images/19.jpg)

---
## 11. SNS Fanout and Filtering Test

Published NORMAL and HIGH priority orders to the SNS topic and verified that subscription filtering routed the messages to the expected SQS queues.

NORMAL order: Delivered to the Standard orders queue only.

![AWS](images/20.jpg)

![AWS](images/21.jpg)

![AWS](images/22.jpg)

![AWS](images/23.jpg)

![AWS](images/24.jpg)

![AWS](images/25.jpg)

---
### Part C — Amazon EventBridge

## 12. EventBridge Custom Event Bus

Created the custom EventBridge event bus aws-day17-orders-bus.

![AWS](images/26.jpg)

---
## 13. EventBridge High-Value Rule

Created aws-day17-high-value-orders-rule with an event pattern matching orders where the amount is greater than 5000.

![AWS](images/27.jpg)

![AWS](images/28.jpg)

![AWS](images/29.jpg)

![AWS](images/30.jpg)

---
## 14. EventBridge Negative Test

Sent an order event with an amount of 3000 and verified that it did not match the high-value order rule, so no message was delivered to the Priority queue.

![AWS](images/32.jpg)

---
## 15. EventBridge Positive Test

Sent an order event with amount 8500 and verified that it matched the rule and was successfully delivered to the Priority SQS queue.

![AWS](images/33.jpg)

---
## Part D — EventBridge Scheduler

## 16. EventBridge Scheduler

Created the one-time schedule aws-day17-payment-reminder with Amazon SQS as the target.

![AWS](images/34.jpg)

![AWS](images/35.jpg)

---
## 17. Scheduler to SQS Result

Verified that the scheduled payment reminder was successfully delivered to the Priority SQS queue.

![AWS](images/36.jpg)

![AWS](images/37.jpg)

---
## Part E — Kinesis Data Streams and Amazon Data Firehose

## 18. Kinesis Data Stream

Created aws-day17-clickstream using On-demand capacity mode with 1-day record retention.

![AWS](images/38.jpg)

---
## 19. Kinesis Data Viewer

Produced clickstream records and verified them using the Kinesis Data Viewer. Records using the same partition key were verified in the same shard.

![AWS](images/39.jpg)

![AWS](images/40.jpg)

![AWS](images/41.jpg)

![AWS](images/42.jpg)

---
## 20. Firehose to S3 Configuration

Created aws-day17-clickstream-firehose with Kinesis Data Streams as the source and Amazon S3 as the destination.

S3 bucket :
![AWS](images/43.jpg)

![AWS](images/44.jpg)

![AWS](images/45.jpg)

---
## 21. Complete Kinesis → Firehose → S3 Flow

Sent records to Kinesis, delivered them through Amazon Data Firehose, and verified that the records were successfully stored as objects in the private S3 bucket.

![AWS](images/46.jpg)

![AWS](images/47.jpg)

![AWS](images/48.jpg)

---
## Part F - Amazon MQ 

- Amazon MQ is included as a messaging technology review.

- No broker creation is required for this project.

- Amazon MQ is useful for applications that use traditional message brokers and messaging protocols.

For this project:

```text
Amazon MQ → Review only
```

---

# Part G — Amazon MSK

- Amazon MSK is included as a streaming technology review.

- No MSK cluster creation is required for this project.

- Amazon MSK provides managed Apache Kafka infrastructure for streaming workloads.

For this project:

```text
Amazon MSK → Review only
```
---

---

# 🧹 Cleanup

Delete the resources after completing the project to avoid unnecessary AWS charges.

## 1. Delete Firehose

```text
aws-day17-clickstream-firehose
```

---

## 2. Delete Kinesis Stream

```text
aws-day17-clickstream
```

---

## 3. Delete S3 Bucket

First delete all objects from:

```text
aws-day17-streaming-<ACCOUNT-ID>-us-east-2
```

Then delete the bucket.

---

## 4. Delete EventBridge Resources

Delete:

```text
aws-day17-high-value-orders-rule
```

Then delete:

```text
aws-day17-orders-bus
```

Delete the scheduler if it still exists:

```text
aws-day17-payment-reminder
```

---

## 5. Delete SNS

Delete the SNS subscriptions first.

Then delete:

```text
aws-day17-orders-topic
```

---

## 6. Delete SQS Queues

Delete:

```text
aws-day17-orders-standard
aws-day17-orders-dlq
aws-day17-orders-fifo.fifo
aws-day17-priority-orders
```

---

## 7. Review IAM Roles

Check IAM for project-specific roles created for:

```text
EventBridge Scheduler
Amazon Data Firehose
```

Delete unused roles after confirming they are not required by another resource.

---

# 🎯 What I Learned

Through this project, I practiced:

* Creating Amazon SQS queues
* Implementing Dead Letter Queues
* Understanding SQS visibility timeout
* Using SQS long polling
* Working with FIFO queues
* Maintaining FIFO message ordering
* Creating SNS topics
* Implementing SNS fanout
* Filtering SNS messages
* Creating custom EventBridge event buses
* Creating EventBridge rules
* Using event patterns
* Routing high-value events to SQS
* Scheduling events with EventBridge Scheduler
* Creating Kinesis Data Streams
* Producing Kinesis records using AWS CLI
* Creating Amazon Data Firehose delivery streams
* Delivering streaming data to Amazon S3
* Understanding Amazon MQ
* Understanding Amazon MSK
* Building event-driven AWS architectures
* Building real-time streaming pipelines

---
---

## 👨‍💻 Author

**Hardik Darji**

---
### ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
