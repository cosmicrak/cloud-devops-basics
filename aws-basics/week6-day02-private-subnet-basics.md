\# Week 6 Day 2 - Private Subnet Basics



\## What I built

\- Private subnet inside custom VPC

\- Private route table

\- Route table association for private subnet



\## CIDR plan

VPC: 10.0.0.0/16

Public subnet A: 10.0.1.0/24

Private subnet A: 10.0.2.0/24



\## Public subnet route

10.0.0.0/16 -> local

0.0.0.0/0 -> Internet Gateway



\## Private subnet route

10.0.0.0/16 -> local

No direct 0.0.0.0/0 route to Internet Gateway



\## Key difference

A public subnet has a direct route to an Internet Gateway.

A private subnet does not have a direct route to an Internet Gateway.



\## NAT concept

A NAT device lets private subnet resources initiate outbound internet traffic while preventing unsolicited inbound internet connections.



\## Why NAT Gateway was not created

NAT Gateway can create extra cost, so this lab focused on route-table understanding first.



\## Lesson

Private subnet isolation is controlled mainly by route table design, not by the word “private” in the subnet name.

