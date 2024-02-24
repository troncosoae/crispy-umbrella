class Player:
    id: int = 0

    def __init__(self) -> None:
        self.id: int = Player.id
        Player.id += 1


    def __str__(self) -> str:
        player_str: str  = "P"
        player_str += str(self.id)
        return player_str

    def __repr__(self) -> str:
        return self.__str__()

