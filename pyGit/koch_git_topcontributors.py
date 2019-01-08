import requests
import json

headers = {'Accept': 'application/vnd.github.v3+json'}


r = requests.get('https://api.github.com/repos/d3/d3/contributors', headers=headers)

print(r.url)

fullList = json.loads(r.content)


for i in fullList:
    unameList = i['login']
    contribsList = i['contributions']
    print (unameList, contribsList)