# from src.variables import *


def bishop_check(gs, c):
    start_x, start_y = gs.select
    end_x, end_y = gs.selected

    # if (gs.select!=gs.selected):
    #     if (gs.target<=15 and check(2)==False) or (gs.target>15 and check(1)==False):
    #         sound_illegal.play()

    if abs(start_x - end_x) != abs(start_y - end_y):
        return False

    dx = 1 if end_x > start_x else -1
    dy = 1 if end_y > start_y else -1
    x, y = start_x + dx, start_y + dy

    while x != end_x and y != end_y:
        if gs.board[y][x] != 0:  # Path is not clear
            return False
        x, y = x + dx, y + dy

    if (c==1 and ((gs.target>15 and gs.target2>15) or (gs.target<=15 and gs.target2<=15))):
        return False
    
    return True

def knight_check(gs, c):
    start_x, start_y = gs.select[0], gs.select[1]
    end_x, end_y = gs.selected[0], gs.selected[1]

    # if (gs.select!=gs.selected):
    #     if (gs.target<=15 and check(2)==False) or (gs.target>15 and check(1)==False):
    #         sound_illegal.play()

    if c==0:
        if (abs(start_x - end_x) == 2 and abs(start_y - end_y) == 1) or \
        (abs(start_x - end_x) == 1 and abs(start_y - end_y) == 2):
            return True
    else:
        if (((abs(start_x - end_x) == 2 and abs(start_y - end_y) == 1) or \
        (abs(start_x - end_x) == 1 and abs(start_y - end_y) == 2)) and ((gs.target>15 and gs.target2<=15) or (gs.target<=15 and gs.target2>15))):
            return True

    return False

def rook_check(gs, c):
    start_x, start_y = gs.select
    end_x, end_y = gs.selected

    # if (gs.select!=gs.selected):
    #     if (gs.target<=15 and check(2)==False) or (gs.target>15 and check(1)==False):
    #         sound_illegal.play()

    if (start_x != end_x and start_y != end_y) or (gs.select==gs.selected):
        return False

    if start_x == end_x:
        step = 1 if start_y < end_y else -1
        for y in range(start_y + step, end_y, step):
            if gs.board[y][start_x] != 0:
                return False
    else:
        step = 1 if start_x < end_x else -1
        for x in range(start_x + step, end_x, step):
            if gs.board[start_y][x] != 0:
                return False

    if (c==1 and ((gs.target>15 and gs.target2>15) or (gs.target<=15 and gs.target2<=15))):
        return False

    return True
