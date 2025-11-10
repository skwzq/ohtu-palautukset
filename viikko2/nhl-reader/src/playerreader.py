import requests
from player import Player

class PlayerReader(): # pylint: disable=too-few-public-methods
    def __init__(self, url):
        self.response = requests.get(url, timeout=1).json()

    def get_players(self):
        players = []

        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)

        return players
