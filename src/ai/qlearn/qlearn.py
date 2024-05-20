from typing import List
from random import choice as random_choice
import torch

from game.player import Player, PlayerAction
from game.board import CellStatus, Board
from ai.qlearn.brain import Brain
from ai.qlearn.specific_models import SampleModel


class QLearnBoardTranslator():
    def __init__(self) -> None:
        pass

    def __map_cell_status(self, status: CellStatus) -> int:
        if status == CellStatus(0):
            return 0
        elif status == CellStatus(1):
            return 1
        elif status == CellStatus(2):
            return -1
        else:
            raise Exception("Inconsistent CellStatus")

    def convert(self, board: Board) -> torch.Tensor:
        row_count: int = board.rows
        col_count: int = board.cols
        tensor_result = torch.empty((row_count, col_count)) 
        for col in range(col_count):
            for row in range(row_count):
                tensor_result[row][col] = \
                    self.__map_cell_status(
                        board.board[row][col].get_status())
        return tensor_result


class QLearningPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.__translator = QLearnBoardTranslator()
        self.__brain = Brain(SampleModel())

    def get_action(
            self, valid_inputs: List[int], board: Board,
            next_status: CellStatus) -> PlayerAction:

        move = random_choice(valid_inputs)

        print(board)
        t = self.__translator.convert(board)
        print(t)

        probs = self.__brain.run(t)
        print(probs)
        print(len(probs))

        print(valid_inputs)
        for i, el in enumerate(probs[0]):
            print(i, el)
            if i not in valid_inputs:
                print("%d not in valid" % i)
                probs[0][i] = 0

        print(probs)

        best_move = self.__brain.choose_by_dist(probs)
        print(type(best_move))
        print(best_move)
        



        return PlayerAction(
            self.id, best_move)

