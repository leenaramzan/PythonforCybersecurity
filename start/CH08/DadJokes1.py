import requests

url = "https://icanhazdadjoke.com"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
