
# GAME SECURITY PORTFOLIO
# Project 1: Multiplayer Game Cheat Detection


# creating a dictionary to store player statistics
player = {
    "name": "Summer",
    "kills": 26,
    "deaths": 10,
    "headshots": 4
}

player2 = {
    "name": "Winter",
    "kills": 15,
    "deaths": 12,
    "headshots": 3
}


# players in a list
players = [player, player2]


# function to calculate kill-death ratio
def calculate_kd(kills, deaths):
    return kills / deaths


# displaying player statistics
print("================================")
print("       PLAYER STATISTICS")
print("================================")

for current_player in players:

    # calculating player statistics
    kd = calculate_kd(
        current_player["kills"],
        current_player["deaths"]
    )

    headshot_percentage = (
        current_player["headshots"] / current_player["kills"]
    ) * 100

    # displaying player statistics
    print("Player Name:", current_player["name"])
    print("Kills:", current_player["kills"])
    print("Deaths:", current_player["deaths"])
    print("Headshots:", current_player["headshots"])
    print("Kill-Death Ratio:", round(kd, 2))
    print("Headshot Percentage:", round(headshot_percentage, 2), "%")

    # basic cheat detection logic based on kill-death ratio
    if kd > 5:
        print("Warning: High Kill-Death Ratio detected. Possible cheating behavior.")
    elif kd > 2:
        print("Notice: Kill-Death Ratio is above average. Monitor player behavior.")
    else:
        print("Kill-Death Ratio is within normal range.")

    print("--------------------------------")
