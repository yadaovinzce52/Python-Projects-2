import requests

api_key = '3c6f9af205d7167ed3c450104c244cc2'

weather_params = {
    'lat': 30.438255,
    'lon': -84.280731,
    'appid': api_key
}

response = requests.get('https://api.openweathermap.org/data/3.0/onecall', params=weather_params)
print(response.json())

