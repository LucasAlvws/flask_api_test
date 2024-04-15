import requests

endpoint = "http://127.0.0.1:8000/api/users/"

data = {"name": "Lucas Alves", "email": "lucas@google.com", "age": 20}

response = requests.post(endpoint, json=data)

print(response.status_code)
print(response.json())
