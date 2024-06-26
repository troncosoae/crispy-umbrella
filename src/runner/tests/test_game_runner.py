import unittest

from game.board import Board
from game.player import Player
from runner.game_runner import GameRunner, GuiType


class TestGameRunner(unittest.TestCase):
    def setUp(self):
        self.player1 = Player()
        self.player2 = Player()
        self.board = Board(6, 7)
        self.game_runner = GameRunner(self.board, self.player1, self.player2, GuiType.TERMINAL)

    def test_run(self):
        # self.game_runner.run()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
