import unittest
from src.statistics_service import StatisticsService
from src.player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_existing_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")

    def test_search_non_existing_player(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_players(self):
        edm_players = self.stats.team("EDM")
        # Stubissa on 3 EDM-pelaajaa: Semenko, Kurri, Gretzky
        self.assertEqual(len(edm_players), 3)
        names = [p.name for p in edm_players]
        self.assertIn("Kurri", names)
        self.assertIn("Gretzky", names)
        self.assertIn("Semenko", names)

    def test_top_scorers(self):
        top = self.stats.top(2)
        # Gretzkyllä eniten pisteitä (124), sitten Lemieux (99)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
