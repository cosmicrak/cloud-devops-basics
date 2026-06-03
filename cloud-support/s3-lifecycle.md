\# Week 5 Day 33 S3 Lifecycle Runbook



\## Scenario

S3 storage cost is increasing because old logs and temporary files are staying in Standard storage.



\## Checks

1\. Check bucket prefixes.

2\. Check object age.

3\. Check lifecycle rules.

4\. Verify rule scope/prefix.

5\. Confirm transition or expiration actions.



\## Diagnosis logic

If logs are old but still in Standard, check whether lifecycle rule exists and whether the prefix matches.

If temp files are not expiring, check expiration rule and prefix.

If small files are transitioned, check whether minimum object size and storage duration make it cost-effective.



\## Example policy idea

logs/ -> transition to Standard-IA after 30 days.

temp/ -> expire after 7 days.



\## Security note

Lifecycle rules manage cost and cleanup, but they do not replace access control.

Keep Block Public Access enabled for private data.



\## Interview explanation

I used S3 Lifecycle rules to transition old log objects to a lower-cost storage class and expire temporary objects. This helps automate cost optimization and cleanup.

