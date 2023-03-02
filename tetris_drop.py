import random, sys, time, pygame
from pygame.locals import *

FPS = 40
WINDOWWIDTH = 600
WINDOWHEIGHT = 800
BOARDWIDTH = 350
BOARDHEIGHT = 700
PIECESIZE = 35

WHITE = (255, 255,255)
BRIGHTGREEN = (0, 255, 255)
DARKGRAY = (169, 169, 169)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
YELLOW = (155, 155, 0)
LIGHTBLUE = (173, 216, 230)
BLUE = (3, 37, 126)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
PURPLE = (221, 160, 221)
bgColor = DARKGRAY

pygame.init()

FPSCLOCK = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Blocky')

BASICFONT = pygame.font.SysFont('tahoma', 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SCREEN.fill(bgColor)
    pygame.draw.rect(SCREEN, BLACK, (125, 50, BOARDWIDTH, BOARDHEIGHT))
    pygame.display.update()
    FPSCLOCK.tick(FPS)
