import requests
import os

response = requests.get("http://localhost:12434/models/run")
print(response.json())

