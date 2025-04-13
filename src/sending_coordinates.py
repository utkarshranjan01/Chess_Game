
def send_coords (gs, ntw, write):
    if(gs.target!=-1):
        if gs.coords_send==0:
            gs.message_content=(f"mouse {gs.mouse_x1_coordinate},{gs.mouse_y1_coordinate},{gs.mouse_x2_coordinate},{gs.mouse_y2_coordinate}|")
            write(gs, ntw)
        else :
            gs.coords_send=0
