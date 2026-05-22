\# Day 03 - Linux Processes and Services



\## What is a process?

A process is a running program in Linux.



\## What is PID?

PID means Process ID. Linux uses it to identify and control processes.



\## What is a service?

A service is a background program managed by systemd.



\## Process commands practiced

\- ps aux

\- ps aux | grep bash

\- ps aux | grep nginx

\- top

\- htop

\- kill PID

\- kill -9 PID

\- pkill process\_name



\## Service commands practiced

\- sudo systemctl status nginx

\- sudo systemctl stop nginx

\- sudo systemctl start nginx

\- sudo systemctl restart nginx



\## nginx process structure

nginx has a master process and worker processes. The master controls nginx and workers handle requests.



\## What I understood

Processes are running programs. Services are background programs managed by systemctl. If a website is down, I should check service status, process list, logs, and then restart the service if needed.

