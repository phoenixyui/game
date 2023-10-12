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

screen_width = 800
screen_height = 600
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
p11 = [0,0]
p15 = [0,0]
p12 = [0,0]
p16 = [0,0]
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
    return fist_flag
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
        pygame.draw.circle(screen, red, (int(hand_left_nodes[i][0]),int(hand_left_nodes[i][1])), ball_radius)
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
        pygame.draw.circle(screen, red, (int(body_nodes[i][0]),int(body_nodes[i][1])), ball_radius)
        if((i >= 11 and i <= 14) or (i >= 23 and i <= 26)):
            pygame.draw.line(screen,red,(int(body_nodes[i][0]),int(body_nodes[i][1])),(int(body_nodes[i+2][0]),int(body_nodes[i+2][1]))) 
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

            body_points = []
            # 印出點的數字
            for i,lm in enumerate(body_landmarks.landmark):
                xPos = int(lm.x*screen_width)
                yPos = int(lm.y*screen_height)
                # cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),2)
                body_points.append((xPos,yPos))   
                body_nodes.append([(screen_width - xPos),(yPos/3)+300])
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
            if left_handF_points:
               finger_angle = hand_angle(left_handF_points)
               fist_left_flag = hand_pos(finger_angle)  
 
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
            if right_handF_points:
               finger_angle = hand_angle(right_handF_points)
               fist_right_flag = hand_pos(finger_angle)       

        if(fist_left_flag and fist_right_flag and shoulder_left_flag and shoulder_right_flag and defense_arm_left_flag and defense_arm_right_flag):
            defense_flag = 1
        else:
            defense_flag = 0
        # 前置動作 如果已經有握拳跟手有收縮        
        if(fist_left_flag and punch_arm_left_flag and armpit_left_flag): 
            step_left_flag = 1
        # 左揮拳動作
        if(step_left_flag and fist_left_flag and not punch_arm_left_flag and p15[0] < p11[0] and p15[1] + 50 > p11[1] and p15[1] - 50 < p11[1]):
            punch_left_flag += 1
            step_left_flag = 0
            
        # 前置動作 如果已經有握拳跟手有收縮         
        if(fist_right_flag and punch_arm_right_flag and armpit_right_flag): 
            step_right_flag = 1 
            
        # 右揮拳動作
        if(step_right_flag and fist_right_flag and not punch_arm_right_flag and p16[0] > p12[0] and p16[1] + 50 > p12[1] and p16[1] - 50 < p12[1]):
            punch_right_flag += 1 
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
    