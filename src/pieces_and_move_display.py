def pieces_and_move_display(gs, screen, lg, dg, indicator):
    if gs.cpos1!=0 and gs.cpos2!=0 and gs.cpos1 != gs.cpos2:
        if ((gs.cpos1[0]+gs.cpos1[1])%2==0):
            if gs.final_selected_color==1:
                screen.blit(dg,(511-gs.ca1-4-32-16-8,511-gs.cb1-4-32-16-8))
            else:
                screen.blit(lg,(gs.ca1-3,gs.cb1-3))
        else:
            if gs.final_selected_color==1:
                screen.blit(lg,(511-gs.ca1-4-32-16-8,511-gs.cb1-4-32-16-8))
            else:
                screen.blit(dg,(gs.ca1-3,gs.cb1-3))

        if ((gs.cpos2[0]+gs.cpos2[1])%2==0):
            if gs.final_selected_color==1:
                screen.blit(dg,(511-gs.ca-4-32-16-8,511-gs.cb-4-32-16-8))
            else:
                screen.blit(lg,(gs.ca-3,gs.cb-3))
        else:
            if gs.final_selected_color==1:
                screen.blit(lg,(511-gs.ca-4-32-16-8,511-gs.cb-4-32-16-8))
            else:
                screen.blit(dg,(gs.ca-3,gs.cb-3))

    for i in range(len(gs.position)):
        if (i in gs.out):
            pass
        else:    
            if i!=gs.target:
                if gs.final_selected_color==1:
                    screen.blit(gs.piece[i],(15*32-gs.position[i][0]-24-2,15*32-gs.position[i][1]-24-2))
                else:
                    screen.blit(gs.piece[i],gs.position[i])

    if (gs.clicked==1 and gs.target!=-1 and ((gs.position[gs.target]).collidepoint(gs.mouse_coordinate)==True or (gs.pospos!=0 and gs.pospos.collidepoint(gs.mouse_coordinate)==True))) or gs.piece_moving==1:

        g1_test=gs.mouse_coordinate
        for i in range (64):
            if gs.spots[i].collidepoint(g1_test):
                gs.test__=i
        if gs.final_selected_color==1:
            screen.blit(indicator,(15*32-gs.spots[gs.test__].x-24-5,15*32-gs.spots[gs.test__].y-24-5))
            screen.blit(gs.piece[gs.target],gs.piece[gs.target].get_rect(center=(511-gs.mouse_coordinate[0],511-gs.mouse_coordinate[1])))
        else:
            screen.blit(indicator,(gs.spots[gs.test__].x-3,gs.spots[gs.test__].y-3))
            screen.blit(gs.piece[gs.target],gs.piece[gs.target].get_rect(center=(gs.mouse_coordinate[0],gs.mouse_coordinate[1])))
        gs.pospos=gs.piece[0].get_rect(center=(gs.mouse_coordinate))
        gs.piece_moving=1
    elif gs.target!=-1:
        if gs.final_selected_color==1:
            screen.blit(gs.piece[gs.target],(15*32-gs.position[gs.target][0]-24-2,15*32-gs.position[gs.target][1]-24-2))
        else:
            screen.blit(gs.piece[gs.target],gs.position[gs.target])
