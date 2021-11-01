import pytest
import json
import otl_client
import os
import uuid

sandbox_base_url = "https://api.sandbox.bureau.id/"
production_base_url = "https://api.bureau.id/"

sandbox_key =  os.environ['SANDBOX_API_KEY']
sandbox_client = os.environ['SANDBOX_CLIENT_ID']

headers_sandbox = {
  'X-Bureau-Auth-API-Key': sandbox_key,
  'Content-Type': 'application/json'
}

client_id_sandbox = sandbox_client

valid_mobile_number = str(779999999995)
invalid_mobile_number = str(9999999995)

crId = str(uuid.uuid4())
crId1 = crId[:-3]


# otl sandbox auth intiate call - gives success response
def test_otl_auth_initate_200():
	response = otl_client.otl_auth_initate(base_url = sandbox_base_url, clientId = client_id_sandbox, mobile = valid_mobile_number,
	correlationId = crId)
	assert response.status_code == 200

# otl sandbox get user info call - gives success response
def test_otl_get_userinfo_200():
	response = otl_client.otl_get_userinfo(base_url = sandbox_base_url, headers = headers_sandbox,
	correlationId = crId)
	assert response.status_code == 200

# otl sandbox auth intiate with existing correlation ID - throws error
def test_otl_auth_initate_400():
	response = otl_client.otl_auth_initate(base_url = sandbox_base_url, clientId = client_id_sandbox, mobile = valid_mobile_number,
	correlationId = crId)
	assert response.status_code == 400 


# otl sandbox auth initate with incorrect phone number
def test_otl_auth_initiate_incorrect_phone_number_400():
	response = otl_client.otl_auth_initate(base_url = sandbox_base_url, clientId = client_id_sandbox, mobile = invalid_mobile_number,
	correlationId = crId1)
	assert response.status_code == 400
