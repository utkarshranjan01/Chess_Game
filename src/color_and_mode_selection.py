import pygame

def color_and_mode_selection(gs, ntw, write, sound_bg_music, channel4):
    if gs.final_selected_color==2:
        gs.mouse_coordinate=pygame.mouse.get_pos()
    else:
        if gs.selection_done!=1:
            gs.mouse_coordinate=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        else:
            if gs.morph_variable!=0:
                gs.mouse_coordinate=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
            else:
                gs.mouse_coordinate=(511-pygame.mouse.get_pos()[0],511-pygame.mouse.get_pos()[1])
        
    if gs.gamemode==1:
        gs.mouse_coordinate=pygame.mouse.get_pos()

    if gs.gamemode==1:
        try:
            sound_bg_music.stop()
        except:
            pass
        gs.message_content="game1|"
        write(gs, ntw)
    elif gs.gamemode==2:
        try:
            sound_bg_music.stop()
        except:
            pass
        gs.message_content="game2|"
        write(gs, ntw)
    elif gs.gamemode==0:
        try:
            if (channel4.get_busy()==False):
                channel4.play(sound_bg_music, loops=-1)
        except:
            pass
        gs.message_content="game0|"
        write(gs, ntw)

    if gs.game_end==1:
        gs.message_content="endscreen|"
        write(gs, ntw)
    elif gs.game_end==0:
        gs.message_content="endscreen0|"
        write(gs, ntw)
