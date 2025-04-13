def move_check(gs, i1, j1, i2, j2, c, item, target5, check):
    move_a=0
    move_b=0
    move_c=0
    move_f=0
    move_g=0
    if c==1:
        move_a=gs.color_board[i2][j2]
        gs.color_board[i2][j2]=1

        move_b=gs.color_board[i1][j1]

        gs.color_board[i1][j1]=0
        move_c=gs.board[i2][j2]
        gs.board[i2][j2]=item
        move_f=gs.board[i1][j1]
        gs.board[i1][j1]=0
        if item==5:
            gs.black_king_target_value=[i2,j2]
        if check(2,gs)==False:
            gs.color_board[i2][j2]=move_a
            gs.color_board[i1][j1]=move_b
            gs.board[i2][j2]=move_c
            gs.board[i1][j1]=move_f
            
            gs.black_king_target_value=gs.black_king_target_value2
            return False
        else:
            # print(item, "can be moved")
            gs.color_board[i2][j2]=move_a
            gs.color_board[i1][j1]=move_b
            gs.board[i2][j2]=move_c
            gs.board[i1][j1]=move_f

            gs.black_king_target_value=gs.black_king_target_value2
            return True
    else:
        move_a=gs.color_board[i2][j2]
        gs.color_board[i2][j2]=2

        move_b=gs.color_board[i1][j1]

        gs.color_board[i1][j1]=0
        move_c=gs.board[i2][j2]
        gs.board[i2][j2]=item
        move_f=gs.board[i1][j1]
        gs.board[i1][j1]=0
        if item==5:
            gs.white_king_target_value=[i2,j2]
        if check(1,gs)==False:
            gs.color_board[i2][j2]=move_a
            gs.color_board[i1][j1]=move_b
            gs.board[i2][j2]=move_c
            gs.board[i1][j1]=move_f
            
            gs.white_king_target_value=gs.white_king_target_value2
            return False
        else:
            # print(item, "can be moved")
            gs.color_board[i2][j2]=move_a
            gs.color_board[i1][j1]=move_b
            gs.board[i2][j2]=move_c
            gs.board[i1][j1]=move_f
            
            gs.white_king_target_value=gs.white_king_target_value2
            return True