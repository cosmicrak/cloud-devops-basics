\# Week 2 Day 12 - Ports and Sockets



\## Port

A port identifies a service inside a machine.



\## Socket

A socket is an IP address plus a port.



Example:

10.0.0.5:80



\## Listening

Listening means a service is waiting for connections on a port.



\## Commands practiced

\- sudo ss -tulpn

\- sudo ss -tulpn | grep :80

\- sudo netstat -tulpn

\- sudo netstat -tulpn | grep :80

\- sudo lsof -i :80

\- sudo systemctl stop nginx

\- sudo systemctl start nginx

\- curl localhost



\## What I understood

If a website is not opening, the server may be reachable but the web service may not be listening on port 80.



\## Common ports

\- 22 SSH

\- 53 DNS

\- 80 HTTP

\- 443 HTTPS

\- 3306 MySQL

\- 5432 PostgreSQL

\- 6379 Redis

\- 8080 alternate web/app port

