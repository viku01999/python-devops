# text  = "server1"
# print(text[0])


# slicing
# server = "web-server-01"
# print(server[0:3])
# print(server[4:10])

# some common
# text = "   DevOps Automation   "
# print(text.lower())
# print(text.strip())
# print(text.replace("Ops", "Engineer"))

# formatting
# server = "web01"
# status = "running"
# print(f"Server {server} is currently {status}.")
# print("Connecting to {}...".format(server))

# checking substring
# log = "Error: disk full on /dev/sda1"
# if "Error" in log: 
#     print("Error found")

# Joining and spilliting
data = "web1,web2,web3"
server = data.split(',')
print(server)

joined = "-".join(server)
print(joined)