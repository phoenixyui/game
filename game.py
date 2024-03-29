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
level=["level1","level2","level3","level4"]
intro=["intro1","intro2","intro3","intro4","intro5","intro6"]
currentScene="menu"
currentClick=[0,0,"menu"]
pygame.init()
mainWindows=pygame.display.set_mode((surface[0],surface[1]),RESIZABLE,32)
mainWindows.fill(windows_colors)
bossposition=[0,0,0,0]
userposition=[surface[0]/2-surface[0]/16,surface[1]*0.75,surface[0]/8,surface[1]*0.25]
destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
distance=[0,5,5] ## 0 左 1 右 2 上 3 下 4 後
clock = pygame.time.Clock()
timeout=0
attTimeout=0
attTimeout2=0
attType=0
attack=0
height=0
height2=0
waittimeout=0
gameovertimeout=0
colortimeout=0
visibility=0
gflag=0
timepass=0
timepass2=0
recordtime=0
usercolor=(255,255,255)
bosscolor=(0,0,0)
useraction=0 
actiontimeout=0
leftPunch=pygame.image.load("image/punch_left-1.jpg")
rightPunch=pygame.image.load("image/punch_right-1.jpg")
multipleAttackZone=[0,surface[0]/5,2*surface[0]/5,3*surface[0]/5,4*surface[0]/5]
zone=0
selected=[]
action_start=0
action_end=0
defence=100
recover=0
defencing=0
introduce0=pygame.image.load("image/introduce0.png").convert()
introduce1=pygame.image.load("image/introduce1.png").convert()
introduce2=pygame.image.load("image/introduce2.png").convert()
introduce3=pygame.image.load("image/introduce3.png").convert()
introduce4=pygame.image.load("image/introduce4.png").convert()
introduce5=pygame.image.load("image/introduce5.png").convert()
introduce6=pygame.image.load("image/introduce6.png").convert()
stage0=pygame.image.load("image/stage0.png").convert()
stage1=pygame.image.load("image/stage1.png").convert()
stage2=pygame.image.load("image/stage2.png").convert()
stage3=pygame.image.load("image/stage3.png").convert()
stage4=pygame.image.load("image/stage4.png").convert()
stage5=pygame.image.load("image/stage5.png").convert()
mouseImage=pygame.image.load("./image/mouse.png").convert()
introbg=pygame.image.load("./image/intro_bg.png").convert()
level1bg=pygame.image.load("./image/level1bg.png").convert()

successtimes=0
jump_effect_time=0
thigh_effect_time=0
hit_flag=0

## menu interface ##
def Menu():
    global currentScene
    mainWindows.fill((0,0,0))
    ##pygame.draw.rect(mainWindows,(255,255,255),((surface[0]-300)/2,surface[1]-200,300,200))
    menuImage=pygame.image.load("./image/menu_punch.png").convert()
    mainWindows.blit(menuImage,[0,50])
    menuFont=pygame.font.SysFont(None,60)
    startText=menuFont.render("start",True,(255,255,255))
    mainWindows.blit(startText,(surface[0]*3/4-startText.get_width()/2,surface[1]/4-startText.get_height()))
    optionalText=menuFont.render("introduce",True,(255,255,255))
    mainWindows.blit(optionalText,(surface[0]*3/4-startText.get_width()/2,surface[1]*2/4-startText.get_height()))
    exitText=menuFont.render("exit",True,(255,255,255))
    mainWindows.blit(exitText,(surface[0]*3/4-startText.get_width()/2,surface[1]*3/4-startText.get_height()))
    mainWindows.blit(mouseImage,[x,y])


    if(x>=surface[0]/2 and y>=0 and y<=surface[1]/4):
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]*2/4+startText.get_width()/2,surface[1]/6,300,66),width=1,border_radius=3)
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="normalMode"

    elif(x>=surface[0]/2 and y>surface[1]/4 and y<=surface[1]*2/4):
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]*2/4+startText.get_width()/2,surface[1]/2-startText.get_height()*1.2,300,66),width=1,border_radius=3)
        if event.type == pygame.MOUSEBUTTONUP:
            
            currentScene="optional"

    elif(x>=surface[0]/2 and y>surface[1]*2/4 and y<=surface[1]*3/4):
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]*2/4+startText.get_width()/2,surface[1]*3/4-startText.get_height()*1.2,300,66),width=1,border_radius=3)
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.quit()
            sys.exit()

## optional interface ##
def optional():
    global currentScene,successtimes,flag
    mainWindows.blit(introduce0,[0,0])
    opFont=pygame.font.SysFont(None,80)
    returnText=opFont.render("return",True,(255,255,255))
    

    if(y<surface[1]/2):
        if(x<surface[0]/3):
            mainWindows.blit(introduce1,[0,0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag=0
                successtimes=0
                currentScene="intro1"
        if(x>=surface[0]/3 and x<surface[0]*2/3):
            mainWindows.blit(introduce2,[0,0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                successtimes=0
                flag=0
                currentScene="intro2"
        if(x>=surface[0]*2/3):
            mainWindows.blit(introduce3,[0,0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                successtimes=0
                flag=0
                currentScene="intro3"
    if(y>surface[1]/2 and y<surface[1]*0.9):
        if(x<surface[0]/3):
            mainWindows.blit(introduce4,[0,0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                successtimes=0
                flag=0
                currentScene="intro4"
        if(x>=surface[0]/3 and x<surface[0]*2/3):
            mainWindows.blit(introduce5,[0,0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                successtimes=0
                flag=0
                currentScene="intro5"
        if(x>=surface[0]*2/3):
            mainWindows.blit(introduce6,[0,0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                successtimes=0
                flag=0
                currentScene="intro6"
    mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.9))
    mainWindows.blit(mouseImage,[x,y])
    if(x>=surface[0]*0.05 and x<=surface[0]*0.05+returnText.get_width() and y>= surface[1]*0.9-5 and y<= surface[1]*0.9+returnText.get_height()):
        returnText=opFont.render("return",True,(255,0,0))
        mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.9))
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="menu"
      
# normal mode ##
def normalMode():
    global currentScene,flag,bossflag,height,attType,destination,distance,gflag,height2
    mainWindows.blit(stage0,[0,0])

    if(x>=surface[0]*3/8 and x<=surface[0]*5/8 and y>=surface[1]*2/6 and y<=surface[1]*4/6):
        mainWindows.blit(stage5,[0,0])
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="menu"
    if(x<surface[0]*3/8 and y<=surface[1]/2):
        mainWindows.blit(stage1,[0,0])
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            flag=0
            bossflag=0
            height=surface[1]
            attType=0
            distance=[0,5,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            windowssize(2)
            currentScene="level1"
    if(x>surface[0]*5/8 and y<surface[1]/2):
        mainWindows.blit(stage2,[0,0])
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            flag=0
            bossflag=0
            height=surface[1]
            attType=0
            distance=[0,5,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            currentScene="level2"
    if(x<surface[0]*3/8 and y>surface[1]/2):
        mainWindows.blit(stage3,[0,0])
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            flag=0
            bossflag=0
            height=surface[1]
            attType=0
            distance=[0,5,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            currentScene="level3"
    if(x>surface[0]*5/8 and y>surface[1]/2):
        mainWindows.blit(stage4,[0,0])
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            flag=0
            bossflag=0
            height=surface[1]
            attType=0
            distance=[0,5,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            currentScene="level4"
    mainWindows.blit(mouseImage,[x,y])
        
def initlife(x):
    global bosslife,life,userposition,attTimeout,waittimeout
    attTimeout=0
    waittimeout=0
    life = 3
    userposition=[surface[0]/2-surface[0]/16,surface[1]*0.75,surface[0]/8,surface[1]*0.25]
    ###
    # 上面的userposition可以刪掉或改成使用者目前位置
    ###
    if x==1:
        bosslife = 100 
    elif x==2:
        bosslife = 150
    elif x==3:
        bosslife = 150
    elif x==4:
        bosslife = 150
        
def usermove():
    global currentScene,bosslife,life,winflag,bossflag,flag,userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility,gflag,timepass,recordtime
    if round(time.time(),1) == round(timeout,1):#這邊以下都是角色移動
        if(distance[1]==0):
            distance=[surface[0]/2-surface[0]/4,5,0]
        elif(distance[1]==1):
            distance=[0-surface[0]/2+surface[0]/4,5,1]
        elif(distance[1]==2):
            distance=[surface[1]*0.15,5,2]
        destination[0]=surface[0]/2-surface[0]/16
        destination[1]=surface[1]*0.75
    
    if(distance[1]!=5):
        if(distance[1]==0 or distance[1]==1):
            userposition[0]+=distance[0]/30
        if(distance[1]==2 or distance[1]==3):
            userposition[1]+=distance[0]/30
    elif(distance[1]==5 ):
        if(distance[2]==0 or distance[2]==1):
            userposition[0]+=distance[0]/10
        elif(distance[2]==2 or distance[2]==3):
            userposition[1]+=distance[0]/10
        
        if(int(userposition[0])>=int(destination[0]) and distance[0]>0):
            userposition[0]=surface[0]/2-surface[0]/16
            
        if(int(userposition[0])<=int(destination[0]) and distance[0]<0):
            userposition[0]=surface[0]/2-surface[0]/16
            
        if(int(userposition[1])>=int(destination[1]) and distance[0]>0):
            userposition[1]=0.75*surface[1]

def drawAttType(x):
    global currentScene,bosslife,life,winflag,bossflag,flag,userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility
    global gflag,timepass,recordtime,selected,zone,multipleAttackZone,attTimeout2,timepass2,height2,multipleAttackZone,surface
    secWindows = pygame.surface.Surface((surface[0],surface[1]), SRCALPHA, 32)
    multipleAttackZone=[0,surface[0]/5,2*surface[0]/5,3*surface[0]/5,4*surface[0]/5]
    if x==1:
        height=surface[1]*(1-timepass/(attTimeout-recordtime))
        pygame.draw.rect(secWindows,(200,0,0,50),(0,0,surface[0]/2,surface[1]),border_radius=3)
        mainWindows.blit(secWindows,(0,height))
            
        pygame.draw.rect(mainWindows,(255,0,0),(0,0,surface[0]/2,surface[1]),width=1,border_radius=3)
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/4-surface[0]/160,surface[1]/2-surface[1]/18,surface[0]/80,surface[1]/12),border_radius=3)
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/4-surface[0]/160,surface[1]/2+surface[1]/20,surface[0]/80,surface[0]/80))
        pygame.draw.polygon(mainWindows,(255,0,0),
            ((surface[0]/4,(surface[1]/2-surface[1]/12)),
            ((surface[0]/4-(surface[1]*0.75/6)),(surface[1]/2+surface[1]/12)),
            ((surface[0]/4+(surface[1]*0.75/6)),(surface[1]/2+surface[1]/12))),width=5)
    elif x==2:
        height=surface[1]*(1-timepass/(attTimeout-recordtime))
        pygame.draw.rect(secWindows,(200,0,0,50),(0,0,surface[0]/2,surface[1]),border_radius=3)
        mainWindows.blit(secWindows,(surface[0]/2,height))

        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/2,0,surface[0]/2,surface[1]),width=1,border_radius=3)
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]*3/4-surface[0]/160,surface[1]/2-surface[1]/18,surface[0]/80,surface[1]/12),border_radius=3)
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]*3/4-surface[0]/160,surface[1]/2+surface[1]/20,surface[0]/80,surface[0]/80))
        pygame.draw.polygon(mainWindows,(255,0,0),
            ((surface[0]*3/4,(surface[1]/2-surface[1]/12)),
            ((surface[0]*3/4-(surface[1]*0.75/6)),(surface[1]/2+surface[1]/12)),
            ((surface[0]*3/4+(surface[1]*0.75/6)),(surface[1]/2+surface[1]/12))),width=5)
    elif x==3:
        height=surface[1]*0.35*(timepass/(attTimeout-recordtime))
        pygame.draw.rect(secWindows,(200,0,0,50),(0,0.65*surface[1],surface[0],height),border_radius=3)
        mainWindows.blit(secWindows,(0,0))

        pygame.draw.rect(mainWindows,(255,0,0),(0,surface[1]*0.65,surface[0],surface[1]*0.35),width=1,border_radius=3)
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/2-surface[0]/160,surface[1]*0.85-surface[1]/18,surface[0]/80,surface[1]/12),border_radius=3)
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/2-surface[0]/160,surface[1]*0.85+surface[1]/20,surface[0]/80,surface[0]/80))
        pygame.draw.polygon(mainWindows,(255,0,0),
            ((surface[0]/2,(surface[1]*0.85-surface[1]/12)),
            ((surface[0]/2-(surface[1]*0.75/6)),(surface[1]*0.85+surface[1]/12)),
            ((surface[0]/2+(surface[1]*0.75/6)),(surface[1]*0.85+surface[1]/12))),width=5)
    elif x==4:
        height=surface[1]*0.85*(timepass/(attTimeout-recordtime))
        pygame.draw.rect(secWindows,(200,0,0,50),(0,0,surface[0],height),border_radius=3)
        mainWindows.blit(secWindows,(0,0))

        pygame.draw.rect(mainWindows,(255,0,0),(0,0,surface[0],surface[1]*0.816),width=1,border_radius=3)
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/2-surface[0]/160,surface[1]*0.408-surface[1]/18,surface[0]/80,surface[1]/12),border_radius=3)
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]/2-surface[0]/160,surface[1]*0.408+surface[1]/20,surface[0]/80,surface[0]/80))
        pygame.draw.polygon(mainWindows,(255,0,0),
            ((surface[0]/2,(surface[1]*0.408-surface[1]/12)),
            ((surface[0]/2-(surface[1]*0.75/6)),(surface[1]*0.408+surface[1]/12)),
            ((surface[0]/2+(surface[1]*0.75/6)),(surface[1]*0.408+surface[1]/12))),width=5)
    elif x==5:
        height=surface[1]*(1-timepass/(attTimeout-recordtime))
        pygame.draw.rect(secWindows,(200,0,0,50),(0,0,surface[0]/5,surface[1]),border_radius=3)
        if zone==5:
            for i in range(0,zone-1):
                mainWindows.blit(secWindows,(multipleAttackZone[selected[i]],height))
                pygame.draw.rect(mainWindows,(255,0,0),(multipleAttackZone[selected[i]],0,surface[0]/5,surface[1]),width=1,border_radius=3)
        else:
            for i in range(0,zone):
                mainWindows.blit(secWindows,(multipleAttackZone[selected[i]],height))
                pygame.draw.rect(mainWindows,(255,0,0),(multipleAttackZone[selected[i]],0,surface[0]/5,surface[1]),width=1,border_radius=3)
        
        
def drawAttType2():
    global currentScene,bosslife,life,winflag,bossflag,flag,userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility
    global gflag,timepass,recordtime,selected,zone,multipleAttackZone,attTimeout2,timepass2,height2,multipleAttackZone,surface
    secWindows = pygame.surface.Surface((surface[0],surface[1]), SRCALPHA, 32)  
    multipleAttackZone=[0,surface[0]/5,2*surface[0]/5,3*surface[0]/5,4*surface[0]/5]
    height2=surface[1]*(1-timepass2/(attTimeout2-recordtime))      
    pygame.draw.rect(secWindows,(200,0,0,50),(0,0,surface[0]/5,surface[1]),border_radius=3)
    mainWindows.blit(secWindows,(multipleAttackZone[selected[zone-1]],height2))
    pygame.draw.rect(mainWindows,(255,0,0),(multipleAttackZone[selected[zone-1]],0,surface[0]/5,surface[1]),width=1,border_radius=3)

def drawUser(x):
    global usercolor,bosscolor,attack

    #boss
         #頭
    pygame.draw.circle(mainWindows,bosscolor,(surface[0]/2+userposition[2]/2-surface[0]/16,surface[1]*0.4+userposition[2]/3),userposition[2]/3)
        #身體
    pygame.draw.line(mainWindows,bosscolor,(surface[0]/2+userposition[2]/2-surface[0]/16,surface[1]*0.4+2*userposition[2]/3),(surface[0]/2+userposition[2]/2-surface[0]/16,surface[1]*0.4+4*userposition[2]/3),3)
        #左腳
    pygame.draw.line(mainWindows,bosscolor,(surface[0]/2-surface[0]/16+userposition[2]/2,surface[1]*0.4+4*userposition[2]/3),(surface[0]/2-surface[0]/16+userposition[2]/4,surface[1]*0.4+5.5*userposition[2]/3),3)
        #右腳
    pygame.draw.line(mainWindows,bosscolor,(surface[0]/2+userposition[2]/2-surface[0]/16,surface[1]*0.4+4*userposition[2]/3),(surface[0]/2-surface[0]/16+userposition[2]*3/4,surface[1]*0.4+5.5*userposition[2]/3),3)
        #左手
    pygame.draw.line(mainWindows,bosscolor,(surface[0]/2+userposition[2]/2-surface[0]/16,surface[1]*0.4+userposition[2]),(surface[0]/2-surface[0]/16+userposition[2]/7,surface[1]*0.4+userposition[2]*0.95),3)
    pygame.draw.line(mainWindows,bosscolor,(surface[0]/2+userposition[2]/7-surface[0]/16,surface[1]*0.4+userposition[2]*0.95),(surface[0]/2-surface[0]/16+userposition[2]/4,surface[1]*0.4+userposition[2]*0.75),3)

        #右手
    pygame.draw.line(mainWindows,bosscolor,(surface[0]/2-surface[0]/16+userposition[2]/2,surface[1]*0.4+userposition[2]),(surface[0]/2-surface[0]/16+userposition[2]*5/6,surface[1]*0.4+userposition[2]*0.85),3)
    pygame.draw.line(mainWindows,bosscolor,(surface[0]/2-surface[0]/16+userposition[2]*5/6,surface[1]*0.4+userposition[2]*0.85),(surface[0]/2-surface[0]/16+userposition[2]*3/4,surface[1]*0.4+userposition[2]*0.65),3)

    if(x==0):
            #user
            #頭
        pygame.draw.circle(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+userposition[2]/3),userposition[2]/3)
            #身體
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+2*userposition[2]/3),(userposition[0]+userposition[2]/2,userposition[1]+4*userposition[2]/3),3)
            #左腳
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+4*userposition[2]/3),(userposition[0]+userposition[2]/4,userposition[1]+5.5*userposition[2]/3),3)
            #右腳
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+4*userposition[2]/3),(userposition[0]+userposition[2]*3/4,userposition[1]+5.5*userposition[2]/3),3)
            #左手
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+userposition[2]),(userposition[0]+userposition[2]/7,userposition[1]+userposition[2]*0.95),3)
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/7,userposition[1]+userposition[2]*0.95),(userposition[0]+userposition[2]/4,userposition[1]+userposition[2]*0.75),3)
        
            #右手
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+userposition[2]),(userposition[0]+userposition[2]*5/6,userposition[1]+userposition[2]*0.85),3)
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]*5/6,userposition[1]+userposition[2]*0.85),(userposition[0]+userposition[2]*3/4,userposition[1]+userposition[2]*0.65),3)
    elif(x==1):
        pygame.draw.circle(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+userposition[2]/3),userposition[2]/3)
            #身體
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+2*userposition[2]/3),(userposition[0]+userposition[2]/2,userposition[1]+4*userposition[2]/3),3)
                #左腳
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+4*userposition[2]/3),(userposition[0]+userposition[2]/4,userposition[1]+5.5*userposition[2]/3),3)
                #右腳
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+4*userposition[2]/3),(userposition[0]+userposition[2]*3/4,userposition[1]+5.5*userposition[2]/3),3)
                #左手
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+userposition[2]),(userposition[0]+userposition[2]*2/5,userposition[1]+userposition[2]*1.1),3)
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]*2/5,userposition[1]+userposition[2]*1.1),(userposition[0]+userposition[2]*2.15/5,userposition[1]+userposition[2]*0.85),3)           
                #右手
        pygame.draw.line(mainWindows,usercolor,(userposition[0]+userposition[2]/2,userposition[1]+userposition[2]),(userposition[0]+userposition[2]*3/4,userposition[1]+userposition[2]*0.6),3)  
        mainWindows.blit(rightPunch,[surface[0]/2+(userposition[0]+userposition[2]/2-surface[0]/3)-rightPunch.get_width(),surface[1]/2]) 
    elif(x==2):
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
        mainWindows.blit(leftPunch,[surface[0]/3,surface[1]/2]) 

def defencefunc():
    global usercolor,defence,life,successtimes
    if(defencing==0) and currentScene in level:
        life-=1
        usercolor=(255,0,0)   
    elif defencing==1 and currentScene in intro:
        successtimes+=1
    elif defencing==1:
        defence=-1

def level1():
    global currentScene,bosslife,bossposition,life,winflag,bossflag,flag,userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility,gflag,timepass,recordtime,usercolor,bosscolor,colortimeout,useraction,actiontimeout
    if flag==0:
        initlife(1)
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        flag=1
        bossposition=userposition
        ##以上是進遊戲後只會做一次的初始化##
    if bossflag ==0:
        attTimeout=int(time.time())+3
        recordtime=int(time.time())
        attType=random.randint(1,2)
        height=surface[1]
        bossflag=1
        timepass=0
        ##以上是每次boss攻擊前需更動的值##
    mainWindows.blit(level1bg,[0,0])
    for i in range (0,life):
        lifeImage=pygame.image.load("./image/Unknown-4.png")
        mainWindows.blit(lifeImage,[50*i,0])
        ##顯示左上角愛心##
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.2+(100-bosslife)*(surface[0]*0.3/100),surface[1]*0.05,bosslife*surface[0]*0.3/100,10))
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.5,surface[1]*0.05,bosslife*surface[0]*0.3/100,10))   
    gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    gameoverText=gameover.render("YOU DIED",True,(255,0,0))

    if not gflag:
        drawUser(useraction)
    
    if attTimeout!=int(time.time()) and (not(gflag)):  #boss攻擊時間未結束 and 遊戲未結束
        
        timepass=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
        drawAttType(attType)
            
    else:     
        if(attType==1):
            if userposition[0]<surface[0]/2 :
                life-=1
                usercolor=(255,0,0)
                colortimeout=int(time.time())+0.5
        elif(attType==2):
            if (userposition[0]+surface[0]/8)>surface[0]/2 :
                life-=1
                usercolor=(255,0,0)
                colortimeout=int(time.time())+0.5
        #以上是當角色在攻擊範圍內且倒數結束時的動作
        if life==0:
            gameovertimeout=int(time.time())+8
            visibility=0
            attType=0
            life-=1
            gflag=1
            # currentScene="normalMode"
            return
            #以上是做死亡動畫的參數初始化
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
        #以上為死亡動畫    
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
                windowssize(1)
                currentScene="normalMode"
        #以上為勝利動畫
        attType=0
        waittimeout=int(time.time())+2 #攻擊間隔
        timepass=0
        
    if actiontimeout <= int(time.time()):    
        useraction=0

    if waittimeout == int(time.time()):
        waittimeout=0
        bossflag=0
    #print(userposition[1],destination[1],distance)
    usermove()
                
def stop():#我還沒做完（或不想做）
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
    
def level2():
    global currentScene,bosslife,bossposition,life,winflag,bossflag,flag
    global userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility
    global gflag,timepass,recordtime,usercolor,bosscolor,colortimeout,useraction,actiontimeout

    if flag==0:
        initlife(2)
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        flag=1
        bossposition=userposition
        ##以上是進遊戲後只會做一次的初始化##
    if bossflag ==0:
        attType=random.randint(1,4)
        if attType==3 or attType==4:
            attTimeout=int(time.time())+1.5
        else:
            attTimeout=int(time.time())+3
        
        recordtime=int(time.time())
        height=surface[1]
        bossflag=1
        timepass=0
        usercolor=(255,255,255)
        ##以上是每次boss攻擊前需更動的值##
    mainWindows.fill((90,0,173))
    for i in range (0,life):
        lifeImage=pygame.image.load("./image/Unknown-4.png")
        mainWindows.blit(lifeImage,[50*i,0])
        ##顯示左上角愛心##
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.2+(100-bosslife)*(surface[0]*0.3/100),surface[1]*0.05,bosslife*surface[0]*0.3/100,10))
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.5,surface[1]*0.05,bosslife*surface[0]*0.3/100,10))   
    gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    gameoverText=gameover.render("YOU DIED",True,(255,0,0))

    if not gflag:
        drawUser(useraction)
    #print(userposition)
    if attTimeout!=round(time.time(),1) and (not(gflag)):  #boss攻擊時間未結束 and 遊戲未結束
        
        timepass=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
        drawAttType(attType)
            
    else:     
        if(attType==1):
            if userposition[0]<surface[0]/2 :
                life-=1
                usercolor=(255,0,0)
                # colortimeout=int(time.time())+0.5
        if(attType==2):
            if (userposition[0]+surface[0]/8)>surface[0]/2 :
                life-=1
                usercolor=(255,0,0)
                # colortimeout=int(time.time())+0.5
        if(attType==3):
            if(userposition[1]+5.5*userposition[2]/3)>surface[1]:
                life-=1
                usercolor=(255,0,0)
                # colortimeout=int(time.time())+0.5
        if(attType==4):
            if(userposition[1])<surface[1]*0.816:
                life-=1
                usercolor=(255,0,0)
                # colortimeout=int(time.time())+0.5
        #print(usercolor)
        #以上是當角色在攻擊範圍內且倒數結束時的動作
        if life==0:
            gameovertimeout=int(time.time())+8
            visibility=0
            attType=0
            life-=1
            gflag=1
            # currentScene="normalMode"
            return
            #以上是做死亡動畫的參數初始化
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
        #以上為死亡動畫    
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
        #以上為勝利動畫
        attType=0
        waittimeout=int(time.time())+2 #攻擊間隔
        timepass=0
    
        
    if actiontimeout == int(time.time()):    
        useraction=0

    if waittimeout == int(time.time()):
        waittimeout=0
        bossflag=0
    #print(userposition[1],destination[1],distance)
    usermove()

def level3():
    global currentScene,bosslife,bossposition,life,winflag,bossflag,flag
    global userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility
    global gflag,timepass,recordtime,usercolor,bosscolor,colortimeout,useraction,actiontimeout,multipleAttackZone,zone,selected,attTimeout2,timepass2

    if flag==0:
        initlife(2)
        attTimeout=int(time.time())+2
        attTimeout2=0
        bossflag=1
        attType=0
        flag=1
        bossposition=userposition
        ##以上是進遊戲後只會做一次的初始化##
    if bossflag ==0:
        attType=random.randint(1,4)
        attType=1
        if attType==3 or attType==4:
            attTimeout=int(time.time())+1.5
        elif attType == 1 or attType == 2:
            attType=5
            attTimeout=int(time.time())+3
            zone=random.randint(1,5)
            selected=random.sample(range(0,5),zone)
            if zone==5:
                attTimeout2=int(time.time())+4
        else:
            attTimeout=int(time.time())+3
        
        recordtime=int(time.time())
        height=surface[1]
        bossflag=1
        timepass=0
        timepass2=0
        usercolor=(255,255,255)
        ##以上是每次boss攻擊前需更動的值##
    mainWindows.fill((90,0,173))
    for i in range (0,life):
        lifeImage=pygame.image.load("./image/Unknown-4.png")
        mainWindows.blit(lifeImage,[50*i,0])
        ##顯示左上角愛心##
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.2+(100-bosslife)*(surface[0]*0.3/100),surface[1]*0.05,bosslife*surface[0]*0.3/100,10))
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.5,surface[1]*0.05,bosslife*surface[0]*0.3/100,10))   
    gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    gameoverText=gameover.render("YOU DIED",True,(255,0,0))

    if not gflag:
        drawUser(useraction)
    #print(userposition)
    if attTimeout2!=int(time.time()) and (not(gflag)) and zone==5:
        timepass2=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass2>attTimeout2-recordtime):timepass2=attTimeout2-recordtime #如果大於timeout就設成timeout
        if(attTimeout2!=0):drawAttType2()
    elif (not(gflag)) and zone==5:
        if (selected[4]==0):
            if userposition[0]<surface[0]/5:
                life-=1
                usercolor=(255,0,0) 
        elif (selected[4]==1):
            if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                life-=1
                usercolor=(255,0,0) 
        elif (selected[4]==2):
            if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                life-=1
                usercolor=(255,0,0) 
        elif (selected[4]==3):
            if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                life-=1
                usercolor=(255,0,0) 
        elif (selected[4]==4):
            if userposition[0]+surface[0]/8>surface[0]*4/5:
                life-=1
                usercolor=(255,0,0) 
        zone=0
        if life==0:
            gameovertimeout=int(time.time())+8
            visibility=0
            attType=0
            life-=1
            gflag=1
            # currentScene="normalMode"
            return
            #以上是做死亡動畫的參數初始化
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
        #以上為死亡動畫    
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
        #以上為勝利動畫
        attType=0
        waittimeout=int(time.time())+1 #攻擊間隔
        timepass=0
        timepass2=0

    if attTimeout!=round(time.time(),1) and (not(gflag)):  #boss攻擊時間未結束 and 遊戲未結束
        timepass=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
        drawAttType(attType)
    else:     
        if(attType==1):
            if userposition[0]<surface[0]/2 :
                life-=1
                usercolor=(255,0,0)      
        if(attType==2):
            if (userposition[0]+surface[0]/8)>surface[0]/2 :
                life-=1
                usercolor=(255,0,0)    
        if(attType==3):
            if(userposition[1]+5.5*userposition[2]/3)>surface[1]:
                life-=1
                usercolor=(255,0,0)  
        if(attType==4):
            if(userposition[1])<surface[1]*0.816:
                life-=1
                usercolor=(255,0,0) 
        if(attType==5):
            if zone!=5:
                if (0 in selected):
                    if userposition[0]<surface[0]/5:
                        life-=1
                        usercolor=(255,0,0) 
                if (1 in selected):
                    if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                        life-=1
                        usercolor=(255,0,0) 
                if (2 in selected):
                    if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                        life-=1
                        usercolor=(255,0,0) 
                if (3 in selected):
                    if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                        life-=1
                        usercolor=(255,0,0) 
                if (4 in selected):
                    if userposition[0]+surface[0]/8>surface[0]*4/5:
                        life-=1
                        usercolor=(255,0,0) 
            else:
                if(selected[4]==0):
                    if userposition[0]+surface[0]/8>surface[0]/5:
                        life-=1
                        usercolor=(255,0,0)
                if(selected[4]==1):
                    if not( (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5)):
                        life-=1
                        usercolor=(255,0,0) 
                if(selected[4]==2):
                    if not((userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5)):
                        life-=1
                        usercolor=(255,0,0)
                if(selected[4]==3):
                    if not((userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5)):
                        life-=1
                        usercolor=(255,0,0)
                if(selected[4]==4):
                    if userposition[0]<surface[0]*4/5:
                        life-=1
                        usercolor=(255,0,0)


        #以上是當角色在攻擊範圍內且倒數結束時的動作
        if life==0:
            gameovertimeout=int(time.time())+8
            visibility=0
            attType=0
            life-=1
            gflag=1
            # currentScene="normalMode"
            return
            #以上是做死亡動畫的參數初始化
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
        #以上為死亡動畫    
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
        #以上為勝利動畫
        attType=0
        waittimeout=int(time.time())+2 #攻擊間隔
        timepass=0
        timepass2=0
    
        
    if actiontimeout == int(time.time()):    
        useraction=0

    if waittimeout == int(time.time()):
        zone=0
        selected=[]
        waittimeout=0
        bossflag=0
    usermove()

def level4():
    global currentScene,bosslife,bossposition,life,winflag,bossflag,flag
    global userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility
    global gflag,timepass,recordtime,usercolor,bosscolor,colortimeout,useraction,actiontimeout,multipleAttackZone,zone,selected,attTimeout2,timepass2
    global action_start,action_end,defence,recover,defencing

    if flag==0:
        initlife(2)
        attTimeout=int(time.time())+2
        attTimeout2=0
        bossflag=1
        attType=0
        flag=1
        bossposition=userposition
        ##以上是進遊戲後只會做一次的初始化##
    if bossflag ==0:
        attType=random.randint(1,4)
        if attType==3 or attType==4:
            attTimeout=int(time.time())+1.5
        elif attType == 1 or attType == 2:
            attType=5
            attTimeout=int(time.time())+3
            zone=random.randint(1,5)
            zone=5
            selected=random.sample(range(0,5),zone)
            if zone==5:
                attTimeout2=int(time.time())+4
        else:
            attTimeout=int(time.time())+3
        
        recordtime=int(time.time())
        height=surface[1]
        bossflag=1
        timepass=0
        timepass2=0
        usercolor=(255,255,255)
        ##以上是每次boss攻擊前需更動的值##
    mainWindows.fill((90,0,173))
    for i in range (0,life):
        lifeImage=pygame.image.load("./image/Unknown-4.png")
        mainWindows.blit(lifeImage,[50*i,0])
        ##顯示左上角愛心##
    pygame.draw.rect(mainWindows,(255,255,255),(10,+((100-defence)*surface[0]*0.3/100)+surface[1]*0.1,20,defence*surface[0]*0.3/100))
    
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.2+(100-bosslife)*(surface[0]*0.3/100),surface[1]*0.05,bosslife*surface[0]*0.3/100,10))
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.5,surface[1]*0.05,bosslife*surface[0]*0.3/100,10))   
    gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    gameoverText=gameover.render("YOU DIED",True,(255,0,0))

    if action_start==1 and action_end==0 and(recover==0 or recover==2) :
        defence -=2
        defencing=1
        recover=0
    if defence <=0:
        recover=1
        defencing=0
    if recover==1 or recover==2:
        defence+=1
    if defence>=100 and recover==1:
        recover=0
        action_start=0
    if action_start==1 and action_end==1:
        recover=2
        defencing=0
        action_start=action_end=0   
    if defence >=100:defence=100
    print(defence,action_start,action_end,recover,defencing)
    

    if not gflag:
        drawUser(useraction)
    #print(userposition)
    if attTimeout2!=int(time.time()) and (not(gflag)) and zone==5:
        timepass2=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass2>attTimeout2-recordtime):timepass2=attTimeout2-recordtime #如果大於timeout就設成timeout
        if(attTimeout2!=0):drawAttType2()
    elif (not(gflag)) and zone==5:
        if (selected[4]==0):
            if userposition[0]<surface[0]/5:
                life-=1
                usercolor=(255,0,0) 
        elif (selected[4]==1):
            if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                life-=1
                usercolor=(255,0,0) 
        elif (selected[4]==2):
            if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                life-=1
                usercolor=(255,0,0) 
        elif (selected[4]==3):
            if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                life-=1
                usercolor=(255,0,0) 
        elif (selected[4]==4):
            if userposition[0]+surface[0]/8>surface[0]*4/5:
                life-=1
                usercolor=(255,0,0) 
        zone=0
        if life==0:
            gameovertimeout=int(time.time())+8
            visibility=0
            attType=0
            life-=1
            gflag=1
            # currentScene="normalMode"
            return
            #以上是做死亡動畫的參數初始化
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
        #以上為死亡動畫    
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
        #以上為勝利動畫
        attType=0
        waittimeout=int(time.time())+1 #攻擊間隔
        timepass=0
        timepass2=0

    if attTimeout!=round(time.time(),1) and (not(gflag)):  #boss攻擊時間未結束 and 遊戲未結束
        timepass=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
        drawAttType(attType)
    else:     
        if(attType==1):
            if userposition[0]<surface[0]/2 :
                defencefunc()
        if(attType==2):
            if (userposition[0]+surface[0]/8)>surface[0]/2 :
                defencefunc()    
        if(attType==3):
            if(userposition[1]+5.5*userposition[2]/3)>surface[1]:
                defencefunc() 
        if(attType==4):
            if(userposition[1])<surface[1]*0.816:
                defencefunc()
        if(attType==5):
            if zone!=5:
                if (0 in selected):
                    if userposition[0]<surface[0]/5:
                        defencefunc()
                if (1 in selected):
                    if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                        defencefunc()
                if (2 in selected):
                    if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                        defencefunc()
                if (3 in selected):
                    if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                        defencefunc()
                if (4 in selected):
                    if userposition[0]+surface[0]/8>surface[0]*4/5:
                        defencefunc()
            else:
                if(selected[4]==0):
                    if userposition[0]+surface[0]/8>surface[0]/5:
                        defencefunc()
                if(selected[4]==1):
                    if not( (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5)):
                        defencefunc()
                if(selected[4]==2):
                    if not((userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5)):
                        defencefunc()
                if(selected[4]==3):
                    if not((userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5)):
                        defencefunc()
                if(selected[4]==4):
                    if userposition[0]<surface[0]*4/5:
                        defencefunc()


        #以上是當角色在攻擊範圍內且倒數結束時的動作
        if life==0:
            gameovertimeout=int(time.time())+8
            visibility=0
            attType=0
            life-=1
            gflag=1
            # currentScene="normalMode"
            return
            #以上是做死亡動畫的參數初始化
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
        #以上為死亡動畫    
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
        #以上為勝利動畫
        attType=0
        waittimeout=int(time.time())+2 #攻擊間隔
        timepass=0
        timepass2=0
    
        
    if actiontimeout == int(time.time()):    
        useraction=0

    if waittimeout == int(time.time()):
        zone=0
        selected=[]
        waittimeout=0
        bossflag=0
    usermove()

def intro1():
    global successtimes,currentScene,visibility,flag
    if flag==0:
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]/2-startText.get_width()/2 and x<=surface[0]/2+startText.get_width()/2
           and y>=surface[1]*0.8-startText.get_height()/2 and y<=surface[1]*0.8+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
            if event.type == pygame.MOUSEBUTTONUP:
                flag=1
    if flag!=0:        
        mainWindows.blit(introbg,[0,0])
        gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        for i in range (0,3):
            image=pygame.image.load("./image/notsuccess.png")
            mainWindows.blit(image,[400+i*150,100])
        a=successtimes
        if a>3:a=3
        for j in range(0,a):
            image2=pygame.image.load("./image/success.png")
            mainWindows.blit(image2,[400+j*150,100])
        if successtimes<3:
            drawUser(useraction)
        elif successtimes>=4:
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
                currentScene="optional"

def intro2():
    global successtimes,currentScene,visibility,attTimeout,bossflag,attType,recordtime,height,timepass,usercolor,colortimeout,flag,useraction,waittimeout
    if flag==0:
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]/2-startText.get_width()/2 and x<=surface[0]/2+startText.get_width()/2
           and y>=surface[1]*0.8-startText.get_height()/2 and y<=surface[1]*0.8+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
            if event.type == pygame.MOUSEBUTTONUP:
                flag=1
    if flag!=0:
        mainWindows.blit(introbg,[0,0])
        gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        if bossflag ==0:
            attType=random.randint(1,2)
            attTimeout=int(time.time())+3
            recordtime=int(time.time())
            height=surface[1]
            bossflag=1
            timepass=0
            usercolor=(255,255,255)
        for i in range (0,3):
            image=pygame.image.load("./image/notsuccess.png")
            mainWindows.blit(image,[400+i*150,100])
        a=successtimes
        if a>3:a=3
        for j in range(0,a):
            image2=pygame.image.load("./image/success.png")
            mainWindows.blit(image2,[400+j*150,100])
        if successtimes<3:
            drawUser(useraction)
        elif successtimes>=4:
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
                currentScene="optional"
        if attTimeout!=int(time.time()) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            
            timepass=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
            drawAttType(attType)
                
        else:     
            if(attType==1):
                if userposition[0]<surface[0]/2 :
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                else:
                    successtimes+=1
            elif(attType==2):
                if (userposition[0]+surface[0]/8)>surface[0]/2 :
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                else:
                    successtimes+=1
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            
        if actiontimeout <= int(time.time()):    
            useraction=0

        if waittimeout == int(time.time()):
            waittimeout=0
            bossflag=0
        #print(userposition[1],destination[1],distance)
        usermove()

def intro3():
    global successtimes,currentScene,visibility,attTimeout,bossflag,attType,recordtime,height,timepass,usercolor,colortimeout,flag,useraction,waittimeout,jump_effect_time
    

    if flag==0:
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]/2-startText.get_width()/2 and x<=surface[0]/2+startText.get_width()/2
           and y>=surface[1]*0.8-startText.get_height()/2 and y<=surface[1]*0.8+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
            if event.type == pygame.MOUSEBUTTONUP:
                flag=1
    if flag!=0:
        mainWindows.blit(introbg,[0,0])
        gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        if bossflag ==0:
            attType=4
            attTimeout=int(time.time())+1.5
            recordtime=int(time.time())
            height=surface[1]
            bossflag=1
            timepass=0
            usercolor=(255,255,255)
        for i in range (0,3):
            image=pygame.image.load("./image/notsuccess.png")
            mainWindows.blit(image,[400+i*150,100])
        a=successtimes
        if a>3:a=3
        for j in range(0,a):
            image2=pygame.image.load("./image/success.png")
            mainWindows.blit(image2,[400+j*150,100])
        if successtimes<3:
            drawUser(useraction)
        elif successtimes>=4:
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
                currentScene="optional"
        if attTimeout!=round(time.time(),1) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            
            timepass=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
            drawAttType(attType)
                
        else:     
            if(attType==4):
                if jump_effect_time<int(time.time()):
                    usercolor=(255,0,0)
                else:
                    successtimes+=1
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            
        if actiontimeout <= int(time.time()):    
            useraction=0

        if waittimeout == int(time.time()):
            waittimeout=0
            bossflag=0
        #print(userposition[1],destination[1],distance)
        usermove()

def intro4():
    global successtimes,currentScene,visibility,attTimeout,bossflag,attType,recordtime,height,timepass,usercolor,colortimeout,flag,useraction,waittimeout,thigh_effect_time
    if flag==0:
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]/2-startText.get_width()/2 and x<=surface[0]/2+startText.get_width()/2
           and y>=surface[1]*0.8-startText.get_height()/2 and y<=surface[1]*0.8+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
            if event.type == pygame.MOUSEBUTTONUP:
                flag=1
    if flag!=0:
        mainWindows.blit(introbg,[0,0])
        gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        if bossflag ==0:
            attType=3
            attTimeout=int(time.time())+1.5
            recordtime=int(time.time())
            height=surface[1]
            bossflag=1
            timepass=0
            usercolor=(255,255,255)
        for i in range (0,3):
            image=pygame.image.load("./image/notsuccess.png")
            mainWindows.blit(image,[400+i*150,100])
        a=successtimes
        if a>3:a=3
        for j in range(0,a):
            image2=pygame.image.load("./image/success.png")
            mainWindows.blit(image2,[400+j*150,100])
        if successtimes<3:
            drawUser(useraction)
        elif successtimes>=4:
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
                currentScene="optional"
        if attTimeout!=round(time.time(),1) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            
            timepass=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
            drawAttType(attType)
                
        else:     
            if(attType==3):
                if thigh_effect_time<int(time.time()):
                    usercolor=(255,0,0)
                else:
                    successtimes+=1
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            
        if actiontimeout <= int(time.time()):    
            useraction=0

        if waittimeout == int(time.time()):
            waittimeout=0
            bossflag=0
        #print(userposition[1],destination[1],distance)
        usermove()

def intro5():
    global successtimes,currentScene,visibility,attTimeout,bossflag,attType,recordtime,height,timepass,usercolor,colortimeout,flag,useraction,waittimeout
    global attTimeout2,selected,zone,hit_flag,timepass2
    

    if flag==0:
        attTimeout=int(time.time())+2
        attTimeout2=0
        bossflag=1
        attType=0
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]/2-startText.get_width()/2 and x<=surface[0]/2+startText.get_width()/2
           and y>=surface[1]*0.8-startText.get_height()/2 and y<=surface[1]*0.8+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
            if event.type == pygame.MOUSEBUTTONUP:
                flag=1
    if flag!=0:
    
        mainWindows.blit(introbg,[0,0])
        gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        if bossflag ==0:
            hit_flag=0
            attType=5
            attTimeout=int(time.time())+3
            zone=random.randint(1,5)
            selected=random.sample(range(0,5),zone)
            if zone==5:
                attTimeout2=int(time.time())+4
            recordtime=int(time.time())
            height=surface[1]
            bossflag=1
            timepass=0
            usercolor=(255,255,255)
            print(zone)
        for i in range (0,3):
            image=pygame.image.load("./image/notsuccess.png")
            mainWindows.blit(image,[400+i*150,100])
        a=successtimes
        if a>3:a=3
        for j in range(0,a):
            image2=pygame.image.load("./image/success.png")
            mainWindows.blit(image2,[400+j*150,100])
        if successtimes<3:
            drawUser(useraction)
        elif successtimes>=4:
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
                currentScene="optional"

        if attTimeout2!=int(time.time()) and (successtimes<=3) and zone==5:
            timepass2=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass2>attTimeout2-recordtime):timepass2=attTimeout2-recordtime #如果大於timeout就設成timeout
            if(attTimeout2!=0):drawAttType2()
        elif (successtimes<=3) and zone==5:
            if (selected[4]==0):
                if userposition[0]<surface[0]/5:
                    usercolor=(255,0,0) 
                    hit_flag=1
            if (selected[4]==1):
                if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                    usercolor=(255,0,0) 
                    hit_flag=1
            if (selected[4]==2):
                if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                    usercolor=(255,0,0) 
                    hit_flag=1
            if (selected[4]==3):
                if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                    usercolor=(255,0,0) 
                    hit_flag=1
            if (selected[4]==4):
                if userposition[0]+surface[0]/8>surface[0]*4/5:
                    usercolor=(255,0,0) 
                    hit_flag=1
            if hit_flag==0:successtimes+=1
            
            zone=0
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            timepass2=0

        if attTimeout!=round(time.time(),1) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            
            timepass=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
            drawAttType(attType)
                
        else:     
            if(attType==5):
                if zone!=5:
                    if (0 in selected):
                        if userposition[0]<surface[0]/5:
                            usercolor=(255,0,0) 
                            hit_flag=1
                    if (1 in selected):
                        if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                            usercolor=(255,0,0) 
                            hit_flag=1
                    if (2 in selected):
                        if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                            usercolor=(255,0,0) 
                            hit_flag=1
                    if (3 in selected):
                        if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                            usercolor=(255,0,0) 
                            hit_flag=1
                    if (4 in selected):
                        if userposition[0]+surface[0]/8>surface[0]*4/5:
                            usercolor=(255,0,0) 
                            hit_flag=1
                    if hit_flag==0:successtimes+=1
                else:
                    if(selected[4]==0):
                        if userposition[0]+surface[0]/8>surface[0]/5:
                            usercolor=(255,0,0)
                            hit_flag=1
                    if(selected[4]==1):
                        if not( (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5)):
                            usercolor=(255,0,0) 
                            hit_flag=1
                    if(selected[4]==2):
                        if not((userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5)):
                            usercolor=(255,0,0)
                            hit_flag=1
                    if(selected[4]==3):
                        if not((userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5)):
                            usercolor=(255,0,0)
                            hit_flag=1
                    if(selected[4]==4):
                        if userposition[0]<surface[0]*4/5:
                            usercolor=(255,0,0)
                            hit_flag=1
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            timepass2=0
            
        if actiontimeout <= int(time.time()):    
            useraction=0

        if waittimeout == int(time.time()):
            waittimeout=0
            bossflag=0
        #print(userposition[1],destination[1],distance)
        usermove()

def intro6():
    global currentScene,bosslife,bossposition,life,winflag,bossflag,flag,hit_flag
    global userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility
    global gflag,timepass,recordtime,usercolor,bosscolor,colortimeout,useraction,actiontimeout,multipleAttackZone,zone,selected,attTimeout2,timepass2
    global action_start,action_end,defence,recover,defencing,successtimes
    
    if flag==0:
        attTimeout=int(time.time())+2
        attTimeout2=0
        bossflag=1
        attType=0
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]/2-startText.get_width()/2 and x<=surface[0]/2+startText.get_width()/2
           and y>=surface[1]*0.8-startText.get_height()/2 and y<=surface[1]*0.8+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]/2-startText.get_width()/2,surface[1]*0.8-startText.get_height()/2))
            if event.type == pygame.MOUSEBUTTONUP:
                flag=1
    if flag!=0:
        mainWindows.blit(introbg,[0,0])
        gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        if bossflag ==0:
            hit_flag=0
            attType=random.randint(1,4)
            if attType==3 or attType==4:
                attTimeout=int(time.time())+1.5
            elif attType == 1 or attType == 2:
                attType=5
                attTimeout=int(time.time())+3
                zone=random.randint(1,5)
                selected=random.sample(range(0,5),zone)
                if zone==5:
                    attTimeout2=int(time.time())+4
            else:
                attTimeout=int(time.time())+3
            
            recordtime=int(time.time())
            height=surface[1]
            bossflag=1
            timepass=0
            timepass2=0
            usercolor=(255,255,255)
        for i in range (0,3):
            image=pygame.image.load("./image/notsuccess.png")
            mainWindows.blit(image,[400+i*150,100])
        a=successtimes
        if a>3:a=3
        for j in range(0,a):
            image2=pygame.image.load("./image/success.png")
            mainWindows.blit(image2,[400+j*150,100])
        if successtimes<3:
            drawUser(useraction)
            pygame.draw.rect(mainWindows,(255,255,255),(10,+((100-defence)*surface[0]*0.3/100)+surface[1]*0.1,20,defence*surface[0]*0.3/100))
        elif successtimes>=4:
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
                currentScene="optional"

        if action_start==1 and action_end==0 and(recover==0 or recover==2) :
            defence -=2
            defencing=1
            recover=0
        if defence <=0:
            recover=1
            defencing=0
        if recover==1 or recover==2:
            defence+=1
        if defence>=100 and recover==1:
            recover=0
            action_start=0
        if action_start==1 and action_end==1:
            recover=2
            defencing=0
            action_start=action_end=0   
        if defence >=100:defence=100

        if attTimeout2!=int(time.time()) and (successtimes<=3) and zone==5:
            timepass2=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass2>attTimeout2-recordtime):timepass2=attTimeout2-recordtime #如果大於timeout就設成timeout
            if(attTimeout2!=0):drawAttType2()
        elif (successtimes<=3) and zone==5:
            if (selected[4]==0):
                if userposition[0]<surface[0]/5:
                    defencefunc()
            if (selected[4]==1):
                if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                    defencefunc()
            if (selected[4]==2):
                if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                    defencefunc()
            if (selected[4]==3):
                if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                    defencefunc()
            if (selected[4]==4):
                if userposition[0]+surface[0]/8>surface[0]*4/5:
                    defencefunc()
            
            zone=0
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            timepass2=0

        if attTimeout!=round(time.time(),1) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            
            timepass=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
            drawAttType(attType)
                
        else:
            if(attType==1):
                if userposition[0]<surface[0]/2 :
                    defencefunc()
            if(attType==2):
                if (userposition[0]+surface[0]/8)>surface[0]/2 :
                    defencefunc()    
            if(attType==3):
                if(userposition[1]+5.5*userposition[2]/3)>surface[1]*2/3:
                    defencefunc() 
            if(attType==4):
                if(userposition[1])<surface[1]*0.816:
                    defencefunc()     
            if(attType==5):
                if zone!=5:
                    if (0 in selected):
                        if userposition[0]<surface[0]/5:
                            defencefunc()
                    if (1 in selected):
                        if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                            defencefunc()
                    if (2 in selected):
                        if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                            defencefunc()
                    if (3 in selected):
                        if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                            defencefunc()
                    if (4 in selected):
                        if userposition[0]+surface[0]/8>surface[0]*4/5:
                            defencefunc()
                else:
                    if(selected[4]==0):
                        if userposition[0]+surface[0]/8>surface[0]/5:
                            defencefunc()
                    if(selected[4]==1):
                        if not( (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5)):
                            defencefunc()
                    if(selected[4]==2):
                        if not((userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5)):
                            defencefunc()
                    if(selected[4]==3):
                        if not((userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5)):
                            defencefunc()
                    if(selected[4]==4):
                        if userposition[0]<surface[0]*4/5:
                            defencefunc()
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            timepass2=0
            
        if actiontimeout <= int(time.time()):    
            useraction=0

        if waittimeout == int(time.time()):
            waittimeout=0
            bossflag=0
        #print(userposition[1],destination[1],distance)
        usermove()

def windowssize(x):
    global mainWindows
    if x==1:
        mainWindows=pygame.display.set_mode((800,600),RESIZABLE,32)
    elif x==2:
        mainWindows=pygame.display.set_mode((1200,900),RESIZABLE,32)
## use "currentScene" variaty to change the interface ##        
def createScene():
    if currentScene == "menu":
        # windowssize(1)
        Menu()
    if currentScene == "optional":
        # windowssize(1)
        optional()
    if currentScene == "normalMode":
        # windowssize(1)
        normalMode()
    if currentScene == "level1":
        # windowssize(2)
        level1()
    if currentScene == "stop":
        stop()
    if currentScene == "level2":
        windowssize(2)
        level2()
    if currentScene == "level3":
        # windowssize(2)
        level3()
    if currentScene == "level4":
        windowssize(2)
        level4()
    if currentScene == "intro1":
        windowssize(2)
        intro1()
    if currentScene == "intro2":
        windowssize(2)
        intro2()
    if currentScene == "intro3":
        windowssize(2)
        intro3()
    if currentScene == "intro4":
        windowssize(2)
        intro4()
    if currentScene == "intro5":
        windowssize(2)
        intro5()
    if currentScene == "intro6":
        windowssize(2)
        intro6()
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
                # print(x,y)
        
        if event.type == pygame.KEYDOWN and ((currentScene in level) or (currentScene in intro)) :
            if event.key ==pygame.K_z:
                bosslife-=5
                bosscolor=(255,0,0)
                attack=1
                useraction=2
                if currentScene == "intro1":
                    successtimes+=1
                colortimeout=int(time.time())+0.5
                actiontimeout=int(time.time()+1)
            if event.key ==pygame.K_x:
                bosslife-=5
                bosscolor=(255,0,0)
                attack=2
                useraction=1
                if currentScene == "intro1":
                    successtimes+=1
                colortimeout=int(time.time())+0.5
                actiontimeout=int(time.time()+1)
            if event.key ==pygame.K_SPACE:
                life-=1
                usercolor=(255,0,0)
                colortimeout=int(time.time())+1.0
                if life<=0:
                    flag=0
                    currentScene="normalMode"
            if event.key == pygame.K_LEFT :
                destination[0]=surface[0]/4-surface[0]/16
                distance=[destination[0]-userposition[0],0,0]
                timeout=time.time()+0.5
            if event.key == pygame.K_RIGHT :
                destination[0]=3*surface[0]/4-surface[0]/16
                distance=[destination[0]-userposition[0],1,1]
                timeout=time.time()+0.5
            if event.key == pygame.K_UP:
                destination[1]=0.6*surface[1]
                distance=[destination[1]-userposition[1],2,2]
                timeout=time.time()+0.5
                thigh_effect_time=int(time.time())+1
            if event.key == pygame.K_DOWN:
                destination[1]=0.9*surface[1]
                distance=[destination[1]-userposition[1],2,2]
                timeout=time.time()+0.5
                jump_effect_time=int(time.time())+1
            if event.key == pygame.K_q:
                life+=1
            if event.key == pygame.K_y:
                successtimes-=1
            if event.key == pygame.K_a :
                userposition[0]-=50
            if event.key == pygame.K_d :
                userposition[0]+=50
            if event.key == pygame.K_f:
                action_start=1
            if action_start==1:
                if event.key == pygame.K_g:
                    action_end=1
                # if(defence>0 and action_start==action_end):action_start=action_end=0
            if event.key ==pygame.K_SPACE:
                    life-=1
                    if life<=0:
                        flag=0
                        windowssize(1)
                        currentScene="normalMode"
        if bosslife==0 and currentScene=="level1":
            gameovertimeout=int(time.time())+8
            visibility=0
            attType=0
            bosslife-=1
            gflag=1
        if successtimes==3 and (currentScene in intro):
            gameovertimeout=int(time.time())+8
            visibility=0
            successtimes+=1
                
            
    if colortimeout == round(time.time(),1):
        usercolor=(255,255,255)
        bosscolor=(0,0,0)
    ## 隨時更新視窗大小 ##
    surface[0]=mainWindows.get_width()
    surface[1]=mainWindows.get_height()
    #print(mainWindows.get_width(),mainWindows.get_height())
    ## 隨時取得滑鼠位置 ##
    x, y = pygame.mouse.get_pos()
    createScene()

    pygame.display.update()