from typing import List
import pickle as pckl
from game.board import Board



class GameMemory:
    __class_id_counter: int = 0

    def __init__(self) -> None:
        self.__moves: List[int] = []
        self.__id: int = GameMemory.__class_id_counter
        GameMemory.__class_id_counter += 1

    @property
    def moves(self) -> List[int]:
        return self.__moves

    def append_move(self, move: int) -> None:
        self.__moves.append(move)


class Memory:
    def __init__(self) -> None:
        self.__games: List[GameMemory] = []

    def load(self, input_file_path: str) -> None:
        assert len(self.__games) == 0
        with open(input_file_path, 'rb') as file:
            self.__games = pckl.load(file)

    def save(self, output_file_path: str) -> None:
        assert len(self.__games) != 0
        with open(output_file_path, 'wb') as file:
            pckl.dump(self.__games, file)

    @property
    def games(self) -> List[GameMemory]:
        return self.__games

    def append_game(self, game: GameMemory) -> None:
        self.__games.append(game)

