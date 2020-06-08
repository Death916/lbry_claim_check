import requests
import json

channel = ""
not_ctrl = {}
cntrl = []

def claim_search(channel):
    try:
        search = requests.post("http://localhost:5279", json={"method": "claim_search", "params": 
        {"channel": "@freestyle"}}).json()
    except:
        print('search failed')
        pass
    return search


version = requests.post("http://localhost:5279", json={"method": "version", "params": {}}).json()

#print(version)

def get_data(search):
    
    result = search["result"]["items"]
    for claim in result:
        
        if claim["meta"]['is_controlling'] == False:
            not_ctrl = dict(claim)
            amount = not_ctrl['meta']['effective_amount']
            print(amount)  
            title = not_ctrl['value']['title']
            print(title)

search_result = claim_search(channel)

get_data(search_result)
