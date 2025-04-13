
def move_king2(gs,i,j,c,item, target5, move_check, check):

    new_x1=i
    new_x2=-1
    new_y1=j
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
    if c==1:
        if i<7:
            new_x01=i+1
        if i>0:
            new_x02=i-1
        if j<7:
            new_y01=j+1
        if j>0:
            new_y02=j-1

        if abs(i-new_x01)==1 and new_x01!=-1:
            if gs.board[new_x01][j]==0 or gs.color_board[new_x01][j]==2:

                if move_check(gs, i,j,new_x01,j,1, item, target5, check)==True:
                    gs.black_king_target_value2=gs.black_king_target_value
                    gs.black_king_target_value=[new_x01,j]
                    
                    move_a=gs.color_board[new_x01][j]
                    gs.color_board[new_x01][j]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x01][j]
                    gs.board[new_x01][j]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[j][new_x01][0]))
                    move_h=gs.king_under_check
                    if check(2,gs):
                        gs.black_king_target_value=gs.black_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.black_king_target_value=gs.black_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(i-new_x02)==1 and new_x02!=-1:
            if gs.board[new_x02][j]==0 or gs.color_board[new_x02][j]==2:
                if move_check(gs, i,j,new_x02,j,1, item, target5, check)==True:
                    gs.black_king_target_value2=gs.black_king_target_value
                    gs.black_king_target_value=[new_x02,j]

                    move_a=gs.color_board[new_x02][j]
                    gs.color_board[new_x02][j]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x02][j]
                    gs.board[new_x02][j]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[j][new_x02][0]))
                    move_h=gs.king_under_check
                    if check(2,gs):
                        gs.black_king_target_value=gs.black_king_target_value2
                        
                        gs.color_board[new_x02][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x02][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.black_king_target_value=gs.black_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(j-new_y01)==1 and new_y01!=-1:
            if gs.board[i][new_y01]==0 or gs.color_board[i][new_y01]==2:
                if move_check(gs, i,j,i,new_y01,1, item, target5, check)==True:
                    gs.black_king_target_value2=gs.black_king_target_value
                    gs.black_king_target_value=[i,new_y01]

                    move_a=gs.color_board[i][new_y01]
                    gs.color_board[i][new_y01]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[i][new_y01]
                    gs.board[i][new_y01]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y01][i][0]))
                    move_h=gs.king_under_check
                    if check(2,gs):
                        gs.black_king_target_value=gs.black_king_target_value2
                        
                        gs.color_board[i][new_y01]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[i][new_y01]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.black_king_target_value=gs.black_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(j-new_y02)==1 and new_y02!=-1:
            if gs.board[i][new_y02]==0 or gs.color_board[i][new_y02]==2:
                if move_check(gs, i,j,i,new_y02,1, item, target5, check)==True:
                    gs.black_king_target_value2=gs.black_king_target_value
                    gs.black_king_target_value=[i,new_y02]

                    move_a=gs.color_board[i][new_y02]
                    gs.color_board[i][new_y02]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[i][new_y02]
                    gs.board[i][new_y02]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y02][i][0]))
                    move_h=gs.king_under_check
                    if check(2,gs):
                        gs.black_king_target_value=gs.black_king_target_value2
                        
                        gs.color_board[i][new_y02]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[i][new_y02]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.black_king_target_value=gs.black_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h

        if abs(i-new_x01)==1 and abs(j-new_y01)==1 and new_x01!=-1 and new_y01!=-1:
            if gs.board[new_x01][new_y01]==0 or gs.color_board[new_x01][new_y01]==2:
                if move_check(gs, i,j,new_x01,new_y01,1, item, target5, check)==True:
                    gs.black_king_target_value2=gs.black_king_target_value
                    gs.black_king_target_value=[new_x01,new_y01]

                    move_a=gs.color_board[new_x01][new_y01]
                    gs.color_board[new_x01][new_y01]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x01][new_y01]
                    gs.board[new_x01][new_y01]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y01][new_x01][0]))
                    move_h=gs.king_under_check
                    if check(2,gs):
                        gs.black_king_target_value=gs.black_king_target_value2
                        
                        gs.color_board[new_x01][new_y01]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][new_y01]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h

                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.black_king_target_value=gs.black_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(i-new_x01)==1 and abs(j-new_y02)==1 and new_x01!=-1 and new_y02!=-1:
            if gs.board[new_x01][new_y02]==0 or gs.color_board[new_x01][new_y02]==2:
                if move_check(gs, i,j,new_x01,new_y02,1, item, target5, check)==True:
                    gs.black_king_target_value2=gs.black_king_target_value
                    gs.black_king_target_value=[new_x01,new_y02]

                    move_a=gs.color_board[new_x01][new_y02]
                    gs.color_board[new_x01][new_y02]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x01][new_y02]
                    gs.board[new_x01][new_y02]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y02][new_x01][0]))
                    move_h=gs.king_under_check
                    if check(2,gs):
                        gs.black_king_target_value=gs.black_king_target_value2
                        
                        gs.color_board[new_x01][new_y02]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][new_y02]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.black_king_target_value=gs.black_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(i-new_x02)==1 and abs(j-new_y01)==1 and new_x02!=-1 and new_y01!=-1:
            if gs.board[new_x02][new_y01]==0 or gs.color_board[new_x02][new_y01]==2:
                if move_check(gs, i,j,new_x02,new_y01,1, item, target5, check)==True:
                    gs.black_king_target_value2=gs.black_king_target_value
                    gs.black_king_target_value=[new_x02,new_y01]

                    move_a=gs.color_board[new_x02][new_y01]
                    gs.color_board[new_x02][new_y01]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x02][new_y01]
                    gs.board[new_x02][new_y01]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y01][new_x02][0]))
                    move_h=gs.king_under_check
                    if check(2,gs):
                        gs.black_king_target_value=gs.black_king_target_value2
                        
                        gs.color_board[new_x02][new_y01]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x02][new_y01]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.black_king_target_value=gs.black_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(i-new_x02)==1 and abs(j-new_y02)==1 and new_x02!=-1 and new_y02!=-1:
            if gs.board[new_x02][new_y02]==0 or gs.color_board[new_x02][new_y02]==2:
                if move_check(gs, i,j,new_x02,new_y02,1, item, target5, check)==True:
                    gs.black_king_target_value2=gs.black_king_target_value
                    gs.black_king_target_value=[new_x02,new_y02]

                    move_a=gs.color_board[new_x02][new_y02]
                    gs.color_board[new_x02][new_y02]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x02][new_y02]
                    gs.board[new_x02][new_y02]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y02][new_x02][0]))
                    move_h=gs.king_under_check
                    if check(2,gs):
                        gs.black_king_target_value=gs.black_king_target_value2
                        
                        gs.color_board[new_x02][new_y02]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x02][new_y02]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.black_king_target_value=gs.black_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h

        return False, i,j,c,item, target5
    
    else:

        if i<7:
            new_x01=i+1
        if i>0:
            new_x02=i-1
        if j<7:
            new_y01=j+1
        if j>0:
            new_y02=j-1

        if abs(i-new_x01)==1 and new_x01!=-1:
            if gs.board[new_x01][j]==0 or gs.color_board[new_x01][j]==1:
                if move_check(gs, i,j,new_x01,j,2, item, target5, check)==True:
                    gs.white_king_target_value2=gs.white_king_target_value
                    gs.white_king_target_value=[new_x01,j]
                    
                    move_a=gs.color_board[new_x01][j]
                    gs.color_board[new_x01][j]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x01][j]
                    gs.board[new_x01][j]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[j][new_x01][0]))
                    move_h=gs.king_under_check
                    if check(1,gs):
                        gs.white_king_target_value=gs.white_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.white_king_target_value=gs.white_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(i-new_x02)==1 and new_x02!=-1:
            if gs.board[new_x02][j]==0 or gs.color_board[new_x02][j]==1:
                if move_check(gs, i,j,new_x02,j,2, item, target5, check)==True:
                    gs.white_king_target_value2=gs.white_king_target_value
                    gs.white_king_target_value=[new_x02,j]

                    move_a=gs.color_board[new_x02][j]
                    gs.color_board[new_x02][j]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x02][j]
                    gs.board[new_x02][j]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[j][new_x02][0]))
                    move_h=gs.king_under_check
                    if check(1,gs):
                        gs.white_king_target_value=gs.white_king_target_value2
                        
                        gs.color_board[new_x02][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x02][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.white_king_target_value=gs.white_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(j-new_y01)==1 and new_y01!=-1:
            if gs.board[i][new_y01]==0 or gs.color_board[i][new_y01]==1:
                if move_check(gs, i,j,i,new_y01,2, item, target5, check)==True:
                    gs.white_king_target_value2=gs.white_king_target_value
                    gs.white_king_target_value=[i,new_y01]

                    move_a=gs.color_board[i][new_y01]
                    gs.color_board[i][new_y01]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[i][new_y01]
                    gs.board[i][new_y01]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y01][i][0]))
                    move_h=gs.king_under_check
                    if check(1,gs):
                        gs.white_king_target_value=gs.white_king_target_value2
                        
                        gs.color_board[i][new_y01]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[i][new_y01]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.white_king_target_value=gs.white_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(j-new_y02)==1 and new_y02!=-1:
            if gs.board[i][new_y02]==0 or gs.color_board[i][new_y02]==1:
                if move_check(gs, i,j,i,new_y02,2, item, target5, check)==True:
                    gs.white_king_target_value2=gs.white_king_target_value
                    gs.white_king_target_value=[i,new_y02]

                    move_a=gs.color_board[i][new_y02]
                    gs.color_board[i][new_y02]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[i][new_y02]
                    gs.board[i][new_y02]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y02][i][0]))
                    move_h=gs.king_under_check
                    if check(1,gs):
                        gs.white_king_target_value=gs.white_king_target_value2
                        
                        gs.color_board[i][new_y02]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[i][new_y02]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.white_king_target_value=gs.white_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h

        if abs(i-new_x01)==1 and abs(j-new_y01)==1 and new_x01!=-1 and new_y01!=-1:
            if gs.board[new_x01][new_y01]==0 or gs.color_board[new_x01][new_y01]==1:
                if move_check(gs, i,j,new_x01,new_y01,2, item, target5, check)==True:
                    gs.white_king_target_value2=gs.white_king_target_value
                    gs.white_king_target_value=[new_x01,new_y01]

                    move_a=gs.color_board[new_x01][new_y01]
                    gs.color_board[new_x01][new_y01]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x01][new_y01]
                    gs.board[new_x01][new_y01]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y01][new_x01][0]))
                    move_h=gs.king_under_check
                    if check(1,gs):
                        gs.white_king_target_value=gs.white_king_target_value2
                        
                        gs.color_board[new_x01][new_y01]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][new_y01]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h

                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.white_king_target_value=gs.white_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(i-new_x01)==1 and abs(j-new_y02)==1 and new_x01!=-1 and new_y02!=-1:
            if gs.board[new_x01][new_y02]==0 or gs.color_board[new_x01][new_y02]==1:
                if move_check(gs, i,j,new_x01,new_y02,2, item, target5, check)==True:
                    gs.white_king_target_value2=gs.white_king_target_value
                    gs.white_king_target_value=[new_x01,new_y02]

                    move_a=gs.color_board[new_x01][new_y02]
                    gs.color_board[new_x01][new_y02]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x01][new_y02]
                    gs.board[new_x01][new_y02]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y02][new_x01][0]))
                    move_h=gs.king_under_check
                    if check(1,gs):
                        gs.white_king_target_value=gs.white_king_target_value2
                        
                        gs.color_board[new_x01][new_y02]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][new_y02]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.white_king_target_value=gs.white_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(i-new_x02)==1 and abs(j-new_y01)==1 and new_x02!=-1 and new_y01!=-1:
            if gs.board[new_x02][new_y01]==0 or gs.color_board[new_x02][new_y01]==1:
                if move_check(gs, i,j,new_x02,new_y01,2, item, target5, check)==True:
                    gs.white_king_target_value2=gs.white_king_target_value
                    gs.white_king_target_value=[new_x02,new_y01]

                    move_a=gs.color_board[new_x02][new_y01]
                    gs.color_board[new_x02][new_y01]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x02][new_y01]
                    gs.board[new_x02][new_y01]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y01][new_x02][0]))
                    move_h=gs.king_under_check
                    if check(1,gs):
                        gs.white_king_target_value=gs.white_king_target_value2
                        
                        gs.color_board[new_x02][new_y01]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x02][new_y01]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.white_king_target_value=gs.white_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        if abs(i-new_x02)==1 and abs(j-new_y02)==1 and new_x02!=-1 and new_y02!=-1:
            if gs.board[new_x02][new_y02]==0 or gs.color_board[new_x02][new_y02]==1:
                if move_check(gs, i,j,new_x02,new_y02,2, item, target5, check)==True:
                    gs.white_king_target_value2=gs.white_king_target_value
                    gs.white_king_target_value=[new_x02,new_y02]

                    move_a=gs.color_board[new_x02][new_y02]
                    gs.color_board[new_x02][new_y02]=move_a
                    move_b=gs.color_board[i][j]
                    gs.color_board[i][j]=0
                    move_c=gs.board[new_x02][new_y02]
                    gs.board[new_x02][new_y02]=item
                    move_f=gs.board[i][j]
                    gs.board[i][j]=0
                    move_g=gs.position[target5]
                    gs.position[target5]=gs.piece[target5].get_rect(center=(gs.pos[j][i][1],gs.pos[new_y02][new_x02][0]))
                    move_h=gs.king_under_check
                    if check(1,gs):
                        gs.white_king_target_value=gs.white_king_target_value2
                        
                        gs.color_board[new_x02][new_y02]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x02][new_y02]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
                        # check(2,gs)
                        return True, i,j,c,item, target5
                    else:
                        gs.white_king_target_value=gs.white_king_target_value2

                        gs.color_board[new_x01][j]=move_a
                        gs.color_board[i][j]=move_b
                        gs.board[new_x01][j]=move_c
                        gs.board[i][j]=move_f
                        gs.position[target5]=move_g
                        gs.king_under_check=move_h
        
        return False, i,j,c,item, target5
