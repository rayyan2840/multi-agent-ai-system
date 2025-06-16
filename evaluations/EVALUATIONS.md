### Step 1: Planner
Input: User goal: "Find the next SpaceX launch and check its weather"
Planner decides: Call SpaceX Agent

### Step 2: SpaceX Agent
Input: (None, SpaceX API call)
Output: Next launch: Falcon 9, Location: LC-39A, Kennedy Space Center
Planner receives location.

### Step 3: Planner
Planner decides: Call Weather Agent with launchpad coordinates.

### Step 4: Weather Agent
Input: Coordinates from SpaceX Agent
Output: Weather: Cloudy, Wind Speed: 5 m/s, Temperature: 22°C

### Step 5: Planner
Planner summarizes the final result:
"Launch is scheduled, weather is favorable."
