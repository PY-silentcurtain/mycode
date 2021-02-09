from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))#chr()中65-90是英文字母
    #return chr(random.randint(48, 57))
    #这一部分被我们注释掉了，如果我们使用这部分，出现的验证码将是4个随机数字
    #chr()中48-57为阿拉伯数字0-9
# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 进行模糊处理:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
image.show()#会启用默认的图片查看器，打开查看图片
#程序去掉最后一步，也会运行，但是需要我们手动查找生成的图片
#一般和运行的脚本处于同一目录下