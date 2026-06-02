\# Week 5 Day 3 - EC2 SSM Access and nginx



\## What I built

\- Used an existing Amazon Linux EC2 instance

\- Attached an IAM role for Systems Manager

\- Connected using Session Manager

\- Installed nginx

\- Started and enabled nginx

\- Tested nginx locally inside EC2

\- Opened HTTP port 80

\- Tested nginx from browser using public IPv4



\## Why SSM is safer

Session Manager allows server access without opening SSH port 22.



\## IAM role

EC2-SSM-Role



\## Permission policy

AmazonSSMManagedInstanceCore



\## Commands used

whoami

pwd

cd \~

sudo dnf install nginx -y

sudo systemctl start nginx

sudo systemctl enable nginx

sudo systemctl status nginx

curl localhost



\## Security group rules

SSH 22 was not needed for SSM access.

HTTP 80 was opened to 0.0.0.0/0 to test the public web server.



\## What worked

curl localhost worked inside EC2.

Browser access using public IPv4 also worked.



\## Lesson

If curl localhost works but browser access fails, the issue is likely security group, public IP, route table, or external network access.

If browser access works, nginx is reachable publicly on HTTP port 80.

