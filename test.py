import requests

url = "https://your-link.up.railway.app"

# login
r = requests.post(url + "/login", json={
    "username": "admin",
    "password": "1234"
})
print(r.json())

# run
r = requests.post(url + "/run", json={
    "username": "admin"
})
print(r.json())