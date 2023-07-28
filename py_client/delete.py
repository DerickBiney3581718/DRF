import requests
endpoint = "http://localhost:8000/"
data = {"title": "God save the King"}
get_response = requests.delete(endpoint + "api/products/4/delete/",)
print(get_response.status_code) 
