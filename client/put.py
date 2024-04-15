import requests

endpoint = "http://127.0.0.1:8000/api/users/1"

data = {"name": "Lucas Alves 2 teste", "email": "lucas@google.com", "age": 20}

response = requests.put(endpoint, json=data)

print(response.status_code)
print(response.json())
