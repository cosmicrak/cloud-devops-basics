\# Week 6 Day 42 - API Gateway with Lambda



\## What I built

\- Python Lambda function

\- HTTP API in API Gateway

\- GET /hello route

\- Lambda integration

\- Public API endpoint returning JSON

\- CloudWatch log verification



\## Architecture

Client/browser -> API Gateway HTTP API -> Lambda -> JSON response



\## Concepts

Lambda runs backend code without managing servers.

API Gateway creates a public HTTP endpoint.

A route maps an HTTP method and path to a backend integration.

Lambda proxy response needs statusCode and body.



\## Route

GET /hello



\## Query parameter test

/hello?name=Rakshit



\## Lambda response

Returned JSON with message, name, service, and status.



\## Practical use

This pattern is used for lightweight backend APIs, webhook handlers, automation endpoints, and serverless microservices without running EC2.



\## Important lesson

If Lambda works but API URL fails, check API route, integration, stage deployment, and Lambda response format.



\## Security

No API IDs, ARNs, account IDs, or raw endpoints committed.

