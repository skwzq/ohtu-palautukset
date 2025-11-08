import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    country = input("Print players from: ")

    print(f"\nPlayers from {country}:")

    for player in sorted((p for p in players if p.nationality == country), key=lambda p: p.points(), reverse=True):
        print(player)

if __name__ == "__main__":
    main()
