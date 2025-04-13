from src.variables import sound_end, sound_draw

def checkmate(gs, moves_left, check):
    # print(moves_left(1), moves_left(2))

    if moves_left(1,gs)==False and check(2,gs)==False:
        gs.king_under_checkmate=1
        sound_end.play()
        # return None
    elif moves_left(2,gs)==False and check(1,gs)==False:
        gs.king_under_checkmate=2
        sound_end.play()
        # return None
    else:
        gs.king_under_checkmate=0
        gs.inside_stalemate_function= stalemate(gs, moves_left, check)

def stalemate(gs, moves_left, check):
    # print(moves_left(1), moves_left(2))
    if moves_left(1,gs)==False and check(2,gs)==True:
        gs.king_under_stalemate=1
        sound_draw.play()
        gs.inside_stalemate_function=0
        # return None
    elif moves_left(2,gs)==False and check(1,gs)==True:
        gs.king_under_stalemate=2
        sound_draw.play()
        gs.inside_stalemate_function=0
        # return None
    else:
        gs.king_under_stalemate=0
        gs.inside_stalemate_function=0

def check_only_king_left(gs):
    count1=0
    count2=[]
    count3=0
    for i in range(8):
        for j in range(8):
            if gs.board[i][j]!=0:
                count1+=1
                count2.append(gs.board[i][j])
    
    for i in range (len(count2)):
        if count2[i]==5 and len(count2)==2:
            count3=1
        else:
            count3=0
    if count3==1 and count1==2:
        sound_draw.play()
        gs.game_end=1
        gs.only_king_game_end=1