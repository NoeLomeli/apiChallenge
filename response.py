import requests
import json


url = 'http://challenge.code2040.org/api/register'
#test = 'token'
tokens = {'token' : '771da4d993f8dc161eca9b1a951bf50e' , 'github' : 'https://github.com/NoeLomeli/apiChallenge'}

r = requests.post(url, json=tokens)


#r = requests.post(url, data = {'token' : test, 'github' : 'https://github.com/NoeLomeli/apiChallenge'})
print(r.text)
