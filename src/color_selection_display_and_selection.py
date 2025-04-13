from src.variables import *

def color_selection_display(gs, screen):
    try:
        if gs.start_selection==1 and gs.gamemode==2 and gs.opponent_gamemode==2 and gs.opponent_game_end==0:
            screen.blit(morph_background,morph_back_rect)
            screen.blit(select_color,select_color_rect)
            if (gs.selected_color==1):
                screen.blit(color_text_black,color_text_black_rect)
            elif gs.opponent_color==1:
                screen.blit(small_black,small_black_rect)
                screen.blit(cross_image,small_black_rect)
            elif small_black_rect.collidepoint(gs.mouse_coordinate)==True:
                if gs.hovering_sound2!=0:
                    sound_click.play()
                    gs.hovering_sound2=0
                screen.blit(big_black,big_black_rect)
            else:
                screen.blit(small_black,small_black_rect)

            if (gs.selected_color==2):
                screen.blit(color_text_white,color_text_white_rect)
            elif gs.opponent_color==2:
                screen.blit(small_white,small_white_rect)
                screen.blit(cross_image,small_white_rect)
            elif small_white_rect.collidepoint(gs.mouse_coordinate)==True:
                if gs.hovering_sound2!=1:
                    sound_click.play()
                    gs.hovering_sound2=1
                screen.blit(big_white,big_white_rect)
            else:
                screen.blit(small_white,small_white_rect)

            if (small_white_rect.collidepoint(gs.mouse_coordinate)==False and small_black_rect.collidepoint(gs.mouse_coordinate)==False):
                gs.hovering_sound2=-1
    
    except TypeError:
        pass

def color_selection_online_mode(gs, ntw, write, sound_promote, small_black_rect, small_white_rect):
    if small_black_rect.collidepoint(gs.mouse_coordinate) and gs.opponent_color!=1:
        if gs.selected_color==1:
            gs.selected_color=0
            gs.message_content="Player : 0|"
        else:
            gs.selected_color=1
            gs.message_content="Player : 1|"
            sound_promote.play()
        write(gs, ntw)
    if small_white_rect.collidepoint(gs.mouse_coordinate) and gs.opponent_color!=2:
        if gs.selected_color==2:
            gs.selected_color=0
            gs.message_content="Player : 0|"
        else:
            gs.selected_color=2
            gs.message_content="Player : 2|"
            sound_promote.play()
        write(gs, ntw)