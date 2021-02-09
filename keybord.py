import os
import sys
import threading
import time
 
from pynput import keyboard
from pynput.keyboard import Controller, Key, Listener
 
# 每隔0.5秒 清空列表
def doWaiting():
    while True:
        time.sleep(0.5)
        all_key.clear()
 
 
# 键盘按压
def on_press(key):
    pass
 
def on_release(key):
    #print("已经释放:", format(key))
    all_key.append(str(key))
    print(all_key)
    # if keyboard.Key.ctrl_l in all_key and keyboard.Key.f5 in all_key:
    #     print('what is your problem?')
 
    if 'Key.ctrl_l' in all_key and "'c'"in all_key:
        print('复制快捷键')
 
    if 'Key.ctrl_l' in all_key and "'v'"in all_key:
        print('粘贴快捷键')
 
    if key == Key.esc:
        # 停止监听
        return False
 
 
def start_listen():
    with Listener(on_press=None, on_release=on_release) as listener:
        listener.join()
 
 
if __name__ == '__main__':
    # 开始监听,按esc退出监听
    all_key = []
 
    t = threading.Thread(target=doWaiting)
    t.setDaemon(True)
    t.start()
 
    start_listen()