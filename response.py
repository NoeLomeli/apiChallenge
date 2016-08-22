import requests
import json


url = 'http://challenge.code2040.org/api/register'

#tokens = {'token' : string, 'github' : 'https://github.com/NoeLomeli/apiChallenge'}

#r = requests.post(url, json=tokens)
test = 'http://challenge.code2040.org/api/register'

r = requests.post(url, data = {'token' : test, 'github' : 'https://github.com/NoeLomeli/apiChallenge'})
print(r.text)
