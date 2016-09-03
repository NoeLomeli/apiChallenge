import requests
import json
import dateutil.parser
import datetime
import iso8601
from datetime import *; from dateutil.relativedelta import *

# this is the endpoint that will give us the dictionary
retrieveDictionary = 'http://challenge.code2040.org/api/dating'

# The endpoint will be expecting a token so we have to create a dictionary
token = {"token" : '771da4d993f8dc161eca9b1a951bf50e'}
# Next step is to send a post request
req = requests.post(retrieveDictionary, json=token)
# this is the dictionary that is being returned to us
print req.text, "\n"
# We have to convert the dictionary to json
data = json.loads(req.text)
# assign the datestamp to date
date = data['datestamp']
interval = data['interval']
print date
print interval
# We have to format the datestamp in order to be able to add the seconds interval
date2 = iso8601.parse_date(date)
addSeconds = date2+relativedelta(seconds = interval)

print date2
print addSeconds
