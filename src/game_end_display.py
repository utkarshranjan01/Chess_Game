from src.variables import *

def game_end_display(gs, screen):
    if gs.king_under_check==1:
        if gs.final_selected_color==1:
            screen.blit(red,(15*32-24-5-gs.position[4].x,15*32-24-5-gs.position[4].y))
        else:
            screen.blit(red,(gs.position[4].x-3,gs.position[4].y-3))

    if gs.king_under_check==2:
        if gs.final_selected_color==1:
            screen.blit(red,(15*32-24-5-gs.position[20].x,15*32-24-5-gs.position[20].y))
        else:
            screen.blit(red,(gs.position[20].x-3,gs.position[20].y-3))

    if gs.king_under_checkmate==1:
        if gs.final_selected_color==1:
            screen.blit(red2,(15*32-24-5-gs.position[4].x,15*32-24-5-gs.position[4].y))
        else:
            screen.blit(red2,(gs.position[4].x-3,gs.position[4].y-3))
    if gs.king_under_checkmate==2:
        if gs.final_selected_color==1:
            screen.blit(red2,(15*32-24-5-gs.position[20].x,15*32-24-5-gs.position[20].y))
        else:
            screen.blit(red2,(gs.position[20].x-3,gs.position[20].y-3))

    if gs.king_under_stalemate==1:
        if gs.final_selected_color==1:
            screen.blit(yellow,(15*32-24-5-gs.position[4].x,15*32-24-5-gs.position[4].y))
        else:
            screen.blit(yellow,(gs.position[4].x-3,gs.position[4].y-3))
    if gs.king_under_stalemate==2:
        if gs.final_selected_color==1:
            screen.blit(yellow,(15*32-24-5-gs.position[20].x,15*32-24-5-gs.position[20].y))
        else:
            screen.blit(yellow,(gs.position[20].x-3,gs.position[20].y-3))

    if gs.king_under_checkmate!=0 or gs.king_under_stalemate!=0:
        gs.game_end=1

