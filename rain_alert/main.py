#api_key = ""
import requests
from twilio.rest import Client



twilio_sid = "AC54c57719c83f820195c83df75daa350c"
twilio_auth_token = "7e522177cf092ebab555df9f12df3cd0"
api_key = "621f9e29411625a1c14b604d4e9d38fb"
my_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# Parameters for the API request
parameters = {
    "lat": "6.695070",
    "lon": "-1.615800",
    "appid": api_key,
    "units": "metric",  # for Celsius units
    "cnt": "4"
}

response = requests.get(my_endpoint, params=parameters)
response.raise_for_status
weather_data = response.json()


will_not_rain = False
for hour_data in weather_data["list"]:
    condition_data = hour_data["weather"][0]["id"]
    if int(condition_data) > 700:
        will_not_rain = True
if will_not_rain:
        
        #Create twilio message
        client = Client(twilio_sid, twilio_auth_token)
        message = client.messages.create(
            body="It's not going  to rain today,!",
            from_="+17753694326",
            to= "+233245660786"
        )
        print(message.status)