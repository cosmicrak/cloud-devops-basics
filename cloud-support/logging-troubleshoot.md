\# Week 3 Day 20 Python Logging Runbook



\## Scenario

A Python automation script runs, but I need to know what happened after execution.



\## Why logs matter

Logs provide a timestamped record of normal events, warnings, and errors.



\## Diagnosis steps

1\. Run the script:

python logging\_health\_check.py



2\. Check output:

cat health\_check.log



3\. Search errors:

grep ERROR health\_check.log



4\. Search warnings:

grep WARNING health\_check.log



\## Common log levels

\- INFO: normal event

\- WARNING: suspicious or unknown state

\- ERROR: failed operation

\- CRITICAL: severe failure



\## Root-cause thinking

If ERROR appears, check the failed service first.

If WARNING appears, check missing or unknown data.

If no logs appear, check logging filename/path and script execution.



\## Interview explanation

I use Python logging instead of only print statements because logs preserve timestamped records of what the script did. This helps debug automation failures later.

