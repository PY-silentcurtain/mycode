from PIL import Image
img = Image.open("hyrz.jfif")   # 读取图片
img = img.convert("L")   # 转化为黑白图片
img.save("444.jpg")   # 存储图片
img.show()