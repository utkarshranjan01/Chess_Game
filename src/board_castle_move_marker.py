from src.variables import *

def board_castle_move_maker(gs, screen):
    if (gs.final_selected_color==2):
        screen.blit(bg,bg1)
    else:
        screen.blit(bg_rev,bg1)

    if gs.flag==1:
            if gs.final_selected_color==1:
                screen.blit(lg,(511-gs.a-4-32-16-8,511-gs.b-4-32-16-8))
            else:
                screen.blit(dg,(gs.a-3,gs.b-3))
    if gs.flag==2:
        if gs.final_selected_color==1:
            screen.blit(dg,(511-gs.a-4-32-16-8,511-gs.b-4-32-16-8))
        else:
            screen.blit(lg,(gs.a-3,gs.b-3))

    if ((gs.final_selected_color==1 and (gs.total_moves)%2!=0) or (gs.final_selected_color==2 and (gs.total_moves)%2==0)):
        if gs.select!=[-1,-1]:
            if gs.final_selected_color==1:
                screen.blit(blue,(15*32-gs.a-29,15*32-gs.b-29))
            else:
                screen.blit(blue,(gs.a-3,gs.b-3))

    if gs.castle_black_1==1 and gs.noc==1 and gs.total_moves%2!=0 and gs.black_king_has_moved==0:
        if gs.final_selected_color==1:
            screen.blit(green,(511-(5*x)-32+1,511-x-32+1))
        else:
            screen.blit(green,((5*32)-32,32-32))
    if gs.castle_black_2==1 and gs.noc==1 and gs.total_moves%2!=0 and gs.black_king_has_moved==0:
        if gs.final_selected_color==1:
            screen.blit(green,(511-(13*32)-32+1,511-32-32+1))
        else:
            screen.blit(green,((13*x)-32,x-32))
    if gs.castle_white_1==1 and gs.noc==1 and gs.total_moves%2==0 and gs.white_king_has_moved==0:
        if gs.final_selected_color==1:
            screen.blit(green,(511-(5*x)-32+1,511-(15*x)-32+1))
        else:
            screen.blit(green,((5*x)-32,(15*x)-32))
    if gs.castle_white_2==1 and gs.noc==1 and gs.total_moves%2==0 and gs.white_king_has_moved==0:
        if gs.final_selected_color==1:
            screen.blit(green,(511-(13*x)-32+1,511-(15*x)-32+1))
        else:
            screen.blit(green,((13*x)-32,(15*x)-32))

