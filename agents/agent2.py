import requests

def fetch_launchpad_location(launch_location_id):
    url = f"https://api.spacexdata.com/v4/launchpads/{launch_location_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location_name = data['name']
        latitude = data['latitude']
        longitude = data['longitude']
        return location_name, latitude, longitude
    else:
        raise Exception("Failed to fetch launchpad location.")
