import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_weather(latitude, longitude):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return weather_description, temperature
    else:
        raise Exception("Failed to fetch weather data.")
