import requests
import os

url = "https://ennzbpev4mlci.x.pipedream.net/"

payload = ""
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
