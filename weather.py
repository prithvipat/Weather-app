import requests
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.openweathermap.org/data/2.5/weather?{city}"
def weather(city_name):
    params = {
        "q": city_name,
        "appid": "API KEY",
        "units": "metric",
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError:
        print("City doesn't exists")
        return('Error')
    
    return data
