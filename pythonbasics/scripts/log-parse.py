from pathlib import Path
import json
import logging
logging.basicConfig(
	filename="parser.log",
	level=logging.INFO,
	format="%(asctime)s - %(levelname)s -%(message)s"
)
log_file=Path("sample.log")
summary_file=Path("log_summary.json")
if not log_file.exists():
	print("Error : sample_app.log not found")
	exit(1)
info_count =0
warning_count=0
error_count=0
error_lines = []
logging.info("log parser started")
with open(log_file , "r") as f:
	for line in f:
		clean_line =line.strip()
		upper_line = clean_line.upper()
		if "INFO" in clean_line:
			info_count +=1
		elif "ERROR" in upper_line:
			error_count += 1
			error_lines.append(clean_line)
		elif "WARNING" in clean_line:
            		warning_count += 1
		

summary ={

    "log_file": str(log_file),
    "info_count": info_count,
    "warning_count": warning_count,
    "error_count": error_count,
    "error_lines": error_lines
}
with open(summary_file , "w") as output:
	json.dump(summary , output , indent=4)
print("Log parsing completed")
print(f"INFO LINES:{info_count}")
print(f"WARNING lines: {warning_count}")
print(f"ERROR lines:{error_count}")
print(f"summary saved to {summary_file}")
logging.info("Log summary created successfully")

