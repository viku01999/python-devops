import re

# log = "User admin logged in from 192.168.10.12"
# ip = re.search(r"\d+\.\d+\.\d+\.\d+", log)

# if ip:
#     print("Ip address is ", ip.group())



logs = [
    "INFO: Server web1 started successfully",
    "ERROR: Server web2 failed to start",
    "WARNING: Server db1 high memory usage"
]


for log in logs:
    if "ERROR" in log:
        server = re.search(r"Server (\w+)", log).group(1)
        print(f"Issue detected on server: {server}")