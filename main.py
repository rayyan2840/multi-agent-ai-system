from planner import plan
from agents.agent1 import fetch_next_launch
from agents.agent2 import fetch_launchpad_location
from agents.agent3 import fetch_weather

def main():
    user_goal = input("Enter your goal: ")

    steps = plan(user_goal)

    if steps == ["agent1", "agent2", "agent3"]:
        print("\nFetching next SpaceX launch...")
        launch_name, launch_date, launch_location_id = fetch_next_launch()

        print("\nFetching launchpad location...")
        location_name, latitude, longitude = fetch_launchpad_location(launch_location_id)

        print("\nFetching weather at launch location...")
        weather_description, temperature = fetch_weather(latitude, longitude)

        print("\n--- Final Summary ---")
        print(f"Launch: {launch_name}")
        print(f"Launch Date: {launch_date}")
        print(f"Launch Location: {location_name}")
        print(f"Weather: {weather_description}, {temperature}°C")

        if "rain" in weather_description.lower() or "storm" in weather_description.lower():
            print("⚠️ Weather might delay the launch.")
        else:
            print("✅ Weather looks good for launch.")

    else:
        print("Goal not recognized or not supported yet.")

if __name__ == "__main__":
    main()
