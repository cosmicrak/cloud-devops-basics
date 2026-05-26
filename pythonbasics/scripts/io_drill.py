from pathlib import Path
from datetime import datetime

log_file= Path("sample.log")
error_file= Path("error.log")
report_file = Path("file_io.txt")
error_count = 0
if not log_file.exists():
	print("Error: sample.log not found")
	exit(1)
with open(log_file, "r") as file, open(error_file, "w") as errors:
    for line in file:
        if "ERROR" in line:
            errors.write(line)
            error_count += 1

with open(report_file, "a") as report:
    report.write(f"{datetime.now()} - Total ERROR lines: {error_count}\n")

print(f"Total ERROR lines: {error_count}")
print("ERROR lines saved to errors_only.log")
print("Summary appended to file_io_report.txt")