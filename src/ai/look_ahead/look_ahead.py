from typing import List, Tuple, Dict
from copy import deepcopy
from random import choice as random_choice
from enum import Enum
import threading
import time
import sys

from game.board import Board, BoardGetter, CellStatus
from game.player import Player, PlayerAction
from game.logic import GameLogic

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def console_think(**kwargs):
    event = kwargs["event"]
    event.clear()

    spinner = spinning_cursor()
    while not event.is_set():
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')


# This class must be able to identify winning opportunities
# which are N moves ahead. 
class LookAheadPlayer(Player):

    def __init__(self, look_ahead_depth=4) -> None:
        super().__init__()
        # Set logic with empty board
        self.__logic = GameLogic(Board())
        self.__getter = BoardGetter()
        self.__look_ahead_depth = look_ahead_depth
        self.__think_is_done = threading.Event()

    def __get_valid_inputs(self, board: Board) -> List[int]:
        input_range: List[int] = [i for i in range(board.cols)]

        return [i for i in input_range
                if board.evaluate_drop_piece(i)]

    def __choose_best_move(
            self, board: Board, next_status: CellStatus, search_depth: int,
            moves_memory: List[int]) -> CellStatus:
        self.__logic.set_board(board)

        # The last element in moves_memory is also the next move
        move = moves_memory[-1]
        other_status = \
            CellStatus(1) if next_status.get_status() == 2 else CellStatus(2)

        assert next_status.get_status() != 0

        assert board.evaluate_drop_piece(move)
        final_position: Tuple[int, int] = board.drop_piece(
                move, next_status)

        have_winner: bool = self.__logic.evaluate_win_with_status(
                final_position[0],
                final_position[1],
                next_status)

        if have_winner:
            return next_status

        if search_depth > self.__look_ahead_depth:
            return CellStatus(0)

        next_valid_moves: List[int] = self.__get_valid_inputs(
                board)
        next_moves_results: Dict[int, CellStatus] = {}
        for move in next_valid_moves:
            board_copy = deepcopy(board)
            moves_memory_copy = deepcopy(moves_memory)
            moves_memory_copy.append(move)

            next_moves_results[move] = \
                    self.__choose_best_move(
                        board=board_copy,
                        next_status=other_status,
                        search_depth=search_depth+1,
                        moves_memory=moves_memory_copy)

        
        # print(board)
        current_always_wins: bool = True
        for move, result in next_moves_results.items():
            # print(moves_memory, move, result)
            if result == other_status:
                return other_status
            elif result == CellStatus(0):
                current_always_wins = False

        if current_always_wins:
            return next_status

        return CellStatus(0)

    def __logic_to_get_action(
            self, valid_inputs: List[int], board: Board,
            next_status: CellStatus) -> int:

        next_moves_results: Dict[int, CellStatus] = {}
        for move in valid_inputs:
            board_copy = deepcopy(board)
            assert board_copy.evaluate_drop_piece(move)

            next_moves_results[move] = \
                    self.__choose_best_move(
                        board=board_copy,
                        next_status=next_status,
                        search_depth=2,
                        moves_memory=[move])

        # print("board on which to make decision!")
        # print(board)

        random_choice_options: List[int] = []
        for move, result in next_moves_results.items():
            # print(move, result)
            if result == next_status:
                return move
            elif result == CellStatus(0):
                random_choice_options.append(move)

        if len(random_choice_options) == 0:
            # print("Already lost!")
            random_choice_options = valid_inputs

        # print("random_choice_options", random_choice_options)
        # print("Choosing randomly!")
        return random_choice(random_choice_options)


    def get_action(
            self, valid_inputs: List[int], board: Board,
            next_status: CellStatus) -> PlayerAction:

        console_think_thread = threading.Thread(
                target=console_think,
                kwargs={"event": self.__think_is_done})
        console_think_thread.start()

        move = self.__logic_to_get_action(
                valid_inputs, board, next_status)

        self.__think_is_done.set()

        console_think_thread.join()
        print()

        return PlayerAction(
            self.id, move)

