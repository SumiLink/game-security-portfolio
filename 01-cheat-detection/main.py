
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


# players in a list
players = [player, player2]

# function to calculate kill-death ratio
def calculate_kd(kills, deaths):
    return kills / deaths

#function for calculating headshot percentage
def calculate_headshot_percentage(headshots, kills):
    return (headshots / kills) * 100

#function to check if a player has a high kill-death ratio
def check_high_kd(kd):
    return kd > 5

#function to check if a player has a high headshot percentage
def check_high_headshot_percentage(headshot_percentage):
    return headshot_percentage > 60

#function to calculate average headshot percentage
def calculate_average(values):
    return sum(values) / len(values)

#function to calculate the difference between current headshot percentage and average headshot percentage
def calculate_difference(current, average):
    return current - average

#function to check if the difference is unusually high, in this case 30% or more 
def check_unusual_performance(difference):
    return difference > 30


# displaying player statistics
print("================================")
print("       PLAYER STATISTICS")
print("================================")

# iterating through the players list to calculate and display statistics for each player
for current_player in players:

    player_average = calculate_average(current_player["headshot_history"])

    current_headshot_percentage = calculate_headshot_percentage(
        current_player["headshots"],
        current_player["kills"]
    )

    difference = calculate_difference(
        current_headshot_percentage,
        player_average
    )

    unusual_performance = check_unusual_performance(difference)

    # calculating player statistics
    kd = calculate_kd(
        current_player["kills"],
        current_player["deaths"]
    )

    headshot_percentage = calculate_headshot_percentage(
        current_player["headshots"],
        current_player["kills"]
    )

#defining what a suspicious player is based on high kill-death ratio or high headshot percentage
    high_kd = check_high_kd(kd)
    high_headshots = check_high_headshot_percentage(headshot_percentage)
    suspicious_player = high_kd or high_headshots or unusual_performance

    # displaying player statistics
    print("Player Name:", current_player["name"])
    print("Kills:", current_player["kills"])
    print("Deaths:", current_player["deaths"])
    print("Headshots:", current_player["headshots"])
    print("Kill-Death Ratio:", round(kd, 2))
    print("Headshot Percentage:", round(headshot_percentage, 2), "%")
    print("Average Headshot Percentage:", round(player_average, 2), "%")
    print("Difference from Average:", round(difference, 2), "%")

    # basic cheat detection logic based on kill-death ratio
    if suspicious_player:
        print("WARNING! Suspicious player detected!")
    else:
        print("No suspicious activity detected.")

    print("--------------------------------")
