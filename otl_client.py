import requests
import json


def otl_auth_initate(base_url, clientId, mobile, correlationId ):
	base_url = base_url
	mobile = mobile
	correlationId = correlationId
	url = base_url + "v2/auth/initiate?" + "correlationId=" + correlationId + "&" + "clientId=" + clientId + "&" + "mobile=" + mobile
	response = requests.request("GET", url)
	return response

def otl_get_userinfo(base_url, headers, correlationId):
	payload={}
	base_url = base_url
	headers = headers
	url = base_url + "v2/auth/userinfo?" + "correlationId=" + correlationId
	response = requests.request("GET", url, headers=headers, data=payload)
	return response
