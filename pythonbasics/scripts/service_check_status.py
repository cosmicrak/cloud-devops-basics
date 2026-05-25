servers = [
    {"name": "web-01", "service": "nginx", "status": "running"},
    {"name": "db-01", "service": "mysql", "status": "stopped"},
    {"name": "cache-01", "service": "redis"},
]
def check_service(i):
   
    status = i.get("status")
   
    if status == "running":
        return "HEALTHY"
    elif status == "stopped":
        return "ALERT"
    
    else:
        return "service status unknown"
    
hc=0
ac=0
unknown=0
print("--server stauts report")
for i in servers:
    result = check_service(i)
    print(f"server is {i['name']} | service: {i['service']} | status is {result} ")


    if result == "HEALTHY":
        hc +=1
    elif result == "ALERT":
        ac +=1
    else:
        unknown +=1
print(f"Healthy: {hc}")
print(f"Alert: {ac}")
print(f"Unknown: {unknown}")


