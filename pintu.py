import random
 
import pygame
 
# 初始化
pygame.init()
# 窗口标题
pygame.display.set_caption('拼图游戏')
# 窗口大小
s = pygame.display.set_mode((1200, 600))
 
#绘图地图
imgMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
 
#判断胜利的地图
winMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
 
#游戏的单击事件
def click(x, y, map):
    if y - 1 >= 0 and map[y - 1][x] == 8:
        map[y][x], map[y - 1][x] = map[y - 1][x], map[y][x]
    elif y + 1 <= 2 and map[y + 1][x] == 8:
        map[y][x], map[y + 1][x] = map[y + 1][x], map[y][x]
    elif x - 1 >= 0 and map[y][x - 1] == 8:
        map[y][x], map[y][x - 1] = map[y][x - 1], map[y][x]
    elif x + 1 <= 2 and map[y][x + 1] == 8:
        map[y][x], map[y][x + 1] = map[y][x + 1], map[y][x]
 
#打乱地图
def randMap(map):
    for i in range(1000):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        click(x, y, map)
 
# 加载图片
img = pygame.image.load('play_4.jpg')
#随机地图
randMap(imgMap)
#游戏主循环
mRunning = True
while mRunning :  # 死循环确保窗口一直显示
    for event in pygame.event.get():
        pygame.time.delay(32)
        if event.type == pygame.QUIT :  # 如果单击关闭窗口，则退出
                mRunning = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:      #鼠标单击事件
            if pygame.mouse.get_pressed() == (1, 0, 0):     #鼠标左键按下
                mx, my = pygame.mouse.get_pos()     #获得当前鼠标坐标
                if mx<498 and my <498:      #判断鼠标是否在操作范围内
                    x=int(mx/166)       #计算鼠标点到了哪个图块
                    y=int(my/166)
                    click(x,y,imgMap)   #调用单击事件
                    if imgMap==winMap:  #如果当前地图情况和胜利情况相同,就print胜利
                        print("胜利了！")
    #背景色填充成绿色
    s.fill((0,255,0))
    #绘图
    for y in range(3):
        for x in range(3):
            i = imgMap[y][x]
            if i == 8:      #8号图块不用绘制
                continue
            dx = (i % 3) * 166      #计算绘图偏移量
            dy = (int(i / 3)) * 166
            s.blit(img, (x * 166, y * 166), (dx, dy, 166, 166))
    # 画参考图片
    s.blit(img, (600, 0))
    # 刷新界面
    pygame.display.flip()
pygame.quit()