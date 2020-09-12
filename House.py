import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
# draw on the surface object

DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, RED, ((146, 50), (236, 156), (236, 327), (56, 327), (56, 156)))
pygame.draw.polygon(DISPLAYSURF, RED, ((146, 50), (300, 30), (385, 110), (236, 156)))
pygame.draw.polygon(DISPLAYSURF, RED, ((236, 156), (385, 110), (385, 275), (236, 327)))
pygame.draw.polygon(DISPLAYSURF, BLACK, ((320, 160), (295,170), (295, 190), (320,180)))
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
pygame.draw.circle(DISPLAYSURF, BLACK, (146, 110), 20, 0)
#pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, BLACK, (95, 200, 110, 127))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
