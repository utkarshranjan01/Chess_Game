import math
from src.paths import *
from src.variables import *

def fill_online_small():
    global online_rect, menu_button_sound
    button_font=pygame.font.Font(ASSETS_DIR / '0_font.ttf',35)
    online_button=button_font.render(f'ONLINE', True, 'black')
    online_button_rect=online_button.get_rect(center=(width/2,330))
    online_rect=pygame.draw.rect(screen,'black',(width/2-60,330-25,120,50))
    pygame.draw.rect(screen,'black',(width/2-60,330-25,120,50))
    pygame.draw.rect(screen,'white',(width/2-55,330-20,110,40))
    screen.blit(online_button, online_button_rect)
    if menu_button_sound==1:
        menu_button_sound=0

def fill_offline_small():
    global offline_rect, menu_button_sound
    button_font=pygame.font.Font(ASSETS_DIR / '0_font.ttf',35)
    offline_button=button_font.render(f'OFFLINE', True, 'black')
    offline_button_rect=offline_button.get_rect(center=(width/2,350+50))
    offline_rect=pygame.draw.rect(screen,'black',(width/2-60,330-25+70,120,50))
    pygame.draw.rect(screen,'black',(width/2-60,330-25+70,120,50))
    pygame.draw.rect(screen,'white',(width/2-55,330-20+70,110,40))
    screen.blit(offline_button, offline_button_rect)
    if menu_button_sound==2:
        menu_button_sound=0

def fill_online_big():
    global online_rect, menu_button_sound
    button_font=pygame.font.Font(ASSETS_DIR / '0_font.ttf',40)
    online_button=button_font.render(f'ONLINE', True, 'black')
    online_button_rect=online_button.get_rect(center=(width/2,330))
    online_rect=pygame.draw.rect(screen,'black',(width/2-60-10,330-25,120+18,50))
    pygame.draw.rect(screen,'black',(width/2-60-10,330-25,120+18,50))
    pygame.draw.rect(screen,'white',(width/2-55-10,330-20,110+18,40))
    screen.blit(online_button, online_button_rect)
    if menu_button_sound!=1:
        sound_click.play()
        menu_button_sound=1

def fill_offline_big():
    global offline_rect, menu_button_sound, sound_click
    button_font=pygame.font.Font(ASSETS_DIR / '0_font.ttf',40)
    offline_button=button_font.render(f'OFFLINE', True, 'black')
    offline_button_rect=offline_button.get_rect(center=(width/2,350+50))
    offline_rect=pygame.draw.rect(screen,'black',(width/2-60-10,330-25+70,120+18,50))
    pygame.draw.rect(screen,'black',(width/2-60-10,330-25+70,120+18,50))
    pygame.draw.rect(screen,'white',(width/2-55-10,330-20+70,110+18,40))
    screen.blit(offline_button, offline_button_rect)
    if menu_button_sound!=2:
        sound_click.play()
        menu_button_sound=2
    
def fill_menu():
    global menu_rect
    button_font=pygame.font.Font(ASSETS_DIR / '0_font.ttf',35)
    offline_button=button_font.render(f'MENU', True, 'black')
    offline_button_rect=offline_button.get_rect(center=(width/2,350+50))
    menu_rect=pygame.draw.rect(screen,'black',(width/2-60,330-25+70,120,50))
    pygame.draw.rect(screen,'black',(width/2-60,330-25+70,120,50))
    pygame.draw.rect(screen,'white',(width/2-55,330-20+70,110,40))
    screen.blit(offline_button, offline_button_rect)

def displaying_menu(gs, pygame, animation, my_sprite_rect):
    if gs.gamemode==0:
        screen.blit(splash_bg,splash_bg1)
    
        next(animation)

        if (online_rect).collidepoint(pygame.mouse.get_pos())==True:
            fill_online_big()
        else:
            fill_online_small()

        if (offline_rect).collidepoint(pygame.mouse.get_pos())==True:
            fill_offline_big()
        else:
            fill_offline_small()

        screen.blit(my_sprite, my_sprite_rect)