import requests
import json

def user_name_match(base_url, headers):
	base_url = base_url
	headers = headers
	url = base_url + "v1/users/match"
	print(url)
	payload = json.dumps({
		"attributes": {
		"name": "Varun Arora",
		"phone": "910000000000",
		"email": "abcdn619n@gmail.com"
		}
		})
	print(payload)
	response = requests.request("POST", url, headers=headers, data=payload)
	print("user_name_match")
	print(json.loads(response.text))
	return response

def user_fetch_signals(base_url, headers):
	base_url = base_url
	headers = headers
	url = base_url + "v1/users/fetch-signals"
	payload = json.dumps({
		"signal": [
		"mno"
		],
		"attributes": {
		"phone": "919900099000"
		}
		})
	response = requests.request("POST", url, headers=headers, data=payload)
	print("user_fetch_signals")
	print(json.loads(response.text))
	return response

def user_risk_score(base_url, headers):
	base_url = base_url
	headers = headers
	url = base_url + "v1/users/risk-score"
	payload = json.dumps({
		"attributes": {
		"name": "test",
		"phone": "919900099000",
		"accountEvent": "create"
		}
		})
	response = requests.request("POST", url, headers=headers, data=payload)
	print("user_risk_score")
	print(json.loads(response.text))
	return response

def user_risk_score_v2(base_url, headers):
	url = base_url + "v2/users/risk-score"
	payload = json.dumps({
		"attributes": {
		"name": "test",
		"phone": "919900099000",
		"email": "test@gmail.com",
		"address": {
		"address1": "koramangala",
		"address2": "koramangala",
		"country": "India",
		"city": "Bengalurur",
		"postalCode": "560034"
		},
		"accountEvent": "create"
		}
		})
	response = requests.request("POST", url, headers=headers, data=payload)
	print("user_risk_score_v2")
	print(json.loads(response.text))
	return response


