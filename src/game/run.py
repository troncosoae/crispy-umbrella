from typing import List, Dict

from game.board import Board
from game.player import Player

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

    board.drop_piece(0, 1)
    print(board)
    board.drop_piece(0, 2)
    print(board)
    board.drop_piece(0, 1)
    print(board)
    board.drop_piece(0, 2)
    print(board)
    board.drop_piece(0, 1)
    print(board)

    player1 = Player()
    print(player1)
    player2 = Player()
    print(player2)

    game_runner = GameRunner(
            board,
            [player1, player2])
    print(game_runner)

    
