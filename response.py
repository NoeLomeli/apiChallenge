import requests
import json

# Noe Lomeli
# code2040 API challenge
# August 22, 2016



# To get started, you are first going to connect to the registration endpoint
# the endpoint can be found in this URL
url = 'http://challenge.code2040.org/api/register'

# The registration endpoint expects a JSON dictionary with two keys
# We will name the first key 'token' and the value is a string that has been provided to us.
# The second key is 'github' and we assign the url to our github repo
tokens = {'token' : '771da4d993f8dc161eca9b1a951bf50e' , 'github' : 'https://github.com/NoeLomeli/apiChallenge'}

#  The registration endpoint is going to be expecting you to use POST to send your JSON.
r = requests.post(url, json=tokens)

print(r.text)
