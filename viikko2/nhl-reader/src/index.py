from rich import print # pylint: disable=redefined-builtin
from rich.prompt import Prompt
from rich.table import Table
from playerreader import PlayerReader
from playerstats import PlayerStats

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
        print_table(season, nationality, players)

def print_table(season, nationality, players):
    table = Table(title=f"Season {season} players from {nationality}")

    columns = [("name", "left", "cyan"), ("teams", "left", "magenta"),
               ("goals", "right", "green"), ("assists", "right", "green"),
               ("points", "right", "yellow"), ("games", "right", "red")]

    for column in columns:
        table.add_column(column[0], justify=column[1], style=column[1])

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists),
                      str(player.points()), str(player.games))

    print(table)

if __name__ == "__main__":
    main()
