from src.variables import sound_draw

def repeat_check(gs):
    while len(gs.board_repeat) < len(gs.board_copy):
        gs.board_repeat.append(0)
    for i in range(len(gs.board_copy)):
        for j in range(len(gs.board_copy)):
            if i!=j and gs.board_copy[i]==gs.board_copy[j]:
                # board_moves_copy+=1
                gs.board_repeat[i]+=1
                gs.board_repeat[j]+=1
    # board_moves_copy/=2
    for i in gs.board_repeat:
        if i>2:
            sound_draw.play()
            gs.game_end=1
            gs.repeat_game_end=1
    for i in range(len(gs.board_repeat)):
        gs.board_repeat[i]=0


def moves_draw(gs):
    if gs.draw_total_moves==50:
        sound_draw.play()
        gs.game_end=1
        gs.moves50_game_end=1

