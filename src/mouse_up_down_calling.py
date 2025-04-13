def calling_mouse_up_down_functions_after_selection(gs, mouse_down_function, mouse_up_function, ntw):
    if gs.click_event1!=-1 and gs.click_event2!=-1 and gs.selection_done==1:
        gs.prev_total_moves=gs.total_moves
        mouse_down_function(gs, 0,gs.click_event1[0], gs.click_event1[1], ntw)
        mouse_up_function(gs, gs.click_event2[0], gs.click_event2[1], ntw)
        gs.click_event1=-1
        gs.click_event2=-1
        if (gs.prev_total_moves+1)==gs.total_moves:
            gs.move_made_by_opponent=1
            gs.total_moves_when_opponent_played=gs.total_moves
        elif (gs.morph_piece!=-1):
            gs.move_made_by_opponent=1
        else:
            gs.move_made_by_opponent=0