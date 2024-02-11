from game.board import Board

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
    board.drop_piece(0, 2)
    print(board)
    board.drop_piece(0, 1)
    print(board)
    board.drop_piece(0, 2)
    print(board)

    
