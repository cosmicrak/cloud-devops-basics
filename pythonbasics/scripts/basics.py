server_name="web 02"
status = "running"
print(server_name)
print(status)
print(f"Server{server_name} is {status}")
logline ="Error database connection failed"
print(logline.strip())
print(logline.lower())
print(logline.upper())
print(logline.replace("database" , "DB"))
servers=["web -01","db-01","cache"]
print(servers)
print(servers[0])
print(servers[-1])
servers.append("api -01")
print(servers)
for i in servers:
    print(f"checkin {i}")
server = {
    "name": "rakshit",
    "ip": "5069",
    "status": "running"
}
print(server["name"])
print(server["ip"])

print(server["status"])
ips=["0.2222","0.5555","9.4444","2324.44","0.2222","0.5555"]

ips.append("8.999")
uniq=set(ips)
print(uniq)

def check_status(server_name , status):
    if status =="running":
        return f"{server_name}is ready to run"
    else:
        return f"{server_name} needs your attention can't work"
print(check_status("web-88","running"))
print(check_status("db-01", "stopped"))
