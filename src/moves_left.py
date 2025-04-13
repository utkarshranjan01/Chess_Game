def moves_left2(gs, c, check, move_check, move_pawn, move_rook, move_knight, move_bishop, move_king):
    moves=[]
    item=0
    count_moves=0
    if c==1:
        for i in range(8):
            for j in range(8):
                if gs.board[i][j]!=0 and gs.color_board[i][j]!=2: #black pieces
                    item=gs.board[i][j]
                    if (item==6 or item==7):
                        if move_pawn(gs, i,j,c,item, i, move_check, check)==True:
                            count_moves+=1
                            # print("pawn moved")
                    if (item==1):
                        was_move_successful = move_rook(gs, i, j, c, item, i, check) 
                        if was_move_successful==True:
                            count_moves+=1
                            # print("rook moved")
                    if (item==2):
                        if move_knight(gs, i,j,c,item, i, move_check, check)==True:
                            count_moves+=1
                            # print("knight moved")
                    if (item==3):
                        was_move_successful = move_bishop(gs, i, j, c, item, i, check) 
                        if was_move_successful==True:
                            count_moves+=1
                            # print("bishop moved")
                    if (item==4):
                        was_move_successful1 = move_bishop(gs, i, j, c, item, i, check) 
                        was_move_successful2 = move_rook(gs, i, j, c, item, i, check) 
                        if was_move_successful1==True or was_move_successful2==True:
                            count_moves+=1
                            # print("queen moved")
                    if (item==5):
                        if move_king(gs, i,j,c,item, i)==True:
                            count_moves+=1
                            # print("king moved")
        gs.countcount=count_moves
        if count_moves==0:
            return False, c
        else:
            return True, c
    else:
        for i in range(8):
            for j in range(8):
                if gs.board[i][j]!=0 and gs.color_board[i][j]!=1: #white pieces
                    item=gs.board[i][j]
                    if (item==6 or item==7):
                        if move_pawn(gs, i,j,c,item, i, move_check, check)==True:
                            count_moves+=1
                    if (item==1):
                        was_move_successful = move_rook(gs, i, j, c, item, i, check) 
                        if was_move_successful==True:
                            count_moves+=1
                            # print("rook moved")
                    if (item==2):
                        if move_knight(gs, i,j,c,item, i, move_check, check)==True:
                            count_moves+=1
                    if (item==3):
                        was_move_successful = move_bishop(gs, i, j, c, item, i,check) 
                        if was_move_successful==True:
                            count_moves+=1
                            # print("bishop moved")
                    if (item==4):
                        was_move_successful1 = move_bishop(gs, i, j, c, item, i, check) 
                        was_move_successful2 = move_rook(gs, i, j, c, item, i, check) 
                        if was_move_successful1==True or was_move_successful2==True:
                            count_moves+=1
                            # print("queen moved")
                    if (item==5):
                        if move_king(gs, i,j,c,item, i)==True:
                            count_moves+=1
        gs.countcount=count_moves
        if count_moves==0:
            return False, c
        else:
            return True, c