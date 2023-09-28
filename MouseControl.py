import cv2
import mediapipe as mp
import math
import pygame
import pyautogui

mp_Draw = mp.solutions.drawing_utils # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles # mediapipe 繪圖樣式
mp_holistic = mp.solutions.holistic # mediapipe 全身偵測方法
holistic = mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) 

pTime = 0
cTime = 0


hand_text = ''
# 初始化Pygame
pygame.init()
circle_color=(255,0,0)
# 定義視窗大小
screen_width = 800
screen_height = 600

# 建立視窗
screen = pygame.display.set_mode((screen_width, screen_height))

# 設定遊戲名稱
pygame.display.set_caption("mouse test")

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
# 根據手指角度的串列內容，返回對應的手勢名稱
def hand_pos(finger_angle):
    f1 = finger_angle[0]   # 大拇指角度
    f2 = finger_angle[1]   # 食指角度
    f3 = finger_angle[2]   # 中指角度
    f4 = finger_angle[3]   # 無名指角度
    f5 = finger_angle[4]   # 小拇指角度
    mousecontrol_flag = 0
    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f3>=50 and f4>=50 and f5>=50:
        mousecontrol_flag = 0        
    elif f4>=50 and f5>=50:#食指跟大拇指伸直
        mousecontrol_flag = 1  
    else:
        mousecontrol_flag = -1 

    return mousecontrol_flag
if __name__ == '__main__':
    # 讀取攝影鏡頭
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open Camera")
        exit()
    # 遊戲迴圈
    mousecontrol_break = 0
    while True:
        ret,img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img,(screen_width,screen_height))
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        holistic_result = holistic.process(imgRGB)
        hand_left_landmarks = holistic_result.left_hand_landmarks
        mousecontrol_flag = -1
        mouse_x,mouse_y = 0,0
        if hand_left_landmarks:
            # 找出左手的線跟點
            mp_Draw.draw_landmarks(img,hand_left_landmarks,mp_holistic.HAND_CONNECTIONS)
            hand_left_nodes = []
            for i,hand_point in enumerate(hand_left_landmarks.landmark):
                xPos = int(hand_point.x*screen_width)
                yPos = int(hand_point.y*screen_height)
                cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),2)
                hand_left_nodes.append([xPos,yPos])
            
            if hand_left_nodes:
                mouse_x =  hand_left_nodes[8][0]
                mouse_x = screen_width - mouse_x
                mouse_y =  hand_left_nodes[8][1]
                #print(mouse_x,mouse_y)       
                ha_angle = hand_angle(hand_left_nodes)
                mousecontrol_flag = hand_pos(ha_angle)
        
        img = cv2.flip(img, 1)  
        cv2.putText(img,hand_text, (30,140),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字                  
        cv2.imshow("WebCam", img)
        if cv2.waitKey(1) == ord('q'):
            break

        screen.fill((0,0,0))
        pygame.draw.circle(screen, circle_color, (400,300), 5)
        
        if mousecontrol_flag == 0:                    
            pygame.mouse.set_pos(mouse_x,mouse_y)
            mousecontrol_break = 0
        if mousecontrol_flag == 1 and mousecontrol_break == 0:
            pyautogui.click()
            mousecontrol_break = 1
            
        
        # 檢查事件
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 檢測滑鼠點擊事件
                if circle_color == (255, 0, 0):  # 如果圓球是紅色
                    circle_color = (0, 0, 255)  # 改變圓球顏色為藍色
                else:
                    circle_color = (255, 0, 0)  # 如果圓球是藍色，改變顏色為紅色            
        # 更新畫面
        pygame.display.update()
        # 設定遊戲速度
        pygame.time.Clock().tick(60)    
    