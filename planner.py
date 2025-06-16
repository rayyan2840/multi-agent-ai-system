def plan(user_goal):
    if "spacex" in user_goal.lower() and "weather" in user_goal.lower():
        return ["agent1", "agent2", "agent3"]
    else:
        return []
