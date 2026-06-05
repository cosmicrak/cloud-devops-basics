\# VPC Flow Logs and CloudWatch Logs

\## What I built 

* CloudWatch log group for VPC Flow Logs
* IAM role for VPC Flow Logs to publish to CloudWatch
* VPC Flow Log generated for week 6
* Generated web traffic for EC2 Nginx
* Viewed flow records in CloudWatch Logs
* Queried logs using CloudWatch Logs insights 

\## Concepts

VPC Flow Logs capture metadata about IP traffic going to and from network interfaces.

They do not capture actual packet contents or website data.

\##Flow Log destination

CloudWatch Logs



\##SQL queries run:

\### Recent Records 

```sql

fields @timestamp, @message

| sort @timestamp desc

| limit 20





\###Rejected Records

fields @timestamp, @message

| filter @message like /REJECT/

| sort @timestamp desc

| limit 20 



\###Accepted Records

fields @timestamp, @message

| filter @message like /ACCEPT/

| sort @timestamp desc 

| limit 20 



\###HTTP Records

fields @timestamp, @message

| filter @message like /80/

| sort @timestamp desc 

| limit 20



