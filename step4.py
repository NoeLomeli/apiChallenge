import requests
import json

# this is the endpoint that will give us the dictionary
retrieveDictionary = 'http://challenge.code2040.org/api/prefix'

# The endpoint will be expecting a token so we have to create a dictionary
token = {"token" : '771da4d993f8dc161eca9b1a951bf50e'}
# Next step is to send a post request
req = requests.post(retrieveDictionary, json=token)
# this is the dictionary that is being returned to us
print req.text, "\n"
# We have to convert the dictionary to json
data = json.loads(req.text)
# assign the key to value
value = data['prefix']
# assign the array to array
array = data['array']
print value
print  array
