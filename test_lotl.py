import requests
import uuid


crId = str(uuid.uuid4())

def test_lotl():

  url = "https://api.bureau.id/v2/auth/initiate?countryCode=IN&callbackUrl=https://en4lssdchkyjk.x.pipedream.net/&clientId=" + crId + "&transactionId=a15facc8-0f38-46f4-bac8&mobile=919845045249"
  payload={}
  headers = {}
  response = requests.request("GET", url, headers=headers, data=payload)
  assert response.status_code == 200
  print(response.text)
