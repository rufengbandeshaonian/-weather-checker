import requests

def get_weather(city: str, api_key: str) -> dict:
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()
