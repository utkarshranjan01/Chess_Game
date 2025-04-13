from src.variables import *
from src.conditions_checker_call import *

def morphing_piece(gs, ntw, screen ,moves_left, check, repeat_check, checkmate, moves_draw, check_only_king_left):
    if gs.morph_variable==1:
        if (gs.opponent_in_menu!=1):
            screen.blit(morph_background,morph_back_rect)
            screen.blit(morph1,morph_rect)

            if (gs.morph_list[0]).collidepoint(gs.mouse_coordinate):
                if gs.hovering_sound!=0:
                    sound_click.play()
                    gs.hovering_sound=0
                screen.blit(morph1_big_q,(140,height/2-27))
            else:
                screen.blit(morph1_small_q,(145,height/2-22))
                if gs.hovering_sound==0:
                    gs.hovering_sound=-1

            if (gs.morph_list[1]).collidepoint(gs.mouse_coordinate):
                if gs.hovering_sound!=1:
                    sound_click.play()
                    gs.hovering_sound=1
                screen.blit(morph1_big_k,(200,height/2-27))
            else:
                screen.blit(morph1_small_k,(205,height/2-22))
                if gs.hovering_sound==1:
                    gs.hovering_sound=-1

            if (gs.morph_list[2]).collidepoint(gs.mouse_coordinate):
                if gs.hovering_sound!=2:
                    sound_click.play()
                    gs.hovering_sound=2
                screen.blit(morph1_big_r,(260,height/2-27))
            else:
                screen.blit(morph1_small_r,(265,height/2-22))
                if gs.hovering_sound==2:
                    gs.hovering_sound=-1

            if (gs.morph_list[3]).collidepoint(gs.mouse_coordinate):
                if gs.hovering_sound!=3:
                    sound_click.play()
                    gs.hovering_sound=3
                screen.blit(morph1_big_b,(315,height/2-27))
            else:
                screen.blit(morph1_small_b,(320,height/2-22))
                if gs.hovering_sound==3:
                    gs.hovering_sound=-1

            if ((gs.morph_list[0]).collidepoint(gs.mouse_coordinate)==False and (gs.morph_list[1]).collidepoint(gs.mouse_coordinate)==False and (gs.morph_list[2]).collidepoint(gs.mouse_coordinate)==False and (gs.morph_list[3]).collidepoint(gs.mouse_coordinate)==False):
                gs.hovering_sound=-1

    if gs.morph_variable==2:
        if (gs.opponent_in_menu!=1):
            screen.blit(morph_background,morph_back_rect)
            screen.blit(morph2,morph_rect)

            if (gs.morph_list[0]).collidepoint(gs.mouse_coordinate):
                if gs.hovering_sound!=0:
                    sound_click.play()
                    gs.hovering_sound=0
                screen.blit(morph2_big_q,(140,height/2-27))
            else:
                screen.blit(morph2_small_q,(145,height/2-22))
                if gs.hovering_sound==0:
                    gs.hovering_sound=-1

            if (gs.morph_list[1]).collidepoint(gs.mouse_coordinate):
                if gs.hovering_sound!=1:
                    sound_click.play()
                    gs.hovering_sound=1
                screen.blit(morph2_big_k,(200,height/2-27))
            else:
                screen.blit(morph2_small_k,(205,height/2-22))
                if gs.hovering_sound==1:
                    gs.hovering_sound=-1

            if (gs.morph_list[2]).collidepoint(gs.mouse_coordinate):
                if gs.hovering_sound!=2:
                    sound_click.play()
                    gs.hovering_sound=2
                screen.blit(morph2_big_r,(260,height/2-27))
            else:
                screen.blit(morph2_small_r,(265,height/2-22))
                if gs.hovering_sound==2:
                    gs.hovering_sound=-1

            if (gs.morph_list[3]).collidepoint(gs.mouse_coordinate):
                if gs.hovering_sound!=3:
                    sound_click.play()
                    gs.hovering_sound=3
                screen.blit(morph2_big_b,(315,height/2-27))
            else:
                screen.blit(morph2_small_b,(320,height/2-22))
                if gs.hovering_sound==3:
                    gs.hovering_sound=-1

    if gs.morph_piece!=-1 and gs.morph_target!=-1:
        if gs.morph_piece==0:
            gs.board[gs.morph_target[0]][gs.morph_target[1]]=4
            gs.color_board[gs.morph_target[0]][gs.morph_target[1]]=gs.morph_target[2]
            gs.morph_piece=-1
            gs.morph_variable=0
            gs.opponent_in_menu=0
            gs.move_made_by_opponent=1
            gs.hovering_sound=-1
            sound_promote.play()
            if gs.morph_target[2]==1:
                gs.piece[gs.morph_pos]=pygame.image.load(ASSETS_DIR / "black/bq.png").convert_alpha()
            elif gs.morph_target[2]==2:
                gs.piece[gs.morph_pos]=pygame.image.load(ASSETS_DIR / "white/wq.png").convert_alpha()
            gs.morph_target=-1
            gs.morph_pos=-1
        if gs.morph_piece==1:
            gs.board[gs.morph_target[0]][gs.morph_target[1]]=2
            gs.color_board[gs.morph_target[0]][gs.morph_target[1]]=gs.morph_target[2]
            gs.morph_piece=-1
            gs.morph_variable=0
            gs.opponent_in_menu=0
            gs.hovering_sound=-1
            sound_promote.play()
            if gs.morph_target[2]==1:
                gs.piece[gs.morph_pos]=pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha()
            elif gs.morph_target[2]==2:
                gs.piece[gs.morph_pos]=pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha()
            gs.morph_target=-1
            gs.morph_pos=-1
        if gs.morph_piece==2:
            gs.board[gs.morph_target[0]][gs.morph_target[1]]=1
            gs.color_board[gs.morph_target[0]][gs.morph_target[1]]=gs.morph_target[2]
            gs.morph_piece=-1
            gs.morph_variable=0
            gs.opponent_in_menu=0
            gs.hovering_sound=-1
            sound_promote.play()
            if gs.morph_target[2]==1:
                gs.piece[gs.morph_pos]=pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha()
            elif gs.morph_target[2]==2:
                gs.piece[gs.morph_pos]=pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha()
            gs.morph_target=-1
            gs.morph_pos=-1
        if gs.morph_piece==3:
            gs.board[gs.morph_target[0]][gs.morph_target[1]]=3
            gs.color_board[gs.morph_target[0]][gs.morph_target[1]]=gs.morph_target[2]
            gs.morph_piece=-1
            gs.morph_variable=0
            gs.opponent_in_menu=0
            gs.hovering_sound=-1
            sound_promote.play()
            if gs.morph_target[2]==1:
                gs.piece[gs.morph_pos]=pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha()
            elif gs.morph_target[2]==2:
                gs.piece[gs.morph_pos]=pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha()
            gs.morph_target=-1
            gs.morph_pos=-1

        if moves_left(1,gs)==True and check(2,gs)==False:
            sound_check.play()
        elif moves_left(2,gs)==True and check(1,gs)==False:
            sound_check.play()

        conditions_checker_call(gs, moves_left, check, repeat_check, checkmate, moves_draw, check_only_king_left)

def morph_check(gs):
    for i in range(8):
        for j in range(8):
            if i==0:
                if gs.board[i][j]==6 and gs.color_board[i][j]==1:
                    gs.morph_variable=1
                    sound_promote.play()
                    gs.morph_target=[i,j,1]
                    for i in range(len(gs.position)):
                        if gs.position[i].collidepoint(gs.mouse_coordinate):
                            if (i in gs.out):
                                pass
                            else:
                                gs.morph_pos=i
                elif gs.board[i][j]==6 and gs.color_board[i][j]==2:
                    gs.morph_variable=2
                    sound_promote.play()
                    gs.morph_target=[i,j,2]
                    for i in range(len(gs.position)):
                        if gs.position[i].collidepoint(gs.mouse_coordinate):
                            if (i in gs.out):
                                pass
                            else:
                                gs.morph_pos=i
            elif i==7:
                if gs.board[i][j]==6 and gs.color_board[i][j]==1:
                    gs.morph_variable=1
                    sound_promote.play()
                    gs.morph_target=[i,j,1]
                    for i in range(len(gs.position)):
                        if gs.position[i].collidepoint(gs.mouse_coordinate):
                            if (i in gs.out):
                                pass
                            else:
                                gs.morph_pos=i
                elif gs.board[i][j]==6 and gs.color_board[i][j]==2:
                    gs.morph_variable=2
                    sound_promote.play()
                    gs.morph_target=[i,j,2]
                    for i in range(len(gs.position)):
                        if gs.position[i].collidepoint(gs.mouse_coordinate):
                            if (i in gs.out):
                                pass
                            else:
                                gs.morph_pos=i


def morph_check_online(gs):
    for i in range(8):
        for j in range(8):
            if i==0:
                if gs.board[i][j]==6 and gs.color_board[i][j]==1:
                    gs.morph_variable=1
                    gs.opponent_in_menu=1
                    sound_promote.play()
                    gs.morph_target=[i,j,1]
                    for i in range(len(gs.position)):
                        if gs.position[i].collidepoint(gs.mouse_coordinate):
                            if (i in gs.out):
                                pass
                            else:
                                gs.morph_pos=i
                elif gs.board[i][j]==6 and gs.color_board[i][j]==2:
                    gs.morph_variable=2
                    gs.opponent_in_menu=1
                    sound_promote.play()
                    gs.morph_target=[i,j,2]
                    for i in range(len(gs.position)):
                        if gs.position[i].collidepoint(gs.mouse_coordinate):
                            if (i in gs.out):
                                pass
                            else:
                                gs.morph_pos=i
            elif i==7:
                if gs.board[i][j]==6 and gs.color_board[i][j]==1:
                    gs.morph_variable=1
                    gs.opponent_in_menu=1
                    sound_promote.play()
                    gs.morph_target=[i,j,1]
                    for i in range(len(gs.position)):
                        if gs.position[i].collidepoint(gs.mouse_coordinate):
                            if (i in gs.out):
                                pass
                            else:
                                gs.morph_pos=i
                elif gs.board[i][j]==6 and gs.color_board[i][j]==2:
                    gs.morph_variable=2
                    gs.opponent_in_menu=1
                    sound_promote.play()
                    gs.morph_target=[i,j,2]
                    for i in range(len(gs.position)):
                        if gs.position[i].collidepoint(gs.mouse_coordinate):
                            if (i in gs.out):
                                pass
                            else:
                                gs.morph_pos=i


def morph_selecting_piece(gs, ntw, write):
    if gs.morph_variable!=0:
        if (gs.morph_list[0]).collidepoint(gs.mouse_coordinate):
            gs.morph_piece=0

        if (gs.morph_list[1]).collidepoint(gs.mouse_coordinate):
            gs.morph_piece=1

        if (gs.morph_list[2]).collidepoint(gs.mouse_coordinate):
            gs.morph_piece=2

        if (gs.morph_list[3]).collidepoint(gs.mouse_coordinate):
            gs.morph_piece=3

        if gs.morph_piece==1 or gs.morph_piece==2 or gs.morph_piece==3 or gs.morph_piece==0:
            gs.message_content=(f"mouse {gs.mouse_x1_coordinate},{gs.mouse_y1_coordinate},{gs.mouse_x2_coordinate},{gs.mouse_y2_coordinate}|")
            write(gs, ntw)

        return False
    return True

def morph_selecting_piece2(gs, ntw):
    function_result = True
    if gs.morph_variable!=0:
        if (gs.morph_list[0]).collidepoint(gs.mouse_coordinate):
            gs.morph_piece=0
            gs.move_made_by_opponent=1

        if (gs.morph_list[1]).collidepoint(gs.mouse_coordinate):
            gs.morph_piece=1
            gs.move_made_by_opponent=1

        if (gs.morph_list[2]).collidepoint(gs.mouse_coordinate):
            gs.morph_piece=2
            gs.move_made_by_opponent=1

        if (gs.morph_list[3]).collidepoint(gs.mouse_coordinate):
            gs.morph_piece=3
            gs.move_made_by_opponent=1

        function_result = False
    return function_result