\# Week 6 Day 43 SQS and SNS Practical Use



\## When SQS is used

Use SQS when work should wait safely until a worker is ready.



Examples:

\- background order processing

\- email jobs

\- image/video processing

\- retryable tasks

\- traffic spike buffering

\- async job queues



\## When SNS is used

Use SNS when one event should notify one or more subscribers.



Examples:

\- alert notifications

\- order-created events

\- fanout to multiple queues

\- triggering Lambda

\- sending events to different systems



\## Real-world pattern

Order service publishes an OrderCreated event to SNS.

SNS sends the same event to multiple SQS queues.

Each queue can be processed by a different worker.



Example:

OrderCreated -> SNS Topic -> Payment Queue

OrderCreated -> SNS Topic -> Inventory Queue

OrderCreated -> SNS Topic -> Email Queue



\## What support engineers check

\- Is the SNS topic receiving messages?

\- Is the SQS queue subscribed?

\- Does the SQS access policy allow SNS to send messages?

\- Are messages stuck in the queue?

\- Are consumers polling and deleting messages?

\- Are there duplicate messages?

\- Is the correct queue/topic being used?



\## Common issues worth remembering

SNS published but SQS received nothing: subscription or queue policy issue.

Messages stay in SQS: no consumer or consumer failed.

Messages reappear: consumer received but did not delete.

Duplicate messages: possible with Standard queues.



\## Interview explanation

SQS is used as a reliable queue for asynchronous processing. SNS is used to broadcast events to subscribers. Together, SNS and SQS decouple services so producers do not directly depend on consumers.

