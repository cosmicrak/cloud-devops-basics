\# Week 5 Day 33 - S3 Storage Classes and Lifecycle



\## What I built

\- Uploaded objects with prefixes

\- Created lifecycle rule for logs/

\- Created lifecycle rule for temp/

\- Kept bucket private



\## Concepts

S3 storage classes are used for different access patterns and cost needs.

S3 Lifecycle rules automate transitions and expiration.

A prefix is the beginning of an object key, such as logs/ or temp/.



\## Objects uploaded

\- logs/app-log-1.txt

\- backups/backup-1.txt

\- temp/temp-report-1.txt



\## Lifecycle rules

logs-transition-rule:

\- Prefix: logs/

\- Action: transition current versions

\- Target: Standard-IA

\- Days: 30



temp-expire-rule:

\- Prefix: temp/

\- Action: expire current versions

\- Days: 7



\## Security

Block Public Access remained ON.

No bucket name or AWS resource IDs committed.



\## Important lesson

Lifecycle rules help reduce storage cost and clean temporary data automatically.

For tiny files, transitions may not be cost-effective, but the concept is important.

