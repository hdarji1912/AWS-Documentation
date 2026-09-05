#  Day 13 – Amazon RDS, Aurora Serverless v2, Recovery & RDS Proxy

## Architecture Design Decisions

### 1. Isolated Database Layer

**Design Choice**

Place Amazon RDS and Aurora resources inside dedicated private database subnets distributed across multiple Availability Zones.

**Rationale**

The database layer should remain isolated from direct internet access. A dedicated database tier creates stronger network separation between the internet-facing, application, and data layers.

---

###  2. Multi-AZ Database Networking

**Design Choice**

Create the RDS DB subnet group using private subnets located in at least two Availability Zones.

**Rationale**

RDS requires a DB subnet group to contain subnets across multiple Availability Zones. This design also provides the network foundation needed for highly available database deployments.

---

### 3. Application-to-Database Trust

**Design Choice**

Configure database security-group rules to accept connections from the application security group instead of allowing the complete VPC CIDR.

**Rationale**

Referencing the application security group provides a more controlled trust relationship. Only workloads associated with the approved application security group can reach the database.

---

###  4. No Public Database Endpoint

**Design Choice**

Configure RDS as a private database and test access through an authorized workload inside the VPC.

**Rationale**

There is no requirement for direct internet access to the database. Keeping the database private limits exposure and ensures database communication remains within the AWS network.

---

###  5. Recovery Point Validation

**Design Choice**

Test both manual snapshots and Point-in-Time Recovery instead of relying only on automated backups.

**Rationale**

Different recovery mechanisms serve different operational requirements. Snapshots provide specific recovery points, while PITR allows restoration to a selected point within the configured backup retention window.

---

###  6. Read Scaling with Replica

**Design Choice**

Create an RDS Read Replica and validate replication from the primary database.

**Rationale**

Read Replicas provide an additional endpoint for read workloads and can help reduce read pressure on the primary database. The replica model also demonstrates asynchronous database replication.

---

###  7. Aurora Serverless v2 Capacity Model

**Design Choice**

Deploy an Aurora Serverless v2 cluster with a reader instance and test its failover capabilities.

**Rationale**

Aurora Serverless v2 is designed to dynamically adjust database compute capacity based on workload requirements. Combining a writer and reader provides an opportunity to validate both scaling and availability behavior.

---

###  8. Database Connection Management

**Design Choice**

Introduce RDS Proxy between the application and the Aurora database cluster.

**Rationale**

Applications can create a large number of database connections, especially during traffic spikes. RDS Proxy provides connection pooling and a managed connection layer that can help reduce connection overhead and improve application behavior during database events.

---

###  9. Logical Backup Strategy

**Design Choice**

Implement a logical database export and restore process alongside RDS-native backup mechanisms.

**Rationale**

Snapshots and PITR operate at the managed database infrastructure level, while logical backups provide database-level recovery. Maintaining both approaches creates additional recovery flexibility.

---

### 10. Recovery as a Testable Process

**Design Choice**

Validate recovery, replication, and failover procedures through hands-on testing.

**Rationale**

Having a backup configuration does not automatically guarantee a successful recovery. Testing restores, PITR, replicas, Aurora failover, Proxy connectivity, and logical backups confirms that the recovery strategy works in practice.

---

## 🏗️ Overall Architecture Principles

| Area | Design Approach |
|------|-----------------|
| Network | Private database subnets |
| Availability | Multiple Availability Zones |
| Security | Security-group based access |
| Connectivity | Private database access |
| Backup | Snapshots + PITR |
| Read Scaling | RDS Read Replica |
| Database Engine | Aurora Serverless v2 |
| Connections | RDS Proxy |
| Recovery | Native + logical backups |
| Validation | Recovery and failover testing |

---

## 🎯 Key Takeaways

- Keep database resources **private and isolated**.
- Use **multiple Availability Zones** for database networking.
- Allow database access only from **trusted application workloads**.
- Use **snapshots and PITR** for recovery flexibility.
- Use **Read Replicas** for read-heavy workloads.
- Use **Aurora Serverless v2** when dynamic capacity is required.
- Use **RDS Proxy** to manage application database connections.
- Maintain both **native and logical backup strategies**.
- Always **test recovery and failover**, rather than assuming they will work.
