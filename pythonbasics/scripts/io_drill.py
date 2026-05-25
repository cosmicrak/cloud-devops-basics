error_count = 0
from pathlib import Path
log_file = Path("sample.log")
if not log_file.exists():
   print("error:sample.log not found")
   exist(1)

with open("sample.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(f"found issue here: {line.strip()}")
            error_count += 1

with open("result.txt", "w") as output:
    output.write(f"Total errors found: {error_count}\n")
