import pygame
from pygame.locals import *
from pygame.locals import QUIT
import sys
import time
import threading
import random
import math
pygame.init()
surface=[800,600]
mainWindows=pygame.display.set_mode((surface[0],surface[1]),RESIZABLE,32)
secWindows = pygame.surface.Surface((500,500), SRCALPHA, 32)
usercolor=(255,0,0)
mainWindows.fill((255, 255, 255))
userposition=[surface[0]/2-surface[0]/16,surface[1]*0.75,surface[0]/8,surface[1]*0.25]
gameover=pygame.font.SysFont(None,100)
gameoverText=gameover.render("YOU DIED",True,(255,0,0))
#secWindows.fill((0,0,0,50))
#secWindows.blit(gameoverText,(100,100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+userposition[2]/3),userposition[2]/3)
            #身體
    pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+2*userposition[2]/3),(userposition[0]+userposition[2]/2,userposition[1]+4*userposition[2]/3),3)
            #左腳
    pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+4*userposition[2]/3),(userposition[0]+userposition[2]/4,userposition[1]+5.5*userposition[2]/3),3)
            #右腳
    pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+4*userposition[2]/3),(userposition[0]+userposition[2]*3/4,userposition[1]+5.5*userposition[2]/3),3)
            #左手
    pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+userposition[2]),(userposition[0]+userposition[2]/4,userposition[1]+userposition[2]*0.6),3)        
            #右手
    pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+userposition[2]),(userposition[0]+userposition[2]*5/8,userposition[1]+userposition[2]*1.1),3)
    pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]*5/8,userposition[1]+userposition[2]*1.1),(userposition[0]+userposition[2]*3/4,userposition[1]+userposition[2]*0.85),3)
    
    #mainWindows.blit(secWindows,(0,0))

    pygame.display.update()

pygame.quit()