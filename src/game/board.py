from typing import Tuple
# TODO: Use inheritance to fix the Board interface. 


class CellStatus:
    def __init__(self, status=0):
        self.__status = status
    
    def __str__(self):
        if self.__status == 0:
            return "_"
        elif self.__status == 1:
            return "X"
        elif self.__status == 2:
            return "O"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other: 'CellStatus'):
        assert(isinstance(other, CellStatus))
        return self.__status == other.__status
    
    def __ne__(self, other: 'CellStatus'):
        assert(isinstance(other, CellStatus))
        return self.__status != other.__status
    
    def is_valid(self):
        return self.status == 0 or \
            self.__status == 1 or \
            self.__status == 2
    
    def get_status(self) -> int:
        return self.__status
    
    def set_status(self, status: int) -> None:
        self.__status = status



class Cell:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__status = CellStatus()
    
    def is_valid(self):
        return self.status.is_valid()
    
    def __str__(self):
        return str(self.__status)
    
    def __repr__(self):
        return self.__str__()
    
    def insert_piece(self, new_status: CellStatus):
        # print(type(new_status))
        self.__status.set_status(new_status.get_status())
        assert self.__status == new_status
    
    def get_status(self) -> CellStatus:
        return self.__status
    

    

class Board:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__board = self._init_board_representation()
    
    def _init_board_representation(self):
        return [[Cell(row, col) for col in range(self.cols)] for row in range(self.rows)]
    
    def __str__(self):
        board_str = "  "
        for i in range(self.cols):
            board_str += str(i) + " "
        board_str += "\n"
        for (i, row) in enumerate(self.board):
            board_str += str(i) + " "
            for cell in row:
                board_str += str(cell) + " "
            board_str += "\n"
        return board_str
    
    def __repr__(self):
        return self.__str__()

    @property
    def cols(self):
        return self.__cols

    @property
    def rows(self):
        return self.__rows

    @property
    def board(self):
        return self.__board

    def evaluate_drop_piece(self, col: int):
        for row in range(self.rows - 1, -1, -1):
            if self.__board[row][col].get_status() == CellStatus(0):
                # print("found spot")
                return True
        return False
    
    def drop_piece(self, col: int, piece_status: CellStatus) -> Tuple[int, int]:
        assert self.evaluate_drop_piece(col)
        for row in range(self.rows - 1, -1, -1):
            if self.__board[row][col].get_status() == CellStatus(0):
                self.__board[row][col].insert_piece(piece_status)
                return (row, col)
        assert False


class BoardGetter:
    def __init__(self):
        pass

    def get_board_col(self, board: Board, col_index: int):
        assert col_index < board.cols
        return [row[col_index] for row in board.board]

    def get_board_row(self, board: Board, row_index: int):
        assert row_index < board.rows
        return board.board[row_index]

    def get_board_diag_pos_pos(self, board: Board, row_index: int, col_index: int):
        assert row_index < board.rows
        assert col_index < board.cols

        # print("row_index: %d, col_index: %d" % (row_index, col_index))

        while (row_index > 0 and col_index > 0):
            row_index -= 1
            col_index -= 1
        
        # print("row_index: %d, col_index: %d" % (row_index, col_index))

        range_size = board.rows - row_index if \
                board.rows - row_index < board.cols - col_index else \
                board.cols - col_index

        # print("range_size: %d" % range_size)

        return [board.board[row_index + i][col_index + i]
            for i in range(range_size)]


    def get_board_diag_pos_neg(self, board: Board, row_index: int, col_index: int):
        assert row_index < board.rows
        assert col_index < board.cols

        # print("row_index: %d, col_index: %d" % (row_index, col_index))

        while (row_index < (board.rows - 1) and col_index > 0):
            row_index += 1
            col_index -= 1
        
        # print("row_index: %d, col_index: %d" % (row_index, col_index))

        range_size = row_index + 1 if \
                row_index + 1 < board.cols - col_index else \
                board.cols - col_index

        # print("range_size: %d" % range_size)

        return [board.board[row_index - i][col_index + i]
            for i in range(range_size)]

