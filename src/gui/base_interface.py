from typing import List

from game.board import Board
from game.player import Player, PlayerAction


class BaseGUI:
    def __init__(self, board: 'Board'):
        self.board = board

    def print_board(self) -> None:
        raise NotImplementedError("This is an abstract class we should never call this method")

    def get_player_action(
            self,
            player: 'Player',
            valid_inputs: 'List[int]') -> PlayerAction:
        raise NotImplementedError("This is an abstract class we should never call this method")

