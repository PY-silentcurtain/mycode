#鼠标交互
import pygame
from pygame.color import THECOLORS

N = [1,2,3,4,5]

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

def play_1():
    box = pygame.image.load("box1.png")
    box = pygame.transform.scale(box, (459, 600))#导入图片
    boxrect = box.get_rect()

    screen.blit(box,boxrect)
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

def xyy():
    i = 0
    while True:
        yield N[i]
        i+=1
        if i == 5:
            i = 0
f = xyy()  

wavFileName = 'ls_1.wav'
sndTrack = pygame.mixer.music.load(wavFileName)
pygame.mixer.music.set_volume(0.8)
#pygame.mixer.music.play()

#g = (x for x in range(5))
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    h = next(f)
                    
                    if h == 1:
                        pygame.mixer.music.play()
                        play_2()
                        
                    elif h == 2:
                        pygame.mixer.music.play()
                        play_3()
                        
                    elif h == 3:
                        pygame.mixer.music.play()
                        play_4()
                        
                    elif h == 4:
                        pygame.mixer.music.play()
                        play_5()
                        
                    elif h == 5:
                        pygame.mixer.music.play()
                        play_1()
                                     
pygame.quit()