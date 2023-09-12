import pygame
from pygame.locals import *
from pygame.locals import QUIT
import sys
import threading
import random
import cv2
import mediapipe as mp
import math
import time
import sys
import pyautogui
## 初始化 ##
mp_Draw = mp.solutions.drawing_utils # mediapipe 繪圖方法
mpd_rawing_styles = mp.solutions.drawing_styles # mediapipe 繪圖樣式
mp_holistic = mp.solutions.holistic # mediapipe 全身偵測方法
holistic = mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) 

###################################
#####共用#####
ball_radius = 2
red = (255,0,0)
fist_left_flag = 0
fist_right_flag = 0
#####DEFENSE#####
defense_flag = 0
defense_arm_left_flag = 0
defense_arm_right_flag = 0
shoulder_left_flag = 0
shoulder_right_flag = 0
#####PUNCH#####
punch_arm_left_flag = 0
punch_arm_right_flag = 0
punch_left_flag = 0
punch_right_flag = 0
armpit_left_flag = 0
armpit_right_flag = 0
step_left_flag = 0
step_right_flag = 0
#####SQUATDOWN#####
thigh_flag = 0
jump_flag=0
###################################
pTime = 0
cTime = 0
thigh_text = ''
# thigh_flag = 0
movePoint = [0,0]
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

multipleAttackZone=[0,surface[0]/5,2*surface[0]/5,3*surface[0]/5,4*surface[0]/5]
zone=0
selected=[]
action_start=0
action_end=0
defence=100
recover=0
defencing=0
hitflag=0
thigh_effect_time=0
jump_effect_time=0
user=2  ##1李 2古

if user==1:
    leftPunch=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\punch_left-1.jpg")
    rightPunch=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\punch_right-1.jpg")
elif user==2:
    leftPunch=pygame.image.load("./image/punch_left-1.jpg")
    rightPunch=pygame.image.load("./image/punch_right-1.jpg")

## menu interface ##
def Menu():
    global currentScene,user
    mainWindows.fill((0,0,0))
    #pygame.draw.rect(mainWindows,(255,255,255),((surface[0]-300)/2,surface[1]-200,300,200))

    if user==1:
        menuImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\menu_punch.png").convert()
        mainWindows.blit(menuImage,[0,50])
    elif user==2:
        menuImage=pygame.image.load("./image/menu_punch.png").convert()
        mainWindows.blit(menuImage,[0,50])

    menuFont=pygame.font.SysFont(None,60)
    startText=menuFont.render("start",True,(255,255,255))
    mainWindows.blit(startText,(surface[0]*3/4-startText.get_width()/2,surface[1]/4-startText.get_height()))
    optionalText=menuFont.render("introduce",True,(255,255,255))
    mainWindows.blit(optionalText,(surface[0]*3/4-startText.get_width()/2,surface[1]*2/4-startText.get_height()))
    exitText=menuFont.render("exit",True,(255,255,255))
    mainWindows.blit(exitText,(surface[0]*3/4-startText.get_width()/2,surface[1]*3/4-startText.get_height()))

    if user==1:
        mouseImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\mouse.png").convert()
        mainWindows.blit(mouseImage,[x,y])
    elif user==2:
        mouseImage=pygame.image.load("./image/mouse.png").convert()
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
    global currentScene,user
    mainWindows.fill((0,0,0))
    if user==1:menuImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\menu.jpg").convert()
    elif user==2:pygame.image.load("./image/menu.jpg").convert()
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
    menuImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\menu.jpg").convert()
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
    global currentScene,flag,bossflag,height,attType,destination,distance,gflag,height2
    mainWindows.fill((0,0,0))
    
    normalModeFont=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    returnText=normalModeFont.render("return",True,(255,255,255))
    mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.85))

    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]/8,surface[1]/6,surface[0]/6,surface[0]/6),border_radius=4)
    pygame.draw.rect(mainWindows,(0,0,0),(surface[0]/8+surface[0]/160,surface[1]/6+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4) 
    
    pygame.draw.rect(mainWindows,(255,255,255),(3.5*surface[0]/8,surface[1]/6,surface[0]/6,surface[0]/6),border_radius=4)
    pygame.draw.rect(mainWindows,(0,0,0),(3.5*surface[0]/8+surface[0]/160,surface[1]/6+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4)
    
    pygame.draw.rect(mainWindows,(255,255,255),(6*surface[0]/8,surface[1]/6,surface[0]/6,surface[0]/6),border_radius=4)
    pygame.draw.rect(mainWindows,(0,0,0),(6*surface[0]/8+surface[0]/160,surface[1]/6+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4)

    pygame.draw.rect(mainWindows,(255,255,255),(3.5*surface[0]/8,surface[1]*2/3,surface[0]/6,surface[0]/6),border_radius=4)
    pygame.draw.rect(mainWindows,(0,0,0),(3.5*surface[0]/8+surface[0]/160,surface[1]*2/3+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4)

    normalModeFont2=pygame.font.SysFont(None,int(surface[0]/5))
    oneText=normalModeFont2.render("1",True,(255,255,255))
    mainWindows.blit(oneText,(surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))
    
    twoText=normalModeFont2.render("2",True,(255,255,255))
    mainWindows.blit(twoText,(3.5*surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))

    threeText=normalModeFont2.render("3",True,(255,255,255))
    mainWindows.blit(threeText,(6*surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))

    fourText=normalModeFont2.render("4",True,(255,255,255))
    mainWindows.blit(fourText,(3.5*surface[0]/8+surface[0]/25,surface[1]*2/3+surface[1]/40))

    if(x>=surface[0]*0.05 and x<=surface[0]*0.05+returnText.get_width() and y>= surface[1]*0.85 and y<= surface[1]*0.85+returnText.get_height()):
        returnText=normalModeFont.render("return",True,(255,0,0))
        mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.85))
        if event.type == pygame.MOUSEBUTTONUP:
            currentScene="menu"

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
            distance=[0,5,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            currentScene="level1"

    if(x>=3.5*surface[0]/8 and x<=3.5*surface[0]/8+surface[0]/6 and y>=surface[1]/6 and y<=surface[1]/6+surface[0]/6):
        pygame.draw.rect(mainWindows,(0,255,255),(3.5*surface[0]/8,surface[1]/6,surface[0]/6,surface[0]/6),border_radius=4)
        pygame.draw.rect(mainWindows,(0,0,0),(3.5*surface[0]/8+surface[0]/160,surface[1]/6+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4)
        twoText=normalModeFont2.render("2",True,(0,255,255))
        mainWindows.blit(twoText,(3.5*surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            flag=0
            bossflag=0
            height=surface[1]
            attType=0
            distance=[0,5,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            currentScene="level2"
    
    if(x>=6*surface[0]/8 and x<=6*surface[0]/8+surface[0]/6 and y>=surface[1]/6 and y<=surface[1]/6+surface[0]/6):
        pygame.draw.rect(mainWindows,(0,255,255),(6*surface[0]/8,surface[1]/6,surface[0]/6,surface[0]/6),border_radius=4)
        pygame.draw.rect(mainWindows,(0,0,0),(6*surface[0]/8+surface[0]/160,surface[1]/6+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4)
        threeText=normalModeFont2.render("3",True,(0,255,255))
        mainWindows.blit(threeText,(6*surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            flag=0
            bossflag=0
            height=surface[1]
            height2=surface[1]
            attType=0
            distance=[0,5,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            currentScene="level3"
    
    if(x>=3.5*surface[0]/8 and x<=3.5*surface[0]/8+surface[0]/6 and y>=surface[1]*2/3 and y<=surface[1]*2/3+surface[0]/6):
        pygame.draw.rect(mainWindows,(0,255,255),(3.5*surface[0]/8,surface[1]*2/3,surface[0]/6,surface[0]/6),border_radius=4)
        pygame.draw.rect(mainWindows,(0,0,0),(3.5*surface[0]/8+surface[0]/160,surface[1]*2/3+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4)
        fourText=normalModeFont2.render("4",True,(0,255,255))
        mainWindows.blit(fourText,(3.5*surface[0]/8+surface[0]/25,surface[1]*2/3+surface[1]/40))
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            flag=0
            bossflag=0
            height=surface[1]
            attType=0
            distance=[0,5,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            currentScene="level4"
    if user==1:mouseImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\mouse.png").convert()
    elif user==2:mouseImage=pygame.image.load("./image/mouse.png").convert()
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
        bosslife = 200
    elif x==4:bosslife = 250
        
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
            userposition[1]+=distance[0]/5
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
    global currentScene,bosslife,life,winflag,bossflag,flag,userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility,gflag,timepass,recordtime
    secWindows = pygame.surface.Surface((surface[0],surface[1]), SRCALPHA, 32)
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
    global gflag,timepass,recordtime,selected,zone,multipleAttackZone,attTimeout2,timepass2,height2
    secWindows = pygame.surface.Surface((surface[0],surface[1]), SRCALPHA, 32)  
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
        mainWindows.blit(rightPunch,[surface[0]*3/4-rightPunch.get_width(),surface[1]/2]) 
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
        mainWindows.blit(leftPunch,[surface[0]/4,surface[1]/2]) 

def defencefunc():
    global usercolor,defence,life,colortimeout
    if(defencing==0):
        life-=1
        usercolor=(255,0,0)   
        colortimeout=int(time.time())+0.5
    else:
        defence=-1

def level1():
    global currentScene,bosslife,bossposition,life,winflag,bossflag,flag,userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility,gflag,timepass,recordtime,usercolor,bosscolor,colortimeout,useraction,actiontimeout
    global hitflag,user
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
        hitflag=0
        timepass=0
        ##以上是每次boss攻擊前需更動的值##
    mainWindows.fill((90,0,173))
    
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.2+(100-bosslife)*(surface[0]*0.3/100),surface[1]*0.05,bosslife*surface[0]*0.3/100,10))
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.5,surface[1]*0.05,bosslife*surface[0]*0.3/100,10))   
    gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    gameoverText=gameover.render("YOU DIED",True,(255,0,0))

    if not gflag:
        drawUser(useraction)
        drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
        for i in range (0,life):
            if user==1:lifeImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\Unknown-4.png")
            elif user==2:lifeImage=pygame.image.load("./image/Unknown-4.png")
            mainWindows.blit(lifeImage,[50*i,0])
        ##顯示左上角愛心##
    
    if attTimeout!=int(time.time()) and (not(gflag)) and bosslife>0:  #boss攻擊時間未結束 and 遊戲未結束
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear() 
        timepass=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
        drawAttType(attType)
            
    else:
        all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear() 
        if(attType==1) and hitflag==0:
            for i in range(len(all_nodes)):
                if all_nodes[i][0]<surface[0]/2 :
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
        elif(attType==2) and hitflag==0:
            for i in range(len(all_nodes)):
                if all_nodes[i][0]>surface[0]/2 :
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
        #以上是當角色在攻擊範圍內且倒數結束時的動作
        if life==0:
            gameovertimeout=int(time.time())+5
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
                visibility+=3
                if visibility>=255:
                    visibility=255
            else:
                mainWindows.fill((0,0,0))
                currentScene="normalMode"
        #以上為死亡動畫    
        if bosslife<=0:
            gflag=1
            secWindows = pygame.surface.Surface((surface[0],surface[1]), SRCALPHA, 32)
            if gameovertimeout>=int(time.time()):
                gameoverText=gameover.render("CONGRATULATION",True,(255,255,56))
                pygame.draw.rect(secWindows,(0,0,0,visibility),(0,0,surface[0],surface[1]))
                secWindows.blit(gameoverText,(surface[0]/2-gameoverText.get_width()/2,surface[1]/2-gameoverText.get_height()/2))
                mainWindows.blit(secWindows,(0,0))
                visibility+=3
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
    if colortimeout <= round(time.time(),1):
        usercolor=(255,255,255)
        bosscolor=(0,0,0)
        
    if actiontimeout <= int(time.time()):    
        useraction=0

    if waittimeout == int(time.time()):
        waittimeout=0
        bossflag=0
    #print(userposition[1],destination[1],distance)
    usermove()   

def level2():
    global currentScene,bosslife,bossposition,life,winflag,bossflag,flag,userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility,gflag,timepass,recordtime,usercolor,bosscolor,colortimeout,useraction,actiontimeout
    global hitflag,thigh_effect_time,jump_effect_time,user
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
        hitflag=0
        recordtime=int(time.time())
        height=surface[1]
        bossflag=1
        timepass=0
        ##以上是每次boss攻擊前需更動的值##
    mainWindows.fill((90,0,173))
    
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.2+(100-bosslife)*(surface[0]*0.3/100),surface[1]*0.05,bosslife*surface[0]*0.3/100,10))
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.5,surface[1]*0.05,bosslife*surface[0]*0.3/100,10))   
    gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    gameoverText=gameover.render("YOU DIED",True,(255,0,0))

    if not gflag:
        drawUser(useraction)
        drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
        for i in range (0,life):
            if user==1:lifeImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\Unknown-4.png")
            elif user==2:lifeImage=pygame.image.load("./image/Unknown-4.png")
            mainWindows.blit(lifeImage,[50*i,0])
        ##顯示左上角愛心##
    #print(userposition)
    if attTimeout!=round(time.time(),1) and (not(gflag)) and bosslife>0:  #boss攻擊時間未結束 and 遊戲未結束
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear() 
        timepass=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
        drawAttType(attType)
            
    else:  
        all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear()    
        if(attType==1) and hitflag==0:
            for i in range(len(all_nodes)):
                if all_nodes[i][0]<surface[0]/2 :
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
        elif(attType==2) and hitflag==0:
            for i in range(len(all_nodes)):
                if all_nodes[i][0]>surface[0]/2 :
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
        elif(attType==3) and hitflag==0:
            if jump_effect_time<int(time.time()):
                life-=1
                usercolor=(255,0,0)
                colortimeout=int(time.time())+0.5
                hitflag=1
            all_nodes.clear()
        elif(attType==4) and hitflag==0:
            if thigh_effect_time<int(time.time()):
                life-=1
                usercolor=(255,0,0)
                colortimeout=int(time.time())+0.5
                hitflag=1
            all_nodes.clear()

        #以上是當角色在攻擊範圍內且倒數結束時的動作
        if life==0:
            gameovertimeout=int(time.time())+5
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
                visibility+=3
                if visibility>=255:
                    visibility=255
            else:
                mainWindows.fill((0,0,0))
                currentScene="normalMode"
        #以上為死亡動畫    
        if bosslife<0:
            life=99999
            secWindows = pygame.surface.Surface((surface[0],surface[1]), SRCALPHA, 32)
            if gameovertimeout!=int(time.time()):
                gameoverText=gameover.render("CONGRATULATION",True,(255,255,56))
                pygame.draw.rect(secWindows,(0,0,0,visibility),(0,0,surface[0],surface[1]))
                secWindows.blit(gameoverText,(surface[0]/2-gameoverText.get_width()/2,surface[1]/2-gameoverText.get_height()/2))
                mainWindows.blit(secWindows,(0,0))
                visibility+=3
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
    if colortimeout <= round(time.time(),1):
        usercolor=(255,255,255)
        bosscolor=(0,0,0)
        
    if actiontimeout <= int(time.time()):    
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
    global hitflag,thigh_effect_time,jump_effect_time,user

    if flag==0:
        initlife(3)
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
            attTimeout=int(time.time())+3.0
            zone=random.randint(1,5)
            print(zone)
            selected=random.sample(range(0,5),zone)
            if zone==5:
                attTimeout2=int(time.time())+4
        else:
            attTimeout=int(time.time())+3
        hitflag=0
        recordtime=int(time.time())
        height=surface[1]
        bossflag=1
        timepass=0
        timepass2=0
        usercolor=(255,255,255)
        ##以上是每次boss攻擊前需更動的值##
    mainWindows.fill((90,0,173))
    for i in range (0,life):
        if user==1:lifeImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\Unknown-4.png")
        elif user==2:lifeImage=pygame.image.load("./image/Unknown-4.png")
        mainWindows.blit(lifeImage,[50*i,0])
        ##顯示左上角愛心##
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.2+(100-bosslife)*(surface[0]*0.3/100),surface[1]*0.05,bosslife*surface[0]*0.3/100,10))
    pygame.draw.rect(mainWindows,(255,255,255),(surface[0]*0.5,surface[1]*0.05,bosslife*surface[0]*0.3/100,10))   
    gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
    gameoverText=gameover.render("YOU DIED",True,(255,0,0))

    if not gflag:
        drawUser(useraction)
        drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
    #print(userposition)
    if attTimeout2!=int(time.time()) and (not(gflag)) and zone==5 :
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear() 
        timepass2=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass2>attTimeout2-recordtime):timepass2=attTimeout2-recordtime #如果大於timeout就設成timeout
        if(attTimeout2!=0):drawAttType2()
    elif (not(gflag)) and zone==5:
        all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear()   
        if (selected[4]==0 and hitflag==0):
            for i in range(len(all_nodes)):
                if all_nodes[i][0]<surface[0]/5 :
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear() 
            # if userposition[0]<surface[0]/5:
            #     life-=1
            #     usercolor=(255,0,0) 
        elif (selected[4]==1 and hitflag==0):
            for i in range(len(all_nodes)):
                if (all_nodes[i][0]<2*surface[0]/5 and all_nodes[i][0]>surface[0]/5):
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
            # if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
            #     life-=1
            #     usercolor=(255,0,0) 
        elif (selected[4]==2 and hitflag==0):
            for i in range(len(all_nodes)):
                if (all_nodes[i][0]<3*surface[0]/5 and all_nodes[i][0]>2*surface[0]/5):
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
            # if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
            #     life-=1
            #     usercolor=(255,0,0) 
        elif (selected[4]==3 and hitflag==0):
            for i in range(len(all_nodes)):
                if (all_nodes[i][0]<4*surface[0]/5 and all_nodes[i][0]>3*surface[0]/5):
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
            # if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
            #     life-=1
            #     usercolor=(255,0,0) 
        elif (selected[4]==4 and hitflag==0):
            for i in range(len(all_nodes)):
                if (all_nodes[i][0]>4*surface[0]/5):
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
            # if userposition[0]+surface[0]/8>surface[0]*4/5:
            #     life-=1
            #     usercolor=(255,0,0) 
        zone=0
        if life==0:
            gameovertimeout=int(time.time())+5
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
                visibility+=3
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
                visibility+=3
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

    if attTimeout!=round(time.time(),1) and (not(gflag)) :  #boss攻擊時間未結束 and 遊戲未結束

        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear()
        timepass=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
        drawAttType(attType)
    else:    
        all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear()    
        if(attType==1) and hitflag==0:
            for i in range(len(all_nodes)):
                if all_nodes[i][0]<surface[0]/2 :
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
        elif(attType==2) and hitflag==0:
            for i in range(len(all_nodes)):
                if all_nodes[i][0]>surface[0]/2 :
                    life-=1
                    usercolor=(255,0,0)
                    colortimeout=int(time.time())+0.5
                    hitflag=1
                    break
            all_nodes.clear()
        elif(attType==3) and hitflag==0:
            if jump_effect_time<int(time.time()):
                life-=1
                usercolor=(255,0,0)
                colortimeout=int(time.time())+0.5
                hitflag=1
            all_nodes.clear()
        elif(attType==4) and hitflag==0:
            if thigh_effect_time<int(time.time()):
                life-=1
                usercolor=(255,0,0)
                colortimeout=int(time.time())+0.5
                hitflag=1
            all_nodes.clear()
        elif(attType==5) and hitflag==0:
            if zone!=5:
                if (0 in selected):
                    for i in range(len(all_nodes)):
                        if all_nodes[i][0]<surface[0]/5 :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if userposition[0]<surface[0]/5:
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if (1 in selected):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]<2*surface[0]/5 and all_nodes[i][0]> surface[0]/5) :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if (2 in selected):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]<3*surface[0]/5 and all_nodes[i][0]> 2*surface[0]/5) :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if (3 in selected):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]<4*surface[0]/5 and all_nodes[i][0]> 3*surface[0]/5) :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if (4 in selected):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>4*surface[0]/5) :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if userposition[0]+surface[0]/8>surface[0]*4/5:
                    #     life-=1
                    #     usercolor=(255,0,0) 
            else:
                if(selected[4]==0 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>surface[0]/5) :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if userposition[0]+surface[0]/8>surface[0]/5:
                    #     life-=1
                    #     usercolor=(255,0,0)
                if(selected[4]==1 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>2*surface[0]/5 and all_nodes[i][0]<surface[0]/5) :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if not( (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5)):
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if(selected[4]==2 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>3*surface[0]/5 and all_nodes[i][0]<2*surface[0]/5) :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if not((userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5)):
                    #     life-=1
                    #     usercolor=(255,0,0)
                if(selected[4]==3 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>4*surface[0]/5 and all_nodes[i][0]<3*surface[0]/5) :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    all_nodes.clear()
                    # if not((userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5)):
                    #     life-=1
                    #     usercolor=(255,0,0)
                if(selected[4]==4 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]<4*surface[0]/5) :
                            life-=1
                            usercolor=(255,0,0)
                            colortimeout=int(time.time())+0.5
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if userposition[0]<surface[0]*4/5:
                    #     life-=1
                    #     usercolor=(255,0,0)


        #以上是當角色在攻擊範圍內且倒數結束時的動作
        if life==0:
            gameovertimeout=int(time.time())+5
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
                visibility+=3
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
                visibility+=3
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
    global hitflag,thigh_effect_time,jump_effect_time,user

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
        hitflag=0
        height=surface[1]
        bossflag=1
        timepass=0
        timepass2=0
        usercolor=(255,255,255)
        ##以上是每次boss攻擊前需更動的值##
    mainWindows.fill((90,0,173))
    for i in range (0,life):
        if user==1:lifeImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\Unknown-4.png")
        elif user==2:lifeImage=pygame.image.load("./image/Unknown-4.png")
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
    if action_start==1 and action_end==1 and recover!=1:
        recover=2
        defencing=0
        action_start=action_end=0   
    if defence >=100:defence=100
    #print(defence,action_start,action_end,recover,defencing)
    

    if not gflag:
        drawUser(useraction)
        drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
    #print(userposition)
    if attTimeout2!=int(time.time()) and (not(gflag)) and zone==5 :
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear() 
        timepass2=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass2>attTimeout2-recordtime):timepass2=attTimeout2-recordtime #如果大於timeout就設成timeout
        if(attTimeout2!=0):drawAttType2()
    elif (not(gflag)) and zone==5:
        all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear()   
        if (selected[4]==0 and hitflag==0):
            for i in range(len(all_nodes)):
                if all_nodes[i][0]<surface[0]/5 :
                    defencefunc()
                    hitflag=1
                    break
            all_nodes.clear() 
            # if userposition[0]<surface[0]/5:
            #     life-=1
            #     usercolor=(255,0,0) 
        elif (selected[4]==1 and hitflag==0):
            for i in range(len(all_nodes)):
                if (all_nodes[i][0]<2*surface[0]/5 and all_nodes[i][0]>surface[0]/5):
                    defencefunc()
                    hitflag=1
                    break
            all_nodes.clear()
            # if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
            #     life-=1
            #     usercolor=(255,0,0) 
        elif (selected[4]==2 and hitflag==0):
            for i in range(len(all_nodes)):
                if (all_nodes[i][0]<3*surface[0]/5 and all_nodes[i][0]>2*surface[0]/5):
                    defencefunc()
                    hitflag=1
                    break
            all_nodes.clear()
            # if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
            #     life-=1
            #     usercolor=(255,0,0) 
        elif (selected[4]==3 and hitflag==0):
            for i in range(len(all_nodes)):
                if (all_nodes[i][0]<4*surface[0]/5 and all_nodes[i][0]>3*surface[0]/5):
                    defencefunc()
                    hitflag=1
                    break
            all_nodes.clear()
            # if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
            #     life-=1
            #     usercolor=(255,0,0) 
        elif (selected[4]==4 and hitflag==0):
            for i in range(len(all_nodes)):
                if (all_nodes[i][0]>4*surface[0]/5):
                    defencefunc()
                    hitflag=1
                    break
            all_nodes.clear()
            # if userposition[0]+surface[0]/8>surface[0]*4/5:
            #     life-=1
            #     usercolor=(255,0,0) 
        zone=0
        if life==0:
            gameovertimeout=int(time.time())+5
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
                visibility+=3
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
                visibility+=3
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

    if attTimeout!=round(time.time(),1) and (not(gflag)) :  #boss攻擊時間未結束 and 遊戲未結束

        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear()
        timepass=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
        drawAttType(attType)
    else:    
        all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear()    
        if(attType==1) and hitflag==0:
            for i in range(len(all_nodes)):
                if all_nodes[i][0]<surface[0]/2 :
                    defencefunc()
                    hitflag=1
                    break
            all_nodes.clear()
        elif(attType==2) and hitflag==0:
            for i in range(len(all_nodes)):
                if all_nodes[i][0]>surface[0]/2 :
                    defencefunc()
                    hitflag=1
                    break
            all_nodes.clear()
        elif(attType==3) and hitflag==0:
            if jump_effect_time<int(time.time()):
                defencefunc()
                hitflag=1
            all_nodes.clear()
        elif(attType==4) and hitflag==0:
            if thigh_effect_time<int(time.time()):
                defencefunc()
                hitflag=1
            all_nodes.clear()
        elif(attType==5) and hitflag==0:
            if zone!=5:
                if (0 in selected):
                    for i in range(len(all_nodes)):
                        if all_nodes[i][0]<surface[0]/5 :
                            defencefunc()
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if userposition[0]<surface[0]/5:
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if (1 in selected):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]<2*surface[0]/5 and all_nodes[i][0]> surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if (2 in selected):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]<3*surface[0]/5 and all_nodes[i][0]> 2*surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if (3 in selected):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]<4*surface[0]/5 and all_nodes[i][0]> 3*surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if (4 in selected):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>4*surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    hitflag=0
                    all_nodes.clear() 
                    # if userposition[0]+surface[0]/8>surface[0]*4/5:
                    #     life-=1
                    #     usercolor=(255,0,0) 
            else:
                if(selected[4]==0 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if userposition[0]+surface[0]/8>surface[0]/5:
                    #     life-=1
                    #     usercolor=(255,0,0)
                if(selected[4]==1 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>2*surface[0]/5 and all_nodes[i][0]<surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if not( (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5)):
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if(selected[4]==2 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>3*surface[0]/5 and all_nodes[i][0]<2*surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if not((userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5)):
                    #     life-=1
                    #     usercolor=(255,0,0)
                if(selected[4]==3 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>4*surface[0]/5 and all_nodes[i][0]<3*surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    all_nodes.clear()
                    # if not((userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5)):
                    #     life-=1
                    #     usercolor=(255,0,0)
                if(selected[4]==4 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]<4*surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if userposition[0]<surface[0]*4/5:
                    #     life-=1
                    #     usercolor=(255,0,0)


        #以上是當角色在攻擊範圍內且倒數結束時的動作
        if life==0:
            gameovertimeout=int(time.time())+5
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
                visibility+=3
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
                visibility+=3
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
    if currentScene == "level2":
        level2()
    if currentScene == "level3":
        level3()
    if currentScene == "level4":
        level4()
def vector_2d_angle(v1, v2):
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_= math.degrees(math.acos((v1_x*v2_x+v1_y*v2_y)/(((v1_x**2+v1_y**2)**0.5)*((v2_x**2+v2_y**2)**0.5))))
    except:
        angle_ = 180
    return angle_
# 根據傳入的 21 個節點座標，得到該手指的角度
def hand_angle(hand_):
    angle_list = []
    # 大拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[2][0])),(int(hand_[0][1])-int(hand_[2][1]))),
        ((int(hand_[3][0])- int(hand_[4][0])),(int(hand_[3][1])- int(hand_[4][1])))
        )
    angle_list.append(angle_)
    # 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])-int(hand_[6][0])),(int(hand_[0][1])- int(hand_[6][1]))),
        ((int(hand_[7][0])- int(hand_[8][0])),(int(hand_[7][1])- int(hand_[8][1])))
        )
    angle_list.append(angle_)
    # 中指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[10][0])),(int(hand_[0][1])- int(hand_[10][1]))),
        ((int(hand_[11][0])- int(hand_[12][0])),(int(hand_[11][1])- int(hand_[12][1])))
        )
    angle_list.append(angle_)
    # 無名指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[14][0])),(int(hand_[0][1])- int(hand_[14][1]))),
        ((int(hand_[15][0])- int(hand_[16][0])),(int(hand_[15][1])- int(hand_[16][1])))
        )
    angle_list.append(angle_)
    # 小拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[18][0])),(int(hand_[0][1])- int(hand_[18][1]))),
        ((int(hand_[19][0])- int(hand_[20][0])),(int(hand_[19][1])- int(hand_[20][1])))
        )
    angle_list.append(angle_)
    return angle_list
# 根據手指角度的串列內容，返回對應的手勢
def hand_pos(finger_angle):
    f1 = finger_angle[0]   # 大拇指角度
    f2 = finger_angle[1]   # 食指角度
    f3 = finger_angle[2]   # 中指角度
    f4 = finger_angle[3]   # 無名指角度
    f5 = finger_angle[4]   # 小拇指角度
    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f2>=50 and f3>=50 and f4>=50 and f5>=50:
        fist_flag = 1
    else:
        fist_flag = 0

    mousecontrol_flag = 0
    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f3>=50 and f4>=50 and f5>=50: #只有食指伸直，表示移動
        mousecontrol_flag = 0        
    elif f4>=50 and f5>=50: #食指跟中指伸直，表示點擊
        mousecontrol_flag = 1  
    else:
        mousecontrol_flag = -1 
    return fist_flag,mousecontrol_flag
    
def arm_angle(arm_):
    angle_list = []
    # 左手臂
    angle_ = vector_2d_angle(
        ((int(arm_[11][0])- int(arm_[13][0])),(int(arm_[11][1])-int(arm_[13][1]))),
        ((int(arm_[13][0])- int(arm_[15][0])),(int(arm_[13][1])- int(arm_[15][1])))
    )
    angle_list.append(angle_)
    # 右手臂
    angle_ = vector_2d_angle(
        ((int(arm_[12][0])- int(arm_[14][0])),(int(arm_[12][1])-int(arm_[14][1]))),
        ((int(arm_[14][0])- int(arm_[16][0])),(int(arm_[14][1])- int(arm_[16][1])))
    )
    angle_list.append(angle_)    
    return angle_list
def arm_pos(arm_angle,x,y):
    left = arm_angle[0]
    right = arm_angle[1]
    
    if left >= x:
        left_flag = 1
    else: 
        left_flag = 0    

    if right >= y:
        right_flag = 1
    else: 
        right_flag = 0
    return left_flag,right_flag
def shoulder_angle(shoulder_):
    angle_list = []
    # 左肩膀
    angle_ = vector_2d_angle(
        ((int(shoulder_[12][0])- int(shoulder_[11][0])),(int(shoulder_[12][1])-int(shoulder_[11][1]))),
        ((int(shoulder_[11][0])- int(shoulder_[13][0])),(int(shoulder_[11][1])- int(shoulder_[13][1])))
    )   
    angle_list.append(angle_)
    # 右肩膀 
    angle_ = vector_2d_angle(
        ((int(shoulder_[11][0])- int(shoulder_[12][0])),(int(shoulder_[11][1])-int(shoulder_[12][1]))),
        ((int(shoulder_[12][0])- int(shoulder_[14][0])),(int(shoulder_[12][1])- int(shoulder_[14][1])))
    )   
    angle_list.append(angle_)
    return angle_list
def shoulder_pos(shoulder_angle):
    left = shoulder_angle[0]
    right = shoulder_angle[1]

    if left >= 90:
        left_flag = 1
    else:
        left_flag = 0  
    if right >= 90:
        right_flag = 1
    else:
        right_flag = 0    
    return left_flag,right_flag
def armpit_angle(armpit_):
    angle_list = []
    # 左腋下
    angle_ = vector_2d_angle(
        ((int(armpit_[23][0])- int(armpit_[11][0])),(int(armpit_[23][1])-int(armpit_[11][1]))),
        ((int(armpit_[11][0])- int(armpit_[13][0])),(int(armpit_[11][1])- int(armpit_[13][1])))
    )   
    angle_list.append(angle_)
    # 右腋下 
    angle_ = vector_2d_angle(
        ((int(armpit_[24][0])- int(armpit_[12][0])),(int(armpit_[24][1])-int(armpit_[12][1]))),
        ((int(armpit_[12][0])- int(armpit_[14][0])),(int(armpit_[12][1])- int(armpit_[14][1])))
    )   
    angle_list.append(angle_)
    return angle_list
def armpit_pos(armpit_angle):
    left = armpit_angle[0]
    right = armpit_angle[1]

    if left >= 150:
        left_flag = 1
    else:
        left_flag = 0
    if right >= 150:
        right_flag = 1
    else:
        right_flag = 0    
    return left_flag,right_flag
def thigh_angle(thigh_):
    angle_list = []
    # 左腿
    angle_ = vector_2d_angle(
        ((int(thigh_[23][0])- int(thigh_[25][0])),(int(thigh_[23][1])-int(thigh_[25][1]))),
        ((int(thigh_[25][0])- int(thigh_[27][0])),(int(thigh_[25][1])- int(thigh_[27][1])))
    )
    angle_list.append(angle_)
    # 右腿
    angle_ = vector_2d_angle(
        ((int(thigh_[24][0])- int(thigh_[26][0])),(int(thigh_[24][1])-int(thigh_[26][1]))),
        ((int(thigh_[26][0])- int(thigh_[28][0])),(int(thigh_[26][1])- int(thigh_[28][1])))
    )
    angle_list.append(angle_)
    return angle_list
def thigh_pos(thigh_angle):
    t1 = thigh_angle[0]
    t2 = thigh_angle[1]
    # 雙腳都要大於50
    if t1 > 50 and t2 > 50:
        thigh_flag = 1
    else: 
        thigh_flag = 0
    return thigh_flag
def drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes):
 # 繪出左手的節點到pygame
    for i in range(len(hand_left_nodes)):
        pygame.draw.circle(mainWindows, red, (int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])), ball_radius)
        if(i==0):
            pygame.draw.line(mainWindows,red,(int(hand_left_nodes[0][0]),int(hand_left_nodes[0][1])),(int(hand_left_nodes[1][0]),int(hand_left_nodes[1][1]))) 
            pygame.draw.line(mainWindows,red,(int(hand_left_nodes[0][0]),int(hand_left_nodes[0][1])),(int(hand_left_nodes[5][0]),int(hand_left_nodes[5][1]))) 
            pygame.draw.line(mainWindows,red,(int(hand_left_nodes[0][0]),int(hand_left_nodes[0][1])),(int(hand_left_nodes[17][0]),int(hand_left_nodes[17][1]))) 
        if(i == 5 or i == 9 or i == 13):
            pygame.draw.line(mainWindows,red,(int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])),(int(hand_left_nodes[i+4][0]),int(hand_left_nodes[i+4][1]))) 
        if(i%4 != 0 and i < len(hand_left_nodes)-1):
            pygame.draw.line(mainWindows,red,(int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])),(int(hand_left_nodes[i+1][0]),int(hand_left_nodes[i+1][1]))) 
    # hand_left_nodes.clear()  
    

    for i in range(len(hand_right_nodes)):
        pygame.draw.circle(mainWindows, red, (int(hand_right_nodes[i][0]),int(hand_right_nodes[i][1])), ball_radius)
        if(i==0):
            pygame.draw.line(mainWindows,red,(int(hand_right_nodes[0][0]),int(hand_right_nodes[0][1])),(int(hand_right_nodes[1][0]),int(hand_right_nodes[1][1]))) 
            pygame.draw.line(mainWindows,red,(int(hand_right_nodes[0][0]),int(hand_right_nodes[0][1])),(int(hand_right_nodes[5][0]),int(hand_right_nodes[5][1]))) 
            pygame.draw.line(mainWindows,red,(int(hand_right_nodes[0][0]),int(hand_right_nodes[0][1])),(int(hand_right_nodes[17][0]),int(hand_right_nodes[17][1]))) 
        if(i == 5 or i == 9 or i == 13):
            pygame.draw.line(mainWindows,red,(int(hand_right_nodes[i][0]),int(hand_right_nodes[i][1])),(int(hand_right_nodes[i+4][0]),int(hand_right_nodes[i+4][1]))) 
        if(i%4 != 0 and i < len(hand_right_nodes)-1):
            pygame.draw.line(mainWindows,red,(int(hand_right_nodes[i][0]),int(hand_right_nodes[i][1])),(int(hand_right_nodes[i+1][0]),int(hand_right_nodes[i+1][1]))) 
    # hand_right_nodes.clear()  

    for i in range(len(body_nodes)):
        pygame.draw.circle(mainWindows, red, (int(body_nodes[i][0]),int(body_nodes[i][1])), ball_radius)
        if((i >= 11 and i <= 14) or (i >= 23 and i <= 26)):
            pygame.draw.line(mainWindows,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+2][0]),int(body_nodes[i+2][1]))) 
        if(i == 11 or i == 23):
            pygame.draw.line(mainWindows,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+1][0]),int(body_nodes[i+1][1]))) 
        if(i == 11 or i == 12):
            pygame.draw.line(mainWindows,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+12][0]),int(body_nodes[i+12][1]))) 
        if(i >= 27 and i <=30):
            pygame.draw.line(mainWindows,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+2][0]),int(body_nodes[i+2][1])))
        if(i == 28 or i == 27):
            pygame.draw.line(mainWindows,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+4][0]),int(body_nodes[i+4][1])))
    # body_nodes.clear()

# 顯示FPS
def showFps(img):
    global cTime,pTime
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,f"FPS:{int(fps)}",(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
## main ##
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open Camera")
        exit()
    hand_left_nodes = []
    hand_right_nodes = []
    body_nodes = []
    mousecontrol_break = 0
    while True:
        ret,img = cap.read()
        if not ret:
            print("Cannot recvive frame")
            break
        img = cv2.resize(img,(surface[0],surface[1]))
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # 使用Holistic模型進行處理
        holistic_result = holistic.process(imgRGB)
        # 獲取身體節點的位置
        body_landmarks = holistic_result.pose_landmarks

        # 如果有偵測到身體節點
        if body_landmarks:
            mp_Draw.draw_landmarks(img,body_landmarks,mp_holistic.POSE_CONNECTIONS)
            arm_points = []
            shoulder_points = []
            armpit_points = []
            thigh_points = []
            # 印出點的數字
            for i,lm in enumerate(body_landmarks.landmark):
                xPos = int(lm.x*surface[0])
                yPos = int(lm.y*surface[1])
                cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),2)
                arm_points.append((xPos,yPos))
                shoulder_points.append((xPos,yPos))
                armpit_points.append((xPos,yPos))
                thigh_points.append((xPos,yPos))
                body_nodes.append([(surface[0] - xPos),(yPos/3)+300])

            # 肩膀角度
            if shoulder_points:
                sh_angle = shoulder_angle(shoulder_points)
                shoulder_left_flag,shoulder_right_flag = shoulder_pos(sh_angle)

            # 手臂角度    
            if arm_points:
                ar_angle = arm_angle(arm_points) 
                defense_arm_left_flag,defense_arm_right_flag = arm_pos(ar_angle,100,100)
                punch_arm_left_flag,punch_arm_right_flag = arm_pos(ar_angle,160,160) 
            # 腋下角度    
            if armpit_points:
                armp_angle = armpit_angle(armpit_points)
                armpit_left_flag,armpit_right_flag = armpit_pos(armp_angle)
            if thigh_points:
                th_angle = thigh_angle(thigh_points)
                thigh_flag = thigh_pos(th_angle)
        # 獲取左手節點
        left_hand_landmarks = holistic_result.left_hand_landmarks
        # 如果有偵測到左手節點
        mouse_x,mouse_y = 0,0
        mousecontrol_flag = -1
        if left_hand_landmarks:
            mp_Draw.draw_landmarks(img,holistic_result.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
            left_handF_points = []
            left_handF_mouse_points = []
            for i,hand_point in enumerate(left_hand_landmarks.landmark):
                xPos = int(hand_point.x*surface[0])
                yPos = int(hand_point.y*surface[1])
                cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),2)
                left_handF_points.append([xPos,yPos])       
                hand_left_nodes.append([(surface[0] - xPos),(yPos/3)+300])
                left_handF_mouse_points.append((surface[0] - xPos,yPos))
            if left_handF_points:
                mouse_x =  surface[0] - left_handF_points[8][0]
                mouse_y =  left_handF_points[8][1]
                finger_angle = hand_angle(left_handF_points)
                fist_left_flag,mousecontrol_flag = hand_pos(finger_angle)  

      
                
        # 獲取右手節點    
        right_hand_landmarks = holistic_result.right_hand_landmarks
        # 如果有偵測的右手節點        
        
        if right_hand_landmarks:
            mp_Draw.draw_landmarks(img,holistic_result.right_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
            right_handF_points = []
            for i,hand_point in enumerate(right_hand_landmarks.landmark):
                xPos = int(hand_point.x*surface[0])
                yPos = int(hand_point.y*surface[1])
                cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),2)
                right_handF_points.append((xPos,yPos))
                hand_right_nodes.append([(surface[0] - xPos),(yPos/3)+300])
            if right_handF_points:
               finger_angle = hand_angle(right_handF_points)
               fist_right_flag,temp = hand_pos(finger_angle)       

        if(fist_left_flag and fist_right_flag and shoulder_left_flag and shoulder_right_flag and defense_arm_left_flag and defense_arm_right_flag):
            defense_flag = 1
        else:
            defense_flag = 0
        # 前置動作 如果已經有握拳跟手有收縮        
        if(fist_left_flag and punch_arm_left_flag and armpit_left_flag): 
            step_left_flag = 1
        # 左揮拳動作
        if(step_left_flag and fist_left_flag and not punch_arm_left_flag and not armpit_left_flag):
            punch_left_flag = 1
            step_left_flag = 0
            
        # 前置動作 如果已經有握拳跟手有收縮         
        if(fist_right_flag and punch_arm_right_flag and armpit_right_flag): 
            step_right_flag = 1 
            
        # 右揮拳動作
        if(step_right_flag and fist_right_flag and not punch_arm_right_flag and not armpit_right_flag):
            punch_right_flag = 1 
            step_right_flag = 0
        # 反轉
        img = cv2.flip(img,1)
        cv2.putText(img,"fist: " + str(fist_left_flag) + ',' + str(fist_right_flag), (30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字 
        cv2.putText(img,'punch_arm: ' + str(punch_arm_left_flag) + ',' + str(punch_arm_right_flag), (30,110),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
        cv2.putText(img,'armpit: ' + str(armpit_left_flag) + ',' + str(armpit_right_flag), (30,140),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
        cv2.putText(img,'punch count: ' + str(punch_left_flag) + ',' + str(punch_right_flag), (30,170),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
        cv2.putText(img,'defense_arm: ' + str(defense_arm_left_flag) + ',' + str(defense_arm_right_flag), (30,200),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
        cv2.putText(img,'shoulder: ' + str(shoulder_left_flag) + ',' + str(shoulder_right_flag), (30,230),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
        cv2.putText(img,"defense_flag: " + str(defense_flag), (30,260),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
        cv2.putText(img,"thigh: " + str(thigh_flag), (30,290),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
        cv2.putText(img,"mouse: " + str(mouse_x) + ',' + str(mouse_y), (30,320),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
            # 顯示FPS
        showFps(img)
            # 開啟視窗
        cv2.imshow('img',img)
            # 結束條件
        if cv2.waitKey(1) == ord('q'):
            break
        if mousecontrol_flag == 0 and fist_left_flag == 0:                    
            pygame.mouse.set_pos(mouse_x,mouse_y)
            mousecontrol_break = 0
        if mousecontrol_flag == 1 and mousecontrol_break == 0:
            pyautogui.click()
            mousecontrol_break = 1
        #drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
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
            
            if event.type == pygame.KEYDOWN and (currentScene in level):
                if event.key ==pygame.K_z:
                    bosslife-=5
                    bosscolor=(255,0,0)
                    attack=1
                    useraction=2
                    
                    colortimeout=int(time.time())+0.5
                    actiontimeout=int(time.time()+1)
                if event.key ==pygame.K_x:
                    bosslife-=5
                    bosscolor=(255,0,0)
                    attack=2
                    useraction=1
                    colortimeout=int(time.time())+0.5
                    actiontimeout=int(time.time()+1)
                if event.key ==pygame.K_SPACE:
                    life-=1
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
                if event.key == pygame.K_DOWN:
                    destination[1]=0.9*surface[1]
                    distance=[destination[1]-userposition[1],2,2]
                    timeout=time.time()+0.5
                    thigh_effect_time=int(time.time())+1
                if event.key == pygame.K_q:
                    life+=1
            
                
        if thigh_flag==1:
            destination[1]=0.9*surface[1]
            distance=[destination[1]-userposition[1],2,2]
            timeout=time.time()+0.5
            thigh_flag=2
            thigh_effect_time=int(time.time())+1

        if punch_left_flag ==1:
            bosslife-=5
            bosscolor=(255,0,0)
            attack=1
            useraction=2
                    
            colortimeout=int(time.time())+0.5
            actiontimeout=int(time.time()+1)
            punch_left_flag=0

        if punch_right_flag ==1:
            bosslife-=5
            bosscolor=(255,0,0)
            attack=2
            useraction=1
                    
            colortimeout=int(time.time())+0.5
            actiontimeout=int(time.time()+1)
            punch_right_flag=0

        if bosslife==0 and (currentScene in level):
            gameovertimeout=int(time.time())+5
            visibility=0
            attType=0
            bosslife=-1
            gflag=1

        if defense_flag==1:action_start=1

        if defense_flag==0 and action_start==1:action_end=1

        if jump_flag ==1:
            destination[1]=0.6*surface[1]
            distance=[destination[1]-userposition[1],2,2]
            timeout=time.time()+0.5
            jump_flag=2
            jump_effect_time=int(time.time())+1

        #userposition[0] = surface[0]/2-surface[0]/16+hand_x
        userposition[0] = 0 + movePoint[0]
        #userposition[1] = surface[1]*0.75
        ## 隨時更新視窗大小 ##
        surface[0]=mainWindows.get_width()
        surface[1]=mainWindows.get_height()
        ## 隨時取得滑鼠位置 ##
        x, y = pygame.mouse.get_pos()
        createScene()

        pygame.display.update()