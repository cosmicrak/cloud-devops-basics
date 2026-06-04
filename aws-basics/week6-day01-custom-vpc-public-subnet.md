\# Week 6 Day 1 - Custom VPC Public Subnet



\## What I built

\- Custom VPC

\- Public subnet

\- Internet gateway

\- Public route table

\- EC2 instance inside custom public subnet

\- nginx web server



\## CIDR plan

VPC: 10.0.0.0/16

Public subnet A: 10.0.1.0/24



\## Route table

Local route: VPC CIDR -> local

Public route: 0.0.0.0/0 -> Internet Gateway



\## Security group

HTTP 80 from 0.0.0.0/0

SSH not opened publicly

Session Manager used for access



\## Commands

whoami

hostname

ip addr

curl -I https://aws.amazon.com

sudo dnf install nginx -y

sudo systemctl start nginx

sudo systemctl enable nginx

sudo systemctl status nginx

curl localhost



\## Break-fix test

Removed the 0.0.0.0/0 route to the internet gateway.

Browser access failed while local nginx still worked.

Added the route back and browser access recovered.



\## Lesson

A public EC2 web server needs:

\- public IPv4

\- subnet route to internet gateway

\- security group allowing HTTP 80

\- running web service



\## Security

No SSH 22 from 0.0.0.0/0.

No AWS resource IDs, account IDs, IPs, ARNs, or keys committed.

