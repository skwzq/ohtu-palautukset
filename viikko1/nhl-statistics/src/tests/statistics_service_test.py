import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.stats.search("zer")
        self.assertEqual(player.name, "Yzerman")

    def test_search_returns_none_if_no_such_player(self):
        name = self.stats.search("abcd")
        self.assertIsNone(name)

    def test_team_returns_players_of_team(self):
        players = self.stats.team("EDM")
        self.assertSetEqual({player.name for player in players}, {"Semenko", "Kurri", "Gretzky"})

    def test_top_by_points_returns_correct_players(self):
        result = self.stats.top(2)
        self.assertEqual((result[0].name, result[1].name), ("Gretzky", "Lemieux"))

    def test_top_by_goals_returns_correct_players(self):
        result = self.stats.top(2, SortBy.GOALS)
        self.assertEqual((result[0].name, result[1].name), ("Lemieux", "Yzerman"))

    def test_top_by_assists_returns_correct_players(self):
        result = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual((result[0].name, result[1].name), ("Gretzky", "Yzerman"))
