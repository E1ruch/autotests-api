import httpx

logindata = {
    "email": "1234567@qa.com",
    "password": "123456",
}
response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=logindata)
print(response.json())
tokendata = {
    "accessToken": response.json()['token']['accessToken']
}
print("Получил:",tokendata)

headers = {"Authorization": f"Bearer {tokendata['accessToken']}"}

response = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)

print(response.json())
print(response.status_code)