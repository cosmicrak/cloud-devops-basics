\# Week 6 Day 3 - Security Groups vs NACLs



\## What I learned

Security Groups are attached to resources like EC2.

Network ACLs are attached to subnets.



\## Main difference

Security Group: resource-level firewall.

NACL: subnet-level firewall.



\## Stateful vs stateless

Security Groups are stateful, so return traffic is automatically allowed.

NACLs are stateless, so inbound and outbound rules both matter.



\## Baseline

nginx worked locally with curl localhost.

Browser access worked through public IPv4.



\## Break-fix test

Added a temporary NACL DENY rule for HTTP 80.

Browser access failed.

curl localhost still worked.

Removed the NACL DENY rule.

Browser access worked again.



\## Root cause

The service was healthy, and the security group could be correct, but subnet-level NACL denied HTTP traffic.



\## Security note

Do not add broad deny rules casually.

Only temporary, narrow break/fix rules were used.

No AWS resource IDs or public IPs were committed.

