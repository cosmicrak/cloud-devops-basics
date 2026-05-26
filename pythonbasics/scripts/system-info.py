import os
import platform
import getpass
from pathlib import Path
hostname = platform.node()
systemname=platform.system()
systemversion=platform.version()
currentuser=getpass.getuser()
currentdirectory=Path.cwd()
print("======SYSTEM INFO REPORT=======")
print(f"Operating System: {systemname}")
print(f"System Version: {systemversion}")
print(f"Current User: {currentuser}")
print(f"Current Directory: {currentdirectory}")
paths_to_check = [
Path.home(),
Path.cwd(),
Path("logs"),
Path("Config"),
Path("reports")
]
print("\n=====PATH CHECKS =======")
for path in paths_to_check:
	if path.exists():
		print(f"{path} exists")
	else:
		print(f"{path} missing")

home_env = os.environ.get("HOME") or os.environ.get("USERPROFILE")
path_env = os.environ.get("PATH")
print("\n =======ENVIRONMENT CHECKS =========")
print(f"HOME VARIABLE IS :{home_env}")
if path_env:
	print("Path environment exists")
else:
	print("Path variable missing")


summary ={
"hostname" : hostname,
"os" : systemname ,
"user" : currentuser ,
"current directory" :str(currentdirectory)
}
print("\n =======SUMMARY=======")
for key , value in summary.items():
	print(f"{key}: {value}")


