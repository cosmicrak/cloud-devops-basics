\# Week 6 Day 3 NACL Troubleshooting Runbook



\## Scenario

EC2 web server works locally but browser access fails.



\## Checks

1\. Check nginx:

sudo systemctl status nginx



2\. Test locally:

curl localhost



3\. Check Security Group:

HTTP 80 should be allowed.



4\. Check subnet NACL:

Inbound HTTP 80 should not be denied.

Outbound response traffic should be allowed.



5\. Check route table:

0.0.0.0/0 should point to Internet Gateway for public subnet.



\## Diagnosis logic

If curl localhost fails, check nginx.

If curl localhost works but browser fails, check SG, NACL, route table, IGW, and public IP.

If SG allows HTTP but browser still fails, check NACL deny rules.

If a lower-numbered NACL deny rule exists, it overrides later allow rules.



\## Interview explanation

Security Groups protect resources and are stateful. NACLs protect subnets and are stateless. If an EC2 service is healthy but traffic fails externally, I check both the instance security group and the subnet NACL.

