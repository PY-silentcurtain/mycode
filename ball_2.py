import pygame,sys
#导入模块
pygame.init()

icon = pygame.image.load("PYG03-flower.png")
pygame.display.set_icon(icon)

size = width,height = 600,400   #窗口尺寸
speed = [1,1]
BLACK = 0,0,0
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption( "弹球")  #窗口名称
ball = pygame.image.load("PYG02-ball.gif")   #导入图片，这里我们可以挑选自己喜欢的图片
ballrect = ball.get_rect()
#这里是对我们导入的球进行一个矩形处理
fps = 300   #这里我们定一个统一的刷新速率，不了解的大家可以查一下“帧”是什么。
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():     #定义我们的关闭事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
        elif event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1)*int(speed[1]/abs(speed[1]))

        elif event.type == pygame.VIDEORESIZE:
            size = width,height = event.size[0],event.size[1]#0是宽，1是高
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)
            
            
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        
    screen.fill(BLACK)#每次循环填充背景色
    screen.blit(ball,ballrect)
    pygame.display.update()#绘制屏幕，也就是刷新
    fclock.tick(fps)