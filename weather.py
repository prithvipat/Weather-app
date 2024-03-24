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

# Getting weather data for the upcoming days
def forecast(city_name): 
    base_url = "https://api.openweathermap.org/data/2.5/forecast?"
    params = {
    "q": city_name,
    "appid": "API KEY",
    "units": "metric",
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

# Images based on weather conditions
def images(city_name):
    data = weather(city_name)
    description = f"{data['weather'][0]['description']}"
    word_list = description.split()

    if word_list[-1] == 'snow':
        return 'snow.png'
    
    elif word_list[-1] == 'rain':
        return 'raining.png'
    
    elif word_list[-1] == 'haze':
        return 'sun_moreclouds.png'
    
    elif description == 'scattered clouds':
        return 'sun_clouds.png'
    
    elif word_list[-1] == 'clouds':
        return 'clouds.png'
    
    else: 
        return 'sun.png'
    
def forecast_img(city_name, day):
    data = forecast(city_name)
    description = data['list'][day]['weather'][0]['description']
    word_list = description.split()

    if word_list[-1] == 'snow':
        return 'snow.png'
    
    elif word_list[-1] == 'rain':
        return 'raining.png'
    
    elif word_list[-1] == 'haze':
        return 'sun_moreclouds.png'
    
    elif description == 'scattered clouds':
        return 'sun_clouds.png'
    
    elif word_list[-1] == 'clouds':
        return 'clouds.png'
    
    else: 
        return 'sun.png'


    
