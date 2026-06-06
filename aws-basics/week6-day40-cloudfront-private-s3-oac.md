\# Week 6 Day 40 - CloudFront with Private S3 Origin



\## What I built

\- Private S3 bucket with uploaded webpage files

\- CloudFront distribution

\- S3 origin connected to CloudFront

\- Origin Access Control for private S3 access

\- Bucket policy allowing CloudFront access

\- Public CloudFront webpage



\## Architecture

User -> CloudFront distribution -> private S3 bucket



\## What worked

\- Direct S3 object access returned AccessDenied

\- CloudFront distribution URL loaded the webpage

\- Image uploaded to S3 loaded through CloudFront



\## Concepts

CloudFront is a CDN that caches and serves content globally.

S3 is the origin storing the actual files.

OAC allows CloudFront to securely access a private S3 bucket.

The bucket stays private while CloudFront serves the content publicly.



\## Security

S3 Block Public Access stayed ON.

S3 bucket was not made public.

Access was allowed only through CloudFront.

No bucket names, distribution IDs, ARNs, or raw resource identifiers were committed.



\## Lesson

For secure static content delivery, keep S3 private and expose content through CloudFront using Origin Access Control.

