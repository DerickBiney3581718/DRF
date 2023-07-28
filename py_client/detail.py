import requests
endpoint = "http://localhost:8000/"
get_response = requests.get(endpoint + "api/products/1", )
print(get_response.json()) 