
import requests
from dotenv import load_dotenv

load_dotenv()

def weather(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather?={city}"
    params = {
        "q": city_name,
        "appid": "e08d3f09710e38f079d5b5fd9eea4e6f",
        "units": "metric",
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data