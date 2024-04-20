import unittest

from game.board import Board
from runner.game_runner import GameRunner, GuiType


class TestGameRunner(unittest.TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        self.game_runner = GameRunner(self.board, GuiType.TERMINAL)

    def test_run(self):
        self.game_runner.run()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
