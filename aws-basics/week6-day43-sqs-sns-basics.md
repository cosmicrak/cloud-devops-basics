\# Week 6 Day 43 - SQS and SNS Basics



\## What I built

\- Standard SQS queue

\- Manual SQS message send/receive/delete test

\- Standard SNS topic

\- SNS subscription to SQS queue

\- SNS publish test

\- SQS received SNS-published message



\## Concepts

SQS is a message queue. It stores messages until a consumer receives and deletes them.



SNS is a publish-subscribe notification service. It broadcasts messages to subscribers.



Together, SNS and SQS are used to decouple systems.



\## Architecture

Producer -> SNS Topic -> SQS Queue -> Consumer



\## SQS test

Sent a manual order message to SQS.

Polled the queue.

Viewed the message.

Deleted the message.



\## SNS test

Published an order message to SNS.

SNS delivered the message to the subscribed SQS queue.

SQS stored the message until it was polled.



\## Practical lesson

SQS is used when work should wait safely.

SNS is used when one event should notify subscribers.

SNS + SQS is useful when one event must be delivered reliably to one or more worker queues.



\## Security

No ARNs, account IDs, queue URLs, topic IDs, or raw resource identifiers committed.

