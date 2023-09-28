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

zeroPoint = [0,0]

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
            body_points = []            
            # 印出點的數字
            for i,lm in enumerate(body_landmarks.landmark):
                if i == 0:
                    zeroPoint = [srceen_width - int(lm.x*srceen_width),int(lm.y*srceen_height)]
                xPos = int(lm.x*srceen_width)
                yPos = int(lm.y*srceen_height)   
                cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),2)               
        img = cv2.flip(img,1)
        cv2.putText(img,str(zeroPoint), (30,170),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) # 印出文字
        
        # 顯示FPS
        showFps(img)
        # 開啟視窗
        cv2.imshow('img',img)
        # 結束條件
        if cv2.waitKey(1) == ord('q'):
            break