def check2(gs, g, cpawnb, crookb, cknightb, cbishopb, ckingb):

    val=True

    for i in range(8):
        for j in range(8):
            if gs.board[i][j]!=0:
                if (gs.color_board[i][j]==1 and (g==1 or g==0)):#check for white king with target>15 which is wk(orientation of gs.board does not matter as only image position we can reverse)
                    if gs.board[i][j]==6 or gs.board[i][j]==7:
                        is_successful = cpawnb(gs, i,j,1)
                        if is_successful:
                            return False, g
                    elif gs.board[i][j]==1:
                        is_successful = crookb(gs, i,j,1)
                        if is_successful:
                            return False, g
                    elif gs.board[i][j]==2:
                        is_successful = cknightb(gs, i,j,1)
                        if is_successful:
                            return False, g
                    elif gs.board[i][j]==3:
                        is_successful = cbishopb(gs, i,j,1)
                        if is_successful:
                            return False, g
                    elif gs.board[i][j]==4:
                        is_successful1 = crookb(gs, i,j,1)
                        is_successful2 = cbishopb(gs, i,j,1)
                        if is_successful1 or is_successful2:
                            return False, g
                    elif gs.board[i][j]==5:
                        is_successful = ckingb(gs, i,j,1)
                        if is_successful:
                            return False, g
                elif (gs.color_board[i][j]==2 and (g==2 or g==0)):#check for black king with target>15 which is wk(orientation of gs.board does not matter as only image position we can reverse)
                    if gs.board[i][j]==6 or gs.board[i][j]==7:
                        is_successful = cpawnb(gs, i,j,2)
                        if is_successful:
                            return False, g
                    elif gs.board[i][j]==1:
                        is_successful = crookb(gs, i,j,2)
                        if is_successful:
                            return False, g
                    elif gs.board[i][j]==2:
                        is_successful = cknightb(gs, i,j,2)
                        if is_successful:
                            return False, g
                    elif gs.board[i][j]==3:
                        is_successful = cbishopb(gs, i,j,2)
                        if is_successful:
                            return False, g
                    elif gs.board[i][j]==4:
                        is_successful1 = crookb(gs, i,j,2)
                        is_successful2 = cbishopb(gs, i,j,2)
                        if is_successful1 or is_successful2:
                            return False, g
                    elif gs.board[i][j]==5:
                        is_successful = ckingb(gs, i,j,2)
                        if is_successful:
                            return False, g
    gs.king_under_check=0
    return val, g