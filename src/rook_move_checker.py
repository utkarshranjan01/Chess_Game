def move_rook(gs, i,j,c,item, target5, check):
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

                if rook_check2(gs, c,i,j,m,n,move_b,move_a) and check(2,gs)==True:
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

                if rook_check2(gs, c,i,j,m,n,move_b,move_a) and check(1,gs)==True:
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

def rook_check2(gs,c,i,j,i1,j1,target01,target02):
    start_x, start_y = j,i
    end_x, end_y = j1,i1

    if (start_x != end_x and start_y != end_y) or (j==j1 and i==i1) or (j==-1 or i==-1 or j1==-1 or i1==-1):
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

    if (target01==target02):
        return False

    return True
