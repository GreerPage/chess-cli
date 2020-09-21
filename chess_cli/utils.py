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

def right_up(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [str(board[c_y-i-1][c_x+i+1]).strip() for i in range(distance)]

def right_down(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [str(board[c_y+i+1][c_x+i+1]).strip() for i in range(distance)]

def right(board, current, distance):
    c_x, c_y = coords_to_index(current)
    return [str(board[c_y][c_x+i+1]).strip() for i in range(distance)]

def left(board, current, distance):
    c_x, c_y = coords_to_index(current)
    print(c_x)
    return [str(board[c_y][c_x-i]).strip() for i in range(1, distance+1)]