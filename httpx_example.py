import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.json())
print(response.status_code)

data = {
    "title": "New TASK",
    "completed": False,
    "userId": 1
}

response = httpx.post('https://jsonplaceholder.typicode.com/todos/', json=data)

print(response.json())
print(response.status_code)