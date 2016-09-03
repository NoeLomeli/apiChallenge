import requests
import json
import iso8601
from datetime import *
from dateutil.relativedelta import *
import dateutil.parser
import datetime as dt


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
# assign interval to interval variable
interval = data['interval']
print date
print interval
# We have to format the datestamp in order to be able to add the seconds interval
date2 = iso8601.parse_date(date)
# create a new datestamp adding the interval of seconds to the original datestamp
addSeconds = date2+relativedelta(seconds = interval)
print addSeconds
# Now we have to convert the datestamp back to iso 8601 format
print unicode(dt.datetime.isoformat(addSeconds)[:-6] + 'Z')

'''
# Last step is to send the new datestamp to this url
sendNewList = 'http://challenge.code2040.org/api/dating/validate'
# We have to create a new dictionary with token and array
result = {"token" : '771da4d993f8dc161eca9b1a951bf50e', "datestamp" : addSeconds}
# Send a post request to upload our dictionary
reqSend = requests.post(sendNewList, json = result)
# The result will confirm that step 3 has been completed
print reqSend.text
'''
