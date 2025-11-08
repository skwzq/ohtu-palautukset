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

    print(f"Players from {country}:")

    for player in players:
        if player.nationality == country:
            print(player)

if __name__ == "__main__":
    main()
