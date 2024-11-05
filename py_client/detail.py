import requests

task_id=input("id=")
try:
    task_id=int(task_id)
except:
    task_id=None
    print(f'{task_id} not a valid id')  
if task_id:    
    endpoint=f"http://localhost:8000/api/tasks/{task_id}/"


get_response= requests.get(endpoint) 
print(get_response.json())

