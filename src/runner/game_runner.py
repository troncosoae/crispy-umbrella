from enum import Enum

from game.board import Board, CellStatus
from game.logic import GameLogic
from game.player import Player
from gui.terminal_interface.terminal_interface import TerminalGUI, TerminalPlayer
from gui.base_interface import BaseGUI


class GuiType(Enum):
    TERMINAL = 1



class GameRunner:
    def __init__(
            self,
            board: 'Board',
            player1: 'Player',
            player2: 'Player',
            gui_type: 'GuiType'):
        self.__board = board
        self.__init_gui(gui_type)
        self.__init_player_map(player1, player2)
        self.__logic = GameLogic(self.__board)

    def __init_gui(self, gui_type: 'GuiType'):
        if gui_type == GuiType.TERMINAL:
            self.__gui = TerminalGUI(self.__board)
        else:
            raise AssertionError("GUI type indicated doesn't exist")

    def __init_player_map(self, player1: 'Player', player2: 'Player'):
        self.__player_cell_status_map = {
            player1.id: 1,
            player2.id: 2}

        self.__player_map = {
            player1.id: player1,
            player2.id: player2}

        self.__player_array = [player1.id, player2.id]

    def __get_player_from_turn_count(self, turn_count: 'int') -> 'Player':
        result = self.__player_map.get(
            self.__player_array[turn_count % 2], None)
        if result is None:
            raise AssertionError("This player id isn't recorded in the game. ")
        return result

    def __get_cell_status_from_player(self, player: 'Player') -> 'CellStatus':
        return CellStatus(self.__player_cell_status_map.get(player.id))

    @property
    def __player1_id(self) -> int:
        return self.__player_array[0]

    @property
    def __player2_id(self) -> int:
        return self.__player_array[1]

    @property
    def player1_cell_status_value(self) -> int:
        result = self.__player_cell_status_map.get(
            self.__player1_id, None)
        if result is None:
            raise AssertionError("This player id isn't recorded in the game. ")
        return result

    @property
    def player2_cell_status_value(self) -> int:
        result = self.__player_cell_status_map.get(
            self.__player2_id, None)
        if result is None:
            raise AssertionError("This player id isn't recorded in the game. ")
        return result
    
    def __evaluate_win(
            self, col_index: int, row_index: int, cell_status: CellStatus) -> bool:
        return self.__logic.evaluate_row(row_index, cell_status) or \
            self.__logic.evaluate_col(col_index, cell_status) or \
            self.__logic.evaluate_diag_pp(row_index, col_index, cell_status) or \
            self.__logic.evaluate_diag_pn(row_index, col_index, cell_status)

    def run(self):
        print("Starting terminal GUI...")

        have_winner = False
        turn_count = 0

        valid_inputs = [i for i in range(7)]

        self.__gui.print_board()

        while not have_winner:
            active_player = self.__get_player_from_turn_count(turn_count)

            filtered_valid_inputs = [
                i for i in valid_inputs
                if self.__board.evaluate_drop_piece(i)]
            
            # print(filtered_valid_inputs)


            player_action = self.__gui.get_player_action(active_player, filtered_valid_inputs)

            final_position = self.__board.drop_piece(
                player_action.col_index,
                self.__get_cell_status_from_player(active_player))
            
            # print(final_position)

            if self.__evaluate_win(
                    final_position[1],
                    final_position[0],
                    self.__get_cell_status_from_player(active_player)):
                print(f"Player {active_player.id} wins!")
                have_winner = True
            
            turn_count += 1

            self.__gui.print_board()


def run():

    banner = "Connect 4!"
    print(banner)

    board = Board(6, 7)

    player1 = TerminalPlayer()
    player2 = TerminalPlayer()

    gui_type = GuiType.TERMINAL
    runner = GameRunner(board, player1, player2, gui_type)
    runner.run()

