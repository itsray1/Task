import requests

endpoint="http://localhost:8000/api/tasks/"

data={
    "title":"test",
}
get_response= requests.post(endpoint,json=data) 
print(get_response.json())



