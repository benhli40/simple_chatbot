import requests

def get_weather(location):
    with open("weather_key.txt", "r") as key_file:
        api_key = key_file.read().strip()

    base_url = "http://api.accuweather.com/locations/v1/search"
    params = {
        "apikey": api_key,
        "q": location,
    }
    response = requests.get(base_url, params=params)
    location_data = response.json()

    if location_data:
        location_key = location_data[0]['Key']

        weather_url = f"http://api.accuweather.com/currentconditions/v1/{location_key}"
        params = {
            "apikey": api_key,
            "details": "true",
        }
        response = requests.get(weather_url, params=params)
        weather_data = response.json()

        if weather_data:
            return weather_data[0]

    return None