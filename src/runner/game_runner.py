from enum import Enum
from typing import List

from game.board import Board, CellStatus
from game.logic import GameLogic
from game.player import Player, PlayerAction
from gui.terminal_interface.terminal_interface import TerminalGUI, TerminalPlayer
from gui.base_interface import BaseGUI
from ai.random.random_ai import RandomPlayer
from ai.look_ahead.look_ahead import LookAheadPlayer
from ai.qlearn.qlearn import QLearningPlayer


class GuiType(Enum):
    TERMINAL = 1



class BaseGameRunner:
    def __init__(
            self,
            board: Board,
            player1: Player,
            player2: Player,
            gui_type: GuiType):
        self.__board = board
        self.__init_gui(gui_type)
        self.__init_player_map(player1, player2)
        self.__logic = GameLogic(self.__board)

    def __init_gui(self, gui_type: GuiType) -> None:
        if gui_type == GuiType.TERMINAL:
            self.__gui = TerminalGUI(self.__board)
        else:
            raise AssertionError("GUI type indicated doesn't exist")

    def __init_player_map(self, player1: Player, player2: Player) -> None:
        self.__player_cell_status_map = {
            player1.id: 1,
            player2.id: 2}

        self.__player_map = {
            player1.id: player1,
            player2.id: player2}

        self.__player_array = [player1.id, player2.id]

    def __get_player_from_turn_count(self, turn_count: int) -> Player:
        result = self.__player_map.get(
            self.__player_array[turn_count % 2], None)
        if result is None:
            raise AssertionError("This player id isn't recorded in the game. ")
        return result

    def __get_cell_status_from_player(self, player: Player) -> CellStatus:
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
        return self.__logic.evaluate_win_with_status(row_index, col_index, cell_status)

    @property
    def valid_inputs(self) -> List[int]:
        return [i for i in range(self.__board.cols)]

    def run(self) -> None:
        raise NotImplementedError("This is an abstract class we should never call this method")


class SimpleGameRunner(BaseGameRunner):
    def __init__(
            self,
            board: Board,
            player1: Player,
            player2: Player,
            gui_type: GuiType):
        BaseGameRunner.__init__(
            self, board, player1, player2, gui_type)

    def run(self) -> None:
        self._BaseGameRunner__gui.print_init_banner()
        self._BaseGameRunner__gui.print_board()

        have_winner = False
        turn_count = 0

        while not have_winner:
            active_player: Player = self._BaseGameRunner__get_player_from_turn_count(turn_count)

            filtered_valid_inputs = [
                i for i in self.valid_inputs
                if self._BaseGameRunner__board.evaluate_drop_piece(i)]
            
            # print(filtered_valid_inputs)

            next_cell_status: CellStatus = self._BaseGameRunner__get_cell_status_from_player(
                    active_player)

            player_action: PlayerAction = self._BaseGameRunner__gui.get_player_action(
                active_player, filtered_valid_inputs, next_cell_status)

            final_position = self._BaseGameRunner__board.drop_piece(
                player_action.col_index,
                self._BaseGameRunner__get_cell_status_from_player(active_player))
            
            # print(final_position)

            if self._BaseGameRunner__evaluate_win(
                    final_position[1],
                    final_position[0],
                    self._BaseGameRunner__get_cell_status_from_player(active_player)):
                self._BaseGameRunner__gui.print_winner(active_player)
                have_winner = True
            
            turn_count += 1

            self._BaseGameRunner__gui.print_board()



def run(player1_type: str, player2_type: str, gui_type: str) -> None:
    board = Board()

    player1: Player = Player()
    if player1_type == "term":
        player1 = TerminalPlayer()
    elif player1_type == "random_ai":
        player1 = RandomPlayer()
    elif player1_type == "look_ahead":
        player1 = LookAheadPlayer()
    elif player1_type == "ml_ai":
        raise Exception("Not implemented yet!")
    elif player1_type == "qlearn":
        player1 = QLearningPlayer()
    else:
        raise Exception("Something doesn't add up... ")

    player2: Player = Player()
    if player2_type == "term":
        player2 = TerminalPlayer()
    elif player2_type == "random_ai":
        player2 = RandomPlayer()
    elif player2_type == "look_ahead":
        player2 = LookAheadPlayer()
    elif player2_type == "ml_ai":
        raise Exception("Not implemented yet!")
    elif player2_type == "qlearn":
        player2 = QLearningPlayer()
    else:
        raise Exception("Something doesn't add up... ")
    
    if gui_type == "term":
        gui_type_enum = GuiType.TERMINAL
    else:
        raise Exception("Something doesn't add up... ")

    runner: BaseGameRunner = SimpleGameRunner(board, player1, player2, gui_type_enum)
    runner.run()

