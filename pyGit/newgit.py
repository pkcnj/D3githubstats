import requests
import json
import time


headers = {'Accept': 'application/vnd.github.v3+json'}


r = requests.get('https://api.github.com/repos/d3/d3/stats/commit_activity', headers=headers)

print(r.url)
fullList = json.dumps(r.json(), indent=2)

print fullList
