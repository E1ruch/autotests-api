import httpx


login_payload = {
    "email": "1234567@qa.com",
    "password": "123456",
}
response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)


print(response.json())
print(response.status_code)

refresh_payload = {
    "refreshToken": response.json()['token']['refreshToken']
}
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
print(refresh_response.json())