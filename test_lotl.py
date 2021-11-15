import requests
import uuid


crId = str(uuid.uuid4())

#def test_lotl():
#url = "https://api.bureau.id/v2/auth/initiate?&mobile=779999999995&countryCode=IN&callbackUrl=https://ent4nlzguowt.x.pipedream.net/&clientId=ebd5ed12-5e42-4f30-b793-056d44af9d19&transactionId=" + crId
url = "https://api.sandbox.bureau.id/v2/auth/initiate?&callbackUrl=https://ent4nlzguowt.x.pipedream.net/&clientId=ebd5ed12-5e42-4f30-b793-056d44af9d19&transactionId=" + crId + "&mobile=919845045249"
payload={}
headers = {}
print(url)
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
print(response.status_code)
