import requests
import os
from twilio.rest import Client


MY_LAT = 29.760427
MY_LON = -95.369804
api_key = "7622173cb7e5115a206998e2e5d86421"

TWILIO_ACCOUNT_SID = "AC8d6e81afbcaba7e94b4f1834dafb84de"
TWILIO_AUTH_TOKEN = "7b79ff8eaab747e5d2c60fdfa2d8303f"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

#1----------SMS Sending----------------------
def send_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
                    .create(
                        body="Ngan oi, It's going to rain today. Remember to bring an umberlla nha. ",
                        from_='+18556430691',
                        to='+8322432370'
                    )

    print(message.sid)
    
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

will_rain = False 

respone = requests.get(OWN_Endpoint, params=weather_params)
respone.raise_for_status()
data = respone.json()
hourly_data = data["hourly"][0:13]
for item in hourly_data:
    weather_id = hourly_data[0]["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    send_sms()

