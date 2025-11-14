import yaml


# data = {'server': 'web1', 'status': 'active'}
# with open('config.yaml', 'w') as file:
#     yaml.dump(data, file)


with open('config.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)
