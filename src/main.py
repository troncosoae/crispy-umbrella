from argparse import ArgumentParser

from runner.game_runner import run as run_standard
from ai_coach.coach_game_runner import run_with_memory, run_from_memory


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="Connect 4",
        description="Platform to run Connect four, play it, and train AI on it. ")
    parser.add_argument(
        '-m', '--mode', type=str, default='run', choices=['run', 'sim', 'train'],
        help='Mode in which to run the platform. ')
    parser.add_argument(
        '-p1', '--player1', type=str, default='term',
        choices=['term', 'random_ai', 'ml_ai', 'look_ahead', 'qlearn'],
        help='Player type for player 1. ')
    parser.add_argument(
        '-p2', '--player2', type=str, default='term',
        choices=['term', 'random_ai', 'ml_ai', 'look_ahead', 'qlearn'],
        help='Player type for player 2. ')
    parser.add_argument(
        '-gt', '--gui_type', type=str, default='term',
        choices=['term'],
        help='GUI type on which the program is run. ')
    parser.add_argument(
        '-n', '--num_iter', type=int, default=1,
        help='Number of iterations to use in training')
    parser.add_argument(
        '-mo', '--memory_output', type=str, default='game_save.txt',
        help='File in which we save the information relevant for each game.')
    parser.add_argument(
        '-mi', '--memory_input', type=str, default='game_save.txt',
        help='File from which we read the information relevant for each game.')
    return parser

def parse_args(parser: ArgumentParser) -> dict:
    return vars(parser.parse_args())


def elect_flow(args: dict) -> None:
    mode = args['mode']
    if mode == 'run':
        run_standard(
            player1_type=args['player1'],
            player2_type=args['player2'],
            gui_type=args['gui_type'])
    elif mode == 'sim':
        run_with_memory(
            player1_type=args['player1'],
            player2_type=args['player2'],
            gui_type=args['gui_type'],
            num_iter=args['num_iter'],
            memory_output_file=args['memory_output'])
    elif mode == 'train':
        run_from_memory(
            memory_input_file=args['memory_input'],
            gui_type=args['gui_type'])


def main():
    parser = build_parser()
    args = parse_args(parser)
    print(args)
    elect_flow(args)

if __name__ == "__main__":
    main()

