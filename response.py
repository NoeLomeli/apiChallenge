import requests

url = 'http://challenge.code2040.org/api/register'
tokens = {'token' : 'token', 'github' : 'https://github.com/NoeLomeli/apiChallenge'}

r = requests.post(url, json=tokens)

#print(r.text)
