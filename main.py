import requests

MY_LAT = 29.760427
MY_LON = -95.369804
api_key = "7622173cb7e5115a206998e2e5d86421"

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
    print("Bring un Umbrella. ")