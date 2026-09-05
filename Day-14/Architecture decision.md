# 🏗️ Architecture Decisions

## 1. Access-Pattern-First Data Modeling

**Decision:**

- Design the DynamoDB table based on the application's expected access patterns rather than following a traditional relational database design.

**Why:**

- DynamoDB is optimized for predictable and efficient access patterns. Defining partition keys, sort keys, and indexes according to application requirements helps avoid unnecessary scans and improves query performance.

---

## 2. Use Query Instead of Scan

**Decision:**

- Prefer DynamoDB `Query` operations whenever the required partition key is known.

**Why:**

- `Query` retrieves items from a specific partition, while `Scan` examines the table more broadly. Using Query-based access patterns generally reduces unnecessary read capacity consumption and improves application efficiency.

---

## 3. Global Secondary Index for Alternate Access

**Decision:**

- Use a Global Secondary Index (GSI) when the application needs to query data using an alternative partition key.

**Why:**

- The primary table should be optimized for its main access pattern. A GSI provides an additional access path without requiring the application to scan the entire table.

**Example:**

```text
Primary Table
     │
     ├── Customer ID → Customer Orders
     │
     └── GSI → Order ID → Specific Order
```
---
## 4. Local Secondary Index for Customer-Based Queries

Decision:

- Use a Local Secondary Index (LSI) when an alternate sort-key access pattern is required while retaining the same partition key.

Why:

- LSIs allow different sorting and querying options within the same partition. This is useful for retrieving customer-specific records based on attributes such as order status.

Example:

Customer ID

     │
     ▼
     
    LSI
    
     │
     ▼
     
Order Status

---

## 5. DynamoDB Streams for Change Events

Decision:

- Enable DynamoDB Streams to capture item-level changes from the table.

Why:

- Streams provide a reliable event source for changes such as:

- INSERT
- MODIFY
- REMOVE

This allows downstream components to react to database changes without tightly coupling additional processing to the main application workflow.

---

## 6. Lambda for Event-Driven Processing

Decision:

- Use AWS Lambda as the consumer for DynamoDB Stream events.

Why:

- Lambda provides a serverless event-processing layer that can automatically execute when DynamoDB changes occur.

This creates a loosely coupled architecture:

Application

    │
    ▼
DynamoDB

    │
    ▼
DynamoDB Stream

    │
    ▼
Lambda

    │
    ▼
Event Processing

This approach avoids requiring the application to perform every downstream operation synchronously.

---

## 7. TTL for Temporary Data

Decision:

- Use DynamoDB Time to Live (TTL) for records that do not need to remain permanently in the table.

Why:

- TTL allows DynamoDB to automatically expire eligible items based on a configured timestamp attribute.

Example:
- ExpiresAt

Typical use cases include:

- Temporary sessions
- Expiring tokens
- Temporary records
- Short-lived application data

This reduces the need for custom cleanup jobs.

---

## 8. Global Tables for Multi-Region Requirements

Decision:

- Evaluate DynamoDB Global Tables as a solution for multi-Region database requirements without deploying a replica as part of this lab.

Why:

- Global Tables are suitable when an application requires:

- Multi-Region availability
- Regional low-latency access
- Cross-Region replication
- Multi-Region write capabilities

A Global Table replica was not created because multi-Region deployment was outside the scope of Day 14.

---

## 9. DAX for DynamoDB Read Acceleration

Decision:

- Evaluate DynamoDB Accelerator (DAX) as an optional caching layer without deploying a DAX cluster.

Why:

- DAX is designed specifically for DynamoDB workloads that require very low-latency cached reads.

It can be considered when:

- Read traffic is high
- Data is accessed repeatedly
- Extremely low read latency is required
- Eventual consistency is acceptable

DAX should not be used as a replacement for proper DynamoDB data modeling.

---

## 10. ElastiCache for Application-Level Caching

Decision:

- Evaluate Amazon ElastiCache as a general-purpose caching solution without deploying a cache cluster.

Why:

- ElastiCache can support caching requirements beyond DynamoDB-specific read acceleration.

Potential use cases include:

- Session management
- Application caching
- Counters
- Rate limiting
- Leaderboards
- Pub/Sub workloads

The caching technology should be selected according to the application's requirements rather than introducing caching without a defined use case.

---

## 11. Least-Privilege IAM

Decision:

- Grant IAM permissions only to the AWS resources and actions required by the DynamoDB and Lambda workflow.

Why:

- Following the principle of least privilege reduces the potential impact of accidental or unauthorized actions.

Lambda should have only the permissions required to consume DynamoDB Stream records and perform its intended processing.

---

## 12. Event-Driven Architecture

Decision:

- Use DynamoDB Streams and Lambda to separate database transactions from downstream processing.

Why:

- An event-driven design reduces application coupling and allows additional processing to occur independently of the original database operation.

                ┌──────────────┐
                │ Application  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  DynamoDB    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │    Stream    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │    Lambda    │
                └──────────────┘

This architecture is suitable for asynchronous workloads such as notifications, auditing, analytics, and downstream data processing.

---

## 13. Separate Practical Resources from Conceptual Services

Decision:

- Deploy only the AWS services required for the Day 14 practical while evaluating additional services conceptually.

Why:

Not every architecture component needs to be deployed in every environment. Limiting resources keeps the lab cost-effective while still providing an understanding of where services such as Global Tables, DAX, and ElastiCache fit into production architectures.

- Deployed / Validated
- DynamoDB
- GSI
- LSI
- TTL
- DynamoDB Streams
- AWS Lambda
- IAM
- Test Data
- Evaluated Conceptually
- DynamoDB Global Tables
- DAX
- Amazon ElastiCache
  
---

## 14. Validate the Architecture Through Testing

Decision:

- Validate DynamoDB access patterns, Streams, TTL behavior, and Lambda processing instead of relying only on configuration.

Why:

- An architecture is not considered reliable simply because the required services have been configured.

Testing confirms that:

- DynamoDB queries return the expected records.
- GSI access patterns work correctly.
- LSI queries return the required data.
- Stream events are generated.
- Lambda processes stream events.
- TTL is configured correctly.
- Event-driven processing behaves as expected.

---

## 🎯 Architecture Principles

The Day 14 implementation follows these core principles:

- Design for access patterns
- Prefer Query over unnecessary Scan
- Use indexes for known alternate access patterns
- Use Streams for change-driven workflows
- Use Lambda for asynchronous processing
- Use TTL for temporary data
- Use Global Tables for multi-Region requirements
- Use DAX for DynamoDB-specific read acceleration
- Use ElastiCache for broader application caching
- Apply least-privilege IAM
= Deploy only required resources
- Test the architecture instead of assuming it works

Core Principle: Design the DynamoDB data model around how the application reads and writes data, then introduce indexes, Streams, TTL, caching, and multi-Region capabilities only when the workload requires them.
