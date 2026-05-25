\# Week 3 Day 18 File Checking Runbook



\## Scenario

A Python script fails because a required file is missing.



\## Diagnosis

Check current folder:

pwd



Check files:

ls



Check if file exists in Python:

Path("sample.log").exists()



\## Fix

Use pathlib before opening files.



Example:

if not log\_file.exists():

&#x20;   print("Error: sample.log not found")

&#x20;   exit(1)



\## Why this matters

Scripts should fail clearly when input files are missing instead of crashing with confusing errors.



\## Interview explanation

Before reading a file, I check whether it exists using pathlib. I use with open() so the file is closed automatically after reading.

