import requests
import json
import os

countries_response = requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json')
countries = countries_response.json()


# canada = countries['Canada']

canada = list(filter(lambda x: x['name'] == 'Canada', countries))[0]
print(type(canada))
gov = canada['legislatures'][0]
url = gov['popolo_url']

politicians_response = requests.get(url)
politicians = politicians_response.json()

name = politicians['persons'][0]['given_name']
print(name)
