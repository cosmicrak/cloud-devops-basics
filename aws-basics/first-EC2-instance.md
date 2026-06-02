\#Week 5 day 02 -First EC2 instance

\##what did I learn and Create:

\-Amazon Linux EC2 instance

\-Key pair

\-Security group

\-Public IPv4 access



\##Concepts

EC2 is a vitual server in AWS

AMI is the operating system image 

Instance Type is the server size

Key pair is used for SSH login 

Security groups out there are called cloud firewall

Public IPv4 is used to connect from the Internet 

Private IPv4 is used inside AWS VPC



\##Settings

AMI: Amazon Linux 2023

Instance type : micro/free eligible

Key pair : cloud-Linux-key

security group- SSH port 22

Storage:default 8 Gib



\##commands ran inside EC2

whoami

pwd

hostname

free -h

uptime



\##Issues faced

EC2 conn worked when SSH sources were temporarily set to 0.0.0.0/0 , but failed while using my IP.



\##Root cause

I was using my mobile hotspot , so my public IP most likely changed or did not match the IP saved in my security group and then failed to establish a conn



\##Lesson

If SSH times out check security group source IP , Public IP , instance state , username and key pair  



