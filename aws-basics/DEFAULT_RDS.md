\# Day 38 - RDS MySQL Connectivity Attempt



\## What happened

The original goal was to create RDS MySQL inside private subnets of the custom VPC.



The RDS Full Create console flow did not show the expected custom VPC even after creating the DB subnet group, so the lab was switched to Easy Create. Easy Create created the database using default VPC settings.



\## Final lab path

Windows EC2 in default VPC -> RDS MySQL in default VPC



\## Commands learned

nslookup RDS\_ENDPOINT

Test-NetConnection RDS\_ENDPOINT -Port 3306

mysql --version

mysql -h RDS\_ENDPOINT -P 3306 -u admin -p



\## What worked

TcpTestSucceeded returned True, proving EC2 could reach RDS on port 3306.



\## Main lesson

RDS connectivity troubleshooting should be done layer by layer:

DNS -> network port -> security group -> MySQL client -> authentication.



\## Security

RDS port 3306 should not be open to 0.0.0.0/0.

Allow MySQL only from the EC2 security group.

No DB endpoint, password, IPs, IDs, or ARNs were committed.







mysql -h $RDS\_ENDPOINT -P 3306 -u admin -p

$RDS\_ENDPOINT = "INstant endpoint number"

Test-NetConnection $RDS\_ENDPOINT -Port 3306

nslookup $RDS\_ENDPOINT

