from src.__init__ import *

def move_king(gs, i,j,c,item, target5):

    val22, i,j,c,item, target5 = move_king2(gs,i,j,c,item, target5, move_check, check)

    return val22

def moves_left(c,gs):

    val22, c = moves_left2(gs, c, check, move_check, move_pawn, move_rook, move_knight, move_bishop, move_king)

    return val22
  
def check(g,gs):
    val22, g = check2(gs, g, cpawnb, crookb, cknightb, cbishopb, ckingb)
    return val22
                                
def clean(gs):
    gs.noc=0
    if gs.moved==0:
        gs.target = gs.target2 = gs.target0 = gs.t1 = gs.t2 = gs.t3 = -1
        gs.selected = gs.select = gs.noc_select = [-1,-1]
        gs.noc = gs.dragging = gs.found = gs.clicks = gs.flag = 0
    gs.moved=0

def capture(gs, ntw):

    capture2(gs, ntw, check, write, sound_illegal, sound_check, sound_capture)

def capture_test(t,gs, ntw):
    # only for en pessant

    for i in range(len(gs.position)):
        if gs.position[i].collidepoint(gs.find):
            if (i in gs.out):
                pass
            else:
                if (i<=15 and t==2):
                    gs.out.append(i)
                    break
                elif (i>15 and t==1):
                    gs.out.append(i)
                    break
                else:
                    gs.samec=-1
                    break

def move(gs, ntw):

    move2(gs, ntw, check, sound_illegal, write, sound_self, sound_castle, sound_check)
    
def king_move(c,gs):
    
    val22, c = king_move2(gs, sound_illegal, check, c)

    if val22 !="":
        return val22
    else:
        return False

def move_sprite_sine(amplitude, period, speed):
    x_offset = 0
    while True:
        y_pos = amplitude * math.sin(2 * math.pi * (x_offset / period))+((height/6)+10-my_sprite_rect.height/2)
        my_sprite_rect.y=y_pos
        x_offset += speed
        yield

def mouse_down_function(gs, which,aaa,bbb, ntw):

    gs.mouse_coordinate=(aaa,bbb)

    if gs.game_end==0 or which==1:
        if which==0:
            gs.mouse_x1_coordinate=gs.mouse_coordinate[0]
            gs.mouse_y1_coordinate=gs.mouse_coordinate[1]

            for i in range(len(gs.position)):
                if gs.position[i].collidepoint(gs.mouse_coordinate):
                    if (i in gs.out):
                        pass
                    else:
                        gs.pospos2=1
                        gs._tester_=i

            function_result= breaking_conditions2(gs, ntw)

            if not function_result:
                return None

            
        
        gs.noc+=1
        gs.clicked=1
        sound_click.play()
        gs.g=gs.mouse_coordinate
        
        castle_logic_checking(gs, check, ntw)

        if gs.select==[-1,-1]:
            gs.dragging=1
            for i in range(len(gs.position)):
                if gs.position[i].collidepoint(gs.g):
                    if (i in gs.out):
                        pass
                    else:
                        gs.found=1
                        gs.target0=i
                        gs.target=i
                        gs.a=gs.position[i].x
                        gs.b=gs.position[i].y
                        gs.t1=math.floor(gs.a/64)
                        gs.t2=math.floor(gs.b/64)
                        gs.select=[gs.t1,gs.t2]
                        if gs.board[gs.select[1]][gs.select[0]]==5 and gs.target<=15 and gs.castle_black_done==0:
                            castle_checker(gs, 1, check)
                        if gs.board[gs.select[1]][gs.select[0]]==5 and gs.target>15 and gs.castle_white_done==0:
                            castle_checker(gs, 2, check)

                        if gs.board[gs.select[1]][gs.select[0]] !=5:
                            gs.castle_black_1 = gs.castle_black_2 = gs.castle_white_1 = gs.castle_white_2=0

                        gs.t3=gs.t1+gs.t2
                        if gs.t3%2==0:
                            gs.flag=2
                            break
                        else:
                            gs.flag=1
                            break
        if gs.found==0 and gs.select==[-1,-1]:
            gs.flag=-1
            gs.t1=-1
            gs.t2=-1
            gs.t3=-1
            gs.clicked=0

        gs.found=0

def mouse_up_function(gs, aaa,bbb, ntw):

    gs.mouse_coordinate=(aaa,bbb)

    if gs.game_end==0:
        gs.mouse_x2_coordinate=gs.mouse_coordinate[0]
        gs.mouse_y2_coordinate=gs.mouse_coordinate[1]

        if (ntw.server_connected==0 or gs.opponent_joined==0):
            return None

        # Players gs.selecting between taking white or black
        if gs.start_selection==1:

            color_selection_online_mode(gs, ntw, write, sound_promote, small_black_rect, small_white_rect)

            if (small_white_rect.collidepoint(gs.mouse_coordinate) and gs.opponent_color==2) or (small_black_rect.collidepoint(gs.mouse_coordinate) and gs.opponent_color==1):
                sound_illegal.play()

            return None

        function_result = morph_selecting_piece2(gs, ntw)
        if not function_result:
            return None

        gs.piece_moving=0
        if gs.pospos2==0 and gs.select==[-1,-1]:
            return None
        gs.old_pos=0
        gs.clicked=0
        gs.dragging=0
        function_result2 = breaking_conditions3(gs, ntw, 1)
        if not function_result2:
            return None
        
        if gs.select!=[-1,-1]:
            gs.g1=gs.mouse_coordinate

            which_block_clicked(gs)

            function_result4 = breaking_conditions_and_target2(gs, ntw)
            if not function_result4:
                return None

            move_selected_piece(gs, ntw, capture, move, check, clean, rook_check, bishop_check, knight_check, king_move, capture_test)

        conditions_checker_call(gs, moves_left, check, repeat_check, checkmate, moves_draw, check_only_king_left)

        # For checking if pawn of 0th (top) row or 7th (bottom) row
        morph_check_online(gs)


if __name__ == "__main__":

    gs = GameState()
    
    ntw = NetworkManager()

    init_globals(gs, ntw)
    server_connection_thread = threading.Thread(target=server_join, daemon=True)
    server_connection_thread.start()

    # Starting a new thread for sending active connections requests to the server
    active_connections_thread = threading.Thread(target=send_active_connections_request, daemon=True)
    active_connections_thread.start()

    # Starting Threads For Listening And Writing
    receive_thread = threading.Thread(target=receive, daemon=True)
    receive_thread.start()

    pygame.init()
    pygame.display.set_caption('Chess')

    animation = move_sprite_sine(10, 75, 1)

    while True:

        color_and_mode_selection(gs, ntw, write, sound_bg_music, channel4)

        calling_mouse_up_down_functions_after_selection(gs, mouse_down_function, mouse_up_function, ntw)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if (ntw.server_connected==1):
                    ntw.client.close()
                try:
                    active_connections_thread.join(timeout=0)
                    server_connection_thread.join(timeout=0)
                    receive_thread.join(timeout=0)
                except:
                    pass
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if gs.gamemode==2 and gs.game_is_reset==1:
                        early_exit=1
                    if gs.gamemode==1 and gs.total_moves==0:
                        early_exit=1
                    if start_ticks is None:
                        start_ticks = pygame.time.get_ticks()

                if event.key == pygame.K_m:
                    if sound_on==1:
                        sound_offoff()
                        sound_on=0
                    else:
                        sound_onon()
                        sound_on=1

                if event.key == pygame.K_y:
                    if gs.reset_allowed==1 and gs.gamemode==2:
                        gs.reset_allowed=2
                    elif gs.gamemode==2:
                        if(gs.opponent_joined==0 and gs.game_end!=0):
                            gs.reset_allowed=2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    start_ticks = None


            if (event.type==pygame.MOUSEBUTTONDOWN and gs.game_end==0) and (gs.gamemode==1 or ((gs.move_made_by_opponent==1 or gs.total_moves==0 or gs.morph_variable!=0) and gs.gamemode==2 and gs.opponent_gamemode==2)):

                if gs.opponent_in_menu==1:
                    break

                gs.mouse_x1_coordinate=gs.mouse_coordinate[0]
                gs.mouse_y1_coordinate=gs.mouse_coordinate[1]

                if gs.mouse_lifted!=0:
                    gs.mouse_lifted=0
                    gs.og_x1_click=gs.mouse_x1_coordinate
                    gs.og_y1_click=gs.mouse_y1_coordinate

                for i in range(len(gs.position)):
                    if gs.position[i].collidepoint(gs.mouse_coordinate):
                        if (i in gs.out):
                            pass
                        else:
                            gs.pospos2=1
                            gs._tester_=i

                function_result= breaking_conditions(gs, ntw)
                if not function_result:
                    break

                mouse_down_function(gs, 1, gs.mouse_coordinate[0], gs.mouse_coordinate[1], ntw)

            if (event.type == pygame.MOUSEBUTTONUP and gs.game_end==0) and (gs.gamemode!=2 or ((gs.move_made_by_opponent==1 or gs.total_moves==0 or gs.morph_variable!=0) and gs.gamemode==2 and gs.opponent_gamemode==2)):
                
                if (online_rect).collidepoint(gs.mouse_coordinate)==True and gs.gamemode==0:
                    sound_promote.play()
                    gs.gamemode=2
                if (offline_rect).collidepoint(gs.mouse_coordinate)==True and gs.gamemode==0:
                    sound_promote.play()
                    gs.gamemode=1

                if gs.opponent_in_menu==1:
                    break
                gs.mouse_x2_coordinate=gs.mouse_coordinate[0]
                gs.mouse_y2_coordinate=gs.mouse_coordinate[1]

                gs.mouse_lifted=1

                if (ntw.server_connected==0 or gs.opponent_joined==0) and gs.gamemode==2 and gs.opponent_gamemode==2:
                    break

                if gs.start_selection==1 and gs.gamemode==2 and gs.opponent_gamemode==2 and gs.opponent_game_end==0:

                    # Players gs.selecting between white and black color
                    color_selection_online_mode(gs, ntw, write, sound_promote, small_black_rect, small_white_rect)

                    if (small_white_rect.collidepoint(gs.mouse_coordinate) and gs.opponent_color==2) or (small_black_rect.collidepoint(gs.mouse_coordinate) and gs.opponent_color==1):
                        sound_illegal.play()

                    break

                if(not morph_selecting_piece(gs, ntw, write)):
                    break

                if gs.selection_done==0 and gs.gamemode==2 and gs.opponent_gamemode==2:
                    break

                gs.piece_moving=0
                if gs.pospos2==0 and gs.select==[-1,-1]:
                    break
                gs.old_pos=0
                gs.clicked=0
                gs.dragging=0

                function_result = breaking_conditions3(gs, ntw, 2)
                if not function_result:
                    break
                    
                if gs.select!=[-1,-1]:
                    gs.g1=gs.mouse_coordinate

                    which_block_clicked(gs)
                    
                    if (gs.selected_1==-1 and gs.selected==gs.select):
                        gs.mouse_clicks_list.append(gs.mouse_x2_coordinate)
                        gs.mouse_clicks_list.append(gs.mouse_y2_coordinate)
                        gs.selected_1=gs.select
                        gs.click_select_with_drag=0
                    elif (gs.selected_1!=-1):
                        if gs.selected_1!=gs.selected and gs.selected!=[-1,-1]:

                            if (gs.select != gs.selected and gs.select !=gs.selected_1):
                                gs.mouse_clicks_list.pop(0)
                                gs.mouse_clicks_list.pop(0)
                                gs.mouse_clicks_list.append(gs.og_x1_click)
                                gs.mouse_clicks_list.append(gs.og_y1_click)

                            gs.mouse_clicks_list.append(gs.mouse_x2_coordinate)
                            gs.mouse_clicks_list.append(gs.mouse_y2_coordinate)
                            gs.click_select_with_drag=0
                            if (gs.final_selected_color==2 and gs.color_board[gs.selected[1]][gs.selected[0]]==2) or (gs.final_selected_color==1 and gs.color_board[gs.selected[1]][gs.selected[0]]==1):
                                gs.selected_1=gs.selected
                                gs.mouse_clicks_list.pop(0)
                                gs.mouse_clicks_list.pop(0)
                            else:
                                gs.coords_send=1
                                gs.message_content=(f"mouse {gs.mouse_clicks_list[0]},{gs.mouse_clicks_list[1]},{gs.mouse_clicks_list[2]},{gs.mouse_clicks_list[3]}|")
                                write(gs, ntw)
                                gs.mouse_clicks_list=[]
                                gs.selected_1=-1

                    if (gs.selected==[-1,-1] and gs.selected_1==-1):
                        gs.selected_1=gs.select
                        gs.mouse_clicks_list.append(gs.og_x1_click)
                        gs.mouse_clicks_list.append(gs.og_y1_click)
                        gs.click_select_with_drag=1

                    function_result = breaking_conditions_and_target2(gs, ntw)
                    if not function_result:
                        break
                    
                    send_coords(gs, ntw, write)

                    move_selected_piece(gs, ntw, capture, move, check, clean, rook_check, bishop_check, knight_check, king_move, capture_test)


                conditions_checker_call(gs, moves_left, check, repeat_check, checkmate, moves_draw, check_only_king_left)

                # Check for pawns as 0th (top) or 7th (bottom) row
                morph_check(gs)
                
                if ((gs.total_moves_when_opponent_played+1)==gs.total_moves):
                    gs.move_made_by_opponent=0

                # for _ in range(8):
                #     for __ in range(8):
                #         print(gs.board[_][__], end=" ")
                #     print()
                # print(gs.select)
                # print()
                

        check(0,gs)
        # print(gs.black_en_pessant_possible)
        
        board_castle_move_maker(gs, screen)

        game_end_display(gs, screen)
        
        # print(gs.select)

        pieces_and_move_display(gs, screen, lg, dg, indicator)

        morphing_piece(gs, ntw, screen ,moves_left, check, repeat_check, checkmate, moves_draw, check_only_king_left)

        if ntw.server_connected==0 and gs.gamemode==2:
            screen.blit(morph_background,morph_back_rect)
            screen.blit(join_text,join_text_rect)
            if gs.game_is_reset==0:
                gs.reset_allowed=2

        color_selection_message(gs, ntw, write)

        color_selection_display(gs, screen)

        countdown(gs)
        
        quit_text_display(gs, ntw, screen)

        if gs.selection_done==1 and gs.gamemode==2 and gs.opponent_gamemode==2:
            gs.game_is_reset=0

        displaying_menu(gs, pygame, animation, my_sprite_rect)

        function_result = resetting_game(gs, ntw, screen, start_ticks, pygame, early_exit, write, quit_text5, quit_text5_rect, quit_text15, quit_text15_rect)

        if function_result:
            from src.variables import * # For resetting the variables not in the class
            gs.reset_variable()

        pygame.display.update()
        clock.tick(FPS)
