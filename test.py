import pygame
import sys

# 初始化 Pygame
pygame.init()

# 設定視窗大小
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# 設定長方形的位置和大小
rect_x = 100
rect_y = 100
rect_width = 200
rect_height = 100

# 設定初始顏色和閃爍間隔
a_color = 0
b_color = 0
flash_interval = 500  # 毫秒

# 設定計時器初始值
flash_timer = pygame.time.get_ticks()
rect_color = 254
flag = 0
# 運行主迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 檢查計時器是否超過閃爍間隔
    # current_time = pygame.time.get_ticks()
    # if current_time - flash_timer >= flash_interval:
    #     # 改變顏色
    #     if rect_color == (255, 0, 0):
    #         rect_color = (0, 0, 255)
    #     else:
    #         rect_color = (255, 0, 0)
        
    #     # 重設計時器
    #     flash_timer = current_time
    
    if rect_color == 255 and flag != -1: 
        flag = 0
    if rect_color == 1:
        flag = 1

    if flag == 0 and flag != -1:
        rect_color = rect_color - 0.5
    if flag == 1 and flag != -1:
        rect_color = rect_color + 0.5

    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > 100 and mouse_pos[0] <200:
        flag = -1
        rect_color,a_color,b_color = 255,255,255

    # 清除畫面
    screen.fill((0, 0, 0))

    # 繪製長方形
    rect = pygame.draw.rect(screen, (rect_color,a_color,b_color), (rect_x, rect_y, rect_width, rect_height), 3)  # 最後一個參數是外框寬度

    # 更新畫面
    pygame.display.flip()
