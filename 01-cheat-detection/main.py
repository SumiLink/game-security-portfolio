
# GAME SECURITY PORTFOLIO
# Project 1: Multiplayer Game Cheat Detection

# creating a dictionary to store player statistics
player = {
    "name": "Summer",
    "kills": 30,
    "deaths": 10,
    "headshots": 20,
    "headshot_history": [20, 25, 22, 24, 53]
}

player2 = {
    "name": "Winter",
    "kills": 15,
    "deaths": 12,
    "headshots": 3,
    "headshot_history": [18, 20, 19, 27, 21]
}

player3 = {
    "name": "Autumn",
    "kills": 2,
    "deaths": 1,
    "headshots": 2,
    "headshot_history": [20, 22, 19]
}

# players in a list
players = [player, player2, player3]

# function to calculate kill-death ratio
def calculate_kd(kills, deaths):
    return kills / max(deaths, 1)  # prevent division by zero

#function for calculating headshot percentage
def calculate_headshot_percentage(headshots, kills):
    return (headshots / kills) * 100 if kills else 0

#function to check if a player has a high kill-death ratio
def check_high_kd(kd):
    return kd > 5

#function to check if a player has a high headshot percentage
def check_high_headshot_percentage(headshot_percentage):
    return headshot_percentage > 60

#function to calculate average headshot percentage
def calculate_average(values):
    return sum(values) / len(values) if values else None #if average is none, skip difference check

#function to calculate the difference between current headshot percentage and average headshot percentage
def calculate_difference(current, average):
    return current - average

#function to check if the difference is unusually high, in this case 30% or more 
def check_unusual_performance(difference):
    return difference > 30

#checking if the player has enough kills to make a judgment on their headshot percentage
def check_enough_kills(kills):
    return kills >= 10


# displaying player statistics
print("================================")
print("       PLAYER STATISTICS")
print("================================")

#for loop to go through each player and calculate their statistics
for current_player in players:

    #checking players average headshot percentage
    player_average = calculate_average(current_player["headshot_history"])

    #calculating current headshot percentage and kill-death ratio
    current_headshot_percentage = calculate_headshot_percentage(
        current_player["headshots"],
        current_player["kills"]
    )

    #calculating kill-death ratio
    kd = calculate_kd(
        current_player["kills"],
        current_player["deaths"]
    )

    # fresh list of reasons for each player
    reasons = []
    if check_high_kd(kd):
        reasons.append("K/D above 5")

    difference = None  # initialize difference variable

    # checking if the player has enough kills to make a judgment on their headshot percentage and giving reason for review
    if check_enough_kills(current_player["kills"]):

        if check_high_headshot_percentage(current_headshot_percentage):
            reasons.append("Headshot percentage above 60%")

        if player_average is not None:
            difference = calculate_difference(current_headshot_percentage, player_average)
            if check_unusual_performance(difference):
                reasons.append("Unusually high headshot percentage compared to average")

    # displaying player statistics
    print("Player Name:", current_player["name"])
    print("Kills:", current_player["kills"])
    print("Deaths:", current_player["deaths"])
    print("Headshots:", current_player["headshots"])
    print("Kill-Death Ratio:", round(kd, 2))
    print("Headshot Percentage:", round(current_headshot_percentage, 2), "%")

    # displaying average headshot percentage and difference if available
    if player_average is not None:
        print("Average Headshot Percentage:", round(player_average, 2), "%")
    else:
        print("No headshot history yet.")

    if difference is not None:
        print("Difference from Average:", round(difference, 2), "percentage points")

    # displaying reasons for review if any
    if reasons:
        print("Flagged for review:", ", ".join(reasons))
    else:
        print("No suspicious activity detected.")

    # giving reason for not being able to judge off headshots
    if not check_enough_kills(current_player["kills"]):
        print("Not enough data to judge headshots")

    print("--------------------------------")