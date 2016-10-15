import requests
import json
token = '0ed42f3dadf8d35e46f449c1ae198824'
r = requests.post('http://challenge.code2040.org/api/haystack', data = {'token': token})
dictt = json.loads(r.text)
needle = dictt['needle']
haystack = dictt['haystack']
i = 0
while i < len(haystack):
    if haystack[i] == needle:
        needlePos = i
        break
    i += 1
newR = requests.post('http://challenge.code2040.org/api/haystack/validate', data = {'token': token, 'needle':needlePos})
