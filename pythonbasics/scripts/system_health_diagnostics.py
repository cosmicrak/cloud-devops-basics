import subprocess
import json
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig (
filename="system_health_report.log",
level = logging.INFO,
format= "%(asctime)s -%(levelname)s-%(message)s"
)

report_file =Path("System_health_report.json")

commands = [
    {"name": "hostname", "command": ["hostname"]},
    {"name": "current_user", "command": ["whoami"]},
    {"name": "uptime", "command": ["uptime"]},
    {"name": "disk_usage", "command": ["df", "-h"]},
    {"name": "memory_usage", "command": ["free", "-h"]},
    {"name": "fake_check", "command": ["fakecommand123"]}
]

def run_command(check):
	name =check["name"]
	command =check["command"]
	try:
		result=subprocess.run(
			command ,
			capture_output =True,
			text=True

		)
		if result.returncode == 0:
			logging.info(f"{name} succeeded")
		return {
			"name" : name,
			"command" : " ".join(command),
			"status" : "success",
			"return_code": result.returncode,
			"output" : result.stdout.strip(),
			"error" : result.stderr.strip()
		}
		logging.error(f"{name} failed with return code 					{result.returncode}")
		return {
			"name" : name,
			"command": " ".join(command),
            		"status": "failed",
           		"return_code": result.returncode,
            		"output": result.stdout.strip(),
            		"error": result.stderr.strip()
        }

			
	except FileNotFoundError:
		logging.error(f"{name} command not found : {command[0]}")
		return { 
			"name": name,
            		"command": " ".join(command),
            		"status": "command_not_found",
            		"return_code": None,
            		"output": "",
            		"error": f"Command not found: {command[0]}"
        	}
logging.info("system health check started")
results =[]
for check in commands:
	result =run_command(check)
	results.append(result)
summary = {
    "generated_at": str(datetime.now()),
    "total_checks": len(results),
    "successful_checks": sum(1 for item in results if item["status"] == 	"success"),
    "failed_checks": sum(1 for item in results if item["status"] != "success"),
    "results": results
}

with open(report_file, "w") as file:
    json.dump(summary, file, indent=4)


print("System health report generated")
print(f"Total checks: {summary['total_checks']}")
print(f"Successful checks: {summary['successful_checks']}")
print(f"Failed checks: {summary['failed_checks']}")
print(f"Report saved to: {report_file}")

logging.info("System health report completed")
	
