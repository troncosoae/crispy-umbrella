class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = self._init_board_representation()
    
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
    
    def evaluate_drop_piece(self, col: int):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col].status == CellStatus(0):
                return True
        return False
    
    def drop_piece(self, col: int, player):
        assert self.evaluate_drop_piece(col)
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col].status == CellStatus(0):
                self.board[row][col].insert_piece(player)
                break



class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.status = CellStatus()
    
    def is_valid(self):
        return self.status.is_valid()
    
    def __str__(self):
        return str(self.status)
    
    def __repr__(self):
        return self.__str__()
    
    def insert_piece(self, player):
        self.status.set_status(player)

class CellStatus:
    def __init__(self, status=0):
        self.status = status
    
    def __str__(self):
        if self.status == 0:
            return "_"
        elif self.status == 1:
            return "X"
        elif self.status == 2:
            return "O"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other: 'CellStatus'):
        return self.status == other.status
    
    def __ne__(self, other: 'CellStatus'):
        return self.status != other.status
    
    def is_valid(self):
        return self.status == 0 or \
            self.status == 1 or \
            self.status == 2
    
    def set_status(self, status):
        self.status = status

    
    