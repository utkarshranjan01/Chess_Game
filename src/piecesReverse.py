from src.paths import *
from src.variables import *

def rev_pieces():
    global piece, position, images, spots
    images.append(pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "white/wq.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "white/wk.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha())

    for i in range (8):
        images.append(pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha())
    
    for i in range (32):
        images.append(pygame.image.load(ASSETS_DIR / "black/br2.png").convert_alpha())

    for i in range (8):
        images.append(pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha())

    images.append(pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "black/bq.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "black/bk.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha())
    images.append(pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha())
    piece[0]=pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha()
    piece[1]=pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha()
    piece[2]=pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha()
    piece[3]=pygame.image.load(ASSETS_DIR / "white/wq.png").convert_alpha()
    piece[4]=pygame.image.load(ASSETS_DIR / "white/wk.png").convert_alpha()
    piece[5]=pygame.image.load(ASSETS_DIR / "white/wb.png").convert_alpha()
    piece[6]=pygame.image.load(ASSETS_DIR / "white/wn.png").convert_alpha()
    piece[7]=pygame.image.load(ASSETS_DIR / "white/wr.png").convert_alpha()
    piece[8]=pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha()
    for i in range(9,16):
        piece[i]=pygame.image.load(ASSETS_DIR / "white/wp.png").convert_alpha()
    piece[16]=pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha()
    piece[17]=pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha()
    piece[18]=pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha()
    piece[19]=pygame.image.load(ASSETS_DIR / "black/bq.png").convert_alpha()
    piece[20]=pygame.image.load(ASSETS_DIR / "black/bk.png").convert_alpha()
    piece[21]=pygame.image.load(ASSETS_DIR / "black/bb.png").convert_alpha()
    piece[22]=pygame.image.load(ASSETS_DIR / "black/bn.png").convert_alpha()
    piece[23]=pygame.image.load(ASSETS_DIR / "black/br.png").convert_alpha()
    piece[24]=pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha()
    for i in range(25,32):
        piece[i]=pygame.image.load(ASSETS_DIR / "black/bp.png").convert_alpha()