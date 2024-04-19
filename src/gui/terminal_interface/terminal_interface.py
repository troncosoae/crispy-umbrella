from game.board import Board
from gui.base_interface import BaseGUI 


class TerminalGUI(BaseGUI):

    def __init__(self, board: 'Board'):
        BaseGUI.__init__(self, board)

    def print_board(self):
        board_str = "    "
        for i in range(self.board.cols):
            board_str += str(i) + " "
        board_str += "\n"
        board_str += "  +"
        for i in range(self.board.cols):
            board_str += "--"
        board_str += "\n"
        for (i, row) in enumerate(self.board.board):
            board_str += str(i) + " | "
            for cell in row:
                board_str += str(cell) + " "
            board_str += "\n"
        print(board_str)

    def get_player_action(self):
        print("x")
        

