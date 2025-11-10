class Player:
    def __init__(self, dict_):
        self.name = dict_['name']
        self.nationality = dict_['nationality']
        self.assists = dict_['assists']
        self.goals = dict_['goals']
        self.team = dict_['team']
        self.games = dict_['games']

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return (f'{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = '
                f'{self.points():3} points from {self.games:2} games')
