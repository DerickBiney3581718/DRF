import requests
endpoint = "http://localhost:8000/"
data = {"title": "Destiny's child yandere"}

get_response = requests.get(endpoint + "api/products/",)
print(get_response.json())
