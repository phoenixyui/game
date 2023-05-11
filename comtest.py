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
## 初始化 ##
mp_Draw = mp.solutions.drawing_utils # mediapipe 繪圖方法
mpd_rawing_styles = mp.solutions.drawing_styles # mediapipe 繪圖樣式
mp_holistic = mp.solutions.holistic # mediapipe 全身偵測方法
holistic = mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) 

srceen_width = 1280
srceen_height = 720

pTime = 0
cTime = 0
thigh_text = ''
thigh_flag = 0
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
bossposition=[0,0,0,0]
userposition=[surface[0]/2-surface[0]/16,surface[1]*0.75,surface[0]/8,surface[1]*0.25]
destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
distance=[0,5,5] ## 0 左 1 右 2 上 3 下 4 後
clock = pygame.time.Clock()
timeout=0
attTimeout=0
attType=0
attack=0
height=0
waittimeout=0
gameovertimeout=0
colortimeout=0
visibility=0
gflag=0
timepass=0
recordtime=0
usercolor=(255,255,255)
bosscolor=(0,0,0)
useraction=0 
actiontimeout=0
leftPunch=pygame.image.load("image/punch_left-1.jpg")
rightPunch=pygame.image.load("image/punch_right-1.jpg")

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
    
    pygame.draw.rect(mainWindows,(255,255,255),(3.5*surface[0]/8,surface[1]/6,surface[0]/6,surface[0]/6),border_radius=4)
    pygame.draw.rect(mainWindows,(0,0,0),(3.5*surface[0]/8+surface[0]/160,surface[1]/6+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4)
    
    pygame.draw.rect(mainWindows,(255,255,255),(6*surface[0]/8,surface[1]/6,surface[0]/6,surface[0]/6),border_radius=4)
    pygame.draw.rect(mainWindows,(0,0,0),(6*surface[0]/8+surface[0]/160,surface[1]/6+surface[1]/120,surface[0]/6-surface[0]/60,surface[0]/6-surface[0]/60),border_radius=4)

    normalModeFont2=pygame.font.SysFont(None,int(surface[0]/5))
    oneText=normalModeFont2.render("1",True,(255,255,255))
    mainWindows.blit(oneText,(surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))
    
    twoText=normalModeFont2.render("2",True,(255,255,255))
    mainWindows.blit(twoText,(3.5*surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))

    threeText=normalModeFont2.render("3",True,(255,255,255))
    mainWindows.blit(threeText,(6*surface[0]/8+surface[0]/25,surface[1]/6+surface[1]/40))

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
            attType=0
            distance=[0,5,5]
            gflag=0
            destination=[surface[0]/2-surface[0]/16,surface[1]*0.75]
            currentScene="level3"

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
        
def usermove():
    global currentScene,bosslife,life,thigh_flag,winflag,bossflag,flag,userposition,destination,distance,attTimeout,attType,waittimeout,height,gameovertimeout,visibility,gflag,timepass,recordtime
    if round(time.time(),1) == round(timeout,1):#這邊以下都是角色移動
        if(distance[1]==0):
            distance=[surface[0]/2-surface[0]/4,5,0]
        elif(distance[1]==1):
            distance=[0-surface[0]/2+surface[0]/4,5,1]
        elif(distance[1]==2):
            distance=[surface[1]*0.15,5,2]
            thigh_flag=0
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
    if flag==0:
        initlife(2)
        attTimeout=int(time.time())+2
        bossflag=1
        attType=0
        flag=1
        bossposition=userposition
        ##以上是進遊戲後只會做一次的初始化##
    if bossflag ==0:
        attType=4
        if attType==3 or attType==4:
            attTimeout=int(time.time())+1.5
        else:
            attTimeout=int(time.time())+3
        
        recordtime=int(time.time())
        height=surface[1]
        bossflag=1
        timepass=0
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
                colortimeout=int(time.time())+0.5
        elif(attType==2):
            if (userposition[0]+surface[0]/8)>surface[0]/2 :
                life-=1
                usercolor=(255,0,0)
                colortimeout=int(time.time())+0.5
        elif(attType==3):
            if(userposition[1]+5.5*userposition[2]/3)>surface[1]:
                life-=1
                usercolor=(255,0,0)
                colortimeout=int(time.time())+0.5
        elif(attType==4):
            if(userposition[1])<surface[1]*0.816:
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
    return
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
    if currentScene == "level2":
        level2()
    if currentScene == "level3":
        level3()
# 根據兩點的座標，計算角度
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
    global thigh_flag
    t1 = thigh_angle[0]
    t2 = thigh_angle[1]
    # 雙腳都要大於50
    if t1 > 50 and t2 > 50:
        thigh_flag = 1
        return 'squat down'
    else: 
        thigh_flag = 0
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
    while True:
        clock.tick(60)
        ret,img = cap.read()
        if not ret:
            print("Cannot recvive frame")
            break
        img = cv2.resize(img,(srceen_width,srceen_height))
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # 使用Holistic模型進行處理
        holistic_result = holistic.process(imgRGB)
        # 獲取身體節點的位置
        body_landmarks = holistic_result.pose_landmarks
        # 如果有偵測到身體節點
        if body_landmarks:            
            mp_Draw.draw_landmarks(img,body_landmarks,mp_holistic.POSE_CONNECTIONS)            
            thigh_points = []            
            # 印出點的數字
            for i,lm in enumerate(body_landmarks.landmark):
                if i == 0:
                    movePoint = [surface[0] - int(lm.x*surface[0]),int(lm.y*surface[1])]
                xPos = int(lm.x*srceen_width)
                yPos = int(lm.y*srceen_height)   
                cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),2)  
                thigh_points.append((xPos,yPos))
            if thigh_points:
                th_angle = thigh_angle(thigh_points)
                thigh_text = thigh_pos(th_angle)
                        
        img = cv2.flip(img,1)
        cv2.putText(img,thigh_text, (30,140),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
            # 顯示FPS
        showFps(img)
            # 開啟視窗
        cv2.imshow('img',img)
            # 結束條件
        if cv2.waitKey(1) == ord('q'):
            break
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
            
            if event.type == pygame.KEYDOWN and (currentScene == "level1" or currentScene == "level2"):
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
                if event.key == pygame.K_q:
                    life+=1

            if bosslife==0 and currentScene=="level1":
                gameovertimeout=int(time.time())+8
                visibility=0
                attType=0
                bosslife-=1
                gflag=1
                
        #print(thigh_flag)
        if thigh_flag==1:
            destination[1]=0.9*surface[1]
            distance=[destination[1]-userposition[1],2,2]
            timeout=time.time()+0.5
            thigh_flag=2
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