import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/todos'

response = requests.get(BASE_URL)

data = response.json()

print(data)