from typing import List
from random import choice as random_choice


from game.board import Board, CellStatus
from game.player import Player, PlayerAction


class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
    
    def get_action(
            self, valid_inputs: List[int], board: Board,
            cell_status: CellStatus) -> PlayerAction:
        return PlayerAction(
            self.id, random_choice(valid_inputs))

