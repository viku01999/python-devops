import json

# data = {"server": "web1", "status": "active"}

# with open("config.json", 'w') as file:
#     json.dump(data, file)


with open("config.json", 'r') as file:
    data = json.load(file)
    print(data)