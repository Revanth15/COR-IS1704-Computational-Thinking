# Name: Revanth
# Email ID: revanth.rs.2026
       
def rotate(puzzle, N, move):
    """
    Perform a rotation of the puzzle as described in the test paper.

    Args:
        puzzle (str): The puzzle, a row-major string of upper-case letters
        N      (int): The number of rows or columns, where 0 < N < 6
        move   (str): A two-character string. The first character is the row or column
                      to rotate, where 0 <= ix < N. The second character is either 'U',
                      'D','L', or 'R', indicating the direction of rotation.
    
    Returns:
        A string representation of the puzzle after being transformed.
        The string is in row-major form.
    """
    # Modify the code below.
    rows = []
    chs = []
    counter = 0
    for ch in puzzle:
        if counter == N:
            rows.append(chs)
            chs = []
            counter = 0
        chs.append(ch)
        counter += 1
    rows.append(chs)
    move_idx = int(move[0])
    move_type = move[1]

    if move_type in ["U", "D"]:
        hold_ch = ""
        if move_type == "U":
            for i in range(len(rows)):
                if i == 0:
                    hold_ch = rows[i][move_idx]
                    rows[i][move_idx] = rows[i+1][move_idx]
                elif i == len(rows) - 1:
                    rows[i][move_idx] = hold_ch
                else:
                    rows[i][move_idx] = rows[i+1][move_idx]
        if move_type == "D":
            for i in range(len(rows)):
                if i == 0:
                    hold_ch = rows[i][move_idx]
                    rows[i][move_idx] = rows[len(rows)-1][move_idx]
                    rows[i+1][move_idx] = hold_ch
                else:
                    if i != 1:
                        hold_ch = rows[i-1][move_idx]
                        rows[i][move_idx] = rows[i-1][move_idx]
    elif move_type in ["L", "R"]:
        if move_type == "L":
            to_move = rows[move_idx][0]
            rows[move_idx].pop(0)
            rows[move_idx].append(to_move)
        elif move_type == "R":
            to_move = rows[move_idx][-1]
            rows[move_idx].pop(-1)
            rows[move_idx].insert(0, to_move)
    # print(rows)
    combined = ""
    for row in rows:
        for ch in row:
            combined += ch
    return combined 
