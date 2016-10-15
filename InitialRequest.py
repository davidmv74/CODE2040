import requests
r = requests.post('http://challenge.code2040.org/api/register', data = {'token':'0ed42f3dadf8d35e46f449c1ae198824', 'github':'https://github.com/davidmv74/CODE2040'})
print(r.url, r.text)
