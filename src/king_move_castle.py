def king_move2(gs, sound_illegal, check, c):

    start_x, start_y = gs.select
    end_x, end_y = gs.selected
    move_a=0
    move_b=0
    move_c=0
    move_d=0
    castle=[] 

    if c==0:
        if gs.castle_black_1==1 and start_y==0 and end_x==2:
            gs.board[0][0]=0
            gs.board[0][3]=1
            gs.color_board[0][0]=0
            gs.color_board[0][3]=1
            gs.position[0]=gs.piece[0].get_rect(center=(gs.pos[0][3][0],gs.pos[0][3][1]))
            gs.castle_black_1=0
            castle.append(1)
        else:
            castle.append(0)
        if gs.castle_black_2==1 and start_y==0 and end_x==6:
            gs.board[0][7]=0
            gs.board[0][5]=1
            gs.color_board[0][7]=0
            gs.color_board[0][5]=1
            gs.position[7]=gs.piece[7].get_rect(center=(gs.pos[0][5][0],gs.pos[0][5][1]))
            gs.castle_black_2=0
            castle.append(1)
        else:
            castle.append(0)
        if gs.castle_white_1==1 and start_y==7 and end_x==2:
            gs.board[7][0]=0
            gs.board[7][3]=1
            gs.color_board[7][0]=0
            gs.color_board[7][3]=2
            gs.position[16]=gs.piece[16].get_rect(center=(gs.pos[7][3][0],gs.pos[7][3][1]))
            gs.castle_white_1=0
            castle.append(1)
        else:
            castle.append(0)
        if gs.castle_white_2==1 and start_y==7 and end_x==6:
            gs.board[7][7]=0
            gs.board[7][5]=1
            gs.color_board[7][7]=0
            gs.color_board[7][5]=2
            gs.position[23]=gs.piece[23].get_rect(center=(gs.pos[7][5][0],gs.pos[7][5][1]))
            gs.castle_white_2=0
            castle.append(1)
        else:
            castle.append(0)

        for i in range (len(castle)):
            if castle[i]==1:
                gs.castle_being_done=1
                return castle, c

        if max(abs(start_x - end_x), abs(start_y - end_y)) != 1:
            return False, c
    else:
        if max(abs(start_x - end_x), abs(start_y - end_y)) != 1:
            gs.castle_black_1=0
            gs.castle_black_2=0
            gs.castle_white_1=0
            gs.castle_white_2=0
            return False, c
        else:
            if (gs.target>15 and gs.target2>15) or (gs.target<=15 and gs.target2<=15):
                return False, c
            
    move_a=gs.board[gs.select[1]][gs.select[0]]
    move_b=gs.board[gs.selected[1]][gs.selected[0]]
    move_c=gs.color_board[gs.select[1]][gs.select[0]]
    move_d=gs.color_board[gs.selected[1]][gs.selected[0]]
    gs.color_board[gs.selected[1]][gs.selected[0]]=gs.color_board[gs.select[1]][gs.select[0]]
    gs.board[gs.selected[1]][gs.selected[0]]=gs.board[gs.select[1]][gs.select[0]]
    gs.board[gs.select[1]][gs.select[0]]=0
    gs.color_board[gs.select[1]][gs.select[0]]=0

    gs.white_king_target_value2 = gs.white_king_target_value
    gs.black_king_target_value2 = gs.black_king_target_value
    if gs.target<=15:
        gs.black_king_target_value=[gs.selected[1],gs.selected[0]]
        if check(2,gs)==True:
            gs.black_king_target_value2=gs.black_king_target_value
            # if (gs.select!=gs.selected):
            #     if (gs.target<=15 and check(2,gs)==False) or (gs.target>15 and check(1,gs)==False):
            #         sound_illegal.play() 
            return True, c
        else:
            gs.black_king_target_value=gs.black_king_target_value2
            sound_illegal.play() 
            gs.color_board[gs.selected[1]][gs.selected[0]]=move_d
            gs.board[gs.selected[1]][gs.selected[0]]=move_b
            gs.board[gs.select[1]][gs.select[0]]=move_a
            gs.color_board[gs.select[1]][gs.select[0]]=move_c
            return False, c
    elif gs.target>15:
        gs.white_king_target_value=[gs.selected[1],gs.selected[0]]

        if check(1,gs)==True:
            gs.white_king_target_value2=gs.white_king_target_value
            # if (gs.select!=gs.selected):
            #     if (gs.target<=15 and check(2,gs)==False) or (gs.target>15 and check(1,gs)==False):
            #         sound_illegal.play() 
            return True, c
        else:
            gs.white_king_target_value=gs.white_king_target_value2
            sound_illegal.play() 
            gs.color_board[gs.selected[1]][gs.selected[0]]=move_d
            gs.board[gs.selected[1]][gs.selected[0]]=move_b
            gs.board[gs.select[1]][gs.select[0]]=move_a
            gs.color_board[gs.select[1]][gs.select[0]]=move_c
            return False, c
        
    return "", c