import requests
import json

channel = ""
not_ctrl = {}


# gets list of claims for specific channel
# only correct for for own channel currently

try:
    while True:
        channel = input('please enter a channel name starting with @: ')
        if channel.startswith('@') == False:
            print('enter a valid channel name ')
            channel = input('please enter a channel name starting with @ ')
        if channel.startswith('@') == True:
            break
except:
    print('Enter a valid channel name starting with @')


def claim_search(channel):
    try:
        search = requests.post("http://localhost:5279", json={"method": "claim_search", "params":
                                                              {"channel": channel}}).json()
    except:
        print('search failed')
        pass
    return search


#version = requests.post("http://localhost:5279", json={"method": "version", "params": {}}).json()

# print(version)

# parses the data for relevant info
def get_data(search):

    result = search["result"]["items"]
    for claim in result:
        not_ctrl = dict(claim)
        amount = not_ctrl['meta']['effective_amount']
        title = not_ctrl['value']['title']

        if claim["meta"]['is_controlling'] == False:

            print(amount)
            print('you are not controlling ' + title)
        else:
            print('You are controlling ' + title)


search_result = claim_search(channel)

get_data(search_result)
