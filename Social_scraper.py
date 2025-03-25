import requests

username = "target_user"
url = f"https://www.instagram.com/{username}/?__a=1"

response = requests.get(url)
data = response.json()

print(f"User Info: {data}"
