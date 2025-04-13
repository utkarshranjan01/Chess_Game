import math

def which_block_clicked(gs):
    for i in range (64):
        if gs.spots[i].collidepoint(gs.g1):
            gs.a1=gs.spots[i].x
            gs.b1=gs.spots[i].y
            gs.t11=math.floor(gs.a1/64)
            gs.t21=math.floor(gs.b1/64)
            gs.selected=[gs.t11,gs.t21]
            break
