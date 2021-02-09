import pygame
import sys
import random
from pygame.locals import *  # 引入鼠标事件类型
import time

pygame.init()  # 初始化
window = pygame.display.set_mode([600, 400])  # 设定窗口

sur = pygame.Surface([600, 400])  # 绘制背景容器
clr = (0, 0, 255)
posAll = [[100, 150], [300, 150], [500, 150], [200, 300], [400, 300]]  # 六个位置
rad = 100
tick = 0  # 计数器
pos = posAll[0]  # 外面记录圆的位置

# 分数
score = 0  # 分数计数
pygame.font.init()  # 初始化文字
score_font = pygame.font.Font("msyh.ttc", 30)  # 设定字体和字号
score_sur = score_font.render(str(score), False, (255, 0, 0))  # 生成计数表面

# 鼠标
pygame.mouse.set_visible(False)  # !!隐藏鼠标
mpos = [300, 200]  # !!记录鼠标位置

times = 0  # 地鼠跳出的次数
times_max = 10  # 最多次数
tick_max = 30  # 地鼠每次跳多少帧
map = pygame.image.load("map_1.jpg")  # ！！读取图片
rat1 = pygame.image.load("rat1.png")# ！！读取地鼠图片
rat1 = pygame.transform.scale(rat1, (100, 100))
rat2 = pygame.image.load("rat2.png")  # ！！读取被砸地鼠图片
rat2 = pygame.transform.scale(rat2, (100, 100))
ham1 = pygame.image.load("cz1.png")  # ！！读取锤子图片
ham1 = pygame.transform.scale(ham1, (100, 100))
ham2 = pygame.image.load("cz2.png")  # ！！读取砸下锤子图片
ham2 = pygame.transform.scale(ham2, (100, 100))

gameover = 0 #！！结束计时
gameover_max = 100 #！！结束计时最大值，超过这个值就重新开始

mRunning = True
while mRunning : # 死循环确保窗口一直显示
    hamsur = ham1
    ratsur = rat1
    for event in pygame.event.get():
        pygame.time.delay(32)
        if event.type == pygame.QUIT :  # 如果单击关闭窗口，则退出
                mRunning = False 
        elif event.type == MOUSEBUTTONDOWN:  # 如果是鼠标按下事件
            hamsur = ham2  # ！！使用下落锤子
            mpos = pygame.mouse.get_pos()  # 获取鼠标位置
            dis = pygame.math.Vector2(mpos[0] - pos[0], mpos[1] - pos[1])  # 计算坐标差
            len = pygame.math.Vector2.length(dis)  # 计算距离
            if len < rad:
                tick = 1000  # 立即变换位置
                score = score + 1  # 计分增加
                ratsur = rat2  # ！！使用被砸地鼠
        elif event.type == MOUSEMOTION:  # 当鼠标移动的时候
            mpos = pygame.mouse.get_pos()  # 更新鼠标位置

    if times >= times_max:
        # 显示结束画面
        sur.fill((0, 0, 0))  # 结束时候仍然用黑色清空画面
        pygame.mouse.set_visible(True)
        end_font = pygame.font.Font("msyh.ttc", 48)  # ！！设定字体和字号
        end_sur = score_font.render(
            "你的分数是:{}/{}！".format(score, times_max), True, (255, 0, 0)
        )  # ！！生成计数表面
        sur.blit(end_sur, (100, 150))
        cd = int((gameover_max - gameover) / 10)
        cd_sur = score_font.render(
            "重新开始倒计时{}".format(cd), True, (255, 0, 0)
        )  # ！！生成计数表面
        sur.blit(cd_sur, (100, 200))  # 增加分数表面
        gameover = gameover + 1 #！！增加结束计时
    else:
        sur.blit(map, (0, 0))  # 添加背景图片
        score_sur = score_font.render(
            "分数:{}/{}！".format(score, times + 1), False, (255, 0, 0)
        )  # 重新生成分数文字表面
        sur.blit(score_sur, (200, 10))  # 增加分数表面
        if tick > tick_max:  # 每50次刷新变换一次
            times = times + 1  # 增加计次
            a = random.randint(0, 4)  # 随机0到4
            pos = posAll[a]  # 更新外部记录的圆的位置
            tick = 0  # 重置计数器
        else:  # 不刷新变换的时候
            tick = tick + 1  # 增加计数器
        if tick > 5:  # 开始几帧不显示地鼠
            sur.blit(ratsur, (pos[0] - 50, pos[1] - 70))  # 绘制地鼠
        sur.blit(hamsur, (mpos[0] - 50, mpos[1] - 100))  # 绘制锤头

    # 刷新画面
    window.blit(sur, (0, 0))
    pygame.display.flip()  # 刷新画面
    time.sleep(0.04)  # ！！保持画面一点时间

    # ！！重置游戏
    if gameover > gameover_max:
        pygame.mouse.set_visible(False)
        times = 0
        score = 0
        gameover = 0

pygame.quit()        