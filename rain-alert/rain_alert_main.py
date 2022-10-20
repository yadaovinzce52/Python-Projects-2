import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

endpoint = 'https://api.openweathermap.org/data/3.0/onecall'
api_key = os.environ.get('OWM_API_KEY')
account_sid = os.environ.get('ACC_SID')
auth_token = os.environ.get('AUTH_TOKEN')

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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="It is going to rain today! Remember to bring an umbrella!",
            from_=os.environ.get('TWIL_PHONE'),
            to=os.environ.get('PHONE')
        )
    print(message.sid)
