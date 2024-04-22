from typing import List

from game.board import Board
from game.player import Player, PlayerAction
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

    def get_player_action(
            self,
            player: 'Player',
            valid_inputs: 'List[int]') -> PlayerAction:
        command_request_str = "Player %s, the column to insert your chip: " % str(player)

        input_is_valid = False

        while not input_is_valid:
            value = input(command_request_str)

            try:
                int_value = int(value)
            except ValueError:
                print("The value inserted isn't a number")
                continue

            if int_value in valid_inputs:
                input_is_valid = True
            else:
                print("This input isn't within the valid inputs")

        return PlayerAction(player.id, int_value)

