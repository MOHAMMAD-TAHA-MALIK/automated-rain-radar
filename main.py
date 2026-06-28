import requests
from twilio.rest import Client
Account_SID = "YOUR KEY"
AUTH_TOKEN = "YOUR AUTHORIZATION TOKEN"
PHN_NO = "PHN NO"

KEY = "YOUR OWN KEY"
LATITUDE = 34.083672
LONGITUDE = 74.797279
params = {
    "lat" : LATITUDE,
    "lon" : LONGITUDE,
    "appid" : KEY,
    "cnt" : 4 
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=params)
response.raise_for_status()
data = response.json()


print(data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in data["list"] :
    condition_code = hour_data["weather"][0]["id"] 
    if (condition_code) < 700 :
        will_rain = True
      
if will_rain :
    client = Client(Account_SID, AUTH_TOKEN)
    message = client.messages.create(
    body="today is going to rain",
    from_=PHN_NO,
    to="OWN NO",
)

print(message.status)

