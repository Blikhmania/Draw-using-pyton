import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
#COLOR    R    G    B
AQUA  = (000, 255, 255)
BLACK = (000, 000, 000)
BLUE  = (  0,   0, 200)
GRAY  = (128, 128, 128)
GREEN = (000, 255, 000)
LIME  = ( 40, 128,  40)
RED   = (255, 000, 000)
WHITE = (255, 255, 255)
ORANGE= (200, 200,   0)

# draw on the surface object

DISPLAYSURF.fill(WHITE)
pygame.draw.rect(DISPLAYSURF, GREEN, (0,220,500,200))
pygame.draw.rect(DISPLAYSURF, BLUE , (0,0,500,220))
pygame.draw.polygon(DISPLAYSURF, GRAY, ((236, 156), (236, 327), (56, 327), (56, 156)))
pygame.draw.polygon(DISPLAYSURF, LIME, ((146, 50), (300, 30), (385, 110), (236, 156)))
pygame.draw.polygon(DISPLAYSURF, GRAY, ((236, 156), (385, 110), (385, 275), (236, 327)))
pygame.draw.polygon(DISPLAYSURF, BLACK, ((320, 160), (295,170), (295, 190), (320,180)))
pygame.draw.polygon(DISPLAYSURF, LIME, ((56,156),(236,156),(146,50)))
pygame.draw.aaline(DISPLAYSURF, BLACK, (56, 156), (236, 156), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (146, 50), (56, 156), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (147, 50), (237, 156), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (236, 156), (236, 327), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (236, 327), (56, 327), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (56, 327), (56, 156), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (146, 50), (300, 30), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (300, 30), (385, 110), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (385, 110), (236, 156), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (385, 110), (385, 275), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (385, 275), (236, 327), 2)
pygame.draw.aaline(DISPLAYSURF, BLACK, (0,220),(56,220),5)
pygame.draw.aaline(DISPLAYSURF, BLACK, (385,220),(500,220),5)
pygame.draw.circle(DISPLAYSURF, BLACK, (146, 110), 20, 0)
pygame.draw.rect(DISPLAYSURF, BLACK, (95, 200, 110, 127))
pygame.draw.circle(DISPLAYSURF, ORANGE, (450, 90), 20, 0)

pixObj = pygame.PixelArray(DISPLAYSURF)
del pixObj
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
