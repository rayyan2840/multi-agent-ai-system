import requests

def fetch_next_launch():
    url = "https://api.spacexdata.com/v4/launches/next"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        launch_name = data['name']
        launch_date = data['date_utc']
        launch_location_id = data['launchpad']
        return launch_name, launch_date, launch_location_id
    else:
        raise Exception("Failed to fetch SpaceX launch data.")
