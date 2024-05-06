from typing import List

class PlayerAction:
    def __init__(self, player_id: 'int', col_index: 'int'):
        self.__player_id = player_id
        self.__col_index = col_index

    @property
    def player_id(self):
        return self.__player_id

    @property
    def col_index(self):
        return self.__col_index



class Player:
    __class_id_counter: int = 0

    def __init__(self) -> None:
        self.__id: int = Player.__class_id_counter
        Player.__class_id_counter += 1

    @property
    def id(self) -> int:
        return self.__id

    def __str__(self) -> str:
        player_str: str  = "P"
        player_str += str(self.id)
        return player_str

    def __repr__(self) -> str:
        return self.__str__()
    
    def get_action(self, valid_inputs: List[int]) -> PlayerAction:
        raise Exception("Calling get_player_action from Player (the base class)")
