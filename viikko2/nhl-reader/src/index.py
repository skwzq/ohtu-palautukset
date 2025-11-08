from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    country = input("Print players from: ")
    players = stats.top_scorers_by_nationality(country)

    print(f"\nPlayers from {country}:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
