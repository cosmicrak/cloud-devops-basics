\# Day 02 Nginx Service Troubleshooting Runbook



\## Scenario

A website hosted on nginx is not responding on localhost.



\## Symptoms

\- curl localhost fails

\- Browser does not show nginx page

\- nginx may be stopped



\## Diagnosis steps



\### 1. Check service status

sudo systemctl status nginx



\### 2. Check nginx process

ps aux | grep nginx



\### 3. Try curl

curl localhost



\### 4. Start service if stopped

sudo systemctl start nginx



\### 5. Restart if needed

sudo systemctl restart nginx



\### 6. Verify again

curl localhost



\## Root cause

nginx service was stopped, so no web server was listening to serve the request.



\## Fix

Start or restart nginx using systemctl.



\## Interview explanation

If a website is not responding, I first check whether the web server service is running. For nginx, I use systemctl status nginx and ps aux | grep nginx. If it is stopped, I start it and verify with curl localhost. This confirms whether the issue is service-level before checking deeper networking or firewall problems.

