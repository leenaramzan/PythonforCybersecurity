import requests
import json

url = "https://icanhazdadjoke.com"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Convert json to python object
dadjokes = response.json()

print(dadjokes)

# Print PRETTY json
print(json.dumps(dadjokes, indent=2))
