\# Week 5 Day 32 - Private S3 Repository and Versioning



\## What I built

\- Private S3 bucket

\- Block Public Access enabled

\- S3 versioning enabled

\- Uploaded the same object twice

\- Observed multiple object versions

\- Deleted object and observed delete marker

\- Restored object by removing delete marker



\## Concepts

S3 stores objects inside buckets.

A bucket can act as a private repository for files, logs, backups, and artifacts.

Block Public Access prevents accidental public exposure.

Versioning keeps previous versions when an object is overwritten.

A delete marker makes an object appear deleted while old versions still exist.



\## Security settings

Block Public Access: ON

ACLs: disabled

Bucket versioning: enabled

Encryption: default



\## Commands used

aws s3 cp version-test.txt s3://BUCKET\_NAME/version-test.txt

aws s3 ls s3://BUCKET\_NAME

aws s3 cp s3://BUCKET\_NAME/version-test.txt downloaded-current.txt

aws s3 rm s3://BUCKET\_NAME/version-test.txt



\## Failure test

The Object URL returned AccessDenied because the bucket and object were private.



\## Restore test

After deleting the delete marker, the object became accessible again through authorized CLI access.



\## Notes

Actual bucket name and version IDs are not committed for security hygiene.

