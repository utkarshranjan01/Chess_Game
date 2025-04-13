from src.variables import *

def quit_text_display(gs, ntw, screen):


    if(gs.king_under_checkmate!=0 or gs.king_under_stalemate!=0 or gs.moves50_game_end!=0 or gs.repeat_game_end!=0 or gs.only_king_game_end!=0):
        game_finished=1
    else:
        game_finished=0

    if gs.moves50_game_end==1:
        screen.blit(quit_text8, quit_text8_rect)

    if gs.repeat_game_end==1:
        screen.blit(quit_text7, quit_text7_rect)

    if gs.only_king_game_end==1:
        screen.blit(quit_text13, quit_text13_rect)


    if gs.gamemode==2:

        # Displaying the waiting text
        if ( ( ( (gs.opponent_joined==0 or gs.opponent_gamemode!=2) and gs.game_is_reset==1) or (gs.game_end==0 and gs.opponent_game_end==1)) and ntw.server_connected==1 ):
            screen.blit(morph_background,morph_back_rect)
            screen.blit(wait_text,wait_text_rect)

        # This is displayed when opponent closed the game after the game ended
        if ((gs.opponent_joined==0 or gs.opponent_gamemode!=2) and gs.game_is_reset==0) or (gs.reset_allowed==1 and gs.reset_pressed_you==0 and (game_finished==1 or gs.opponent_left_once==1)):

            gs.opponent_left_once=1 # This variable is used to check if the opponent has left the game once and is not trying to join a new game again but this opponent left will still be showing on other players screen since he has not left
            if gs.reset_allowed==0:
                gs.reset_allowed=1
            screen.blit(quit_text0,quit_text0_rect)
            screen.blit(quit_text3,quit_text3_rect)

        # Opponent pressed reset before game end
        elif gs.reset_pressed_you==1 and gs.game_is_reset==0 and game_finished==0:
            screen.blit(quit_text1,quit_text1_rect)
            screen.blit(quit_text3,quit_text3_rect)

        # You pressed reset before game end
        elif gs.reset_pressed_opponent==1 and gs.game_is_reset==0 and game_finished==0:
            screen.blit(quit_text2,quit_text2_rect)
            screen.blit(quit_text3,quit_text3_rect)

        # You pressed reset after game end
        elif gs.reset_pressed_you==1 and gs.game_is_reset==0 and game_finished==1:
            screen.blit(quit_text6,quit_text6_rect)
            screen.blit(quit_text3,quit_text3_rect)


        if (gs.king_under_checkmate==1 and gs.final_selected_color==2) or (gs.king_under_checkmate==2 and gs.final_selected_color==1):
            screen.blit(quit_text9, quit_text9_rect)

        if (gs.king_under_checkmate==1 and gs.final_selected_color==1) or (gs.king_under_checkmate==2 and gs.final_selected_color==2):
            screen.blit(quit_text10, quit_text10_rect)

    elif (gs.gamemode==1):

        if gs.king_under_checkmate==1:
            screen.blit(quit_text11, quit_text11_rect)

        if gs.king_under_checkmate==2:
            screen.blit(quit_text12, quit_text12_rect)

        