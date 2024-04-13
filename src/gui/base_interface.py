from game.board import Board


class BaseGUI:
    def __init__(self, board: 'Board'):
        self.board = board

    def print_board(self):
        raise NotImplementedError("This is an abstract class we should never call this method")

    def get_player_action(self):
        raise NotImplementedError("This is an abstract class we should never call this method")

