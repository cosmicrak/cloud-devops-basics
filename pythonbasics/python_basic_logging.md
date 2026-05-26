\# Week 3 Day 20 - Python Logging



\## What is logging?

Logging records events from a script into a file or console.



\## Why logging is better than print

print is temporary output. logging creates structured records with time, level, and message.



\## Log levels

\- INFO = normal event

\- WARNING = suspicious or unknown state

\- ERROR = failure

\- CRITICAL = serious failure



\## logging.basicConfig

basicConfig sets where logs go, what level to record, and how log lines should look.



\## Script built

logging\_health\_check.py



\## What it does

It checks service status values and logs running, stopped, and unknown services to health\_check.log.



\## Failure case tested

A service with missing status was handled as unknown instead of crashing.



\## Why this matters for Cloud Support

Automation scripts need logs so engineers can understand what happened after the script runs.

