servers = [
    {"name": "web-01", "ip": "10.0.1.10", "role": "web", "status": "running"},
    {"name": "web-02", "ip": "10.0.1.11", "role": "web", "status": "running"},
    {"name": "db-01", "ip": "10.0.2.10", "role": "database", "status": "stopped"},
    {"name": "cache-01", "ip": "10.0.3.10", "role": "cache", "status": "running"},
]
for s in servers:
    print(f"name : {s['name']} , IP : {s['ip']}")

print("\n---- stopped servers are")
for s in servers:
    if s['status'] =='stopped':
        print(f"This server has stopped working {s['name']}")
for s in servers:
    if s['role'] == 'web':
        print(f"These are web based servers {s['name']}")
running_count=0
for s in servers:
    if s['status'] =='running':
        running_count +=1
print(f"total running severs are : {running_count}")


