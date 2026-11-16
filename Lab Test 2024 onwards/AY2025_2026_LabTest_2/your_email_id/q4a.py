# Name:
# Email ID:
    
def help_frog_against_snakes(map):
    # Modify the code below.
    jump_seqs = []
    allowed_moved = [1,2,3]
    safe_moves = []
    move_coutner = 0
    nest_sq = False
    for ch in map:
        if nest_sq and move_coutner == 2:
            return [0,[]]
        elif move_coutner == 3:
            safe_moves.append(move_coutner)
            move_coutner = 0

        if ch == "*":
            nest_sq = True
            if move_coutner != 0:
                safe_moves.append(move_coutner)
            move_coutner += 1
        else:
            move_coutner += 1
    safe_moves.append(move_coutner)
    print(safe_moves)
    return None
