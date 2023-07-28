import requests
endpoint = "http://localhost:8000/"
data = {"title": "God save the King"}
get_response = requests.put(endpoint + "api/products/1/update/", json=data )
print(get_response.json()) 