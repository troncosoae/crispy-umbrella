from enum import Enum

from game.board import Board, CellStatus
from game.logic import GameLogic
from gui.terminal_interface.terminal_interface import TerminalGUI


class GuiType(Enum):
    TERMINAL = 1



class GameRunner:
    def __init__(self, board: 'Board', gui_type: 'GuiType'):
        self.__board = board
        self.__init_gui(gui_type)
        self.__logic = GameLogic(self.__board)

    def __init_gui(self, gui_type: 'GuiType'):
        if gui_type == GuiType.TERMINAL:
            self.__gui = TerminalGUI(self.__board)
        else:
            raise AssertionError("GUI type indicated doesn't exist")

    def run(self):
        print("Starting terminal GUI")
        self.__gui.print_board()
        self.__logic.evaluate_row(1, CellStatus(2))
        print(self.__logic.evaluate_col(0, CellStatus(1)))
        print(self.__logic.evaluate_row(2, CellStatus(1)))
        print("evaluating true")
        print(self.__logic.evaluate_row(5, CellStatus(1)))

        print(self.__logic.evaluate_diag_pn(2, 2, CellStatus(1)))
        print(self.__logic.evaluate_diag_pp(2, 2, CellStatus(1)))

        print(self.__logic.evaluate_diag_pn(5, 5, CellStatus(1)))
        print(self.__logic.evaluate_diag_pp(5, 5, CellStatus(1)))


