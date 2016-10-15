import requests
token = '0ed42f3dadf8d35e46f449c1ae198824'
r = requests.post('http://challenge.code2040.org/api/reverse', data = {'token': token})
word = r.text
reverse = []
i = len(word)-1
while i >= 0:
    reverse.append(word[i])
    i -= 1
reverse = ''.join(reverse)

newR = requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token': token, 'string':reverse})
print(newR.text)
