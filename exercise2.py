import requests
import json
import os

postal_codes_response = requests.get('https://represent.opennorth.ca/postcodes/L5G4L3/?sets=federal-electoral-districts')
json_dict = postal_codes_response.json()

print(type(json_dict))
