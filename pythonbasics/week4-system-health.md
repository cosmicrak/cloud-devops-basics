\# Week 4 Day 24 - System Health Report



\## What I built

I built system\_health\_report.py to run multiple Linux diagnostic commands and save their results into a JSON report.



\## Concepts used

\- subprocess

\- json

\- logging

\- datetime

\- pathlib

\- functions

\- list of dictionaries

\- return codes

\- stdout and stderr

\- FileNotFoundError handling



\## Commands checked

\- hostname

\- whoami

\- uptime

\- df -h

\- free -h

\- fakecommand123



\## What the JSON report contains

\- generated time

\- total checks

\- successful checks

\- failed checks

\- command output

\- command errors



\## Failure case tested

A fake command was added to confirm the script handles missing commands without crashing.



\## Cloud Support use

This script can collect basic server diagnostic information automatically and save it in a structured report.

