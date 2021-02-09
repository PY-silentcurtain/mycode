#混合交互
import pygame
import sys
import time
pygame.init()
m = 1000
n = 600
size = width,height = m,n#窗口大小
screen = pygame.display.set_mode(size)#绘制屏幕
color = 255,255,255
ball = pygame.image.load('ball.png')#导入小球图片
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
speed =[5,5]
state_time = pygame.time.Clock()

#right
rect = pygame.image.load('rect_1.png')#导入
rect = pygame.transform.scale(rect, (30, 200))
rectarea = rect.get_rect()
x,y=m-30,n-200

#left
box = pygame.image.load('rect_2.png')#导入
box = pygame.transform.scale(box, (30, 200))
boxarea = box.get_rect()
h,z=0,n-200
move_h=move_z=0

mRunning = True
while mRunning :  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT :  # 如果单击关闭窗口，则退出
            mRunning = False 
        #键盘响应部分    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_z = -10
            elif event.key == pygame.K_s:
                move_z = 10
            
        elif event.type == pygame.MOUSEMOTION:  
            v,b = pygame.mouse.get_pos()
            y = b-100
            
        elif event.type == pygame.KEYUP:
            move_z = 0
        
    z += move_z
    state_time.tick(50)
    ballrect = ballrect.move(speed)
    screen.fill(color)#每次循环填充背景色
    screen.blit(ball,ballrect)
    screen.blit(rect,(x,y))
    screen.blit(box,(h,z))
    pygame.display.flip()
    #小球碰壁反弹处理
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
     
    elif ballrect.right==m-30 and ballrect.top+50>=y and ballrect.top<=y+200 :
        speed[0] = -speed[0]
        
    
    elif ballrect.left==30 and ballrect.top+50>=z and ballrect.top<=z+200 :
        speed[0] = -speed[0]    
      
    elif ballrect.left<0 or ballrect.left>m:
        mRunning = False
            
pygame.quit()