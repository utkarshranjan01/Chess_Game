def move_selected_piece(gs, ntw, capture, move, check, clean, rook_check, bishop_check, knight_check, king_move, capture_test):

    sending_result=0

    if gs.target!=-1:
        gs.value=gs.board[gs.select[1]][gs.select[0]]
        gs.val2=gs.board[gs.selected[1]][gs.selected[0]]
        if gs.value==6 or gs.value==7:
            if gs.select[1]==1 and gs.board[gs.selected[1]][gs.selected[0]]==0 and gs.color_board[gs.select[1]][gs.select[0]]==1:
                if (gs.selected[0]==gs.select[0]):
                    if ((gs.selected[1]-gs.select[1])==1 or (gs.selected[1]-gs.select[1])==2):
                        if (gs.selected[1]-gs.select[1])==2:
                            gs.value=7
                        move(gs, ntw)
            elif gs.select[1]==6 and gs.board[gs.selected[1]][gs.selected[0]]==0 and gs.color_board[gs.select[1]][gs.select[0]]==2:
                if (gs.selected[0]==gs.select[0]):
                    if ((gs.select[1]-gs.selected[1])==1 or (gs.select[1]-gs.selected[1])==2):
                        if (gs.select[1]-gs.selected[1])==2:
                            gs.value=7
                        move(gs, ntw)
            elif (gs.target>=24 and gs.target<32 and gs.board[gs.selected[1]][gs.selected[0]]==0):
                if (gs.selected[0]==gs.select[0]):
                    if ((gs.select[1]-gs.selected[1])==1):
                        move(gs, ntw)
                #en pessant
                if (((gs.select[0]-1)==gs.selected[0])) and gs.board[gs.selected[1]+1][gs.selected[0]]==7:
                    if ((gs.select[1]-gs.selected[1])==1):
                        gs.gone=gs.board[gs.select[1]][gs.select[0]-1]
                        if gs.board[gs.select[1]][gs.select[0]-1]==7:
                            gs.find=tuple(gs.pos[gs.select[1]][gs.select[0]-1])
                            capture_test(2,gs, ntw)
                        if gs.samec==0:
                            move(gs, ntw)
                        else:
                            gs.samec=0
                #en pessant
                elif  (gs.select[0]+1)==gs.selected[0] and gs.board[gs.selected[1]+1][gs.selected[0]]==7:
                    if ((gs.select[1]-gs.selected[1])==1):
                        gs.gone=gs.board[gs.select[1]][gs.select[0]+1]
                        if gs.board[gs.select[1]][gs.select[0]+1]==7:
                            gs.find=tuple(gs.pos[gs.select[1]][gs.select[0]+1])
                            capture_test(2,gs, ntw)
                        if gs.samec==0:
                            move(gs, ntw)
                        else:
                            gs.samec=0


            elif (gs.target>=8 and gs.target<16 and gs.board[gs.selected[1]][gs.selected[0]]==0):
                if (gs.selected[0]==gs.select[0]):
                    if ((gs.selected[1]-gs.select[1])==1):
                        move(gs, ntw)
                #en pessant
                if (((gs.select[0]-1)==gs.selected[0])) and gs.board[gs.selected[1]-1][gs.selected[0]]==7:  
                    if ((gs.selected[1]-gs.select[1])==1):
                        gs.gone=gs.board[gs.select[1]][gs.select[0]-1]
                        if gs.board[gs.select[1]][gs.select[0]-1]==7:
                            gs.find=tuple(gs.pos[gs.select[1]][gs.select[0]-1])
                            capture_test(1,gs, ntw)
                        if gs.samec==0:
                            move(gs, ntw)
                        else:
                            gs.samec=0

                #en pessant
                elif (gs.select[0]+1)==gs.selected[0] and gs.board[gs.selected[1]-1][gs.selected[0]]==7:
                    if (abs(gs.selected[1]-gs.select[1])==1):
                        gs.gone=gs.board[gs.select[1]][gs.select[0]+1]
                        if gs.board[gs.select[1]][gs.select[0]+1]==7:
                            gs.find=tuple(gs.pos[gs.select[1]][gs.select[0]+1])
                            capture_test(1,gs, ntw)
                        if gs.samec==0:
                            move(gs, ntw)
                        else:
                            gs.samec=0


            elif gs.target>=24 and gs.target<32 and gs.board[gs.selected[1]][gs.selected[0]]!=0 and (gs.target2<=15):
                if (gs.select[0]-1)==gs.selected[0] and gs.board[gs.selected[1]][gs.selected[0]]!=0:
                    if ((gs.select[1]-gs.selected[1])==1):
                        capture(gs, ntw)
                if (gs.select[0]+1)==gs.selected[0] and gs.board[gs.selected[1]][gs.selected[0]]!=0:
                    if ((gs.select[1]-gs.selected[1])==1):
                        capture(gs, ntw)

            elif gs.target>=8 and gs.target<16 and gs.board[gs.selected[1]][gs.selected[0]]!=0 and (gs.target2>15):
                if (gs.selected[0]-1)==gs.select[0] and gs.board[gs.selected[1]][gs.selected[0]]!=0:
                    if ((gs.selected[1]-gs.select[1])==1):
                        capture(gs, ntw)
                if (gs.selected[0]+1)==gs.select[0] and gs.board[gs.selected[1]][gs.selected[0]]!=0:
                    if ((gs.selected[1]-gs.select[1])==1):
                        capture(gs, ntw)

            check(0,gs)
            clean(gs)
        
        elif gs.value==1:
            test_var1=gs.select
            test_var2=gs.selected
            if gs.board[gs.selected[1]][gs.selected[0]]==0 and rook_check(gs, 0):
                move(gs, ntw)

            elif gs.board[gs.selected[1]][gs.selected[0]]!=0 and rook_check(gs, 1):
                capture(gs, ntw)
            check(0,gs)
            if gs.moved==1 and test_var1[1]==0 and test_var1[0]==0 and gs.color_board[test_var2[1]][test_var2[0]]==1:
                gs.black_left_rook_has_moved=1
            if gs.moved==1 and test_var1[1]==0 and test_var1[0]==7 and gs.color_board[test_var2[1]][test_var2[0]]==1:
                gs.black_right_rook_has_moved=1
            if gs.moved==1 and test_var1[1]==7 and test_var1[0]==0 and gs.color_board[test_var2[1]][test_var2[0]]==2:
                gs.white_left_rook_has_moved=1
            if gs.moved==1 and test_var1[1]==7 and test_var1[0]==7 and gs.color_board[test_var2[1]][test_var2[0]]==2:
                gs.white_right_rook_has_moved=1
            clean(gs)
        
        elif gs.value==3:
            if gs.board[gs.selected[1]][gs.selected[0]]==0 and bishop_check(gs, 0):
                move(gs, ntw)

            elif gs.board[gs.selected[1]][gs.selected[0]]!=0 and bishop_check(gs, 1):
                capture(gs, ntw)
            check(0,gs)
            clean(gs)
        
        elif gs.value==4:
            if gs.board[gs.selected[1]][gs.selected[0]]==0:
                if bishop_check(gs, 0):
                    move(gs, ntw)
                elif rook_check(gs, 0):
                    move(gs, ntw)
            else:
                if bishop_check(gs, 1):
                    capture(gs, ntw)
                elif rook_check(gs, 1):
                    capture(gs, ntw)
            check(0,gs)
            clean(gs)

        elif gs.value==2:
            if gs.board[gs.selected[1]][gs.selected[0]]==0 and knight_check(gs, 0):
                move(gs, ntw)
            elif knight_check(gs, 1):
                capture(gs, ntw)
            check(0,gs)
            clean(gs)

        elif gs.value==5:
            test_var1=gs.select
            test_var2=gs.selected
            if gs.board[gs.selected[1]][gs.selected[0]]==0 and king_move(0,gs):
                move(gs, ntw)
            elif king_move(1,gs):
                capture(gs, ntw)
            check(0,gs)
            if gs.moved==1 and test_var1[1]==0 and test_var1[0]==4 and gs.color_board[test_var2[1]][test_var2[0]]==1:
                gs.black_king_has_moved=1
            if gs.moved==1 and test_var1[1]==7 and test_var1[0]==4 and gs.color_board[test_var2[1]][test_var2[0]]==2:
                gs.white_king_has_moved=1
            clean(gs)
    

