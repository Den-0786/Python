import requests


response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status

data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (longitude, latitude)

print(f"The current position of the International Space Station is at {iss_position}")