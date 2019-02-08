import requests
import json
def GetToken():
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    data = {}
    data['username'] = "devnetuser"
    data['password'] = "Cisco123!"
    data= json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data,headers=headers)
    return response.json()

print(GetToken())
