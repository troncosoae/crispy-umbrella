from typing import List, Dict

from game.board import Board, CellStatus
from game.player import Player

from gui.base_interface import BaseGUI
from gui.terminal_interface.terminal_interface import TerminalGUI

from runner.game_runner import GameRunner as Runner, GuiType

# TODO: make sure that the players is the right type. 

class GameRunner:
    def __init__(self, board: 'Board', players: 'List[Player]'):
        self.board = board
        assert len(players) == 2
        self.players = players

    def __str__(self):
        game_runner_str = ""
        for player in self.players:
            print(player)
        game_runner_str += str(self.board)
        return game_runner_str

    def __repr__(self):
        return self.__str__()

def run():
    print("Connect 4!")
    board = Board(6, 7)
    print(board)

    board.drop_piece(0, CellStatus(1))
    print(board)
    board.drop_piece(0, CellStatus(2))
    print(board)
    board.drop_piece(0, CellStatus(1))
    print(board)
    board.drop_piece(0, CellStatus(2))
    print(board)
    board.drop_piece(0, CellStatus(1))
    print(board)
    board.drop_piece(1, CellStatus(1))
    print(board)
    board.drop_piece(2, CellStatus(1))
    print(board)
    board.drop_piece(3, CellStatus(1))
    print(board)

    player1 = Player()
    print(player1)
    player2 = Player()
    print(player2)


    base_gui = BaseGUI(board)
    terminal_gui = TerminalGUI(board)

    terminal_gui.print_board()

    try: 
        base_gui.print_board()
    except NotImplementedError:
        print("base_gui not implemented")

    gui_type = GuiType.TERMINAL
    runner = Runner(board, gui_type)
    runner.run()


    
