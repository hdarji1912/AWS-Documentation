## Day - 10 :  Enterprise Blue-Green Deployment on AWS using Application Load Balancer

Production-style AWS DevOps project implementing a highly available Blue-Green deployment architecture using Application Load Balancer, Target Groups, private EC2 instances  and  health checks.

---
## 📌 Project Overview

This project demonstrates an enterprise-style Blue-Green deployment strategy on AWS.

The architecture maintains two independent application environments:

- 🔵 Blue Environment — Current production version
- 🟢 Green Environment — New application version prepared for release

Application traffic is managed through an Application Load Balancer (ALB). This allows the new version to be validated before directing production traffic to it.

The design focuses on:

- High availability
- Zero/minimal downtime deployments
- Automated health checks
- Controlled traffic switching
- Fault tolerance across Availability Zones
- Secure private application infrastructure
- Easy rollback

---
## 🏗️ Architecture

![ Architecture ](images/architecture.png)

---
## 1. Create VPC

![ VPC ](images/1.jpg)

---
## 2. Create Internet Gateway and Attach to VPC

![ VPC ](images/2.jpg)

---
## 3. Create Public and Private Subnet

![ VPC ](images/3.jpg)

---
## 4. Configure Public Route Tables and Associate Subnet

![ VPC ](images/4.jpg)

---
## 5. Configure NAT Gateway and Allocate EIP

![ VPC ](images/5.jpg)

---
## 6 . Configure Private Route Tables and Associate Subnet

![ VPC ](images/6.jpg)

---
## 7. Create IAM Role 

![ VPC ](images/7.jpg)

---
## 8. Create Security Groups 

For Application load balancer :

![ VPC ](images/8.jpg)

For web server :
![ VPC ](images/10.jpg)

---
## 9. Launch Blue EC2 server 

![ VPC ](images/11.jpg)

---
## 10. Launch Green EC2 server 

![ VPC ](images/12.jpg)

---
## 11. Connect Blue EC2 session manager

![ VPC ](images/13.jpg)

---
## 12. Check Nginx Status  For Blue EC2 server

![ VPC ](images/14.jpg)

---
## 13. Connect Green EC2 session manager

![ VPC ](images/15.jpg)

---
## 14. Check Nginx Status For Green EC2 seerver

![ VPC ](images/16.jpg)

---
## 15. Create Blue Target Group

![ VPC ](images/17.jpg)

---
## 16. Create Green Target Group

![ VPC ](images/18.jpg)

---
## 17. Create Application Load Balancer

![ VPC ](images/19.jpg)

---
## 18. Validate Blue Environment

![ VPC ](images/20.jpg)

---
## 19. Validate Green Environment

![ VPC ](images/21.png)

---
## 🎯 Key DevOps Concepts Demonstrated

This project demonstrates practical understanding of:

- AWS VPC architecture
- Public vs Private Subnets
- Multi-AZ architecture
- Application Load Balancing
- Target Groups
- Blue-Green Deployment
- Target Tracking
- Health Checks
- High Availability
- Fault Tolerance
- Zero/Minimal Downtime Deployment
  
---
## 👨‍💻 Author

Hardik Darji

DevOps Engineer

---

## ⭐ Support

If this project helped you understand AWS Blue-Green deployment and enterprise traffic management, consider giving the repository a ⭐.

Built for hands-on DevOps learning and real-world cloud architecture practice.
        
