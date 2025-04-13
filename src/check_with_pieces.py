
def cbishopb(gs, i,j,c):
    start_x, start_y = j, i
    if c==1:
        end_y, end_x = gs.white_king_target_value
    else:
        end_y, end_x = gs.black_king_target_value

    if abs(start_x - end_x) != abs(start_y - end_y):
        return False

    dx = 1 if end_x > start_x else -1
    dy = 1 if end_y > start_y else -1
    x, y = start_x + dx, start_y + dy

    while x != end_x and y != end_y:
        if gs.board[y][x] != 0:  # Path is not clear
            return False
        x, y = x + dx, y + dy
    
    if c==1:
        gs.king_under_check=2
    else:
        gs.king_under_check=1
    return True

def cknightb(gs, i,j,c):
    start_x, start_y = i, j
    if c==1:
        end_x, end_y = gs.white_king_target_value
    else:
        end_x, end_y = gs.black_king_target_value
    if (abs(start_x - end_x) == 2 and abs(start_y - end_y) == 1) or \
    (abs(start_x - end_x) == 1 and abs(start_y - end_y) == 2):
        if c==1:
            gs.king_under_check=2
        else:
            gs.king_under_check=1
        return True
    return False

def crookb(gs, i,j,c):
    start_x, start_y = i,j
    if c==1:
        end_x, end_y = gs.white_king_target_value
    else:
        end_x, end_y = gs.black_king_target_value
    # we reversed gs.board[][] the x and y here from the check_rook function as its reversed the i and j in place of x and y we put in the above 2 lines

    if (start_x != end_x and start_y != end_y) or ([i,j]==[end_x,end_y]):
        return False

    if start_x == end_x:
        step = 1 if start_y < end_y else -1
        for y in range(start_y + step, end_y, step):
            if gs.board[start_x][y] != 0:
                return False
    else:
        step = 1 if start_x < end_x else -1
        for x in range(start_x + step, end_x, step):
            if gs.board[x][start_y] != 0:
                return False

    if c==1:
        gs.king_under_check=2
    else:
        gs.king_under_check=1
    return True

def cpawnb(gs, i,j,c):
    new_x=-1
    new_y1=-1
    new_y2=-1

    if c==1:
        if i<7:
            new_x=i+1
        else:
            return False
        if j>0:
            new_y1=j-1
        if j<7:
            new_y2=j+1
        if new_y1!=-1:
            if (gs.white_king_target_value==[new_x,new_y1]):
                if c==1:
                    gs.king_under_check=2
                else:
                    gs.king_under_check=1
                return True
        if new_y2!=-1:
            if (gs.white_king_target_value==[new_x,new_y2]):
                if c==1:
                    gs.king_under_check=2
                else:
                    gs.king_under_check=1
                return True
    else:
        if i>0:
            new_x=i-1
        else:
            return False
        if j>0:
            new_y1=j-1
        if j<7:
            new_y2=j+1
        if new_y1!=-1:
            if (gs.black_king_target_value==[new_x,new_y1]):
                if c==1:
                    gs.king_under_check=2
                else:
                    gs.king_under_check=1
                return True
        if new_y2!=-1:
            if (gs.black_king_target_value==[new_x,new_y2]):
                if c==1:
                    gs.king_under_check=2
                else:
                    gs.king_under_check=1
                return True
    return False

def ckingb(gs, i,j,c):
    start_x, start_y = i,j
    if c==1:
        end_x, end_y = gs.white_king_target_value
    else:
        end_x, end_y = gs.black_king_target_value
    if max(abs(start_x - end_x), abs(start_y - end_y)) != 1:
        return False
    if c==1:
        gs.king_under_check=2
    else:
        gs.king_under_check=1
    return True   
