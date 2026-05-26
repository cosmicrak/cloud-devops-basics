from datetime import datetime

filename ="app.log"
error_count=0

try:
	with open(filename , "r") as file:
		for line in file:
			if "ERROR" in line:
				error_count +=1
	print(f"total error count :{error_count}")
	rn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	with open("script.log" , "a") as log_file:
		log_file.write(f"[{rn}] successfully processed {filename}.\n")
except FileNotFoundError:
	print(f"Error: the file '{filename}' was not found.")
except Exception as e :
	print(f"Error an unexpected error occured :{e}")



