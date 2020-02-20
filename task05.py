import requests
import json
import re

def getnetworkdevicecount():
	
	controller='sandboxapic.cisco.com'
	
	url='https://devnetapi.cisco.com/sandbox/apic_em/api/v1/ticket'

	payload = {"username":"devnetuser","password":"Cisco123!"}

	header = {"content-type": "application/json"}

	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
	
	r_json=response.json()
	
	ticket = r_json["response"]["serviceTicket"]

	url = "https://" + controller + "/api/v1/host?limit=1&offset=1"

	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	response = requests.get(url, headers=header, verify=False)
	
	data = json.dumps(response.json())
	data = json.loads(data)
	
	data = data["response"][0]
	
	q = 0
	for i in data.keys():
		if re.findall("Mac",i) != []:
			q += 1
	
	
	print(f"the count of network devices is {q}")
	return q

getnetworkdevicecount()	
		