from playerreader import PlayerReader
from playerstats import PlayerStats
from rich import print
from rich.prompt import Prompt
from rich.table import Table

def main():
    seasons = [f"20{i}-{i+1}" for i in range(18, 26)]

    season = Prompt.ask("Season", choices=seasons, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationalities = stats.nationalities()

    while True:
        nationality = Prompt.ask("Nationality", choices=nationalities)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Season {season} players from {nationality}")

        table.add_column("name", style="cyan")
        table.add_column("teams", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="yellow")
        table.add_column("games", justify="right", style="red")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points()), str(player.games))

        print(table)

if __name__ == "__main__":
    main()
