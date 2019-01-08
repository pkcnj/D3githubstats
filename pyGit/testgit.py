import requests
import json
from datetime import datetime



headers = {'Accept': 'application/vnd.github.v3+json'}


r = requests.get('https://api.github.com/repos/d3/d3/stats/commit_activity', headers=headers)

print(r.url)

fullList = json.loads(r.content)


for i in fullList:
    weekList = i['week']
    timeList = datetime.fromtimestamp(weekList).strftime('%Y-%m-%d')
    dayList = i['days']
    totalList = i['total']
    print (str(dayList), str(totalList), str(timeList))

