import sys
import random
import pygame
from pygame.locals import *
        
WIDTH, HEIGHT = 640, 480
BACKGROUND = (255, 255, 255)

# 按钮
def button(text, x, y, w, h, color, screen):
        pygame.draw.rect(screen, color, (x, y, w, h))
        font = pygame.font.Font('SIMYOU.ttf', 20)
        textRender = font.render(text, True, (0, 0, 0))
        textRect = textRender.get_rect()
        textRect.center = ((x+w/2), (y+h/2))        
        screen.blit(textRender, textRect)
     
# 标题
def title(text, screen, scale, color=(255, 0, 0)):
        font = pygame.font.Font('SIMYOU.ttf', WIDTH//(len(text)*2))
        textRender = font.render(text, True, color)
        textRect = textRender.get_rect()
        textRect.midtop = (WIDTH/scale[0], HEIGHT/scale[1])
        screen.blit(textRender, textRect)

        
# 生成随机的位置坐标
def get_random_pos():
        x, y = random.randint(20, 620), random.randint(20, 460)
        return x, y

# 点击喜欢按钮后显示的页面
def show_like_interface(text, screen, color=(255, 0, 0)):
        screen.fill(BACKGROUND)
        pygame.mouse.set_visible(True)
        font = pygame.font.Font('SIMYOU.ttf', WIDTH//(len(text)))
        textRender = font.render(text, True, color)
        textRect = textRender.get_rect()
        textRect.midtop = (WIDTH/2, HEIGHT/2)
        screen.blit(textRender, textRect)
        pygame.display.update()
        while True:
                for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
               
# 主函数
def main():
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('FROM一个喜欢你很久的小哥哥')
        clock = pygame.time.Clock()
        
        unlike_pos_x = 330
        unlike_pos_y = 250
        unlike_pos_width = 100
        unlike_pos_height = 50
        unlike_color = (0, 191, 255)
        like_pos_x = 180
        like_pos_y = 250
        like_pos_width = 100
        like_pos_height = 50
        like_color = (0, 191, 255)
        
        p_4 = pygame.image.load('play_4.png').convert_alpha ()
        p_4 = pygame.transform.scale(p_4, (100,100))
        
        
        #pygame.mixer.init()
        wavFileName = 'bad_guy.mp3'
        sndTrack = pygame.mixer.music.load(wavFileName)
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play(-1)
 
        mrunning = True
        while mrunning:
                screen.fill(BACKGROUND)
                img = pygame.image.load( 'bixin.jfif')
                img = pygame.transform.scale(img, (300,170))
                imgRect = img.get_rect()
                imgRect.midtop = int(WIDTH/1.3), HEIGHT//7
                screen.blit(img, imgRect)
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = pygame.mouse.get_pos()
                                if mouse_pos[0] < like_pos_x+like_pos_width+5 and mouse_pos[0] > like_pos_x-5 and\
                                        mouse_pos[1] < like_pos_y+like_pos_height+5 and mouse_pos[1] > like_pos_y-5:
                                        mrunning = False
                h,v = mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] < unlike_pos_x+unlike_pos_width+5 and mouse_pos[0] > unlike_pos_x-5 and\
                        mouse_pos[1] < unlike_pos_y+unlike_pos_height+5 and mouse_pos[1] > unlike_pos_y-5:
                        while True:
                                unlike_pos_x, unlike_pos_y = get_random_pos()
                                if mouse_pos[0] < unlike_pos_x+unlike_pos_width+5 and mouse_pos[0] > unlike_pos_x-5 and\
                                        mouse_pos[1] < unlike_pos_y+unlike_pos_height+5 and mouse_pos[1] > unlike_pos_y-5:
                                        continue
                                break
                                
                                
                pygame.mouse.set_visible(False)
                h -= p_4.get_width() / 2
                v -= p_4.get_height() / 2
                #用其他图形代替鼠标
                screen.blit(p_4, (h, v))
                
                title('小姐姐，我观察你很久了', screen, scale=[3, 8])
                title('做我女朋友好不好呀', screen, scale=[3, 4])
                button('好呀', like_pos_x, like_pos_y, like_pos_width, like_pos_height, like_color, screen)
                button('算了吧', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, unlike_color, screen)
                pygame.display.flip()
                pygame.display.update()
                clock.tick(60)
        show_like_interface('单身狗进化~恋爱狗！！！', screen, color=(255, 0, 0))
main()