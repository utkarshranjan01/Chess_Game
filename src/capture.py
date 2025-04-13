def capture2(gs, ntw, check, write, sound_illegal, sound_check, sound_capture):

    # if gs.target<=15 and gs.final_selected_color==2:
    #     return None

    # if gs.target>15 and gs.final_selected_color==1:
    #     return None

    move_a=0
    move_b=0
    move_c=0
    move_f=0
    move_g=0
    move_d=gs.cpos1
    move_e=gs.cpos2
    cca=gs.ca
    ccb=gs.cb
    cca1=gs.ca1
    ccb1=gs.cb1
    gs.gone=gs.board[gs.selected[1]][gs.selected[0]]
    if gs.target2!=-1:
        gs.out.append(gs.target2)
    move_a=gs.color_board[gs.selected[1]][gs.selected[0]]
    if gs.target<=15:
        gs.color_board[gs.selected[1]][gs.selected[0]]=1
    else:
        gs.color_board[gs.selected[1]][gs.selected[0]]=2
    move_b=gs.color_board[gs.select[1]][gs.select[0]]
    gs.color_board[gs.select[1]][gs.select[0]]=0

    move_c=gs.board[gs.selected[1]][gs.selected[0]]
    gs.board[gs.selected[1]][gs.selected[0]]=gs.value
    gs.cpos1=(gs.selected[1],gs.selected[0])
    move_f=gs.board[gs.select[1]][gs.select[0]]
    gs.board[gs.select[1]][gs.select[0]]=0
    gs.cpos2=(gs.select[1],gs.select[0])
    gs.ca=gs.a
    gs.cb=gs.b
    gs.ca1=gs.a1
    gs.cb1=gs.b1
    if gs.target!=-1:
        move_g=gs.position[gs.target]
        gs.position[gs.target]=gs.piece[gs.target].get_rect(center=(gs.pos[gs.selected[0]][gs.selected[1]][1],gs.pos[gs.selected[0]][gs.selected[1]][0]))
    gs.clicks=0
    gs.target0=-1
    gs.moved=1

    if gs.target<=15:
        if check(2,gs)==False:
            sound_illegal.play()
            gs.ca=cca
            gs.cb=ccb
            gs.ca1=cca1
            gs.cb1=ccb1
            gs.cpos1=move_d
            gs.cpos2=move_e
            gs.moved=0
            if gs.value==5:
                if gs.target<=15:
                    gs.black_king_target_value=[gs.selected[1],gs.selected[0]]
                else:
                    gs.white_king_target_value=[gs.selected[1],gs.selected[0]]
            gs.color_board[gs.selected[1]][gs.selected[0]]=move_a
            gs.color_board[gs.select[1]][gs.select[0]]=move_b
            gs.board[gs.selected[1]][gs.selected[0]]=move_c
            gs.board[gs.select[1]][gs.select[0]]=move_f
            if gs.target!=-1:
                gs.position[gs.target]=move_g
            if gs.target2!=-1:
                gs.out.remove(gs.target2)
        else:
            if check(1,gs)==False:
                sound_check.play()
            else:
                sound_capture.play()
            gs.total_moves+=1
            gs.message_content="moved|"
            write(gs, ntw)
            gs.draw_total_moves=0
            for i in range(8):
                for j in range(8):
                    if gs.board[i][j]==7:
                        gs.board[i][j]=6
            gs.moves_since_en_pessant=0
            gs.board_copy.append([[[0 for _ in range(8)] for _ in range(8)],[[0 for _ in range(8)] for _ in range(8)]])
            for i in range(8):
                for j in range(8):
                    gs.board_copy[len(gs.board_copy)-1][0][i][j]=gs.board[i][j]
                    gs.board_copy[len(gs.board_copy)-1][1][i][j]=gs.color_board[i][j]

        gs.select=[-1,-1]
        gs.selected=[-1,-1]

    elif gs.target>15:
        if check(1,gs)==False:
            sound_illegal.play()
            gs.moved=0
            gs.ca=cca
            gs.cb=ccb
            gs.ca1=cca1
            gs.cb1=ccb1
            gs.cpos1=move_d
            gs.cpos2=move_e
            if gs.value==5:
                if gs.target<=15:
                    gs.black_king_target_value=[gs.selected[1],gs.selected[0]]
                else:
                    gs.white_king_target_value=[gs.selected[1],gs.selected[0]]
            gs.color_board[gs.selected[1]][gs.selected[0]]=move_a
            gs.color_board[gs.select[1]][gs.select[0]]=move_b
            gs.board[gs.selected[1]][gs.selected[0]]=move_c
            gs.board[gs.select[1]][gs.select[0]]=move_f
            if gs.target!=-1:
                gs.position[gs.target]=move_g
            if gs.target2!=-1:
                gs.out.remove(gs.target2)
        else:
            if check(2,gs)==False:
                sound_check.play()
            else:
                sound_capture.play()
            gs.total_moves+=1
            gs.message_content="gs.moved|"
            write(gs, ntw)
            gs.draw_total_moves=0
            for i in range(8):
                for j in range(8):
                    if gs.board[i][j]==7:
                        gs.board[i][j]=6
            gs.moves_since_en_pessant=0
            gs.board_copy.append([[[0 for _ in range(8)] for _ in range(8)],[[0 for _ in range(8)] for _ in range(8)]])
            for i in range(8):
                for j in range(8):
                    gs.board_copy[len(gs.board_copy)-1][0][i][j]=gs.board[i][j]
                    gs.board_copy[len(gs.board_copy)-1][1][i][j]=gs.color_board[i][j]

        gs.select=[-1,-1]
        gs.selected=[-1,-1]
