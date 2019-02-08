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
    return response.json()['response']['serviceTicket']

def getNetworkData():
    token = GetToken()
    print(token)
    url = "https://sandboxapicem.cisco.com/api/v1/reachability-info"
    headers = {'Content-type': 'application/json','X-Auth-Token':token}
    response = requests.get(url,headers=headers,verify=False)
    print(response.json()['response'])
 #   for r in response:
  #      print(r)

getNetworkData()

