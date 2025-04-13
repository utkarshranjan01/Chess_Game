import math

def breaking_conditions(gs, ntw):
    if gs.gamemode==1:
        if gs._tester_<=15 and (gs.total_moves%2)==0 and gs._tester_!=-1:
            gs._tester_=-1
            return False

        if gs._tester_>15 and (gs.total_moves%2)!=0 and gs._tester_!=-1:
            gs._tester_=-1
            return False

    if gs.gamemode==2 and gs.opponent_gamemode==2:
        if gs._tester_<=15 and gs.final_selected_color==2 and gs._tester_!=-1:
            gs._tester_=-1
            return False

        if gs._tester_>15 and gs.final_selected_color==1 and gs._tester_!=-1:
            gs._tester_=-1
            return False

        if gs._tester_==-1:
            return False

        if gs.total_moves%2==0 and gs.final_selected_color==1:
            return False

        if gs.total_moves%2!=0 and gs.final_selected_color==2:
            return False

        if (ntw.server_connected==0 or gs.opponent_joined==0):
            return False

        if gs.start_selection==1:
            return False

        if gs.selection_done==0:
            return False

    if gs.morph_variable!=0:
        return False

    if gs.pospos2==0 and gs.select==[-1,-1]:
        return False
    else:
        gs.pospos2=0
    
    return True

def breaking_conditions2(gs, ntw):
    if gs._tester_==-1:
        return False
    
    if (ntw.server_connected==0 or gs.opponent_joined==0):
        return False

    if gs.morph_variable!=0:
        return False

    if gs.start_selection==1:
        return False

    if gs.pospos2==0 and gs.select==[-1,-1]:
        return False
    else:
        gs.pospos2=0
    return True


def breaking_conditions3(gs, ntw, func_call_where):
    function_result = True
    if gs.noc==2:
        gs.noc=0
        gs.g=gs.mouse_coordinate
        for i in range(len(gs.position)):
            if gs.position[i].collidepoint(gs.g):
                if (i in gs.out):
                    pass
                else:
                    gs.noc_select=[math.floor(gs.position[i].x/64),math.floor(gs.position[i].y/64)]
        if gs.noc_select==gs.select:
            gs.select=[-1,-1]
            gs.selected=[-1,-1]
            gs.noc_select=[-1,-1]
            if func_call_where==2:
                gs.mouse_clicks_list=[]
                gs.selected_1=-1
            gs.flag=-1
            gs.t1=-1
            gs.t2=-1
            gs.t3=-1
            gs.clicked=0
            gs.found=0
            function_result = False
        
    return function_result

def breaking_conditions_and_target2(gs, ntw):

    if gs.selected==gs.select or gs.selected==[-1,-1]:
        gs.selected=[-1,-1]
        return False

    for i in range (len(gs.position)):
        if gs.position[i].collidepoint(gs.g1):
            if (i in gs.out):
                pass
            else:
                gs.target2=i
                break
        gs.target2=-1
    return True