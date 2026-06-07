\# Week 6 Day 42 API Gateway Lambda Practical Use



\## When this is used

Use API Gateway + Lambda when an application needs a lightweight public backend endpoint without running an EC2 server.



\## Real-world examples

\- Contact form backend

\- Webhook receiver

\- Small JSON API

\- File metadata API

\- Automation endpoint

\- Internal tool backend

\- Serverless microservice



\## Example flow

Frontend/mobile app -> API Gateway -> Lambda -> JSON response



\## What support engineers check

1\. API route exists.

2\. Method and path are correct.

3\. Route is integrated with the correct Lambda.

4\. Stage is deployed or auto-deploy is enabled.

5\. Lambda permission allows API Gateway invocation.

6\. Lambda returns correct proxy format.

7\. CloudWatch Logs show invocation/errors.



\## Common errors worth remembering

\- Wrong route path: Not Found

\- Bad Lambda response format: 502 Bad Gateway

\- Lambda code error: 5xx response and CloudWatch traceback

\- Missing permission: API Gateway cannot invoke Lambda



\## Interview explanation

API Gateway acts as the public front door, while Lambda runs backend logic. This is useful for small APIs and event-driven backend tasks where maintaining a full EC2 server would be unnecessary.

