import pygame
from pygame.locals import *
from pygame.locals import QUIT
import sys
import time
import threading
import random
import math

## 初始化 ##
x=0
y=0
flag=0
bossflag=0
bosslife=0
life=0
winflag=[0,0,0,0]
surface=[800,600]
windows_colors=(0,0,0)
currentScene="menu"
currentClick=[0,0,"menu"]
pygame.init()
mainWindows=pygame.display.set_mode((surface[0],surface[1]),RESIZABLE,32)
mainWindows.fill(windows_colors)
userposition=[surface[0]/2-surface[0]/16,surface[1]*0.75,surface[0]/8,surface[1]*0.25]
destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
distance=[0,5] ## 0 左 1 右 2 上 3 下 4 後
clock = pygame.time.Clock()
timeout=0
attTimeout=0
attType=0
height=0
waittimeout=0
gameovertimeout=0
visibility=0
gflag=0

## menu interface ##
def Menu():
    global currentScene
    mainWindows.fill((0,0,0))
    pygame.draw.rect(mainWindows,(255,255,255),((surface[0]-300)/2,surface[1]-200,300,200))
    menuImage=pygame.image.load("./image/menu.jpg").convert()
    mainWindows.blit(menuImage,[0,0])
    menuFont=pygame.font.SysFont(None,60)
    startText=menuFont.render("start",True,(0,0,0))
    mainWindows.blit(startText,((surface[0]-300)/2+100,surface[1]-180))
    optionalText=menuFont.render("optional",True,(0,0,0))
    mainWindows.blit(optionalText,((surface[0]-300)/2+80,surface[1]-120))
    exitText=menuFont.render("exit",True,(0,0,0))
    mainWindows.blit(exitText,((surface[0]-300)/2+110,surface[1]-60))

    if(x>=(surface[0]-300)/2 and x<=(surface[0]-300)/2+300 and y>=surface[1]-200 and y<=surface[1]-200+66):
        pygame.draw.rect(mainWindows,(255,0,0),((surface[0]-300)/2,surface[1]-200,300,66),width=1,border_radius=3)
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="selectMode"

    elif(x>=(surface[0]-300)/2 and x<=(surface[0]-300)/2+300 and y>=surface[1]-200+67 and y<=surface[1]-200+132):
        pygame.draw.rect(mainWindows,(255,0,0),((surface[0]-300)/2,surface[1]-200+67,300,66),width=1,border_radius=3)
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="optional"

    elif(x>=(surface[0]-300)/2 and x<=(surface[0]-300)/2+300 and y>=surface[1]-200+133 and y<=surface[1]):
        pygame.draw.rect(mainWindows,(255,0,0),((surface[0]-300)/2,surface[1]-200+133,300,66),width=1,border_radius=3)
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.quit()
            sys.exit()

## optional interface ##
def optional():
    global currentScene
    mainWindows.fill((0,0,0))
    menuImage=pygame.image.load("./image/menu.jpg").convert()
    mainWindows.blit(menuImage,[0,0])
    opFont=pygame.font.SysFont(None,100)
    returnText=opFont.render("return",True,(0,0,0))
    mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.85))

    if(x>=surface[0]*0.05 and x<=surface[0]*0.05+200 and y>= surface[1]*0.85-5 and y<= surface[1]*0.85+55):
        returnText=opFont.render("return",True,(255,0,0))
        mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.85))
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="menu"

## select mode ##
def selectMode():
    global currentScene,currentClick
    mainWindows.fill((0,0,0))
    menuImage=pygame.image.load("./image/menu.jpg").convert()
    mainWindows.blit(menuImage,[0,0])
    # pygame.draw.rect(mainWindows,(255,255,255),(surface[0]/2-surface[0]/3.5-surface[0]/6,surface[1]*0.3,surface[0]/3.5,surface[1]/10))
    # pygame.draw.rect(mainWindows,(255,255,255),(surface[0]/2+surface[0]/6,surface[1]*0.3,surface[0]/3,surface[1]/10))
    selectModeFont=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    returnText=selectModeFont.render("return",True,(0,0,0))
    mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.85))
    normalModeText=selectModeFont.render("normal",True,(0,0,0))
    mainWindows.blit(normalModeText,(surface[0]/2-surface[0]/3.5-surface[0]/8,surface[1]*0.3))
    challengeModeText=selectModeFont.render("challenge",True,(0,0,0))
    mainWindows.blit(challengeModeText,(surface[0]/2+surface[0]/6+surface[0]/30,surface[1]*0.3))

    ##print(surface[0]/2-surface[0]/3.5-surface[0]/8-5+normalModeText.get_width())

    if(x>=surface[0]*0.05 and x<=surface[0]*0.05+170 and y>= surface[1]*0.85-5 and y<= surface[1]*0.85+55):
        returnText=selectModeFont.render("return",True,(255,0,0))
        mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.85))
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="selectMode":
            currentScene = "menu"

    if(x>=surface[0]/2-surface[0]/3.5-surface[0]/8-5 
    and x<=surface[0]/2-surface[0]/3.5-surface[0]/8+int(normalModeText.get_width())+5 
    and y>=surface[1]*0.3-5 and y<= surface[1]*0.3+int(normalModeText.get_height())+5):
        normalModeText=selectModeFont.render("normal",True,(255,0,0))
        mainWindows.blit(normalModeText,(surface[0]/2-surface[0]/3.5-surface[0]/8,surface[1]*0.3))
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="normalMode"

    if(x>=surface[0]/2+surface[0]/6+surface[0]/30-5 
    and x<=surface[0]/2+surface[0]/6+surface[0]/30+int(challengeModeText.get_width())+5 
    and y>=surface[1]*0.3-5 and y<= surface[1]*0.3+int(challengeModeText.get_height())+5):
        challengeModeText=selectModeFont.render("challenge",True,(255,0,0))
        mainWindows.blit(challengeModeText,(surface[0]/2+surface[0]/6+surface[0]/30,surface[1]*0.3))
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="challengeMode"

# normal mode ##
def normalMode():
    global currentScene,flag,bossflag,height,attType,destination,distance,gflag
    mainWindows.fill((0,0,0))
    
    normalModeFont=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    returnText=normalModeFont.render("return",True,(255,255,255))
    mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.85))

    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]/8,surface[1]/6,surface[0]/6,surface[0]/6),border_radius=4)
    pygame.draw.rect(mainWindows,(0,0,0),(surface[0]/8+surface[0]/160,surface[1]/6+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4) 
    normalModeFont2=pygame.font.SysFont(None,int(surface[0]/5))
    oneText=normalModeFont2.render("1",True,(255,255,255))
    mainWindows.blit(oneText,(surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))

    if(x>=surface[0]*0.05 and x<=surface[0]*0.05+returnText.get_width() and y>= surface[1]*0.85 and y<= surface[1]*0.85+returnText.get_height()):
        returnText=normalModeFont.render("return",True,(255,0,0))
        mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.85))
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="selectMode"

    if(x>=surface[0]/8 and x<=surface[0]/8+surface[0]/6 and y>=surface[1]/6 and y<=surface[1]/6+surface[0]/6):
        pygame.draw.rect(mainWindows,(0,255,255),(surface[0]/8,surface[1]/6,surface[0]/6,surface[0]/6),border_radius=4)
        pygame.draw.rect(mainWindows,(0,0,0),(surface[0]/8+surface[0]/160,surface[1]/6+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4)
        oneText=normalModeFont2.render("1",True,(0,255,255))
        mainWindows.blit(oneText,(surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            flag=0
            bossflag=0
            height=surface[1]
            attType=0
            distance=[0,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            currentScene="level1"

def initlife(x):
    global bosslife,life,userposition,attTimeout,waittimeout
    attTimeout=0
    waittimeout=0
    if x==1:
        bosslife = 100
        life = 3
        userposition=[surface[0]/2-surface[0]/16,surface[1]*0.75,surface[0]/8,surface[1]*0.25]
        

def level1():
    global currentScene,bosslife,life,winflag,bossflag,flag,userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility,gflag
    if flag==0:
        initlife(1)
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        flag=1
    if bossflag ==0:
        attTimeout=int(time.time())+3
        attType=random.randint(1,2)
        height=surface[1]
        bossflag=1
    mainWindows.fill((90,0,173))
    for i in range (0,life):
        lifeImage=pygame.image.load("./image/Unknown-4.png")
        mainWindows.blit(lifeImage,[50*i,0])
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.2+(100-bosslife)*(surface[0]*0.3/100),surface[1]*0.05,bosslife*surface[0]*0.3/100,10))
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.5,surface[1]*0.05,bosslife*surface[0]*0.3/100,10))   
    gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    gameoverText=gameover.render("YOU DIED",True,(255,0,0))
    # Text1=level.render(str(bosslife),True,(255,255,255))
    # mainWindows.blit(Text1,(100,100))
    # Text2=level.render(str(life),True,(255,255,255))
    # mainWindows.blit(Text2,(300,100))
    if not gflag:
        pygame.draw.rect(mainWindows,(255,255,255),tuple(userposition))
    # print(height)
    
    if attTimeout!=int(time.time()) and (not(gflag)):
        
        # secWindows.set_alpha(64)
        secWindows = pygame.surface.Surface((surface[0]/2,surface[1]), SRCALPHA, 32)
        if attType==1:
            height-=surface[1]/180
            pygame.draw.rect(secWindows,(200,0,0,50),(0,0,surface[0]/2,surface[1]),border_radius=3)
            mainWindows.blit(secWindows,(0,height))
            
            pygame.draw.rect(mainWindows,(255,0,0),(0,0,surface[0]/2,surface[1]),width=1,border_radius=3)
            pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/4-surface[0]/160,surface[1]/2-surface[1]/18,surface[0]/80,surface[1]/12),border_radius=3)
            pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/4-surface[0]/160,surface[1]/2+surface[1]/20,surface[0]/80,surface[0]/80))
            pygame.draw.polygon(mainWindows,(255,0,0),
                ((surface[0]/4,(surface[1]/2-surface[1]/12)),
                ((surface[0]/4-(surface[1]*0.75/6)),(surface[1]/2+surface[1]/12)),
                ((surface[0]/4+(surface[1]*0.75/6)),(surface[1]/2+surface[1]/12))),width=5)
            
            
        elif attType==2:
            height-=surface[1]/180
            pygame.draw.rect(secWindows,(200,0,0,50),(0,0,surface[0]/2,surface[1]),border_radius=3)
            mainWindows.blit(secWindows,(surface[0]/2,height))

            pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/2,0,surface[0]/2,surface[1]),width=1,border_radius=3)
            pygame.draw.rect(mainWindows,(255,0,0),(surface[0]*3/4-surface[0]/160,surface[1]/2-surface[1]/18,surface[0]/80,surface[1]/12),border_radius=3)
            pygame.draw.rect(mainWindows,(255,0,0),(surface[0]*3/4-surface[0]/160,surface[1]/2+surface[1]/20,surface[0]/80,surface[0]/80))
            pygame.draw.polygon(mainWindows,(255,0,0),
                ((surface[0]*3/4,(surface[1]/2-surface[1]/12)),
                ((surface[0]*3/4-(surface[1]*0.75/6)),(surface[1]/2+surface[1]/12)),
                ((surface[0]*3/4+(surface[1]*0.75/6)),(surface[1]/2+surface[1]/12))),width=5)
            
    else:     
        if(attType==1):
            if userposition[0]<surface[0]/2 :
                life-=1
        elif(attType==2):
            if (userposition[0]+surface[0]/8)>surface[0]/2 :
                life-=1
        if life==0:
            gameovertimeout=int(time.time())+8
            visibility=0
            attType=0
            life-=1
            gflag=1
            # currentScene="normalMode"
            return
        elif life<=0:
            secWindows = pygame.surface.Surface((surface[0],surface[1]), SRCALPHA, 32)
            
            if gameovertimeout != int(time.time()):
                
                pygame.draw.rect(secWindows,(0,0,0,visibility),(0,0,surface[0],surface[1]))
                secWindows.blit(gameoverText,(surface[0]/2-gameoverText.get_width()/2,surface[1]/2-gameoverText.get_height()/2))
                mainWindows.blit(secWindows,(0,0))
                visibility+=1
                if visibility>=255:
                    visibility=255
            else:
                mainWindows.fill((0,0,0))
                currentScene="normalMode"
        if bosslife<0:
            secWindows = pygame.surface.Surface((surface[0],surface[1]), SRCALPHA, 32)
            if gameovertimeout!=int(time.time()):
                gameoverText=gameover.render("CONGRATULATION",True,(255,255,56))
                pygame.draw.rect(secWindows,(0,0,0,visibility),(0,0,surface[0],surface[1]))
                secWindows.blit(gameoverText,(surface[0]/2-gameoverText.get_width()/2,surface[1]/2-gameoverText.get_height()/2))
                mainWindows.blit(secWindows,(0,0))
                visibility+=1
                if visibility>=255:
                    visibility=255
            else:
                mainWindows.fill((0,0,0))
                winflag[0]=1
                flag=0
                currentScene="normalMode"
        attType=0
        waittimeout=int(time.time())+2

    if waittimeout == int(time.time()):
        waittimeout=0
        bossflag=0

    if round(time.time(),1) == round(timeout,1):
        # print("___________________")
        if(distance[1]==0):
            distance=[surface[0]/2-surface[0]/4,5]
        elif(distance[1]==1):
            distance=[0-surface[0]/2+surface[0]/4,5]
        destination[0]=surface[0]/2-surface[0]/16
    if(distance[1]!=5):
        userposition[0]+=distance[0]/30
    elif(distance[1]==5 ):
        userposition[0]+=distance[0]/10
        if(int(userposition[0])>=int(destination[0]) and distance[0]>0):
            userposition[0]=surface[0]/2-surface[0]/16
            return
        elif(int(userposition[0])<=int(destination[0]) and distance[0]<0):
            userposition[0]=surface[0]/2-surface[0]/16
            return
    
def stop():
    global currentScene
    mainWindows.fill((0,0,0))
    stopFont=pygame.font.SysFont(None,int(surface[0]/5))
    continueText=stopFont.render("Continue",True,(255,255,255))
    mainWindows.blit(continueText,(surface[0]/2-(continueText.get_width()/2),surface[1]/4-(continueText.get_height()/2)))

    if(x>=surface[0]/2-(continueText.get_width()/2) and x<=surface[0]/2+continueText.get_width() 
       and y>=surface[1]/4-(continueText.get_height()/2) and y<=surface[1]/4+continueText.get_height()):
        continueText=stopFont.render("Continue",True,(255,0,0))
        mainWindows.blit(continueText,(surface[0]-(continueText.get_width()/2),surface[1]/4-(continueText.get_height()/2)))
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="level1"
    

## use "currentScene" variaty to change the interface ##        
def createScene():
    if currentScene == "menu":
        Menu()
    if currentScene == "optional":
        optional()
    if currentScene == "selectMode":
        selectMode()
    if currentScene == "normalMode":
        normalMode()
    if currentScene == "level1":
        level1()
    if currentScene == "stop":
        stop()
## main ##
while True:
    clock.tick(60)
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
                # 取得滑鼠位置
                x, y = pygame.mouse.get_pos()
                currentClick[0]=x
                currentClick[1]=y
                currentClick[2]=currentScene
                print(x,y)
        
        if event.type == pygame.KEYDOWN and currentScene == "level1":
            if event.key ==pygame.K_z or event.key ==pygame.K_x:
                bosslife-=5
                
                    
            if event.key ==pygame.K_SPACE:
                life-=1
                if life<=0:
                    flag=0
                    currentScene="normalMode"
            if event.key == pygame.K_LEFT :
                destination[0]=surface[0]/4-surface[0]/16
                distance=[destination[0]-userposition[0],0]
                timeout=time.time()+0.5
            if event.key == pygame.K_RIGHT :
                destination[0]=3*surface[0]/4-surface[0]/16
                distance=[destination[0]-userposition[0],1]
                timeout=time.time()+0.5
            if event.key == pygame.K_q:

                currentScene="stop"
        
        if event.type == pygame.KEYDOWN and currentScene == "stop":
            if event.key == pygame.K_ESCAPE:
                currentScene="level1"
        if bosslife==0 and currentScene=="level1":
            gameovertimeout=int(time.time())+8
            visibility=0
            attType=0
            bosslife-=1
            gflag=1
                
            
    
    ## 隨時更新視窗大小 ##
    surface[0]=mainWindows.get_width()
    surface[1]=mainWindows.get_height()
    ## 隨時取得滑鼠位置 ##
    x, y = pygame.mouse.get_pos()
    createScene()

    pygame.display.update()