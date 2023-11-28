import cv2
import mediapipe as mp
import math
import time
import cv2
import pygame
mp_Draw = mp.solutions.drawing_utils # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles # mediapipe 繪圖樣式
mp_holistic = mp.solutions.holistic # mediapipe 全身偵測方法
holistic = mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) 

screen_width = 1200
screen_height = 720
# 初始化Pygame

pygame.init()
# 建立視窗
screen = pygame.display.set_mode((screen_width, screen_height))
# 設定遊戲名稱
pygame.display.set_caption("Random Ball")
# 定義顏色
red = (255, 0, 0)

# 定義球的半徑和顏色
ball_radius = 2
pTime = 0
cTime = 0
#####共用#####
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
#####JUMP#####

# 顯示FPS
def showFps(img):
    global cTime,pTime
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,f"FPS:{int(fps)}",(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)


def drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes):
    # 繪出左手的節點到pygame
    for i in range(len(hand_left_nodes)):
        pygame.draw.circle(screen, red, (int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])),ball_radius)
        if(i==0):
            pygame.draw.line(screen,red,(int(hand_left_nodes[0][0]),int(hand_left_nodes[0][1])),(int(hand_left_nodes[1][0]),int(hand_left_nodes[1][1]))) 
            pygame.draw.line(screen,red,(int(hand_left_nodes[0][0]),int(hand_left_nodes[0][1])),(int(hand_left_nodes[5][0]),int(hand_left_nodes[5][1]))) 
            pygame.draw.line(screen,red,(int(hand_left_nodes[0][0]),int(hand_left_nodes[0][1])),(int(hand_left_nodes[17][0]),int(hand_left_nodes[17][1]))) 
        if(i == 5 or i == 9 or i == 13):
            pygame.draw.line(screen,red,(int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])),(int(hand_left_nodes[i+4][0]),int(hand_left_nodes[i+4][1]))) 
        if(i%4 != 0 and i < len(hand_left_nodes)-1):
            pygame.draw.line(screen,red,(int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])),(int(hand_left_nodes[i+1][0]),int(hand_left_nodes[i+1][1]))) 
    hand_left_nodes.clear()    
    # 繪出右手的節點到pygame
    for i in range(len(hand_right_nodes)):
        pygame.draw.circle(screen, red, (int(hand_right_nodes[i][0]),int(hand_right_nodes[i][1])), ball_radius)
        if(i==0):
            pygame.draw.line(screen,red,(int(hand_right_nodes[0][0]),int(hand_right_nodes[0][1])),(int(hand_right_nodes[1][0]),int(hand_right_nodes[1][1]))) 
            pygame.draw.line(screen,red,(int(hand_right_nodes[0][0]),int(hand_right_nodes[0][1])),(int(hand_right_nodes[5][0]),int(hand_right_nodes[5][1]))) 
            pygame.draw.line(screen,red,(int(hand_right_nodes[0][0]),int(hand_right_nodes[0][1])),(int(hand_right_nodes[17][0]),int(hand_right_nodes[17][1]))) 
        if(i == 5 or i == 9 or i == 13):
            pygame.draw.line(screen,red,(int(hand_right_nodes[i][0]),int(hand_right_nodes[i][1])),(int(hand_right_nodes[i+4][0]),int(hand_right_nodes[i+4][1]))) 
        if(i%4 != 0 and i < len(hand_right_nodes)-1):
            pygame.draw.line(screen,red,(int(hand_right_nodes[i][0]),int(hand_right_nodes[i][1])),(int(hand_right_nodes[i+1][0]),int(hand_right_nodes[i+1][1]))) 
    hand_right_nodes.clear()  
    # 繪出身體的節點到pygame
    for i in range(len(body_nodes)):
        pygame.draw.circle(screen, red, (int(body_nodes[i][0]),int(body_nodes[i][1])),ball_radius)
        if((i >= 11 and i <= 14) or (i >= 23 and i <= 26)):
        # if((i >= 23 and i <= 26)):
            pygame.draw.line(screen,(255,255,255),(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+2][0]),int(body_nodes[i+2][1]))) 
        if(i == 11 or i == 23):
            pygame.draw.line(screen,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+1][0]),int(body_nodes[i+1][1]))) 
        if(i == 11 or i == 12):
            pygame.draw.line(screen,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+12][0]),int(body_nodes[i+12][1]))) 
        if(i >= 27 and i <=30):
            pygame.draw.line(screen,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+2][0]),int(body_nodes[i+2][1])))
        if(i == 28 or i == 27):
            pygame.draw.line(screen,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+4][0]),int(body_nodes[i+4][1])))
    body_nodes.clear()

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open Camera")
        exit()
    hand_left_nodes = []
    hand_right_nodes = []
    body_nodes = []
    while True:
        ret,img = cap.read()
        if not ret:
            print("Cannot recvive frame")
            break
        img = cv2.resize(img,(screen_width,screen_height))
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # 使用Holistic模型進行處理
        holistic_result = holistic.process(imgRGB)
        # 獲取身體節點的位置
        body_landmarks = holistic_result.pose_landmarks

        # 如果有偵測到身體節點
        if body_landmarks:
            mp_Draw.draw_landmarks(img,body_landmarks,mp_holistic.POSE_CONNECTIONS)

            # 印出點的數字
            for i,lm in enumerate(body_landmarks.landmark):
                xPos = int(lm.x*screen_width)
                yPos = int(lm.y*screen_height)
                cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),2)
                body_nodes.append([(screen_width - xPos),(yPos/3)+300])

           
        # 獲取左手節點
        left_hand_landmarks = holistic_result.left_hand_landmarks
        # 如果有偵測到左手節點
        if left_hand_landmarks:
            mp_Draw.draw_landmarks(img,holistic_result.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
            left_handF_points = []
            for i,hand_point in enumerate(left_hand_landmarks.landmark):
                xPos = int(hand_point.x*screen_width)
                yPos = int(hand_point.y*screen_height)
                # cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),2)
                
                left_handF_points.append([xPos,yPos])  
                hand_left_nodes.append([(screen_width - xPos),(yPos/3)+300])

        # 獲取右手節點    
        right_hand_landmarks = holistic_result.right_hand_landmarks
        # 如果有偵測的右手節點        
        
        if right_hand_landmarks:
            mp_Draw.draw_landmarks(img,holistic_result.right_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
            right_handF_points = []
            for i,hand_point in enumerate(right_hand_landmarks.landmark):
                xPos = int(hand_point.x*screen_width)
                yPos = int(hand_point.y*screen_height)
                # cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),2)
                right_handF_points.append((xPos,yPos))
                hand_right_nodes.append([(screen_width - xPos),(yPos/3)+300])
        
        # 反轉
        img = cv2.flip(img,1)
        # cv2.putText(img,'fist: ' + str(fist_left_flag) + ',' + str(fist_right_flag), (30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字 
        # 顯示FPS
        showFps(img)
        # 開啟視窗
        cv2.imshow('img',img)
        # 結束條件
        if cv2.waitKey(1) == ord('q'):
            break
        screen.fill((0,0,0))
        # 繪出身體的節點到pygame
        drawUserbody(hand_left_nodes,hand_right_nodes,body_nodes)
        # 檢查事件
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                pygame.quit()
        # 更新畫面
        pygame.display.update()
        # 設定遊戲速度
        pygame.time.Clock().tick(60)    
    