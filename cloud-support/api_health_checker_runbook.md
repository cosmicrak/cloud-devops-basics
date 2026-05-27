# Week 4 Day 25 API Health Checker sqlite3 Runbook

## Scenario
I need to monitor API or website health and keep previous check results.

## Tool
api_health_checker_sqlite.py

## What it checks
- URL reachability
- HTTP status code
- timeout
- DNS or connection failure

## Output
- health_checks.db
- api_health_checker_sqlite.log

## Database table
health_checks

## Diagnosis logic
If status is UP, the endpoint returned HTTP 200.
If status is UNHEALTHY, the endpoint responded but with an unexpected status code.
If status is DOWN, the request failed due to DNS, timeout, or connection issue.

## Failure handling
A fake domain should be recorded as DOWN instead of crashing the script.

## Interview explanation
I built an API health checker using requests and sqlite3. It checks endpoints, handles failures, logs activity, and stores each result in a local database for historical tracking.