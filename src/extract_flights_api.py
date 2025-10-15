# Fetch data from OpenSky API and write raw JSON
import requests, json

URL = 'https://opensky-network.org/api/states/all'
response = requests.get(URL)
data = response.json()
with open('raw_flights.json', 'w') as f:
    json.dump(data, f, indent=2)
print('Data extracted and saved to raw_flights.json')
