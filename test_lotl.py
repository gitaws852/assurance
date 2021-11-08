import requests
import uuid


crId = str(uuid.uuid4())

#def test_lotl():
url = "https://api.bureau.id/v2/auth/initiate?countryCode=IN&callbackUrl=https://en4lssdchkyjk.x.pipedream.net/&clientId=babab5b5-404c-4180-8e49-a24b0c924f3c&transactionId=" + crId+"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
assert response.status_code == 200
print(response.text)
