import pygame
from pygame.locals import *

WINDOW_W, WINDOW_H = 640, 480
pygame.init()
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.DOUBLEBUF, 32)
pygame.display.set_caption("小球弹跳")
FPS = 60
g = 9.8 * 100
is_run = True  # 是否运行
clock = pygame.time.Clock()

x, y = WINDOW_W / 2, 10
vx, vy = 0, 0

def my_event():
    global vx,vy,is_run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if is_run:
        vy += g * 1/FPS

if __name__ == '__main__':
    while True:
        # 侦听事件
        my_event()

        # 是否暂停
        if not is_run:
            continue

        # 计算小球
        x += vx * 1 / FPS
        y += vy * 1 / FPS
        if y >= WINDOW_H - 10:
            vy = -vy
        if x >= WINDOW_W:
            x-=WINDOW_W
        if x < 0:
            x+=WINDOW_W

        # 将背景图画上去
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 10)

        # 刷新画面
        pygame.display.update()
        time_passed = clock.tick(FPS)
