import httpx
from tools.fakers import get_random_email

createdata = {
  "email": get_random_email(),
  "password": "123456",
  "lastName": "qaqa",
  "firstName": "vlados",
  "middleName": "gengen"
    }
create_response = httpx.post('http://localhost:8000/api/v1/users', json=createdata)
create_response.json()
print(create_response.status_code)

auth_data = {
    "email": createdata['email'],
    "password": createdata['password'],
}
auth_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=auth_data)
tokendata = {
    "accessToken": auth_response.json()['token']['accessToken']
}
headers = {"Authorization": f"Bearer {tokendata['accessToken']}"}
print(auth_response.status_code)

patch_user_data = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
user_id = create_response.json()['user']['id']
user_patch = httpx.patch(f'http://localhost:8000/api/v1/users/{user_id}', headers=headers, json=patch_user_data)
print(user_patch.status_code)
print(user_patch.json())














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