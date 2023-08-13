# Video Game Competition
# Mark Joshwel - SXXXXXXXX

player = ["Hafu", "Toast", "Pokimane", "Pewdiepie", "Ninja", "Markiplier"]

results = [
    [98, 107, 87, 121],
    [88, 111],
    [79, 130, 99],
    [86, 100, 121, 66, 98],
    [108, 79, 92],
    [77, 126, 93, 100, 73, 89],
]

print("Player       Games Wins Total")

for player_name, player_result in zip(player, results):
    games = len(player_result)
    wins = len([s for s in player_result if s >= 100])
    total = sum(player_result)

    print(f"{player_name:<12} {games:^5} {wins:^4} {total:^5}")
