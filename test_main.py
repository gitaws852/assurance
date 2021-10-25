import pytest
import json
import assurance_connections
import os

sandbox_base_url = "https://api.sandbox.bureau.id/"
production_base_url = "https://api.bureau.id/"

prod_key = os.environ['PROD_API_KEY']
sandbox_key = os.environ['SANDBOX_API_KEY']

headers_production = {
  'X-Bureau-Auth-API-Key': prod_key,
  'Content-Type': 'application/json'
}

headers_sandbox = {
  'X-Bureau-Auth-API-Key': sandbox_key,
  'Content-Type': 'application/json'
}

def test_sandbox_user_name_match_200():
	response = assurance_connections.user_name_match(base_url = sandbox_base_url, headers = headers_sandbox)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_sandbox_user_fetch_signals_200():
	response = assurance_connections.user_fetch_signals(base_url = sandbox_base_url, headers = headers_sandbox)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_sandbox_user_risk_score_200():
	response = assurance_connections.user_risk_score(base_url = sandbox_base_url, headers = headers_sandbox)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_sandbox_user_risk_score_v2_200():
	response = assurance_connections.user_risk_score_v2(base_url = sandbox_base_url, headers = headers_sandbox)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_production_user_name_match_200():
	response = assurance_connections.user_name_match(base_url = production_base_url, headers = headers_production)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_production_user_fetch_signals_200():
	response = assurance_connections.user_fetch_signals(base_url = production_base_url, headers = headers_production)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_production_user_risk_score_200():
	response = assurance_connections.user_risk_score(base_url = production_base_url, headers = headers_production)
	json_response = json.loads(response.text)
	assert response.status_code == 200

def test_production_user_risk_score_v2_200():
	response = assurance_connections.user_risk_score_v2(base_url = production_base_url, headers = headers_production)
	json_response = json.loads(response.text)
	assert response.status_code == 200
