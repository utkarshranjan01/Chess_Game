import pygame
from src.paths import *
import socket

class GameData:
    def __init__(self) -> None:
        pygame.init()
        self.width=512
        self.height=512
        self.clock = pygame.time.Clock()
        self.start_ticks = None
        self.screen=pygame.display.set_mode((self.width,self.height))

        self.ip_address="127.0.0.1"
        self.server_connected=0
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sleep_counter1=0 
        self.sleep_counter2=0
        self.sleep_counter3=0
        self.opponent_color=0


        self.numbers_str=[]
        self.click_event1=-1
        self.click_event2=-1
        self.click_event3=-1
        self.click_event4=-1

        self.prev_total_moves=0
        self.move_made_by_opponent=-1

        self.turn_played=0
        self.opponent_turn_played=0

        self.total_moves_when_opponent_played=0

        self.message=''
        self.message_content=''

        self.opponent_joined=0
        self.your_color=0
        self.start_selection=0
        self.selected_color=0
        self.selection_done=0

        self.mouse_x1_coordinate=-1
        self.mouse_y1_coordinate=-1
        self.mouse_x2_coordinate=-1
        self.mouse_y2_coordinate=-1

        self.final_selected_color=0
        self.final_opponent_color=0

        self.opponent_in_menu=0

        self.x=32
        self.c=3
        self.mouseX=0
        self.mouseY=0
        self.find=0
        self.a=0
        self.countdown_time=5
        self.start_time=-1
        self.b=0
        self.moved=0
        self.piece=[None]*32
        self.position=[None]*32
        self.pos= [[0 for _ in range(8)] for _ in range(8)]
        self.pos2= []
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.color_board = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            self.color_board[0][i]=1
            self.color_board[1][i]=1
            self.color_board[6][i]=2
            self.color_board[7][i]=2
        self.count=0
        self.flag=0
        self.t1=-1
        self.t2=-1
        self.t3=-1
        self.select=[-1,-1]
        self.selected=[-1,-1]
        self.target=-1
        self.g=0
        self.g1=0
        self.found=0
        self.king_under_check=0
        self.king_under_checkmate=0
        self.king_under_stalemate=0
        self.castle_white_1=0
        self.castle_white_2=0
        self.castle_black_1=0
        self.castle_black_2=0
        self.border=4

        self.q1=0
        self.q2=0
        self.a1=0
        self.countcount=0
        self.b1=0
        self.t11=0
        self.t21=0
        self.clicked=0
        self.cpos1=0
        self.cpos2=0
        self.ca=self.cb=self.ca1=self.cb1=0
        self.value=0
        self.gone=0
        self.target2=-1
        self.got=0
        self.out=[]
        self.target0=-1
        self.samec=0
        self.ibk=4
        self.iwk=28
        self.en_pessant=0
        self.moves_since_en_pessant=0
        self.total_moves=0
        self.white_king_has_moved=0
        self.white_left_rook_has_moved=0
        self.white_right_rook_has_moved=0
        self.whi=0
        self.black_left_rook_has_moved=0
        self.black_right_rook_has_moved=0
        self.black_king_target_value2=[0,4]
        self.black_king_target_value=[0,4]
        self.white_king_target_value2=[7,4]
        self.white_king_target_value=[7,4]
        self.dragging=0
        self.game_end=0
        self.castle_being_done=0
        for i in range(64):
            self.pos2.append([self.q1,self.q2])
            if self.q2<7:
                self.q2+=1
            else:
                self.q2=0
                self.q1+=1

        for i in range(0, 8):
            self.board[0][i]=1
            self.board[1][i]=1
            self.board[6][i]=1
            self.board[7][i]=1

        # rook=1, knight=2, bishop=3, queen=4, king=5, pawn=6,en pessant pawn=7, nothing=0(which i initialized all with zero so now putting values only in places with pieces)

        for i in range (8):
            self.board[1][i]=6
            self.board[6][i]=6

        self.board[0][0]=self.board[7][0]=1
        self.board[0][1]=self.board[7][1]=2
        self.board[0][2]=self.board[7][2]=3
        self.board[0][3]=self.board[7][3]=4
        self.board[0][4]=self.board[7][4]=5
        self.board[0][5]=self.board[7][5]=3
        self.board[0][6]=self.board[7][6]=2
        self.board[0][7]=self.board[7][7]=1

        self.inside_stalemate_function=0
        self.draw_total_moves=0
        self.board_repeat=[0]
        self.board_copy=[]
        self.board_copy.append([[[0 for _ in range(8)] for _ in range(8)],[[0 for _ in range(8)] for _ in range(8)]])
        for i in range(8):
            for j in range(8):
                self.board_copy[len(self.board_copy)-1][0][i][j]=self.board[i][j]
                self.board_copy[len(self.board_copy)-1][1][i][j]=self.color_board[i][j]


        self.board_moves_copy=0

        self.c1=1
        self.c2=1
        self.clicks=0
        self.dist=0
        self.gap=0
        self.val2=0
        self.dragpos=0
        self.noc=0
        self._tester_=-1
        self.old_pos=0
        self.noc_select=[-1,-1]
        self.empty=0
        self.sound_on=1
        self.piece_moving=0
        self.castle_white_done=0
        self.castle_black_done=0
        self.hovering_sound=-1
        self.hovering_sound2=-1
        for i in range(0,8):
            for j in range(0,8):
                self.pos[i][j]=[self.c1*self.x,self.c2*self.x]
                self.c1+=2
            self.c1=1
            self.c2+=2

        self.bg=pygame.image.load(ASSETS_DIR / "Board4.png").convert()
        self.bg_rev=pygame.image.load(ASSETS_DIR / "Board4_rev.png").convert()
        self.bg1=self.bg.get_rect(topleft=(0,0))

        self.text_font=pygame.font.Font(ASSETS_DIR / "0_font.ttf",40)

        self.wait_text=self.text_font.render(f'Waiting For Another Player...', True, 'white')
        self.wait_text_rect=self.wait_text.get_rect(center=(self.width/2,self.height/2))

        self.join_text=self.text_font.render(f'Waiting For Server To Be Online...', True, 'white')
        self.join_text_rect=self.join_text.get_rect(center=(self.width/2,self.height/2))

        self.text_font_5=pygame.font.Font(ASSETS_DIR / '0_font.ttf',30)
        self.quit_text=self.text_font_5.render(f'QUITS', True, 'red')
        self.text_font_5=pygame.font.Font(ASSETS_DIR / '0_font.ttf',25)
        self.quit_text0=self.text_font_5.render(f'Opponent Left...', True, 'red')
        self.quit_text1=self.text_font_5.render(f'You Resigned...', True, 'red')
        self.quit_text2=self.text_font_5.render(f'Opponent Resigned...', True, 'red')
        self.quit_text4=self.text_font_5.render(f'Opponent Left...', True, 'red')
        self.quit_text5=self.text_font_5.render(f"Keep Holding 'R' To Reset...", True, 'red')
        self.quit_text6=self.text_font_5.render(f"You Left", True, 'red')
        self.quit_text7=self.text_font_5.render(f"Draw By Repetition...", True, 'red')
        self.quit_text8=self.text_font_5.render(f"Draw By 50 Moves Rule...", True, 'red')
        self.quit_text9=self.text_font_5.render(f"WON", True, 'green')
        self.quit_text10=self.text_font_5.render(f"LOST", True, 'red')
        self.quit_text11=self.text_font_5.render(f"White Won", True, 'red')
        self.quit_text12=self.text_font_5.render(f"Black Won", True, 'red')
        self.quit_text13=self.text_font_5.render(f"DRAW", True, 'red')
        self.text_font_6=pygame.font.Font(ASSETS_DIR / '0_font.ttf',20)
        self.quit_text3=self.text_font_6.render(f"'Y' To Reset", True, 'darkgreen')
        self.quit_text0_rect=self.quit_text0.get_rect(center=(self.width/2,self.height/2-12))
        self.quit_text1_rect=self.quit_text1.get_rect(center=(self.width/2,self.height/2-12))
        self.quit_text2_rect=self.quit_text2.get_rect(center=(self.width/2,self.height/2-12))
        self.quit_text3_rect=self.quit_text3.get_rect(center=(self.width/2,self.height/2+12))
        self.quit_text4_rect=self.quit_text4.get_rect(center=(self.width/2,self.height/2-12))
        self.quit_text5_rect=self.quit_text5.get_rect(center=(self.width/2,self.height/2-12))
        self.quit_text6_rect=self.quit_text6.get_rect(center=(self.width/2,self.height/2-12))
        self.quit_text7_rect=self.quit_text7.get_rect(center=(self.width/2,self.height/2+30))
        self.quit_text8_rect=self.quit_text8.get_rect(center=(self.width/2,self.height/2+30))
        self.quit_text9_rect=self.quit_text9.get_rect(center=(self.width/2,self.height/2+30))
        self.quit_text10_rect=self.quit_text10.get_rect(center=(self.width/2,self.height/2+30))
        self.quit_text11_rect=self.quit_text11.get_rect(center=(self.width/2,self.height/2+30))
        self.quit_text12_rect=self.quit_text12.get_rect(center=(self.width/2,self.height/2+30))
        self.quit_text13_rect=self.quit_text13.get_rect(center=(self.width/2,self.height/2+30))

        self.color_text_white=self.text_font.render(f'WHITE', True, 'green')
        self.color_text_white_rect=self.color_text_white.get_rect(center=(self.width/2-64,self.height/2))

        self.color_text_black=self.text_font.render(f'BLACK', True, 'green')
        self.color_text_black_rect=self.color_text_black.get_rect(center=(self.width/2+64,self.height/2))

        self.select_color=pygame.image.load(ASSETS_DIR / "select_color.png").convert_alpha()
        self.select_color_rect=self.select_color.get_rect(center=(256,self.height/2))

        self.small_black=pygame.image.load(ASSETS_DIR / "small_black.png").convert_alpha()
        self.small_black_rect=self.small_black.get_rect(center=(256+64,self.height/2))

        self.small_white=pygame.image.load(ASSETS_DIR / "small_white.png").convert_alpha()
        self.small_white_rect=self.small_white.get_rect(center=(256-64,self.height/2))

        self.big_black=pygame.image.load(ASSETS_DIR / "large_black.png").convert_alpha()
        self.big_black_rect=self.big_black.get_rect(center=(256+64,self.height/2))

        self.big_white=pygame.image.load(ASSETS_DIR / "large_white.png").convert_alpha()
        self.big_white_rect=self.big_white.get_rect(center=(256-64,self.height/2))

        self.cross_image=pygame.image.load(ASSETS_DIR / "cross.png").convert_alpha()

        self.white_color_selected=0
        self.black_color_selected=0

        self.morph1=pygame.image.load(ASSETS_DIR / "morph1/morph1.png").convert_alpha()
        self.morph1_small_q=pygame.image.load(ASSETS_DIR / "morph1/small/q.png").convert_alpha()
        self.morph1_small_r=pygame.image.load(ASSETS_DIR / "morph1/small/r.png").convert_alpha()
        self.morph1_small_b=pygame.image.load(ASSETS_DIR / "morph1/small/b.png").convert_alpha()
        self.morph1_small_k=pygame.image.load(ASSETS_DIR / "morph1/small/k.png").convert_alpha()
        self.morph1_big_q=pygame.image.load(ASSETS_DIR / "morph1/big/q.png").convert_alpha()
        self.morph1_big_r=pygame.image.load(ASSETS_DIR / "morph1/big/r.png").convert_alpha()
        self.morph1_big_b=pygame.image.load(ASSETS_DIR / "morph1/big/b.png").convert_alpha()
        self.morph1_big_k=pygame.image.load(ASSETS_DIR / "morph1/big/k.png").convert_alpha()

        self.morph2=pygame.image.load(ASSETS_DIR / "morph2/morph2.png").convert_alpha()
        self.morph2_small_q=pygame.image.load(ASSETS_DIR / "morph2/small/q.png").convert_alpha()
        self.morph2_small_r=pygame.image.load(ASSETS_DIR / "morph2/small/r.png").convert_alpha()
        self.morph2_small_b=pygame.image.load(ASSETS_DIR / "morph2/small/b.png").convert_alpha()
        self.morph2_small_k=pygame.image.load(ASSETS_DIR / "morph2/small/k.png").convert_alpha()
        self.morph2_big_q=pygame.image.load(ASSETS_DIR / "morph2/big/q.png").convert_alpha()
        self.morph2_big_r=pygame.image.load(ASSETS_DIR / "morph2/big/r.png").convert_alpha()
        self.morph2_big_b=pygame.image.load(ASSETS_DIR / "morph2/big/b.png").convert_alpha()
        self.morph2_big_k=pygame.image.load(ASSETS_DIR / "morph2/big/k.png").convert_alpha()

        self.morph_rect=self.morph1.get_rect(center=(256,self.height/2))
        self.morph_variable=0

        self.morph_piece=-1
        self.morph_target=-1
        self.morph_pos=-1

        self.morph_list=[0,0,0,0]
        self.morph_list[0]=self.morph1_small_q.get_rect(topleft=(145,self.height/2-22))
        self.morph_list[1]=self.morph1_small_k.get_rect(topleft=(205,self.height/2-22))
        self.morph_list[2]=self.morph1_small_r.get_rect(topleft=(265,self.height/2-22))
        self.morph_list[3]=self.morph1_small_b.get_rect(topleft=(320,self.height/2-22))

        self.morph_background=pygame.image.load(ASSETS_DIR / "end.png").convert_alpha()

        self.morph_back_rect=self.morph2.get_rect(topleft=(0,0))

        self.red=pygame.image.load(ASSETS_DIR / "red.png").convert()
        self.indicator=pygame.image.load(ASSETS_DIR / "indicator.png").convert_alpha()
        self.red2=pygame.image.load(ASSETS_DIR / "red2.png").convert()
        self.yellow=pygame.image.load(ASSETS_DIR / "yellow.png").convert()
        self.blue=pygame.image.load(ASSETS_DIR / "blue.png").convert()
        self.green=pygame.image.load(ASSETS_DIR / "green.png").convert()

        self.dg=pygame.image.load(ASSETS_DIR / "darkg.png").convert()
        self.dg1=self.dg.get_rect(center=(0,0))

        self.lg=pygame.image.load(ASSETS_DIR / "lightg.png").convert()
        self.lg1=self.lg.get_rect(center=(0,0))

        self.piece[0]=pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha()
        self.position[0]=self.piece[0].get_rect(center=(self.x,self.x))

        self.piece[1]=pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha()
        self.position[1]=self.piece[1].get_rect(center=(3*self.x,self.x))

        self.piece[2]=pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha()
        self.position[2]=self.piece[2].get_rect(center=(5*self.x,self.x))

        self.piece[3]=pygame.image.load(ASSETS_DIR / "black/bq.png").convert_alpha()
        self.position[3]=self.piece[3].get_rect(center=(7*self.x,self.x))

        self.piece[4]=pygame.image.load(ASSETS_DIR / "black/bk.png").convert_alpha()
        self.position[4]=self.piece[4].get_rect(center=(9*self.x,self.x))

        self.piece[5]=pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha()
        self.position[5]=self.piece[5].get_rect(center=(11*self.x,self.x))

        self.piece[6]=pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha()
        self.position[6]=self.piece[6].get_rect(center=(13*self.x,self.x))

        self.piece[7]=pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha()
        self.position[7]=self.piece[7].get_rect(center=(15*self.x,self.x))

        self.piece[8]=pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha()
        self.position[8]=self.piece[8].get_rect(center=(self.x,3*self.x))

        for i in range(9,16):
            self.piece[i]=pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha()
            self.position[i]=self.piece[i].get_rect(center=(self.c*self.x,3*self.x))
            self.c+=2
        self.c=3

        self.piece[16]=pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha()
        self.position[16]=self.piece[16].get_rect(center=(self.x,15*self.x))

        self.piece[17]=pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha()
        self.position[17]=self.piece[17].get_rect(center=(3*self.x,15*self.x))

        self.piece[18]=pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha()
        self.position[18]=self.piece[18].get_rect(center=(5*self.x,15*self.x))

        self.piece[19]=pygame.image.load(ASSETS_DIR / "white/wq.png").convert_alpha()
        self.position[19]=self.piece[19].get_rect(center=(7*self.x,15*self.x))

        self.piece[20]=pygame.image.load(ASSETS_DIR / "white/wk.png").convert_alpha()
        self.position[20]=self.piece[20].get_rect(center=(9*self.x,15*self.x))

        self.piece[21]=pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha()
        self.position[21]=self.piece[21].get_rect(center=(11*self.x,15*self.x))

        self.piece[22]=pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha()
        self.position[22]=self.piece[22].get_rect(center=(13*self.x,15*self.x))

        self.piece[23]=pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha()
        self.position[23]=self.piece[23].get_rect(center=(15*self.x,15*self.x))

        self.piece[24]=pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha()
        self.position[24]=self.piece[24].get_rect(center=(self.x,13*self.x))

        for i in range(25,32):
            self.piece[i]=pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha()
            self.position[i]=self.piece[i].get_rect(center=(self.c*self.x,13*self.x))
            self.c+=2

        # pospos=position
        self.pospos=0
        self.pospos2=0

        self.images01=pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha()

        self.images=[]
        self.spots=[]
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha())
        self.spots.append(self.images[0].get_rect(center=(self.x,self.x)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha())
        self.spots.append(self.images[1].get_rect(center=(3*self.x,self.x)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha())
        self.spots.append(self.images[2].get_rect(center=(self.x*5,self.x)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bq.png").convert_alpha())
        self.spots.append(self.images[3].get_rect(center=(7*self.x,self.x)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bk.png").convert_alpha())
        self.spots.append(self.images[4].get_rect(center=(9*self.x,self.x)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha())
        self.spots.append(self.images[5].get_rect(center=(11*self.x,self.x)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha())
        self.spots.append(self.images[6].get_rect(center=(13*self.x,self.x)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha())
        self.spots.append(self.images[7].get_rect(center=(15*self.x,self.x)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
        self.spots.append(self.images[8].get_rect(center=(self.x,3*self.x)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
        self.spots.append(self.images[9].get_rect(center=(self.x*3,self.x*3)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
        self.spots.append(self.images[10].get_rect(center=(self.x*5,self.x*3)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
        self.spots.append(self.images[11].get_rect(center=(self.x*7,self.x*3)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
        self.spots.append(self.images[12].get_rect(center=(self.x*9,self.x*3)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
        self.spots.append(self.images[13].get_rect(center=(self.x*11,self.x*3)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
        self.spots.append(self.images[14].get_rect(center=(self.x*13,self.x*3)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
        self.spots.append(self.images[15].get_rect(center=(self.x*15,self.x*3)))

        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[16].get_rect(center=(self.x,self.x*5)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[17].get_rect(center=(self.x*3,self.x*5)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[18].get_rect(center=(self.x*5,self.x*5)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[19].get_rect(center=(self.x*7,self.x*5)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[20].get_rect(center=(self.x*9,self.x*5)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[21].get_rect(center=(self.x*11,self.x*5)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[22].get_rect(center=(self.x*13,self.x*5)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[23].get_rect(center=(self.x*15,self.x*5)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[24].get_rect(center=(self.x,self.x*7)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[25].get_rect(center=(self.x*3,self.x*7)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[26].get_rect(center=(self.x*5,self.x*7)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[27].get_rect(center=(self.x*7,self.x*7)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[28].get_rect(center=(self.x*9,self.x*7)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[29].get_rect(center=(self.x*11,self.x*7)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[30].get_rect(center=(self.x*13,self.x*7)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[31].get_rect(center=(self.x*15,self.x*7)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[32].get_rect(center=(self.x,self.x*9)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[33].get_rect(center=(self.x*3,self.x*9)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[34].get_rect(center=(self.x*5,self.x*9)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[35].get_rect(center=(self.x*7,self.x*9)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[36].get_rect(center=(self.x*9,self.x*9)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[37].get_rect(center=(self.x*11,self.x*9)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[38].get_rect(center=(self.x*13,self.x*9)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[39].get_rect(center=(self.x*15,self.x*9)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[40].get_rect(center=(self.x,self.x*11)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[41].get_rect(center=(self.x*3,self.x*11)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[42].get_rect(center=(self.x*5,self.x*11)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[43].get_rect(center=(self.x*7,self.x*11)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[44].get_rect(center=(self.x*9,self.x*11)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[45].get_rect(center=(self.x*11,self.x*11)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
        self.spots.append(self.images[46].get_rect(center=(self.x*13,self.x*11)))
        self.images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())

        self.spots.append(self.images[47].get_rect(center=(self.x*15,self.x*11)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
        self.spots.append(self.images[48].get_rect(center=(self.x,self.x*13)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
        self.spots.append(self.images[49].get_rect(center=(self.x*3,self.x*13)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
        self.spots.append(self.images[50].get_rect(center=(self.x*5,self.x*13)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
        self.spots.append(self.images[51].get_rect(center=(self.x*7,self.x*13)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
        self.spots.append(self.images[52].get_rect(center=(self.x*9,self.x*13)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
        self.spots.append(self.images[53].get_rect(center=(self.x*11,self.x*13)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
        self.spots.append(self.images[54].get_rect(center=(self.x*13,self.x*13)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
        self.spots.append(self.images[55].get_rect(center=(self.x*15,self.x*13)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha())
        self.spots.append(self.images[56].get_rect(center=(self.x,self.x*15)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha())
        self.spots.append(self.images[57].get_rect(center=(self.x*3,self.x*15)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha())
        self.spots.append(self.images[58].get_rect(center=(self.x*5,self.x*15)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wq.png").convert_alpha())
        self.spots.append(self.images[59].get_rect(center=(self.x*7,self.x*15)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wk.png").convert_alpha())
        self.spots.append(self.images[60].get_rect(center=(self.x*9,self.x*15)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha())
        self.spots.append(self.images[61].get_rect(center=(self.x*11,self.x*15)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha())
        self.spots.append(self.images[62].get_rect(center=(self.x*13,self.x*15)))
        self.images.append(pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha())
        self.spots.append(self.images[63].get_rect(center=(self.x*15,self.x*15)))

        self.sound_capture=pygame.mixer.Sound(AUDIO_DIR / "capture.mp3")
        self.sound_capture.set_volume(1)

        self.sound_castle=pygame.mixer.Sound(AUDIO_DIR / "castle.mp3")
        self.sound_castle.set_volume(1)

        self.sound_click=pygame.mixer.Sound(AUDIO_DIR / "click.mp3")
        self.sound_click.set_volume(1)

        self.sound_draw=pygame.mixer.Sound(AUDIO_DIR / "game-draw.mp3")
        self.sound_draw.set_volume(1)

        self.sound_end=pygame.mixer.Sound(AUDIO_DIR / "game-end.mp3")
        self.sound_end.set_volume(1)

        self.sound_illegal=pygame.mixer.Sound(AUDIO_DIR / "illegal.mp3")
        self.sound_illegal.set_volume(1)

        self.sound_bg_music=pygame.mixer.Sound(AUDIO_DIR / "bg_music.mp3")
        self.sound_bg_music.set_volume(0.3)
        self.channel4 = pygame.mixer.Channel(0)
        self.channel4.play(self.sound_bg_music, loops=-1)

        self.sound_check=pygame.mixer.Sound(AUDIO_DIR / "move-check.mp3")
        self.sound_check.set_volume(1)

        self.sound_self=pygame.mixer.Sound(AUDIO_DIR / "move-self.wav")
        self.sound_self.set_volume(1)

        self.sound_promote=pygame.mixer.Sound(AUDIO_DIR / "promote.mp3")
        self.sound_promote.set_volume(1)

        self.sound_tenseconds=pygame.mixer.Sound(AUDIO_DIR / "tenseconds.mp3")
        self.sound_tenseconds.set_volume(1)

        self.plus=0
        self.mouse_coordinate=0
        self.make_move=0

        self.previous_moves=0

        self.mouse_clicks_list=[]
        self.selected_1=-1
        self.coords_send=0
        self.og_x1_click=-1
        self.og_y1_click=-1
        self.mouse_lifted=-1
        self.click_select_with_drag=0
        self.mouse_went_outside=0

        self.reset_pressed_opponent=0
        self.reset_pressed_you=0
        self.reset_message_send=0
        self.reset_allowed=0

        self.early_exit=0

        self.game_is_reset=1

        self.gamemode=0
        self.opponent_gamemode=0

        self.splash_bg=pygame.image.load(MENU_DIR / "splash.png").convert()
        self.splash_bg1=self.splash_bg.get_rect(topleft=(0,0))

        self.offline_rect=pygame.draw.rect(self.screen,'black',(self.width/2-60,330-25+70,120,50))

        self.online_rect=pygame.draw.rect(self.screen,'black',(self.width/2-60,330-25,120,50))

        self.menu_rect=pygame.draw.rect(self.screen,'black',(self.width/2-60,330-25+70,120,50))

        self.my_sprite = pygame.image.load(MENU_DIR / "logo.png").convert_alpha()
        self.my_sprite_rect=self.my_sprite.get_rect(center=(self.width/2,self.height/2))


        self.menu_button_sound=0

        self.opponent_game_end=0

        self.repeat_game_end=0
        self.moves50_game_end=0
        self.only_king_game_end=0