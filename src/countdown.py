from src.variables import *

def countdown(gs):
    if gs.start_selection==1 and ((gs.opponent_color==1 and gs.selected_color==2) or (gs.opponent_color==2 and gs.selected_color==1)) and gs.gamemode==2 and gs.opponent_gamemode==2:
        if gs.start_time==-1:
            gs.start_time = pygame.time.get_ticks()  # Track starting time
        elapsed_time = pygame.time.get_ticks() - gs.start_time
        if elapsed_time >= 1000:  # Check for at least one second
            gs.countdown_time = max(0, gs.countdown_time - 1)  # Decrement by 1
            gs.start_time = pygame.time.get_ticks()  # Reset starting time for the next second
            sound_click.play()
        timer_text = text_font.render(f"Game starting in {gs.countdown_time}...", True, "white")
        timer_text_rect=timer_text.get_rect(center=(width/2,height/2+96))
        screen.blit(timer_text,timer_text_rect)
    
    if gs.start_selection==1 and (gs.opponent_color==0 or gs.selected_color==0) and gs.gamemode==2 and gs.opponent_gamemode==2:
        gs.start_time=-1
        gs.countdown_time=3

    if gs.countdown_time == 0 and gs.gamemode==2 and gs.opponent_gamemode==2:  # Countdown finished

        gs.final_selected_color=gs.selected_color
        gs.final_opponent_color=gs.opponent_color

        sound_castle.play()
        gs.start_time=-1
        gs.countdown_time=3
        gs.start_selection=0
        gs.opponent_color=0
        gs.selected_color=0
        gs.selection_done=1
