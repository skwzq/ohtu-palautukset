class PlayerStats():
    def __init__(self, reader):
        self.players = reader.get_players()

    def nationalities(self):
        return list(set(player.nationality for player in self.players))

    def top_scorers_by_nationality(self, country):
        return sorted((p for p in self.players if p.nationality == country), key=lambda p: p.points(), reverse=True)
