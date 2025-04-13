import pygame
from main import *
from git_chess.src.paths import *
import os


def reset_all_variables2():

    global x, c, mouseX, mouseY, find, a, b, moved, piece, position, pos, pos2, board, color_board, count, flag, t1, t2, t3, select, selected, target, g, g1 ,found, king_under_check, king_under_checkmate, castle_white_1, castle_white_2, king_under_stalemate, castle_white_1, castle_white_2, castle_black_1, castle_black_2, border, q1, q2, a1, countcount, b1, t11, t21, clicked, cpos1, cpos2, ca, cb, ca1, cb1, value, gone, target2, got, out, target0, samec, ibk, iwk, en_pessant, moves_since_en_pessant, total_moves, white_king_has_moved, white_left_rook_has_moved, white_right_rook_has_moved, whi, black_left_rook_has_moved ,black_right_rook_has_moved, black_king_target_value2, black_king_target_value, white_king_target_value2, white_king_target_value, dragging, game_end, castle_being_done, inside_stalemate_function, draw_total_moves, board_repeat, board_copy, board_moves_copy, c1, c2, clicks, dist, gap, val2, dragpos, noc, _tester_, old_pos, noc_select, empty, sound_on, piece_moving, castle_white_done, castle_black_done, hovering_sound, hovering_sound2, white_color_selected, black_color_selected, morph_rect, morph_variable, morph_piece, morph_target, morph_pos, pospos, pospos2, plus, mouse_coordinate, make_move, previous_moves, mouse_clicks_list, selected_1, coords_send, og_x1_click, og_y1_click, mouse_lifted, click_select_with_drag, mouse_went_outside, reset_pressed_opponent, reset_pressed_you, reset_message_send, reset_allowed, early_exit, game_is_reset, gamemode, opponent_gamemode, menu_button_sound, opponent_game_end, repeat_game_end, moves50_game_end, only_king_game_end, clock, start_ticks, countdown_time, start_time,  sleep_counter1, sleep_counter2, sleep_counter3, opponent_color, turn_played, opponent_turn_played, total_moves_when_opponent_played, message, message_content, your_color, start_selection, selected_color, selection_done, mouse_x1_coordinate, mouse_x2_coordinate, mouse_y1_coordinate, mouse_y2_coordinate, final_selected_color, final_opponent_color, opponent_in_menu, numbers_str, click_event1, click_event2, click_event3, click_event4, prev_total_moves, move_made_by_opponent, morph_list, bg, bg1, bg_rev, images, images01, piece, position, spots, screen

    early_exit=0
    menu_button_sound=0
    repeat_game_end=0
    moves50_game_end=0
    only_king_game_end=0
    gamemode=0
    opponent_gamemode=0
    game_is_reset=1
    clock=pygame.time.Clock()
    width=512
    height=512
    x=32
    reset_pressed_opponent=0
    reset_pressed_you=0
    reset_message_send=0
    reset_allowed=0
    c=3
    mouseX=0
    plus=0
    mouseY=0
    find=0
    previous_moves=0
    make_move=0
    mouse_coordinate=0
    a=0
    b=0
    numbers_str=[]
    click_event1=-1
    click_event2=-1
    click_event3=-1
    click_event4=-1
    sleep_counter1=0 
    sleep_counter2=0
    sleep_counter3=0
    opponent_color=0
    countdown_time=5
    start_time=-1
    turn_played=0
    opponent_turn_played=0

    total_moves_when_opponent_played=0
    prev_total_moves=0
    move_made_by_opponent=-1
    message=''
    message_content=''

    your_color=0
    start_selection=0
    selected_color=0
    selection_done=0

    mouse_x1_coordinate=-1
    mouse_y1_coordinate=-1
    mouse_x2_coordinate=-1
    mouse_y2_coordinate=-1

    final_selected_color=0
    final_opponent_color=0

    opponent_in_menu=0
    moved=0
    piece=[None]*32
    position=[None]*32
    pos= [[0 for _ in range(8)] for _ in range(8)]
    pos2= []
    board = [[0 for _ in range(8)] for _ in range(8)]
    color_board = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        color_board[0][i]=1
        color_board[1][i]=1
        color_board[6][i]=2
        color_board[7][i]=2
    count=0
    flag=0
    t1=-1
    t2=-1
    t3=-1
    select=[-1,-1]
    selected=[-1,-1]
    target=-1
    g=0
    g1=0
    found=0
    king_under_check=0
    king_under_checkmate=0
    king_under_stalemate=0
    castle_white_1=0
    castle_white_2=0
    castle_black_1=0
    castle_black_2=0
    border=4

    q1=0
    q2=0
    a1=0
    countcount=0
    b1=0
    t11=0
    t21=0
    clicked=0
    cpos1=0
    cpos2=0
    ca=cb=ca1=cb1=0
    value=0
    gone=0
    target2=-1
    got=0
    out=[]
    target0=-1
    samec=0
    ibk=4
    iwk=28
    en_pessant=0
    moves_since_en_pessant=0
    total_moves=0
    white_king_has_moved=0
    white_left_rook_has_moved=0
    white_right_rook_has_moved=0
    whi=0
    black_left_rook_has_moved=0
    black_right_rook_has_moved=0
    black_king_target_value2=[0,4]
    black_king_target_value=[0,4]
    white_king_target_value2=[7,4]
    white_king_target_value=[7,4]
    dragging=0
    game_end=0
    mouse_clicks_list=[]
    selected_1=-1
    coords_send=0
    og_x1_click=-1
    og_y1_click=-1
    mouse_lifted=-1
    click_select_with_drag=0
    mouse_went_outside=0
    inside_stalemate_function=0
    castle_being_done=0
    for i in range(64):
        pos2.append([q1,q2])
        if q2<7:
            q2+=1
        else:
            q2=0
            q1+=1

    for i in range(0, 8):
        board[0][i]=1
        board[1][i]=1
        board[6][i]=1
        board[7][i]=1

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

    draw_total_moves=0
    board_repeat=[0]
    board_copy=[]
    board_copy.append([[[0 for _ in range(8)] for _ in range(8)],[[0 for _ in range(8)] for _ in range(8)]])
    for i in range(8):
        for j in range(8):
            board_copy[len(board_copy)-1][0][i][j]=board[i][j]
            board_copy[len(board_copy)-1][1][i][j]=color_board[i][j]

    board_moves_copy=0

    c1=1
    c2=1
    clicks=0
    dist=0
    gap=0
    val2=0
    dragpos=0
    noc=0
    _tester_=-1
    old_pos=0
    noc_select=[-1,-1]
    empty=0
    piece_moving=0
    castle_white_done=0
    castle_black_done=0
    hovering_sound=-1
    hovering_sound2=-1
    for i in range(0,8):
        for j in range(0,8):
            pos[i][j]=[c1*x,c2*x]
            c1+=2
        c1=1
        c2+=2
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Chess')

    bg=pygame.image.load(os.path.join("assets/things2","Board4.png"))
    bg1=bg.get_rect(topleft=(0,0))

    morph_variable=0

    white_color_selected=0
    black_color_selected=0

    morph_piece=-1
    morph_target=-1
    morph_pos=-1

    piece[0]=pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha()
    position[0]=piece[0].get_rect(center=(x,x))

    piece[1]=pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha()
    position[1]=piece[1].get_rect(center=(3*x,x))

    piece[2]=pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha()
    position[2]=piece[2].get_rect(center=(5*x,x))

    piece[3]=pygame.image.load(ASSETS_DIR / "black/bq.png").convert_alpha()
    position[3]=piece[3].get_rect(center=(7*x,x))

    piece[4]=pygame.image.load(ASSETS_DIR / "black/bk.png").convert_alpha()
    position[4]=piece[4].get_rect(center=(9*x,x))

    piece[5]=pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha()
    position[5]=piece[5].get_rect(center=(11*x,x))

    piece[6]=pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha()
    position[6]=piece[6].get_rect(center=(13*x,x))

    piece[7]=pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha()
    position[7]=piece[7].get_rect(center=(15*x,x))

    piece[8]=pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha()
    position[8]=piece[8].get_rect(center=(x,3*x))

    for i in range(9,16):
        piece[i]=pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha()
        position[i]=piece[i].get_rect(center=(c*x,3*x))
        c+=2
    c=3

    piece[16]=pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha()
    position[16]=piece[16].get_rect(center=(x,15*x))

    piece[17]=pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha()
    position[17]=piece[17].get_rect(center=(3*x,15*x))

    piece[18]=pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha()
    position[18]=piece[18].get_rect(center=(5*x,15*x))

    piece[19]=pygame.image.load(ASSETS_DIR / "white/wq.png").convert_alpha()
    position[19]=piece[19].get_rect(center=(7*x,15*x))

    piece[20]=pygame.image.load(ASSETS_DIR / "white/wk.png").convert_alpha()
    position[20]=piece[20].get_rect(center=(9*x,15*x))

    piece[21]=pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha()
    position[21]=piece[21].get_rect(center=(11*x,15*x))

    piece[22]=pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha()
    position[22]=piece[22].get_rect(center=(13*x,15*x))

    piece[23]=pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha()
    position[23]=piece[23].get_rect(center=(15*x,15*x))

    piece[24]=pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha()
    position[24]=piece[24].get_rect(center=(x,13*x))

    for i in range(25,32):
        piece[i]=pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha()
        position[i]=piece[i].get_rect(center=(c*x,13*x))
        c+=2

    pospos=0
    pospos2=0

    bg=pygame.image.load(ASSETS_DIR / "Board4.png").convert()
    bg_rev=pygame.image.load(ASSETS_DIR / "Board4_rev.png").convert()
    bg1=bg.get_rect(topleft=(0,0))

    images01=pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha()

    images=[]
    spots=[]
    images.append(pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha())
    spots.append(images[0].get_rect(center=(x,x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha())
    spots.append(images[1].get_rect(center=(3*x,x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha())
    spots.append(images[2].get_rect(center=(5*x,x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bq.png").convert_alpha())
    spots.append(images[3].get_rect(center=(7*x,x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bk.png").convert_alpha())
    spots.append(images[4].get_rect(center=(9*x,x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha())
    spots.append(images[5].get_rect(center=(11*x,x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha())
    spots.append(images[6].get_rect(center=(13*x,x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha())
    spots.append(images[7].get_rect(center=(15*x,x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
    spots.append(images[8].get_rect(center=(x,3*x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
    spots.append(images[9].get_rect(center=(3*x,3*x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
    spots.append(images[10].get_rect(center=(5*x,3*x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
    spots.append(images[11].get_rect(center=(7*x,3*x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
    spots.append(images[12].get_rect(center=(9*x,3*x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
    spots.append(images[13].get_rect(center=(11*x,3*x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
    spots.append(images[14].get_rect(center=(13*x,3*x)))
    images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())
    spots.append(images[15].get_rect(center=(15*x,3*x)))

    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[16].get_rect(center=(x,x*5)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[17].get_rect(center=(x*3,x*5)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[18].get_rect(center=(x*5,x*5)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[19].get_rect(center=(x*7,x*5)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[20].get_rect(center=(x*9,x*5)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[21].get_rect(center=(x*11,x*5)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[22].get_rect(center=(x*13,x*5)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[23].get_rect(center=(x*15,x*5)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[24].get_rect(center=(x,x*7)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[25].get_rect(center=(x*3,x*7)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[26].get_rect(center=(x*5,x*7)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[27].get_rect(center=(x*7,x*7)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[28].get_rect(center=(x*9,x*7)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[29].get_rect(center=(x*11,x*7)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[30].get_rect(center=(x*13,x*7)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[31].get_rect(center=(x*15,x*7)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[32].get_rect(center=(x,x*9)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[33].get_rect(center=(x*3,x*9)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[34].get_rect(center=(x*5,x*9)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[35].get_rect(center=(x*7,x*9)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[36].get_rect(center=(x*9,x*9)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[37].get_rect(center=(x*11,x*9)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[38].get_rect(center=(x*13,x*9)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[39].get_rect(center=(x*15,x*9)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[40].get_rect(center=(x,x*11)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[41].get_rect(center=(x*3,x*11)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[42].get_rect(center=(x*5,x*11)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[43].get_rect(center=(x*7,x*11)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[44].get_rect(center=(x*9,x*11)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[45].get_rect(center=(x*11,x*11)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())
    spots.append(images[46].get_rect(center=(x*13,x*11)))
    images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())

    spots.append(images[47].get_rect(center=(x*15,x*11)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
    spots.append(images[48].get_rect(center=(x,x*13)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
    spots.append(images[49].get_rect(center=(3*x,x*13)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
    spots.append(images[50].get_rect(center=(5*x,x*13)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
    spots.append(images[51].get_rect(center=(7*x,x*13)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
    spots.append(images[52].get_rect(center=(9*x,x*13)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
    spots.append(images[53].get_rect(center=(11*x,x*13)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
    spots.append(images[54].get_rect(center=(13*x,x*13)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
    spots.append(images[55].get_rect(center=(15*x,x*13)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha())
    spots.append(images[56].get_rect(center=(x,x*15)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha())
    spots.append(images[57].get_rect(center=(x*3,x*15)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha())
    spots.append(images[58].get_rect(center=(x*5,x*15)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wq.png").convert_alpha())
    spots.append(images[59].get_rect(center=(x*7,x*15)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wk.png").convert_alpha())
    spots.append(images[60].get_rect(center=(x*9,x*15)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha())
    spots.append(images[61].get_rect(center=(x*11,x*15)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha())
    spots.append(images[62].get_rect(center=(x*13,x*15)))
    images.append(pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha())
    spots.append(images[63].get_rect(center=(x*15,x*15)))

    clock = pygame.time.Clock()
    start_ticks = None

