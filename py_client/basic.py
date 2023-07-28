import requests
endpoint = "http://localhost:8000/"
get_response = requests.get(endpoint + "api/",json={"title":'123'} )
print(get_response.json()) 