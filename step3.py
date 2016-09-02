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
# We have to convert the dictionary to json
data = json.loads(req.text)
# assign the key to value
value = data['needle']
# assign the array to array
array = data['haystack']
# This line iterates through the array to find the needle
index = array.index(value)
# print index to confirm the result is correct
print index
# this is the url where we will send our result to be validated
sendIndex = 'http://challenge.code2040.org/api/haystack/validate'
# We have to create a new dictionary with token and needle keys
result = {"token" : '771da4d993f8dc161eca9b1a951bf50e', 'needle' : index}
# Send a post request to upload our dictionary
reqSend = requests.post(sendIndex, json = result)
# The result will confirm that step 3 has been completed
print reqSend.text
