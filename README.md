# Multiplayer Game Cheat Detection

## What it does

This is a cheat detection tool for a shooter game. It uses player statistics to decide whether a player should be reviewed, then prints their statistics along with the outcome. It looks at their current statistics and their headshot history.

## Detection rules

### K/D

The kill to death ratio gives an idea of how skilled a player is. I set the threshold to 5, so a player with more than 5 kills for each death is flagged.

### Headshot percentage

This is how many of a player's kills were headshots. I flag anything over 60%, which I chose as an example value. The current percentage is also compared to the player's average, and they're flagged if it's more than 30 percentage points higher.

Both headshot checks only run when a player has at least 10 kills, so players aren't judged on only a few kills.

## How to run it

From the `game-security-portfolio` folder:

```powershell
python .\01-cheat-detection\main.py
```

## Test results

These are made-up players I used for testing.

| Player | Type | Verdict |
|---|---|---|
| Summer | Sudden headshot spike | Flagged for review: Headshot percentage above 60%; Unusually high headshot percentage compared to average |
| Winter | Typical player | No suspicious activity detected. |
| Autumn | Very few kills | Not enough data to judge headshots |
| Spring | Skilled legit player | Flagged for review: K/D above 5 |
| Season | Sneaky cheater | No suspicious activity detected. |
| Sunny | Brand-new player | Not enough data to judge headshots |

## Limitations

- Players just under the thresholds can avoid review. Season gets through with a K/D of 4.76, 59% headshots and no change from their average.
- Skilled players like Spring can be flagged for having a K/D above 5, because rank and matchmaking aren't considered. A flag means they need reviewing, not that they're cheating.
- Cheaters could stay under 10 kills to avoid the headshot checks. The K/D check still applies to them.

## What I'd improve next

- Compare current K/D with past K/D, so consistently skilled players are less likely to be flagged. This wouldn't catch someone who has always cheated.
- Add rank and matchmaking data to compare players with others at a similar level. Being top of the lobby shouldn't clear someone automatically, since cheaters can be top too.