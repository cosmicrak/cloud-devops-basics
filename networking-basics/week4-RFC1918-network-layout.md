\# Week 4 Day 28 - RFC1918 Private Network Layout



\## RFC1918 Private Ranges



| Range | CIDR | Use |

|---|---|---|

| 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 | Cloud/company networks |

| 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 | Enterprise private networks |

| 192.168.0.0 - 192.168.255.255 | 192.168.0.0/16 | Home/small office networks |



\## Parent VPC



VPC CIDR:

10.0.0.0/16



This gives the private range:

10.0.0.0 - 10.0.255.255



\## Availability Zone A



\### Public Subnet A

CIDR: 10.0.1.0/24  

Range: 10.0.1.0 - 10.0.1.255  

Usable: 10.0.1.1 - 10.0.1.254  

Purpose: load balancer, bastion, public-facing resources



\### Private App Subnet A

CIDR: 10.0.2.0/24  

Range: 10.0.2.0 - 10.0.2.255  

Usable: 10.0.2.1 - 10.0.2.254  

Purpose: backend application servers



\### Database Subnet A

CIDR: 10.0.3.0/24  

Range: 10.0.3.0 - 10.0.3.255  

Usable: 10.0.3.1 - 10.0.3.254  

Purpose: database resources, not public



\## Availability Zone B



\### Public Subnet B

CIDR: 10.0.11.0/24  

Range: 10.0.11.0 - 10.0.11.255  

Usable: 10.0.11.1 - 10.0.11.254  

Purpose: load balancer, bastion, public-facing resources



\### Private App Subnet B

CIDR: 10.0.12.0/24  

Range: 10.0.12.0 - 10.0.12.255  

Usable: 10.0.12.1 - 10.0.12.254  

Purpose: backend application servers



\### Database Subnet B

CIDR: 10.0.13.0/24  

Range: 10.0.13.0 - 10.0.13.255  

Usable: 10.0.13.1 - 10.0.13.254  

Purpose: database resources, not public



\## Management and Monitoring



\### Admin/Bastion Subnet

CIDR: 10.0.50.0/24  

Purpose: controlled admin access



\### Monitoring Subnet

CIDR: 10.0.60.0/24  

Purpose: logging, metrics, monitoring tools



\## Why This Layout Does Not Overlap



Each /24 subnet has a unique third octet:

1, 2, 3, 11, 12, 13, 50, 60



Because each /24 subnet covers only:

10.0.X.0 - 10.0.X.255



No two subnets use the same X value.



\## Public vs Private vs Database



Public subnet:

Can have route to Internet Gateway.



Private app subnet:

Should not be directly reachable from internet. It may use NAT Gateway for outbound updates.



Database subnet:

Should not be public. App servers should connect to it privately.



\## Cloud Support Troubleshooting Use



If an EC2 instance is unreachable, I first identify which subnet it belongs to.



Then I check:

1\. Is it public or private?

2\. Does the route table match its purpose?

3\. Does the subnet overlap another subnet?

4\. Does the security group allow required traffic?

5\. Is the database accidentally placed in a public subnet?



\## Interview Explanation



I design private cloud networks using RFC1918 ranges. I choose a parent VPC CIDR such as 10.0.0.0/16, then divide it into non-overlapping public, private app, database, and monitoring subnets across multiple availability zones. This makes routing, security, and troubleshooting cleaner.

