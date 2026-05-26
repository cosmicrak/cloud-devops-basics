\# Week 3 Day 19 - Python Error Handling



\## What is error handling?

Error handling means controlling what happens when a script faces a problem.



\## try

try contains risky code that may fail.



\## except

except handles the error instead of letting the program crash.



\## FileNotFoundError

This happens when a script tries to open a file that does not exist.



\## Exception

Exception catches unexpected errors.



\## Script built

safe\_log\_reader.py



\## What it does

It reads app.log, counts ERROR lines, prints the result, and writes success or error messages to script.log.



\## Failure case tested

I renamed app.log and confirmed the script handled the missing file cleanly.



\## Why this matters for Cloud Support

Automation scripts should fail clearly and log errors so troubleshooting is easier.

