def resetting_game(gs, ntw, screen, start_ticks, pygame, early_exit, write, quit_text5, quit_text5_rect, quit_text15, quit_text15_rect):
        
    returning_value = False

    # For resetting the game after the reset button pressed long enough
    if (gs.gamemode==2 and ((start_ticks is not None and pygame.time.get_ticks() - start_ticks >= 2500 and gs.selection_done==1) or (gs.reset_allowed==2))) or (gs.gamemode==1 and (start_ticks is not None and pygame.time.get_ticks() - start_ticks >= 2500)) or early_exit==1:  # 2500 milliseconds = 2.5 seconds

        if gs.reset_message_send==0 and gs.reset_pressed_opponent==0 and gs.gamemode==2 and gs.opponent_gamemode==2 and early_exit==0 and gs.opponent_joined==1:
            gs.reset_pressed_you=1
            gs.message_content=(f"reset|")
            write(gs, ntw)
            gs.game_end=1
            gs.reset_message_send=1
            gs.reset_allowed=1

        if gs.gamemode==1:
            gs.reset_allowed=1

        if early_exit==1:
            gs.message_content="earlyexit|"
            write(gs, ntw)

        if (gs.reset_allowed==2 and gs.gamemode==2) or (gs.gamemode==1 and gs.reset_allowed==1) or early_exit==1:

            returning_value = True


    # For showing text to keep holding the reset button
    if (start_ticks is not None and pygame.time.get_ticks() - start_ticks < 2500 and pygame.time.get_ticks() - start_ticks >0) and ((gs.gamemode==2 and gs.selection_done==1 and gs.reset_pressed_you==0 and gs.reset_pressed_opponent==0) or (gs.gamemode==1)):
        screen.blit(quit_text5, quit_text5_rect)

    if (start_ticks is None and gs.game_end!=0 and gs.reset_pressed_you==0 and gs.reset_pressed_opponent==0 and not (gs.gamemode==2 and (gs.opponent_joined==0 or gs.reset_pressed_opponent!=0 or gs.reset_pressed_you!=0))):
        screen.blit(quit_text15, quit_text15_rect)

    return returning_value