\# Week 6 Day 41 - Lambda S3 Trigger



\## What I built

\- Lambda function using Python

\- S3 trigger on object upload

\- Lambda execution role

\- S3 read permission for Lambda

\- CloudWatch log verification



\## Flow

S3 object upload -> Lambda trigger -> Lambda reads object -> Lambda prints content type -> CloudWatch Logs



\## Concepts

Lambda runs code without managing servers.

An event is the input sent to Lambda.

The handler is the function AWS runs.

The execution role controls what Lambda can access.

CloudWatch Logs stores Lambda output and errors.



\## Error faced

Lambda was triggered but failed with AccessDenied during s3:GetObject.



\## Root cause

The Lambda execution role did not have effective identity-based permission for s3:GetObject on the uploaded object.



\## Fix

Attached correct S3 GetObject permission to the exact execution role used by the Lambda function.



\## Lesson

S3 trigger permission and Lambda S3 read permission are different:

\- S3 trigger invokes Lambda

\- Lambda execution role reads the S3 object



\## Security

No bucket names, ARNs, account IDs, object keys, or raw identifiers committed.

