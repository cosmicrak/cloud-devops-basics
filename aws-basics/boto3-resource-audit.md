\# Week 5 Day 35 - boto3 Resource Audit



\## What I built

I built a Python boto3 script that audits AWS resources in read-only mode.



\## Concepts

boto3 is the AWS SDK for Python.

It lets Python interact with AWS services programmatically.

This lab used read-only calls to inspect resources.



\## Script

aws\_resource\_audit.py



\## AWS calls used

\- sts.get\_caller\_identity()

\- ec2.describe\_instances()

\- s3.list\_buckets()



\## Safety

The script redacts account IDs, ARNs, instance IDs, and bucket names.

No access keys or secrets are committed.



\## Access review checklist

\- EC2 stopped when not in use

\- SSH 22 not open to 0.0.0.0/0

\- S3 Block Public Access ON

\- IAM test access keys deleted

\- Budget alert active

\- .gitignore protects credentials and .pem files



\## Failure test

I tested with a fake AWS profile and confirmed the script fails when credentials/profile are invalid.



\## Lesson

A cloud support engineer can use boto3 to audit resource state programmatically instead of checking everything manually in the console.

