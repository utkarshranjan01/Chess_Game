import pygame
from src.paths import *
import socket
from constants import *


def make_list6():
    pos2=[]
    q1=0
    q2=0
    for i in range(64):
        pos2.append([q1,q2])
        if q2<7:
            q2+=1
        else:
            q2=0
            q1+=1
    return pos2

def make_list7():
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

    return images, spots

def make_list8():
    x=32
    c=3
    piece=[None]*32
    position=[None]*32

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

    return piece, position

def make_list9():
    c1=1
    c2=1
    pos=[[0 for _ in range(8)] for _ in range(8)]
    for i in range(0,8):
        for j in range(0,8):
            pos[i][j]=[c1*x,c2*x]
            c1+=2
        c1=1
        c2+=2

    return pos

pygame.init()
width=WIDTH
height=HEIGHT
clock = pygame.time.Clock()
start_ticks = None
screen=pygame.display.set_mode((width,height))

ip_address=IP_ADDRESS
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x=32
c=3
mouseX=0
mouseY=0

count=0
border=4
q1=0
q2=0
got=0
ibk=4
iwk=28
c1=1
c2=1
dist=0
gap=0
val2=0
dragpos=0
empty=0
sound_on=1

white_color_selected=0
black_color_selected=0
# pospos=position
plus=0

previous_moves=0

click_select_with_drag=0
mouse_went_outside=0

early_exit=0

menu_button_sound=0



bg=pygame.image.load(ASSETS_DIR / "Board4.png").convert()
bg_rev=pygame.image.load(ASSETS_DIR / "Board4_rev.png").convert()
bg1=bg.get_rect(topleft=(0,0))

text_font=pygame.font.Font(ASSETS_DIR / "0_font.ttf",40)

wait_text=text_font.render(f'Waiting For Another Player...', True, 'white')
wait_text_rect=wait_text.get_rect(center=(width/2,height/2))

join_text=text_font.render(f'Waiting For Server To Be Online...', True, 'white')
join_text_rect=join_text.get_rect(center=(width/2,height/2))

text_font_5=pygame.font.Font(ASSETS_DIR / '0_font.ttf',30)
quit_text=text_font_5.render(f'QUITS', True, 'red')
text_font_5=pygame.font.Font(ASSETS_DIR / '0_font.ttf',25)
quit_text0=text_font_5.render(f'Opponent Left...', True, 'red')
quit_text1=text_font_5.render(f'You Resigned...', True, 'red')
quit_text2=text_font_5.render(f'Opponent Resigned...', True, 'red')
quit_text4=text_font_5.render(f'Opponent Left...', True, 'red')
quit_text5=text_font_5.render(f"Keep Holding 'R' To Reset...", True, 'red')
quit_text6=text_font_5.render(f"You Left", True, 'red')
quit_text7=text_font_5.render(f"Draw By Repetition...", True, 'red')
quit_text8=text_font_5.render(f"Draw By 50 Moves Rule...", True, 'red')
quit_text9=text_font_5.render(f"WON", True, 'green')
quit_text10=text_font_5.render(f"LOST", True, 'red')
quit_text11=text_font_5.render(f"White Won", True, 'red')
quit_text12=text_font_5.render(f"Black Won", True, 'red')
quit_text13=text_font_5.render(f"DRAW", True, 'red')
quit_text15=text_font_5.render(f"'R' To Reset...", True, 'red')
text_font_6=pygame.font.Font(ASSETS_DIR / '0_font.ttf',20)
quit_text3=text_font_6.render(f"'Y' To Reset", True, 'darkgreen')
quit_text0_rect=quit_text0.get_rect(center=(width/2,height/2-12))
quit_text1_rect=quit_text1.get_rect(center=(width/2,height/2-12))
quit_text2_rect=quit_text2.get_rect(center=(width/2,height/2-12))
quit_text3_rect=quit_text3.get_rect(center=(width/2,height/2+12))
quit_text4_rect=quit_text4.get_rect(center=(width/2,height/2-12))
quit_text5_rect=quit_text5.get_rect(center=(width/2,height/2-12))
quit_text6_rect=quit_text6.get_rect(center=(width/2,height/2-12))
quit_text7_rect=quit_text7.get_rect(center=(width/2,height/2+30))
quit_text8_rect=quit_text8.get_rect(center=(width/2,height/2+30))
quit_text9_rect=quit_text9.get_rect(center=(width/2,height/2+30))
quit_text10_rect=quit_text10.get_rect(center=(width/2,height/2+30))
quit_text11_rect=quit_text11.get_rect(center=(width/2,height/2+30))
quit_text12_rect=quit_text12.get_rect(center=(width/2,height/2+30))
quit_text13_rect=quit_text13.get_rect(center=(width/2,height/2+30))
quit_text15_rect=quit_text15.get_rect(center=(width/2+2,height/2-12))

color_text_white=text_font.render(f'WHITE', True, 'green')
color_text_white_rect=color_text_white.get_rect(center=(width/2-64,height/2))

color_text_black=text_font.render(f'BLACK', True, 'green')
color_text_black_rect=color_text_black.get_rect(center=(width/2+64,height/2))

select_color=pygame.image.load(ASSETS_DIR / "select_color.png").convert_alpha()
select_color_rect=select_color.get_rect(center=(256,height/2))

small_black=pygame.image.load(ASSETS_DIR / "small_black.png").convert_alpha()
small_black_rect=small_black.get_rect(center=(256+64,height/2))

small_white=pygame.image.load(ASSETS_DIR / "small_white.png").convert_alpha()
small_white_rect=small_white.get_rect(center=(256-64,height/2))

big_black=pygame.image.load(ASSETS_DIR / "large_black.png").convert_alpha()
big_black_rect=big_black.get_rect(center=(256+64,height/2))

big_white=pygame.image.load(ASSETS_DIR / "large_white.png").convert_alpha()
big_white_rect=big_white.get_rect(center=(256-64,height/2))

cross_image=pygame.image.load(ASSETS_DIR / "cross.png").convert_alpha()



morph1=pygame.image.load(ASSETS_DIR / "morph1/morph1.png").convert_alpha()
morph1_small_q=pygame.image.load(ASSETS_DIR / "morph1/small/q.png").convert_alpha()
morph1_small_r=pygame.image.load(ASSETS_DIR / "morph1/small/r.png").convert_alpha()
morph1_small_b=pygame.image.load(ASSETS_DIR / "morph1/small/b.png").convert_alpha()
morph1_small_k=pygame.image.load(ASSETS_DIR / "morph1/small/k.png").convert_alpha()
morph1_big_q=pygame.image.load(ASSETS_DIR / "morph1/big/q.png").convert_alpha()
morph1_big_r=pygame.image.load(ASSETS_DIR / "morph1/big/r.png").convert_alpha()
morph1_big_b=pygame.image.load(ASSETS_DIR / "morph1/big/b.png").convert_alpha()
morph1_big_k=pygame.image.load(ASSETS_DIR / "morph1/big/k.png").convert_alpha()

morph2=pygame.image.load(ASSETS_DIR / "morph2/morph2.png").convert_alpha()
morph2_small_q=pygame.image.load(ASSETS_DIR / "morph2/small/q.png").convert_alpha()
morph2_small_r=pygame.image.load(ASSETS_DIR / "morph2/small/r.png").convert_alpha()
morph2_small_b=pygame.image.load(ASSETS_DIR / "morph2/small/b.png").convert_alpha()
morph2_small_k=pygame.image.load(ASSETS_DIR / "morph2/small/k.png").convert_alpha()
morph2_big_q=pygame.image.load(ASSETS_DIR / "morph2/big/q.png").convert_alpha()
morph2_big_r=pygame.image.load(ASSETS_DIR / "morph2/big/r.png").convert_alpha()
morph2_big_b=pygame.image.load(ASSETS_DIR / "morph2/big/b.png").convert_alpha()
morph2_big_k=pygame.image.load(ASSETS_DIR / "morph2/big/k.png").convert_alpha()

morph_rect=morph1.get_rect(center=(256,height/2))

morph_list=[0,0,0,0]
morph_list[0]=morph1_small_q.get_rect(topleft=(145,height/2-22))
morph_list[1]=morph1_small_k.get_rect(topleft=(205,height/2-22))
morph_list[2]=morph1_small_r.get_rect(topleft=(265,height/2-22))
morph_list[3]=morph1_small_b.get_rect(topleft=(320,height/2-22))

morph_background=pygame.image.load(ASSETS_DIR / "end.png").convert_alpha()

morph_back_rect=morph2.get_rect(topleft=(0,0))

red=pygame.image.load(ASSETS_DIR / "red.png").convert()
indicator=pygame.image.load(ASSETS_DIR / "indicator.png").convert_alpha()
red2=pygame.image.load(ASSETS_DIR / "red2.png").convert()
yellow=pygame.image.load(ASSETS_DIR / "yellow.png").convert()
blue=pygame.image.load(ASSETS_DIR / "blue.png").convert()
green=pygame.image.load(ASSETS_DIR / "green.png").convert()

dg=pygame.image.load(ASSETS_DIR / "darkg.png").convert()
dg1=dg.get_rect(center=(0,0))

lg=pygame.image.load(ASSETS_DIR / "lightg.png").convert()
lg1=lg.get_rect(center=(0,0))

images01=pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha()

sound_capture=pygame.mixer.Sound(AUDIO_DIR / "capture.mp3")
sound_capture.set_volume(1)

sound_castle=pygame.mixer.Sound(AUDIO_DIR / "castle.mp3")
sound_castle.set_volume(1)

sound_click=pygame.mixer.Sound(AUDIO_DIR / "click.mp3")
sound_click.set_volume(1)

sound_draw=pygame.mixer.Sound(AUDIO_DIR / "game-draw.mp3")
sound_draw.set_volume(1)

sound_end=pygame.mixer.Sound(AUDIO_DIR / "game-end.mp3")
sound_end.set_volume(1)

sound_illegal=pygame.mixer.Sound(AUDIO_DIR / "illegal.mp3")
sound_illegal.set_volume(1)

sound_bg_music=pygame.mixer.Sound(AUDIO_DIR / "bg_music.mp3")
sound_bg_music.set_volume(0.3)
channel4 = pygame.mixer.Channel(0)
channel4.play(sound_bg_music, loops=-1)

sound_check=pygame.mixer.Sound(AUDIO_DIR / "move-check.mp3")
sound_check.set_volume(1)

sound_self=pygame.mixer.Sound(AUDIO_DIR / "move-self.wav")
sound_self.set_volume(1)

sound_promote=pygame.mixer.Sound(AUDIO_DIR / "promote.mp3")
sound_promote.set_volume(1)

sound_tenseconds=pygame.mixer.Sound(AUDIO_DIR / "tenseconds.mp3")
sound_tenseconds.set_volume(1)

splash_bg=pygame.image.load(MENU_DIR / "splash.png").convert()
splash_bg1=splash_bg.get_rect(topleft=(0,0))

offline_rect=pygame.draw.rect(screen,'black',(width/2-60,330-25+70,120,50))

online_rect=pygame.draw.rect(screen,'black',(width/2-60,330-25,120,50))

menu_rect=pygame.draw.rect(screen,'black',(width/2-60,330-25+70,120,50))

my_sprite = pygame.image.load(MENU_DIR / "logo.png").convert_alpha()
my_sprite_rect=my_sprite.get_rect(center=(width/2,height/2))
