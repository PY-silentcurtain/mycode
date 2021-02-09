#键盘交互
import pygame
from pygame.color import THECOLORS

# 初始化
pygame.init()

# 生成一个窗口
screen = pygame.display.set_mode([800,600])
icon = pygame.image.load("PYG03-flower.png")
pygame.display.set_icon(icon)

pygame.display.set_caption( "快乐源泉小瓶子（依次按qwer填满它）")  
# 将白色铺满整个窗口
screen.fill(THECOLORS['white'])

box = pygame.image.load("box1.png")
box = pygame.transform.scale(box, (459, 600))#导入图片
boxrect = box.get_rect()

screen.blit(box,boxrect,)
pygame.display.flip()

def play_2():
    box = pygame.image.load("box2.png")
    box = pygame.transform.scale(box, (459, 600))#导入图片
    boxrect = box.get_rect()

    screen.blit(box,boxrect)
    pygame.display.flip()
    
def play_3():
    box = pygame.image.load("box3.png")
    box = pygame.transform.scale(box, (459, 600))#导入图片
    boxrect = box.get_rect()

    screen.blit(box,boxrect)
    pygame.display.flip()
    
def play_4():
    box = pygame.image.load("box4.png")
    box = pygame.transform.scale(box, (459, 600))#导入图片
    boxrect = box.get_rect()

    screen.blit(box,boxrect)
    pygame.display.flip()
    
def play_5():
    box = pygame.image.load("box5.png")
    box = pygame.transform.scale(box, (459, 600))#导入图片
    boxrect = box.get_rect()

    screen.blit(box,boxrect)
    pygame.display.flip()
 

wavFileName = 'ls_1.wav'
sndTrack = pygame.mixer.music.load(wavFileName)
pygame.mixer.music.set_volume(0.8)
#pygame.mixer.music.play()

mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.mixer.music.play()
                play_2()
            elif event.key == pygame.K_w:
                pygame.mixer.music.play()
                play_3()
            elif event.key == pygame.K_e:
                pygame.mixer.music.play()
                play_4()
            elif event.key == pygame.K_r:
                pygame.mixer.music.play()
                play_5()
        
pygame.quit()