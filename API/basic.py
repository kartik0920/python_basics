"""
I am going to start working on API
Library used: request
"""

import requests

lat = 19.619548
lon = 74.66
token = "b3152064895630b2a5c93190e4fb41a9"

url = (
    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={token}"
)

response = requests.get(url=url)

data = response.json()
