# 导入模块
import pygame
from pygame.locals import *
from sys import exit

# 初始化部分
pygame.init()

# 设置游戏窗口
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("My Game Window")
background = pygame.image.load("background_640x480.jpg").convert()

# 坦克精灵类
tank_image = pygame.image.load('tank.png').convert_alpha()
cannon1_image = pygame.image.load('cannon_1.png').convert_alpha()
cannon2_image = pygame.image.load('cannon_2.png').convert_alpha()

class HeroTank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tank_image = tank_image
        self.cannon1_image = cannon1_image
        self.cannon2_image = cannon2_image
        self.tank_rect = self.tank_image.get_rect()
        self.cannon1_rect = self.cannon1_image.get_rect()
        self.cannon2_rect = self.cannon2_image.get_rect()
        self.speed = 8

    def moveLeft(self):
        if self.tank_rect.left > 0:
            self.tank_rect.x -= self.speed
        self.rotate(270)

    def moveRight(self):
        if self.tank_rect.right < 640:
            self.tank_rect.x += self.speed
        self.rotate(90)

    def moveUp(self):
        if self.tank_rect.top > 0:
            self.tank_rect.y -= self.speed
        self.rotate(180)

    def moveDown(self):
        if self.tank_rect.bottom < 480:
            self.tank_rect.y += self.speed
        self.rotate(0)

    def rotate(self, angle):
        # 选择机身 参数(对象，角度)
        self.tank_image = pygame.transform.rotate(tank_image, angle)
        self.tank_rect = self.tank_image.get_rect(center=self.tank_rect.center)
        # 旋转炮筒
        self.cannon1_image = pygame.transform.rotate(cannon1_image, angle)
        self.cannon1_rect = self.cannon1_image.get_rect(center=self.cannon1_rect.center)
        
        self.cannon2_image = pygame.transform.rotate(cannon2_image, angle)
        self.cannon2_rect = self.cannon2_image.get_rect(center=self.cannon2_rect.center)

    def display(self, screen):
        screen.blit(self.tank_image, self.tank_rect)
        self.cannon1_rect.center = self.tank_rect.center
        screen.blit(self.cannon1_image, self.cannon1_rect)
        
    def display_1(self, screen):
        screen.blit(self.tank_image, self.tank_rect)
        self.cannon2_rect.center = self.tank_rect.center
        screen.blit(self.cannon2_image, self.cannon2_rect)

my_tank = HeroTank()
framerate = pygame.time.Clock()

nrunning = True
mrunning = True
while mrunning:
    framerate .tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            mrunning = False
    key_press = pygame.key.get_pressed()
    if key_press[K_w]:
        my_tank.moveUp()
    elif key_press[K_s]:
        my_tank.moveDown()
    elif key_press[K_a]:
        my_tank.moveLeft()
    elif key_press[K_d]:
        my_tank.moveRight()
    
    screen.blit(background, (0, 0))

    my_tank.display(screen)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            nrunning = False
        if event.key == pygame.K_e:
            nrunning = True

    if nrunning:
        my_tank.display(screen)
    else :
        my_tank.display_1(screen)
    
    pygame.display.update()
    
pygame.quit()