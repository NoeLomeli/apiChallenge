import requests
import json

# this is the endpoint that will give us the string that needs to be reversed
retrieveString = 'http://challenge.code2040.org/api/reverse'

# The endpoint will be expecting a token so we have to create a dictionary
token = {"token" : '771da4d993f8dc161eca9b1a951bf50e'}
# Next step is to send a post request
req = requests.post(retrieveString, json=token)
# this is the string that is being returned to us
print req.text, "\n"
# This line will reverse the string
reverseString = req.text[::-1]
# Print this line just to make sure we are getting a reversed string
print reverseString

# Once we have the reversed string we have to send it back to this url
sendString = 'http://challenge.code2040.org/api/reverse/validate'
# We create another dictionary that includes our reversed string
revString = {"token" : '771da4d993f8dc161eca9b1a951bf50e' , "string" : reverseString}
# We make another post request to submit our result
result = requests.post(sendString, json=revString)
# This message will tell us step 2 is complete
print result.text
