from src.variables import *

class GameState:
    def __init__(self):

        self.king_under_check = 0
        self.king_under_checkmate=0
        self.king_under_stalemate=0

        self.black_king_target_value2=[0,4]
        self.black_king_target_value=[0,4]
        self.white_king_target_value2=[7,4]
        self.white_king_target_value=[7,4]

        self.board = self.make_list4()
        self.color_board = self.make_list5()
        self.board_copy = self.make_list3()
        self.piece, self.position= make_list8()
        self.pos= make_list9()
        self.pos2= make_list6()
        self.images, self.spots = make_list7()

        self.opponent_joined=0
        self.your_color=0
        self.start_selection=0
        self.selected_color=0
        self.selection_done=0

        self.final_selected_color=0
        self.final_opponent_color=0

        self.mouse_x1_coordinate=-1
        self.mouse_y1_coordinate=-1
        self.mouse_x2_coordinate=-1
        self.mouse_y2_coordinate=-1

        self.white_king_has_moved=0
        self.white_left_rook_has_moved=0
        self.white_right_rook_has_moved=0

        self.black_king_has_moved=0
        self.black_left_rook_has_moved=0
        self.black_right_rook_has_moved=0

        self.en_pessant=0
        self.moves_since_en_pessant=0
        self.total_moves=0
        self.draw_total_moves=0

        self.castle_white_done=0
        self.castle_black_done=0
        self.castle_being_done=0

        self.castle_white_1=0
        self.castle_white_2=0
        self.castle_black_1=0
        self.castle_black_2=0
        self.castle_being_done=0

        self.opponent_game_end=0
        self.repeat_game_end=0
        self.moves50_game_end=0
        self.only_king_game_end=0

        self.reset_pressed_opponent=0
        self.reset_pressed_you=0
        self.reset_message_send=0
        self.reset_allowed=0
        self.game_is_reset=1

        self.morph_variable=0
        self.morph_piece=-1
        self.morph_target=-1
        self.morph_pos=-1
        self.morph_list=morph_list

        self.opponent_left_once=0

        self.opponent_in_menu=0

        self.mouse_coordinate=0

        self.inside_stalemate_function=0

        self.out=[]

        self.move_made_by_opponent=-1
        self.opponent_color=0

        self.message_content=''

        self.game_end=0

        self.board_repeat=[0]

        self.countdown_time=3
        self.start_time=-1

        self.numbers_str=[]
        self.click_event1=-1
        self.click_event2=-1
        self.click_event3=-1
        self.click_event4=-1

        self.gamemode=0
        self.opponent_gamemode=0

        self.select=[-1,-1]
        self.selected=[-1,-1]
        self.noc_select=[-1,-1]

        self.target=-1
        self.target2=-1
        self.target0=-1

        self.ca=self.cb=self.ca1=self.cb1=0

        self.cpos1=0
        self.cpos2=0

        self.gone=0
        self.moved=0
        self.samec=0

        self.a = self.b = self.a1 = self.b1 = self.clicks = 0
        self.value=0

        self.dragging=0
        self.board_moves_copy=0
        self.piece_moving=0
        self.make_move=0

        self.opponent_turn_played=0
        self.turn_played=0

        self.coords_send=0
        self.noc=0

        self.t1 = self.t2 = self.t3 = -1
        self.clicked=0

        self.pospos=0
        self.pospos2=0

        self.val2=0
        self.test__=0

        self.found=0

        self.find=0
        self.flag=0

        self.selected_1=-1

        self.t11=0
        self.t21=0

        self.countcount=0

        self.hovering_sound=-1
        self.hovering_sound2=-1

        self.total_moves_when_opponent_played=0

        self.old_pos=0

        self.g1=0

        self.__select=0

        self._tester_=-1

        self.prev_total_moves=0

        self.g=0

        self.og_x1_click=-1
        self.og_y1_click=-1
        self.mouse_lifted=-1

        self.mouse_clicks_list=[]

    
    def reset_variable(self):

        self.__init__()
        

    def make_list3(self):
        board_copy=[]
        board_copy.append([[[0 for _ in range(8)] for _ in range(8)],[[0 for _ in range(8)] for _ in range(8)]])
        for i in range(8):
            for j in range(8):
                board_copy[len(board_copy)-1][0][i][j]=self.board[i][j]
                board_copy[len(board_copy)-1][1][i][j]=self.color_board[i][j]

        return board_copy

    def make_list4(self):

        board=[[0 for _ in range(8)] for _ in range(8)]

        for i in range(0, 8):
            board[0][i]=1
            board[1][i]=1
            board[6][i]=1
            board[7][i]=1

        # rook=1, knight=2, bishop=3, queen=4, king=5, pawn=6,en pessant pawn=7, nothing=0(which i initialized all with zero so now putting values only in places with pieces)

        for i in range (8):

            board[1][i]=6
            board[6][i]=6

            board[0][0]=board[7][0]=1
            board[0][1]=board[7][1]=2
            board[0][2]=board[7][2]=3
            board[0][3]=board[7][3]=4
            board[0][4]=board[7][4]=5
            board[0][5]=board[7][5]=3
            board[0][6]=board[7][6]=2
            board[0][7]=board[7][7]=1

        return board

    def make_list5(self):
        color_board=[[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            color_board[0][i]=1
            color_board[1][i]=1
            color_board[6][i]=2
            color_board[7][i]=2
        return color_board


    def make_list(self):
        new_list=[[0 for _ in range(8)] for _ in range(8)]
        return new_list

    def make_list2(self):
        new_list=[[[0 for _ in range(8)] for _ in range(8)],[[0 for _ in range(8)] for _ in range(8)]]
        return new_list
