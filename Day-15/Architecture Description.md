## 🏗️ Architecture Description

This infrastructure deployment represents a **secure and highly available AWS architecture** combining global content delivery, edge protection, private content storage, and multi-region application failover.
---

### 1. DNS Management Tier

**Amazon Route 53** manages the public hosted zone for `hdarji.dpnds.org`. It handles DNS resolution for the application and CloudFront endpoints using appropriate routing records.

### 2. Edge Security Layer

Incoming HTTPS traffic is inspected by **AWS WAF** at the CloudFront edge. WAF evaluates requests using configured security rules, including IP-based testing rules.

### 3. SSL/TLS Certificate Layer

An **AWS Certificate Manager (ACM)** public certificate is provisioned in **`us-east-2`** and associated with CloudFront to provide secure HTTPS access for `cdn.hdarji.dpnds.org`.

### 4. CloudFront Content Delivery

**Amazon CloudFront** provides global content delivery and caching for the private S3 origin.

* **Default Behavior (`*`)** – Uses the `CachingOptimized` policy for cached content delivery.
* **Private Behavior (`private/*`)** – Uses a **Trusted Key Group** to validate signed URLs before allowing access.

### 5. Origin Access Control

**CloudFront Origin Access Control (OAC)** securely connects CloudFront to the private S3 bucket using **AWS Signature Version 4 (SigV4)**.

### 6. Private Storage Layer

The **Amazon S3 bucket** is configured with:

* **Block Public Access** enabled
* **Default encryption** enabled
* **Versioning** enabled
* **Static website hosting disabled**
* Bucket policy restricted to the authorized CloudFront OAC

Direct S3 object access is denied, while authorized content is delivered through CloudFront.

### 7. Multi-Region Failover Layer

**Route 53 health checks and failover routing** connect two regional EC2 web endpoints:

* **Primary:** Ohio (`us-east-2`)
* **Secondary:** N. California (`us-west-1`)

If the primary endpoint becomes unhealthy, Route 53 redirects DNS traffic to the secondary endpoint. When the primary recovers, traffic can automatically return to the primary region.

### 8. Overall Data Flow

**CDN Flow:**
Viewer → Route 53 → HTTPS / ACM → AWS WAF → CloudFront → Trusted Key Group → OAC / SigV4 → Private S3

**Failover Flow:**
Client → Route 53 → Health Check → Ohio Primary EC2 → N. California Secondary EC2
