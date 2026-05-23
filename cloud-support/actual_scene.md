\# Day 03 Process and Service Troubleshooting Runbook



\## Scenario

A web server is not responding.



\## Symptoms

\- curl localhost fails

\- Browser cannot load website

\- nginx may be stopped

\- nginx process may not exist



\## Diagnosis steps



\### 1. Test the web server

curl localhost



\### 2. Check service status

sudo systemctl status nginx



\### 3. Check process list

ps aux | grep nginx



\### 4. Check logs

sudo tail /var/log/nginx/error.log



\### 5. Restart service

sudo systemctl restart nginx



\### 6. Verify again

curl localhost



\## If a process is stuck

Find PID:

ps aux | grep process\_name



Stop normally:

kill PID



Force stop:

kill -9 PID



Stop by name:

pkill process\_name



\## Root cause examples

\- Service was stopped

\- Process crashed

\- Wrong config stopped nginx from starting

\- Port already in use

\- System resource pressure



\## Interview explanation

If a Linux web service is not responding, I first test with curl, then check systemctl status to see whether the service is running. I verify actual processes using ps aux | grep nginx, check error logs, then restart the service if needed. If a process is stuck, I identify its PID and stop it carefully, using kill -9 only as a last resort.

