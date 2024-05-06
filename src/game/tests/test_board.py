import unittest

from game.board import Board, Cell, CellStatus, BoardGetter

class TestBoard(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_starting_board(self):
        board = Board(6, 7)
        self.assertEqual(board.rows, 6)
        self.assertEqual(board.cols, 7)
    
    def test_drop_piece(self):
        board = Board(6, 7)
        board.drop_piece(0, CellStatus(1))
        self.assertEqual(board.board[5][0].get_status(), CellStatus(1))

        board.drop_piece(0, CellStatus(2))
        self.assertEqual(board.board[4][0].get_status(), CellStatus(2))

        board.drop_piece(1, CellStatus(1))
        self.assertEqual(board.board[5][1].get_status(), CellStatus(1))
    
    def test_fail_on_drop_piece(self):
        board = Board(6, 7)
        board.drop_piece(0, CellStatus(1))
        board.drop_piece(0, CellStatus(2))
        board.drop_piece(0, CellStatus(1))
        board.drop_piece(0, CellStatus(2))
        board.drop_piece(0, CellStatus(1))
        board.drop_piece(0, CellStatus(2))
        self.assertFalse(board.evaluate_drop_piece(0))

        with self.assertRaises(AssertionError):
            board.drop_piece(0, CellStatus(1))
    
    def get_populated_board(self) -> 'Board':
        board = Board(6, 7)

        board.drop_piece(0, CellStatus(1))
        board.drop_piece(0, CellStatus(2))
        board.drop_piece(0, CellStatus(1))
        board.drop_piece(0, CellStatus(2))
        board.drop_piece(0, CellStatus(1))
        board.drop_piece(0, CellStatus(2))

        board.drop_piece(1, CellStatus(1))
        board.drop_piece(1, CellStatus(2))
        board.drop_piece(1, CellStatus(1))
        board.drop_piece(1, CellStatus(2))
        board.drop_piece(1, CellStatus(1))
        board.drop_piece(1, CellStatus(2))

        board.drop_piece(2, CellStatus(1))
        board.drop_piece(2, CellStatus(2))
        board.drop_piece(2, CellStatus(1))
        board.drop_piece(2, CellStatus(2))

        board.drop_piece(3, CellStatus(1))
        board.drop_piece(3, CellStatus(2))
        board.drop_piece(3, CellStatus(1))
        board.drop_piece(3, CellStatus(2))

        board.drop_piece(4, CellStatus(1))
        board.drop_piece(4, CellStatus(2))

        return board

    def test_get_board_column(self):
        board = self.get_populated_board()
        board_getter = BoardGetter()

        col0 = board_getter.get_board_col(board, 0)

        row_index = 0
        for cell in col0:
            self.assertEqual(type(cell), Cell)
            self.assertEqual(type(cell.get_status()), CellStatus)
            if row_index % 2 == 0:
                self.assertEqual(cell.get_status(), CellStatus(2))
            else:
                self.assertEqual(cell.get_status(), CellStatus(1))

            row_index += 1

    
    def test_get_board_row(self):
        board = self.get_populated_board()
        board_getter = BoardGetter()

        row0 = board_getter.get_board_row(board, 5)

        col_index = 0
        for cell in row0:
            self.assertEqual(type(cell), Cell)
            self.assertEqual(type(cell.get_status()), CellStatus)
            if col_index <= 4:
                self.assertEqual(cell.get_status(), CellStatus(1))
            else:
                self.assertEqual(cell.get_status(), CellStatus(0))

            col_index += 1
        
        row1 = board_getter.get_board_row(board, 4)
        col_index = 0
        for cell in row1:
            self.assertEqual(type(cell), Cell)
            self.assertEqual(type(cell.get_status()), CellStatus)
            if col_index <= 4:
                self.assertEqual(cell.get_status(), CellStatus(2))
            else:
                self.assertEqual(cell.get_status(), CellStatus(0))
            
            col_index += 1
    
    def test_get_board_diag_pos_pos(self):
        board = self.get_populated_board()
        board_getter = BoardGetter()

        diag = board_getter.get_board_diag_pos_pos(board, 2, 2)
        self.assertEqual(len(diag), 6)

        diag = board_getter.get_board_diag_pos_pos(board, 0, 6)
        self.assertEqual(len(diag), 1)

        diag = board_getter.get_board_diag_pos_pos(board, 5, 0)
        self.assertEqual(len(diag), 1)

        diag = board_getter.get_board_diag_pos_pos(board, 3, 0)
        self.assertEqual(len(diag), 3)

        self.assertEqual(
            board_getter.get_board_diag_pos_pos(board, 0, 0),
            board_getter.get_board_diag_pos_pos(board, 5, 5))
        
        self.assertEqual(
            board_getter.get_board_diag_pos_pos(board, 1, 0),
            board_getter.get_board_diag_pos_pos(board, 4, 3))
        
        diag = board_getter.get_board_diag_pos_pos(board, 1, 0)
        index = 0
        for cell in diag:
            if index % 2 == 0:
                self.assertEqual(cell.get_status(), CellStatus(1))
            else:
                self.assertEqual(cell.get_status(), CellStatus(2))
            index += 1
    
    def test_get_board_diag_pos_neg(self):
        board = self.get_populated_board()
        board_getter = BoardGetter()
        print(board)

        diag = board_getter.get_board_diag_pos_neg(board, 0, 0)
        self.assertEqual(len(diag), 1)

        diag = board_getter.get_board_diag_pos_neg(board, 2, 2)
        self.assertEqual(len(diag), 5)

        diag = board_getter.get_board_diag_pos_neg(board, 0, 1)
        self.assertEqual(len(diag), 2)

        diag = board_getter.get_board_diag_pos_neg(board, 1, 0)
        self.assertEqual(len(diag), 2)

        diag = board_getter.get_board_diag_pos_neg(board, 5, 6)
        self.assertEqual(len(diag), 1)

        diag = board_getter.get_board_diag_pos_neg(board, 5, 2)
        self.assertEqual(len(diag), 5)

        diag = board_getter.get_board_diag_pos_neg(board, 3, 6)
        self.assertEqual(len(diag), 3)

        diag = board_getter.get_board_diag_pos_neg(board, 0, 6)
        self.assertEqual(len(diag), 6)

        self.assertEqual(
            board_getter.get_board_diag_pos_neg(board, 0, 6),
            board_getter.get_board_diag_pos_neg(board, 2, 4))
        
        self.assertEqual(
            board_getter.get_board_diag_pos_neg(board, 1, 6),
            board_getter.get_board_diag_pos_neg(board, 3, 4))
        
        diag = board_getter.get_board_diag_pos_neg(board, 1, 6)
        self.assertEqual(diag[0].get_status(), CellStatus(1))
        self.assertEqual(diag[1].get_status(), CellStatus(2))
        self.assertEqual(diag[2].get_status(), CellStatus(0))
        self.assertEqual(diag[3].get_status(), CellStatus(0))
        self.assertEqual(diag[4].get_status(), CellStatus(0))
        
        diag = board_getter.get_board_diag_pos_neg(board, 1, 0)
        self.assertEqual(diag[0].get_status(), CellStatus(1))
        self.assertEqual(diag[1].get_status(), CellStatus(2))

        self.assertEqual(
            board_getter.get_board_diag_pos_neg(board, 3, 0),
            board_getter.get_board_diag_pos_neg(board, 0, 3))


if __name__ == "__main__":
    unittest.main()

