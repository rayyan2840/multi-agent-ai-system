def planner(user_goal):
    """
    Simple planner that decides which agents to run based on the user goal.
    """
    if "SpaceX" in user_goal and "weather" in user_goal:
        return ["spacex_agent", "weather_agent"]
    else:
        print("Planner could not understand the goal.")
        return []
    
import requests

def spacex_agent():
    """
    Calls the SpaceX API to get the next launch details.
    """
    url = "https://api.spacexdata.com/v4/launches/next"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        launch_name = data['name']
        launch_date = data['date_utc']
        launch_location = data['launchpad']

        return {
            'launch_name': launch_name,
            'launch_date': launch_date,
            'launch_location_id': launch_location
        }
    else:
        print("Failed to get launch data from SpaceX API.")
        return None

def get_launchpad_location(launchpad_id):
    """
    Gets the location name and coordinates using the launchpad ID.
    """
    url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location_name = data['name']
        latitude = data['latitude']
        longitude = data['longitude']

        return {
            'location_name': location_name,
            'latitude': latitude,
            'longitude': longitude
        }
    else:
        print("Failed to get launchpad location.")
        return None
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def weather_agent(latitude, longitude):
    """
    Calls the OpenWeatherMap API to get the weather at the given coordinates.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']

        return {
            'weather_description': weather_description,
            'temperature': temperature
        }
    else:
        print("Failed to get weather data.")
        return None

def run_multi_agent_system():
    """
    Runs the full multi-agent system.
    """
    user_goal = input("Enter your goal: ")

    agent_sequence = planner(user_goal)

    if agent_sequence == ["spacex_agent", "weather_agent"]:
        # Run SpaceX agent
        spacex_data = spacex_agent()
        if spacex_data:
            # Get launchpad location
            location_data = get_launchpad_location(spacex_data['launch_location_id'])
            if location_data:
                # Run weather agent
                weather_data = weather_agent(location_data['latitude'], location_data['longitude'])
                if weather_data:
                    # Final output
                    print("\n=== Mission Summary ===")
                    print(f"Next Launch: {spacex_data['launch_name']}")
                    print(f"Launch Date: {spacex_data['launch_date']}")
                    print(f"Launch Location: {location_data['location_name']}")
                    print(f"Weather: {weather_data['weather_description']}, {weather_data['temperature']}°C")

                    # Simple weather check
                    if "rain" in weather_data['weather_description'].lower() or "storm" in weather_data['weather_description'].lower():
                        print("Warning: Launch may be delayed due to bad weather.")
                    else:
                        print("Weather looks good for launch!")
                else:
                    print("Weather data not available.")
            else:
                print("Launch location not found.")
        else:
            print("Launch data not available.")

if __name__ == "__main__":
    run_multi_agent_system()
