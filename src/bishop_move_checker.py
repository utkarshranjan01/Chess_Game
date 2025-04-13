def move_bishop(gs, i,j,c,item, target5, check):
    new_x1=-1
    new_x2=-1
    new_y1=-1
    new_y2=-1
    new_x01=-1
    new_x02=-1
    new_y01=-1
    new_y02=-1
    move_a=0
    move_b=0
    move_c=0
    move_f=0
    move_g=0
    move_h=0
    total_rook_count=0
    
    if c==1:
        for m in range(8):
            for n in range(8):

                move_a=gs.color_board[m][n]
                move_b=gs.color_board[i][j]
                move_c=gs.board[m][n]
                move_f=gs.board[i][j]
                move_h=gs.king_under_check

                gs.color_board[m][n]=move_b
                gs.color_board[i][j]=0
                gs.board[m][n]=move_f
                gs.board[i][j]=0

                if bishop_check2(gs, c,i,j,m,n,move_b,move_a) and check(2,gs)==True:
                    total_rook_count+=1
                    gs.color_board[m][n]=move_a
                    gs.color_board[i][j]=move_b
                    gs.board[m][n]=move_c
                    gs.board[i][j]=move_f
                    gs.king_under_check=move_h
                else:
                    gs.color_board[m][n]=move_a
                    gs.color_board[i][j]=move_b
                    gs.board[m][n]=move_c
                    gs.board[i][j]=move_f
                    gs.king_under_check=move_h
        if total_rook_count==0:
            return False
        else:
            return True
    else:
        for m in range(8):
            for n in range(8):

                move_a=gs.color_board[m][n]
                move_b=gs.color_board[i][j]
                move_c=gs.board[m][n]
                move_f=gs.board[i][j]
                move_h=gs.king_under_check

                gs.color_board[m][n]=move_b
                gs.color_board[i][j]=0
                gs.board[m][n]=move_f
                gs.board[i][j]=0

                if bishop_check2(gs, c,i,j,m,n,move_b,move_a) and check(1,gs)==True:
                    total_rook_count+=1
                    gs.color_board[m][n]=move_a
                    gs.color_board[i][j]=move_b
                    gs.board[m][n]=move_c
                    gs.board[i][j]=move_f
                    gs.king_under_check=move_h
                else:
                    gs.color_board[m][n]=move_a
                    gs.color_board[i][j]=move_b
                    gs.board[m][n]=move_c
                    gs.board[i][j]=move_f
                    gs.king_under_check=move_h
        if total_rook_count==0:
            return False
        else:
            return True

def bishop_check2(gs, c,i,j,i1,j1,target01,target02):
    start_x, start_y = j,i
    end_x, end_y = j1,i1

    if abs(start_x - end_x) != abs(start_y - end_y):
        return False

    dx = 1 if end_x > start_x else -1
    dy = 1 if end_y > start_y else -1
    x, y = start_x + dx, start_y + dy

    while x != end_x and y != end_y and x!=-1 and y!=-1:
        if gs.board[y][x] != 0:  # Path is not clear
            return False
        x, y = x + dx, y + dy

    if (target01==target02):
        return False
    
    return True