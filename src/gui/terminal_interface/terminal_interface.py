from typing import List

from game.board import Board, CellStatus
from game.player import Player, PlayerAction
from gui.base_interface import BaseGUI


class TerminalPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
    
    def get_action(
            self, valid_inputs: List[int], board: Board,
            cell_status: CellStatus) -> PlayerAction:
        command_request_str = "Player %s, the column to insert your chip: " % self.id

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
        
        return PlayerAction(self.id, int_value)


class TerminalGUI(BaseGUI):

    def __init__(self, board: 'Board'):
        BaseGUI.__init__(self, board)

    def print_init_banner(self) -> None:
        print("Starting terminal GUI...")

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
            player: Player,
            valid_inputs: List[int],
            cell_status: CellStatus) -> PlayerAction:
        command_request_str = "Player %s, the column to insert your chip: " % str(player)

        return player.get_action(valid_inputs, self.board, cell_status)

    def print_winner(self, player: Player) -> None:
        print(f"Player {player.id} wins!")


