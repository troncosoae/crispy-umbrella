from runner.game_runner import BaseGameRunner, GuiType
from game.board import Board, CellStatus
from game.player import Player, PlayerAction
from gui.terminal_interface.terminal_interface import TerminalPlayer
from ai.random.random_ai import RandomPlayer
from ai_coach.memory import Memory, GameMemory


class MemoryGameRunner(BaseGameRunner):
    def __init__(
            self,
            board: Board,
            player1: Player,
            player2: Player,
            memory: Memory):
        BaseGameRunner.__init__(
            self, board, player1, player2, GuiType.TERMINAL)
        self.__memory = memory
    
    def run(self) -> None:
        self._BaseGameRunner__gui.print_init_banner()
        self._BaseGameRunner__gui.print_board()

        game_memory: GameMemory = GameMemory()

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

            assert self._BaseGameRunner__board.evaluate_drop_piece(
                player_action.col_index)

            game_memory.append_move(player_action.col_index)

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

        self.__memory.append_game(game_memory)

    def run_saved(self, saved_game: GameMemory) -> None:
        self._BaseGameRunner__gui.print_init_banner()
        self._BaseGameRunner__gui.print_board()

        turn_count = 0

        for move in saved_game.moves:
            active_player: Player = self._BaseGameRunner__get_player_from_turn_count(
                    turn_count)

            assert self._BaseGameRunner__board.evaluate_drop_piece(
                move)

            final_position = self._BaseGameRunner__board.drop_piece(
                move,
                self._BaseGameRunner__get_cell_status_from_player(active_player))

            if self._BaseGameRunner__evaluate_win(
                    final_position[1],
                    final_position[0],
                    self._BaseGameRunner__get_cell_status_from_player(active_player)):
                self._BaseGameRunner__gui.print_winner(active_player)
                assert turn_count == len(saved_game.moves) - 1
            
            turn_count += 1

            self._BaseGameRunner__gui.print_board()
        assert turn_count == len(saved_game.moves)


def run_with_memory(
        player1_type: str, player2_type: str, gui_type: str, num_iter: int,
        memory_output_file: str) -> None:
    board = Board()

    player1: Player = Player()
    if player1_type == "term":
        player1 = TerminalPlayer()
    elif player1_type == "random_ai":
        player1 = RandomPlayer()
    elif player1_type == "ml_ai":
        raise Exception("Not implemented yet!")
    else:
        raise Exception("Something doesn't add up... ")

    player2: Player = Player()
    if player2_type == "term":
        player2 = TerminalPlayer()
    elif player2_type == "random_ai":
        player2 = RandomPlayer()
    elif player2_type == "ml_ai":
        raise Exception("Not implemented yet!")
    else:
        raise Exception("Something doesn't add up... ")
    
    if gui_type == "term":
        gui_type_enum = GuiType.TERMINAL
    else:
        raise Exception("GUI type chosen not available... ")

    memory: Memory = Memory()

    for i in range(num_iter):
        board.reset()
        runner: MemoryGameRunner = MemoryGameRunner(
            board, player1, player2, memory)
        print("iteration: %d" % i)
        runner.run()

    memory.save(memory_output_file)


def run_from_memory(memory_input_file: str, gui_type: str) -> None:

    board = Board()
    
    if gui_type == "term":
        gui_type_enum = GuiType.TERMINAL
    else:
        raise Exception("GUI type chosen not available... ")

    player1: Player = TerminalPlayer()
    player2: Player = TerminalPlayer()

    memory: Memory = Memory()
    memory.load(memory_input_file)

    i: int = 1
    for game in memory.games:
        print("iteration: %d" % i)
        board.reset()
        runner: MemoryGameRunner = MemoryGameRunner(
            board, player1, player2, memory)

        runner.run_saved(game)

        i += 1


