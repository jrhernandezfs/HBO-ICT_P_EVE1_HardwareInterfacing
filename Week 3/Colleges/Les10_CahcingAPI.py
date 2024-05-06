import requests
from cachecontrol import CacheControl

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    session = requests.session()
    cached_session = CacheControl(session)
    response = cached_session.get(url)
    return response.json()

api_key = 'your_api_key_here'
city = "Amsterdam"

# Eerste aanroep, de data wordt opgehaald en gecachet
weather_data = get_weather(city, api_key)
print(weather_data)

# Tweede aanroep, dezelfde data wordt snel uit de cache gehaald
weather_data_cached = get_weather(city, api_key)
print(weather_data_cached)