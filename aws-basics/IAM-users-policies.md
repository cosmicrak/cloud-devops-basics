\# Week 5 Day 34 - IAM Users Groups Policies Roles



\## What I learned

IAM controls who can do what in AWS.



\## IAM identities

\- User: identity for a person or long-term credentials

\- Group: collection of users

\- Role: assumable identity for AWS services or temporary access

\- Policy: JSON permission document



\## Lab created

\- Group: S3ReadOnlyStudents

\- Test user: s3-readonly-test-user

\- Policy: AmazonS3ReadOnlyAccess



\## Commands tested

aws configure --profile s3readonly

aws sts get-caller-identity --profile s3readonly

aws s3 ls --profile s3readonly

aws s3 ls s3://BUCKET\_NAME --profile s3readonly

aws s3 cp denied-test.txt s3://BUCKET\_NAME/denied-test.txt --profile s3readonly



\## Result

Read/list actions worked.

Upload action failed with AccessDenied.

This proved least privilege.



\## Important IAM rule

Permissions are denied by default.

An Allow is required.

Explicit Deny overrides Allow.



\## Security hygiene

Actual account IDs, access keys, ARNs, and bucket names were not committed.

The test access key was deleted after the lab.

