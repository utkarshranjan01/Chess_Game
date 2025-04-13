def move_knight(gs, i,j,c,item, target5, move_check, check):
    new_x1=-1
    new_x2=-1
    new_y1=-1
    new_y2=-1
    new_x01=-1
    new_x02=-1
    new_y01=-1
    new_y02=-1
    if c==1:
        if i<7:
            new_x01=i+1
        if i<6:
            new_x1=i+2

        if i>0:
            new_x02=i-1
        if i>1:
            new_x2=i-2

        if j<7:
            new_y01=j+1
        if j<6:
            new_y1=j+2
        
        if j>0:
            new_y02=j-1
        if j>1:
            new_y2=j-2

        if new_x1!=-1 and new_y01!=-1:
            if gs.board[new_x1][new_y01]==0 or gs.color_board[new_x1][new_y01]==2:
                if move_check(gs, i,j,new_x1,new_y01,1, item, target5,check)==True:
                        return True
                
        if new_x1!=-1 and new_y02!=-1:
            if gs.board[new_x1][new_y02]==0 or gs.color_board[new_x1][new_y02]==2:        
                if move_check(gs, i,j,new_x1,new_y02,1, item, target5,check)==True:
                        return True

        if new_x2!=-1 and new_y01!=-1:
            if gs.board[new_x2][new_y01]==0 or gs.color_board[new_x2][new_y01]==2:           
                if move_check(gs, i,j,new_x2,new_y01,1, item, target5,check)==True:
                        return True
                
        if new_x2!=-1 and new_y02!=-1:
            if gs.board[new_x2][new_y02]==0 or gs.color_board[new_x2][new_y02]==2:   
                if move_check(gs, i,j,new_x2,new_y02,1, item, target5,check)==True:
                        return True

        if new_x01!=-1 and new_y1!=-1:
            if gs.board[new_x01][new_y1]==0 or gs.color_board[new_x01][new_y1]==2:   
                if move_check(gs, i,j,new_x01,new_y1,1, item, target5,check)==True:
                        return True
                
        if new_x02!=-1 and new_y1!=-1:
            if gs.board[new_x02][new_y1]==0 or gs.color_board[new_x02][new_y1]==2:   
                if move_check(gs, i,j,new_x02,new_y1,1, item, target5,check)==True:
                        return True
                
        if new_x01!=-1 and new_y2!=-1:
            if gs.board[new_x01][new_y2]==0 or gs.color_board[new_x01][new_y2]==2:   
                if move_check(gs, i,j,new_x01,new_y2,1, item, target5,check)==True:
                        return True
        
        if new_x02!=-1 and new_y2!=-1:
            if gs.board[new_x02][new_y2]==0 or gs.color_board[new_x02][new_y2]==2:   
                if move_check(gs, i,j,new_x02,new_y2,1, item, target5,check)==True:
                        return True

        return False
    else:
        if i<7:
            new_x01=i+1
        if i<6:
            new_x1=i+2

        if i>0:
            new_x02=i-1
        if i>1:
            new_x2=i-2

        if j<7:
            new_y01=j+1
        if j<6:
            new_y1=j+2
        
        if j>0:
            new_y02=j-1
        if j>1:
            new_y2=j-2

        if new_x1!=-1 and new_y01!=-1:
            if gs.board[new_x1][new_y01]==0 or gs.color_board[new_x1][new_y01]==1:
                if move_check(gs, i,j,new_x1,new_y01,2, item, target5, check)==True:
                        return True
                
        if new_x1!=-1 and new_y02!=-1:
            if gs.board[new_x1][new_y02]==0 or gs.color_board[new_x1][new_y02]==1:        
                if move_check(gs, i,j,new_x1,new_y02,2, item, target5, check)==True:
                        return True

        if new_x2!=-1 and new_y01!=-1:
            if gs.board[new_x2][new_y01]==0 or gs.color_board[new_x2][new_y01]==1:           
                if move_check(gs, i,j,new_x2,new_y01,2, item, target5, check)==True:
                        return True
                
        if new_x2!=-1 and new_y02!=-1:
            if gs.board[new_x2][new_y02]==0 or gs.color_board[new_x2][new_y02]==1:   
                if move_check(gs, i,j,new_x2,new_y02,2, item, target5, check)==True:
                        return True

        if new_x01!=-1 and new_y1!=-1:
            if gs.board[new_x01][new_y1]==0 or gs.color_board[new_x01][new_y1]==1:   
                if move_check(gs, i,j,new_x01,new_y1,2, item, target5, check)==True:
                        return True
                
        if new_x02!=-1 and new_y1!=-1:
            if gs.board[new_x02][new_y1]==0 or gs.color_board[new_x02][new_y1]==1:   
                if move_check(gs, i,j,new_x02,new_y1,2, item, target5, check)==True:
                        return True
                
        if new_x01!=-1 and new_y2!=-1:
            if gs.board[new_x01][new_y2]==0 or gs.color_board[new_x01][new_y2]==1:
                if move_check(gs, i,j,new_x01,new_y2,2, item, target5, check)==True:
                        return True
        
        if new_x02!=-1 and new_y2!=-1:
            if gs.board[new_x02][new_y2]==0 or gs.color_board[new_x02][new_y2]==1:   
                if move_check(gs, i,j,new_x02,new_y2,2, item, target5, check)==True:
                        return True

        return False