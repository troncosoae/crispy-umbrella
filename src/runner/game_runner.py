from enum import Enum

from game.board import Board
from gui.terminal_interface.terminal_interface import TerminalGUI


class GuiType(Enum):
    TERMINAL = 1



class GameRunner:
    def __init__(self, board: 'Board', gui_type: 'GuiType'):
        self.__board = board
        self.__init_gui(gui_type)

    def __init_gui(self, gui_type: 'GuiType'):
        if gui_type == GuiType.TERMINAL:
            self.__gui = TerminalGUI(self.__board)
        else:
            raise AssertionError("GUI type indicated doesn't exist")

    def run(self):
        print("Starting terminal GUI")
        self.__gui.print_board()


