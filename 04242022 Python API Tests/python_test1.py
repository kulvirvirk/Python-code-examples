import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
print(response)     # print the response from the endpoint 

# response.json() returns a JSON object of the result.
# (if the result was written in JSON format, if not it raises an error). 
# Python requests are generally used to fetch the content from a particular resource URI.

#print(response.json()['items']) 


# use for loop on dictionary to access JSON > items > title
for questions in (response.json()['items']):
    print (questions['title'])
