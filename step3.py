import requests
import json

# this is the endpoint that will give us the dictionary
retrieveDictionary = 'http://challenge.code2040.org/api/haystack'

# The endpoint will be expecting a token so we have to create a dictionary
token = {"token" : '771da4d993f8dc161eca9b1a951bf50e'}
# Next step is to send a post request
req = requests.post(retrieveDictionary, json=token)
# this is the dictionary that is being returned to us
print req.text, "\n"
