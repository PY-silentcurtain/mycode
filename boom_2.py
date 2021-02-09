import random 
def keyboard_input(string):
    from pynput.keyboard import Key,Controller
    #导入相应的库
    keyboard = Controller() #开始控制键盘
    keyboard.type(string) #键盘输入string
    return None
 
def mouse_click():#点击发送消息
    from pynput.mouse import Button,Controller
    #导入相应的库
    mouse = Controller() #开始控制鼠标
    mouse.press(Button.left)  # 按住鼠标左键
    mouse.release(Button.left)  # 放开鼠标左键
    return None
 

    
def main(number,string):#参数分别表示你要发多少条信息和发送的内容
    import time #导入time
    time.sleep(5) # 此时暂停5s，方便你打开聊天窗，并把鼠标停放在发送按钮上
    for i in range(number):#用循环来控制你发送多少条消息
        string = random.choice(["你好我是龙王","信息轰炸机","demo"])
        keyboard_input(string)
        mouse_click()
        time.sleep(2)
    
if __name__ == '__main__':
    main(50,string)