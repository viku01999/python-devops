

servers = ["web1","web2","web3"]
print(servers)
print(servers[0])

servers.append("web4")
print(servers)

for s in servers:
    print(f"Checking status of {s}... ")