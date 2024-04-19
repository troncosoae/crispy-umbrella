from typing import List

from game.board import Board, BoardGetter, CellStatus, Cell

class GameLogic:
    def __init__(self, board: 'Board'):
        self.__board = board
        self.__getter = BoardGetter()

    @property
    def board_cols(self):
        return self.__board.cols

    @property
    def board_rows(self):
        return self.__board.rows

    def __get_board_row(self, row_index: 'int'):
        return self.__getter.get_board_row(self.__board, row_index)

    def __get_board_col(self, col_index: 'int'):
        return self.__getter.get_board_col(self.__board, col_index)

    def __get_board_diag_pp(self, row_index: 'int', col_index: 'int'):
        print(self.__getter.get_board_diag_pos_pos(
            self.__board, row_index, col_index))
        return self.__getter.get_board_diag_pos_pos(
            self.__board, row_index, col_index)

    def __get_board_diag_pn(self, row_index: 'int', col_index: 'int'):
        print(self.__getter.get_board_diag_pos_neg(
            self.__board, row_index, col_index))
        return self.__getter.get_board_diag_pos_neg(
            self.__board, row_index, col_index)

    @staticmethod
    def __evaluate_four(cell_list: 'List[Cell]', cell_status: 'CellStatus') -> bool:
        consecutive_count = 0
        for cell in cell_list:
            if cell.get_status() == cell_status:
                consecutive_count += 1
            else:
                consecutive_count = 0
            if consecutive_count == 4:
                return True
        return False

    def evaluate(self, cell_status: 'CellStatus'):
        pass

    def evaluate_row(self, row_index: 'int', cell_status: 'CellStatus') -> bool:
        return self.__evaluate_four(
            self.__get_board_row(row_index),
            cell_status)

    def evaluate_col(self, col_index: 'int', cell_status: 'CellStatus'):
        return self.__evaluate_four(
            self.__get_board_col(col_index),
            cell_status)
    
    def evaluate_diag_pp(self, row_index: 'int', col_index: 'int', cell_status: 'CellStatus'):
        return self.__evaluate_four(
            self.__get_board_diag_pp(row_index, col_index),
            cell_status)
    
    def evaluate_diag_pn(self, row_index: 'int', col_index: 'int', cell_status: 'CellStatus'):
        return self.__evaluate_four(
            self.__get_board_diag_pn(row_index, col_index),
            cell_status)

