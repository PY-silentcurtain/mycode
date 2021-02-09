import pygame
from sys import exit
from pygame.color import THECOLORS

pygame.init()
m = 1000
n = 600
size = width,height = m,n#窗口大小
screen = pygame.display.set_mode(size)#绘制屏幕

p_1 = pygame.image.load('play_1.png')#导入图片素材
p_1 = pygame.transform.scale(p_1, (165,55))
p_1rect = p_1.get_rect()
x,y = 400,300

p_2 = pygame.image.load('play_2.png')#导入图片素材
p_2 = pygame.transform.scale(p_2, (165,55))
p_2rect = p_2.get_rect()
h,z = 400,300

nRunning = True
mRunning = True
while mRunning :  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT :  # 如果单击关闭窗口，则退出
            mRunning = False    
         
        if event.type == pygame.MOUSEMOTION:
            v,b = pygame.mouse.get_pos()
            if x<v<x+165 and y<b<y+55:
                nRunning = False 
            else :
                nRunning = True
              
        if event.type ==pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and x<v<x+165 and y<b<y+55:
                print('6')
                #接上你需要的功能，比如 游戏开始
       
    screen.fill(THECOLORS['white']) 
    
    if nRunning == True:
        screen.blit(p_1,(x,y))
    elif nRunning == False:
        screen.blit(p_2,(h,z))
    
    pygame.display.flip()
            
pygame.quit()