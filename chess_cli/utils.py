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

# function to check for universal invalidations for piece movement
def global_move_checker(c_x, c_y, n_x, n_y, b):

    # check if piece moves forward
    if c_x == n_x and c_y > n_y:
        chk = c_y - 1
        #check for piece in the way
        if b[chk][c_x] != '. ':
            return False
    
    #check if piece moves back
    elif c_x == n_x and c_y < n_y:
        chk = c_y + 1
        #check for piece in the way
        if b[chk][c_x] != '. ':
            return False

    #check if the piece moves right
    elif c_x < n_x and c_y == n_y:
        chk = c_x + 1
        #check for piece in the way
        if b[c_y][chk] != '. ':
            return False        

    #check if the piece moves left
    elif c_x > n_x and c_y == n_y:
        chk = c_x - 1
        #check for piece in the way
        if b[c_y][chk] != '. ':
            return False        

    #check if the piece moves diagonal top right
    elif c_x < n_x and c_y > n_y:
        chk = c_x + 1
        chk1 = c_y - 1
        #check for piece in the way
        if b[chk][chk1] != '. ':
            return False     

    return True