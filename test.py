import requests

url = "https://myserver-production-0c1f.up.railway.app"

r = requests.post(url + "/login", json={
    "username": "admin",
    "password": "1234"
})
print(r.json())

r = requests.post(url + "/run", json={
    "username": "admin"
})
print(r.json())