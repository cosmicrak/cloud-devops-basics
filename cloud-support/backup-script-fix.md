\# Day 06 Backup Script Troubleshooting Runbook



\## Scenario

Backup script does not create a .tar.gz file.



\## Diagnosis steps



\### 1. Check current folder

pwd



\### 2. Check script exists

ls -l backup.sh



\### 3. Check execute permission

ls -l backup.sh



\### 4. Run script with bash

bash backup.sh source-folder



\### 5. Check input folder exists

ls source-folder



\### 6. Check backup files

ls \*.tar.gz



\### 7. Check logs

cat backup.log



\## Common root causes

\- Missing input argument

\- Wrong folder name

\- Missing execute permission

\- Typo in script filename

\- Missing quote in Bash syntax

\- tar command failed



\## Fix examples



If permission denied:

chmod +x backup.sh



If folder is wrong:

./backup.sh correct-folder-name



If syntax error:

bash -n backup.sh



\## Interview explanation

If a backup script fails, I first check the script permission, input argument, source folder, syntax using bash -n, and logs. I use set -euo pipefail so that script failures are visible instead of silent.

