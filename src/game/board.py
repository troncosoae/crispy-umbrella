# TODO: Use inheritance to fix the Board interface. 

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
                return True
        return False
    
    def drop_piece(self, col: int, piece_status: 'CellStatus'):
        assert self.evaluate_drop_piece(col)
        for row in range(self.rows - 1, -1, -1):
            if self.__board[row][col].get_status() == CellStatus(0):
                self.__board[row][col].insert_piece(piece_status)
                break



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
    
    def insert_piece(self, new_status: 'CellStatus'):
        print(type(new_status))
        self.__status.set_status(new_status.get_status())
        assert self.__status == new_status
    
    def get_status(self) -> 'CellStatus':
        return self.__status

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
    
    def __eq__(self, other: 'object'):
        assert(isinstance(other, CellStatus))
        return self.__status == other.__status
    
    def __ne__(self, other: 'object'):
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

    
    
