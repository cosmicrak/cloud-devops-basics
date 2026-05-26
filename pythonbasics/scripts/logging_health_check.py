import logging
logging.basicConfig(
filename ="health_check.log",
level=logging.INFO,
format="%(asctime)s - %(levelname)s -%(message)s"
)
services =[
{"name" : "nginx" , "status" : "running"},
{"name": "mysql", "status": "stopped"},
{"name": "redis", "status": "unknown"},
{"name": "docker"} ,
{"name": "postgres"}
]
healthy =0
failed =0
unknown=0
for i in services :
	name =i.get("name " , "unknown service")
	status = i.get("status" , "unknown")
	if status == "running":
		healthy += 1
		logging.info(f"{name} is running")
	elif status == "stopped":
		failed +=1
		logging.error(f"{name} has stopped running")
	else:
		unknown +=1
		logging.warning(f"{name} status unknown")
print(f"healthy:{healthy}")
print(f"Failed: {failed}")
print(f"Unknown: {unknown}")
print("Log written to health_check.log")

