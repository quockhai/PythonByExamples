#!/usr/bin/env python3

import json
import ssl
from urllib.request import urlopen
# import requests

class objectFile(object):
    categoryId = 0
    fileName = ''
    materialNames = ['']
    scale = 0.005
    title = ''

    def __init__(self, data):
	    self.__dict__ = json.loads(data)

ssl._create_default_https_context = ssl._create_unverified_context

response = urlopen('https://api.npoint.io/0620c352c41ab71a8c92')

json_data = json.load(response)

# print(data)
print(json.dumps(json_data, indent=4, sort_keys=True))
print(json_data['title'])

for object in json_data['objects']:
    tempObject = objectFile(json.dumps(object))
    print(tempObject.title)
    # print(object['title'])