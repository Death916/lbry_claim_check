import requests
import json

channel = ""
not_ctrl = {}
cntrl = []


try:
    search = requests.post("http://localhost:5279", json={"method": "claim_search", "params": 
    {"channel": "@freestyle"}}).json()
except:
    print('search failed')
    pass


version = requests.post("http://localhost:5279", json={"method": "version", "params": {}}).json()

#print(version)


result = search["result"]["items"]
for claim in result:
    
    if claim["meta"]['is_controlling'] == False:
        not_ctrl = dict(claim)
        amount = not_ctrl['meta']['effective_amount']
        print(amount)  
        title = not_ctrl['value']['title']