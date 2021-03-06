import json
import assurance_connections
import os

sandbox_base_url = "https://api.sandbox.bureau.id/"
production_base_url = "https://api.bureau.id/"

prod_key = os.environ['PROD_API_KEY']
sandbox_key = os.environ['SANDBOX_API_KEY']
test_env = os.environ['env_value']


headers_production = {
  'X-Bureau-Auth-API-Key': prod_key,
  'Content-Type': 'application/json'
}

headers_sandbox = {
  'X-Bureau-Auth-API-Key': sandbox_key,
  'Content-Type': 'application/json'
}
"""
def test_set_params():
	if testing_env == 0:
		base_url = sandbox_base_url
		headers = headers_sandbox
		print("Testing in Sandbox")
	elif testing_env == 1:
		base_url = production_base_url
		headers = headers_production
		print("Testing in Production")
"""

value = str(test_env)

if value == 's':
	print("In this loop")
	base_url = sandbox_base_url
	headers = headers_sandbox
	print("Testing in Sandbox")
elif value == 'p':
	print("In this loop")
	base_url = production_base_url
	headers = headers_production
	print("Testing in Production")

def test_user_name_match_200():
	response = assurance_connections.user_name_match(base_url = base_url, headers = headers)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_user_fetch_signals_200():

	response = assurance_connections.user_fetch_signals(base_url = base_url, headers = headers)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_user_risk_score_200():
	response = assurance_connections.user_risk_score(base_url = base_url, headers = headers)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_user_risk_score_v2_200():
	response = assurance_connections.user_risk_score_v2(base_url = base_url, headers = headers)
	json_response = json.loads(response.text)
	assert response.status_code == 200
