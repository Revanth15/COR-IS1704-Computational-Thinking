# Name:
# Email ID:
from q4_utils import print_board

def insert_to_board(game_board, row_index , col_index, player):
    row = game_board[row_index]
    row = row[0:col_index] + player + row[col_index+1:]
    game_board[row_index] = row

def check_if_occupied(game_board, col):
    insertable_range = -1
    for i in range(len(game_board), 0, -1):
        if game_board[i-1][col] == "-":
            return i - 1
    return insertable_range

def get_board_state_gravity(N, game):
    # Replace the code below with your implementation.
    game_board = []
    row = '-' * N
    for i in range(N):
        game_board.append(row)

    game_moves = []
    s = ""
    counter = 0
    for i in range(len(game)):
        counter += 1
        s += game[i]
        if counter == 2:
            game_moves.append(s)
            s = ""
            counter = 0
            
    for move in game_moves:
        col_move = int(move[0])
        player = move[1]
        row_insertion = check_if_occupied(game_board, col_move)
        if row_insertion != -1:
            insert_to_board(game_board, row_insertion, col_move, player)

    return game_board