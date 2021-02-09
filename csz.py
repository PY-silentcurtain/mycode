import time
import random
target = random.randint(1,1000)
count = 0
while True:
    try:
        guess = eval(input("请输入你猜的数字（1到1000）："))

    except:
        print("输入有误，请重试，不计入猜测次数呦！")
        continue

    count = count + 1

    if guess > target:
        print("猜大了，再小一点")

    elif guess < target:
        print("猜小了，再大一点")

    else:
        print("恭喜你猜对了")

        break
print("本轮猜测的次数是：",count)
time.sleep(30)
    
    
        
