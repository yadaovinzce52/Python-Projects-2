import requests
from twilio.rest import Client

endpoint = 'https://api.openweathermap.org/data/3.0/onecall'
api_key = '3c6f9af205d7167ed3c450104c244cc2'
account_sid = 'AC37e61f3ddaabe345e2c182eceea32689'
auth_token = 'f96dab8cf4ee726924ce927d085a343d'

weather_params = {
    'lat': 18.3363,
    'lon': 146.2259,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It is going to rain today! Remember to bring an umbrella!",
            from_='+19207173270',
            to='+18505596306'
        )
    print(message.sid)
