import os
import json

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string)

# print(parsed_json['first_name'])

"""
Takes in a filename as input (JSON)
Returns the parsed dictionary
"""
def parseFiles(filename):
    with open('strings.json') as fileData:
        d = json.load(fileData)
        print(d)
