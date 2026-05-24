\# Week 2 Day 09 - cut, awk and sed



\## What problem these commands solve

They help extract and modify useful text from logs, config files, and command output.



\## cut

cut extracts simple fields from a file.



Example:

cut -d ":" -f1 users.txt



\## awk

awk processes columns and can filter rows using conditions.



Examples:

awk -F ":" '{print $1, $2}' users.txt

awk -F ":" '$3=="active" {print $1}' users.txt



\## sed

sed replaces or edits text in a stream.



Example:

sed 's/inactive/disabled/g' users.txt



\## Commands practiced

\- cut -d ":" -f1 users.txt

\- cut -d ":" -f1,3 users.txt

\- awk -F ":" '{print $1, $2}' users.txt

\- awk -F ":" '$3=="active" {print $1}' users.txt

\- awk -F ":" '$2=="developer" {print $1}' users.txt

\- sed 's/inactive/disabled/g' users.txt

\- sed 's/inactive/disabled/g' users.txt > users-updated.txt



\## Cloud Support use

These tools are useful for reading logs, extracting usernames, statuses, IPs, errors, timestamps, and replacing text patterns in config-style files.

