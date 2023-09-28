import cv2
import mediapipe as mp
import math
import time

mp_Draw = mp.solutions.drawing_utils # mediapipe 繪圖方法
mpd_rawing_styles = mp.solutions.drawing_styles # mediapipe 繪圖樣式
mp_holistic = mp.solutions.holistic # mediapipe 全身偵測方法
holistic = mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) 

srceen_width = 1280
srceen_height = 720

pTime = 0
cTime = 0
thigh_flag = 0

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
    t1 = thigh_angle[0]
    t2 = thigh_angle[1]
    # 雙腳都要大於50
    if t1 > 50 and t2 > 50:
        thigh_flag = 1
    else: 
        thigh_flag = 0
    return thigh_flag
# 顯示FPS
def showFps(img):
    global cTime,pTime
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,f"FPS:{int(fps)}",(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)

if __name__ == '__main__':    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open Camera")
        exit()
    while True:
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
                xPos = int(lm.x*srceen_width)
                yPos = int(lm.y*srceen_height)   
                cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),2)  
                thigh_points.append((xPos,yPos))
            if thigh_points:
                th_angle = thigh_angle(thigh_points)
                thigh_flag = thigh_pos(th_angle)
                       
        img = cv2.flip(img,1)
        print(thigh_flag)
        cv2.putText(img,"thigh: " + str(thigh_flag), (30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
        # 顯示FPS
        showFps(img)
        # 開啟視窗
        cv2.imshow('img',img)
        # 結束條件
        if cv2.waitKey(1) == ord('q'):
            break