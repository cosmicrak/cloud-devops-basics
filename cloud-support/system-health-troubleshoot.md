\# Week 4 Day 24 System Health Report Runbook



\## Scenario

I need to collect quick diagnostic information from a Linux machine.



\## Tool

system\_health\_report.py



\## Checks performed

\- hostname

\- current user

\- uptime

\- disk usage

\- memory usage



\## Output

The script creates system\_health\_report.json and system\_health\_report.log.



\## Diagnosis logic

If a check status is success, the command ran correctly.

If status is failed, check stderr and return code.

If status is command\_not\_found, check whether the command exists or PATH is correct.



\## Failure handling

The script handles missing commands using FileNotFoundError and records the failure in JSON instead of crashing.



\## Interview explanation

I built a Python diagnostic script that uses subprocess to run Linux commands, captures stdout, stderr, and return codes, then writes a structured JSON report. This helps automate basic server health checks.

