import requests
import os
from twilio.rest import Client

MY_LAT = 29.760427
MY_LON = -95.369804
api_key = "7622173cb7e5115a206998e2e5d86421"

account_sid = "AC8d6e81afbcaba7e94b4f1834dafb84de"
auth_token = "a956b69e108d6dc121b8b1142f72f695"

# account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]

#1----------SMS Sending----------------------
def send_sms():
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="Hello, it's going to rain to day. ",
                        from_='+18556430691',
                        to='+18322432370'
                    )

    print(message.status)
    
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

will_rain = False 

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"][0:13]
for item in hourly_data:
    weather_id = hourly_data[0]["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    send_sms()