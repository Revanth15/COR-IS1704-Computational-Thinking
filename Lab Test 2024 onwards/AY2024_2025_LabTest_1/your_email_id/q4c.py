# Name:
# Email ID:
from q4_utils import print_board

def get_who_won(M, board):
    # Replace the code below with your implementation.
    game_board_width = len(board)
    player_1_combo = "o" * M
    player_2_combo = "x" * M

    #Check tie
    tie_bool = True
    for row in board:
        if "-" in row:
            tie_bool = False

    if tie_bool:
        return "tie"

    # Check rows
    for row in board:
        if player_1_combo in row:
            return "o"
        elif player_2_combo in row:
            return "x"

    # Col checker 
    col_list = []
    for i in range(game_board_width):
        col = ""
        for row in board:
            col += row[i]
        col_list.append(col)

    for col in col_list:
        if player_1_combo in col:
            return "o"
        elif player_2_combo in col:
            return "x"

    # diagonal checker
    diagonal_plays = []
    for i in range(game_board_width):
        line = ""
        for j in range(i,0,-1):
            row = board[i]
            cell = row[j]
            line += cell
        diagonal_plays.append(line)
    print(diagonal_plays)
    return None