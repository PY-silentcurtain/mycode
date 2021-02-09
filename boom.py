import pygame,sys
from pygame.sprite import Sprite
from pygame.sprite import Group
 
class Mysprite(Sprite):
    def __init__(self):
        super().__init__()
        self.mast_image = pygame.image.load('2233.jfif') #读取图像
        self.rect = self.mast_image.get_rect() #获取图像矩形参数
        self.frame_rect = self.rect.copy() #声明框架参数
        self.rect.x,self.rect.y = 400,300  #这里是我实验的动画坐标绘制,如果把这两个参数放在第12行之前,那么就会报错,显示子表面绘制超出了范围 .
        self.frame_rect.width /= 4
        self.frame_rect.height /= 4
        self.frame = 0
        #最后一个框架
        self.last_frame = (self.rect.width // self.frame_rect.width) * (self.rect.height // self.frame_rect.height) - 1
        #这里的值为15，我们的素材有16个，从0开始索引，最后一个值即为15，每行有x*y个框架。代入值可知4*4=16个框架
        self.old_frame = 1
        self.last_time = 0

    
    def update(self):
        self.current_time = pygame.time.get_ticks() #获取以毫秒为单位的时间
        rate = 100 #因为这个属性在别的地方不会有调用,所以这里我就写成了方法的局部变量
        #我们不希望他一股脑的播放完，我们设置隔100ms播放一次。也就是说100ms之后播放下一张图片。
        if self.current_time >= self.last_time + rate:
            self.frame += 1
            self.last_time = self.current_time
            #如果当前框架和最后一个框架重合，把他重新变成第一个框架，以此来完成循环播放。
            if self.frame > self.last_frame:
                self.frame = 0
 
        if self.old_frame != self.frame:
            #计算子表面框架在剪切时所处的位置.即大小
            self.frame_rect.x = (self.frame % 4) * self.frame_rect.width
            self.frame_rect.y = (self.frame // 4) * self.frame_rect.height
            self.old_frame = self.frame
 
        self.image = self.mast_image.subsurface(self.frame_rect) #这里就是在生成子表面

pygame.init() 
screen = pygame.display.set_mode((800,600))
color = (255,255,255)
mysprite = Mysprite()

print(mysprite.last_frame)#打印出最后一个子表面的位置。

group = Group()
group.add(mysprite)
tick = pygame.time.Clock()
 
mrunning = True
while mrunning:
    tick.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mrunning = False
 
    screen.fill(color)
    group.update()
    group.draw(screen)
    pygame.display.update()

pygame.quit()