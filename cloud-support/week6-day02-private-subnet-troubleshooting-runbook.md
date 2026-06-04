\# Week 6 Day 2 Private Subnet Troubleshooting Runbook



\## Scenario

An EC2 instance in a private subnet cannot be reached from the internet or cannot access public services.



\## Checks

1\. Does the instance have a public IPv4?

2\. Is the subnet route table public or private?

3\. Does route table have 0.0.0.0/0 -> Internet Gateway?

4\. Is there a NAT device for outbound internet?

5\. Is there a VPC endpoint for AWS service access?

6\. Is the security group allowing required traffic?

7\. Is outbound HTTPS 443 allowed if using SSM?



\## Diagnosis logic

If subnet has no route to IGW, it is private.

If private EC2 has no NAT/VPC endpoint, it may not access internet or SSM endpoints.

If public access is required, resource should be in public subnet or exposed through a load balancer.

If only outbound updates are needed, use NAT or VPC endpoints.



\## Security note

Do not add IGW route to a private subnet just to “fix” access unless the design should become public.



\## Interview explanation

A private subnet is private because its route table lacks a direct route to an internet gateway. To allow outbound-only access, use NAT or VPC endpoints instead of making the subnet public.

