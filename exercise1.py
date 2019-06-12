import requests
import json
import os

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
json_dict = ottawa_wards_response.json()

# [print(key) for key in json_dict.keys()]


areas = json_dict['objects']
[print(area['name']) for area in areas]
   




