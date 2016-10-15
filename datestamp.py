import requests
import json
token = '0ed42f3dadf8d35e46f449c1ae198824'
r = requests.post('http://challenge.code2040.org/api/dating', data = {'token': token})
dictt = json.loads(r.text)
datestamp = dictt['datestamp']
interval = dictt['interval']
#assuming interval does not exceed a month's worth of seconds

year = datestamp[0:4]
month = datestamp[5:7]
day = datestamp[8:10]
hour = datestamp[11:13]
minute = datestamp[14:16]
second = datestamp[17:19]

interSecs = int(interval)%60
totalMin = (int(interval)-interSecs)/60
interMin = totalMin%60
totalHours = (totalMin-interMin)/60
interHours = totalHours%24
totalDays = (totalHours-interHours)/24
interDays = totalDays%24

if int(second)+interSecs >= 60:
    second = str((int(second)+interSecs)%60)
    minute = str(int(minute)+1)
else:
    second = str(int(second)+interSecs)
if int(second) < 10:
    second = '0'+second

if int(minute)+interMin >= 60:
    minute = str((int(minute)+interMin)%60)
    hour = str(int(hour)+1)
else:
    minute = str(int(minute)+interMin)
if int(minute) < 10:
    minute = '0'+minute
if int(hour)+interHours >= 24:
    hour = str((int(hour)+interHours)%24)
    day = str(int(day)+1)
else:
    hour = str(int(hour)+interHours)
if int(hour) < 10:
    hour = '0'+hour

day = str(int(day)+interDays)
newDate = year + '-'+ month + '-' + day + 'T'+hour+':'+minute+':'+second+'Z'

newR = requests.post('http://challenge.code2040.org/api/dating/validate', data = {'token': token, 'datestamp':newDate})
print(newR.text)
