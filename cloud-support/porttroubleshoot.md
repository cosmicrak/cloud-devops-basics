\# Week 2 Day 12 Port Troubleshooting Runbook



\## Scenario

A website or service is not reachable.



\## Goal

Check whether the service is listening on the expected port.



\## Step 1: Check listening ports

sudo ss -tulpn



\## Step 2: Check specific port

sudo ss -tulpn | grep :80



\## Step 3: Check process using port

sudo lsof -i :80



\## Step 4: Check service status

sudo systemctl status nginx



\## Step 5: Restart service

sudo systemctl restart nginx



\## Step 6: Verify

curl localhost



\## Diagnosis logic

If server is reachable but port is not listening, the service may be stopped or misconfigured.

If port is listening but curl fails, check firewall, config, logs, or app behavior.

If wrong process owns the port, there may be a port conflict.



\## Interview explanation

I check whether the expected service is listening on the correct port using ss or netstat. Then I map the port to a process using lsof or ss output. If no process is listening, I check the service with systemctl and restart it if needed.

