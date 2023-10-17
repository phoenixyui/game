import pygame
from pygame.locals import *
from pygame.locals import QUIT
import sys
import os
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
user_color=(0,255,0)
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
p11 = [0,0]
p12 = [0,0]
p15 = [0,0]
p16 = [0,0]
#####SQUATDOWN#####
thigh_flag = 0
jump_flag=0
jumpready_flag =0
jump_ready_keep =0
jumpready_flag=0
ctime_leg=0
jump_ctime=0
#######READY########
detect_point = [[0,0],[0,0],[0,0]]
a_color,b_color,c_color = 255,0,0
color_flag = 0



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
intro=["intro1","intro2","intro3","intro4","intro5","intro6"]
currentScene="menu"
tempScene=""
currentClick=[0,0,"menu"]
pygame.init()
xPos = 20
yPos = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (xPos, yPos)
mainWindows=pygame.display.set_mode((surface[0],surface[1]),RESIZABLE,32)
mainWindows.fill(0)
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
successtimes=0
hit_flag=0



if user==1:
    leftPunch=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\punch_left-1.jpg")
    rightPunch=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\punch_right-1.jpg")
    introduce0=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\introduce0.png").convert()
    introduce1=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\introduce1.png").convert()
    introduce2=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\introduce2.png").convert()
    introduce3=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\introduce3.png").convert()
    introduce4=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\introduce4.png").convert()
    introduce5=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\introduce5.png").convert()
    introduce6=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\introduce6.png").convert()
    stage0=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\stage0.png").convert()
    stage1=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\stage1.png").convert()
    stage2=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\stage2.png").convert()
    stage3=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\stage3.png").convert()
    stage4=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\stage4.png").convert()
    stage5=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\stage5.png").convert()
    mouseImage=pygame.image.load("C:\\Users\\User\\Desktop\\media\\game-main\\image\\mouse.png").convert()
elif user==2:
    leftPunch=pygame.image.load("image/punch_left-1.jpg")
    rightPunch=pygame.image.load("image/punch_right-1.jpg")
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
    mouseImage=pygame.image.load("image/mouse.png").convert()
    menuImage=pygame.image.load("image/menu_punch.png").convert()
    introbg=pygame.image.load("image/intro_bg.png").convert()
    level1bg=pygame.image.load("image/level1bg.png").convert()
    level2bg=pygame.image.load("image/level2bg.png").convert()
    level3bg=pygame.image.load("image/level3bg.png").convert()
    level4bg=pygame.image.load("image/level4bg.png").convert()
    ready1=pygame.image.load("image/ready1.png").convert()
    ready2=pygame.image.load("image/ready2.png").convert()
    ready3=pygame.image.load("image/ready3.png").convert()
    ready4=pygame.image.load("image/ready4.png").convert()
    ready5=pygame.image.load("image/ready5.png").convert()
    ready6=pygame.image.load("image/ready6.png").convert()

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
            windowssize(1)
            currentScene="normalMode"

    elif(x>=surface[0]/2 and y>surface[1]/4 and y<=surface[1]*2/4):
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]*2/4+startText.get_width()/2,surface[1]/2-startText.get_height()*1.2,300,66),width=1,border_radius=3)
        if event.type == pygame.MOUSEBUTTONUP:
            windowssize(1)
            currentScene="optional"

    elif(x>=surface[0]/2 and y>surface[1]*2/4 and y<=surface[1]*3/4):
        pygame.draw.rect(mainWindows,(255,0,0),(surface[0]*2/4+startText.get_width()/2,surface[1]*3/4-startText.get_height()*1.2,300,66),width=1,border_radius=3)
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.quit()
            sys.exit()

def optional():
    global currentScene,successtimes,flag,tempScene,color_flag
    mainWindows.blit(introduce0,[0,0])
    opFont=pygame.font.SysFont(None,80)
    returnText=opFont.render("return",True,(255,255,255))
    

    if(y<surface[1]/2):
        if(x<surface[0]/3):
            mainWindows.blit(introduce1,[0,0])
            if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="optional":
                windowssize(2)
                currentScene="ready"
                tempScene="intro1"
        if(x>=surface[0]/3 and x<surface[0]*2/3):
            mainWindows.blit(introduce2,[0,0])
            if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="optional":
                windowssize(2)
                currentScene="ready"
                tempScene="intro2"
        if(x>=surface[0]*2/3):
            mainWindows.blit(introduce3,[0,0])
            if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="optional":
                windowssize(2)
                currentScene="ready"
                tempScene="intro3"
    if(y>surface[1]/2 and y<surface[1]*0.9):
        if(x<surface[0]/3):
            mainWindows.blit(introduce4,[0,0])
            if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="optional":
                windowssize(2)
                currentScene="ready"
                tempScene="intro4"
        if(x>=surface[0]/3 and x<surface[0]*2/3):
            mainWindows.blit(introduce5,[0,0])
            if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="optional":
                windowssize(2)
                currentScene="ready"
                tempScene="intro5"
        if(x>=surface[0]*2/3):
            mainWindows.blit(introduce6,[0,0])
            if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="optional":
                windowssize(2)
                currentScene="ready"
                tempScene="intro6"
    mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.9))
    mainWindows.blit(mouseImage,[x,y])
    if(x>=surface[0]*0.05 and x<=surface[0]*0.05+returnText.get_width() and y>= surface[1]*0.9-5 and y<= surface[1]*0.9+returnText.get_height()):
        returnText=opFont.render("return",True,(255,0,0))
        mainWindows.blit(returnText,(surface[0]*0.05,surface[1]*0.9))
        if event.type == pygame.MOUSEBUTTONUP:
            windowssize(1)
            currentScene="menu"

def normalMode():
    global currentScene,flag,bossflag,height,attType,destination,distance,gflag,height2,tempScene,color_flag
    mainWindows.blit(stage0,[0,0])

    if(x>=surface[0]*3/8 and x<=surface[0]*5/8 and y>=surface[1]*2/6 and y<=surface[1]*4/6):
        mainWindows.blit(stage5,[0,0])
        if event.type == pygame.MOUSEBUTTONUP:
            windowssize(1)
            currentScene="menu"
    if(x<surface[0]*3/8 and y<=surface[1]/2):
        mainWindows.blit(stage1,[0,0])
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            windowssize(2)
            currentScene="ready"
            tempScene="level1"
    if(x>surface[0]*5/8 and y<surface[1]/2):
        mainWindows.blit(stage2,[0,0])
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            windowssize(2)
            currentScene="ready"
            tempScene="level2"
    if(x<surface[0]*3/8 and y>surface[1]/2):
        mainWindows.blit(stage3,[0,0])
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            windowssize(2)
            currentScene="ready"
            tempScene="level3"
    if(x>surface[0]*5/8 and y>surface[1]/2):
        mainWindows.blit(stage4,[0,0])
        if event.type == pygame.MOUSEBUTTONUP and currentClick[2]=="normalMode":
            windowssize(2)
            currentScene="ready"
            tempScene="level4"
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
    elif x==4:bosslife = 150
        
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

    if(x==1):mainWindows.blit(rightPunch,[surface[0]*3/4-rightPunch.get_width(),surface[1]/2]) 
    elif(x==2):mainWindows.blit(leftPunch,[surface[0]/4,surface[1]/2]) 

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
    global hitflag,user
    if flag==0:
        initlife(1)
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        flag=1
        bossposition=userposition
        gflag=0
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
    mainWindows.blit(level1bg,[0,0])
    
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
                windowssize(1)
                currentScene="normalMode"
                flag=0
                return
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
                windowssize(1)
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
        gflag=0
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
    mainWindows.blit(level2bg,[0,0])
    
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
                windowssize(1)
                currentScene="normalMode"
                flag=0
                return
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
                windowssize(1)
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
        gflag=0
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
            #print(zone)
            zone=5
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
    mainWindows.blit(level3bg,[0,0])
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
        # hand_left_nodes.clear()
        # hand_right_nodes.clear() 
        # body_nodes.clear() 
        timepass2=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass2>attTimeout2-recordtime):timepass2=attTimeout2-recordtime #如果大於timeout就設成timeout
        if(attTimeout2!=0):drawAttType2()
    elif (not(gflag)) and zone==5:
        all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear()   
        hitflag=0
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
                windowssize(1)
                currentScene="normalMode"
                flag=0
                return
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
                windowssize(1)
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
        hitflag=0  
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
            elif zone==5:
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
                        if (all_nodes[i][0]>2*surface[0]/5 or all_nodes[i][0]<surface[0]/5) :
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
                        if (all_nodes[i][0]>3*surface[0]/5 or all_nodes[i][0]<2*surface[0]/5) :
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
                        if (all_nodes[i][0]>4*surface[0]/5 or all_nodes[i][0]<3*surface[0]/5) :
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
                windowssize(1)
                currentScene="normalMode"
                flag=0
                return
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
                windowssize(1)
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
        gflag=0
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
    mainWindows.blit(level4bg,[0,0])
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
        defence -=3
        defencing=1
        recover=0
    if defence <=0:
        recover=1
        defencing=0
    if recover==1 or recover==2:
        defence+=2
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
        timepass2=round(time.time(),2)-recordtime #計算經過的時間
        if(timepass2>attTimeout2-recordtime):timepass2=attTimeout2-recordtime #如果大於timeout就設成timeout
        if(attTimeout2!=0):drawAttType2()
    elif (not(gflag)) and zone==5:
        all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
        hand_left_nodes.clear()
        hand_right_nodes.clear() 
        body_nodes.clear()   
        hitflag=0
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
                windowssize(1)
                currentScene="normalMode"
                flag=0
                return
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
                windowssize(1)
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
        hitflag=0  
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
                        if (all_nodes[i][0]>2*surface[0]/5 or all_nodes[i][0]<surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if not( (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5)):
                    #     life-=1
                    #     usercolor=(255,0,0) 
                if(selected[4]==2 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>3*surface[0]/5 or all_nodes[i][0]<2*surface[0]/5) :
                            defencefunc()
                            hitflag=1
                            break
                    all_nodes.clear() 
                    # if not((userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5)):
                    #     life-=1
                    #     usercolor=(255,0,0)
                if(selected[4]==3 and hitflag==0):
                    for i in range(len(all_nodes)):
                        if (all_nodes[i][0]>4*surface[0]/5 or all_nodes[i][0]<3*surface[0]/5) :
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
                windowssize(1)
                currentScene="normalMode"
                flag=0
                return
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
                windowssize(1)
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
        mainWindows.blit(ready1,[0,0])
        mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]*0.1-startText.get_width()/2 and x<=surface[0]*0.1+startText.get_width()/2
           and y>=surface[1]*0.1-startText.get_height()/2 and y<=surface[1]*0.1+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
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
            drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
            drawUser(useraction)
            hand_left_nodes.clear()
            hand_right_nodes.clear() 
            body_nodes.clear() 
        
        
        elif successtimes>=4:
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
                windowssize(1)
                currentScene="optional"
                flag=0
                return
        

def intro2():
    global successtimes,currentScene,visibility,attTimeout,bossflag,attType,recordtime,height,timepass,usercolor,colortimeout,flag,useraction,waittimeout,hitflag
    if flag==0:
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(ready2,[0,0])
        mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]*0.1-startText.get_width()/2 and x<=surface[0]*0.1+startText.get_width()/2
           and y>=surface[1]*0.1-startText.get_height()/2 and y<=surface[1]*0.1+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
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
            hitflag=0
        for i in range (0,3):
            image=pygame.image.load("./image/notsuccess.png")
            mainWindows.blit(image,[400+i*150,100])
        a=successtimes
        if a>3:a=3
        for j in range(0,a):
            image2=pygame.image.load("./image/success.png")
            mainWindows.blit(image2,[400+j*150,100])
        if successtimes<3:
            drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
            drawUser(useraction)
            hand_left_nodes.clear()
            hand_right_nodes.clear() 
            body_nodes.clear() 
        elif successtimes>=4:
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
                windowssize(1)
                currentScene="optional"
                flag=0
                return
        if attTimeout!=int(time.time()) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            
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
                if hitflag==0:successtimes+=1
                all_nodes.clear()
            elif(attType==2) and hitflag==0:
                for i in range(len(all_nodes)):
                    if all_nodes[i][0]>surface[0]/2 :
                        life-=1
                        usercolor=(255,0,0)
                        colortimeout=int(time.time())+0.5
                        hitflag=1
                        break
                if hitflag==0:successtimes+=1
                all_nodes.clear()
            
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
    global successtimes,currentScene,visibility,attTimeout,bossflag,attType,recordtime,height,timepass,usercolor,colortimeout,flag,useraction,waittimeout,jump_effect_time
    

    if flag==0:
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(ready4,[0,0])
        mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]*0.1-startText.get_width()/2 and x<=surface[0]*0.1+startText.get_width()/2
           and y>=surface[1]*0.1-startText.get_height()/2 and y<=surface[1]*0.1+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
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
            drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
            drawUser(useraction)
            hand_left_nodes.clear()
            hand_right_nodes.clear() 
            body_nodes.clear() 
        elif successtimes>=4:
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
                windowssize(1)
                currentScene="optional"
                flag=0
                return
        if attTimeout!=round(time.time(),1) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            
            timepass=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
            drawAttType(attType)
                
        else:     
            if(attType==4):
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

def intro3():
    global successtimes,currentScene,visibility,attTimeout,bossflag,attType,recordtime,height,timepass,usercolor,colortimeout,flag,useraction,waittimeout,thigh_effect_time
    if flag==0:
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(ready3,[0,0])
        mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]*0.1-startText.get_width()/2 and x<=surface[0]*0.1+startText.get_width()/2
           and y>=surface[1]*0.1-startText.get_height()/2 and y<=surface[1]*0.1+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
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
            drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
            drawUser(useraction)
            hand_left_nodes.clear()
            hand_right_nodes.clear() 
            body_nodes.clear() 
        elif successtimes>=4:
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
                windowssize(1)
                currentScene="optional"
                flag=0
                return
        if attTimeout!=round(time.time(),1) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            
            timepass=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
            drawAttType(attType)
                
        else:     
            if(attType==3):
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

def intro5():
    global successtimes,currentScene,visibility,attTimeout,bossflag,attType,recordtime,height,timepass,usercolor,colortimeout,flag,useraction,waittimeout
    global attTimeout2,selected,zone,hitflag,timepass2
    

    if flag==0:
        attTimeout=int(time.time())+2
        attTimeout2=0
        bossflag=1
        attType=0
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render("Got it!",True,(255,255,255))
        mainWindows.blit(ready5,[0,0])
        mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]*0.1-startText.get_width()/2 and x<=surface[0]*0.1+startText.get_width()/2
           and y>=surface[1]*0.1-startText.get_height()/2 and y<=surface[1]*0.1+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
            if event.type == pygame.MOUSEBUTTONUP:
                flag=1
    if flag!=0:
        
        mainWindows.blit(introbg,[0,0])
        gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        if bossflag ==0:
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
            
        for i in range (0,3):
            image=pygame.image.load("./image/notsuccess.png")
            mainWindows.blit(image,[400+i*150,100])
        a=successtimes
        if a>3:a=3
        for j in range(0,a):
            image2=pygame.image.load("./image/success.png")
            mainWindows.blit(image2,[400+j*150,100])
        if successtimes<3:
            drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
            drawUser(useraction)
            # hand_left_nodes.clear()
            # hand_right_nodes.clear() 
            # body_nodes.clear() 
        elif successtimes>=4:
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
                windowssize(1)
                currentScene="optional"
                flag=0
                return
        
        if attTimeout2!=int(time.time()) and (successtimes<=3) and zone==5:
            timepass2=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass2>attTimeout2-recordtime):timepass2=attTimeout2-recordtime #如果大於timeout就設成timeout
            if(attTimeout2!=0):drawAttType2()
        elif (successtimes<=3) and zone==5:
            all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
            
            if (selected[4]==0 and hitflag==0):
                for i in range(len(all_nodes)):
                    if all_nodes[i][0]<surface[0]/5 :
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
                        usercolor=(255,0,0)
                        colortimeout=int(time.time())+0.5
                        hitflag=1
                        break
                all_nodes.clear()
                # if userposition[0]+surface[0]/8>surface[0]*4/5:
                #     life-=1
                #     usercolor=(255,0,0) 
            if hitflag==0 :successtimes+=1
            hand_left_nodes.clear()
            hand_right_nodes.clear() 
            body_nodes.clear()
            zone=0      
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            timepass2=0

        if attTimeout!=round(time.time(),1) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            hand_left_nodes.clear()
            hand_right_nodes.clear() 
            body_nodes.clear() 
            timepass=round(time.time(),2)-recordtime #計算經過的時間
            if(timepass>attTimeout-recordtime):timepass=attTimeout-recordtime #如果大於timeout就設成timeout
            drawAttType(attType)
                
        elif attTimeout<=round(time.time(),1) and (successtimes<=3):  
            all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
            hand_left_nodes.clear()
            hand_right_nodes.clear() 
            body_nodes.clear()    
            if(attType==5):
                if zone!=5:
                    if (0 in selected):
                        for i in range(len(all_nodes)):
                            if all_nodes[i][0]<surface[0]/5 :
                                usercolor=(255,0,0)
                                colortimeout=int(time.time())+0.5
                                hitflag=1
                                break
                        
                        all_nodes.clear() 
                        # if userposition[0]<surface[0]/5:
                        #     life-=1
                        #     usercolor=(255,0,0) 
                    if (1 in selected):
                        for i in range(len(all_nodes)):
                            if (all_nodes[i][0]<2*surface[0]/5 and all_nodes[i][0]> surface[0]/5) :
                                usercolor=(255,0,0)
                                colortimeout=int(time.time())+0.5
                                hitflag=1
                                break
                        
                        all_nodes.clear() 
                        # if (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5):
                        #     life-=1
                        #     usercolor=(255,0,0) 
                    if (2 in selected):
                        for i in range(len(all_nodes)):
                            if (all_nodes[i][0]<3*surface[0]/5 and all_nodes[i][0]> 2*surface[0]/5) :
                                usercolor=(255,0,0)
                                colortimeout=int(time.time())+0.5
                                hitflag=1
                                break
                        
                        all_nodes.clear() 
                        # if (userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5):
                        #     life-=1
                        #     usercolor=(255,0,0) 
                    if (3 in selected):
                        for i in range(len(all_nodes)):
                            if (all_nodes[i][0]<4*surface[0]/5 and all_nodes[i][0]> 3*surface[0]/5) :
                                usercolor=(255,0,0)
                                colortimeout=int(time.time())+0.5
                                hitflag=1
                                break
                        
                        all_nodes.clear() 
                        # if (userposition[0]<4*surface[0]/5 and userposition[0]>3*surface[0]/5) or(userposition[0]+surface[0]/8>3*surface[0]/5 and userposition[0]+surface[0]/8<4*surface[0]/5):
                        #     life-=1
                        #     usercolor=(255,0,0) 
                    if (4 in selected):
                        for i in range(len(all_nodes)):
                            if (all_nodes[i][0]>4*surface[0]/5) :
                                usercolor=(255,0,0)
                                colortimeout=int(time.time())+0.5
                                hitflag=1
                                break
                        
                        all_nodes.clear() 
                        # if userposition[0]+surface[0]/8>surface[0]*4/5:
                        #     life-=1
                        #     usercolor=(255,0,0) 
                    if hitflag==0:successtimes+=1
                elif zone==5:
                    if(selected[4]==0 and hitflag==0):
                        for i in range(len(all_nodes)):
                            if (all_nodes[i][0]>surface[0]/5) :
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
                            if (all_nodes[i][0]>2*surface[0]/5 or all_nodes[i][0]<surface[0]/5) :
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
                            if (all_nodes[i][0]>3*surface[0]/5 or all_nodes[i][0]<2*surface[0]/5) :
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
                            if (all_nodes[i][0]>4*surface[0]/5 or all_nodes[i][0]<3*surface[0]/5) :
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
                                usercolor=(255,0,0)
                                colortimeout=int(time.time())+0.5
                                hitflag=1
                                break
                        all_nodes.clear() 
                        # if userposition[0]<surface[0]*4/5:
                        #     life-=1
                        #     usercolor=(255,0,0)
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            timepass2=0  
        if actiontimeout <= int(time.time()):    
            useraction=0

        if waittimeout == int(time.time()):
            hitflag=0
            waittimeout=0
            bossflag=0
        #print(userposition[1],destination[1],distance)
        usermove()

def intro6():
    global currentScene,bosslife,bossposition,life,winflag,bossflag,flag,hitflag
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
        mainWindows.blit(ready6,[0,0])
        mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
        mainWindows.blit(mouseImage,[x,y])
        if(x>=surface[0]*0.1-startText.get_width()/2 and x<=surface[0]*0.1+startText.get_width()/2
           and y>=surface[1]*0.1-startText.get_height()/2 and y<=surface[1]*0.1+startText.get_height()/2):
            startText=text.render("Got it!",True,(255,0,0))
            mainWindows.blit(startText,(surface[0]*0.1-startText.get_width()/2,surface[1]*0.1-startText.get_height()/2))
            if event.type == pygame.MOUSEBUTTONUP:
                flag=1
    if flag!=0:
        mainWindows.blit(introbg,[0,0])
        gameover=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        if bossflag ==0:
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
            drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
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
                windowssize(1)
                currentScene="optional"
                flag=0
                return

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
                
                zone=0
                attType=0
                waittimeout=int(time.time())+2 #攻擊間隔
                timepass=0
                timepass2=0

        if attTimeout!=round(time.time(),1) and (successtimes<=3):  #boss攻擊時間未結束 and 遊戲未結束
            all_nodes=hand_left_nodes+hand_right_nodes+body_nodes     
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
                            if (all_nodes[i][0]>2*surface[0]/5 or all_nodes[i][0]<surface[0]/5) :
                                defencefunc()
                                hitflag=1
                                break
                        all_nodes.clear() 
                        # if not( (userposition[0]<2*surface[0]/5 and userposition[0]>surface[0]/5) or(userposition[0]+surface[0]/8>surface[0]/5 and userposition[0]+surface[0]/8<2*surface[0]/5)):
                        #     life-=1
                        #     usercolor=(255,0,0) 
                    if(selected[4]==2 and hitflag==0):
                        for i in range(len(all_nodes)):
                            if (all_nodes[i][0]>3*surface[0]/5 or all_nodes[i][0]<2*surface[0]/5) :
                                defencefunc()
                                hitflag=1
                                break
                        all_nodes.clear() 
                        # if not((userposition[0]<3*surface[0]/5 and userposition[0]>2*surface[0]/5) or(userposition[0]+surface[0]/8>2*surface[0]/5 and userposition[0]+surface[0]/8<3*surface[0]/5)):
                        #     life-=1
                        #     usercolor=(255,0,0)
                    if(selected[4]==3 and hitflag==0):
                        for i in range(len(all_nodes)):
                            if (all_nodes[i][0]>4*surface[0]/5 or all_nodes[i][0]<3*surface[0]/5) :
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
            attType=0
            waittimeout=int(time.time())+2 #攻擊間隔
            timepass=0
            
        if actiontimeout <= int(time.time()):    
            useraction=0

        if waittimeout == int(time.time()):
            hitflag=0
            waittimeout=0
            bossflag=0
        #print(userposition[1],destination[1],distance)
        usermove()

def ready():
    global currentScene,tempScene,hand_left_nodes,hand_right_nodes,body_nodes,a_color,b_color,c_color,color_flag,waittimeout,successtimes,life
    global flag,bossflag,height,attType,destination,distance,gflag,height2
    mainWindows.fill((0,0,0))
    drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
    all_node=hand_left_nodes+hand_right_nodes+body_nodes
    a_color,b_color,c_color = 255,0,0
    for i in range(len(all_node)): 
        if i>200:
            color_flag=0
            break
        if all_node[i][1]<surface[1]*0.3 or all_node[i][0]>surface[0]/2:
            color_flag=0
            waittimeout=0
            break
        if all_node[len(all_node)-1][1]>surface[1]*0.3 and all_node[len(all_node)-1][0]<surface[0]/2 and color_flag==0:
            color_flag=1
            

    if color_flag==1:
        a_color,b_color,c_color = 0,255,0
        waittimeout=int(time.time())+3
    elif color_flag==2:a_color,b_color,c_color = 0,255,0
    elif color_flag==0:a_color,b_color,c_color = 255,0,0

    if waittimeout!=0 and color_flag==1:color_flag=2
    if waittimeout!=0 and waittimeout!=int(time.time()) and color_flag!=0:
        text=pygame.font.SysFont(None,60+(int((surface[0]-600)/25)))
        startText=text.render(str(int(waittimeout)-int(time.time())),True,(255,255,255))
        mainWindows.blit(startText,(surface[0]*0.5-startText.get_width()/2,surface[1]*0.2-startText.get_height()/2))
    elif waittimeout!=0 and waittimeout==int(time.time()):
        waittimeout=0
        flag=0
        bossflag=0
        height=surface[1]
        attType=0
        distance=[0,5,5]
        gflag=0
        destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
        color_flag=0
        successtimes=0
        currentScene=tempScene

    # if a_color == 255 and color_flag != -1: 
    #     color_flag = 0
    #     if a_color == 0 and color_flag != -1:
    #         color_flag = 1
    #     if color_flag == 0:
    #         a_color = a_color - 50
    #     if color_flag == 1:
    #         a_color = a_color + 50
    #     if (detect_point[0][1] > surface[1]/2 and detect_point[0][1] < surface[1] and detect_point[1][1] > surface[1]/2 and 
    #         detect_point[1][1] < surface[1] and detect_point[2][1] > surface[1]/2 and detect_point[2][1] < surface[1]):
            
    #         color_flag = -1
    #         a_color,b_color,c_color = 0,255,0  
    #     else:
    #         if color_flag == -1:
    #             a_color,b_color,c_color = 255,0,0  
    #             color_flag = 0
    pygame.draw.rect(mainWindows, (a_color,b_color,c_color), (0,surface[1]*0.3,surface[0]/2,surface[1]*0.7),5)  # 最後一個參數是外框寬度
    hand_left_nodes.clear()
    hand_right_nodes.clear() 
    body_nodes.clear() 
    all_node.clear()


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
    if currentScene == "level2":
        # windowssize(2)
        level2()
    if currentScene == "level3":
        # windowssize(2)
        level3()
    if currentScene == "level4":
        # windowssize(2)
        level4()
    if currentScene == "intro1":
        # windowssize(2)
        intro1()
    if currentScene == "intro2":
        # windowssize(2)
        intro2()
    if currentScene == "intro3":
        # windowssize(2)
        intro3()
    if currentScene == "intro4":
        # windowssize(2)
        intro4()
    if currentScene == "intro5":
        # windowssize(2)
        intro5()
    if currentScene == "intro6":
        # windowssize(2)
        intro6()
    if currentScene == "ready":
        # windowssize(2)
        ready()

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

    mousecontrol_flag = -1
    if f2 <= 50: #食指伸直
        mousecontrol_flag = 0
    if f2<=50 and f3<=50: #食指跟大拇指伸直
        mousecontrol_flag = 1 
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
    # 雙腳角度都要小於160度
    if t1 > 20 and t2 > 20:
        thigh_flag = 1
    else: 
        thigh_flag = 0
    return thigh_flag

def jump_ready(thigh_angle):
    global jumpready_flag
    global jump_ready_keep
    global jump_flag
    t1 = thigh_angle[0]
    t2 = thigh_angle[1]
    # 雙腳都要大於40
    if t1 > 40 and t2 > 40:
        jumpready_flag = 1
        jump_ready_keep = 1
        return 'jump ready'        
    else: 
        jumpready_flag = 0
        #jump_flag = 0
        
#辦定跳躍
def jump_pos(body_position):
    global jump_flag #是否跳躍 0沒有 1有
    global ctime_leg #蹲下時起跳預備位置
    global jump_ctime #蹲下時起跳預備時間
    global jump_ready_keep #保持這次預備直到起跳
    global jumpready_flag   
    if ctime_leg == 0:        
        ctime_leg = body_position[24][1]
        print("ctime_leg:={}".format(ctime_leg))
        jump_ctime = time.time()
    if jumpready_flag == 0 and jump_ready_keep == 1:
        ptime_leg = body_position[24][1] #起跳位置
        print("ptime_leg:={}".format(ptime_leg))
        jump_ptime = time.time() #起跳時間
        if (jump_ptime - jump_ctime) != 0 and ctime_leg > ptime_leg:            
            speed = (ctime_leg - ptime_leg)/(jump_ptime - jump_ctime)
            print("speed = {}".format(speed))
            if speed>=30: #速度可改 
                jump_flag = 1
                jump_ready_keep = 0
                jumpready_flag = 0
                ctime_leg = 0
                ptime_leg = 0
                jump_ptime= 0
                jump_ctime= 0
                print("jump")                
                return 'jump'
            else:
                jump_flag = 0
                jump_ready_keep = 0
                jumpready_flag = 0
                ctime_leg = 0
                ptime_leg = 0
                jump_ptime=0
                jump_ctime=0
                return ''
        else :
            jump_flag = 0
            jump_ready_keep = 0
            jumpready_flag = 0
            ctime_leg = 0
            ptime_leg = 0
            jump_ptime=0
            jump_ctime=0
            return ''
    else:
        jump_flag = 0
        """
        ctime_leg = 0
        jump_ctime = 0
        """
        return ''  
   
def drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes):
 # 繪出左手的節點到pygame
    for i in range(len(hand_left_nodes)):
        pygame.draw.circle(mainWindows, red, (int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])), ball_radius)
        if(i==0):
            pygame.draw.line(mainWindows,user_color,(int(hand_left_nodes[0][0]),int(hand_left_nodes[0][1])),(int(hand_left_nodes[1][0]),int(hand_left_nodes[1][1])),2) 
            pygame.draw.line(mainWindows,user_color,(int(hand_left_nodes[0][0]),int(hand_left_nodes[0][1])),(int(hand_left_nodes[5][0]),int(hand_left_nodes[5][1])),2) 
            pygame.draw.line(mainWindows,user_color,(int(hand_left_nodes[0][0]),int(hand_left_nodes[0][1])),(int(hand_left_nodes[17][0]),int(hand_left_nodes[17][1])),2) 
        if(i == 5 or i == 9 or i == 13):
            pygame.draw.line(mainWindows,user_color,(int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])),(int(hand_left_nodes[i+4][0]),int(hand_left_nodes[i+4][1])),2) 
        if(i%4 != 0 and i < len(hand_left_nodes)-1):
            pygame.draw.line(mainWindows,user_color,(int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])),(int(hand_left_nodes[i+1][0]),int(hand_left_nodes[i+1][1])),2) 
    # hand_left_nodes.clear()  
    

    for i in range(len(hand_right_nodes)):
        pygame.draw.circle(mainWindows, red, (int(hand_right_nodes[i][0]),int(hand_right_nodes[i][1])), ball_radius)
        if(i==0):
            pygame.draw.line(mainWindows,user_color,(int(hand_right_nodes[0][0]),int(hand_right_nodes[0][1])),(int(hand_right_nodes[1][0]),int(hand_right_nodes[1][1])),2) 
            pygame.draw.line(mainWindows,user_color,(int(hand_right_nodes[0][0]),int(hand_right_nodes[0][1])),(int(hand_right_nodes[5][0]),int(hand_right_nodes[5][1])),2) 
            pygame.draw.line(mainWindows,user_color,(int(hand_right_nodes[0][0]),int(hand_right_nodes[0][1])),(int(hand_right_nodes[17][0]),int(hand_right_nodes[17][1])),2) 
        if(i == 5 or i == 9 or i == 13):
            pygame.draw.line(mainWindows,user_color,(int(hand_right_nodes[i][0]),int(hand_right_nodes[i][1])),(int(hand_right_nodes[i+4][0]),int(hand_right_nodes[i+4][1])),2) 
        if(i%4 != 0 and i < len(hand_right_nodes)-1):
            pygame.draw.line(mainWindows,user_color,(int(hand_right_nodes[i][0]),int(hand_right_nodes[i][1])),(int(hand_right_nodes[i+1][0]),int(hand_right_nodes[i+1][1])),2) 
    # hand_right_nodes.clear()  

    for i in range(len(body_nodes)):
        pygame.draw.circle(mainWindows, red, (int(body_nodes[i][0]),int(body_nodes[i][1])), ball_radius)
        if((i >= 11 and i <= 14) or (i >= 23 and i <= 26)):
            pygame.draw.line(mainWindows,user_color,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+2][0]),int(body_nodes[i+2][1])),2) 
        if(i == 11 or i == 23):
            pygame.draw.line(mainWindows,user_color,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+1][0]),int(body_nodes[i+1][1])),2) 
        if(i == 11 or i == 12):
            pygame.draw.line(mainWindows,user_color,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+12][0]),int(body_nodes[i+12][1])),2) 
        if(i >= 27 and i <=30):
            pygame.draw.line(mainWindows,user_color,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+2][0]),int(body_nodes[i+2][1])),2)
        if(i == 28 or i == 27):
            pygame.draw.line(mainWindows,user_color,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+4][0]),int(body_nodes[i+4][1])),2)
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
            body_points = []
            # 印出點的數字
            for i,lm in enumerate(body_landmarks.landmark):
                xPos = int(lm.x*surface[0])
                yPos = int(lm.y*surface[1])
                cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),2)
                body_points.append((xPos,yPos))
                body_nodes.append([(surface[0] - xPos),(yPos/3)+300])
                if i == 0 : detect_point[0] = [(surface[0] - xPos),(yPos/3)+300]
                if i == 27: detect_point[1] = [(surface[0] - xPos),(yPos/3)+300]
                if i == 28: detect_point[2] = [(surface[0] - xPos),(yPos/3)+300]
               
                if i == 11: p11 = [xPos,yPos]
                if i == 15: p15 = [xPos,yPos]
                if i == 12: p12 = [xPos,yPos]
                if i == 16: p16 = [xPos,yPos]
            if body_points:
                # 肩膀角度
                sh_angle = shoulder_angle(body_points)
                shoulder_left_flag,shoulder_right_flag = shoulder_pos(sh_angle)    
                # 手臂角度    
                ar_angle = arm_angle(body_points) 
                defense_arm_left_flag,defense_arm_right_flag = arm_pos(ar_angle,100,100)
                punch_arm_left_flag,punch_arm_right_flag = arm_pos(ar_angle,150,150)
                # 腋下角度    
                armp_angle = armpit_angle(body_points)
                armpit_left_flag,armpit_right_flag = armpit_pos(armp_angle)   
                # 大腿角度      
                th_angle = thigh_angle(body_points)
                thigh_flag = thigh_pos(th_angle)          
                jump_ready_text = jump_ready(th_angle)                

            if jumpready_flag == 0 and jump_ready_keep ==0:
                jump_flag = 0
                jump_text = ''            
            elif jumpready_flag == 1 or jump_ready_keep == 1:      
                jump_text = jump_pos(body_points)   
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
                # cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),2)
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
                # cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),2)
                right_handF_points.append((xPos,yPos))
                hand_right_nodes.append([(surface[0] - xPos),(yPos/3)+300])
            if right_handF_points:
                mouse_x =  surface[0] - right_handF_points[8][0]
                mouse_y =  right_handF_points[8][1]
                finger_angle = hand_angle(right_handF_points)
                fist_right_flag,mousecontrol_flag = hand_pos(finger_angle)       

        if(fist_left_flag and fist_right_flag and shoulder_left_flag and shoulder_right_flag and defense_arm_left_flag and defense_arm_right_flag):
            defense_flag = 1
        else:
            defense_flag = 0
        # 前置動作 如果已經有握拳跟手有收縮        
        if(fist_left_flag and punch_arm_left_flag and armpit_left_flag): 
            step_left_flag = 1
        # 左揮拳動作
        if(step_left_flag and fist_left_flag and not punch_arm_left_flag and p15[0] < p11[0] and p15[1] + 50 > p11[1] and p15[1] - 50 < p11[1]):
            punch_left_flag = 1
            step_left_flag = 0
            
        # 前置動作 如果已經有握拳跟手有收縮         
        if(fist_right_flag and punch_arm_right_flag and armpit_right_flag): 
            step_right_flag = 1 
            
        # 右揮拳動作
        if(step_right_flag and fist_right_flag and not punch_arm_right_flag and p16[0] > p12[0] and p16[1] + 50 > p12[1] and p16[1] - 50 < p12[1]):
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
        if mousecontrol_flag == 0 and fist_left_flag == 0 and flag!=1:                    
            pygame.mouse.set_pos(mouse_x,mouse_y)
            mousecontrol_break = 0
        if mousecontrol_flag == 1 and mousecontrol_break == 0 and flag!=1:
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
                    successtimes+=1  
                    colortimeout=int(time.time())+0.5
                    actiontimeout=int(time.time()+1)
                if event.key ==pygame.K_x:
                    bosslife-=5
                    bosscolor=(255,0,0)
                    attack=2
                    useraction=1
                    successtimes+=1  
                    colortimeout=int(time.time())+0.5
                    actiontimeout=int(time.time()+1)
                if event.key ==pygame.K_SPACE:
                    life-=1
                    if life<=0:
                        flag=0
                        windowssize(1)
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
                if event.key == pygame.K_l:
                    successtimes+=1
            
        if jump_flag==1:
            jump_effect_time=int(time.time())+1        
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
            if currentScene=="intro1":successtimes+=1       
            colortimeout=int(time.time())+0.5
            actiontimeout=int(time.time()+1)
            punch_left_flag=0
        if punch_right_flag ==1:
            bosslife-=5
            bosscolor=(255,0,0)
            attack=2
            useraction=1
            if currentScene=="intro1":successtimes+=1          
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
        if successtimes==3 and (currentScene in intro):
            gameovertimeout=int(time.time())+8
            visibility=0
            successtimes+=1
        #userposition[0] = surface[0]/2-surface[0]/16+hand_x
        userposition[0] = 0 + movePoint[0]
        #userposition[1] = surface[1]*0.75
        ## 隨時更新視窗大小 ##
        surface[0]=mainWindows.get_width()
        surface[1]=mainWindows.get_height()
        #print(visibility)
        ## 隨時取得滑鼠位置 ##
        x, y = pygame.mouse.get_pos()
        createScene()

        pygame.display.update()