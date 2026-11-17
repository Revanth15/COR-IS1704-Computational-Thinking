# Name:
# Email ID:

def help_frog_against_snakes(map):
    goal = len(map) - 1

    def routes_from(position):
        if position == goal:
            return ((),)
        routes = []
        for jump in (1, 2, 3):
            landing = position + jump
            if landing <= goal and map[landing] != "*":
                for suffix in routes_from(landing):
                    routes.append((jump,) + suffix)
        return tuple(routes)

    sequences = [list(route) for route in routes_from(0)]
    return (len(sequences), sequences)
    
# def help_frog_against_snakes(map):
#     # Modify the code below.
#     jump_seqs = []
#     allowed_moved = [1,2,3]
#     safe_moves = []
#     move_coutner = 0
#     nest_sq = False
#     for ch in map:
#         if nest_sq and move_coutner == 2:
#             return [0,[]]
#         elif move_coutner == 3:
#             safe_moves.append(move_coutner)
#             move_coutner = 0

#         if ch == "*":
#             nest_sq = True
#             if move_coutner != 0:
#                 safe_moves.append(move_coutner)
#             move_coutner += 1
#         else:
#             move_coutner += 1
#     safe_moves.append(move_coutner)
#     print(safe_moves)
#     return None
