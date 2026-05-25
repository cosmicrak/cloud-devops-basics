server_list = [
    {"name": "web 01", "status": "running actively"},
    {"name": "cloud-EC2", "status": "not running"},
    {"name": "server 03", "status": "can t configure"}
]
for i in server_list:
    if i["status"] == "not running" and i["name"] == "cloud-eC2":
        print(f"NEED YOUR ATTENTION {i['name']} is {i['status']}")
    else:
        print("everything working correctly")
    print(f"running servers are  {len(server_list)}")
                                  


