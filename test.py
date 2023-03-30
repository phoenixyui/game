import pygame
from pygame.locals import *
from pygame.locals import QUIT
import sys
import time
import threading
import random
import math
pygame.init()

screen = pygame.display.set_mode([500, 500])
secWindows = pygame.surface.Surface((500,500), SRCALPHA, 32)
gameover=pygame.font.SysFont(None,100)
gameoverText=gameover.render("YOU DIED",True,(255,0,0))
secWindows.fill((0,0,0,50))
secWindows.blit(gameoverText,(100,100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(secWindows,(0,0))

    pygame.display.flip()

pygame.quit()