import requests
import json

channel = ""
not_ctrl = []
cntrl = []


try:
    search = requests.post("http://localhost:5279", json={"method": "claim_search", "params": 
    {"channel": "@freestyle", "is_controlling":"false"}}).json()
except:
    pass
try:
    print(search)
except:
    print('search failed')
    pass

version = requests.post("http://localhost:5279", json={"method": "version", "params": {}}).json()
print('im here')
print(version)