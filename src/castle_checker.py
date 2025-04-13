import math

def castle_checker(gs,c, check): # For making guiding block color for castle not used in checking castle
    ani1=0
    ani2=0
    ani3=0
    check_counter=0
    end1=0
    end2=0
    end3=0
    end4=0
    final=[]
    start_y, start_x = gs.select

    original_check=gs.king_under_check

    if gs.target<=15  and start_x==0 and start_y==4 and gs.black_king_has_moved==0 and gs.black_left_rook_has_moved==0 and gs.board[start_x][start_y]==5 and gs.board[0][0]==1 and gs.color_board[0][0]==1 and gs.color_board[start_x][start_y]==1 and gs.board[start_x][start_y-1]==0 and gs.board[start_x][start_y-2]==0 and gs.board[start_x][start_y-3]==0 and c==1 and check(2,gs):
            ani1=gs.black_king_target_value
            ani2=gs.board[0][4]
            ani3=gs.color_board[0][4]
            if check(2,gs)==True:
                check_counter+=1
            gs.board[0][4]=0
            gs.board[0][3]=5
            gs.color_board[0][4]=0
            gs.color_board[0][3]=1
            gs.black_king_target_value=[start_x,start_y-1]
            if check(2,gs)==True:
                check_counter+=1
            gs.board[0][3]=0
            gs.board[0][2]=5
            gs.color_board[0][3]=0
            gs.color_board[0][2]=1
            gs.black_king_target_value=[start_x,start_y-2]
            if check(2,gs)==True:
                check_counter+=1
            gs.board[0][2]=0
            gs.board[0][1]=5
            gs.color_board[0][2]=0
            gs.color_board[0][1]=1
            gs.black_king_target_value=[start_x,start_y-3]
            if check(2,gs)==True:
                check_counter+=1
            gs.board[0][4]=ani2
            gs.board[0][3]=0
            gs.board[0][2]=0
            gs.board[0][1]=0
            gs.color_board[0][4]=ani3
            gs.color_board[0][3]=0
            gs.color_board[0][2]=0
            gs.color_board[0][1]=0
            gs.black_king_target_value=ani1
            if check_counter==4:
                end1=1
                gs.castle_black_1=1

    check_counter=0
    if gs.target<=15 and start_x==0 and start_y==4 and gs.black_king_has_moved==0 and gs.black_right_rook_has_moved==0 and gs.board[start_x][start_y]==5 and gs.board[0][7]==1 and gs.color_board[0][7]==1 and gs.color_board[start_x][start_y]==1 and gs.board[start_x][start_y+1]==0 and gs.board[start_x][start_y+2]==0 and c==1 and check(1,gs):
            ani1=gs.black_king_target_value
            ani2=gs.board[0][4]
            ani3=gs.color_board[0][4]
            if check(2,gs)==True:
                check_counter+=1
            gs.board[0][4]=0
            gs.board[0][5]=5
            gs.color_board[0][4]=0
            gs.color_board[0][5]=1
            gs.black_king_target_value=[start_x,start_y+1]
            if check(2,gs)==True:
                check_counter+=1
            gs.board[0][5]=0
            gs.board[0][6]=5
            gs.color_board[0][5]=0
            gs.color_board[0][6]=1
            gs.black_king_target_value=[start_x,start_y+2]
            if check(2,gs)==True:
                check_counter+=1
            gs.board[0][4]=ani2
            gs.board[0][5]=0
            gs.board[0][6]=0
            gs.color_board[0][4]=ani3
            gs.color_board[0][5]=0
            gs.color_board[0][6]=0
            gs.black_king_target_value=ani1
            if check_counter==3:
                end2=1
                gs.castle_black_2=1

    check_counter=0
    if c==1 and end1==1 and end2==1:
        final.append(1)
        final.append(1)
    elif c==1 and end1==1:
        final.append(1)
        final.append(0)
    elif c==1 and end2==1:
        final.append(0)
        final.append(1)
    else: 
        final.append(0)
        final.append(0)
    check_counter=0
    if gs.target>15 and start_x==7 and start_y==4 and gs.white_king_has_moved==0 and gs.white_left_rook_has_moved==0 and gs.board[start_x][start_y]==5 and gs.board[7][0]==1 and gs.color_board[7][0]==2 and gs.color_board[start_x][start_y]==2 and gs.board[start_x][start_y-1]==0 and gs.board[start_x][start_y-2]==0 and gs.board[start_x][start_y-3]==0 and c==2:
            ani1=gs.white_king_target_value
            ani2=gs.board[7][4]
            ani3=gs.color_board[7][4]
            if check(1,gs)==True:
                check_counter+=1
            gs.board[7][4]=0
            gs.board[7][3]=5
            gs.color_board[7][4]=0
            gs.color_board[7][3]=2
            gs.white_king_target_value=[start_x,start_y-1]
            if check(1,gs)==True:
                check_counter+=1
            gs.board[7][3]=0
            gs.board[7][2]=5
            gs.color_board[7][3]=0
            gs.color_board[7][2]=2
            gs.white_king_target_value=[start_x,start_y-2]
            if check(1,gs)==True:
                check_counter+=1
            gs.board[7][2]=0
            gs.board[7][1]=5
            gs.color_board[7][2]=0
            gs.color_board[7][1]=2
            gs.white_king_target_value=[start_x,start_y-3]
            if check(1,gs)==True:
                check_counter+=1
            gs.board[7][4]=ani2
            gs.board[7][3]=0
            gs.board[7][2]=0
            gs.board[7][1]=0
            gs.color_board[7][4]=ani3
            gs.color_board[7][3]=0
            gs.color_board[7][2]=0
            gs.color_board[7][1]=0
            gs.white_king_target_value=ani1
            if check_counter==4:
                end3=1
                gs.castle_white_1=1

    check_counter=0
    if gs.target>15 and start_x==7 and start_y==4 and gs.white_king_has_moved==0 and gs.white_right_rook_has_moved==0 and gs.board[start_x][start_y]==5 and gs.board[7][7]==1 and gs.color_board[7][7]==2 and gs.color_board[start_x][start_y]==2 and gs.board[start_x][start_y+1]==0 and gs.board[start_x][start_y+2]==0 and c==2:
            ani1=gs.white_king_target_value
            ani2=gs.board[7][4]
            ani3=gs.color_board[7][4]
            if check(1,gs)==True:
                check_counter+=1
            gs.board[7][4]=0
            gs.board[7][5]=5
            gs.color_board[7][4]=0
            gs.color_board[7][5]=2
            gs.white_king_target_value=[start_x,start_y+1]
            if check(1,gs)==True:
                check_counter+=1
            gs.board[7][5]=0
            gs.board[7][6]=5
            gs.color_board[7][5]=0
            gs.color_board[7][6]=2
            gs.white_king_target_value=[start_x,start_y+2]
            if check(1,gs)==True:
                check_counter+=1
            gs.board[7][4]=ani2
            gs.board[7][5]=0
            gs.board[7][6]=0
            gs.color_board[7][4]=ani3
            gs.color_board[7][5]=0
            gs.color_board[7][6]=0
            gs.white_king_target_value=ani1
            if check_counter==3:
                end4=1
                gs.castle_white_2=1

    check_counter=0
    if c==2 and end3==1 and end4==1:
        final.append(1)
        final.append(1)
    elif c==2 and end3==1:
        final.append(1)
        final.append(0)
    elif c==2 and end4==1:
        final.append(0)
        final.append(1)
    else: 
        final.append(0)
        final.append(0)

    gs.king_under_check = original_check
    

def castle_logic_checking(gs, check, ntw):
     for i in range(len(gs.position)):
        if gs.position[i].collidepoint(gs.mouse_coordinate):
            if (i in gs.out):
                pass
            elif gs.select!=[-1,-1]:
                gs.__select=[math.floor(gs.position[i].x/64),math.floor(gs.position[i].y/64)]
                if gs.color_board[gs.select[1]][gs.select[0]]==gs.color_board[gs.__select[1]][gs.__select[0]] and gs.__select!=gs.select:
                    gs.select=gs.__select
                    gs.noc=1
                    gs.target0=i
                    gs.target=i
                    gs.found=1
                    gs.a=gs.position[i].x
                    gs.b=gs.position[i].y
                    gs.t1=math.floor(gs.a/64)
                    gs.t2=math.floor(gs.b/64)
                    if gs.board[gs.select[1]][gs.select[0]]==5 and gs.target<=15 and gs.castle_black_done==0:
                        castle_checker(gs, 1, check)
                    if gs.board[gs.select[1]][gs.select[0]]==5 and gs.target>15 and gs.castle_white_done==0:
                        castle_checker(gs, 2, check)

                    if gs.board[gs.select[1]][gs.select[0]] !=5:
                        gs.castle_black_1 = gs.castle_black_2 = gs.castle_white_1 = gs.castle_white_2 = 0
                    gs.t3=gs.t1+gs.t2
                    if gs.t3%2==0:
                        gs.flag=2
                        break
                    else:
                        gs.flag=1
                        break