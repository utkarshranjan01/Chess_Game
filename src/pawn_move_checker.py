def move_pawn(gs, i,j,c,item, target5, move_check, check):
    new_x=-1
    new_x2=-1
    new_y1=-1
    new_y2=-1
    new_y3=-1
    if c==1: # black pieces
        if i<7:
            new_x=i+1
        else:
            return False
        if j>0:
            new_y1=j-1
        if j<7:
            new_y2=j+1

        if i==4:
            if (j+1)<=7:
                if gs.color_board[i][j+1]==2 and gs.board[i][j+1]==7:
                    if move_check(gs, i,j,i,j+1,1, item, target5, check)==True:
                        return True
            if (j-1)>=0:
                if gs.color_board[i][j-1]==2 and gs.board[i][j-1]==7:
                    if move_check(gs, i,j,i,j-1,1, item, target5, check)==True:
                        return True

        if gs.board[i+1][j]==0:
            new_y3=j
            if move_check(gs, i,j,new_x,j,1, item, target5, check)==True:
                return True
        if i==1 and i<6 and gs.board[i+2][j]==0 and gs.board[i+1][j]==0 :
            new_x2=i+2
            if move_check(gs, i,j,new_x2,j,1, item, target5, check)==True:
                return True
        if (new_y2!=-1 and gs.board[new_x][j+1]!=0 and gs.color_board[new_x][j+1]==2) or (new_y2!=-1 and gs.board[i][j+1]==7 and gs.color_board[i][j+1]==2):
            if move_check(gs, i,j,new_x,j+1,1, item, target5, check)==True:
                return True
        if (new_y1!=-1 and gs.board[new_x][j-1]!=0 and gs.color_board[new_x][j-1]==2) or (new_y1!=-1 and gs.board[i][j-1]==7 and gs.color_board[i][j-1]==2):
            if move_check(gs, i,j,new_x,j-1,1, item, target5, check)==True:
                return True
        return False

    else: # white pieces
        if i>1:
            new_x=i-1
        else:
            return False
        if j>0:
            new_y1=j-1
        if j<7:
            new_y2=j+1

        if i==3:
            if (j+1)<=7:
                if gs.color_board[i][j+1]==1 and gs.board[i][j+1]==7:
                    if move_check(gs, i,j,i,j+1,2, item, target5, check)==True:
                        return True
            if (j-1)>=0:
                if gs.color_board[i][j-1]==1 and gs.board[i][j-1]==7:
                    if move_check(gs ,i,j,i,j-1,2, item, target5, check)==True:
                        return True

        if gs.board[i-1][j]==0:
            new_y3=j
            if move_check(gs ,i,j,new_x,j,2, item, target5, check)==True:
                # print("hey 3.3")
                return True
        if i==6 and i>1 and gs.board[i-2][j]==0 and gs.board[i-1][j]==0:
            new_x2=i-2
            if move_check(gs ,i,j,new_x2,j,2, item, target5, check)==True:
                # print("hey 4.4")
                return True
        if (new_y2!=-1 and gs.board[new_x][j+1]!=0 and gs.color_board[new_x][j+1]==1) or (new_y2!=-1 and gs.board[i][j+1]==7 and gs.color_board[i][j+1]==1):
            if move_check(gs ,i,j,new_x,j+1,2, item, target5, check)==True:
                # print("hey 3")
                return True
        if (new_y1!=-1 and gs.board[new_x][j-1]!=0 and gs.color_board[new_x][j-1]==1) or (new_y1!=-1 and gs.board[i][j-1]==7 and gs.color_board[i][j-1]==1):
            if move_check(gs ,i,j,new_x,j-1,2, item, target5, check)==True:
                # print("hey 4")
                return True
        return False