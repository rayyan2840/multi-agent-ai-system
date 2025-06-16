import requests
from dotenv import load_dotenv
import os

# Load the API key from .env file
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Ask user for city name
city = input("Enter the city name: ")

# Build the API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send GET request to the API
response = requests.get(url)

# Check if the API call was successful
if response.status_code == 200:
    print("API call successful!")

   # Convert the response to JSON
    data = response.json()

    # Extract weather information
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    weather_description = data['weather'][0]['description']
    city_name = data['name']

    # Display the weather information
    print(f"\nWeather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Description: {weather_description}")

else:
    if response.status_code == 404:
        print("City not found. Please enter a valid city name.")
    else:
        print(f"API call failed with status code: {response.status_code}")
    if response.status_code == 404:
        print("City not found. Please enter a valid city name.")
    else:
        print(f"API call failed with status code: {response.status_code}")

    # Optional: Ask user to retry
    retry = input("Do you want to try again? (yes/no): ")
    if retry.lower() == 'yes':
        # You can run the file again or wrap your code in a loop later
        print("Please restart the program and try again.")
    else:
        print("Exiting the program.")



