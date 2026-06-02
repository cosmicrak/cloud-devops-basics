\# Week 5 Day 31 - EC2 Route Properties and S3 Copy



\## What I completed

\- Verified nginx web host on EC2

\- Inspected EC2 networking properties

\- Checked VPC, subnet, public IPv4, private IPv4, security group, and route table

\- Created a private S3 bucket/object

\- Attached S3 read permission to EC2 IAM role

\- Used aws s3 cp inside EC2 to copy a file from S3



\## Route path

Browser -> Public IPv4 -> Internet Gateway -> Route table -> Subnet -> Security group HTTP 80 -> EC2 nginx



\## Important EC2 network properties (Screenshot saved on Local device)

\- VPC ID:

\- Subnet ID:

\- Public IPv4:

\- Private IPv4:

\- Security group:

\- Availability Zone:



\## IAM role

EC2-SSM-Role



\## Policies attached

\- AmazonSSMManagedInstanceCore

\- AmazonS3ReadOnlyAccess



\## Commands used inside EC2

aws --version

aws sts get-caller-identity

aws s3 ls s3://BUCKET\_NAME

aws s3 cp s3://BUCKET\_NAME/ec2-message.txt .

cat ec2-message.txt



\## Failure test

Tried copying a non-existing object key from S3.

The command failed as expected.



\## Lesson

EC2 should use an IAM role for AWS access instead of storing access keys on the server. A private S3 object can be copied to EC2 using aws s3 cp if the EC2 role has permission.

