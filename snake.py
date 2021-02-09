#原代码
import pygame
from sys import exit
import random
from pygame.color import THECOLORS

class Point():
    row = 0
    clo = 0

    def __init__(self, row, clo):
        self.row = row
        self.clo = clo

    def copy(self):
        return Point(row=self.row, clo=self.clo)


# 初始化
pygame.init()
width = 800
hight = 400

ROW = 30
CLO = 40

direct = 'left'
window = pygame.display.set_mode((width, hight))
pygame.display.set_caption('贪吃蛇游戏')

# 蛇头坐标定在中间
head = Point(row=int(ROW / 2), clo=int(CLO / 2))
# 初始化蛇身的元素数量
snake = [
    Point(row=head.row, clo=head.clo + 1),
    Point(row=head.row, clo=head.clo + 2),
    Point(row=head.row, clo=head.clo + 3)
]


# 生成食物并且不让食物生成在蛇的身体里面
def gen_food():
    while True:
        position = Point(row=random.randint(0, ROW - 1), clo=random.randint(0, CLO - 1))
        is_coll = False
        if head.row == position.row and head.clo == position.clo:
            is_coll = True
        for body in snake:
            if body.row == position.row and body.clo == position.clo:
                is_coll = True
                break
        if not is_coll:
            break
    return position


# 定义坐标
# 蛇头颜色可以自定义
head_color = (0, 158, 128)

# 食物坐标
snakeFood = gen_food()
# 食物颜色
snakeFood_color = (255, 255, 0)


snake_color = (200, 147, 158)


# 需要执行很多步画图操作 所以定义一个函数
def rect(point, color):
    # 定位 画图需要left和top
    left = point.clo * width / CLO
    top = point.row * hight / ROW
    # 将方块涂色
    pygame.draw.rect(window, color, (left, top, width / CLO, hight / ROW))


quit = True
# 设置帧频率
clock = pygame.time.Clock()
while quit:
    # 处理帧频 锁帧，这里决定蛇的速度快慢
    clock.tick(5)
    # pygame.event.get()获取当前事件的队列 可以同时发生很多事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            # 这里小细节蛇不可以直接左右上下 要判断当前是在什么状态下前行
            if event.key == 273 or event.key == 119:
                if direct == 'left' or direct == 'right':
                    direct = 'top'
            if event.key == 274 or event.key == 115:
                if direct == 'left' or direct == 'right':
                    direct = 'bottom'
            if event.key == 276 or event.key == 97:
                if direct == 'top' or direct == 'bottom':
                    direct = 'left'
            if event.key == 275 or event.key == 100:
                if direct == 'top' or direct == 'bottom':
                    direct = 'right'
    # 吃东西
    eat = (head.row == snakeFood.row and head.clo == snakeFood.clo)

    # 处理蛇的身子
    # 1.把原来的头插入到snake的头上
    # 2.把最后一个snake删掉
    if eat:
        snakeFood = Point(row=random.randint(0, ROW - 1), clo=random.randint(0, CLO - 1))
    snake.insert(0, head.copy())
    if not eat:
        snake.pop()

    # 移动一下
    if direct == 'left':
        head.clo -= 1
    if direct == 'right':
        head.clo += 1
    if direct == 'top':
        head.row -= 1
    if direct == 'bottom':
        head.row += 1
    dead = False
    if head.clo < 0 or head.row < 0 or head.clo >= CLO or head.row >= ROW:
        dead = True
    for body in snake:
        if head.clo == body.clo and head.row == body.row:
            dead = True
            break
    if dead:
        print('Game Over')
        quit = False
    # 背景画图
    #pygame.draw.rect(window, (245, 135, 155), (0, 0, width, hight))
    window.fill(THECOLORS['white'])
    # 蛇头
    rect(head, head_color)
    # 绘制食物
    rect(snakeFood, snakeFood_color)
    # 绘制蛇的身子
    for body in snake:
        rect(body, snake_color)

    # 交还控制权
    pygame.display.flip()

pygame.quit()