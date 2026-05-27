\# Week 4 Day 25 - API Health Checker with sqlite3



\## What I built

I upgraded the API health checker to store endpoint health check results in a sqlite3 database.



\## Concepts used

\- requests

\- sqlite3

\- logging

\- datetime

\- try/except

\- status codes

\- database table

\- INSERT query

\- SELECT query



\## Database file

health\_checks.db



\## Table

health\_checks



\## Fields stored

\- url

\- status

\- status\_code

\- error

\- checked\_at



\## Failure case tested

A fake domain was checked and saved as DOWN without crashing the script.



\## Why this matters for Cloud Support

A database lets the script keep historical health check results instead of only showing the latest run.

