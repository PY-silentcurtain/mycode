from turtle import *
from random import *

def ground():
    hideturtle()#隐藏画笔的形状
    speed(100)#绘制速度
    for i in range(400):
        pensize(randint(5,10))
        x=randint(-400,350)
        y=randint(-280,-1)
        r=-y/280
        g=-y/280
        b=-y/280
        pencolor(r,g,b)
        penup()
        goto(x,y)
        pendown()
        forward(randint(40,100))

def snow():
    hideturtle()
    speed(100)
    pensize(2)
    #我们用for循环绘制100朵雪花，且颜色随机
    for i in range(100):
        r=random()
        g=random()
        b=random()
        pencolor(r,g,b)#不同的色彩
        penup()
        #我们用randint来换取-350到350之间的随机数
        setx(randint(-350,350))#X坐标轴范围
        sety(randint(1,270))  #y轴坐标范围
        pendown()
        dens=randint(8,12)
        snowsize=randint(10,14)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360/dens)

def main():
    setup(800, 600, 0, 0)
    tracer(False)
    '''这里关闭了绘制过程的动画，改为True会显示一步步的绘制效果，
    但是绘制过程太漫长了，我们选择直接呈现效果图'''
    bgcolor("black")#背景色我们选择黑色
    snow()
    ground()
    mainloop()
main()