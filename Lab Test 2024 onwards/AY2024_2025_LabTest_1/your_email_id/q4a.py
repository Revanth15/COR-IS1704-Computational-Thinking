# Name:
# Email ID:
from q4_utils import print_board

def get_board_state(N, game):      
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
        if counter == 3:
            game_moves.append(s)
            s = ""
            counter = 0

    for move in game_moves:
        row_move = int(move[0])
        col_move = int(move[1])
        player = move[2]

        row = game_board[row_move]
        row = row[0:col_move] + player + row[col_move+1:]
        game_board[row_move] = row
    return game_board

    
