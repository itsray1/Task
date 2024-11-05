import requests

endpoint="http://localhost:8000/api/tasks/3/update/"

data={
   "title":"test",
   "complete":"true"
   
}
get_response= requests.put(endpoint,json=data) 
print(get_response.json())

