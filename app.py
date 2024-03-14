import requests
from flask import Flask, render_template


def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?={city}"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    wind = data['wind']['speed']
    feels_like = data['main']['feels_like']
    print(f"Weather in {city_name}: {description}, Temperature: {temperature}°C "
          f"Feels Like {feels_like}°C, Wind {wind} KM/H")


if __name__ == "__main__":
    city = input("Enter the city name: ")
    API_KEY = "e08d3f09710e38f079d5b5fd9eea4e6f" 
    get_weather(city, API_KEY)

