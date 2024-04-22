import unittest

from game.board import Board, CellStatus
from game.logic import GameLogic


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        pass

    def get_populated_board(self) -> 'Board':
        board = Board(6, 7)

        board.drop_piece(2, CellStatus(1))
        board.drop_piece(2, CellStatus(2))
        board.drop_piece(3, CellStatus(1))
        board.drop_piece(1, CellStatus(2))
        board.drop_piece(3, CellStatus(1))
        board.drop_piece(3, CellStatus(2))
        board.drop_piece(4, CellStatus(1))
        board.drop_piece(5, CellStatus(2))
        board.drop_piece(2, CellStatus(1))
        board.drop_piece(2, CellStatus(2))

        return board


    def test_evaluate_diag_pp(self):
        board = self.get_populated_board()
        print(board)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()

