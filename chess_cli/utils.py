# file containing functions used throughout the project

# take board x value and turn return a equivalent value for the matrix
def x_axis_to_index(x):
    if x == 'a': return 1
    if x == 'b': return 2
    if x == 'c': return 3
    if x == 'd': return 4
    if x == 'e': return 5
    if x == 'f': return 6
    if x == 'g': return 7
    if x == 'h': return 8

# take board y value and turn return a equivalent value for the matrix
def y_axis_to_index(y):
    y = int(y)
    if y == 1: return 7
    if y == 2: return 6
    if y == 3: return 5
    if y == 4: return 4
    if y == 5: return 3
    if y == 6: return 2
    if y == 7: return 1
    if y == 8: return 0

# take x and y and return corresponding indices
def coords_to_index(coords):
    return [x_axis_to_index(coords[0]), y_axis_to_index(coords[1])]

# get right up path
def right_up(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [board[c_y-i-1][c_x+i+1] for i in range(distance)]

# get right down path
def right_down(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [board[c_y+i+1][c_x+i+1] for i in range(distance)]


# get right path
def right(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [board[c_y][c_x+i+1] for i in range(distance)]

# get left path
def left(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [board[c_y][c_x-i] for i in range(1, distance+1)]

# get up path
def up(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [board[c_y-i-1][c_x] for i in range(distance)]

# get down path
def down(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [board[c_y+i+1][c_x] for i in range(distance)]

# get left up path
def left_up(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [board[c_y-i][c_x-i] for i in range(1, distance+1)]

# get left down path
def left_down(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [board[c_y+i][c_x-i] for i in range(1, distance+1)]

# get valid moves vertical and horizontal
def valid_vertical_horizontal_moves(b, current, new, side):
    valid_moves = []
    cx, cy = coords_to_index(current)
    move_to = coords_to_index(new)
    board = b.board
    paths = [up(board, current, cy), down(board, current, 7-cy), right(board, current, 8-cx), left(board, current, cx-1)]
    for i in range(len(paths[0])):
        if paths[0][i] == '. ':
            valid_moves.append([cx, cy-i-1])
        elif paths[0][i] in side:
            break
        else:
            valid_moves.append([cx, cy-i-1])  
            break
    
    for i in range(len(paths[1])):
        if paths[1][i] == '. ':
            valid_moves.append([cx, cy+i+1])
        elif paths[1][i] in side:
            break
        else:
            valid_moves.append([cx, cy+i+1])  
            break

    for i in range(len(paths[2])):
        if paths[2][i] == '. ':
            valid_moves.append([cx+i+1, cy])
        elif paths[2][i] in side:
            break
        else:
            valid_moves.append([cx+i+1, cy])  
            break

    for i in range(1, len(paths[3])+1):
        if paths[3][i-1] == '. ':
            valid_moves.append([cx-i, cy]) 
        elif paths[3][i-1] in side:
            break
        else:
            valid_moves.append([cx-i, cy])  
            break
    
    if move_to in valid_moves:
        return True

    return False

# knight moves
def l_up_right(board, current):
    cx, cy = coords_to_index(current)
    return [board[cy-2][cx+1], board[cy-1][cx+2]]

def l_up_left(board, current):
    cx, cy = coords_to_index(current)
    return [board[cy-2][cx-1], board[cy-1][cx-2]]

def l_down_right(board, current):
    cx, cy = coords_to_index(current)
    return [board[cy+2][cx+1], board[cy+1][cx+2]]

def l_down_left(board, current):
    cx, cy = coords_to_index(current)
    return [board[cy+2][cx-1], board[cy+1][cx-2]]

def knight_logic(board, current, side):
    valid_moves = []
    cx, cy = coords_to_index(current)
    if l_up_right(board, current)[0] not in side:
            valid_moves.append([cx+1, cy-2])
    if l_up_right(board, current)[1] not in side:
        valid_moves.append([cx+2, cy-1])
    if l_up_left(board, current)[0] not in side:
        valid_moves.append([cx-1, cy-2])
    if l_up_left(board, current)[1] not in side:
        valid_moves.append([cx-2, cy-1])
    if l_down_right(board, current)[0] not in side:
        valid_moves.append([cx+1, cy+2])
    if l_down_right(board, current)[1] not in side:
        valid_moves.append([cx+2, cy+1])
    if l_down_left(board, current)[0] not in side:
        valid_moves.append([cx-1, cy+2])
    if l_down_left(board, current)[1] not in side:
        valid_moves.append([cx-2, cy+1])
    return valid_moves

def split_str(w):
    return [l for l in w]